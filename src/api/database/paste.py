from database import Base, User

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Paste(Base):
    __tablename__ = "paste"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    path: Mapped[str]
    
    user: Mapped[User] = relationship()
