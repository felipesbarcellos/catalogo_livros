from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Author, Book
from loguru import logger

engine = create_engine("sqlite:///books.db", echo=True)

def select_all_books():
    session = Session(engine)
    stmt = select(Book).where()
    for book in session.scalars(stmt):
        logger.info(book)

def select_all_authors():
    session = Session(engine)
    stmt = select(Author).where()
    for author in session.scalars(stmt):
        logger.info(author)

def create_book(nome:str, authors: list[Author]):
    session = Session(engine)
    book = Book(name=nome, authors=authors)
    session.add(book)
    session.commit()
    ...
    pass

if __name__ == "__main__":
    #create_book("A mulher de trinta anos", [Author(first_name = "Honoré de", last_name = "Balzac")])
    #create_book("Quincas Borbas", [Author(first_name = "Machado de", last_name = "Assis")])
    #select_all_books()
    #select_all_authors()
    pass