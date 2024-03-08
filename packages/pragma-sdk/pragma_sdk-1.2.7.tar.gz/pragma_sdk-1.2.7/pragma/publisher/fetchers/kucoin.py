import asyncio
import logging
import time
from typing import List, Union

import requests
from aiohttp import ClientSession

from pragma.core.assets import PragmaAsset, PragmaSpotAsset
from pragma.core.entry import SpotEntry
from pragma.core.utils import currency_pair_to_pair_id
from pragma.publisher.types import PublisherFetchError, PublisherInterfaceT

logger = logging.getLogger(__name__)


class KucoinFetcher(PublisherInterfaceT):
    BASE_URL: str = "https://api.kucoin.com/api/v1/market/orderbook/level1"
    SOURCE: str = "KUCOIN"

    publisher: str

    def __init__(self, assets: List[PragmaAsset], publisher):
        self.assets = assets
        self.publisher = publisher

    async def _fetch_pair(
        self, asset: PragmaSpotAsset, session: ClientSession
    ) -> Union[SpotEntry, PublisherFetchError]:
        pair = asset["pair"]
        if pair == ("STRK", "USD"):
            pair = ("STRK", "USDT")
        url = self.format_url(pair[0], pair[1])
        async with session.get(url) as resp:
            if resp.status == 404:
                return PublisherFetchError(
                    f"No data found for {'/'.join(pair)} from Kucoin"
                )
            result = await resp.json()
            if result["data"] == None:
                return await self.operate_usdt_hop(asset, session)
            return self._construct(asset, result)

    def _fetch_pair_sync(
        self, asset: PragmaSpotAsset
    ) -> Union[SpotEntry, PublisherFetchError]:
        pair = asset["pair"]
        if pair == ("STRK", "USD"):
            pair = ("STRK", "USDT")
        url = self.format_url(pair[0], pair[1])
        resp = requests.get(url)
        if resp.status_code == 404:
            return PublisherFetchError(
                f"No data found for {'/'.join(pair)} from Kucoin"
            )
        result = resp.json()
        if result["data"] == None:
            return self.operate_usdt_hop_sync(asset)
        return self._construct(asset, result)

    async def fetch(
        self, session: ClientSession
    ) -> List[Union[SpotEntry, PublisherFetchError]]:
        entries = []
        for asset in self.assets:
            if asset["type"] != "SPOT":
                logger.debug("Skipping Kucoin for non-spot asset %s", asset)
                continue
            entries.append(asyncio.ensure_future(self._fetch_pair(asset, session)))
        return await asyncio.gather(*entries, return_exceptions=True)

    def fetch_sync(self) -> List[Union[SpotEntry, PublisherFetchError]]:
        entries = []
        for asset in self.assets:
            if asset["type"] != "SPOT":
                logger.debug("Skipping Kucoin for non-spot asset %s", asset)
                continue
            entries.append(self._fetch_pair_sync(asset))
        return entries

    def format_url(self, quote_asset, base_asset):
        url = f"{self.BASE_URL}?symbol={quote_asset}-{base_asset}"
        return url

    async def operate_usdt_hop(self, asset, session) -> SpotEntry:
        pair = asset["pair"]
        url_pair1 = self.format_url(asset["pair"][0], "USDT")
        async with session.get(url_pair1) as resp:
            if resp.status == 404:
                return PublisherFetchError(
                    f"No data found for {'/'.join(pair)} from Kucoin - hop failed for {pair[0]}"
                )
            pair1_usdt = await resp.json()
            if pair1_usdt["data"] == None:
                return PublisherFetchError(
                    f"No data found for {'/'.join(pair)} from Kucoin - hop failed for {pair[0]}"
                )
        url_pair2 = self.format_url(asset["pair"][1], "USDT")
        async with session.get(url_pair2) as resp:
            if resp.status == 404:
                return PublisherFetchError(
                    f"No data found for {'/'.join(pair)} from Kucoin - hop failed for {pair[1]}"
                )
            pair2_usdt = await resp.json()
            if pair2_usdt["data"] == None:
                return PublisherFetchError(
                    f"No data found for {'/'.join(pair)} from Kucoin - hop failed for {pair[1]}"
                )
        return self._construct(asset, pair2_usdt, pair1_usdt)

    def operate_usdt_hop_sync(self, asset) -> SpotEntry:
        pair = asset["pair"]
        url_pair1 = self.format_url(asset["pair"][0], "USDT")
        resp = requests.get(url_pair1)
        if resp.status_code == 404:
            return PublisherFetchError(
                f"No data found for {'/'.join(pair)} from Kucoin - hop failed for {pair[0]}"
            )
        pair1_usdt = resp.json()
        if pair1_usdt["data"] == None:
            return PublisherFetchError(
                f"No data found for {'/'.join(pair)} from Kucoin - hop failed for {pair[0]}"
            )
        url_pair2 = self.format_url(asset["pair"][1], "USDT")
        resp = requests.get(url_pair2)
        if resp.status_code == 404:
            return PublisherFetchError(
                f"No data found for {'/'.join(pair)} from Kucoin - hop failed for {pair[1]}"
            )
        pair2_usdt = resp.json()
        if pair2_usdt["data"] == None:
            return PublisherFetchError(
                f"No data found for {'/'.join(pair)} from Kucoin - hop failed for {pair[1]}"
            )
        return self._construct(asset, pair2_usdt, pair1_usdt)

    def _construct(self, asset, result, hop_result=None) -> SpotEntry:
        pair = asset["pair"]
        price = float(result["data"]["price"])
        if hop_result is not None:
            hop_price = float(hop_result["data"]["price"])
            price = hop_price / price
        timestamp = int(result["data"]["time"] / 1000)
        price_int = int(price * (10 ** asset["decimals"]))
        pair_id = currency_pair_to_pair_id(*pair)
        logger.info("Fetched price %d for %s from Kucoin", price, "/".join(pair))

        return SpotEntry(
            pair_id=pair_id,
            price=price_int,
            timestamp=timestamp,
            source=self.SOURCE,
            publisher=self.publisher,
        )
