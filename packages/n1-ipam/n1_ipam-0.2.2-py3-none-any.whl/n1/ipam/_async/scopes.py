import dataclasses
import logging
from ipaddress import IPv4Address, IPv4Network
from typing import Any, NamedTuple, overload

import conscia.infoblox.infoblox_sdk.model as ib_m
import conscia.tasklog as tasklog
from conscia.infoblox.infoblox_sdk.consts import DEFAULT_VIEW
from conscia.infoblox.infoblox_sdk.extattr import ExtAttrCollection
from conscia.infoblox.infoblox_sdk.model import (
    DHCPMember,
    Members,
    OptionDHCPLeaseTime,
    OptionRouter,
    Options,
    SearchExtAttr,
)
from conscia.infoblox.infoblox_sdk.types import NextAvailableIPv4Address, NextAvailableNetwork
from tabulate import SEPARATING_LINE, tabulate
from typing_extensions import override

import n1.ipam.extattr as ea
import n1.ipam.models as m
from n1.ipam import ipcalc
from n1.ipam._api import AsyncApi
from n1.ipam.scopes_base import (
    ColWOffset,
    NameSiteid,
    ObjWOffset,
    VerifyLog,
    format_extra,
)
from n1.ipam.scopes_base import DHCPRange as DHCPRange

log = logging.getLogger(__name__)


class UnknownFixedAddr(ib_m.FixedAddress):
    extattrs: ExtAttrCollection


@dataclasses.dataclass(slots=True, kw_only=True)
class AsyncAddrScope:
    nid: ea.NID
    net: IPv4Network
    comment: str | None
    skip: int

    @property
    def name(self) -> str:
        return self.nid.value

    @overload
    def calc_addr(self, addr: int | IPv4Address) -> IPv4Address:
        ...

    @overload
    def calc_addr(self, addr: None) -> NextAvailableIPv4Address:
        ...

    def calc_addr(self, addr: int | IPv4Address | None) -> IPv4Address | NextAvailableIPv4Address:
        match addr:
            case IPv4Address():
                return addr
            case int():
                return ipcalc.offset_addr(self.net, addr + 1 + self.skip)
            case None:
                return NextAvailableIPv4Address(self.net)

    def calc_offset(self, addr: IPv4Address) -> int:
        return ipcalc.addr_offset(self.net, addr) - 1 - self.skip

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.startswith("t"):
            indent_str = __format_spec[1:]
            indent = int(indent_str) if len(indent_str) > 0 else 0
            ind = " " * (indent * 4)
            return f"""
{ind}{self.comment}
{ind}{self.nid}
{ind}{self.net}
{ind}{self.skip}"""

        return super().__format__(__format_spec)

    async def _get_unknowns(self, api: AsyncApi) -> list[UnknownFixedAddr]:
        return await api.get_unknown_addrs(self.net, UnknownFixedAddr)


@dataclasses.dataclass(slots=True, kw_only=True)
class AsyncNetScope:
    nid: ea.NID
    net: IPv4Network
    prefix: int
    comment: str | None
    gw: int | None
    members: list[DHCPMember]
    dhcp: DHCPRange | None

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.startswith("t"):
            indent_str = __format_spec[1:]
            indent = int(indent_str) if len(indent_str) > 0 else 0
            ind = " " * (indent * 4)
            return f"""
{ind}{self.comment}
{ind}{self.nid}
{ind}{self.net} -> {self.prefix}"""

        return super().__format__(__format_spec)

    @property
    def name(self) -> str:
        return self.nid.value

    def get_options(self, net: IPv4Network | None = None) -> list[Options]:
        options: list[Options] = []

        if isinstance(self.dhcp, DHCPRange):
            options.append(OptionDHCPLeaseTime(value=self.dhcp.lease))

        if isinstance(net, IPv4Network) and self.gw is not None:
            options.append(OptionRouter(value=net.network_address + self.gw))

        return options

    def get_members(self) -> list[Members]:
        return list(self.members)

    @overload
    def calc_net(self, net: None) -> NextAvailableNetwork:
        ...

    @overload
    def calc_net(self, net: int | IPv4Network) -> IPv4Network:
        ...

    def calc_net(self, net: int | IPv4Network | None) -> IPv4Network | NextAvailableNetwork:
        match net:
            case IPv4Network():
                return net
            case int() as offset:
                return ipcalc.offset_net(self.net, offset, self.prefix)
            case None:
                return NextAvailableNetwork(network=self.net, cidr=self.prefix, view=DEFAULT_VIEW)

    def calc_offset(self, net: IPv4Network) -> int:
        return ipcalc.net_offset(self.net, net)

    async def get_unknown_net(self, api: AsyncApi, net: IPv4Network | int) -> ib_m.Network:
        net = self.calc_net(net)
        return await api.get_net(network_container=self.net, network=net, return_cls=ib_m.Network)

    async def get_unknown_nets(self, api: AsyncApi) -> list[ib_m.Network]:
        return await api.get_unknown_nets(self.net, return_cls=ib_m.Network)

    async def get_unknown_ranges(self, api: AsyncApi) -> list[ib_m.Range]:
        return await api.get_unknown_ranges(self.nid, return_cls=ib_m.Range)

    async def _get_range[
        T: ib_m.Range
    ](self, api: AsyncApi, siteid: ea.SiteID, network: IPv4Network, return_cls: type[T]) -> T:
        return await api.get_range(self.nid, siteid, network=network, return_cls=return_cls)

    async def _try_get_range[
        T: ib_m.Range
    ](self, api: AsyncApi, siteid: ea.SiteID, network: IPv4Network, return_cls: type[T]) -> T | None:
        try:
            return await self._get_range(api, siteid, network, return_cls)
        except Exception:
            return None

    async def _get_net[
        T: ib_m.Network
    ](self, api: AsyncApi, oid: ea.SiteID | int | IPv4Network, return_cls: type[T]) -> T:
        match oid:
            case ea.SiteID():
                return await api.get_net(
                    oid,
                    network_container=self.net,
                    return_cls=return_cls,
                )
            case _:
                return await api.get_net(
                    network_container=self.net,
                    network=self.calc_net(oid),
                    return_cls=return_cls,
                )


class MPLSGroups(NamedTuple):
    registered: list[m.MPLSRegGroup]
    assigned: list[m.MPLSGroup]
    free: list[IPv4Network]


class MPLSNets(NamedTuple):
    registered: list[m.MPLSRegNet]
    assigned: list[m.MPLSNet]
    free: list[IPv4Network]


class MPLSRanges(NamedTuple):
    registered: list[m.MPLSRegRange]
    assigned: list[m.MPLSRange]


