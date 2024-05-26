from redis import Redis
from typing import Iterator
from dataclasses import dataclass, field
from itertools import count
from hash_func import hash_id


@dataclass
class UniqueNumberSequence:
    storage: Redis
    recomended_size: int
    iterator: Iterator[int] = field(default_factory=count)
    
    def fill_up(self, quantity: int) -> None:
        for number, _ in zip(self.iterator, range(quantity)):
            self.storage.set(hash_id(number), number)
    
    def start_loop(self) -> None:   
        while True:
            missing = self.recomended_size - self.storage.dbsize()
            if missing:
                self.fill_up(missing)
