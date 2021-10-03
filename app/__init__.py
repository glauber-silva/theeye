import os

from flask import Flask
from flask_migrate import Migrate

from app.api import api_bp
from app.api.health.viewer import ns as health
from app.api.event.viewer import ns as event
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig
from flask_cors import CORS
from app.databases import db

migrate = Migrate()


def create_app(deploy_env: str = os.getenv("FLASK_ENV", "Development")) -> Flask:
    app = Flask(__name__)
    configuration = {
        "Development": DevelopmentConfig,
        "Testing": TestingConfig,
        "Production": ProductionConfig
    }[deploy_env]

    app.config.from_object(configuration)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    with app.app_context():
        __configure_extensions(app)
    app.app_context().push()

    app.register_blueprint(api_bp)

    return app


def __configure_extensions(app: Flask):
    cors = CORS(app, resources={
        r"/*": {
            "origin": "*"
        }
    })
    cors.init_app(app)
    db.init_app(app)
    from app.databases import models
    _module_dir = os.path.dirname(os.path.abspath(__file__))
    migrate.init_app(app=app, db=db, directory=os.path.join(_module_dir, '..', 'migrations'))
