import logging

from flask import make_response, jsonify, request
from flask_restx import Namespace, Resource
from http import HTTPStatus

from app.databases import db
from app.databases.models import Session

ns = Namespace("session", description="Manage sessions used to save events")


@ns.route("/")
class SessionApi(Resource):

    def post(self):
        """
        This will create a new session
        """
        try:
            session = Session()
            db.session.add(session)
            db.session.commit()
            logging.info("Session created")
            response = make_response(jsonify({"session_id": session.id}), HTTPStatus.OK)
        except Exception as e:
            message = f"Problems generating session: {e}"
            logging.exception(message)
            db.session.rollback()
            response = make_response(jsonify({"error": message}), HTTPStatus.BAD_REQUEST)
        finally:
            db.session.close()

        return response
