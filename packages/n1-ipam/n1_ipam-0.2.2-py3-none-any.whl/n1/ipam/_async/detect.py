import logging
from typing import TypeVar

from conscia.infoblox.infoblox_sdk.model import DHCPMember, Member, Network, NetworkContainer

import n1.ipam._async.scopes as scopes
import n1.ipam.extattr as ea
from n1.ipam import _config
from n1.ipam._api import AsyncApi

log = logging.getLogger(__name__)


def _dhcp_from_conf(config: _config.DHCPRange | None) -> scopes.DHCPRange | None:
    if config is None:
        return None
    return scopes.DHCPRange(
        start_offset=config.start_offset,
        end_offset=config.end_offset,
        lease=config.lease,
    )


async def _detect_dhcp_members(api: AsyncApi, dhcp_members: list[_config.DHCPMember], detect: bool) -> list[DHCPMember]:
    newmembers: list[DHCPMember] = []
    if len(dhcp_members) == 0:
        log.info("detecting dhcp members")
        for member in await api.get_members(Member):
            newmembers.append(member.as_dhcp_member())
        return newmembers
    if detect or any((x.ipv4 is None and x.ipv6 is None) for x in dhcp_members):
        members: dict[str, Member] = {}
        log.info("detecting dhcp members")
        for member in await api.get_members(Member):
            members[member.host_name] = member

        for dhcp_member in dhcp_members:
            if detect or (dhcp_member.ipv4 is None and dhcp_member.ipv6 is None):
                newmembers.append(members[dhcp_member.name].as_dhcp_member())
            else:
                newmembers.append(
                    DHCPMember(
                        name=dhcp_member.name,
                        ipv4_addr=dhcp_member.ipv4,
                        ipv6_addr=dhcp_member.ipv6,
                    )
                )
        return newmembers

    return [DHCPMember(name=s.name, ipv4_addr=s.ipv4, ipv6_addr=s.ipv6) for s in dhcp_members]


AddrScopeT = TypeVar("AddrScopeT", bound=scopes.AsyncAddrScope)


async def _detect_addr_scope(
    api: AsyncApi,
    scope: type[AddrScopeT],
    config: _config.AddrScope,
    detect: bool,
) -> AddrScopeT:
    if detect or config.net is None:
        log.info(f"detecting addr scope {config.nid}")
        net = await api.get_addrscope(config.nid, Network)
        network = net.network
    else:
        network = config.net
    return scope(nid=config.nid, comment=config.comment, net=network, skip=config.skip)


async def _detect_mpls_scope(
    api: AsyncApi,
    config: _config.NetScope,
    dhcp_members: list[DHCPMember],
    detect: bool,
) -> scopes.AsyncMPLSScope:
    dhcp_members = (
        dhcp_members
        if detect
        else [DHCPMember(name=s.name, ipv4_addr=s.ipv4, ipv6_addr=s.ipv6) for s in config.members]
    )
    if detect or config.net is None:
        log.info(f"detecting mpls scope {config.nid}")
        net = await api.get_netscope(config.nid, return_cls=NetworkContainer)
        network = net.network
    else:
        network = config.net

    return scopes.AsyncMPLSScope(
        nid=config.nid,
        net=network,
        prefix=config.prefix,
        gw=config.gw,
        members=dhcp_members,
        dhcp=_dhcp_from_conf(config.dhcp),
        comment=config.comment,
    )


async def _detect_vnet_scope(
    api: AsyncApi,
    config: _config.NetScope,
    st: ea.SiteType,
    dhcp_members: list[DHCPMember],
    detect: bool,
) -> scopes.AsyncVNetScope:
    dhcp_members = (
        dhcp_members
        if detect
        else [DHCPMember(name=s.name, ipv4_addr=s.ipv4, ipv6_addr=s.ipv6) for s in config.members]
    )
    if detect or config.net is None:
        log.info(f"detecting vnet scope {st} {config.nid}")
        net = await api.get_netscope(config.nid, st, return_cls=NetworkContainer)
        network = net.network
    else:
        network = config.net

    return scopes.AsyncVNetScope(
        nid=config.nid,
        net=network,
        prefix=config.prefix,
        gw=config.gw,
        members=dhcp_members,
        dhcp=_dhcp_from_conf(config.dhcp),
        comment=config.comment,
        st=st,
    )


async def _detect_vnet_scope_set(
    api: AsyncApi,
    config: _config.VNetScopes,
    st: ea.SiteType,
    dhcp_members: list[DHCPMember],
    detect: bool,
) -> scopes.AsyncVNetSet:
    return scopes.AsyncVNetSet(
        vn001=await _detect_vnet_scope(api, config.vn001, st, dhcp_members, detect=detect),
        vn002=await _detect_vnet_scope(api, config.vn002, st, dhcp_members, detect=detect),
        vn003=await _detect_vnet_scope(api, config.vn003, st, dhcp_members, detect=detect),
        vn004=await _detect_vnet_scope(api, config.vn004, st, dhcp_members, detect=detect),
        vn005=await _detect_vnet_scope(api, config.vn005, st, dhcp_members, detect=detect),
        vn006=await _detect_vnet_scope(api, config.vn006, st, dhcp_members, detect=detect),
        vn007=await _detect_vnet_scope(api, config.vn007, st, dhcp_members, detect=detect),
        vn008=await _detect_vnet_scope(api, config.vn008, st, dhcp_members, detect=detect),
    )


async def _detect_loop_scope_set(api: AsyncApi, config: _config.LoopScopes, detect: bool) -> scopes.AsyncLoopSet:
    return scopes.AsyncLoopSet(
        lo0=await _detect_addr_scope(api, scopes.AsyncLoopScope, config.lo0, detect=detect),
        lo1=await _detect_addr_scope(api, scopes.AsyncLoopScope, config.lo1, detect=detect),
        lo2=await _detect_addr_scope(api, scopes.AsyncLoopScope, config.lo2, detect=detect),
        lo3=await _detect_addr_scope(api, scopes.AsyncLoopScope, config.lo3, detect=detect),
        lo4=await _detect_addr_scope(api, scopes.AsyncLoopScope, config.lo4, detect=detect),
    )


async def detect_scopes(api: AsyncApi, config: _config.Config, detect: bool) -> scopes.AsyncIPAMScope:
    dhcp_members = await _detect_dhcp_members(api, config.dhcp_members, detect=detect)
    netscopes = config.netscopes
    addrscopes = config.addrscopes
    sitetypes = config.sitetypes

    return scopes.AsyncIPAMScope(
        info=await _detect_addr_scope(api, scopes.AsyncSiteInfoScope, addrscopes.info, detect=detect),
        apn=await _detect_addr_scope(api, scopes.AsyncAPNScope, addrscopes.apn, detect=detect),
        mpls=await _detect_mpls_scope(api, netscopes.mpls, dhcp_members, detect=detect),
        loops=await _detect_loop_scope_set(api, addrscopes.loops, detect=detect),
        s60kV=await _detect_vnet_scope_set(api, netscopes.s60kV, sitetypes.S60kV, dhcp_members, detect=detect),
        s10kV=await _detect_vnet_scope_set(api, netscopes.s10kV, sitetypes.S10kV, dhcp_members, detect=detect),
    )
