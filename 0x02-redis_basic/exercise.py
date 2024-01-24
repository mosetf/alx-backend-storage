#!/usr/bin/env python3
"""Exercise for Redis"""
import redis
import uuid


class Cache:
    """Cache class"""
    def __init__(self):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: bytes) -> str:
        """Store data in Redis"""
        key = str(self._redis.incr("count:{}".format(data)), "utf-8")
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: object) -> str:
        """Get data from Redis"""
        data = self._redis.get(key)
        if data:
            return fn(data)
        return None

    def get_str(self, data: bytes) -> str:
        """Convert bytes to string"""
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """Convert bytes to int"""
        return int.from_bytes(data, "big")
        