from flask import Flask
from flask_admin.contrib.sqla import ModelView

from .extension import admin, db, login_manager
from .models import User
from .views import main


def create_app(db_url="sqlite:///users.db"):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url

    app.config["SECRET_KEY"] = "FesC9cBSuxakv9yN0vBY"

    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.register_blueprint(main)
    if not admin._views:
        admin.add_view(
            ModelView(User, db.session, name="User Management", endpoint="admin_user")
        )
    return app
