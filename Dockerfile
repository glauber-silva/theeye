FROM python:3.8-alpine

RUN apk add --no-cache --update libffi-dev gcc git openssh-client linux-headers alpine-sdk \
   openssl-dev python3-dev musl-dev openssh netcat-openbsd postgresql-dev

RUN pip install pip==21.2.4  setuptools==41.0.1 --no-cache-dir

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir


copy app app/

COPY migrations migrations/


COPY wsgi.py .
COPY uwsgi.ini .
COPY manage.py .
COPY entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

CMD ["/bin/sh", "/app/entrypoint.sh"]