@dataclasses.dataclass(slots=True, kw_only=True)
class AsyncMPLSScope(AsyncNetScope):
    # region Calculations
    @override
    def calc_offset(self, net: IPv4Network | m.MPLSGroup | m.MPLSRegGroup | m.MPLSNet | m.MPLSRegNet) -> int:
        match net:
            case IPv4Network():
                return ipcalc.net_offset(self.net, net)
            case m.MPLSNet() | m.MPLSRegNet():
                return ipcalc.net_offset(self.net, net.network)
            case m.MPLSGroup() | m.MPLSRegGroup():
                return ipcalc.net_offset(self.net, net.net.network)

    # endregion

    # region Prepare

    def prepare_reg_range(self, net: IPv4Network | int) -> m.NewMPLSRegRange:
        if self.dhcp is None:
            raise Exception("not dhcp")
        net = self.calc_net(net)
        return m.NewMPLSRegRange(
            start_addr=self.dhcp.calc_start_addr(net),
            end_addr=self.dhcp.calc_end_addr(net),
            server_association_type=self.dhcp.server_association_type,
            failover_association=self.dhcp.failover_association,
            extattrs=m.MPLSRegRangeAttrs(),
        )

    def prepare_range(self, net: IPv4Network | int, info: m.SiteInfo | m.SiteInfoAttrs) -> m.NewMPLSRange:
        if self.dhcp is None:
            raise Exception("not dhcp")
        return self.prepare_reg_range(net).assign(info)

    def prepare_reg_net(self, tmpl: m.MPLSTmpl) -> m.NewMPLSRegNet:
        network = self.calc_net(tmpl.net)

        return m.NewMPLSRegNet(
            network=network,
            options=self.get_options(network),
            members=self.get_members(),
            extattrs=m.MPLSRegNetAttrs(kreds=tmpl.kreds, inst=tmpl.inst),
        )

    def prepare_net(self, tmpl: m.MPLSTmpl, info: m.SiteInfo | m.SiteInfoAttrs) -> m.NewMPLSNet:
        return self.prepare_reg_net(tmpl).assign(info)

    def prepare_reg_gnet(self, tmpl: m.MPLSTmpl) -> m.NewMPLSRegGroup:
        return m.NewMPLSRegGroup(
            net=self.prepare_reg_net(tmpl),
            dhcp=None if self.dhcp is None else self.prepare_reg_range(tmpl.net),
        )

    def prepare_gnet(self, tmpl: m.MPLSTmpl, info: m.SiteInfo | m.SiteInfoAttrs) -> m.NewMPLSGroup:
        return self.prepare_reg_gnet(tmpl).assign(info)

    # endregion

    # region Internal Create Update Delete
    @overload
    async def _create(self, api: AsyncApi, gnet: m.NewMPLSRegGroup) -> m.MPLSRegGroup:
        ...

    @overload
    async def _create(self, api: AsyncApi, gnet: m.NewMPLSGroup) -> m.MPLSGroup:
        ...

    async def _create(self, api: AsyncApi, gnet: m.NewMPLSGroup | m.NewMPLSRegGroup) -> m.MPLSGroup | m.MPLSRegGroup:
        log.info(f"Creating {self.name} {gnet}")

        if isinstance(gnet, m.NewMPLSGroup):
            return m.MPLSGroup(
                net=await api.create(gnet.net),
                dhcp=None if gnet.dhcp is None else await api.create(gnet.dhcp),
            )

        return m.MPLSRegGroup(
            net=await api.create(gnet.net),
            dhcp=None if gnet.dhcp is None else await api.create(gnet.dhcp),
        )

    @overload
    async def _update(self, api: AsyncApi, gnet: m.MPLSGroup) -> m.MPLSGroup:
        ...

    @overload
    async def _update(self, api: AsyncApi, gnet: m.MPLSRegGroup) -> m.MPLSRegGroup:
        ...

    async def _update(self, api: AsyncApi, gnet: m.MPLSGroup | m.MPLSRegGroup) -> m.MPLSGroup | m.MPLSRegGroup:
        if isinstance(gnet, m.MPLSGroup):
            return m.MPLSGroup(
                net=await api.update(gnet.net),
                dhcp=None if gnet.dhcp is None else await api.update(gnet.dhcp),
            )
        return m.MPLSRegGroup(
            net=await api.update(gnet.net),
            dhcp=None if gnet.dhcp is None else await api.update(gnet.dhcp),
        )

    async def _delete(self, api: AsyncApi, gnet: m.MPLSRegGroup | m.MPLSGroup) -> None:
        if gnet.dhcp is not None:
            await api.delete(gnet.dhcp)
        await api.delete(gnet.net)

    # endregion

    # region Group

    async def get_gnet(self, api: AsyncApi, oid: ea.SiteID | int | IPv4Network) -> m.MPLSGroup:
        net = await self._get_net(api, oid, m.MPLSNet)
        dhcp = await self._try_get_range(api, net.extattrs.siteid, net.network, m.MPLSRange)
        return m.MPLSGroup(net=net, dhcp=dhcp)

    async def try_get_gnet(self, api: AsyncApi, oid: ea.SiteID | int | IPv4Network) -> m.MPLSGroup | None:
        try:
            return await self.get_gnet(api, oid)
        except Exception:
            return None

    async def get_gnets(self, api: AsyncApi) -> list[m.MPLSGroup]:
        nets = await self.get_nets(api)
        ranges = await self.get_ranges(api)
        ran_dct: dict[IPv4Network, m.MPLSRange] = {n.network: n for n in ranges}

        return [m.MPLSGroup(net=net, dhcp=ran_dct.get(net.network, None)) for net in nets]

    async def get_reg_gnet(self, api: AsyncApi, oid: int | IPv4Network) -> m.MPLSRegGroup:
        network = self.calc_net(oid)
        return m.MPLSRegGroup(
            net=await api.get_net(network_container=self.net, network=network, return_cls=m.MPLSRegNet),
            dhcp=(
                None if self.dhcp is None else await api.get_range(self.nid, network=network, return_cls=m.MPLSRegRange)
            ),
        )

    async def try_get_reg_gnet(self, api: AsyncApi, oid: int | IPv4Network) -> m.MPLSRegGroup | None:
        try:
            return await self.get_reg_gnet(api, oid)
        except Exception:
            return None

    async def get_reg_gnets(self, api: AsyncApi) -> list[m.MPLSRegGroup]:
        nets = await self.get_reg_nets(api)

        ranges = await api.get_ranges(
            self.nid,
            ea.SiteID.is_not_null(),
            return_cls=m.MPLSRegRange,
        )
        ran_dct: dict[IPv4Network, m.MPLSRegRange] = {n.network: n for n in ranges}

        return [m.MPLSRegGroup(net=net, dhcp=ran_dct.get(net.network, None)) for net in nets]

    async def get_all_gnets(self, api: AsyncApi) -> MPLSGroups:
        registered_nets: list[m.MPLSRegGroup] = []
        assigned_nets: list[m.MPLSGroup] = []
        nets = await api.get_nets(network_container=self.net, return_cls=m.MPLSRegNet)
        ranges = await api.get_ranges(self.nid, return_cls=m.MPLSRegRange)
        for net in nets:
            for r in ranges:
                if r.network == net.network:
                    group = m.MPLSRegGroup(net=net, dhcp=r)
                    break
            else:
                group = m.MPLSRegGroup(net=net, dhcp=None)

            try:
                assigned_nets.append(group.as_obj())
            except Exception:
                registered_nets.append(group)

        free_nets = set(self.net.subnets(new_prefix=self.prefix)).difference(n.network for n in nets)
        return MPLSGroups(
            registered=registered_nets,
            assigned=assigned_nets,
            free=list(free_nets),
        )

    async def lookup_reg_gnet(
        self, api: AsyncApi, oid: int | IPv4Network | m.MPLSRegGroup | m.MPLSRegNet
    ) -> m.MPLSRegGroup:
        match oid:
            case m.MPLSRegGroup():
                return oid
            case m.MPLSRegNet():
                return await self.get_reg_gnet(api, oid.network)
            case _:
                return await self.get_reg_gnet(api, oid)

    async def lookup_gnet(self, api: AsyncApi, oid: int | IPv4Network | m.MPLSGroup | m.MPLSNet) -> m.MPLSGroup:
        match oid:
            case m.MPLSGroup():
                return oid
            case m.MPLSNet():
                return await self.get_gnet(api, oid.network)
            case _:
                return await self.get_gnet(api, oid)

    # endregion

    # region Nets

    async def get_net(self, api: AsyncApi, oid: ea.SiteID | int | IPv4Network) -> m.MPLSNet:
        return await self._get_net(api, oid, m.MPLSNet)

    async def try_get_net(self, api: AsyncApi, oid: ea.SiteID | int | IPv4Network) -> m.MPLSNet | None:
        try:
            return await self.get_net(api, oid)
        except Exception:
            return None

    async def get_nets(self, api: AsyncApi) -> list[m.MPLSNet]:
        return await api.get_nets(
            ea.SiteID.is_not_null(),
            network_container=self.net,
            return_cls=m.MPLSNet,
        )

    async def get_reg_net(self, api: AsyncApi, oid: int | IPv4Network) -> m.MPLSRegNet:
        network = self.calc_net(oid)
        return await api.get_net(network_container=self.net, network=network, return_cls=m.MPLSRegNet)

    async def get_reg_nets(self, api: AsyncApi) -> list[m.MPLSRegNet]:
        return await api.get_nets(
            ea.SiteID.is_not_null(),
            network_container=self.net,
            return_cls=m.MPLSRegNet,
        )

    async def get_all_nets(self, api: AsyncApi) -> MPLSNets:
        nets = await api.get_nets(network_container=self.net, return_cls=m.MPLSRegNet)
        res = MPLSNets([], [], [])

        for net in nets:
            if net.extattrs.siteid is not None:
                res.assigned.append(net.as_obj())
            else:
                res.registered.append(net)

        res.free.extend(set(self.net.subnets(new_prefix=self.prefix)).difference(n.network for n in nets))
        return res

    async def lookup_net(self, api: AsyncApi, oid: int | IPv4Network | m.MPLSNet) -> m.MPLSNet:
        match oid:
            case m.MPLSNet():
                return oid
            case _:
                return await self.get_net(api, oid)

    async def lookup_reg_net(self, api: AsyncApi, oid: int | IPv4Network | m.MPLSRegNet) -> m.MPLSRegNet:
        match oid:
            case m.MPLSRegNet():
                return oid
            case _:
                return await self.get_reg_net(api, oid)

    # endregion

    # region Ranges

    async def get_ranges(self, api: AsyncApi) -> list[m.MPLSRange]:
        return await api.get_ranges(self.nid, ea.SiteID.is_not_null(), return_cls=m.MPLSRange)

    async def get_all_ranges(self, api: AsyncApi) -> MPLSRanges:
        res = MPLSRanges([], [])
        for r in await api.get_ranges(self.nid, return_cls=m.MPLSRegRange):
            if r.extattrs.siteid is not None:
                res.assigned.append(r.as_obj())
            else:
                res.registered.append(r)
        return res

    # endregion

    async def register(self, api: AsyncApi, tmpl: m.MPLSTmpl) -> m.MPLSRegGroup:
        new_gnet = self.prepare_reg_gnet(tmpl)
        log.info(f"Register {self.name} {new_gnet}")
        return await self._create(api, new_gnet)

    async def assign(
        self,
        api: AsyncApi,
        net: IPv4Network | int | m.MPLSRegNet | m.MPLSRegGroup,
        info: m.SiteInfoAttrs,
    ) -> m.MPLSGroup:
        gregnet = await self.lookup_reg_gnet(api, net)
        gnet = await self._update(api, gregnet.assign(info))
        log.info(f"Assigned {info.siteid} {self.name} {gnet.net.network} {gnet.net.comment}")
        return gnet

    async def release(self, api: AsyncApi, gnet: m.MPLSGroup | m.MPLSNet | IPv4Network | int) -> m.MPLSRegGroup:
        _gnet = await self.lookup_gnet(api, gnet)
        return await self._update(api, _gnet.release())

    async def create(self, api: AsyncApi, tmpl: m.MPLSTmpl, info: m.SiteInfoAttrs) -> m.MPLSGroup:
        new_gnet = self.prepare_gnet(tmpl, info)
        log.info(f"Register and assign {self.name} {new_gnet} to {info.siteid}")
        return await self._create(api, new_gnet)

    async def create_or_assign(self, api: AsyncApi, tmpl: m.MPLSTmpl, info: m.SiteInfoAttrs) -> m.MPLSGroup:
        try:
            mpls_reg = await self.get_reg_gnet(api, tmpl.net)
        except Exception:
            return await self.create(api, tmpl, info)
        else:
            return await self.assign(api, mpls_reg, info)

    async def delete_gnet(
        self,
        api: AsyncApi,
        oid: m.MPLSRegGroup | m.MPLSGroup | m.MPLSNet | m.MPLSRegNet | IPv4Network | int,
    ) -> None:
        match oid:
            case m.MPLSGroup() | m.MPLSRegGroup():
                gnet = oid
            case m.MPLSNet() | m.MPLSRegNet():
                gnet = await self.lookup_reg_gnet(api, oid.network)
            case _:
                gnet = await self.lookup_reg_gnet(api, oid)
        await self._delete(api, gnet)

    async def _verify_reg_net(
        self,
        api: AsyncApi,
        net: m.MPLSRegNet,
        ranges: list[m.MPLSRegRange | m.MPLSRange],
        skip_comment: bool,
        fix: bool,
        hide_ok: bool,
    ) -> m.MPLSRegGroup | None:
        if self.calc_offset(net.network) < 0:
            return None

        vlog = VerifyLog(title=f"{net.network}")

        #############
        # Router
        #############
        old_router = net.router
        match self.gw:
            case None:
                match old_router:
                    case None:
                        vlog.ok("Router")
                    case _:
                        vlog.error("Router", f"Shoule be None is {old_router}")
                        if fix:
                            net.router = None
            case _:
                match old_router:
                    case None:
                        router = OptionRouter(value=net.network.network_address + self.gw)
                        vlog.error("Router", f"Missing {router}")
                        if fix:
                            net.router = router
                    case _:
                        router = OptionRouter(value=net.network.network_address + self.gw)
                        if router == old_router:
                            vlog.ok("Router")
                        else:
                            vlog.error("Router", f"Invalid {old_router} -> {router}")
                            if fix:
                                net.router = router

        #############
        # Members
        #############
        match len(self.members):
            case 0:
                match len(net.members):
                    case 0:
                        vlog.ok("Members")
                    case _:
                        vlog.error("Members", f"Should be empty got {net.members}")
                        if fix:
                            net.members = []
            case _:
                match len(net.members):
                    case 0:
                        vlog.error("Members", f"Missing members {self.members}")
                        if fix:
                            net.members = self.members
                    case _:
                        if set(net.members) != set(self.members):
                            vlog.error("Members", f"{net.members} -> {self.members}")
                            if fix:
                                net.members = self.members
                        else:
                            vlog.ok("Members")

        #############
        # Comment
        #############
        if not skip_comment:
            if net.comment is None:
                vlog.ok("Comment")
            else:
                vlog.error("Comment", f"Should be None [{net.comment}]")
                if fix:
                    net.comment = ""

        #############
        # Extattrs
        #############
        if net.extattrs.inst is not None:
            vlog.ok("ISPInst")
        else:
            vlog.error("ISPInst", "Missing value", update=False)

        if net.extattrs.kreds is not None:
            vlog.ok("ISPKreds")
        else:
            vlog.error("ISPKreds", "Missing value", update=False)

        #############
        # DHCP
        #############
        ranges_to_delete: list[m.MPLSRegRange | m.MPLSRange] = list()
        ranges_to_add: list[m.NewMPLSRegRange] = list()
        ranges_to_update: list[m.MPLSRegRange] = list()
        match self.dhcp:
            case None:
                match len(ranges):
                    case 0:
                        vlog.ok("Range")
                    case _:
                        vlog.error("Range", f"Should not be here {ranges}")
                        ranges_to_delete.extend(ranges)
            case _:
                match len(ranges):
                    case 0:
                        valid_range = self.prepare_reg_range(net.network)
                        vlog.error(
                            "Range",
                            f"Missing -> {valid_range.start_addr} - {valid_range.end_addr}",
                        )
                        ranges_to_add.append(valid_range)
                    case 1:
                        _lrange = ranges[0]
                        if isinstance(_lrange, m.MPLSRange):
                            vlog.error("Range", f"Assigned but should not be {_lrange}")
                            lrange = _lrange.as_reg(release=True)
                            ranges_to_update.append(lrange)
                        else:
                            lrange = _lrange
                        valid_range = self.prepare_reg_range(net.network)
                        if (
                            lrange.start_addr != valid_range.start_addr
                            or lrange.comment != valid_range.comment
                            or lrange.end_addr != valid_range.end_addr
                            or lrange.failover_association != valid_range.failover_association
                            or lrange.server_association_type != valid_range.server_association_type
                        ):
                            vlog.error("Range", f"{lrange} -> {valid_range}")
                            lrange.start_addr = valid_range.start_addr
                            lrange.end_addr = valid_range.end_addr
                            lrange.failover_association = valid_range.failover_association
                            lrange.server_association_type = valid_range.server_association_type
                            lrange.comment = valid_range.comment
                            lrange.extattrs.siteid = None
                            if lrange not in ranges_to_update:
                                ranges_to_update.append(lrange)
                        else:
                            vlog.ok("Range")
                    case _:
                        valid_range = self.prepare_reg_range(net.network)
                        vlog.error("Range", f"Multiple ranges {ranges} -> {valid_range}")
                        ranges_to_delete.extend(ranges)
                        ranges_to_add.append(valid_range)

        vlog.print(show_ok=not hide_ok)

        #############
        # Commit changes
        #############
        if fix and vlog.update:
            await api.update(net)
            for ran in ranges_to_delete:
                await api.delete(ran)
            for _ran in ranges_to_add:
                await api.create(_ran)
            for __ran in ranges_to_update:
                await api.update(__ran)

        if vlog.is_ok:
            r = None if self.gw is None or len(ranges) == 0 or not isinstance(ranges[0], m.MPLSRegRange) else ranges[0]
            return m.MPLSRegGroup(net=net, dhcp=r)
        else:
            return None

    async def _verify_net(
        self,
        api: AsyncApi,
        net: m.MPLSNet,
        ranges: list[m.MPLSRegRange | m.MPLSRange],
        info: m.SiteInfo | m.SiteInfoAttrs,
        skip_comment: bool,
        fix: bool,
        hide_ok: bool,
    ) -> m.MPLSGroup | None:
        if self.calc_offset(net.network) < 0:
            return None

        siteid = info.siteid
        comment = info.as_comment

        vlog = VerifyLog(title=f"{net.extattrs.siteid} - {net.network} - {info.as_comment}")

        #############
        # Router
        #############
        old_router = net.router
        match self.gw:
            case None:
                match old_router:
                    case None:
                        vlog.ok("Router")
                    case _:
                        vlog.error("Router", f"Shoule be None is {old_router}")
                        if fix:
                            net.router = None
            case _:
                match old_router:
                    case None:
                        router = OptionRouter(value=net.network.network_address + self.gw)
                        vlog.error("Router", f"Missing {router}")
                        if fix:
                            net.router = router
                    case _:
                        router = OptionRouter(value=net.network.network_address + self.gw)
                        if router == old_router:
                            vlog.ok("Router")
                        else:
                            vlog.error("Router", f"Invalid {old_router} -> {router}")
                            if fix:
                                net.router = router

        #############
        # Members
        #############
        match len(self.members):
            case 0:
                match len(net.members):
                    case 0:
                        vlog.ok("Members")
                    case _:
                        vlog.error("Members", f"Should be empty got {net.members}")
                        if fix:
                            net.members = []
            case _:
                match len(net.members):
                    case 0:
                        vlog.error("Members", f"Missing members {self.members}")
                        if fix:
                            net.members = self.members
                    case _:
                        if set(net.members) != set(self.members):
                            vlog.error("Members", f"{net.members} -> {self.members}")
                            if fix:
                                net.members = self.members
                        else:
                            vlog.ok("Members")

        #############
        # Extattrs
        #############
        if net.extattrs.inst is not None:
            vlog.ok("ISPInst")
        else:
            vlog.error("ISPInst", "Missing value", update=False)

        if net.extattrs.kreds is not None:
            vlog.ok("ISPKreds")
        else:
            vlog.error("ISPKreds", "Missing value", update=False)

        if net.extattrs.siteid == siteid:
            vlog.ok("SiteID")
        else:
            vlog.error("SiteID", f"SiteID {net.extattrs.siteid} -> {siteid}")
            net.extattrs.siteid = siteid

        #############
        # Comment
        #############
        if not skip_comment:
            if net.comment == comment:
                vlog.ok("Comment")
            else:
                vlog.error("Comment", f"[{net.comment}] -> [{comment}]")
                if fix:
                    net.comment = comment

        #############
        # DHCP
        #############
        ranges_to_delete: list[ib_m.RangeBase] = list()
        ranges_to_add: list[m.NewMPLSRange] = list()
        ranges_to_update: list[m.MPLSRange] = list()

        match self.dhcp:
            case None:
                match len(ranges):
                    case 0:
                        vlog.ok("Range")
                    case _:
                        vlog.error("Range", f"Should not be here {ranges}")
                        ranges_to_delete.extend(ranges)
            case _:
                match len(ranges):
                    case 0:
                        valid_range = self.prepare_range(net.network, info)
                        vlog.error(
                            "Range",
                            f"Missing -> {valid_range.start_addr} - {valid_range.end_addr}",
                        )
                        ranges_to_add.append(valid_range)
                    case 1:
                        valid_range = self.prepare_range(net.network, info)
                        _lrange = ranges[0]
                        if isinstance(_lrange, m.MPLSRegRange):
                            vlog.error("Range", f"Should be registered {_lrange}")
                            lrange = _lrange.assign(info)
                            ranges_to_update.append(lrange)
                        else:
                            lrange = _lrange
                        if (
                            lrange.start_addr != valid_range.start_addr
                            or lrange.end_addr != valid_range.end_addr
                            or lrange.failover_association != valid_range.failover_association
                            or lrange.server_association_type != valid_range.server_association_type
                        ):
                            vlog.error(
                                "Range From",
                                f"{lrange.start_addr} - {lrange.end_addr} - {lrange.extattrs.siteid} - {lrange.comment}",
                            )
                            vlog.error(
                                "Range To  ",
                                f"{valid_range.start_addr} - {valid_range.end_addr} - {valid_range.extattrs.siteid} - {valid_range.comment}",
                            )
                            lrange.start_addr = valid_range.start_addr
                            lrange.end_addr = valid_range.end_addr
                            lrange.failover_association = valid_range.failover_association
                            lrange.server_association_type = valid_range.server_association_type
                            lrange.comment = valid_range.comment
                            vlog.error("Range", f"Should updates {lrange} -> {valid_range}")
                            if lrange not in ranges_to_update:
                                ranges_to_update.append(lrange)
                        elif lrange.comment != comment and not skip_comment:
                            vlog.error(
                                "Range",
                                f"Comment should updates {lrange.comment} -> {valid_range.comment}",
                            )
                            lrange.comment = comment
                            if lrange not in ranges_to_update:
                                ranges_to_update.append(lrange)
                        else:
                            vlog.ok("Range")
                    case _:
                        valid_range = self.prepare_range(net.network, info)
                        vlog.error("Range", f"Multiple ranges {ranges} -> {valid_range}")
                        ranges_to_delete.extend(ranges)
                        ranges_to_add.append(valid_range)

        vlog.print(show_ok=not hide_ok)

        #############
        # Commit changes
        #############
        if fix and vlog.update:
            await api.update(net)
            for ran in ranges_to_delete:
                await api.delete(ran)
            for _ran in ranges_to_add:
                await api.create(_ran)
            for __ran in ranges_to_update:
                await api.update(__ran)

        if vlog.is_ok:
            dhcp = None if self.gw is None or len(ranges) == 0 or not isinstance(ranges[0], m.MPLSRange) else ranges[0]
            return m.MPLSGroup(net=net, dhcp=dhcp)
        else:
            return None

    async def verify(
        self,
        api: AsyncApi,
        infos: dict[ea.SiteID, m.SiteInfo],
        skip_comment: bool,
        fix: bool,
        hide_unused: bool,
        hide_ok: bool,
    ) -> None:
        PART = "MPLS"
        siteids_with_info = set(infos.keys())

        print(f"\n{PART}: Getting info")
        all_ranges = await self.get_all_ranges(api)
        all_nets = await self.get_all_nets(api)

        all_networks = set(n.network for n in all_nets.assigned)
        all_networks.update(n.network for n in all_nets.registered)

        assigned_net_dct: dict[ea.SiteID, list[m.MPLSNet]] = {}
        for net in all_nets.assigned:
            assigned_net_dct.setdefault(net.extattrs.siteid, []).append(net)
        siteids_with_mpls = set(assigned_net_dct.keys())
        siteids_witout_mpls = siteids_with_info.difference(siteids_with_mpls)

        single_assigned_net: dict[ea.SiteID, m.MPLSNet] = {}
        multi_assigned_net: dict[ea.SiteID, list[m.MPLSNet]] = {}
        for siteid, nets in assigned_net_dct.items():
            if len(nets) > 1:
                multi_assigned_net[siteid] = nets
            else:
                single_assigned_net[siteid] = nets[0]

        ranges_dct: dict[IPv4Network, list[m.MPLSRegRange | m.MPLSRange]] = {}
        ranges_without_net: list[m.MPLSRegRange | m.MPLSRange] = []
        for r in all_ranges.assigned:
            if r.network not in all_networks:
                ranges_without_net.append(r)
            ranges_dct.setdefault(r.network, []).append(r)
        for r2 in all_ranges.registered:
            if r2.network not in all_networks:
                ranges_without_net.append(r2)
            ranges_dct.setdefault(r2.network, []).append(r2)

        tdata: list[list[Any]] = []
        tdata.append(["Registered Nets", len(all_nets.registered)])
        tdata.append(["Assigned Nets", len(all_nets.assigned)])
        tdata.append(["Free Nets", len(all_nets.free)])
        tdata.append([SEPARATING_LINE])
        tdata.append(["All Ranges", len(all_ranges.registered) + len(all_ranges.assigned)])
        tdata.append(["Registered Ranges", len(all_ranges.registered)])
        tdata.append(["Assigned Ranges", len(all_ranges.assigned)])

        print()
        print(tabulate(tdata, tablefmt="simple"))

        print(f"\n{PART}: SiteIDs without mpls")
        for name, siteid in sorted(NameSiteid(s.value, s) for s in siteids_witout_mpls):
            print(f"  - {name}")

        print(f"\n{PART}: Ranges without net")
        net_table: list[list[str]] = []
        headers = ["DHCP Start", "DHCP Stop"]
        for ran in sorted(ranges_without_net, key=lambda x: x.start_addr):
            net_line = [
                str(ran.start_addr),
                str(ran.end_addr),
            ]
            net_table.append(net_line)
        if len(net_table) > 0:
            print()
            print(tabulate(net_table, headers=headers, tablefmt="outline"))

        print(f"\n{PART}: Registered Nets Validation")
        validated_reg_nets: list[m.MPLSRegGroup] = []

        async def _registered_nets_validation() -> None:
            for net in sorted(all_nets.registered, key=lambda x: x.network):
                gnet = await self._verify_reg_net(
                    api,
                    net,
                    ranges_dct.get(net.network, []),
                    skip_comment,
                    fix,
                    hide_ok,
                )
                if gnet is not None:
                    validated_reg_nets.append(gnet)

        await _registered_nets_validation()

        if not hide_unused:
            un_net_table: list[list[str]] = []
            print(f"\n{PART}: Registered Nets")
            headers = ["Net", "ISPKreds", "ISPInst"]
            if self.dhcp is not None:
                headers.extend(["DHCP Start", "DHCP Stop"])
            for gnet in validated_reg_nets:
                net_line = [
                    str(gnet.net.network),
                    str(gnet.net.extattrs.kreds),
                    str(gnet.net.extattrs.inst),
                ]
                if gnet.dhcp is not None:
                    net_line.extend(
                        [
                            str(gnet.dhcp.start_addr),
                            str(gnet.dhcp.end_addr),
                        ]
                    )
                un_net_table.append(net_line)
            if len(un_net_table) > 0:
                print()
                print(tabulate(un_net_table, headers=headers, tablefmt="outline"))

        print(f"\n{PART}: Assigned Nets With Overlapping SiteIDs")
        for siteid, nets in multi_assigned_net.items():
            print(f" - {siteid}")
            for net in nets:
                print(f"   - {net.network} - {net.extattrs}")

        print(f"\n{PART}: Assigned Nets Validation")
        validated_nets: list[m.MPLSGroup] = []

        async def _assigned_nets_validation() -> None:
            for siteid, net in sorted(single_assigned_net.items(), key=lambda x: x[1].network):
                gnet = await self._verify_net(
                    api,
                    net,
                    ranges_dct.get(net.network, []),
                    infos[siteid],
                    skip_comment=skip_comment,
                    fix=fix,
                    hide_ok=hide_ok,
                )
                if gnet is not None:
                    validated_nets.append(gnet)

        await _assigned_nets_validation()

        if not hide_unused:

            def _print_assigned_net_list() -> None:
                _net_table: list[list[str]] = []
                print(f"\n{PART}: Assigned Nets List")
                headers = ["Net", "SiteID", "ISPKreds", "ISPInst"]
                if self.dhcp is not None:
                    headers.extend(["DHCP Start", "DHCP Stop"])
                for gnet in validated_nets:
                    net_line = [
                        str(gnet.net.network),
                        str(gnet.net.extattrs.siteid),
                        str(gnet.net.extattrs.kreds),
                        str(gnet.net.extattrs.inst),
                    ]
                    if gnet.dhcp is not None:
                        net_line.extend(
                            [
                                str(gnet.dhcp.start_addr),
                                str(gnet.dhcp.end_addr),
                            ]
                        )
                    _net_table.append(net_line)
                if len(_net_table) > 0:
                    print()
                    print(tabulate(_net_table, headers=headers, tablefmt="outline"))

            _print_assigned_net_list()


