from typing import Generic, NamedTuple, TypeVar

from conscia.infoblox.infoblox_sdk.extattr import ExtAttrBase


class Street(ExtAttrBase[str]):
    pass


class City(ExtAttrBase[str]):
    pass


class DKRegion(ExtAttrBase[str]):
    pass


class PostCode(ExtAttrBase[str], alias="Postcode"):
    pass


class ISPInst(ExtAttrBase[str]):
    pass


class ISPKreds(ExtAttrBase[str]):
    pass


class NID(ExtAttrBase[str], alias="VirtualNetwork"):
    pass


class SiteType(ExtAttrBase[str]):
    pass


class SiteID(ExtAttrBase[str]):
    pass


class SIMID(ExtAttrBase[str], alias="SIM iccid"):
    pass


class LoopID(ExtAttrBase[str], alias="LoopNetwork"):
    pass


class Address(ExtAttrBase[str]):
    pass


T = TypeVar("T")


class KV(NamedTuple, Generic[T]):
    name: str
    value: T


class ExtAttrGroup(Generic[T]):
    @classmethod
    def values(cls) -> list[KV[T]]:
        return [KV(name, getattr(cls, name)) for name in dir(cls) if not name.startswith("_") and name != "values"]


class SiteTypes(ExtAttrGroup[SiteType]):
    S60kV = SiteType("60kV")
    S10kV = SiteType("10kV")


class VNETS(ExtAttrGroup[NID]):
    VN001 = NID("VN001")
    VN002 = NID("VN002")
    VN003 = NID("VN003")
    VN004 = NID("VN004")
    VN005 = NID("VN005")
    VN006 = NID("VN006")
    VN007 = NID("VN007")
    VN008 = NID("VN008")


class CommonNetContainers(ExtAttrGroup[NID]):
    MPLS = NID("VNUnderlay")


class CommonNets(ExtAttrGroup[NID]):
    INFO = NID("Info")
    LO0 = NID("Lo0")
    LO1 = NID("Lo1")
    LO2 = NID("Lo2")
    LO3 = NID("Lo3")
    LO4 = NID("Lo4")
    APN = NID("APNUnderlay")


class NIDS(ExtAttrGroup[NID]):
    INFO = NID("Info")
    LO0 = NID("Lo0")
    LO1 = NID("Lo1")
    LO2 = NID("Lo2")
    LO3 = NID("Lo3")
    LO4 = NID("Lo4")
    APN = NID("APNUnderlay")
    MPLS = NID("VNUnderlay")
    VN001 = NID("VN001")
    VN002 = NID("VN002")
    VN003 = NID("VN003")
    VN004 = NID("VN004")
    VN005 = NID("VN005")
    VN006 = NID("VN006")
    VN007 = NID("VN007")
    VN008 = NID("VN008")


ALL_EXTATTRS = [
    Street,
    City,
    DKRegion,
    PostCode,
    ISPInst,
    ISPKreds,
    NID,
    SiteType,
    SiteID,
    SIMID,
    LoopID,
    Address,
]
