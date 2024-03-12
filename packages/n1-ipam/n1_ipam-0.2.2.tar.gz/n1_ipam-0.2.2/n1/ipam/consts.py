import pathlib
from datetime import timedelta

import conscia.infoblox.infoblox_sdk.consts as ib_const

SECOND = timedelta(seconds=1)
MINUTE = SECOND * 60


# Cli Env

PREFIX = "IPAM"
IB_PREFIX = ib_const.PREFIX

ENV_DEFAULT = ".env"
ENV_NAME = f"{PREFIX}_ENV_FILE"
ENV_OPT = "-e"
ENV_LOPT = "--env-file"
ENV_ARG = "env_file"


DEFAULT_HTTPX_TIMEOUT = 2 * MINUTE
DEFAULT_URL_SCHEME = ib_const.DEFAULT_URL_SCHEME
DEFAULT_URL_PATH = ib_const.DEFAULT_URL_PATH
DEFAULT_CAPATH = ib_const.DEFAULT_CAPATH
DEFAULT_INSECURE = ib_const.DEFAULT_INSECURE
DEFAULT_CONFIG_FILE = pathlib.Path("ipam.yml")
