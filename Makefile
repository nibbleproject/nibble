.PHONY: test docker-setup docker-run functional-test docs

MINICOMI_DATABASE_PASSWORD ?= test
REMOTE_URL ?= http://localhost:5000

docker-setup:
	docker-compose build
	MINICOMI_DATABASE_PASSWORD=$(MINICOMI_DATABASE_PASSWORD) \
		docker-compose run web python manage.py migrate

docker-run:
	docker-compose up

lint:
	pycodestyle . --exclude=docs

unit-test:
	coverage run --source='.' manage.py test
	coverage report

functional-test:
	python manage.py behave

test: lint unit-test functional-test

smoke:
	REMOTE_URL=$(REMOTE_URL) python manage.py behave features/smoke.feature 

docs:
	cd docs/; make html
