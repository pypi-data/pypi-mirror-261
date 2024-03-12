from datetime import timedelta
from ipaddress import IPv4Address, IPv4Network, IPv6Address
from typing import Any

import pydantic as pyd

import n1.ipam.extattr as ea


class DHCPMember(pyd.BaseModel):
    name: str
    ipv4: IPv4Address | None = None
    ipv6: IPv6Address | None = None


class SiteTypes(pyd.BaseModel):
    S60kV: ea.SiteType = pyd.Field(default_factory=lambda: ea.SiteType("60kV"))
    S10kV: ea.SiteType = pyd.Field(default_factory=lambda: ea.SiteType("10kV"))

    @pyd.field_validator("S60kV", "S10kV", mode="before")
    def validate_aid(cls, data: str | ea.SiteType, _info: pyd.ValidationInfo) -> Any:
        return data if isinstance(data, ea.SiteType) else {"value": data}

    @pyd.field_serializer("S60kV", "S10kV")
    def serialize_aid(self, st: ea.SiteType, _info: pyd.FieldSerializationInfo) -> str:
        return st.value

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.startswith("t"):
            indent_str = __format_spec[1:]
            indent = int(indent_str) if len(indent_str) > 0 else 0
            ind = " " * (indent * 4)
            return f"""
{ind}S10kV: {repr(self.S10kV)}
{ind}S60kV: {repr(self.S60kV)}"""

        return super().__format__(__format_spec)


class DHCPRange(pyd.BaseModel):
    start_offset: int = 0
    end_offset: int = 0
    lease: timedelta = timedelta(seconds=43200)


class NetScope(pyd.BaseModel):
    nid: ea.NID
    comment: str | None = None
    net: IPv4Network | None = None
    prefix: int
    gw: int | None = 1
    members: list[DHCPMember] = []
    dhcp: DHCPRange | None = None

    @pyd.field_validator("nid", mode="before")
    def validate_aid(cls, data: str | ea.NID, _info: pyd.ValidationInfo) -> Any:
        return data if isinstance(data, ea.NID) else {"value": data}

    @pyd.field_serializer("nid")
    def serialize_aid(self, nid: ea.NID, _info: pyd.FieldSerializationInfo) -> str:
        return nid.value

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


class AddrScope(pyd.BaseModel):
    nid: ea.NID
    comment: str | None = None
    net: IPv4Network | None = None
    skip: int = 0

    @pyd.field_validator("nid", mode="before")
    def validate_aid(cls, data: str | ea.NID, _info: pyd.ValidationInfo) -> Any:
        return data if isinstance(data, ea.NID) else {"value": data}

    @pyd.field_serializer("nid")
    def serialize_aid(self, nid: ea.NID, _info: pyd.FieldSerializationInfo) -> str:
        return nid.value

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.startswith("t"):
            indent_str = __format_spec[1:]
            indent = int(indent_str) if len(indent_str) > 0 else 0
            ind = " " * (indent * 4)
            return f"""
{ind}{self.comment}
{ind}{self.nid}
{ind}{self.net}"""

        return super().__format__(__format_spec)


class VNetScopes(pyd.BaseModel):
    vn001: NetScope = pyd.Field(
        default_factory=lambda: NetScope(nid=ea.NID("VN001"), prefix=27, dhcp=DHCPRange(start_offset=10))
    )
    vn002: NetScope = pyd.Field(
        default_factory=lambda: NetScope(nid=ea.NID("VN002"), prefix=27, dhcp=DHCPRange(start_offset=10))
    )
    vn003: NetScope = pyd.Field(
        default_factory=lambda: NetScope(nid=ea.NID("VN003"), prefix=27, dhcp=DHCPRange(start_offset=10))
    )
    vn004: NetScope = pyd.Field(
        default_factory=lambda: NetScope(nid=ea.NID("VN004"), prefix=27, dhcp=DHCPRange(start_offset=10))
    )
    vn005: NetScope = pyd.Field(
        default_factory=lambda: NetScope(nid=ea.NID("VN005"), prefix=27, dhcp=DHCPRange(start_offset=10))
    )
    vn006: NetScope = pyd.Field(
        default_factory=lambda: NetScope(nid=ea.NID("VN006"), prefix=27, dhcp=DHCPRange(start_offset=10))
    )
    vn007: NetScope = pyd.Field(
        default_factory=lambda: NetScope(nid=ea.NID("VN007"), prefix=27, dhcp=DHCPRange(start_offset=10))
    )
    vn008: NetScope = pyd.Field(
        default_factory=lambda: NetScope(nid=ea.NID("VN008"), prefix=27, dhcp=DHCPRange(start_offset=10))
    )

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.startswith("t"):
            fields = self.model_fields
            indent_str = __format_spec[1:]
            indent = int(indent_str) if len(indent_str) > 0 else 0
            ind = " " * (indent * 4)
            fieldstrs = [f"{ind}{name}:{getattr(self, name):t{indent+1}}" for name in fields]
            return "\n" + "\n".join(fieldstrs)

        return super().__format__(__format_spec)


