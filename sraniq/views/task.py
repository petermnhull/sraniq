from dataclasses import dataclass, asdict
from typing import List
from rq import Queue
from redis.exceptions import ConnectionError
from http import HTTPStatus

from sanic.request import Request
from sanic.views import HTTPMethodView
from sanic.response import HTTPResponse, json

from sraniq.task import Task
from sraniq.views.errors import AppError
from sraniq.views.constants import REDIS_CONNECTION_ERROR_MESSAGE


@dataclass(frozen=True)
class TaskViewGet:
    ids: List[str]


@dataclass(frozen=True)
class TaskViewPost:
    id: str


class TaskView(HTTPMethodView):
    def get(self, request: Request) -> HTTPResponse:
        queue = Queue(name=request.app.ctx.config.task_queue_name, connection=request.app.ctx.redis)
        try:
            ids = queue.get_job_ids()
        except ConnectionError:
            error = AppError(REDIS_CONNECTION_ERROR_MESSAGE)
            return json(asdict(error), HTTPStatus.INTERNAL_SERVER_ERROR)
        response = TaskViewGet(ids)
        data = asdict(response)
        return json(data, HTTPStatus.OK)

    def post(self, request: Request) -> HTTPResponse:
        queue = Queue(name=request.app.ctx.config.task_queue_name, connection=request.app.ctx.redis)
        task = Task(request.app.ctx.http_client)
        try:
            job = queue.enqueue(task.run, "input variable")
        except ConnectionError:
            error = AppError(REDIS_CONNECTION_ERROR_MESSAGE)
            return json(asdict(error), HTTPStatus.INTERNAL_SERVER_ERROR)
        response = TaskViewPost(job.id)
        data = asdict(response)
        return json(data, HTTPStatus.ACCEPTED)
