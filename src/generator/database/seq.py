from typing import Iterator
from dataclasses import dataclass

from sqlalchemy import Sequence, select
from sqlalchemy.orm import Session


@dataclass
class UniqueNumberSequence(Iterator):
    seq: Sequence
    session: Session
    
    def __next__(self) -> int:
        return self.session.scalar(
            select(self.seq.next_value())
        )
    