class VNetGroups(NamedTuple):
    assigned: list[m.VNetGroup]
    unknown: list[ib_m.Network]
    free: list[IPv4Network]


class VNets(NamedTuple):
    assigned: list[m.VNet]
    unknown: list[ib_m.Network]
    free: list[IPv4Network]


class VNetRanges(NamedTuple):
    assigned: list[m.VNetRange]
    unknown: list[ib_m.Range]


@dataclasses.dataclass(slots=True, kw_only=True)
class AsyncVNetScope(AsyncNetScope):
    st: ea.SiteType

    # region Calculations
    @override
    def calc_offset(self, net: IPv4Network | m.VNetGroup | m.VNet) -> int:
        match net:
            case IPv4Network():
                return ipcalc.net_offset(self.net, net)
            case m.VNet():
                return ipcalc.net_offset(self.net, net.network)
            case m.VNetGroup():
                return ipcalc.net_offset(self.net, net.net.network)

    # endregion

    # region Prepare

    def prepare_net(self, tmpl: m.VNetTmpl, info: m.SiteInfo | m.SiteInfoAttrs) -> m.NewVNet:
        return m.NewVNet(
            network=self.calc_net(tmpl),
            comment=info.as_comment,
            options=self.get_options(),
            members=self.get_members(),
            extattrs=m.VNetAttrs(siteid=info.siteid),
        )

    def prepare_range(self, net: IPv4Network, info: m.SiteInfo | m.SiteInfoAttrs) -> m.NewVNetRange:
        if self.dhcp is None:
            raise Exception("not dhcp")
        return m.NewVNetRange(
            start_addr=self.dhcp.calc_start_addr(net),
            end_addr=self.dhcp.calc_start_addr(net),
            comment=info.as_comment,
            server_association_type=self.dhcp.server_association_type,
            failover_association=self.dhcp.failover_association,
            extattrs=m.VNetRangeAttrs(siteid=info.siteid),
        )

    # endregion

    # region Group

    async def create(
        self,
        api: AsyncApi,
        tmpl: m.VNetTmpl,
        info: m.SiteInfo | m.SiteInfoAttrs,
    ) -> m.VNetGroup:
        vnet = await self.create_net(api, tmpl, info)
        dhcp = None if self.dhcp is None else await self.create_range(api, vnet.network, info)

        return m.VNetGroup(net=vnet, dhcp=dhcp)

    async def get_gnet(self, api: AsyncApi, oid: ea.SiteID | int | IPv4Network) -> m.VNetGroup:
        net = await self._get_net(api, oid, m.VNet)
        dhcp = await self._try_get_range(api, net.extattrs.siteid, net.network, m.VNetRange)
        return m.VNetGroup(net=net, dhcp=dhcp)

    async def try_get_gnet(self, api: AsyncApi, oid: ea.SiteID | int | IPv4Network) -> m.VNetGroup | None:
        try:
            return await self.get_gnet(api, oid)
        except Exception:
            return None

    async def get_gnets(self, api: AsyncApi) -> list[m.VNetGroup]:
        nets = await self.get_nets(api)
        ranges = await self.get_ranges(api)
        ran_dct: dict[IPv4Network, m.VNetRange] = {n.network: n for n in ranges}

        return [m.VNetGroup(net=net, dhcp=ran_dct.get(net.network, None)) for net in nets]

    async def lookup_gnet(self, api: AsyncApi, oid: int | IPv4Network | m.VNetGroup | m.VNet) -> m.VNetGroup:
        match oid:
            case m.VNetGroup():
                return oid
            case m.VNet():
                return await self.get_gnet(api, oid.network)
            case _:
                return await self.get_gnet(api, oid)

    async def get_all(self, api: AsyncApi) -> VNetGroups:
        res = VNetGroups([], [], [])
        res.assigned.extend(await self.get_gnets(api))
        res.unknown.extend(await self.get_unknown_nets(api))
        res.free.extend(
            set(self.net.subnets(new_prefix=self.prefix))
            .difference(n.network for n in res.unknown)
            .difference(n.net.network for n in res.assigned)
        )
        return res

    # endregion

    # region Nets

    async def create_net(
        self,
        api: AsyncApi,
        tmpl: m.VNetTmpl,
        info: m.SiteInfo | m.SiteInfoAttrs,
    ) -> m.VNet:
        vnet: m.VNet = await api.create(self.prepare_net(tmpl, info))

        if self.gw is not None:
            vnet.options = self.get_options(vnet.network)
            vnet = await api.update(vnet)

        log.info(f"Allocated {info.siteid} {self.name} {vnet.network} {vnet.comment}")
        return vnet

    async def get_net(self, api: AsyncApi, oid: ea.SiteID | int | IPv4Network) -> m.VNet:
        return await self._get_net(api, oid, m.VNet)

    async def try_get_net(self, api: AsyncApi, oid: ea.SiteID | int | IPv4Network) -> m.VNet | None:
        try:
            return await self.get_net(api, oid)
        except Exception:
            return None

    async def get_nets(self, api: AsyncApi) -> list[m.VNet]:
        return await api.get_nets(
            ea.SiteID.is_not_null(),
            network_container=self.net,
            return_cls=m.VNet,
        )

    async def get_all_nets(self, api: AsyncApi) -> VNets:
        res = VNets([], [], [])
        res.assigned.extend(await self.get_nets(api))
        res.unknown.extend(await self.get_unknown_nets(api))
        res.free.extend(
            set(self.net.subnets(new_prefix=self.prefix))
            .difference(n.network for n in res.unknown)
            .difference(n.network for n in res.assigned)
        )
        return res

    async def lookup_net(self, api: AsyncApi, oid: int | IPv4Network | m.VNet) -> m.VNet:
        match oid:
            case m.VNet():
                return oid
            case _:
                return await self.get_net(api, oid)

    # endregion

    # region Ranges

    async def create_range(self, api: AsyncApi, net: IPv4Network, info: m.SiteInfo | m.SiteInfoAttrs) -> m.VNetRange:
        ran = await api.create(self.prepare_range(net, info))
        log.info(f"Allocated {info.siteid} Range {ran.start_addr}-{ran.end_addr}")
        return ran

    async def get_ranges(self, api: AsyncApi) -> list[m.VNetRange]:
        return await api.get_ranges(self.nid, ea.SiteID.is_not_null(), return_cls=m.VNetRange)

    async def get_all_ranges(self, api: AsyncApi) -> VNetRanges:
        res = VNetRanges([], [])
        res.assigned.extend(await self.get_ranges(api))
        res.unknown.extend(await self.get_unknown_ranges(api))
        return res

    # endregion

    async def release(self, api: AsyncApi, gnet: m.VNetGroup) -> None:
        await self.delete(api, gnet)

    async def delete(self, api: AsyncApi, oid: ea.SiteID | int | IPv4Network | m.VNet | m.VNetGroup) -> None:
        match oid:
            case m.VNetGroup():
                gnet = oid
            case m.VNet():
                gnet = m.VNetGroup(
                    net=oid,
                    dhcp=await self._try_get_range(
                        api, oid.extattrs.siteid, network=oid.network, return_cls=m.VNetRange
                    ),
                )
            case _:
                gnet = await self.get_gnet(api, oid)

        if gnet.dhcp is not None:
            await api.delete(gnet.dhcp)
        await api.delete(gnet.net)

    def _verify_range(
        self,
        net: m.VNet,
        info: m.SiteInfo | m.SiteInfoAttrs,
        range: m.VNetRange | m.VNetUnknownRange,
        ranges_to_update: list[m.VNetRange],
        skip_comment: bool,
        vlog: VerifyLog,
    ) -> None:
        valid_range = self.prepare_range(net.network, info)
        _lrange = range
        if isinstance(_lrange, m.VNetUnknownRange):
            vlog.error("Range", f"Unkown but should not be {_lrange}")
            lrange = _lrange.assign(info)
            ranges_to_update.append(lrange)
        else:
            lrange = _lrange
        if (
            lrange.start_addr != valid_range.start_addr
            or lrange.end_addr != valid_range.end_addr
            or lrange.failover_association != valid_range.failover_association
            or lrange.server_association_type != valid_range.server_association_type
        ):
            vlog.error(
                "Range From",
                f"{lrange.start_addr} - {lrange.end_addr} - {lrange.extattrs.siteid} - {lrange.comment}",
            )
            vlog.error(
                "Range To  ",
                f"{valid_range.start_addr} - {valid_range.end_addr} - {valid_range.extattrs.siteid} - {valid_range.comment}",
            )
            lrange.start_addr = valid_range.start_addr
            lrange.end_addr = valid_range.end_addr
            lrange.failover_association = valid_range.failover_association
            lrange.server_association_type = valid_range.server_association_type
            lrange.comment = valid_range.comment
            lrange.extattrs.siteid = info.siteid

            if lrange not in ranges_to_update:
                ranges_to_update.append(lrange)
        elif lrange.comment != info.as_comment and not skip_comment:
            lrange.comment = info.as_comment
            ranges_to_update.append(lrange)
        else:
            vlog.ok("Range")

    async def _verify_net(
        self,
        api: AsyncApi,
        net: m.VNet,
        ranges: list[m.VNetRange],
        uranges: list[m.VNetUnknownRange],
        info: m.SiteInfo | m.SiteInfoAttrs,
        skip_comment: bool,
        fix: bool,
        hide_ok: bool,
    ) -> ObjWOffset[m.VNetGroup] | None:
        if self.calc_offset(net.network) < 0:
            return None

        siteid = info.siteid
        comment = info.as_comment

        vlog = VerifyLog(title=f"{self.nid.value} - {net.extattrs.siteid} - {net.network}")

        #############
        # Router
        #############
        old_router = net.router
        match self.gw:
            case None:
                match old_router:
                    case None:
                        vlog.ok("Router")
                    case _:
                        vlog.error("Router", f"Shoule be None is {old_router}")
                        if fix:
                            net.router = None
            case _:
                match old_router:
                    case None:
                        router = OptionRouter(value=net.network.network_address + self.gw)
                        vlog.error("Router", f"Missing {router}")
                        if fix:
                            net.router = router
                    case _:
                        router = OptionRouter(value=net.network.network_address + self.gw)
                        if router == old_router:
                            vlog.ok("Router")
                        else:
                            vlog.error("Router", f"Invalid {old_router} -> {router}")
                            if fix:
                                net.router = router

        #############
        # Members
        #############
        match len(self.members):
            case 0:
                match len(net.members):
                    case 0:
                        vlog.ok("Members")
                    case _:
                        vlog.error("Members", f"Should be empty got {net.members}")
                        if fix:
                            net.members = []
            case _:
                match len(net.members):
                    case 0:
                        vlog.error("Members", f"Missing members {self.members}")
                        if fix:
                            net.members = self.members
                    case _:
                        if set(net.members) != set(self.members):
                            vlog.error("Members", f"{net.members} -> {self.members}")
                            if fix:
                                net.members = self.members
                        else:
                            vlog.ok("Members")

        #############
        # Extattrs
        #############
        if net.extattrs.siteid == siteid:
            vlog.ok("SiteID")
        else:
            vlog.error("SiteID", f"SiteID {net.extattrs.siteid} -> {siteid}")
            net.extattrs.siteid = siteid

        #############
        # Comment
        #############
        if not skip_comment:
            if net.comment == comment:
                vlog.ok("Comment")
            else:
                vlog.error("Comment", f"[{net.comment}] -> [{comment}]")
                if fix:
                    net.comment = comment

        #############
        # DHCP
        #############
        ranges_to_delete: list[ib_m.RangeBase] = []
        ranges_to_add: list[m.NewVNetRange] = []
        ranges_to_update: list[m.VNetRange] = []

        all_ranges: list[m.VNetUnknownRange | m.VNetRange] = [*uranges, *ranges]

        match self.dhcp:
            case None:
                match len(all_ranges):
                    case 0:
                        vlog.ok("Range")
                    case _:
                        vlog.error("Range", f"Should not be here {ranges}")
                        ranges_to_delete.extend(ranges)
            case _:
                match len(all_ranges):
                    case 0:
                        valid_range = self.prepare_range(net.network, info)
                        vlog.error(
                            "Range",
                            f"Missing -> {valid_range.start_addr} - {valid_range.end_addr}",
                        )
                        ranges_to_add.append(valid_range)
                    case 1:
                        self._verify_range(net, info, all_ranges[0], ranges_to_update, skip_comment, vlog)
                    case _:

                        def _dhc_() -> None:
                            valid_range = self.prepare_range(net.network, info)
                            vlog.error("Range", f"Multiple ranges {ranges} -> {valid_range}")
                            ranges_to_delete.extend(ranges)
                            ranges_to_add.append(valid_range)

                        _dhc_()

        vlog.print(show_ok=not hide_ok)

        #############
        # Commit changes
        #############
        if fix and vlog.update:
            await api.update(net)
            for ran in ranges_to_delete:
                await api.delete(ran)
            for _ran in ranges_to_add:
                await api.create(_ran)
            for __ran in ranges_to_update:
                await api.update(__ran)

        if vlog.is_ok:
            return ObjWOffset(
                m.VNetGroup(net=net, dhcp=None if self.gw is None else ranges[0]),
                self.calc_offset(net.network),
            )
        else:
            return None

    async def verify(
        self,
        api: AsyncApi,
        infos: dict[ea.SiteID, m.SiteInfo],
        skip_comment: bool,
        fix: bool,
        hide_unused: bool,
        hide_ok: bool = True,
    ) -> ColWOffset[ea.NID]:
        PART = f"VNET: {self.nid.value}"
        siteid_all_set = set(infos.keys())

        print(f"\n{PART}: Getting info")
        all_ranges = await api.get_ranges(self.nid, return_cls=m.VNetUnknownRange)
        unknown_nets = await api.get_unknown_nets(self.net, return_cls=m.VNetUnknown)
        assigned_nets = await self.get_nets(api)

        assigned_net_dct: dict[ea.SiteID, list[m.VNet]] = {}
        for net in assigned_nets:
            assigned_net_dct.setdefault(net.extattrs.siteid, []).append(net)

        single_assigned_net: dict[ea.SiteID, m.VNet] = {}
        multi_assigned_net: dict[ea.SiteID, list[m.VNet]] = {}
        for siteid, nets in assigned_net_dct.items():
            try:
                siteid_all_set.remove(siteid)
            except Exception:
                print(f"Wonky {siteid}")
            if len(nets) > 1:
                multi_assigned_net[siteid] = nets
            else:
                single_assigned_net[siteid] = nets[0]

        unknown_ranges: dict[IPv4Network, list[m.VNetUnknownRange]] = {}
        assigned_ranges: dict[IPv4Network, list[m.VNetRange]] = {}
        uassigned_ranges: dict[IPv4Network, list[m.VNetUnknownRange]] = {}
        ranges_without_net: list[m.VNetUnknownRange] = []

        def _run_all_ranges() -> None:
            for ran in all_ranges:
                for net in unknown_nets:
                    if ran.start_addr in net.network:
                        unknown_ranges.setdefault(net.network, []).append(ran)
                        break
                else:
                    for net2 in assigned_nets:
                        if ran.start_addr in net2.network:
                            if ran.extattrs.siteid is None:
                                uassigned_ranges.setdefault(net2.network, []).append(ran)
                            else:
                                assigned_ranges.setdefault(net2.network, []).append(ran.as_obj())
                            break
                    else:
                        ranges_without_net.append(ran)

        _run_all_ranges()

        tdata: list[list[Any] | str] = []
        tdata.append(["Unknown Nets", len(unknown_nets)])
        tdata.append(["Assigned Nets", len(assigned_nets)])
        tdata.append(SEPARATING_LINE)
        tdata.append(["All Ranges", len(all_ranges)])
        tdata.append(["Unknown Ranges", len(unknown_ranges)])
        tdata.append(["Uassigned Ranges", len(uassigned_ranges)])
        tdata.append(["Assigned Ranges", len(assigned_ranges)])
        tdata.append(["Unknown Ranges", len(ranges_without_net)])

        print()
        print(tabulate(tdata, tablefmt="simple"))

        print(f"\n{PART}: SiteIDs without vnet")
        for name, siteid in sorted(NameSiteid(s.value, s) for s in siteid_all_set):
            print(f"  - {name}")

        print(f"\n{PART}: Ranges without net")
        net_table: list[list[str]] = []
        headers = ["DHCP Start", "DHCP Stop"]
        for ran in ranges_without_net:
            net_line = [
                str(ran.start_addr),
                str(ran.end_addr),
            ]
            net_table.append(net_line)
        if len(net_table) > 0:
            print()
            print(tabulate(net_table, headers=headers, tablefmt="outline"))

        print(f"\n{PART}: Unknown Nets")
        unnet_table: list[list[str]] = []
        headers = ["Net"]

        net_lines = [[str(net.network)] for net in unknown_nets]
        unnet_table.extend(net_lines)
        if len(unnet_table) > 0:
            print()
            print(tabulate(unnet_table, headers=headers, tablefmt="outline"))

        print(f"\n{PART}: Unknown Ranges")
        urnet_table: list[list[str]] = []
        headers = ["SiteID", "DHCP Start", "DHCP Stop"]
        for _siteid, rans in unknown_ranges.items():
            for ran in rans:
                net_line = [
                    str(_siteid),
                    str(ran.start_addr),
                    str(ran.end_addr),
                ]
                urnet_table.append(net_line)
        if len(urnet_table) > 0:
            print()
            print(tabulate(urnet_table, headers=headers, tablefmt="outline"))

        print(f"\n{PART}: Nets Validation of {len(single_assigned_net)}")
        validated_nets: list[tuple[m.VNetGroup, int]] = []
        for siteid, net in single_assigned_net.items():
            gnet = await self._verify_net(
                api,
                net,
                assigned_ranges.get(net.network, []),
                uassigned_ranges.get(net.network, []),
                infos[siteid],
                skip_comment=skip_comment,
                fix=fix,
                hide_ok=hide_ok,
            )
            if gnet is not None:
                validated_nets.append(gnet)

        if not hide_unused:
            huh_net_table: list[list[str]] = []
            print(f"\n{PART}: Assigned Nets List")
            headers = ["Net", "SiteID"]
            if self.dhcp is not None:
                headers.extend(["DHCP Start", "DHCP Stop"])
            for gnet3, _ in validated_nets:
                net_line = [
                    str(gnet3.net.network),
                    str(gnet3.net.extattrs.siteid),
                ]
                if gnet3.dhcp is not None:
                    net_line.extend(
                        [
                            str(gnet3.dhcp.start_addr),
                            str(gnet3.dhcp.end_addr),
                        ]
                    )
                huh_net_table.append(net_line)
            if len(huh_net_table) > 0:
                print()
                print(tabulate(huh_net_table, headers=headers, tablefmt="outline"))

        print(f"\n{PART}: Valids {len(validated_nets)}")

        valid_dct: dict[ea.SiteID, int] = {gnet.net.extattrs.siteid: offset for gnet, offset in validated_nets}

        print(f"\n{PART}: Total {len(valid_dct)}")

        return ColWOffset(self.nid, valid_dct)


