from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={"autoflush": False})

def init_db(app):
    db.init_app(app)
