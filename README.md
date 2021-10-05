# THE EYE
A service api that will collect those events from some applications
The objective is use these data to analyze user behavior

## WEBAPI with PYTHON
In this API was used: 
- Python as main language,
- Flask as Web Framework,
- Postgresql to store data,
- Redis as queue broker,
- Celery to manage tasks,
- Marshmallow as serializer,
- Docker to start the diferents services


### API Docs

- JSON file at docs/farmers_market.postman_collection.json
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
$ mv .envfile .env
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
$ make up
```

### Seeds

- There is not seed for run manually. Everything will run during the build 


### Development

This project was built thinking about three main entities:
- Event: It will handle event data associated to a session
- Session: It will handle session info and can be associated with many events
- Error: It will store data related with failed events validations