@dataclasses.dataclass(slots=True, kw_only=True)
class AsyncVNetSet:
    vn001: AsyncVNetScope
    vn002: AsyncVNetScope
    vn003: AsyncVNetScope
    vn004: AsyncVNetScope
    vn005: AsyncVNetScope
    vn006: AsyncVNetScope
    vn007: AsyncVNetScope
    vn008: AsyncVNetScope

    async def get(self, api: AsyncApi, siteid: ea.SiteID) -> m.VNetSet:
        return m.VNetSet(
            vn001=await self.vn001.get_gnet(api, siteid),
            vn002=await self.vn002.get_gnet(api, siteid),
            vn003=await self.vn003.get_gnet(api, siteid),
            vn004=await self.vn004.get_gnet(api, siteid),
            vn005=await self.vn005.get_gnet(api, siteid),
            vn006=await self.vn006.get_gnet(api, siteid),
            vn007=await self.vn007.get_gnet(api, siteid),
            vn008=await self.vn008.get_gnet(api, siteid),
        )

    async def get_all(self, api: AsyncApi) -> dict[ea.SiteID, m.VNetSet]:
        async with tasklog.TaskGroup() as tg:
            t_vn001 = tg.create_task(self.vn001.get_gnets(api), "Getting VN001")
            t_vn002 = tg.create_task(self.vn002.get_gnets(api), "Getting VN002")
            t_vn003 = tg.create_task(self.vn003.get_gnets(api), "Getting VN003")
            t_vn004 = tg.create_task(self.vn004.get_gnets(api), "Getting VN004")
            t_vn005 = tg.create_task(self.vn005.get_gnets(api), "Getting VN005")
            t_vn006 = tg.create_task(self.vn006.get_gnets(api), "Getting VN006")
            t_vn007 = tg.create_task(self.vn007.get_gnets(api), "Getting VN007")
            t_vn008 = tg.create_task(self.vn008.get_gnets(api), "Getting VN008")

        vn001 = {n.net.extattrs.siteid: n for n in t_vn001.result()}
        vn002 = {n.net.extattrs.siteid: n for n in t_vn002.result()}
        vn003 = {n.net.extattrs.siteid: n for n in t_vn003.result()}
        vn004 = {n.net.extattrs.siteid: n for n in t_vn004.result()}
        vn005 = {n.net.extattrs.siteid: n for n in t_vn005.result()}
        vn006 = {n.net.extattrs.siteid: n for n in t_vn006.result()}
        vn007 = {n.net.extattrs.siteid: n for n in t_vn007.result()}
        vn008 = {n.net.extattrs.siteid: n for n in t_vn008.result()}

        dct: dict[ea.SiteID, m.VNetSet] = {}
        for siteid in vn001:
            try:
                dct[siteid] = m.VNetSet(
                    vn001=vn001[siteid],
                    vn002=vn002[siteid],
                    vn003=vn003[siteid],
                    vn004=vn004[siteid],
                    vn005=vn005[siteid],
                    vn006=vn006[siteid],
                    vn007=vn007[siteid],
                    vn008=vn008[siteid],
                )
            except Exception:
                pass
        return dct

    async def release(self, api: AsyncApi, vnets: m.VNetSet) -> None:
        await self.vn008.release(api, vnets.vn008)
        await self.vn007.release(api, vnets.vn007)
        await self.vn006.release(api, vnets.vn006)
        await self.vn005.release(api, vnets.vn005)
        await self.vn004.release(api, vnets.vn004)
        await self.vn003.release(api, vnets.vn003)
        await self.vn002.release(api, vnets.vn002)
        await self.vn001.release(api, vnets.vn001)

    async def delete(self, api: AsyncApi, siteid: ea.SiteID) -> None:
        await self.vn008.delete(api, siteid)
        await self.vn007.delete(api, siteid)
        await self.vn006.delete(api, siteid)
        await self.vn005.delete(api, siteid)
        await self.vn004.delete(api, siteid)
        await self.vn003.delete(api, siteid)
        await self.vn002.delete(api, siteid)
        await self.vn001.delete(api, siteid)

    async def create(self, api: AsyncApi, tmpl: m.VNetTmpl, info: m.SiteInfoAttrs) -> m.VNetSet:
        vn001 = await self.vn001.create(api, tmpl, info)
        offset = self.vn001.calc_offset(vn001)
        vn002 = await self.vn002.create(api, offset, info)
        vn003 = await self.vn003.create(api, offset, info)
        vn004 = await self.vn004.create(api, offset, info)
        vn005 = await self.vn005.create(api, offset, info)
        vn006 = await self.vn006.create(api, offset, info)
        vn007 = await self.vn007.create(api, offset, info)
        vn008 = await self.vn008.create(api, offset, info)

        return m.VNetSet(
            vn001=vn001,
            vn002=vn002,
            vn003=vn003,
            vn004=vn004,
            vn005=vn005,
            vn006=vn006,
            vn007=vn007,
            vn008=vn008,
        )

    async def verify(
        self,
        api: AsyncApi,
        infos: dict[ea.SiteID, m.SiteInfo],
        comments: dict[ea.SiteID, str],
        skip_comment: bool,
        fix: bool,
        hide_unused: bool,
        hide_ok: bool,
    ) -> None:
        PART = "VNETS"

        vnet_dcts = [
            await self.vn001.verify(
                api,
                infos,
                skip_comment,
                fix=fix,
                hide_unused=hide_unused,
                hide_ok=hide_ok,
            ),
            await self.vn002.verify(
                api,
                infos,
                skip_comment,
                fix=fix,
                hide_unused=hide_unused,
                hide_ok=hide_ok,
            ),
            await self.vn003.verify(
                api,
                infos,
                skip_comment,
                fix=fix,
                hide_unused=hide_unused,
                hide_ok=hide_ok,
            ),
            await self.vn004.verify(
                api,
                infos,
                skip_comment,
                fix=fix,
                hide_unused=hide_unused,
                hide_ok=hide_ok,
            ),
            await self.vn005.verify(
                api,
                infos,
                skip_comment,
                fix=fix,
                hide_unused=hide_unused,
                hide_ok=hide_ok,
            ),
            await self.vn006.verify(
                api,
                infos,
                skip_comment,
                fix=fix,
                hide_unused=hide_unused,
                hide_ok=hide_ok,
            ),
            await self.vn007.verify(
                api,
                infos,
                skip_comment,
                fix=fix,
                hide_unused=hide_unused,
                hide_ok=hide_ok,
            ),
            await self.vn008.verify(
                api,
                infos,
                skip_comment,
                fix=fix,
                hide_unused=hide_unused,
                hide_ok=hide_ok,
            ),
        ]

        siteids: set[ea.SiteID] = set()
        for _, vnet_dct in vnet_dcts:
            siteids.update(vnet_dct.keys())

        siteids_incorrect_vnets: dict[ea.SiteID, list[ea.NID]] = {}
        siteids_incorrect_offset: dict[ea.SiteID, list[ObjWOffset[ea.NID]]] = {}
        valid_siteids = set(siteids)
        for siteid in siteids:
            offsets: list[ObjWOffset[ea.NID]] = []
            offset_count: set[int] = set()
            nids: list[ea.NID] = []
            for nid, vnet_dct in vnet_dcts:
                offset = vnet_dct.get(siteid, None)
                if offset is not None:
                    offsets.append(ObjWOffset(nid, offset))
                    offset_count.add(offset)
                    nids.append(nid)
            if len(nids) != len(vnet_dcts):
                siteids_incorrect_vnets[siteid] = nids
                valid_siteids.discard(siteid)
            if len(offset_count) != 1:
                siteids_incorrect_offset[siteid] = offsets
                valid_siteids.discard(siteid)

        print(f"\n{PART}: ea.SiteIDs with incorrect number vnets")
        for siteid, loops in siteids_incorrect_vnets.items():
            print(f"{siteid} [{loops}]")

        print(f"\n{PART}: ea.SiteIDs with incorrect vnet offset")
        for siteid, offsets in siteids_incorrect_offset.items():
            print(f"{siteid} [{offsets}]")

        print(f"\n{PART}: Total {len(valid_siteids)}")

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.startswith("t"):
            fields = dataclasses.fields(self)
            indent_str = __format_spec[1:]
            indent = int(indent_str) if len(indent_str) > 0 else 0
            ind = " " * (indent * 4)
            fieldstrs = [f"{ind}{field.name}:{getattr(self, field.name):t{indent+1}}" for field in fields]
            return "\n" + "\n".join(fieldstrs)

        return super().__format__(__format_spec)


