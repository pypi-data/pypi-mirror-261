from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from omu.event import EventData, EventType
    from omu.network import Address


type ConnectionStatus = Literal["connecting", "connected", "disconnected"]


class ConnectionListener:
    async def on_connected(self) -> None: ...

    async def on_disconnected(self) -> None: ...

    async def on_event(self, event: EventData) -> None: ...

    async def on_status_changed(self, status: ConnectionStatus) -> None: ...


class Connection(abc.ABC):
    @property
    @abc.abstractmethod
    def address(self) -> Address: ...

    @property
    @abc.abstractmethod
    def connected(self) -> bool: ...

    @abc.abstractmethod
    async def connect(
        self, *, token: str | None = None, reconnect: bool = True
    ) -> None: ...

    @abc.abstractmethod
    async def disconnect(self) -> None: ...

    @abc.abstractmethod
    async def send[T](self, event: EventType[T], data: T) -> None: ...

    @abc.abstractmethod
    def add_listener[T: ConnectionListener](self, listener: T) -> T: ...

    @abc.abstractmethod
    def remove_listener[T: ConnectionListener](self, listener: T) -> T: ...
