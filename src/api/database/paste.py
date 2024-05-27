from database import Base, UserModel

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class PasteModel(Base):
    __tablename__ = "paste"
    
    hash: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    path: Mapped[str]
    
    user: Mapped[UserModel] = relationship()
