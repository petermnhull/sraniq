from dataclasses import dataclass, asdict
from typing import List
from rq import Queue

from sanic.request import Request
from sanic.views import HTTPMethodView
from sanic.response import HTTPResponse, json

from sraniq.task import Task


@dataclass(frozen=True)
class TaskViewGet:
    ids: List[str]


@dataclass(frozen=True)
class TaskViewPost:
    id: str


class TaskView(HTTPMethodView):
    def get(self, request: Request) -> HTTPResponse:
        queue = Queue(name="default", connection=request.app.ctx.redis)
        ids = queue.get_job_ids()
        response = TaskViewGet(ids)
        data = asdict(response)
        return json(data, 200)

    def post(self, request: Request) -> HTTPResponse:
        queue = Queue(name="default", connection=request.app.ctx.redis)
        task = Task("inject dependencies in here")
        job = queue.enqueue(task.run, 5)
        response = TaskViewPost(job.id)
        data = asdict(response)
        return json(data, 202)
