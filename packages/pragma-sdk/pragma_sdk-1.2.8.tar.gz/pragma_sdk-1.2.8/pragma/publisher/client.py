import asyncio
from typing import List

import aiohttp

from pragma.core.client import PragmaClient
from pragma.publisher.types import PublisherInterfaceT


class PragmaPublisherClient(PragmaClient):
    """
    This client extends the pragma client with functionality for fetching from our third party sources.
    It can be used to synchronously or asynchronously fetch assets using the Asset format, ie.

    `{"type": "SPOT", "pair": ("BTC", "USD"), "decimals": 18}`

    More to follow on the standardization of this format.

    The client works by setting up fetchers that are provided the assets to fetch and the publisher name.

    ```python
    cex_fetcher = CexFetcher(PRAGMA_ALL_ASSETS, "pragma_fetcher_test")
    gemini_fetcher = GeminiFetcher(PRAGMA_ALL_ASSETS, "pragma_fetcher_test")
    fetchers = [
        cex_fetcher,
        gemini_fetcher,
    ]
    eapc = PragmaPublisherClient('testnet')
    eapc.add_fetchers(fetchers)
    await eapc.fetch()
    eapc.fetch_sync()
    ```

    You can also set a custom timeout duration as followed:
    ```python
    await eapc.fetch(timeout_duration=20) # Denominated in seconds (default=10)
    ```

    """

    fetchers: List[PublisherInterfaceT] = []

    @staticmethod
    def convert_to_publisher(client: PragmaClient):
        client.__class__ = PragmaPublisherClient
        return client

    def add_fetchers(self, fetchers: List[PublisherInterfaceT]):
        self.fetchers.extend(fetchers)

    def add_fetcher(self, fetcher: PublisherInterfaceT):
        self.fetchers.append(fetcher)

    def update_fetchers(self, fetchers: List[PublisherInterfaceT]):
        self.fetchers = fetchers

    def get_fetchers(self):
        return self.fetchers

    async def fetch(
        self, filter_exceptions=True, return_exceptions=True, timeout_duration=10
    ) -> List[any]:
        tasks = []
        timeout = aiohttp.ClientTimeout(
            total=timeout_duration
        )  # 10 seconds per request
        async with aiohttp.ClientSession(timeout=timeout) as session:
            for fetcher in self.fetchers:
                data = fetcher.fetch(session)
                tasks.append(data)
            result = await asyncio.gather(*tasks, return_exceptions=return_exceptions)
            if filter_exceptions:
                result = [subl for subl in result if not isinstance(subl, Exception)]
            return [val for subl in result for val in subl]

    def fetch_sync(self) -> List[any]:
        results = []
        for fetcher in self.fetchers:
            data = fetcher.fetch_sync()
            results.extend(data)
        return results
