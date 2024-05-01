#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union


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
    def get(self, key, fn=None):
        """
        get method that take a key string argument and an
        optional Callable argument named fn.
        This callable will be used to convert
        the data back to the desired format.

        Args:

            fn (_type_, optional): _description_. Defaults to None.
        """
        if fn and callable(fn):
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, key):
        """
        get value as a string
        """
        return self.get(key, str)

    def get_int(self, key):
        """
        get value as a integer
        """
        return self.get(key, int)
