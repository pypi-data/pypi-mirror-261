import dataclasses
import logging
from datetime import timedelta
from ipaddress import IPv4Address, IPv4Network
from typing import Any, Generic, NamedTuple, TypeVar

from conscia.infoblox.infoblox_sdk.extattr import ExtAttrCollection
from conscia.infoblox.infoblox_sdk.types import (
    FailoverAssociation,
    ServerAssociationType,
)

import n1.ipam.extattr as ea

log = logging.getLogger(__name__)


class NameSiteid(NamedTuple):
    name: str
    siteid: ea.SiteID


class LogLine(NamedTuple):
    part: str
    ok: bool
    line: str = ""


@dataclasses.dataclass(slots=True, kw_only=True)
class VerifyLog:
    title: str
    is_ok: bool = True
    update: bool = False
    lines: list[LogLine] = dataclasses.field(default_factory=list)

    def error(self, part: str, line: str, update: bool = True) -> None:
        self.is_ok = False
        if update:
            self.update = True
        self.lines.append(LogLine(part, False, line))

    def ok(self, part: str) -> None:
        self.lines.append(LogLine(part, True))

    def print(self, show_ok: bool) -> None:
        if self.is_ok and not show_ok:
            return
        print(f" - {self.title}: {'ok' if self.is_ok else 'error'}")
        if self.is_ok:
            return
        for part, ok, line in self.lines:
            if ok and not show_ok:
                continue
            if ok:
                print(f"  - {part}: ok")
            else:
                print(f"  - {part}: {line}")


def format_extra(extattrs: ExtAttrCollection | None) -> dict[str, Any]:
    if extattrs is None or extattrs.model_extra is None:
        return {}
    return {k: v["value"] for k, v in extattrs.model_extra.items()}


@dataclasses.dataclass(slots=True, kw_only=True)
class DHCPRange:
    start_offset: int
    end_offset: int
    lease: timedelta
    server_association_type: ServerAssociationType = ServerAssociationType.FAILOVER
    failover_association: FailoverAssociation = FailoverAssociation.FAILOVER

    def calc_start_addr(self, net: IPv4Network) -> IPv4Address:
        return net.network_address + 1 + self.start_offset

    def calc_end_addr(self, net: IPv4Network) -> IPv4Address:
        return net.broadcast_address - 1 - self.end_offset


Tcv = TypeVar("Tcv")


class ObjWOffset(NamedTuple, Generic[Tcv]):
    obj: Tcv
    offset: int


class ColWOffset(NamedTuple, Generic[Tcv]):
    obj: Tcv
    offsets: dict[ea.SiteID, int]
