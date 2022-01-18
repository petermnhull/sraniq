from dataclasses import dataclass, asdict
from http import HTTPStatus
from sanic.request import Request
from sanic.views import HTTPMethodView
from sanic.response import HTTPResponse, json


@dataclass(frozen=True)
class IndexViewGet:
    app: str
    alive: bool


class IndexView(HTTPMethodView):
    def get(self, request: Request) -> HTTPResponse:
        is_alive = request.app.ctx.health()
        code = HTTPStatus.OK if is_alive else HTTPStatus.INTERNAL_SERVER_ERROR
        data = IndexViewGet(
            request.app.name,
            is_alive,
        )
        return json(asdict(data), code)
