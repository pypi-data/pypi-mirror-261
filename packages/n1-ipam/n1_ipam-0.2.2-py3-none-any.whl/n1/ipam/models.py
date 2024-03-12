from __future__ import annotations

import dataclasses
from ipaddress import IPv4Address, IPv4Interface, IPv4Network
from typing import Self, TypeAlias

import pydantic
from conscia.infoblox.infoblox_sdk.extattr import ExtAttrCollection
from conscia.infoblox.infoblox_sdk.model import (
    DHCPMember,
    FixedAddress,
    Network,
    NewFixedAddressBase,
    NewNetworkBase,
    NewRangeBase,
    OptionDHCPLeaseTime,
    OptionRouter,
    Options,
    Range,
)
from conscia.infoblox.infoblox_sdk.types import FailoverAssociation, ServerAssociationType

import n1.ipam.extattr as ea

# region Models

# region SiteInfo


@dataclasses.dataclass(slots=True)
class SiteInfoTmpl:
    siteid: ea.SiteID
    sitetype: ea.SiteType
    street: ea.Street | None = None
    city: ea.City | None = None
    postcode: ea.PostCode | None = None
    dkregion: ea.DKRegion | None = None
    addr: IPv4Address | None = None

    def as_infoattrs(self) -> SiteInfoAttrs:
        return SiteInfoAttrs(
            siteid=self.siteid,
            sitetype=self.sitetype,
            street=self.street,
            postcode=self.postcode,
            city=self.city,
            dkregion=self.dkregion,
        )


class SiteInfoAttrs(ExtAttrCollection):
    siteid: ea.SiteID
    sitetype: ea.SiteType
    street: ea.Street | None = None
    postcode: ea.PostCode | None = None
    city: ea.City | None = None
    dkregion: ea.DKRegion | None = None
    nid: ea.NID | None = None
    aid: ea.LoopID | None = None

    @property
    def address(self) -> str:
        street = "" if self.street is None else self.street.value
        postcode = "" if self.postcode is None else self.postcode.value
        city = "" if self.city is None else self.city.value
        return f"{street}, {postcode} {city}".strip()

    @property
    def as_comment(self) -> str:
        return f"{self.siteid.value} - {self.address}"


class SiteInfo(FixedAddress):
    comment: str | None = None
    extattrs: SiteInfoAttrs

    @property
    def as_comment(self) -> str:
        return self.extattrs.as_comment

    @property
    def dkregion(self) -> ea.DKRegion | None:
        return self.extattrs.dkregion

    @property
    def city(self) -> ea.City | None:
        return self.extattrs.city

    @property
    def siteid(self) -> ea.SiteID:
        return self.extattrs.siteid

    @property
    def sitetype(self) -> ea.SiteType:
        return self.extattrs.sitetype

    @property
    def street(self) -> ea.Street | None:
        return self.extattrs.street

    @property
    def postcode(self) -> ea.PostCode | None:
        return self.extattrs.postcode

    @property
    def address(self) -> str:
        return self.extattrs.address


class NewSiteInfo(NewFixedAddressBase[SiteInfo, SiteInfoAttrs]):
    pass


# endregion

# region LoopAddr

LoopAddrTmpl = IPv4Address | int | None


class LoopAddrAttrs(ExtAttrCollection):
    siteid: ea.SiteID
    nid: ea.NID | None = None


class LoopAddr(FixedAddress):
    network: IPv4Network
    comment: str | None = None
    extattrs: LoopAddrAttrs


class NewLoopAddr(NewFixedAddressBase[LoopAddr, LoopAddrAttrs]):
    pass


# endregion

# region VNet

VNetTmpl = IPv4Network | int | None


class VNetAttrs(ExtAttrCollection):
    siteid: ea.SiteID
    nid: ea.NID | None = None


