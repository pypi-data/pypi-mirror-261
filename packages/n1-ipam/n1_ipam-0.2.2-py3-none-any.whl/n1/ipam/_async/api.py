import dataclasses
import logging
from ipaddress import IPv4Address, IPv4Network
from typing import Any, Unpack, overload

import conscia.infoblox.infoblox_sdk.model as _m
from conscia.infoblox.infoblox_sdk import AsyncClient
from conscia.infoblox.infoblox_sdk.extattr import ExtAttrBase
from conscia.infoblox.infoblox_sdk.model import SearchExtAttr
from typing_extensions import TypeVar

import n1.ipam.extattr as ea

T = TypeVar("T")

log = logging.getLogger(__name__)


def one_or_raise[T](objs: list[T]) -> T:
    if len(objs) != 1:
        raise ValueError(f"Expected 1 object, got {len(objs)}")
    return objs[0]


@dataclasses.dataclass(slots=True)
class AsyncApi:
    client: AsyncClient

    # Base
    async def create[T: _m.BaseRefModel[Any]](self, obj: _m.BaseNewModel[T]) -> T:
        return await self.client.create(obj)

    async def update[T: _m.BaseRefModel[Any]](self, obj: T) -> T:
        return await self.client.update(obj)

    async def delete(self, obj: _m.BaseRefModel[Any]) -> None:
        await self.client.delete(obj)

    # ExtAttrs

    @overload
    async def create_if_missing(self, extattr: None) -> None:
        ...

    @overload
    async def create_if_missing[
        T: ExtAttrBase[str]  # type: ignore[valid-type]
    ](self, extattr: T) -> _m.ExtAttrEnumDefT[T]:
        ...

    async def create_if_missing[
        T: ExtAttrBase[str]  # type: ignore[valid-type]
    ](self, extattr: T | None) -> _m.ExtAttrEnumDefT[T] | None:
        if extattr is None:
            return None

        extdef = await self.client.get_extattrenumdef(type(extattr))
        if not extdef.contains(extattr):
            extdef.add(extattr)
            log.info(f"adding [{extattr}]")
            extdef = await self.client.update(extdef)

        return extdef

    async def get_siteids(self) -> _m.ExtAttrEnumDefT[ea.SiteID]:
        return await self.client.get_extattrenumdef(ea.SiteID)

    # NetScopes

    async def get_netscope[
        T: _m.NetworkContaier  # type: ignore[valid-type]
    ](self, nid: ea.NID, *extattrs: SearchExtAttr, return_cls: type[T],) -> T:
        return one_or_raise(await self.client.find_network_container(nid, *extattrs, return_cls=return_cls))

    async def get_netscopes[
        T: _m.NetworkContaier  # type: ignore[valid-type]
    ](self, nid: ea.NID, *extattrs: SearchExtAttr, return_cls: type[T],) -> list[T]:
        return await self.client.find_network_container(nid, *extattrs, return_cls=return_cls)

    # Nets

    async def get_unknown_nets[T: _m.Network](self, network: IPv4Network, return_cls: type[T]) -> list[T]:
        return await self.client.find_network(ea.SiteID.is_null(), network_container=network, return_cls=return_cls)

    async def get_net[
        T: _m.Network
    ](self, *extattrs: SearchExtAttr, return_cls: type[T], **kwargs: Unpack[_m.NetworkSearch]) -> T:
        return one_or_raise(await self.client.find_network(*extattrs, return_cls=return_cls, **kwargs))

    async def get_nets[
        T: _m.Network
    ](self, *extattrs: SearchExtAttr, return_cls: type[T], **kwargs: Unpack[_m.NetworkSearch]) -> list[T]:
        return await self.client.find_network(*extattrs, return_cls=return_cls, **kwargs)

    # AddrScopes

    async def get_addrscope[T: _m.Network](self, nid: ea.NID, return_cls: type[T]) -> T:
        return one_or_raise(await self.client.find_network(nid, return_cls=return_cls))

    async def get_addrscopes[T: _m.Network](self, nid: ea.NID, return_cls: type[T]) -> list[T]:
        return await self.client.find_network(nid, return_cls=return_cls)

    # Addrs

    async def get_unknown_addrs[T: _m.FixedAddress](self, network: IPv4Network, return_cls: type[T]) -> list[T]:
        return await self.client.find_fixedaddress(ea.SiteID.is_null(), network=network, return_cls=return_cls)

    async def get_addrs[
        T: _m.FixedAddress
    ](self, *extattrs: _m.SearchExtAttr, return_cls: type[T], **kwargs: Unpack[_m.FixedAddressSearch],) -> list[T]:
        return await self.client.find_fixedaddress(ea.SiteID.is_not_null(), *extattrs, return_cls=return_cls, **kwargs)

    async def get_addr_reg[
        T: _m.FixedAddress
    ](self, return_cls: type[T], **kwargs: Unpack[_m.FixedAddressSearch],) -> T:
        return one_or_raise(await self.client.find_fixedaddress(return_cls=return_cls, **kwargs))

    async def get_addr[
        T: _m.FixedAddress
    ](self, network: IPv4Network, oid: ea.SiteID | IPv4Address, return_cls: type[T],) -> T:
        if isinstance(oid, IPv4Address):
            return one_or_raise(
                await self.client.find_fixedaddress(ipv4addr=oid, network=network, return_cls=return_cls)
            )
        return one_or_raise(await self.client.find_fixedaddress(oid, network=network, return_cls=return_cls))

    # Ranges

    async def get_ranges[
        T: _m.Range
    ](self, nid: ea.NID, *extattrs: SearchExtAttr, network: IPv4Network | None = None, return_cls: type[T],) -> list[T]:
        kwargs: _m.RangeSearch = {"network": network} if network else {}
        return await self.client.find_range(nid, *extattrs, **kwargs, return_cls=return_cls)

    async def get_range[
        T: _m.Range
    ](self, nid: ea.NID, *extattrs: SearchExtAttr, network: IPv4Network, return_cls: type[T],) -> T:
        return one_or_raise(await self.client.find_range(nid, *extattrs, network=network, return_cls=return_cls))

    async def get_unknown_ranges[T: _m.Range](self, nid: ea.NID, return_cls: type[T]) -> list[T]:
        return await self.client.find_range(ea.SiteID.is_null(), nid, return_cls=return_cls)

    # Members

    async def get_members[T: _m.Member](self, return_cls: type[T]) -> list[T]:
        return await self.client.find_member(return_cls=return_cls)
