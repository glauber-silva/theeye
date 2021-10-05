import logging

from flask import make_response, jsonify, request
from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.api.error.schema import ErrorSchema
from app.databases.models import Error

ns = Namespace("error", description="Endpoint to list or retrieve errors ocurred during validation event data")


@ns.route("/")
class ErrorsApi(Resource):

    def get(self):
        errors = Error.query.order_by(Error.created_dt).all()
        result = ErrorSchema(many=True).dump(errors)
        return make_response(jsonify(result), HTTPStatus.OK)
