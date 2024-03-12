import dataclasses
import pathlib

import conscia.infoblox.infoblox_sdk as ib
import yaml

from n1.ipam._api import AsyncApi
from n1.ipam._client import AsyncClient
from n1.ipam._config import Config


@dataclasses.dataclass(kw_only=True, slots=True)
class Settings:
    infoblox: ib.Settings
    config_file: pathlib.Path | None = None
    detect: bool | None = None

    def load_config(self) -> Config:
        if self.config_file is None:
            return Config()
        with open(self.config_file, "r") as fp:
            return Config.model_validate(yaml.load(fp, yaml.CLoader))

    def load_asyncapi(self) -> AsyncApi:
        return AsyncApi(self.infoblox.load_asyncclient())

    async def load_asyncclient(self) -> AsyncClient:
        config = self.load_config()

        api = self.load_asyncapi()

        return await AsyncClient.load(api, config, detect=self.detect)

    # def load_api(self) -> Api:
    #    return Api(self.infoblox.load_client())

    # def load_client(self) -> Client:
    #    config = self.load_config()
    #
    #    api = self.load_api()
    #
    #    return Client.load(api, config, detect=self.detect)
