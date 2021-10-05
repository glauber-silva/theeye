import logging

from flask import make_response, jsonify, request
from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.consumers import celery
from app.databases.models import Event

logger = logging.getLogger(__name__)

ns = Namespace("event", description="Manage Events data")


@ns.route("/")
class EventsApi(Resource):

    def get(self):
        events = Event.query.order_by(Event.timestamp).all()
        return make_response(jsonify({"events": events}), HTTPStatus.OK)

    def post(self):
        body = request.json
        try:
            task = celery.send_task("tasks.add_event", args=[body], kwargs={})
            response = make_response(jsonify({"message": "Event will be validated"}), HTTPStatus.ACCEPTED)
        except Exception as e:
            response = make_response(jsonify({"message": f"Problems inserting task to validate event {str(task)} {e}"}),
                                     HTTPStatus.BAD_REQUEST)

        return response