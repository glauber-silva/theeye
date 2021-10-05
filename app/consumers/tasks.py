import time

from logging import getLogger

from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound

from app.api.event.schema import EventSchema
from app.consumers import celery
from app.databases import db

logger = getLogger(__name__)


@celery.task(name="tasks.sleep")
def sleep(_time, name):
    time.sleep(_time)
    return name


@celery.task(name="tasks.add_event")
def add_event(data):
    """
    This function will validate event data and timestamp before create a new event.
    If everything is ok, create event if not will add a new error
    :param data:
    :return: None
    """
    logger.info("Validating Event Data:")
    try:
        event = EventSchema().load(data)
        db.session.add(event)
        db.session.commit()
        logger.info("Event data validated")
        logger.info(f"Event : {data}")
    except ValidationError as e:
        logger.error(f"Problems validating Event Data: {e.messages}")
        db.session.rollback()
    except NoResultFound as e:
        logger.error(f"Session {data['session_id']} not found in session table")
        db.session.rollback()
    finally:
        db.session.close()
