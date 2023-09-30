from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'  # cria o banco de dados
app.config['SECRET_KEY'] = '6df62f064495dbdf96daac6278e3927b'
app.config['UPLOAD_FOLDER'] = 'static/fotos_posts'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'  # caso o usuário não esteja logado

from fakepinterest import routes