@dataclasses.dataclass(slots=True, kw_only=True)
class AsyncSiteInfoScope(AsyncAddrScope):
    async def create(self, api: AsyncApi, addr: IPv4Address | int | None, attrs: m.SiteInfoAttrs) -> m.SiteInfo:
        new_obj = m.NewSiteInfo(
            network=self.net,
            ipv4addr=self.calc_addr(addr),
            comment=attrs.as_comment,
            extattrs=attrs,
        )

        obj: m.SiteInfo = await api.create(new_obj)

        log.info(f"Created {obj.extattrs.siteid} Siteinfo {obj.ipv4addr} {obj.comment}")

        return obj

    async def release(self, api: AsyncApi, addr: m.SiteInfo) -> None:
        await api.delete(addr)

    async def get(self, api: AsyncApi, siteid: ea.SiteID) -> m.SiteInfo:
        return await api.get_addr(self.net, siteid, return_cls=m.SiteInfo)

    async def get_all(self, api: AsyncApi) -> dict[ea.SiteID, m.SiteInfo]:
        addrs = await api.get_addrs(ea.SiteID.is_not_null(), network=self.net, return_cls=m.SiteInfo)
        dct: dict[ea.SiteID, m.SiteInfo] = {a.siteid: a for a in addrs}
        return dct

    async def filter(self, api: AsyncApi, *extattrs: SearchExtAttr) -> list[m.SiteInfo]:
        return await api.get_addrs(*extattrs, network=self.net, return_cls=m.SiteInfo)

    async def delete(self, api: AsyncApi, info: ea.SiteID | m.SiteInfo) -> None:
        if isinstance(info, ea.SiteID):
            _info = await self.get(api, info)
        else:
            _info = info
        log.info(f"Removing {_info.extattrs.siteid} Siteinfo {_info.ipv4addr} {_info.comment}")
        await api.delete(_info)

    async def update(self, api: AsyncApi, info: m.SiteInfo) -> m.SiteInfo:
        return await api.update(info)

    async def verify(self, api: AsyncApi, siteids: set[ea.SiteID], fix: bool) -> dict[ea.SiteID, m.SiteInfo]:
        PART = "INFO"
        siteid_all_set = set(siteids)

        print(f"\n{PART}: {self.nid}")
        print(f"\n{PART}: Missing ea.SiteIDs")
        addr_without_siteid = await self._get_unknowns(api)
        for addr in addr_without_siteid:
            if self.calc_offset(addr.ipv4addr) < 0:
                continue

            attrs = format_extra(addr.extattrs)
            print(f" - {addr.ipv4addr} - {attrs}")
            if fix:
                await api.delete(addr)

        addr_dct: dict[ea.SiteID, list[m.SiteInfo]] = {}
        addrs = await self.filter(api)
        for addr3 in addrs:
            addr_dct.setdefault(addr3.extattrs.siteid, []).append(addr3)

        siteid_set: set[ea.SiteID] = set()
        dup_siteid: set[ea.SiteID] = set()
        valid_addrs: dict[ea.SiteID, m.SiteInfo] = {}
        for siteid, addrs in addr_dct.items():
            siteid_all_set.remove(siteid)
            siteid_set.add(siteid)
            if len(addrs) > 1:
                dup_siteid.add(siteid)
            else:
                valid_addrs[siteid] = addrs[0]

        print(f"\n{PART}: ea.SiteIDs without loop")
        for name, siteid in sorted(NameSiteid(s.value, s) for s in siteid_all_set):
            print(f"  - {name}")

        print(f"\n{PART}: Duplicate ea.SiteIDs")
        for siteid in dup_siteid:
            addrs = addr_dct[siteid]
            print(f" - {siteid}")
            for dup_addr in addrs:
                print(f"   - {dup_addr.ipv4addr} - {dup_addr.extattrs}")

        print(f"\n{PART}: Valid ea.SiteIDS")
        print(f" - {len(valid_addrs)}")

        return valid_addrs


