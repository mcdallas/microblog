from src.db import init_db
from src import create_app

app = create_app()

with app.app_context():
    init_db()