class VNet(Network):
    network_container: IPv4Network = pydantic.Field(exclude=True)
    extattrs: VNetAttrs

    @property
    def router(self) -> OptionRouter | None:
        for opt in self.options:
            if isinstance(opt, OptionRouter):
                return opt
        return None

    @router.setter
    def router(self, value: OptionRouter | None) -> None:
        old = self.router
        if old is not None:
            self.options.remove(old)
        if value is not None:
            self.options.append(value)

    @property
    def lease(self) -> OptionDHCPLeaseTime | None:
        for opt in self.options:
            if isinstance(opt, OptionDHCPLeaseTime):
                return opt
        return None


class NewVNet(NewNetworkBase[VNet, VNetAttrs]):
    pass


class VNetRangeAttrs(ExtAttrCollection):
    siteid: ea.SiteID
    nid: ea.NID | None = None


class VNetRange(Range):
    member: DHCPMember | None = None
    options: list[Options] = pydantic.Field(default_factory=list)
    server_association_type: ServerAssociationType = ServerAssociationType.NONE
    failover_association: FailoverAssociation | None = None
    extattrs: VNetRangeAttrs


class NewVNetRange(NewRangeBase[VNetRange, VNetRangeAttrs]):
    @classmethod
    def prepare(
        cls,
        siteid: ea.SiteID,
        comment: str | None,
        net: IPv4Network,
        start_offset: int,
        end_offset: int,
    ) -> Self:
        return cls(
            comment=comment,
            start_addr=(net.network_address + 1 + start_offset),
            end_addr=(net.broadcast_address - 1 - end_offset),
            server_association_type=ServerAssociationType.FAILOVER,
            failover_association=FailoverAssociation.FAILOVER,
            extattrs=VNetRangeAttrs(siteid=siteid),
        )


@dataclasses.dataclass(slots=True)
class VNetGroup:
    net: VNet
    dhcp: VNetRange | None = None


class VNetUnknownRangeAttrs(ExtAttrCollection):
    siteid: ea.SiteID | None = None
    nid: ea.NID | None = None

    def assign(self, info: SiteInfo | SiteInfoAttrs) -> VNetRangeAttrs:
        return self.as_obj(assign=info)

    def as_obj(self, *, assign: SiteInfo | SiteInfoAttrs | None = None) -> VNetRangeAttrs:
        if assign is not None:
            return VNetRangeAttrs(siteid=assign.siteid, nid=self.nid)
        if self.siteid is None:
            raise Exception("siteid is None")
        return VNetRangeAttrs(siteid=self.siteid, nid=self.nid)


class VNetUnknownRange(Range):
    member: DHCPMember | None = None
    options: list[Options] = pydantic.Field(default_factory=list)
    server_association_type: ServerAssociationType = ServerAssociationType.NONE
    failover_association: FailoverAssociation | None = None
    extattrs: VNetUnknownRangeAttrs

    def assign(self, info: SiteInfo | SiteInfoAttrs) -> VNetRange:
        return self.as_obj(assign=info)

    def as_obj(self, *, assign: SiteInfo | SiteInfoAttrs | None = None) -> VNetRange:
        return VNetRange(
            ref=self.ref,
            comment=self.comment if assign is None else assign.as_comment,
            start_addr=self.start_addr,
            end_addr=self.end_addr,
            network=self.network,
            network_view=self.network_view,
            server_association_type=self.server_association_type,
            failover_association=self.failover_association,
            options=self.options,
            member=self.member,
            extattrs=self.extattrs.as_obj(assign=assign),
        )


class VNetUnknownAttrs(ExtAttrCollection):
    siteid: ea.SiteID | None = None
    nid: ea.NID | None = None

    def assign(self, info: SiteInfo | SiteInfoAttrs) -> VNetAttrs:
        return self.as_obj(assign=info)

    def as_obj(self, *, assign: SiteInfo | SiteInfoAttrs | None = None) -> VNetAttrs:
        if assign is not None:
            return VNetAttrs(siteid=assign.siteid, nid=self.nid)
        if self.siteid is None:
            raise Exception("siteid is None")
        return VNetAttrs(siteid=self.siteid, nid=self.nid)