@dataclasses.dataclass(slots=True, kw_only=True)
class AsyncAPNScope(AsyncAddrScope):
    async def create(
        self,
        api: AsyncApi,
        tmpl: m.APNRegTmpl,
        info: m.SiteInfoAttrs,
    ) -> ObjWOffset[m.APNAddr]:
        new_obj = m.NewAPN(
            network=self.net,
            ipv4addr=self.calc_addr(tmpl.addr),
            comment=info.as_comment,
            extattrs=m.APNAttrs(siteid=info.siteid, sim=tmpl.sim),
        )

        obj = await api.create(new_obj)

        log.info(f"Create {info.siteid} {self.name} {obj.ipv4addr} {obj.comment} {obj.extattrs.sim}")

        return ObjWOffset(obj, self.calc_offset(obj.ipv4addr))

    async def get(self, api: AsyncApi, oid: ea.SiteID) -> m.APNAddr:
        return await api.get_addr(self.net, oid, return_cls=m.APNAddr)

    async def get_all(self, api: AsyncApi) -> dict[ea.SiteID, m.APNAddr]:
        addrs = await api.get_addrs(ea.SiteID.is_not_null(), network=self.net, return_cls=m.APNAddr)
        dct: dict[ea.SiteID, m.APNAddr] = {a.extattrs.siteid: a for a in addrs}
        return dct

    async def try_get(self, api: AsyncApi, oid: ea.SiteID) -> m.APNAddr | None:
        try:
            return await self.get(api, oid)
        except Exception:
            return None

    async def get_reg(self, api: AsyncApi, oid: int | IPv4Address) -> m.APNRegAddr:
        ipv4addr = self.calc_addr(oid)
        return await api.get_addr_reg(ipv4addr=ipv4addr, network=self.net, return_cls=m.APNRegAddr)

    async def get_registered_addrs(self, api: AsyncApi) -> list[m.APNRegAddr]:
        return await api.get_addrs(ea.SiteID.is_null(), network=self.net, return_cls=m.APNRegAddr)

    async def get_addrs(self, api: AsyncApi) -> list[m.APNAddr]:
        return await api.get_addrs(ea.SiteID.is_not_null(), network=self.net, return_cls=m.APNAddr)

    async def register(self, api: AsyncApi, tmpl: m.APNRegTmpl) -> m.APNRegAddr:
        addr = await api.create(
            m.NewAPNReg(
                ipv4addr=self.calc_addr(tmpl.addr),
                extattrs=m.APNRegAttrs(sim=tmpl.sim),
            )
        )

        log.info(f"Register {self.name} {addr.ipv4addr} {addr.comment} {addr.extattrs.sim}")
        return addr

    async def assign(self, api: AsyncApi, addr: IPv4Address | int | m.APNRegAddr, info: m.SiteInfoAttrs) -> m.APNAddr:
        raddr = addr if isinstance(addr, m.APNRegAddr) else await self.get_reg(api, addr)
        raddr.extattrs.siteid = info.siteid
        _raddr = raddr.as_obj()  # TODO Fix put so it has a return cls
        return await api.update(_raddr)

    async def release(self, api: AsyncApi, addr: m.APNAddr) -> None:
        raddr = addr.as_reg()
        raddr.extattrs.siteid = None
        await api.update(raddr)

    async def filter(self, api: AsyncApi, *extattrs: SearchExtAttr) -> list[m.APNAddr]:
        return await api.get_addrs(*extattrs, network=self.net, return_cls=m.APNAddr)

    async def delete(self, api: AsyncApi, siteid: ea.SiteID) -> None:
        try:
            addrs = await api.get_addrs(siteid, network=self.net, return_cls=m.APNAddr)
            if len(addrs) > 5:
                raise Exception(f"to many addresses {addrs}")
            for addr in addrs:
                log.info(f"Deallocate {siteid} {self.name} {addr.ipv4addr}")
                await api.delete(addr)
        except Exception as e:
            log.error(e)

    async def create_or_assign(self, api: AsyncApi, tmpl: m.APNTmpl, info: m.SiteInfoAttrs) -> m.APNAddr:
        try:
            apn_reg = await self.get_reg(api, tmpl.addr)
        except Exception:
            simid = tmpl.sim if tmpl.sim is not None else ea.SIMID("MISSING")
            apn_reg = await self.register(
                api,
                m.APNRegTmpl(addr=tmpl.addr, sim=simid),
            )
        return await self.assign(api, apn_reg, info)

    async def _verify_reg_addr(
        self, api: AsyncApi, addr: m.APNRegAddr, skip_comment: bool, fix: bool, hide_ok: bool
    ) -> m.APNRegAddr | None:
        if self.calc_offset(addr.ipv4addr) < 0:
            return None

        vlog = VerifyLog(title=f"{addr.ipv4addr}")

        #############
        # Comment
        #############
        if not skip_comment:
            if addr.comment is None:
                vlog.ok("Comment")
            else:
                vlog.error("Comment", f"Should be None [{addr.comment}]")
                if fix:
                    addr.comment = ""

        #############
        # Extattrs
        #############
        if addr.extattrs.sim is not None:
            vlog.ok("SIMID")
        else:
            vlog.error("SIMID", "Missing value", update=False)

        vlog.print(show_ok=not hide_ok)

        #############
        # Commit changes
        #############
        if fix and vlog.update:
            await api.update(addr)

        if vlog.is_ok:
            return addr
        else:
            return None

    async def _verify_addr(
        self,
        api: AsyncApi,
        addr: m.APNAddr,
        siteid: ea.SiteID,
        comment: str | None,
        skip_comment: bool,
        fix: bool,
        hide_ok: bool,
    ) -> m.APNAddr | None:
        if self.calc_offset(addr.ipv4addr) < 0:
            return None

        vlog = VerifyLog(title=f"{addr.ipv4addr}")

        #############
        # Comment
        #############
        if not skip_comment:
            if addr.comment == comment:
                vlog.ok("Comment")
            else:
                vlog.error("Comment", f"[{addr.comment}] -> [{comment}]")
                if fix:
                    addr.comment = comment

        #############
        # Extattrs
        #############
        if addr.extattrs.sim is not None:
            vlog.ok("SIMID")
        else:
            vlog.error("SIMID", "Missing value", update=False)

        if addr.extattrs.siteid == siteid:
            vlog.ok("SiteID")
        else:
            vlog.error("SiteID", f"SiteID {addr.extattrs.siteid} -> {siteid}")
            addr.extattrs.siteid = siteid

        vlog.print(show_ok=not hide_ok)

        #############
        # Commit changes
        #############
        if fix and vlog.update:
            await api.update(addr)

        if vlog.is_ok:
            return addr
        else:
            return None

    async def verify(
        self,
        api: AsyncApi,
        siteinfo: dict[ea.SiteID, m.SiteInfo],
        comments: dict[ea.SiteID, str],
        skip_comment: bool,
        fix: bool,
        hide_unused: bool,
        hide_ok: bool,
    ) -> None:
        PART = "APN"
        siteid_all_set = set(siteinfo.keys())

        print(f"\n{PART}: Getting info")
        registered_addrs = await self.get_registered_addrs(api)
        assigned_addrs = await self.get_addrs(api)

        assigned_addr_dct: dict[ea.SiteID, list[m.APNAddr]] = {}
        for addr in assigned_addrs:
            assigned_addr_dct.setdefault(addr.extattrs.siteid, []).append(addr)

        single_assigned_addr: dict[ea.SiteID, m.APNAddr] = {}
        multi_assigned_addr: dict[ea.SiteID, list[m.APNAddr]] = {}
        for siteid, addrs in assigned_addr_dct.items():
            siteid_all_set.remove(siteid)
            if len(addrs) > 1:
                multi_assigned_addr[siteid] = addrs
            else:
                single_assigned_addr[siteid] = addrs[0]

        tdata: list[list[Any]] = []
        tdata.append(["Registered Addrs", len(registered_addrs)])
        tdata.append(["Assigned Addrs", len(assigned_addrs)])

        print()
        print(tabulate(tdata, tablefmt="simple"))

        print(f"\n{PART}: SiteIDs without apn")

        for name, siteid in sorted(NameSiteid(s.value, s) for s in siteid_all_set):
            print(f"  - {name}")

        print(f"\n{PART}: Registered Addrs Validation")
        validated_reg_addrs: list[m.APNRegAddr] = []
        for reg_addr in registered_addrs:
            _reg_addr = await self._verify_reg_addr(api, reg_addr, skip_comment, fix, hide_ok)
            if _reg_addr is not None:
                validated_reg_addrs.append(_reg_addr)

        if not hide_unused:
            addr_table: list[list[str]] = []
            print(f"\n{PART}: Registered Addrs")
            headers = ["Addr", "SIMID"]

            v_addr_lines = [[str(addr.ipv4addr), str(addr.extattrs.sim)] for addr in validated_reg_addrs]
            addr_table.extend(v_addr_lines)
            if len(addr_table) > 0:
                print()
                print(tabulate(addr_table, headers=headers, tablefmt="outline"))

        print(f"\n{PART}: Assigned Addrs With Overlapping SiteIDs")
        for siteid, addrs in multi_assigned_addr.items():
            print(f" - {siteid}")
            for addr in addrs:
                print(f"   - {addr.network} - {addr.extattrs}")

        print(f"\n{PART}: Assigned Addrs Validation")
        validated_addrs: list[m.APNAddr] = []
        for siteid, addr in single_assigned_addr.items():
            _vaa_addr = await self._verify_addr(
                api,
                addr,
                siteid,
                comments[siteid],
                skip_comment=skip_comment,
                fix=fix,
                hide_ok=hide_ok,
            )
            if _vaa_addr is not None:
                validated_addrs.append(_vaa_addr)

        if not hide_unused:
            hu_addr_table: list[list[str]] = []
            print(f"\n{PART}: Assigned Addrs")
            headers = ["Addr", "SiteID", "SIMID"]

            for addr in validated_addrs:
                addr_line = [
                    str(addr.ipv4addr),
                    str(addr.extattrs.siteid),
                    str(addr.extattrs.sim),
                ]
                hu_addr_table.append(addr_line)
            if len(hu_addr_table) > 0:
                print()
                print(tabulate(hu_addr_table, headers=headers, tablefmt="outline"))


