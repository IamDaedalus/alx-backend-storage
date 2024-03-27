#!/usr/bin/env python3

import redis
from typing import Union, Optional, Callable
import uuid

from redis.commands.core import ResponseT


class Cache:
    def __init__(self):
        """ this is the init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ this is the store method """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