class VNetUnknown(Network):
    network_container: IPv4Network = pydantic.Field(exclude=True)
    extattrs: VNetUnknownAttrs

    def assign(self, info: SiteInfo | SiteInfoAttrs) -> VNet:
        return self.as_obj(assign=info)

    def as_obj(self, *, assign: SiteInfo | SiteInfoAttrs | None = None) -> VNet:
        return VNet(
            ref=self.ref,
            network=self.network,
            network_view=self.network_view,
            network_container=self.network_container,
            comment=self.comment if assign is None else assign.as_comment,
            options=self.options,
            members=self.members,
            extattrs=self.extattrs.as_obj(assign=assign),
        )


# endregion

# region MPLS

# region MPLS Base


@dataclasses.dataclass(slots=True)
class MPLSTmpl:
    net: IPv4Network | int
    kreds: ea.ISPKreds | None = None
    inst: ea.ISPInst | None = None


class MPLSNetAttrs(ExtAttrCollection):
    siteid: ea.SiteID
    kreds: ea.ISPKreds | None = None
    inst: ea.ISPInst | None = None

    def as_reg(self, *, release: bool = False) -> MPLSRegNetAttrs:
        return MPLSRegNetAttrs(
            siteid=None if release else self.siteid,
            kreds=self.kreds,
            inst=self.inst,
        )

    def release(self) -> MPLSRegNetAttrs:
        return self.as_reg(release=True)


class MPLSRegNetAttrs(ExtAttrCollection):
    siteid: ea.SiteID | None = None
    kreds: ea.ISPKreds | None = None
    inst: ea.ISPInst | None = None

    def assign(self, info: SiteInfo | SiteInfoAttrs) -> MPLSNetAttrs:
        return self.as_obj(info)

    def as_obj(self, assign: SiteInfo | SiteInfoAttrs | None = None) -> MPLSNetAttrs:
        if assign is not None:
            return MPLSNetAttrs(siteid=assign.siteid, kreds=self.kreds, inst=self.inst)
        if self.siteid is None:
            raise Exception("siteid is None")
        return MPLSNetAttrs(siteid=self.siteid, kreds=self.kreds, inst=self.inst)


class MPLSNet(Network):
    network_container: IPv4Network = pydantic.Field(exclude=True)
    extattrs: MPLSNetAttrs

    @property
    def siteid(self) -> ea.SiteID:
        return self.extattrs.siteid

    @property
    def kreds(self) -> ea.ISPKreds | None:
        return self.extattrs.kreds

    @property
    def inst(self) -> ea.ISPInst | None:
        return self.extattrs.inst

    @property
    def router(self) -> OptionRouter | None:
        for opt in self.options:
            if isinstance(opt, OptionRouter):
                return opt
        return None

    @router.setter
    def router(self, value: OptionRouter | None) -> None:
        old = self.router
        if old is not None:
            self.options.remove(old)
        if value is not None:
            self.options.append(value)

    @property
    def lease(self) -> OptionDHCPLeaseTime | None:
        for opt in self.options:
            if isinstance(opt, OptionDHCPLeaseTime):
                return opt
        return None

    def release(self) -> MPLSRegNet:
        return self.as_reg(release=True)

    def as_reg(self, *, release: bool = False) -> MPLSRegNet:
        return MPLSRegNet(
            ref=self.ref,
            network=self.network,
            network_view=self.network_view,
            network_container=self.network_container,
            comment="" if release else self.comment,
            options=self.options,
            members=self.members,
            extattrs=self.extattrs.as_reg(release=release),
        )