@dataclasses.dataclass(slots=True, kw_only=True)
class AsyncLoopScope(AsyncAddrScope):
    async def get(self, api: AsyncApi, oid: ea.SiteID | IPv4Address) -> m.LoopAddr:
        return await api.get_addr(self.net, oid, return_cls=m.LoopAddr)

    async def get_all(self, api: AsyncApi) -> dict[ea.SiteID, m.LoopAddr]:
        addrs = await api.get_addrs(ea.SiteID.is_not_null(), network=self.net, return_cls=m.LoopAddr)
        dct: dict[ea.SiteID, m.LoopAddr] = {a.extattrs.siteid: a for a in addrs}
        return dct

    async def get_addrs(self, api: AsyncApi) -> list[m.LoopAddr]:
        return await api.get_addrs(ea.SiteID.is_not_null(), network=self.net, return_cls=m.LoopAddr)

    async def create(
        self,
        api: AsyncApi,
        siteid: ea.SiteID,
        ipv4addr: int | IPv4Address | None,
        comment: str | None,
    ) -> ObjWOffset[m.LoopAddr]:
        addr = await api.create(
            m.NewLoopAddr(
                network=self.net,
                ipv4addr=self.calc_addr(ipv4addr),
                comment=comment,
                extattrs=m.LoopAddrAttrs(siteid=siteid),
            )
        )

        log.info(f"Allocate {siteid} {self.name} {addr.ipv4addr} {addr.comment}")

        return ObjWOffset(addr, self.calc_offset(addr.ipv4addr))

    async def filter(
        self, api: AsyncApi, *extattrs: SearchExtAttr, ipv4addr: IPv4Address | None = None
    ) -> list[m.LoopAddr]:
        if ipv4addr is not None:
            return await api.get_addrs(*extattrs, network=self.net, ipv4addr=ipv4addr, return_cls=m.LoopAddr)
        return await api.get_addrs(*extattrs, network=self.net, return_cls=m.LoopAddr)

    async def release(self, api: AsyncApi, addr: m.LoopAddr) -> None:
        await api.delete(addr)

    async def delete(self, api: AsyncApi, siteid: ea.SiteID) -> None:
        try:
            addrs = await api.get_addrs(siteid, network=self.net, return_cls=m.APNAddr)
            if len(addrs) > 5:
                raise Exception(f"to many addresses {addrs}")
            for addr in addrs:
                log.info(f"Deallocate {siteid} {self.name} {addr.ipv4addr}")
                await api.delete(addr)
        except Exception as e:
            log.error(e)

    async def _verify_addr(
        self,
        api: AsyncApi,
        addr: m.LoopAddr,
        siteid: ea.SiteID,
        comment: str | None,
        skip_comment: bool,
        fix: bool,
        hide_ok: bool,
    ) -> ObjWOffset[m.LoopAddr] | None:
        if self.calc_offset(addr.ipv4addr) < 0:
            return None

        vlog = VerifyLog(title=f"{addr.ipv4addr}")

        #############
        # Comment
        #############
        if not skip_comment:
            if addr.comment == comment:
                vlog.ok("Comment")
            else:
                vlog.error("Comment", f"[{addr.comment}] -> [{comment}]")
                if fix:
                    addr.comment = comment

        #############
        # Extattrs
        #############
        if addr.extattrs.siteid == siteid:
            vlog.ok("SiteID")
        else:
            vlog.error("SiteID", f"SiteID {addr.extattrs.siteid} -> {siteid}")
            addr.extattrs.siteid = siteid

        vlog.print(show_ok=not hide_ok)

        #############
        # Commit changes
        #############
        if fix and vlog.update:
            await api.update(addr)

        if vlog.is_ok:
            return ObjWOffset(addr, self.calc_offset(addr.ipv4addr))
        else:
            return None

    async def verify(
        self,
        api: AsyncApi,
        siteinfo: dict[ea.SiteID, m.SiteInfo],
        comments: dict[ea.SiteID, str],
        skip_comment: bool,
        fix: bool,
        hide_unused: bool,
        hide_ok: bool,
    ) -> ColWOffset[ea.NID]:
        PART = f"LOOP: {self.nid.value}"
        siteid_all_set = set(siteinfo.keys())

        print(f"\n{PART}: Getting info")
        unknown_addrs = await self._get_unknowns(api)
        assigned_addrs = await self.get_addrs(api)

        assigned_addr_dct: dict[ea.SiteID, list[m.LoopAddr]] = {}
        for addr in assigned_addrs:
            assigned_addr_dct.setdefault(addr.extattrs.siteid, []).append(addr)

        single_assigned_addr: dict[ea.SiteID, m.LoopAddr] = {}
        multi_assigned_addr: dict[ea.SiteID, list[m.LoopAddr]] = {}
        for siteid, addrs in assigned_addr_dct.items():
            siteid_all_set.remove(siteid)
            if len(addrs) > 1:
                multi_assigned_addr[siteid] = addrs
            else:
                single_assigned_addr[siteid] = addrs[0]

        tdata: list[list[Any]] = []
        tdata.append(["Unknown Addrs", len(unknown_addrs)])
        tdata.append(["Assigned Addrs", len(assigned_addrs)])

        print()
        print(tabulate(tdata, tablefmt="simple"))

        print(f"\n{PART}: SiteIDs without loop")
        for name, siteid in sorted(NameSiteid(s.value, s) for s in siteid_all_set):
            print(f"  - {name}")

        print(f"\n{PART}: Unknown Addrs")
        addr_table: list[list[str]] = []
        headers = ["Offset", "Addr"]

        uk_addr_lines = [
            [str(self.calc_offset(addr.ipv4addr)), str(addr.ipv4addr)]
            for addr in unknown_addrs
            if self.calc_offset(addr.ipv4addr) >= 0
        ]
        addr_table.extend(uk_addr_lines)
        if len(addr_table) > 0:
            print()
            print(tabulate(addr_table, headers=headers, tablefmt="outline"))

        print(f"\n{PART}: Assigned Addrs With Overlapping SiteIDs")
        for siteid, addrs in multi_assigned_addr.items():
            print(f" - {siteid}")
            for addr in addrs:
                print(f"   - {addr.network} - {addr.extattrs}")

        print(f"\n{PART}: Assigned Addrs Validation")
        validated_addrs: list[ObjWOffset[m.LoopAddr]] = []

        async def _assigned_addrs_validation() -> None:
            for siteid, addr in single_assigned_addr.items():
                _addr = await self._verify_addr(
                    api,
                    addr,
                    siteid,
                    comments[siteid],
                    skip_comment=skip_comment,
                    fix=fix,
                    hide_ok=hide_ok,
                )
                if _addr is not None:
                    validated_addrs.append(_addr)

        await _assigned_addrs_validation()
        if not hide_unused:
            u_addr_table: list[list[str]] = []
            print(f"\n{PART}: Assigned Addrs")
            headers = ["Offset", "Addr", "SiteID"]

            for addr, offset in validated_addrs:
                addr_line = [
                    str(offset),
                    str(addr.ipv4addr),
                    str(addr.extattrs.siteid),
                ]
                u_addr_table.append(addr_line)
            if len(u_addr_table) > 0:
                print()
                print(tabulate(u_addr_table, headers=headers, tablefmt="outline"))

        dct: dict[ea.SiteID, int] = {addr.extattrs.siteid: offset for addr, offset in validated_addrs}

        return ColWOffset(self.nid, dct)


