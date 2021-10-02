import os

from flask import Blueprint
from flask_restx import Api

from app.api.health.viewer import ns as health

api_bp = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_bp, version="0.1", title="THE EYE",
          description="THE EYE: user behavior data aggregator", doc="/docs")

api.add_namespace(health)
