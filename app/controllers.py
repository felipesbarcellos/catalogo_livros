from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Author, Book
from loguru import logger
from models import db
from sqlalchemy import select

#Seleciona todos os livros
def select_all_books():
    books = db.session.execute(select(Book))
    for book in books:
        logger.info(book)

#Seleciona todos os autores
#def select_all_authors():
    #session = Session(engine)
    #stmt = select(Author).where()
    #for author in session.scalars(stmt):
    #    logger.info(author)

#Cria um novo livro
#def create_book(nome:str, authors: list[Author]):
 #   session = Session(engine)
  #  book = Book(name=nome, authors=authors)
   # session.add(book)
    #session.commit()
    #...
    #pass

if __name__ == "__main__":
    #create_book("A mulher de trinta anos", [Author(first_name = "Honoré de", last_name = "Balzac")])
    #create_book("Quincas Borbas", [Author(first_name = "Machado de", last_name = "Assis")])
    select_all_books()
    #select_all_authors()
    pass