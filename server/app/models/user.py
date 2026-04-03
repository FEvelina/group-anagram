from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database.session import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    points: Mapped[int] = mapped_column(Integer, default=0, nullable=False)