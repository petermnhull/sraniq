from dataclasses import dataclass, asdict
from rq import Queue
from rq.job import Job
from rq.exceptions import NoSuchJobError

from sanic.request import Request
from sanic.views import HTTPMethodView
from sanic.response import HTTPResponse, json

from sraniq.task import Task


@dataclass(frozen=True)
class TaskStatus:
    job_id: str
    status: str
    result: str


class TaskView(HTTPMethodView):
    def get(self, request: Request) -> HTTPResponse:
        id = request.args["id"][0]
        try:
            job = Job.fetch(id, connection=request.app.ctx.redis)
            task_status = TaskStatus(job.id, job.get_status(), job.result)
            data = asdict(task_status)
            code = 200
        except NoSuchJobError:
            data = {"message": "no job associated to id"}
            code = 404
        return json(data, code)

    def post(self, request: Request) -> HTTPResponse:
        queue = Queue(name="default", connection=request.app.ctx.redis)
        task = Task("inject dependencies in here")
        job = queue.enqueue(task.run, 5)
        task_status = TaskStatus(job.id, job.get_status(), job.result)
        return json(asdict(task_status), 202)
