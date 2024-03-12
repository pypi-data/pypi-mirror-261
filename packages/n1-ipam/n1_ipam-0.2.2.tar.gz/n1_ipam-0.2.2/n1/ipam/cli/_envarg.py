import argparse
import functools
from os import environ
from typing import Any, Callable, ParamSpec, Protocol, TypeVar, cast

import dotenv
from click_option_group import optgroup

from n1.ipam.consts import ENV_ARG, ENV_DEFAULT, ENV_LOPT, ENV_NAME, ENV_OPT

P = ParamSpec("P")
T = TypeVar("T")


def with_env_file(func: Callable[P, T]) -> Callable[P, T]:
    @optgroup.group("Environment configuration", help="The configuration of some server connection")  # type: ignore
    @optgroup.option(ENV_LOPT, ENV_OPT, envvar=ENV_NAME, help="Host", required=False, default=ENV_DEFAULT)  # type: ignore
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        kwargs.pop(ENV_ARG, None)
        return func(*args, **kwargs)

    return wrapper


class EnvArgs(Protocol):  # pragma: no cover
    @property
    def env_file(self) -> str | None:
        ...


def load_env():  # pragma: no cover
    parser = argparse.ArgumentParser(exit_on_error=False, add_help=False)
    parser.add_argument(ENV_OPT, ENV_LOPT)
    args, _ = cast(tuple[EnvArgs, Any], parser.parse_known_args())

    env_file = environ.get(ENV_NAME, ENV_DEFAULT) if args.env_file is None else args.env_file

    dotenv.load_dotenv(env_file)
