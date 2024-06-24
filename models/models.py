from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass

class Livro(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    authors: Mapped[List["Author"]] = relationship(
        back_populates="user", cascade='all, delete-orphan'
    )
    def __repr__(self) -> str:
        return f"Livro(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    book: Mapped["Livro"] = relationship(back_populates="authors")
    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r})"