import asyncio
import csv
import functools
import json
import logging
import sys
from ipaddress import IPv4Network
from typing import Any, Callable, Coroutine, ParamSpec, TypeVar, cast

import click
import conscia.infoblox.infoblox_sdk as ib
import tabulate
import yaml
from click_option_group import optgroup
from conscia.infoblox.infoblox_sdk.extattr import ExtAttrBase
from conscia.infoblox.infoblox_sdk.types import Endpoint

import n1.ipam.extattr as ea
import n1.ipam.models as m
from n1.ipam import __version__
from n1.ipam._settings import Settings
from n1.ipam.cli._envarg import load_env, with_env_file
from n1.ipam.cli.opts import with_settings
from n1.ipam.models import (
    APNAddr,
    APNTmpl,
    LoopAddr,
    MPLSNet,
    MPLSTmpl,
    Site60kVTmpl,
    SiteInfo,
    SiteInfoTmpl,
    VNet,
)

P = ParamSpec("P")
T = TypeVar("T")

log = logging.getLogger(__name__)


def GREEN(s: str):
    return "\u001B[32m" + s + "\u001B[0m"


def RED(s: str):
    return "\u001B[31m" + s + "\u001B[0m"


# region Helpers


def as_async(func: Callable[P, Coroutine[None, None, T]]) -> Callable[P, T]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        return asyncio.run(func(*args, **kwargs))

    return wrapper


def with_logging(func: Callable[P, T]) -> Callable[P, T]:
    @optgroup.group("Misc configuration", help="The configuration of some misc")  # type: ignore
    @optgroup.option("--verbose", "-v", count=True, help="Enables verbose mode.")  # type: ignore
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        verbose = cast(int, kwargs.pop("verbose"))
        match verbose:
            case 0:  # pragma: no cover
                logging.basicConfig(level=logging.ERROR)
            case 1:  # pragma: no cover
                logging.basicConfig(level=logging.INFO)
            case _:  # pragma: no cover
                logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("httpx").setLevel(logging.ERROR)
        logging.getLogger("httpcore").setLevel(logging.ERROR)
        return func(*args, **kwargs)

    return wrapper


# endregion

# region tasks


def _make_attrs[T: ExtAttrBase[Any]](*extattrs: type[T]) -> dict[str, type[T]]:
    return {x.name: x for x in extattrs}


EXTATTRS = _make_attrs(*ea.ALL_EXTATTRS)


async def allocate_site(settings: Settings, tmpl: Site60kVTmpl):
    ipam = await settings.load_asyncclient()
    try:
        await ipam.get_siteinfo(tmpl.siteid)
        print("Already exists")
        return
    except Exception:
        pass
    site = await ipam.allocate(tmpl)
    print(site)


async def deallocate_site(settings: Settings, siteid: ea.SiteID):
    ipam = await settings.load_asyncclient()
    await ipam.deallocate(siteid)


async def register_site(settings: Settings, info: SiteInfoTmpl):
    ipam = await settings.load_asyncclient()
    await ipam.register_site(info)


async def deregister_site(settings: Settings, siteid: ea.SiteID):
    ipam = await settings.load_asyncclient()
    await ipam.deregister_site(siteid)


async def nuke_site(settings: Settings, siteid: ea.SiteID):
    ipam = await settings.load_asyncclient()
    api = ipam.api

    async def _nuke_apn():
        objs = await api.get_addrs(siteid, network=ipam.scopes.apn.net, return_cls=APNAddr)
        for obj in objs:
            print(obj)
        input("Press Enter to continue...")
        for obj in objs:
            reg_obj = obj.release()
            await api.update(reg_obj)

    await _nuke_apn()

    async def _nuke_mpls():
        objs = await api.get_nets(siteid, network_container=ipam.scopes.mpls.net, return_cls=MPLSNet)
        for obj in objs:
            print(obj)
        input("Press Enter to continue...")
        for obj in objs:
            obj = obj.release()
            await api.update(obj)

    await _nuke_mpls()

    async def _nuke_vnets():
        g = ipam.scopes.s60kV
        for net in [g.vn001, g.vn002, g.vn003, g.vn004, g.vn005, g.vn006, g.vn007, g.vn008]:
            objs = await api.get_nets(siteid, network_container=net.net, return_cls=VNet)
            for obj in objs:
                print(obj)
            input("Press Enter to continue...")
            for obj in objs:
                await api.delete(obj)

    await _nuke_vnets()

    async def _nuke_loops():
        g = ipam.scopes.loops
        for net in [g.lo0, g.lo1, g.lo2, g.lo3, g.lo4]:
            objs = await api.get_addrs(siteid, network=net.net, return_cls=LoopAddr)
            for obj in objs:
                print(obj)
            input("Press Enter to continue...")
            for obj in objs:
                await api.delete(obj)

    await _nuke_loops()

    async def _nuke_info():
        objs = await api.get_addrs(siteid, network=ipam.scopes.info.net, return_cls=SiteInfo)
        for obj in objs:
            print(obj)
        input("Press Enter to continue...")
        for obj in objs:
            await api.delete(obj)

    await _nuke_info()


