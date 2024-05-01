#!/usr/bin/env python3
"""
exercise.py
"""

import uuid
import redis
from typing import Union


class Cache:
    """
    cash class
    """

    def __init__(self):
        """
        initializer...
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> str:
        """
         store the input data in Redis using the random
         key and return the key.
        Args:
            data (_type_): _description_
        """
        red_key = str(uuid.uuid4())
        self._redis.set(red_key, data)
        return red_key
