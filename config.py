from os import path

#Cria a configuração do software
class Config:
    def __init__(self):
        self.MAIN_PATH = self.get_main_path()
        self.DB_NAME = "site.db"
        self.DB_PATH = self.get_db_path()

    #Define o path inicial do software
    def get_main_path(self):
        dir_path = path.dirname(path.realpath(__file__))
        return dir_path
    
    #Define o path do banco de dados sqlite
    def get_db_path(self):
        dir_path = path.join(self.MAIN_PATH, 'instance')
        dir_path = f"{dir_path}/{self.DB_NAME}"
        return dir_path
    
    #Verifica se o caminho do banco existe
    def verify_file_db(self):
        return path.isfile(self.DB_PATH)

#Instancia as configurações do software
config = Config()