async def verify_all(
    settings: Settings,
    fix: bool,
    no_loop: bool,
    no_vnet: bool,
    no_mpls: bool,
    no_apn: bool,
    skip_comment: bool,
    hide_unused: bool,
    hide_ok: bool,
):
    ipam = await settings.load_asyncclient()
    await ipam.verify(
        skip_loop=no_loop,
        skip_vnet=no_vnet,
        skip_mpls=no_mpls,
        skip_apn=no_apn,
        fix=fix,
        hide_unused=hide_unused,
        skip_comment=skip_comment,
        hide_ok=hide_ok,
    )


async def dump_endpoint(settings: Settings, endpoint: str, search: bool):
    ipam = await settings.load_asyncclient()
    ep_cls = Endpoint(endpoint)
    scheme = await ipam.api.client.get_schema(ep_cls)
    if search:
        print(f"{scheme:s}")
    else:
        print(f"{scheme}")


# endregion


@click.group()
@with_env_file
@with_settings("settings")
@with_logging
@click.version_option(__version__)
@click.pass_context
def cli(ctx: click.Context, settings: Settings):
    ctx.obj = settings


@cli.command()
@click.argument("siteid", required=True)
@click.option("--street")
@click.option("--postcode")
@click.option("--city")
@click.option("--dkregion")
@click.make_pass_decorator(Settings)
def reg(
    settings: Settings,
    siteid: str,
    street: str | None,
    postcode: str | None,
    city: str | None,
    dkregion: str | None,
):
    config = settings.load_config()
    info = SiteInfoTmpl(
        siteid=ea.SiteID(siteid),
        sitetype=config.sitetypes.S60kV,
        street=None if street is None else ea.Street(street),
        postcode=None if postcode is None else ea.PostCode(postcode),
        city=None if city is None else ea.City(city),
        dkregion=ea.DKRegion("Midt") if dkregion is None else ea.DKRegion(dkregion),
    )
    asyncio.run(register_site(settings, info))


@cli.command()
@click.argument("siteid", required=True)
@click.make_pass_decorator(Settings)
def dereg(
    settings: Settings,
    siteid: str,
):
    asyncio.run(deregister_site(settings, ea.SiteID(siteid)))


@cli.command()
@click.argument("siteid", required=True)
@click.make_pass_decorator(Settings)
def nuke(
    settings: Settings,
    siteid: str,
):
    asyncio.run(nuke_site(settings, ea.SiteID(siteid)))


@cli.command()
@click.argument("siteid", required=True)
@click.option("--street")
@click.option("--postcode")
@click.option("--city")
@click.option("--dkregion")
@click.option("--mpls", type=int)
@click.option("--apn", type=int)
@click.make_pass_decorator(Settings)
def all(
    settings: Settings,
    siteid: str,
    street: str | None,
    postcode: str | None,
    city: str | None,
    dkregion: str | None,
    mpls: int | None,
    apn: int | None,
):
    config = settings.load_config()
    tmpl = Site60kVTmpl(
        info=SiteInfoTmpl(
            siteid=ea.SiteID(siteid),
            sitetype=config.sitetypes.S60kV,
            street=None if street is None else ea.Street(street),
            postcode=None if postcode is None else ea.PostCode(postcode),
            city=None if city is None else ea.City(city),
            dkregion=ea.DKRegion("Midt") if dkregion is None else ea.DKRegion(dkregion),
        ),
        mpls=MPLSTmpl(mpls) if mpls is not None else None,
        apn=APNTmpl(apn) if apn is not None else None,
    )
    asyncio.run(allocate_site(settings, tmpl))


@cli.command()
@click.argument("siteid", required=True)
@click.make_pass_decorator(Settings)
def deall(settings: Settings, siteid: str):
    asyncio.run(deallocate_site(settings, ea.SiteID(siteid)))


@cli.command()
@click.option("--fix", is_flag=True)
@click.option("--no-loop", is_flag=True)
@click.option("--no-vnet", is_flag=True)
@click.option("--no-mpls", is_flag=True)
@click.option("--no-apn", is_flag=True)
@click.option("--skip-comment", is_flag=True)
@click.option("--hide-unused", is_flag=True)
@click.option("--hide-ok", is_flag=True)
@click.make_pass_decorator(Settings)
@as_async
async def verify(
    settings: Settings,
    fix: bool,
    no_loop: bool,
    no_vnet: bool,
    no_mpls: bool,
    no_apn: bool,
    skip_comment: bool,
    hide_unused: bool,
    hide_ok: bool,
):
    async with await settings.load_asyncclient() as ipam:
        await ipam.verify(
            skip_loop=no_loop,
            skip_vnet=no_vnet,
            skip_mpls=no_mpls,
            skip_apn=no_apn,
            fix=fix,
            hide_unused=hide_unused,
            skip_comment=skip_comment,
            hide_ok=hide_ok,
        )


