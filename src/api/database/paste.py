from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .user import UserModel


class PasteModel(Base):
    __tablename__ = "paste"

    hash: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("user.id"))
    path: Mapped[str]

    user: Mapped[Optional[UserModel]] = relationship()