class MPLSRegNet(Network):
    network_container: IPv4Network = pydantic.Field(exclude=True)
    extattrs: MPLSRegNetAttrs

    @property
    def router(self) -> OptionRouter | None:
        for opt in self.options:
            if isinstance(opt, OptionRouter):
                return opt
        return None

    @router.setter
    def router(self, value: OptionRouter | None) -> None:
        old = self.router
        if old is not None:
            self.options.remove(old)
        if value is not None:
            self.options.append(value)

    @property
    def lease(self) -> OptionDHCPLeaseTime | None:
        for opt in self.options:
            if isinstance(opt, OptionDHCPLeaseTime):
                return opt
        return None

    def assign(self, info: SiteInfo | SiteInfoAttrs) -> MPLSNet:
        return self.as_obj(info)

    def as_obj(self, assign: SiteInfo | SiteInfoAttrs | None = None) -> MPLSNet:
        return MPLSNet(
            ref=self.ref,
            network_view=self.network_view,
            network=self.network,
            network_container=self.network_container,
            comment=self.comment if assign is None else assign.as_comment,
            options=self.options,
            members=self.members,
            extattrs=self.extattrs.as_obj(assign),
        )


class MPLSRegRangeAttrs(ExtAttrCollection):
    siteid: ea.SiteID | None = None
    nid: ea.NID | None = None

    def assign(self, info: SiteInfo | SiteInfoAttrs) -> MPLSRangeAttrs:
        return self.as_obj(info)

    def as_obj(self, assign: SiteInfo | SiteInfoAttrs | None = None) -> MPLSRangeAttrs:
        if assign is not None:
            return MPLSRangeAttrs(siteid=assign.siteid, nid=self.nid)

        if self.siteid is None:
            raise Exception("siteid is None")
        return MPLSRangeAttrs(siteid=self.siteid, nid=self.nid)


class MPLSRegRange(Range):
    member: DHCPMember | None = None
    options: list[Options] = pydantic.Field(default_factory=list)
    server_association_type: ServerAssociationType = ServerAssociationType.NONE
    failover_association: FailoverAssociation | None = None
    extattrs: MPLSRegRangeAttrs

    def assign(self, info: SiteInfo | SiteInfoAttrs) -> MPLSRange:
        return self.as_obj(info)

    def as_obj(self, assign: SiteInfo | SiteInfoAttrs | None = None) -> MPLSRange:
        return MPLSRange(
            comment=self.comment if assign is None else assign.as_comment,
            ref=self.ref,
            start_addr=self.start_addr,
            end_addr=self.end_addr,
            network=self.network,
            network_view=self.network_view,
            server_association_type=self.server_association_type,
            failover_association=self.failover_association,
            options=self.options,
            member=self.member,
            extattrs=self.extattrs.as_obj(assign),
        )


@dataclasses.dataclass(slots=True, kw_only=True)
class MPLSRegGroup:
    net: MPLSRegNet
    dhcp: MPLSRegRange | None

    def as_obj(self, assign: SiteInfo | SiteInfoAttrs | None = None) -> MPLSGroup:
        return MPLSGroup(
            net=self.net.as_obj(assign),
            dhcp=None if self.dhcp is None else self.dhcp.as_obj(assign),
        )

    def assign(self, info: SiteInfo | SiteInfoAttrs) -> MPLSGroup:
        return self.as_obj(info)


class MPLSRangeAttrs(ExtAttrCollection):
    siteid: ea.SiteID
    nid: ea.NID | None = None

    def as_reg(self, *, release: bool) -> MPLSRegRangeAttrs:
        return MPLSRegRangeAttrs(
            siteid=None if release else self.siteid,
            nid=self.nid,
        )

    def release(self) -> MPLSRegRangeAttrs:
        return self.as_reg(release=True)


