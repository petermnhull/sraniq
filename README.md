# sraniq
Sanic and RQ proof of concept application.

- Lightweight and simple alternative to Celery and Flask.
- Extremely easy to test using `sanic-testing` and `fakeredis`.

## Endpoints
This server has three endpoints relating to running tasks.

- `GET /task` for viewing all running tasks. Returns a list of IDs.
- `POST /task` for creating a new task. Returns the ID of the new task.
- `GET /task/<id>` for viewing the status of a single task by ID. Returns status, result, and id.

## Development
This was developed on Ubuntu 20.04 with Python 3.8.10 and Docker 20.10.12.

1. Set up a new `pipenv` virtual environment and install dependencies with `pipenv install`.
2. Run a Redis broker with `make redis`.

Now use the below commands for development.

- `make server` for running the server.
- `make worker` for running the `rq` worker to do tasks.
- `make test` for running tests with coverage.
- `make fmt` for running linting and formatting tools.
