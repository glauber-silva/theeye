import os

from flask import Flask

from app.api import api_bp
from app.api.health.viewer import ns as health
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig
from flask_cors import CORS


def create_app(deploy_env: str = os.getenv("FLASK_ENV", "Development")) -> Flask:
    app = Flask(__name__)
    configuration = {
        "Development": DevelopmentConfig,
        "Testing": TestingConfig,
        "Production": ProductionConfig
    }[deploy_env]

    app.config.from_object(configuration)

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