class MPLSRange(Range):
    member: DHCPMember | None = None
    options: list[Options] = pydantic.Field(default_factory=list)
    server_association_type: ServerAssociationType = ServerAssociationType.NONE
    failover_association: FailoverAssociation | None = None
    extattrs: MPLSRangeAttrs

    def as_reg(self, *, release: bool = False) -> MPLSRegRange:
        return MPLSRegRange(
            ref=self.ref,
            comment="" if release else self.comment,
            start_addr=self.start_addr,
            end_addr=self.end_addr,
            network=self.network,
            network_view=self.network_view,
            server_association_type=self.server_association_type,
            failover_association=self.failover_association,
            options=self.options,
            member=self.member,
            extattrs=self.extattrs.as_reg(release=release),
        )

    def release(self) -> MPLSRegRange:
        return self.as_reg(release=True)


class NewMPLSRegRange(NewRangeBase[MPLSRegRange, MPLSRegRangeAttrs]):
    def assign(self, info: SiteInfo | SiteInfoAttrs) -> NewMPLSRange:
        return self.as_obj(info)

    def as_obj(self, assign: SiteInfo | SiteInfoAttrs | None = None) -> NewMPLSRange:
        return NewMPLSRange(
            start_addr=self.start_addr,
            end_addr=self.end_addr,
            network_view=self.network_view,
            comment=self.comment if assign is None else assign.as_comment,
            server_association_type=self.server_association_type,
            failover_association=self.failover_association,
            extattrs=self.extattrs.as_obj(assign),
        )


class NewMPLSRange(NewRangeBase[MPLSRange, MPLSRangeAttrs]):
    pass


class NewMPLSRegNet(NewNetworkBase[MPLSRegNet, MPLSRegNetAttrs]):
    def assign(self, info: SiteInfo | SiteInfoAttrs) -> NewMPLSNet:
        return self.as_obj(info)

    def as_obj(self, assign: SiteInfo | SiteInfoAttrs | None = None) -> NewMPLSNet:
        return NewMPLSNet(
            network=self.network,
            comment=self.comment if assign is None else assign.as_comment,
            network_view=self.network_view,
            options=self.options,
            members=self.members,
            extattrs=self.extattrs.as_obj(assign),
        )


class NewMPLSNet(NewNetworkBase[MPLSNet, MPLSNetAttrs]):
    network_view: str | None = None


@dataclasses.dataclass(slots=True, kw_only=True)
class NewMPLSRegGroup:
    net: NewMPLSRegNet
    dhcp: NewMPLSRegRange | None

    def as_obj(self, assign: SiteInfo | SiteInfoAttrs | None = None) -> NewMPLSGroup:
        return NewMPLSGroup(
            net=self.net.as_obj(assign),
            dhcp=None if self.dhcp is None else self.dhcp.as_obj(assign),
        )

    def assign(self, info: SiteInfo | SiteInfoAttrs) -> NewMPLSGroup:
        return self.as_obj(info)


@dataclasses.dataclass(slots=True, kw_only=True)
class NewMPLSGroup:
    net: NewMPLSNet
    dhcp: NewMPLSRange | None


@dataclasses.dataclass(slots=True, kw_only=True)
class MPLSGroup:
    net: MPLSNet
    dhcp: MPLSRange | None

    def as_reg(self, *, release: bool = False) -> MPLSRegGroup:
        return MPLSRegGroup(
            net=self.net.as_reg(release=release),
            dhcp=None if self.dhcp is None else self.dhcp.as_reg(release=release),
        )

    def release(self) -> MPLSRegGroup:
        return self.as_reg(release=True)


# endregion


# endregion

# region APN

# region APN Base


@dataclasses.dataclass(slots=True)
class APNTmpl:
    addr: IPv4Address | int
    sim: ea.SIMID | None = None


class APNAttrs(ExtAttrCollection):
    siteid: ea.SiteID
    sim: ea.SIMID | None = None

    def release(self) -> APNRegAttrs:
        return self.as_reg(release=True)

    def as_reg(self, *, release: bool = False) -> APNRegAttrs:
        return APNRegAttrs(
            siteid=None if release else self.siteid,
            sim=self.sim,
        )


