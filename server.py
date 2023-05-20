from app import create_app
from app.extension import db 

app = create_app()

if __name__ == "__main__":
    app.debug = True
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000)
