from typing import Optional

from .abc import Cache


class DataCache(Cache):
    EXPIRE = 60

    def get(self, key: str) -> Optional[str]:
        value: Optional[bytes] = self.cache.get(key)
        if value is not None:
            return value.decode()

    def set(self, key: str, value: str) -> None:
        self.cache.set(key, value, self.EXPIRE)

    def delete(self, key: str) -> None:
        self.cache.delete(key)
