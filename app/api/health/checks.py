from app.databases import db
from app.consumers import celery


def db_available():
    try:
        res = db.session.execute("SELECT COUNT(version_num) from alembic_version")
        db.session.close()
        if res.scalar() == 1:
            return {"database": "OK"}
    except Exception as e:
        return {"database": "ERROR", "error": str(e)}


def queue_available():
    try:
        time = 0.1
        name = "theeye"

        task = celery.send_task("tasks.sleep", args=[time, name], kwargs={})

        if task.id:
            message = {"queue": "OK"}
        else:
            message = {"queue": "ERROR", "error": str(task)}
    except Exception as e:
        message = {"queue": "ERROR", "error": str(e)}

    return message