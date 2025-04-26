from app.models import User


def test_user_methods():
    """Test all User model methods"""
    user = User(username="testuser", password="testpass")
    user.id = 1  # Simulate database assignment of ID

    # Test is_active
    assert user.is_active() is True

    # Test is_authenticated
    assert user.is_authenticated is True  # Now a property

    # Test is_anonymous
    assert user.is_anonymous() is False

    # Test is_admin
    assert user.is_admin() is False  # Should be False by default
    user.admin = True
    assert user.is_admin() is True

    # Test get_id
    assert user.get_id() == "1"  # Flask-Login expects string

    # Test string representation
    assert str(user) == "<User testuser>"
    assert repr(user) == "<User testuser>"
