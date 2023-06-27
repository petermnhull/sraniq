#!make

server:
	python -m scripts.server 

worker:
	python -m scripts.worker

redis:
	docker-compose up -d redis

test:
	coverage run --source sraniq/ -m pytest tests/
	coverage report

black:
	black . --line-length=100

lint:
	flake8 . --max-line-length=100

mypy:
	mypy .

fmt: black mypy lint
