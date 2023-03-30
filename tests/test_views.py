from app.models import User


def test_home(client):
    resp = client.get("/")

    assert resp.status_code == 302


def test_registration(client, app):

    resp = client.post("/register", data={"username": "princekr", "password": "test"})

    with app.app_context():
        print(User.query.all())
        assert User.query.count() == 1
