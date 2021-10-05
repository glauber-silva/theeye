clean:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name __pycache__ -delete
	rm -f .coverage
	rm -rf htmlcov

build:
	docker-compose build --no-cache

start:
	docker-compose up -d

stop:
	docker-compose stop

db_upgrade:
	docker-compose run --rm web python manage.py db upgrade head