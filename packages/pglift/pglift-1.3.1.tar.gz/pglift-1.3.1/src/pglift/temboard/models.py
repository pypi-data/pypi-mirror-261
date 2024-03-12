# SPDX-FileCopyrightText: 2021 Dalibo
#
# SPDX-License-Identifier: GPL-3.0-or-later

from pathlib import Path
from typing import Annotated, ClassVar, Final, Optional

from attrs import frozen
from pydantic import Field, SecretStr

from .. import types
from ..settings._temboard import Settings
from . import impl

default_port: Final = 2345
service_name: Final = "temboard_agent"


@frozen
class Service:
    """A temboard-agent service bound to a PostgreSQL instance."""

    __service_name__: ClassVar[str] = service_name

    name: str
    """Identifier for the service, usually the instance qualname."""

    settings: Settings

    port: int
    """TCP port for the temboard-agent API."""

    password: Optional[SecretStr]

    def __str__(self) -> str:
        return f"{self.__service_name__}@{self.name}"

    def args(self) -> list[str]:
        configpath = impl._configpath(self.name, self.settings)
        return impl._args(self.settings.execpath, configpath)

    def pidfile(self) -> Path:
        return impl._pidfile(self.name, self.settings)

    def env(self) -> None:
        return None


class ServiceManifest(types.ServiceManifest, service_name="temboard"):
    port: Annotated[
        types.Port, Field(description="TCP port for the temboard-agent API.")
    ] = default_port
    password: Annotated[
        Optional[SecretStr],
        Field(
            description="Password of PostgreSQL role for temboard agent.",
            exclude=True,
        ),
    ] = None
