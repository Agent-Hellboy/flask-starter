from app import create_app
from app.extension import db, login_manager
from app.models import User


def test_create_app():
    """Test the application factory."""
    app = create_app("sqlite://")

    # Test configuration
    assert app.config["SQLALCHEMY_DATABASE_URI"] == "sqlite://"
    assert app.config["SECRET_KEY"] == "FesC9cBSuxakv9yN0vBY"

    # Test that extensions are initialized
    assert hasattr(app, "extensions")
    assert "sqlalchemy" in app.extensions
    assert "admin" in app.extensions

    # Test blueprint registration
    assert "main" in app.blueprints

    # Test database functionality
    with app.app_context():
        db.create_all()

        # Test that we can create and query a user
        user = User(username="testuser", password="testpass123")
        db.session.add(user)
        db.session.commit()

        assert User.query.count() == 1
        assert User.query.first().username == "testuser"

        # Test that the user loader is working
        assert login_manager._user_callback is not None
        loaded_user = login_manager._user_callback(str(user.id))
        assert loaded_user is not None
        assert loaded_user.username == "testuser"

        db.session.remove()
        db.drop_all()


def test_user_loader():
    """Test the user loader function."""
    app = create_app("sqlite://")

    with app.app_context():
        db.create_all()

        # Create a test user
        user = User(username="testuser", password="testpass123")
        db.session.add(user)
        db.session.commit()

        # Test the user loader
        loaded_user = login_manager._user_callback(str(user.id))
        assert loaded_user is not None
        assert loaded_user.username == "testuser"

        # Test with non-existent user
        loaded_user = login_manager._user_callback("999")
        assert loaded_user is None

        db.session.remove()
        db.drop_all()
