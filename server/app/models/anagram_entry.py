from sqlalchemy import String, Integer, DateTime, func, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database.session import Base


class AnagramEntry(Base):
    __tablename__ = "anagram_entries"
    __table_args__ = (
        UniqueConstraint("word", name="uq_anagram_entries_word"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    word: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    sorted_key: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now())