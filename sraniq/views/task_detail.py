from dataclasses import dataclass, asdict
from rq.job import Job
from rq.exceptions import NoSuchJobError
from redis.exceptions import ConnectionError
from http import HTTPStatus

from sanic.request import Request
from sanic.views import HTTPMethodView
from sanic.response import HTTPResponse, json

from sraniq.views.errors import AppError
from sraniq.views.constants import REDIS_CONNECTION_ERROR_MESSAGE, NO_TASK_FOR_ID_MESSAGE


@dataclass(frozen=True)
class TaskDetailGet:
    id: str
    status: str
    result: str


class TaskDetailView(HTTPMethodView):
    def get(self, request: Request, id: str) -> HTTPResponse:
        try:
            job = Job.fetch(id, connection=request.app.ctx.redis)
        except NoSuchJobError:
            error = AppError(NO_TASK_FOR_ID_MESSAGE)
            return json(asdict(error), HTTPStatus.NOT_FOUND)
        except ConnectionError:
            error = AppError(REDIS_CONNECTION_ERROR_MESSAGE)
            return json(asdict(error), HTTPStatus.INTERNAL_SERVER_ERROR)
        response = TaskDetailGet(job.id, job.get_status(), job.result)
        return json(asdict(response), HTTPStatus.OK)
