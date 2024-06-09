from typing import Callable, Optional, Any

from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase


class Database:    
    def __init__(self, sessionmaker: sessionmaker, model: DeclarativeBase) -> None:
        self.Session: Callable[..., Session] = sessionmaker
        self.model = model
    
    def add(self, model: DeclarativeBase) -> None:
        with self.Session() as session:
            with session.begin():
                session.add(model)
    
    def get(self, identifier: Any) -> Optional[DeclarativeBase]:
        with self.Session() as session:
            return session.get(self.model, identifier)

    def delete(self, identifier: Any) -> None:
        with self.Session() as session:
            with session.begin():
                model = self.get(identifier)
                session.delete(model)
