.PHONY: test docker-setup docker-run functional-test docs

DATABASE_PASSWORD ?= test
REMOTE_URL ?= http://localhost:5000

docker-setup:
	docker-compose build
	DATABASE_PASSWORD=$(DATABASE_PASSWORD) \
		docker-compose run web python manage.py migrate

docker-run:
	docker-compose up

lint:
	pycodestyle . --exclude=docs

unit-test:
	coverage run --source='.' manage.py test
	coverage report

functional-test:
	python manage.py behave -e smoke.feature

test: lint unit-test functional-test

smoke:
	REMOTE_URL=$(REMOTE_URL) python manage.py behave -i smoke.feature

docs:
	cd docs/; make html