# region MPLS


@cli.group("mpls")
def mpls():
    pass


@mpls.command("get")
@click.argument("net")
@click.make_pass_decorator(Settings)
@as_async
async def get_mpls(settings: Settings, net: str):
    async with await settings.load_asyncclient() as client:
        mpls_net = await client.scopes.mpls.get_unknown_net(client.api, IPv4Network(net))
        print(mpls_net)


@mpls.command("list")
@click.option("--free/--no-free", default=True)
@click.option("--unknown/--no-unknown", default=True)
@click.option("--registered/--no-registered", default=True)
@click.option("--assigned/--no-assigned", default=True)
@click.option("all_net", "--all/--no-all", default=True)
@click.make_pass_decorator(Settings)
@as_async
async def list_mpls(settings: Settings, unknown: bool, registered: bool, assigned: bool, all_net: bool, free: bool):
    async with await settings.load_asyncclient() as client:
        data: list[list[str]] = []

        all_nets = await client.scopes.mpls.get_all_gnets(client.api)

        if registered:
            for net in sorted(all_nets.registered, key=lambda x: x.net.network):
                data.append(
                    [
                        "Registered",
                        str(net.net.network),
                        "",
                        str(net.net.extattrs.inst),
                        str(net.net.extattrs.kreds),
                    ]
                )

        if assigned:
            for net in sorted(all_nets.assigned, key=lambda x: x.net.network):
                data.append(
                    [
                        "Assigned",
                        str(net.net.network),
                        str(net.net.extattrs.siteid),
                        str(net.net.extattrs.inst),
                        str(net.net.extattrs.kreds),
                    ]
                )

        if free:
            for net in sorted(all_nets.free):
                data.append(["Free", str(net), "", "", ""])

        print(tabulate.tabulate(data, headers=["Type", "Net", "SiteID", "Inst", "Kreds"]))


@mpls.command("reg")
@click.argument("net")
@click.option("--kreds", required=True)
@click.option("--inst", required=True)
@click.make_pass_decorator(Settings)
@as_async
async def register_mpls(settings: Settings, net: str | IPv4Network, kreds: str, inst: str):
    async with await settings.load_asyncclient() as client:
        tmpl = m.MPLSTmpl(IPv4Network(net), ea.ISPKreds(kreds), ea.ISPInst(inst))
        mpls_net = await client.register_mpls(tmpl)
        print(mpls_net)


@mpls.command("assign")
@click.option("--siteid", required=True)
@click.option("--net", required=True)
@click.make_pass_decorator(Settings)
@as_async
async def assign_mpls(settings: Settings, net: str, siteid: str):
    async with await settings.load_asyncclient() as client:
        res = await client.assign_mpls(ea.SiteID(siteid), IPv4Network(net))
        print(res)


def abort_if_false(ctx: click.Context, param: click.Parameter, value: bool):
    if not value:
        ctx.abort()


@mpls.command("delete")
@click.argument("net")
@click.option(
    "--yes",
    is_flag=True,
    callback=abort_if_false,
    expose_value=False,
    prompt="Are you sure you want to delete the net?",
)
@click.make_pass_decorator(Settings)
@as_async
async def delete_mpls(settings: Settings, net: str):
    async with await settings.load_asyncclient() as client:
        mpls_net = await client.scopes.mpls.get_reg_gnet(client.api, IPv4Network(net))
        if mpls_net.dhcp is not None:
            print(f"Deleting {mpls_net.dhcp}")
            await client.api.delete(mpls_net.dhcp)
        print(f"Deleting {mpls_net.net}")
        await client.api.delete(mpls_net.net)
        print("Deleted")


# endregion


# region Config


@cli.group("config")
def _config():
    pass


@_config.command("show")
@click.make_pass_decorator(Settings)
def show_config(settings: Settings):
    print(settings)


@_config.group("validate")
def _validate():
    pass


async def _validate_extattr_group(
    client: ib.AsyncClient, ea_cls: type[ExtAttrBase[Any]], ea_group: type[ea.SiteTypes | ea.NIDS]
):
    print(ea_cls.name)
    print("===========================")
    extattrdef = await client.get_extattrenumdef(ea_cls)
    for name, value in ea_group.values():
        print(f"{extattrdef.name}:{name} [{value}] ", end="")
        if extattrdef.contains(value):
            print(GREEN("PASSED"))
        else:
            print(RED("MISSING"))
    print()