class APNAddr(FixedAddress):
    comment: str | None = None
    mac: str
    network: IPv4Network
    network_view: str
    options: list[Options] = pydantic.Field(default_factory=list)
    extattrs: APNAttrs

    @property
    def siteid(self) -> ea.SiteID:
        return self.extattrs.siteid

    @property
    def sim(self) -> ea.SIMID | None:
        return self.extattrs.sim

    def release(self) -> APNRegAddr:
        return self.as_reg(release=True)

    def as_reg(self, *, release: bool = False) -> APNRegAddr:
        return APNRegAddr(
            ref=self.ref,
            ipv4addr=self.ipv4addr,
            mac=self.mac,
            comment="" if release else self.comment,
            network=self.network,
            network_view=self.network_view,
            options=self.options,
            extattrs=self.extattrs.as_reg(release=release),
        )


class NewAPN(NewFixedAddressBase[APNAddr, APNAttrs]):
    pass


@dataclasses.dataclass(slots=True)
class APNRegTmpl:
    addr: IPv4Address | int
    sim: ea.SIMID | None = None


class APNRegAttrs(ExtAttrCollection):
    siteid: ea.SiteID | None = None
    sim: ea.SIMID | None = None

    def assign(self, siteid: ea.SiteID) -> APNAttrs:
        return APNAttrs(siteid=siteid, sim=self.sim)

    def as_obj(self) -> APNAttrs:
        if self.siteid is None:
            raise Exception("siteid is none")
        return APNAttrs(
            siteid=self.siteid,
            sim=self.sim,
        )


class APNRegAddr(FixedAddress):
    mac: str
    comment: str | None = None
    network: IPv4Network
    network_view: str
    options: list[Options] = pydantic.Field(default_factory=list)
    extattrs: APNRegAttrs

    def assign(self, siteid: ea.SiteID, comment: str | None) -> APNAddr:
        return APNAddr(
            ref=self.ref,
            ipv4addr=self.ipv4addr,
            mac=self.mac,
            comment=comment,
            network=self.network,
            network_view=self.network_view,
            options=self.options,
            extattrs=self.extattrs.assign(siteid),
        )

    def as_obj(self) -> APNAddr:
        extattrs = self.extattrs.as_obj()
        return APNAddr(
            ref=self.ref,
            ipv4addr=self.ipv4addr,
            mac=self.mac,
            comment=self.comment,
            network=self.network,
            network_view=self.network_view,
            options=self.options,
            extattrs=extattrs,
        )


class NewAPNReg(NewFixedAddressBase[APNRegAddr, APNRegAttrs]):
    pass


# endregion


# endregion


# endregion


@dataclasses.dataclass(slots=True)
class LoopSet:
    lo0: LoopAddr
    lo1: LoopAddr
    lo2: LoopAddr
    lo3: LoopAddr
    lo4: LoopAddr


@dataclasses.dataclass(slots=True)
class VNetSet:
    vn001: VNetGroup
    vn002: VNetGroup
    vn003: VNetGroup
    vn004: VNetGroup
    vn005: VNetGroup
    vn006: VNetGroup
    vn007: VNetGroup
    vn008: VNetGroup


@dataclasses.dataclass(kw_only=True, slots=True)
class Router60kV:
    site_id: ea.SiteID
    lo0: IPv4Interface
    lo1: IPv4Interface
    lo2: IPv4Interface
    lo3: IPv4Interface
    lo4: IPv4Interface
    vlan10: IPv4Interface
    vlan20: IPv4Interface
    vlan30: IPv4Interface
    vlan40: IPv4Interface
    vlan50: IPv4Interface
    vlan60: IPv4Interface
    vlan70: IPv4Interface
    vlan80: IPv4Interface
    idx: int = 1
    info: SiteInfo

    @property
    def mgmt_ip(self) -> IPv4Address:
        return self.lo0.ip

    @property
    def hostname(self) -> str:
        return f"XF{self.idx}-RO-{self.site_id.value}"


