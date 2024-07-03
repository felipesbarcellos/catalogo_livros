from datetime import datetime
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column

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
    reviews: Mapped[List["Review"]] = relationship()
    bio: Mapped[str] = mapped_column(nullable=True)
    location:Mapped[str] = mapped_column(nullable=True)
    profile_picture:Mapped[str] = mapped_column(nullable=True)


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, psw):
        return check_password_hash(self.password, psw)

class Review(db.Model):
    __tablename__ = "reviews_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("user_accounts.id"))
    content: Mapped[str]
    created_at: Mapped[datetime]

    def __init__(self, usuario_id, content) -> None:
        self.created_at = datetime.now()
        self.usuario_id = usuario_id
        self.content = content
    def __repr__(self) -> str:
        return f"Review(id={self.id!r}, content={self.content!r})"



author_book_table = db.Table(
    "author_book_table",
    db.metadata,
    Column("author_id", ForeignKey("authors_table.id")),
    Column("book_id", ForeignKey("books_table.id")),
)

class Book(db.Model):
    __tablename__ = "books_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    isbn: Mapped[int]
    reviews: Mapped[list[Review]] = relationship()
    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, name={self.name!r})"

class Author(db.Model):
    __tablename__ = "authors_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    livros: Mapped[list[Book]] = relationship(secondary=author_book_table)
    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r})"

class Shelf(db.Model):
    __tablename__ = "shelf_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[User] = mapped_column(ForeignKey("user_accounts.id"))