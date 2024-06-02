from .abc import Cache


class HashCache(Cache):
    def get_hash(self) -> str:
        key = self.cache.randomkey().decode()
        self.cache.delete(key)
        return key
