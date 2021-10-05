import time

from logging import getLogger
from app.consumers import celery

logger = getLogger(__name__)


@celery.task(name="tasks.sleep")
def sleep(_time, name):
    logger.info("")
    time.sleep(_time)
    return name
