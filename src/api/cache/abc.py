from redis import Redis


class Cache:
    def __init__(self, cache: Redis) -> None:
        self.cache = cache
    
    def __del__(self) -> None:
        self.cache.close()
