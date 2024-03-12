import dataclasses
import functools
import pathlib
from typing import Any, Callable, Generic, ParamSpec, Protocol, TypeVar, cast

import click
from click_option_group import optgroup
from conscia.infoblox.infoblox_sdk import Settings as IBSettings
from conscia.infoblox.infoblox_sdk.cli.opts import with_settings as with_ib_settings

from n1.ipam._settings import Settings
from n1.ipam.consts import DEFAULT_CONFIG_FILE, PREFIX

# region option helpers

P = ParamSpec("P")
T = TypeVar("T")
Tcv = TypeVar("Tcv", covariant=True)


class Converter(Protocol[Tcv]):
    def convert(self, value: Any, param: Any, ctx: Any) -> Tcv:
        ...


@dataclasses.dataclass(slots=True)
class Prefix:
    default_prefix: str
    prefix: str | bool | None

    def arg(self, name: str):
        if isinstance(self.prefix, str):
            return f"{self.prefix}_{name}"
        return f"{self.default_prefix}_{name}"

    def envvar(self, name: str):
        match self.prefix:
            case None | True:
                return {"envvar": f"{self.default_prefix.upper()}_{name}"}
            case False:
                return {"envvar": name}
            case str():
                return {"envvar": f"{self.prefix.upper()}_{name}"}

    def opt(self, lopt: str, opt: None | str = None):
        match self.prefix:
            case None | False:
                if opt is None:
                    return (lopt,)
                return (lopt, opt)
            case True:
                return (f"--{self.default_prefix.lower()}-{lopt[2:]}",)
            case str():
                return (f"--{self.prefix.lower()}-{lopt[2:]}",)

    def create(
        self,
        lopt: str,
        opt: str | None = None,
        *,
        envvar: str | None = None,
        type: type[T] | Converter[T] | None = None,
    ) -> "Opt[T]":
        if isinstance(opt, str):
            return Opt(self, envvar, (lopt, opt), type)
        return Opt(self, envvar, (lopt,), type)


@dataclasses.dataclass(slots=True)
class Opt(Generic[T]):
    _prefix: Prefix
    _envvar: str | None
    _opts: tuple[str, ...]
    _type: type[T] | Converter[T] | None = None

    @property
    def arg(self):
        return self._prefix.arg(self._opts[0].replace("-", "_"))

    @property
    def kwargs(self):
        res: dict[str, Any] = {}
        if self._type is not None:
            res["type"] = self._type
        if self._envvar is not None:
            res["show_envvar"] = True
            res.update(self._prefix.envvar(self._envvar))
        return res

    @property
    def args(self):
        return (self.arg, *self._prefix.opt(*self._opts))

    def get(self, kwargs: dict[str, Any]) -> T:
        return kwargs.pop(self.arg)


def with_settings(name: str = "settings", *, prefix: str | bool | None = None, ib_prefix: str | bool | None = None):
    p = Prefix(PREFIX, prefix)

    config_file = p.create(
        "--config-file",
        "-c",
        envvar="CONFIG",
        type=cast(Converter[pathlib.Path], click.Path(exists=True, dir_okay=False, path_type=pathlib.Path)),
    )
    detect = p.create("--detect", envvar="DETECT", type=bool)
    ib_settings: Opt[IBSettings] = p.create("--ib-settings", type=IBSettings)

    def _wrap(fn: Callable[P, T]) -> Callable[P, T]:
        @optgroup.group("IPAM Settings")  # type: ignore
        @optgroup.option(*config_file.args, **config_file.kwargs, default=DEFAULT_CONFIG_FILE, show_default=True)  # type: ignore
        @optgroup.option(*detect.args, **detect.kwargs, is_flag=True)  # type: ignore
        @with_ib_settings(ib_settings.arg, prefix=ib_prefix)
        @functools.wraps(fn)
        def _inner(*args: P.args, **kwargs: P.kwargs) -> T:
            kwargs[name] = Settings(
                infoblox=ib_settings.get(kwargs),
                detect=detect.get(kwargs),
                config_file=config_file.get(kwargs),
            )
            return fn(*args, **kwargs)

        return _inner  # type: ignore

    return _wrap


# endregion
