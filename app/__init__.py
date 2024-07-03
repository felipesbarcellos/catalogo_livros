from flask import Flask
from app.models import db, login_manager
from config import config

#Instancia o Flask
app = Flask(__name__)

#Configura as variáveis do flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{config.DB_NAME}'
app.config['SECRET_KEY'] = 'a_chave_mais_secreta_de_todas_as_chaves'

#inicializa módulos do servidor
login_manager.init_app(app)
db.init_app(app)

#Adiciona o contexto para o banco de dados
app.app_context().push()