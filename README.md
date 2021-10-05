# THE EYE
A service api that will collect those events from some applications. 

The objective is use these data to analyze user behavior.

## WEBAPI with PYTHON
In this API was used: 
- Python as main language,
- Flask as Web Framework,
- Postgresql to store data,
- Redis as queue broker,
- Celery to manage tasks,
- Marshmallow as serializer,
- Docker to virtualization service


### API Docs

- JSON file at contrib/theeye.postman_collection.json
- Also It is possible to see a swagger doc in `http://localhost:5000/api/docs`

### Running the services

1 - 1. Install [Docker](https://docs.docker.com/engine/install/ubuntu/) and [Docker Compose](https://docs.docker.com/compose/install/)


2 - Clone: `git clone https://github.com/glauber-silva/theeye.git`

3 - Access the package:
```
$ cd theeye
```
4 - Configure env file
```
$ mv contrib/.env.config .env
```
5 - Build the project
```
$ make build
```
6 - Upgrade the database
```
$ make db_upgrade
```
7 - Run services
```
$ make start
```

### Seeds

- There is not seed for run manually. Everything will run during the build 


### About the Project

This project was built thinking about three main entities:
- Event: It will handle event data associated to a session
- Session: It will handle session info and can be associated with many events
- Error: It will store data related with failed events validations


Before adding the Event it is necessary to generate a session UUID on the session endpoint. It should be used in the session_id attribute of the Event payload.

Events are not processed in real time. For this, when the inclusion of an event is requested, a message in the response is sent informing that the information will be validated. Behind the scenes a task is added to the broker. For this, celery and redis are used.

There is a worker that will process these tasks and do the validations. In case of success the event is included. In case of failure it will be included as Error.
