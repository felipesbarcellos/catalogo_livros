from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    authors: Mapped[List["Author"]] = relationship(
        back_populates="book", cascade='all, delete-orphan'
    )
    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, name={self.name!r}), authors={self.authors!r})"

class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    books: Mapped[List[Book]] = relationship(back_populates="authors")
    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r})"

if __name__ == "__main__":
    engine = create_engine("sqlite:///books.db", echo=True)
    Base.metadata.create_all(engine)