@dataclasses.dataclass(kw_only=True, slots=True)
class Router10kV:
    site_id: ea.SiteID
    lo0: IPv4Interface
    lo1: IPv4Interface
    lo2: IPv4Interface
    lo3: IPv4Interface
    lo4: IPv4Interface
    vlan10: IPv4Interface
    vlan20: IPv4Interface
    vlan30: IPv4Interface
    vlan40: IPv4Interface
    vlan50: IPv4Interface
    vlan60: IPv4Interface
    vlan70: IPv4Interface
    vlan80: IPv4Interface
    idx: int = 1
    info: SiteInfo

    @property
    def mgmt_ip(self) -> IPv4Address:
        return self.lo0.ip

    @property
    def hostname(self) -> str:
        return f"XF{self.idx}-RO-{self.site_id.value}"


@dataclasses.dataclass(kw_only=True, slots=True)
class Switch60kV:
    idx: int
    site_id: ea.SiteID
    vlan10: IPv4Interface
    vlan10_gw: IPv4Address
    info: SiteInfo

    @property
    def mgmt_ip(self) -> IPv4Address:
        return self.vlan10.ip

    @property
    def hostname(self) -> str:
        return f"XF{self.idx}-SW-{self.site_id.value}"


@dataclasses.dataclass(kw_only=True, slots=True)
class Switch10kV:
    idx: int
    site_id: ea.SiteID
    vlan10: IPv4Interface
    vlan10_gw: IPv4Address
    info: SiteInfo

    @property
    def mgmt_ip(self) -> IPv4Address:
        return self.vlan10.ip

    @property
    def hostname(self) -> str:
        return f"XF{self.idx}-SW-{self.site_id.value}"


@dataclasses.dataclass(slots=True)
class Site10kVTmpl:
    info: SiteInfoTmpl
    apn: APNTmpl | None = None
    lo0: LoopAddrTmpl | None = None
    vn001: VNetTmpl | None = None


@dataclasses.dataclass(slots=True)
class Site60kVTmpl:
    info: SiteInfoTmpl
    lo0: LoopAddrTmpl = None
    vn001: VNetTmpl = None
    mpls: MPLSTmpl | None = None
    apn: APNTmpl | None = None

    @property
    def siteid(self) -> ea.SiteID:
        return self.info.siteid


def make_iface(netw: IPv4Network, idx: int) -> IPv4Interface:
    return IPv4Interface(f"{netw[idx]}/{netw.prefixlen}")


