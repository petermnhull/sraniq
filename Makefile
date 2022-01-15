#!make

run:
	pipenv run python3 -m scripts.server 

test:
	pipenv run coverage run --source sraniq/ -m pytest tests/

coverage: test
	pipenv run coverage report

black:
	pipenv run black . --line-length=100

lint:
	pipenv run flake8 . --max-line-length=100

mypy:
	pipenv run mypy .

fmt: black mypy lint
