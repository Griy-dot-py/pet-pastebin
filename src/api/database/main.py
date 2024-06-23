from typing import Any, Callable, Optional

from sqlalchemy.orm import Session, sessionmaker


class Database[T]:
    def __init__(self, sessionmaker: sessionmaker, model: T) -> None:
        self.Session: Callable[..., Session] = sessionmaker
        self.model = model

    def add(self, model: T) -> None:
        with self.Session() as session:
            with session.begin():
                session.add(model)

    def get(self, identifier: Any) -> Optional[T]:
        with self.Session() as session:
            return session.get(self.model, identifier)

    def delete(self, identifier: Any) -> None:
        with self.Session() as session:
            with session.begin():
                model = self.get(identifier)
                session.delete(model)
