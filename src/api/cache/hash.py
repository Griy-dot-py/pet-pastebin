from typing import Any
from redis import Redis


class HashCache:
    def __init__(self, cache: Redis) -> None:
        self.__cache = cache
    
    def __del__(self) -> None:
        self.__cache.close()
    
    def get_hash(self) -> str:
        key: bytes = self.__cache.randomkey()
        self.__cache.delete(key)
        return key.decode()
