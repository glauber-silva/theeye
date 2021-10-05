import time

from logging import getLogger

from marshmallow import ValidationError

from app.api.event.schema import EventSchema
from app.consumers import celery
from app.databases import db
from app.databases.models import Error

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
        logger.info(f"Event data validated: {data}")
    except ValidationError as e:
        message = f"Problems validating Event Data: {e.messages}"
        logger.error(message)
        error = Error(data=data, message=message)
        db.session.add(error)
        db.session.commit()
    finally:
        db.session.rollback()
        db.session.close()