@_validate.command("db")
@click.make_pass_decorator(Settings)
@as_async
async def validate_db(settings: Settings):
    client = settings.infoblox.load_asyncclient()
    print()

    print("Extattr")
    print("===========================")
    for extattr in ea.ALL_EXTATTRS:
        print(f"Extattr:{extattr.name} ", end="")
        try:
            await client.get_extattrdef(extattr)
        except Exception as e:
            log.info(e)
            print(RED("MISSING"))
        else:
            print(GREEN("PASSED"))
    print()

    await _validate_extattr_group(client, ea.SiteType, ea.SiteTypes)
    await _validate_extattr_group(client, ea.NID, ea.NIDS)

    print("Network Containers")
    print("===========================")
    for net in ea.CommonNetContainers.values():
        print(f"NetCon:{net.name} ", end="")
        try:
            await client.find_network_container(net.value)
        except Exception as e:
            log.info(e)
            print(RED("MISSING"))
        else:
            print(GREEN("PASSED"))
    for st in ea.SiteTypes.values():
        for vnet in ea.VNETS.values():
            print(f"VNET:{st.name}:{vnet.name} ", end="")
            try:
                await client.find_network_container(st.value, vnet.value)
            except Exception as e:
                log.info(e)
                print(RED("MISSING"))
            else:
                print(GREEN("PASSED"))
    print()

    print("Networks")
    print("===========================")
    for net in ea.CommonNets.values():
        print(f"Net:{net.name} ", end="")
        try:
            await client.find_network(net.value)
        except Exception as e:
            log.info(e)
            print(RED("MISSING"))
        else:
            print(GREEN("PASSED"))
    print()


# endregion


# region Dump


@cli.group()
def dump():
    pass


@dump.command("schema")
@click.argument(
    "endpoint",
    type=click.Choice([t.value for t in Endpoint.__members__.values()], case_sensitive=False),
    required=True,
)
@click.option("--search", "-s", is_flag=True, help="Search only.")
@click.make_pass_decorator(Settings)
@as_async
async def schema(settings: Settings, endpoint: str, search: bool):
    ipam = await settings.load_asyncclient()
    ep_cls = Endpoint(endpoint)
    scheme = await ipam.api.client.get_schema(ep_cls)
    if search:
        print(f"{scheme:s}")
    else:
        print(f"{scheme}")


@dump.command("extattr")
@click.argument(
    "extattr",
    type=click.Choice(list(EXTATTRS.keys()), case_sensitive=False),
    required=True,
)
@click.make_pass_decorator(Settings)
@as_async
async def extattr(settings: Settings, extattr: str):
    ipam = await settings.load_asyncclient()
    extattr_def = await ipam.api.client.get_extattrenumdef(EXTATTRS[extattr])
    print(yaml.dump(extattr_def.model_dump(mode="json"), allow_unicode=True))


@dump.command("sites")
@click.option(
    "--format",
    type=click.Choice(["csv", "json", "table"], case_sensitive=False),
    required=True,
    default="csv",
)
@click.make_pass_decorator(Settings)
@as_async
async def sites(settings: Settings, format: str):
    def value_or_none[T: (str, int)](o: ExtAttrBase[T] | None) -> T | None:
        if o is None:
            return None
        return o.value

    ipam = await settings.load_asyncclient()
    sites = await ipam.get_siteinfos()
    sites = sorted(sites, key=lambda x: x.extattrs.siteid)

    site_dct_lst = [
        {
            "siteid": value_or_none(site.extattrs.siteid),
            "street": value_or_none(site.extattrs.street),
            "postcode": value_or_none(site.extattrs.postcode),
            "city": value_or_none(site.extattrs.city),
            "dkregion": value_or_none(site.extattrs.dkregion),
        }
        for site in sites
    ]

    print(site_dct_lst)

    site_lst_lst = [
        [
            value_or_none(site.extattrs.siteid),
            value_or_none(site.extattrs.street),
            value_or_none(site.extattrs.postcode),
            value_or_none(site.extattrs.city),
            value_or_none(site.extattrs.dkregion),
        ]
        for site in sites
    ]

    match format:
        case "table":
            headers = [
                "SiteID",
                "Street",
                "Postcode",
                "City",
                "DKRegion",
            ]
            print(tabulate.tabulate(site_lst_lst, headers=headers))
        case "csv":
            w = csv.DictWriter(sys.stdout, site_dct_lst[0].keys(), delimiter=";")
            w.writeheader()
            w.writerows(site_dct_lst)
        case "json":
            print(json.dumps(site_dct_lst, indent=4))
        case _:
            raise Exception("invalid format")


# endregion


def main():
    load_env()
    cli(max_content_width=120)
