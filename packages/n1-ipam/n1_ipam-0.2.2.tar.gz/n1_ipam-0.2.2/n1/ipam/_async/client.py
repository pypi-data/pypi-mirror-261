import dataclasses
import logging
from ipaddress import IPv4Address, IPv4Network
from types import TracebackType
from typing import Literal, Self, overload

import conscia.infoblox.infoblox_sdk.model as ib_m
from conscia.infoblox.infoblox_sdk.model import SearchExtAttr

import n1.ipam.extattr as ea
from n1.ipam import _config
from n1.ipam import models as m
from n1.ipam._api import AsyncApi
from n1.ipam._async.detect import detect_scopes
from n1.ipam._scopes import AsyncIPAMScope

__version__ = "0.1.428"


log = logging.getLogger(__name__)


@dataclasses.dataclass(slots=True)
class AsyncClient:
    api: AsyncApi
    sitetypes: _config.SiteTypes
    scopes: AsyncIPAMScope

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        excinst: BaseException | None,
        exctb: TracebackType | None,
    ) -> Literal[False]:
        await self.close()
        return False

    async def close(self) -> None:
        await self.api.client.close()

    @classmethod
    async def load(cls, api: AsyncApi, config: _config.Config, detect: bool | None) -> Self:
        if detect is None:
            detect = True
        scopes = await detect_scopes(api, config, detect=detect)
        log.info(f"{scopes:t}")
        return cls(
            api=api,
            sitetypes=config.sitetypes,
            scopes=scopes,
        )

    async def get_siteids(self) -> ib_m.ExtAttrEnumDefT[ea.SiteID]:
        return await self.api.get_siteids()

    # region SiteInfo

    async def get_siteinfo(self, siteid: ea.SiteID) -> m.SiteInfo:
        return await self.scopes.info.get(self.api, siteid)

    async def get_siteinfos(self, *extattrs: SearchExtAttr) -> list[m.SiteInfo]:
        return await self.scopes.info.filter(self.api, *extattrs)

    async def create_siteinfo(self, tmpl: m.SiteInfoTmpl) -> m.SiteInfo:
        attrs = tmpl.as_infoattrs()
        await self.api.create_if_missing(attrs.siteid)
        await self.api.create_if_missing(attrs.street)
        await self.api.create_if_missing(attrs.city)
        await self.api.create_if_missing(attrs.postcode)

        return await self.scopes.info.create(self.api, tmpl.addr, attrs)

    async def delete_siteinfo(self, info: ea.SiteID | m.SiteInfo) -> None:
        await self.scopes.info.delete(self.api, info)

    async def delete_siteinfo_all(self, siteid: ea.SiteID, max: int | None = None) -> None:
        infos = await self.get_siteinfos(siteid)
        if max is not None and len(infos) > max:
            raise Exception("to many siteinfos to delete", infos)
        for info in infos:
            await self.delete_siteinfo(info)

    async def update_siteinfo(self, info: m.SiteInfo) -> m.SiteInfo:
        await self.api.create_if_missing(info.extattrs.siteid)
        await self.api.create_if_missing(info.extattrs.street)
        await self.api.create_if_missing(info.extattrs.city)
        await self.api.create_if_missing(info.extattrs.postcode)

        return await self.scopes.info.update(self.api, info)

    # endregion

    # region Siteinfo

    async def register_site(self, tmpl: m.SiteInfoTmpl) -> m.SiteInfo:
        await self.api.create_if_missing(tmpl.siteid)
        infos = await self.get_siteinfos(tmpl.siteid)
        if len(infos) > 0:
            raise Exception(f"site already registered {infos}")
        return await self.create_siteinfo(tmpl)

    async def deregister_site(self, siteid: ea.SiteID) -> None:
        await self.delete_siteinfo_all(siteid, max=5)

    # endregion

    # region MPLS

    async def register_mpls(self, tmpl: m.MPLSTmpl) -> m.MPLSRegGroup:
        net = self.scopes.mpls.calc_net(tmpl.net)
        if net.prefixlen != self.scopes.mpls.prefix:
            raise Exception(f"invalid prefix should be {self.scopes.mpls.prefix}")
        if not self.scopes.mpls.net.supernet_of(net):
            raise Exception(f"is not in mpls net {self.scopes.mpls.net}")
        try:
            mpls_net = await self.scopes.mpls.get_unknown_net(self.api, net)
        except Exception:
            pass
        else:
            raise Exception(f"net already exists {mpls_net}")
        await self.api.create_if_missing(tmpl.inst)
        await self.api.create_if_missing(tmpl.kreds)
        return await self.scopes.mpls.register(self.api, tmpl)

    async def assign_mpls(self, site: m.Site60kV | m.SiteInfo | ea.SiteID, net: IPv4Network | int) -> m.MPLSGroup:
        net = self.scopes.mpls.calc_net(net)
        match site:
            case m.Site60kV():
                info = site.info
            case m.SiteInfo():
                info = site
            case ea.SiteID():
                info = await self.get_siteinfo(site)
        mpls = await self.scopes.mpls.assign(self.api, net, info.extattrs)
        if isinstance(site, m.Site60kV):
            site.mpls = mpls
        return mpls

    # endregion

    # region Sites

    async def get_site(self, siteid: ea.SiteID) -> m.Site10kV | m.Site60kV:
        info = await self.get_siteinfo(siteid)
        log.info(info)
        match info.extattrs.sitetype:
            case self.sitetypes.S10kV:
                try:
                    apn = await self.scopes.apn.get(self.api, siteid)
                except Exception:
                    apn = None

                return m.Site10kV(
                    info=info,
                    loops=await self.scopes.loops.get(self.api, siteid),
                    vnets=await self.scopes.s10kV.get(self.api, siteid),
                    apn=apn,
                )
            case self.sitetypes.S60kV:
                mpls = await self.scopes.mpls.try_get_gnet(self.api, siteid)

                try:
                    apn = await self.scopes.apn.get(self.api, siteid)
                except Exception:
                    apn = None
                return m.Site60kV(
                    info=info,
                    loops=await self.scopes.loops.get(self.api, siteid),
                    vnets=await self.scopes.s60kV.get(self.api, siteid),
                    mpls=mpls,
                    apn=apn,
                )
            case _:
                raise Exception("no sites found")

    async def get_sites(self) -> dict[ea.SiteID, m.Site60kV]:
        return await self.scopes.get_all(self.api)

    async def _allocate_10kV(self, tmpl: m.Site10kVTmpl) -> m.Site10kV:
        infoattr = tmpl.info.as_infoattrs()

        await self.api.create_if_missing(infoattr.siteid)
        await self.api.create_if_missing(infoattr.street)
        await self.api.create_if_missing(infoattr.city)
        await self.api.create_if_missing(infoattr.postcode)
        if tmpl.apn is not None:
            await self.api.create_if_missing(tmpl.apn.sim)

        info = await self.create_siteinfo(tmpl.info)
        loops = await self.scopes.loops.create(self.api, tmpl.lo0, infoattr)
        vnets = await self.scopes.s10kV.create(self.api, tmpl.vn001, infoattr)
        apn = None if tmpl.apn is None else await self.scopes.apn.create_or_assign(self.api, tmpl.apn, infoattr)

        return m.Site10kV(
            info=info,
            loops=loops,
            apn=apn,
            vnets=vnets,
        )

    async def _deallocate_10kV(self, site: m.Site10kV) -> None:
        await self.scopes.loops.release(self.api, site.loops)
        await self.scopes.info.release(self.api, site.info)

    async def _allocate_60kV(self, tmpl: m.Site60kVTmpl) -> m.Site60kV:
        infoattr = tmpl.info.as_infoattrs()

        await self.api.create_if_missing(infoattr.siteid)
        await self.api.create_if_missing(infoattr.street)
        await self.api.create_if_missing(infoattr.city)
        await self.api.create_if_missing(infoattr.postcode)
        if tmpl.mpls is not None:
            await self.api.create_if_missing(tmpl.mpls.inst)
            await self.api.create_if_missing(tmpl.mpls.kreds)
        if tmpl.apn is not None:
            await self.api.create_if_missing(tmpl.apn.sim)

        info = await self.create_siteinfo(tmpl.info)
        loops = await self.scopes.loops.create(self.api, tmpl.lo0, infoattr)
        vnets = await self.scopes.s60kV.create(self.api, tmpl.vn001, infoattr)
        mpls = None if tmpl.mpls is None else await self.scopes.mpls.create_or_assign(self.api, tmpl.mpls, infoattr)
        apn = None if tmpl.apn is None else await self.scopes.apn.create_or_assign(self.api, tmpl.apn, infoattr)

        return m.Site60kV(
            info=info,
            loops=loops,
            vnets=vnets,
            mpls=mpls,
            apn=apn,
        )

    async def _deallocate_60kV(self, site: m.Site60kV) -> None:
        if site.apn is not None:
            await self.scopes.apn.release(self.api, site.apn)
        if site.mpls is not None:
            await self.scopes.mpls.release(self.api, site.mpls)

        await self.scopes.s60kV.release(self.api, site.vnets)
        await self.scopes.loops.release(self.api, site.loops)
        await self.scopes.info.release(self.api, site.info)

    @overload
    async def allocate(self, site: m.Site60kVTmpl) -> m.Site60kV:
        ...

    @overload
    async def allocate(self, site: m.Site10kVTmpl) -> m.Site10kV:
        ...

    async def allocate(self, site: m.Site60kVTmpl | m.Site10kVTmpl) -> m.Site10kV | m.Site60kV:
        match site:
            case m.Site60kVTmpl():
                return await self._allocate_60kV(site)
            case m.Site10kVTmpl():
                return await self._allocate_10kV(site)

        raise Exception("invalid site")

    async def deallocate(self, site: ea.SiteID | m.SiteInfo | m.Site60kV | m.Site10kV) -> None:
        match site:
            case m.Site60kV():
                await self._deallocate_60kV(site)
            case m.Site10kV():
                await self._deallocate_10kV(site)
            case ea.SiteID() as siteid:
                site = await self.get_site(siteid)
                await self.deallocate(site)
            case m.SiteInfo() as info:
                site = await self.get_site(info.extattrs.siteid)
                await self.deallocate(site)

    async def assign_apn(self, site: m.Site60kV | m.SiteInfo | ea.SiteID, tmpl: m.APNTmpl) -> m.APNAddr:
        match site:
            case m.Site60kV():
                info = site.info
            case m.SiteInfo():
                info = site
            case ea.SiteID():
                info = await self.get_siteinfo(site)
        apn = await self.scopes.apn.assign(self.api, tmpl.addr, info.extattrs)
        if isinstance(site, m.Site60kV):
            site.apn = apn
        return apn

    async def release_mpls(self, site: m.Site60kV | m.SiteInfo | ea.SiteID) -> None:
        match site:
            case m.Site60kV():
                mpls = site.mpls
            case m.SiteInfo():
                mpls = await self.scopes.mpls.try_get_gnet(self.api, site.extattrs.siteid)
            case ea.SiteID():
                mpls = await self.scopes.mpls.try_get_gnet(self.api, site)
        if mpls is None:
            return
        await self.scopes.mpls.release(self.api, mpls)
        if isinstance(site, m.Site60kV):
            site.mpls = None

    async def release_apn(self, site: m.Site60kV | m.Site10kV | m.SiteInfo | ea.SiteID) -> None:
        match site:
            case m.Site60kV() | m.Site10kV():
                apn = site.apn
            case m.SiteInfo():
                apn = await self.scopes.apn.try_get(self.api, site.extattrs.siteid)
            case ea.SiteID():
                apn = await self.scopes.apn.try_get(self.api, site)
        if apn is None:
            return
        await self.scopes.apn.release(self.api, apn)
        if isinstance(site, m.Site60kV):
            site.apn = None
        if isinstance(site, m.Site10kV):
            site.apn = None

    async def get_assigned_mpls_nets(self) -> list[m.MPLSGroup]:
        return await self.scopes.mpls.get_gnets(self.api)

    async def get_cities(self) -> ib_m.ExtAttrEnumDefT[ea.City]:
        return await self.api.client.get_extattrenumdef(ea.City)

    async def get_postcodes(self) -> ib_m.ExtAttrEnumDefT[ea.PostCode]:
        return await self.api.client.get_extattrenumdef(ea.PostCode)

    async def get_streets(self) -> ib_m.ExtAttrEnumDefT[ea.Street]:
        return await self.api.client.get_extattrenumdef(ea.Street)

    async def get_dkregions(self) -> ib_m.ExtAttrEnumDefT[ea.DKRegion]:
        return await self.api.client.get_extattrenumdef(ea.DKRegion)

    async def get_sitetypes(self) -> ib_m.ExtAttrEnumDefT[ea.SiteType]:
        return await self.api.client.get_extattrenumdef(ea.SiteType)

    async def find_siteid(self, ipv4_addr: IPv4Address) -> m.LoopAddr | None:
        if ipv4_addr in self.scopes.loops.lo0.net:
            return await self.scopes.loops.lo0.get(self.api, ipv4_addr)
        log.warning(f"cannot find {ipv4_addr}")
        return None

    # endregion

    async def verify(
        self,
        *,
        fix: bool,
        skip_loop: bool,
        skip_vnet: bool,
        skip_mpls: bool,
        skip_apn: bool,
        hide_unused: bool,
        hide_ok: bool,
        skip_comment: bool,
    ) -> None:
        siteids: ib_m.ExtAttrEnumDefT[ea.SiteID] = await self.api.get_siteids()

        siteinfos = await self.scopes.info.verify(self.api, siteids.get_all(), fix=fix)

        comments: dict[ea.SiteID, str] = {siteid: info.extattrs.as_comment for siteid, info in siteinfos.items()}

        if not skip_loop:
            await self.scopes.loops.verify(
                self.api,
                siteinfos,
                comments,
                skip_comment=skip_comment,
                fix=fix,
                hide_unused=hide_unused,
                hide_ok=hide_ok,
            )

        if not skip_vnet:
            await self.scopes.s60kV.verify(
                self.api,
                siteinfos,
                comments,
                skip_comment=skip_comment,
                fix=fix,
                hide_unused=hide_unused,
                hide_ok=hide_ok,
            )

        if not skip_mpls:
            await self.scopes.mpls.verify(
                self.api,
                siteinfos,
                skip_comment,
                fix,
                hide_unused,
                hide_ok=hide_ok,
            )

        if not skip_apn:
            await self.scopes.apn.verify(
                self.api,
                siteinfos,
                comments,
                skip_comment,
                fix,
                hide_unused,
                hide_ok=hide_ok,
            )
