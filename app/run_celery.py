from app import create_app
from app.consumers import celery
from app.consumers.tasks import *

application = create_app()

TaskBase = celery.Task


class ContextTask(TaskBase):
    abstract = True

    def __call__(self, *args, **kwargs):
        with application.app_context():
            return TaskBase.__call__(self, *args, **kwargs)


celery.Task = ContextTask
