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
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, int, bytes, float]) -> uuid:
        """
         store the input data in Redis using the random
         key and return the key.
        Args:
            data (_type_): _description_
        """
        red_key = str(uuid.uuid4())
        self.__redis.set(red_key, data)
        return red_key
