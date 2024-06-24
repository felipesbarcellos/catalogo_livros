from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Author, Book

engine = create_engine("sqlite:///books.db", echo=True)

def select_all_books():
    session = Session(engine)
    stmt = select(Book).where()
    for book in session.scalars(stmt):
        print(book)

def select_all_authors():
    session = Session(engine)
    stmt = select(Author).where()
    for author in session.scalars(stmt):
        print(author)

def create_book(nome:str, authors: list[Author]):
    session = Session(engine)
    book = Book(name=nome, authors=authors)
    session.add(book)
    session.commit()
    ...
    pass

if __name__ == "__main__":
    # select_all_books()
    pass