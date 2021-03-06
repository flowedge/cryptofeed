'''
Copyright (C) 2017-2020  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from cryptofeed.defines import OKEX, OKEX_SWAP, OKEX_FUTURES
from cryptofeed.exchange.okcoin import OKCoin

import aiohttp
import requests
from yapic import json

from cryptofeed.defines import OKEX, LIQUIDATIONS, BUY, SELL
from cryptofeed.exchange.okcoin import OKCoin


class OKEx(OKCoin):
    """
    OKEx has the same api as OKCoin, just a different websocket endpoint
    """
    id = OKEX
    api = 'https://www.okex.com/api/'

    def __init__(self, pairs=None, channels=None, callbacks=None, **kwargs):
        super().__init__(pairs=pairs, channels=channels, callbacks=callbacks, **kwargs)
        self.address = 'wss://real.okex.com:8443/ws/v3'
        self.book_depth = 200

    @staticmethod
    def get_active_symbols_info():
        return requests.get(OKEx.api + 'futures/v3/instruments').json()

    @staticmethod
    def get_active_symbols():
        symbols = []
        for data in OKEx.get_active_symbols_info():
            symbols.append(data['instrument_id'])
        return symbols
    
class OKEx_swap(OKCoin):
    """
    OKEx has the same api as OKCoin, just a different websocket endpoint
    """
    id = OKEX_SWAP
    api = 'https://www.okex.com/api/'

    def __init__(self, pairs=None, channels=None, callbacks=None, **kwargs):
        super().__init__(pairs=pairs, channels=channels, callbacks=callbacks, **kwargs)
        self.address = 'wss://real.okex.com:8443/ws/v3'
        self.book_depth = 200
        self.open_interest = {}

    @staticmethod
    def get_active_symbols_info():
        return requests.get(OKEx.api + 'futures/v3/instruments').json()

    @staticmethod
    def get_active_symbols():
        symbols = []
        for data in OKEx.get_active_symbols_info():
            symbols.append(data['instrument_id'])
        return symbols
    
class OKEx_futures(OKCoin):
    """
    OKEx has the same api as OKCoin, just a different websocket endpoint
    """
    id = OKEX_FUTURES
    api = 'https://www.okex.com/api/'

    def __init__(self, pairs=None, channels=None, callbacks=None, **kwargs):
        super().__init__(pairs=pairs, channels=channels, callbacks=callbacks, **kwargs)
        self.address = 'wss://real.okex.com:8443/ws/v3'
        self.book_depth = 200

    @staticmethod
    def get_active_symbols_info():
        return requests.get(OKEx.api + 'futures/v3/instruments').json()

    @staticmethod
    def get_active_symbols():
        symbols = []
        for data in OKEx.get_active_symbols_info():
            symbols.append(data['instrument_id'])
        return symbols
