from http import HTTPStatus

from flask import make_response, jsonify
from flask_restx import Resource, Namespace

ns = Namespace("healthcheck", "Health check information")


@ns.route("/", methods=["GET"])
class Health(Resource):

    @ns.response(code=200, description="General check")
    def get(self):
        """
        Check API's health status
        :return:
        """

        # TODO: Add database check
        return make_response(jsonify({"status": "OK", "message": "Services Running"}), HTTPStatus.OK)
