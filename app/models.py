from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = "user_accounts"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, psw):
        return check_password_hash(self.password, psw)


class Book(db.Model):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    authors: Mapped[List["Author"]] = relationship(
        back_populates="books", cascade='all, delete-orphan'
    )
    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, name={self.name!r}), authors={self.authors!r})"

class Author(db.Model):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    books: Mapped[List[Book]] = relationship(back_populates="authors")
    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r})"
