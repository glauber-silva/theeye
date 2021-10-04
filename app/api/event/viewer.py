import logging

from flask import make_response, jsonify, request
from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.databases import db

from app.databases.models import Event

ns = Namespace("event", description="Manage Events data")


@ns.route("/")
class EventsApi(Resource):

    def get(self):
        events = Event.query.order_by(Event.timestamp).all()
        return make_response(jsonify({"events": events}), HTTPStatus.OK)

    def post(self):
        body = request.json
        try:
            event = Event(**body)
            db.session.add(event)
            db.session.commit()
            response = make_response(jsonify({"message": "Created"}), HTTPStatus.CREATED)
        except Exception as e:
            message = f"Problems saving Event with session_id: {body['session_id']} and data: {body} | {e}"
            logging.exception(message)
            db.session.rollback()
            response = make_response(jsonify({"message": message}), HTTPStatus.BAD_REQUEST)
        finally:
            db.session.close()

        return response
