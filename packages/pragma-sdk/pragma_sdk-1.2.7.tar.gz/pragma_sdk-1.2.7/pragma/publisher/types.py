import abc
from typing import Any, List

import aiohttp
from aiohttp import ClientSession


# Abstract base class for all publishers
class PublisherInterfaceT(abc.ABC):
    @abc.abstractmethod
    async def fetch(self, session: ClientSession) -> List[Any]: ...

    @abc.abstractmethod
    def fetch_sync(self) -> List[Any]: ...

    @abc.abstractmethod
    def format_url(self, quote_asset, base_asset) -> str: ...

    async def _fetch(self):
        async with aiohttp.ClientSession() as session:
            data = await self.fetch(session)
            return data


class PublisherFetchError(Exception):
    message: str

    def __init__(self, message: str):
        self.message = message

    def __eq__(self, other):
        return self.message == other.message

    def __repr__(self):
        return self.message

    def serialize(self):
        return self.message
