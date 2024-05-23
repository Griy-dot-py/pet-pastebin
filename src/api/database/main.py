from typing import Optional

from sqlalchemy import select


from database import Session, Paste


class Database:    
    @staticmethod       
    def add(paste: Paste) -> None:
        with Session() as session:
            with session.begin():
                session.add(paste)
    
    @staticmethod
    def get(id: int) -> Optional[Paste]:
        with Session() as session:
            return session.scalar(select(Paste).filter_by(id=id))