@dataclasses.dataclass(slots=True, kw_only=True)
class AsyncLoopSet:
    lo0: AsyncLoopScope
    lo1: AsyncLoopScope
    lo2: AsyncLoopScope
    lo3: AsyncLoopScope
    lo4: AsyncLoopScope

    async def get_all(self, api: AsyncApi) -> dict[ea.SiteID, m.LoopSet]:
        async with tasklog.TaskGroup() as tg:
            t_lo0 = tg.create_task(self.lo0.get_all(api), "Getting Lo0")
            t_lo1 = tg.create_task(self.lo1.get_all(api), "Getting Lo1")
            t_lo2 = tg.create_task(self.lo2.get_all(api), "Getting Lo2")
            t_lo3 = tg.create_task(self.lo3.get_all(api), "Getting Lo3")
            t_lo4 = tg.create_task(self.lo4.get_all(api), "Getting Lo4")

        lo0 = t_lo0.result()
        lo1 = t_lo1.result()
        lo2 = t_lo2.result()
        lo3 = t_lo3.result()
        lo4 = t_lo4.result()

        dct: dict[ea.SiteID, m.LoopSet] = {}
        for siteid in lo0:
            try:
                dct[siteid] = m.LoopSet(
                    lo0=lo0[siteid],
                    lo1=lo1[siteid],
                    lo2=lo2[siteid],
                    lo3=lo3[siteid],
                    lo4=lo4[siteid],
                )
            except Exception:
                pass
        return dct

    async def get(self, api: AsyncApi, siteid: ea.SiteID) -> m.LoopSet:
        return m.LoopSet(
            lo0=await self.lo0.get(api, siteid),
            lo1=await self.lo1.get(api, siteid),
            lo2=await self.lo2.get(api, siteid),
            lo3=await self.lo3.get(api, siteid),
            lo4=await self.lo4.get(api, siteid),
        )

    async def release(self, api: AsyncApi, loops: m.LoopSet) -> None:
        await self.lo4.release(api, loops.lo4)
        await self.lo3.release(api, loops.lo3)
        await self.lo2.release(api, loops.lo2)
        await self.lo1.release(api, loops.lo1)
        await self.lo0.release(api, loops.lo0)

    async def delete(self, api: AsyncApi, siteid: ea.SiteID) -> None:
        await self.lo4.delete(api, siteid)
        await self.lo3.delete(api, siteid)
        await self.lo2.delete(api, siteid)
        await self.lo1.delete(api, siteid)
        await self.lo0.delete(api, siteid)

    async def create(self, api: AsyncApi, tmpl: m.LoopAddrTmpl, info: m.SiteInfoAttrs) -> m.LoopSet:
        siteid = info.siteid
        comment = info.as_comment

        lo0, offset = await self.lo0.create(api, siteid, tmpl, comment)
        lo1, _ = await self.lo1.create(api, siteid, offset, comment)
        lo2, _ = await self.lo2.create(api, siteid, offset, comment)
        lo3, _ = await self.lo3.create(api, siteid, offset, comment)
        lo4, _ = await self.lo4.create(api, siteid, offset, comment)

        return m.LoopSet(
            lo0=lo0,
            lo1=lo1,
            lo2=lo2,
            lo3=lo3,
            lo4=lo4,
        )

    async def verify(
        self,
        api: AsyncApi,
        infos: dict[ea.SiteID, m.SiteInfo],
        comments: dict[ea.SiteID, str],
        *,
        skip_comment: bool,
        fix: bool,
        hide_unused: bool,
        hide_ok: bool,
    ) -> None:
        PART = "LOOPS"

        lo_dcts = [
            await self.lo0.verify(api, infos, comments, skip_comment, fix, hide_unused, hide_ok),
            await self.lo1.verify(api, infos, comments, skip_comment, fix, hide_unused, hide_ok),
            await self.lo2.verify(api, infos, comments, skip_comment, fix, hide_unused, hide_ok),
            await self.lo3.verify(api, infos, comments, skip_comment, fix, hide_unused, hide_ok),
            await self.lo4.verify(api, infos, comments, skip_comment, fix, hide_unused, hide_ok),
        ]

        siteids: set[ea.SiteID] = set()
        for _, lo_dct in lo_dcts:
            siteids.update(lo_dct.keys())

        siteids_incorrect_loops: dict[ea.SiteID, list[ea.NID]] = {}
        siteids_incorrect_offset: dict[ea.SiteID, list[ObjWOffset[ea.NID]]] = {}
        valid_siteids = set(siteids)
        for siteid in siteids:
            offsets: list[ObjWOffset[ea.NID]] = []
            offset_count: set[int] = set()
            nids: list[ea.NID] = []
            for nid, lo_dct in lo_dcts:
                offset = lo_dct.get(siteid, None)
                if offset is not None:
                    offsets.append(ObjWOffset(nid, offset))
                    offset_count.add(offset)
                    nids.append(nid)
            if len(nids) != len(lo_dcts):
                siteids_incorrect_loops[siteid] = nids
                valid_siteids.discard(siteid)
            if len(offset_count) != 1:
                siteids_incorrect_offset[siteid] = offsets
                valid_siteids.discard(siteid)

        print(f"\n{PART}: SiteIDs with incorrect number loops")
        for siteid, loops in siteids_incorrect_loops.items():
            print(f"{siteid} [{loops}]")

        print(f"\n{PART}: SiteIDs with incorrect loop offset")
        for siteid, offsets in siteids_incorrect_offset.items():
            print(f"{siteid} [{offsets}]")

        print(f"\n{PART}: Total {len(valid_siteids)}")

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.startswith("t"):
            fields = dataclasses.fields(self)
            indent_str = __format_spec[1:]
            indent = int(indent_str) if len(indent_str) > 0 else 0
            ind = " " * (indent * 4)
            fieldstrs = [f"{ind}{field.name}:{getattr(self, field.name):t{indent+1}}" for field in fields]
            return "\n" + "\n".join(fieldstrs)

        return super().__format__(__format_spec)


@dataclasses.dataclass(slots=True, kw_only=True)
class AsyncIPAMScope:
    info: AsyncSiteInfoScope
    apn: AsyncAPNScope
    mpls: AsyncMPLSScope
    loops: AsyncLoopSet
    s60kV: AsyncVNetSet
    s10kV: AsyncVNetSet

    async def get_all(self, api: AsyncApi) -> dict[ea.SiteID, m.Site60kV]:
        async with tasklog.TaskGroup() as tg:
            t_info = tg.create_task(self.info.get_all(api), "Getting Info Addresses")
            t_apn = tg.create_task(self.apn.get_all(api), "Getting APN Addresses")
            t_mpls = tg.create_task(self.mpls.get_gnets(api), "Getting MPLS Nets")
            t_loops = tg.create_task(self.loops.get_all(api), "Getting Loop Addresses")
            t_s60kV = tg.create_task(self.s60kV.get_all(api), "Getting 60kV VNets")

        info = t_info.result()
        apn = t_apn.result()
        mpls = {n.net.extattrs.siteid: n for n in t_mpls.result()}
        loops = t_loops.result()
        s60kV = t_s60kV.result()

        dct: dict[ea.SiteID, m.Site60kV] = {}
        for siteid in info:
            try:
                dct[siteid] = m.Site60kV(
                    info=info[siteid],
                    loops=loops[siteid],
                    vnets=s60kV[siteid],
                    mpls=mpls.get(siteid, None),
                    apn=apn.get(siteid, None),
                )
            except Exception:
                pass
        return dct

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.startswith("t"):
            fields = dataclasses.fields(self)
            indent_str = __format_spec[1:]
            indent = int(indent_str) if len(indent_str) > 0 else 0
            ind = " " * (indent * 4)
            fieldstrs = [f"{ind}{field.name}:{getattr(self, field.name):t{indent+1}}" for field in fields]
            return "\n" + "\n".join(fieldstrs)

        return super().__format__(__format_spec)