@dataclasses.dataclass(slots=True)
class Site60kV:
    info: SiteInfo
    loops: LoopSet
    vnets: VNetSet
    mpls: MPLSGroup | None
    apn: APNAddr | None

    @property
    def dkregion(self) -> ea.DKRegion | None:
        return self.info.dkregion

    @property
    def city(self) -> ea.City | None:
        return self.info.city

    @property
    def siteid(self) -> ea.SiteID:
        return self.info.siteid

    @property
    def sitetype(self) -> ea.SiteType:
        return self.info.sitetype

    @property
    def street(self) -> ea.Street | None:
        return self.info.street

    @property
    def postcode(self) -> ea.PostCode | None:
        return self.info.postcode

    @property
    def address(self) -> str:
        return self.info.address

    @property
    def mpls_net(self) -> MPLSNet | None:
        if self.mpls is None:
            return None
        return self.mpls.net

    @property
    def apn_addr(self) -> IPv4Address | None:
        if self.apn is None:
            return None
        return self.apn.ipv4addr

    def contains_ip(self, addr: IPv4Address) -> bool:
        if self.mpls is not None and addr in self.mpls.net.network:
            return True

        if self.apn is not None and addr == self.apn.ipv4addr:
            return True

        if self.info.ipv4addr == addr:
            return True

        if addr in [
            self.loops.lo0.ipv4addr,
            self.loops.lo1.ipv4addr,
            self.loops.lo2.ipv4addr,
            self.loops.lo3.ipv4addr,
            self.loops.lo4.ipv4addr,
        ]:
            return True

        nets = (
            self.vnets.vn001.net.network,
            self.vnets.vn002.net.network,
            self.vnets.vn003.net.network,
            self.vnets.vn004.net.network,
            self.vnets.vn005.net.network,
            self.vnets.vn006.net.network,
            self.vnets.vn007.net.network,
            self.vnets.vn008.net.network,
        )

        return any(addr in net for net in nets)

    def get_router(self) -> Router60kV:
        return Router60kV(
            site_id=self.info.extattrs.siteid,
            lo0=IPv4Interface(f"{self.loops.lo0.ipv4addr}/32"),
            lo1=IPv4Interface(f"{self.loops.lo1.ipv4addr}/32"),
            lo2=IPv4Interface(f"{self.loops.lo2.ipv4addr}/32"),
            lo3=IPv4Interface(f"{self.loops.lo3.ipv4addr}/32"),
            lo4=IPv4Interface(f"{self.loops.lo4.ipv4addr}/32"),
            vlan10=make_iface(self.vnets.vn001.net.network, 1),
            vlan20=make_iface(self.vnets.vn002.net.network, 1),
            vlan30=make_iface(self.vnets.vn003.net.network, 1),
            vlan40=make_iface(self.vnets.vn004.net.network, 1),
            vlan50=make_iface(self.vnets.vn005.net.network, 1),
            vlan60=make_iface(self.vnets.vn006.net.network, 1),
            vlan70=make_iface(self.vnets.vn007.net.network, 1),
            vlan80=make_iface(self.vnets.vn008.net.network, 1),
            info=self.info,
        )

    def get_switch(self, idx: int) -> Switch60kV:
        if self.vnets.vn001.net.router is None:
            raise Exception("missing router")
        return Switch60kV(
            idx=idx,
            site_id=self.info.extattrs.siteid,
            vlan10=make_iface(self.vnets.vn001.net.network, 1 + idx),
            vlan10_gw=self.vnets.vn001.net.router.value,
            info=self.info,
        )


@dataclasses.dataclass(slots=True)
class Site10kV:
    info: SiteInfo
    loops: LoopSet
    vnets: VNetSet
    apn: APNAddr | None

    def get_router(self) -> Router10kV:
        return Router10kV(
            site_id=self.info.extattrs.siteid,
            lo0=IPv4Interface(f"{self.loops.lo0.ipv4addr}/32"),
            lo1=IPv4Interface(f"{self.loops.lo1.ipv4addr}/32"),
            lo2=IPv4Interface(f"{self.loops.lo2.ipv4addr}/32"),
            lo3=IPv4Interface(f"{self.loops.lo3.ipv4addr}/32"),
            lo4=IPv4Interface(f"{self.loops.lo4.ipv4addr}/32"),
            vlan10=make_iface(self.vnets.vn001.net.network, 1),
            vlan20=make_iface(self.vnets.vn002.net.network, 1),
            vlan30=make_iface(self.vnets.vn003.net.network, 1),
            vlan40=make_iface(self.vnets.vn004.net.network, 1),
            vlan50=make_iface(self.vnets.vn005.net.network, 1),
            vlan60=make_iface(self.vnets.vn006.net.network, 1),
            vlan70=make_iface(self.vnets.vn007.net.network, 1),
            vlan80=make_iface(self.vnets.vn008.net.network, 1),
            info=self.info,
        )

    def get_switch(self, idx: int) -> Switch10kV:
        if self.vnets.vn001.net.router is None:
            raise Exception("missing router")
        return Switch10kV(
            idx=idx,
            site_id=self.info.extattrs.siteid,
            vlan10=make_iface(self.vnets.vn001.net.network, 1 + idx),
            vlan10_gw=self.vnets.vn001.net.router.value,
            info=self.info,
        )


Site: TypeAlias = Site10kV | Site60kV
Switch: TypeAlias = Switch10kV | Switch60kV
Router: TypeAlias = Router10kV | Router60kV