class NetScopes(pyd.BaseModel):
    s10kV: VNetScopes = pyd.Field(default_factory=VNetScopes)
    s60kV: VNetScopes = pyd.Field(default_factory=VNetScopes)
    mpls: NetScope = pyd.Field(
        default_factory=lambda: NetScope(nid=ea.NID("VNUnderlay"), prefix=30, dhcp=DHCPRange(start_offset=1))
    )

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.startswith("t"):
            fields = self.model_fields
            indent_str = __format_spec[1:]
            indent = int(indent_str) if len(indent_str) > 0 else 0
            ind = " " * (indent * 4)
            fieldstrs = [f"{ind}{name}:{getattr(self, name):t{indent+1}}" for name in fields]
            return "\n" + "\n".join(fieldstrs)

        return super().__format__(__format_spec)


class LoopScopes(pyd.BaseModel):
    lo0: AddrScope = pyd.Field(default_factory=lambda: AddrScope(nid=ea.NID("Lo0"), skip=9))
    lo1: AddrScope = pyd.Field(default_factory=lambda: AddrScope(nid=ea.NID("Lo1"), skip=9))
    lo2: AddrScope = pyd.Field(default_factory=lambda: AddrScope(nid=ea.NID("Lo2"), skip=9))
    lo3: AddrScope = pyd.Field(default_factory=lambda: AddrScope(nid=ea.NID("Lo3"), skip=9))
    lo4: AddrScope = pyd.Field(default_factory=lambda: AddrScope(nid=ea.NID("Lo4"), skip=9))

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.startswith("t"):
            fields = self.model_fields
            indent_str = __format_spec[1:]
            indent = int(indent_str) if len(indent_str) > 0 else 0
            ind = " " * (indent * 4)
            fieldstrs = [f"{ind}{name}:{getattr(self, name):t{indent+1}}" for name in fields]
            return "\n" + "\n".join(fieldstrs)

        return super().__format__(__format_spec)


class AddrScopes(pyd.BaseModel):
    info: AddrScope = pyd.Field(default_factory=lambda: AddrScope(nid=ea.NID("Info")))
    apn: AddrScope = pyd.Field(default_factory=lambda: AddrScope(nid=ea.NID("APNUnderlay")))
    loops: LoopScopes = pyd.Field(default_factory=LoopScopes)

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.startswith("t"):
            fields = self.model_fields
            indent_str = __format_spec[1:]
            indent = int(indent_str) if len(indent_str) > 0 else 0
            ind = " " * (indent * 4)
            fieldstrs = [f"{ind}{name}:{getattr(self, name):t{indent+1}}" for name in fields]
            return "\n" + "\n".join(fieldstrs)

        return super().__format__(__format_spec)


class Config(pyd.BaseModel):
    dhcp_members: list[DHCPMember] = pyd.Field(default_factory=list)
    sitetypes: SiteTypes = pyd.Field(default_factory=SiteTypes)
    netscopes: NetScopes = pyd.Field(default_factory=NetScopes)
    addrscopes: AddrScopes = pyd.Field(default_factory=AddrScopes)

    def __format__(self, __format_spec: str) -> str:
        if __format_spec.startswith("t"):
            indent_str = __format_spec[1:]
            indent = int(indent_str) if len(indent_str) > 0 else 0
            ind = " " * (indent * 4)
            members = [f"{ind}    {m.name}\n{ind}        {m.ipv4}" for m in self.dhcp_members]
            members_str = "\n".join(members)
            return f"""
{ind}DHCPMembers:
{members_str}
{ind}SiteTypes:{self.sitetypes:t{indent+1}}
{ind}NetScopes:{self.netscopes:t{indent+1}}
{ind}AddrScopes:{self.addrscopes:t{indent+1}}
"""
        return super().__format__(__format_spec)
