from main import db
from os import system
from loguru import logger
from config import config
from click import confirm

#Script para executar durante o desenvolvimento
#do banco
#O banco é deletado e criado um novo
#Se o banco existir, verifica se o dev quer excluir
#Se o banco não existir, cria com create_all

if __name__ == "__main__":
    #Verifica se o db existe
    try:
        if config.verify_file_db():
            delete = confirm(text="Você tem certeza que quer DELETAR o BANCO DE DADOS? Essa ação é IRREVERSÍVEL")
            if delete == True:
                system(f"rm {config.DB_PATH}")
                logger.warning("DB deletado")
            else:
                logger.info("Você escolheu não excluir o banco :)")
        else:
            raise Exception
    #Cria o banco de dados
    except:
        db.create_all()
        logger.info("O banco de dados foi criado com create_all.")