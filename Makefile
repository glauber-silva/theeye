clean:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name __pycache__ -delete
	rm -f .coverage
	rm -rf htmlcov

build:
	docker-compose build --no-cache

up:
	docker-compose up -d


about:
	docker-compose run --rm web python manage.py about


db_init:
	docker-compose run --rm web python manage.py db init

migrate:
	docker-compose run --rm web python manage.py db migrate

db_upgrade:
	docker-compose run --rm web python manage.py db upgrade head