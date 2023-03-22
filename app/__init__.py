from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager
import re
app = Flask(__name__)
login_manager=LoginManager(app)
# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

from app import views