from .extension import db


class User(db.Model):
    """User model that implements Flask-Login UserMixin interface."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    admin = db.Column(db.Boolean, default=False)

    def is_active(self) -> bool:
        """Return True as all users are active by default."""
        return True

    @property
    def is_authenticated(self) -> bool:
        """Return True as all users are authenticated by default."""
        return True

    def is_anonymous(self) -> bool:
        """Return False as anonymous users are not supported."""
        return False

    def is_admin(self) -> bool:
        """Return True if the user has admin privileges."""
        return bool(self.admin)

    def get_id(self) -> str:
        """Return the user ID as a unicode string."""
        return str(self.id)

    def __repr__(self) -> str:
        """Return string representation of the user."""
        return f"<User {self.username}>"
