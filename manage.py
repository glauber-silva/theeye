from flask_script import Manager

from app import create_app

app = create_app()
manager = Manager(app)


@manager.command
def about():
    return "THE EYE: user behavior data aggregator"


if __name__ == "__main__":
    manager.run()


# TODO: Create database
# TODO: Create Models (Session, Event, Errors)
# TODO: Create endpoints
# TODO: Add Schema validators
# TODO: Create tests
# TODO: Improve post event resource
