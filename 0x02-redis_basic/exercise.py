#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union, Optional


class Cache:
    """
    Cache class for interacting with Redis
    """

    def __init__(self):
        """
        Initialize the Cache instance with a Redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a random key
        Args:
            data: Data to store, can be a string, bytes, int, or float
        Returns:
            Randomly generated key used for storing the data in Redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @getter
    def get(
           self, key: str, fn: Optional[callable]
           ) -> Union[int, str, bytes, float]:
        """
        get method that take a key string argument and an
        optional Callable argument named fn.
        This callable will be used to convert
        the data back to the desired format.

        Args:

            fn (_type_, optional): _description_. Defaults to None.
        """
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        get value as a string
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int():
        """
        get value as a integer
        """
        return self.get(key, int)
