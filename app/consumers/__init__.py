from celery import Celery

celery = Celery("tasks", include=["app.consumers.tasks"])

