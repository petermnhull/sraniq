#!make

server:
	pipenv run python3 -m scripts.server 

worker:
	pipenv run python3 -m scripts.worker

redis:
	docker-compose up -d redis

test:
	pipenv run coverage run --source sraniq/ -m pytest tests/
	pipenv run coverage report

black:
	pipenv run black . --line-length=100

lint:
	pipenv run flake8 . --max-line-length=100

mypy:
	pipenv run mypy .

fmt: black mypy lint
