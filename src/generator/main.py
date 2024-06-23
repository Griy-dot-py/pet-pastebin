from typing import Iterator

from redis import Redis
from utils import hash_id


class HashGenerator:
    def __init__(
        self,
        storage: Redis,
        recomended_size: int,
        iterator: Iterator[int],
    ) -> None:
        self.__storage = storage
        self.__recom_size = recomended_size
        self.__iterator = iterator

    def start(self) -> None:
        while True:
            missing = self.__recom_size - self.__storage.dbsize()
            if missing:
                self.yield_hashes(missing)

    def yield_hashes(self, quantity: int) -> None:
        for _ in range(quantity):
            new = next(self.__iterator)
            self.__storage.set(hash_id(new), new)
