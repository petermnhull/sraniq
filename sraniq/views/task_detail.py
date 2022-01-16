from dataclasses import dataclass, asdict
from rq.job import Job
from rq.exceptions import NoSuchJobError

from sanic.request import Request
from sanic.views import HTTPMethodView
from sanic.response import HTTPResponse, json

from sraniq.views.errors import AppError


@dataclass(frozen=True)
class TaskDetailGet:
    id: str
    status: str
    result: str


class TaskDetailView(HTTPMethodView):
    def get(self, request: Request, id: str) -> HTTPResponse:
        try:
            job = Job.fetch(id, connection=request.app.ctx.redis)
            response = TaskDetailGet(job.id, job.get_status(), job.result)
            data = asdict(response)
            code = 200
        except NoSuchJobError:
            error = AppError("no task associated to id")
            data = asdict(error)
            code = 404
        return json(data, code)
