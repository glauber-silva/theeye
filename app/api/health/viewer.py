import logging

from http import HTTPStatus

from flask import make_response, jsonify
from flask_restx import Resource, Namespace

from app.api.health.checks import db_available, queue_available


logger = logging.getLogger(__name__)

ns = Namespace("healthcheck", "Health check information")


@ns.route("/")
class Health(Resource):

    @ns.response(code=200, description="General check")
    def get(self):
        """
        Check API's health status
        :return:
        """
        services = {
            "celery": queue_available(),
            "database": db_available(),
        }

        return make_response(jsonify({"services": services}), HTTPStatus.OK)
