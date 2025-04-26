from app.models import User


def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 302


def test_registration(client, app):
    client.post("/register", data={"username": "princekr", "password": "test"})

    with app.app_context():
        assert User.query.count() == 1
