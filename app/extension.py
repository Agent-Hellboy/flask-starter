from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

login_manager = LoginManager()
db = SQLAlchemy()
admin = Admin()