#!/usr/bin/env python3

import redis
from typing import Optional, Union
import uuid


class Cache:
    """ this class stores a Redis instance """

    def __init__(self):
        """ this is the init method """
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ this is the store method """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
    

    def get(self, key: str, fn: Optional[callable] = None) -> Union[
            str, bytes, int, float]:
        """ this is the get method """
        if self._redis.get(key) is None:
            return None
        if fn is None:
            return self._redis.get(key)
        else:
            return fn(self._redis.get(key))


    def get_str(self, key: str) -> str:
        """ this is the get_str method """
        if self._redis.get(key) is None:
            return None
        return str(self._redis.get(key))


    def get_int(self, key: str) -> int:
        """ this is the get_int method """
        if not self._redis.exists(key):
            return None
        # https://stackoverflow.com/questions/34009653/convert-bytes-to-int
        return int.from_bytes(self._redis.get(key), byteorder='big')
