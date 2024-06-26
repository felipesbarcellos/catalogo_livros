from flask import Flask
from app.models import db, login_manager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'a_chave_mais_secreta_de_todas_as_chaves'

login_manager.init_app(app)
db.init_app(app)
app.app_context().push()