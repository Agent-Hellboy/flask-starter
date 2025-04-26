from app.models import User


def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 302  # Should redirect to login


def test_registration(client, app):
    # Test successful registration
    resp = client.post(
        "/register",
        data={"username": "princekr", "password": "testpass123", "submit": "Register"},
        follow_redirects=True,
    )
    assert resp.status_code == 200
    assert b"Login" in resp.data  # Should redirect to login page

    with app.app_context():
        assert User.query.count() == 1
        user = User.query.first()
        assert user.username == "princekr"


def test_login(client, app):
    # First register a user
    client.post(
        "/register",
        data={"username": "testuser", "password": "testpass123", "submit": "Register"},
    )

    # Try to login with correct credentials
    resp = client.post(
        "/login",
        data={"username": "testuser", "password": "testpass123", "submit": "Login"},
        follow_redirects=True,
    )
    assert resp.status_code == 200
    assert b"Welcome" in resp.data

    # Try to login with incorrect password
    resp = client.post(
        "/login",
        data={"username": "testuser", "password": "wrongpass", "submit": "Login"},
    )
    assert resp.status_code == 200
    assert b"Invalid username or password" in resp.data


def test_logout(client):
    # First login
    client.post(
        "/register",
        data={"username": "testuser", "password": "testpass123", "submit": "Register"},
    )
    client.post(
        "/login",
        data={"username": "testuser", "password": "testpass123", "submit": "Login"},
    )

    # Then logout
    resp = client.get("/logout", follow_redirects=True)
    assert resp.status_code == 200
    assert b"Login" in resp.data  # Should redirect to login page


def test_profile_requires_login(client):
    resp = client.get("/profile")
    assert resp.status_code == 401  # Flask-Login returns 401 for unauthorized access


def test_profile_with_login(client):
    # Register and login
    client.post(
        "/register",
        data={"username": "testuser", "password": "testpass123", "submit": "Register"},
    )
    client.post(
        "/login",
        data={"username": "testuser", "password": "testpass123", "submit": "Login"},
    )

    # Access profile
    resp = client.get("/profile")
    assert resp.status_code == 200
    assert b"testuser" in resp.data
    assert b"User" in resp.data  # Should show account type


def test_home_with_login(client):
    # Register and login
    client.post(
        "/register",
        data={"username": "testuser", "password": "testpass123", "submit": "Register"},
    )
    client.post(
        "/login",
        data={"username": "testuser", "password": "testpass123", "submit": "Login"},
    )

    # Access home
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Welcome" in resp.data
    assert b"testuser" in resp.data


def test_invalid_registration(client):
    # Try to register with invalid username
    resp = client.post(
        "/register",
        data={"username": "test@user", "password": "testpass123", "submit": "Register"},
    )
    assert resp.status_code == 200
    assert b"Username must contain only characters and numbers" in resp.data

    # Try to register with empty fields
    resp = client.post(
        "/register", data={"username": "", "password": "", "submit": "Register"}
    )
    assert resp.status_code == 200
    assert b"This field is required" in resp.data

    # Try to register with existing username
    client.post(
        "/register",
        data={"username": "testuser", "password": "testpass123", "submit": "Register"},
    )
    resp = client.post(
        "/register",
        data={"username": "testuser", "password": "testpass123", "submit": "Register"},
    )
    assert resp.status_code == 200
    assert b"Account already exists" in resp.data
