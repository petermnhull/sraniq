from dataclasses import dataclass, asdict
from typing import Any
from sanic.request import Request
from sanic.views import HTTPMethodView
from sanic.response import HTTPResponse, json


@dataclass
class AppResponse:
    data: Any
    status: str = "success"
    code: int = 200


@dataclass
class IndexViewGetData:
    message: str
    app: str


class IndexView(HTTPMethodView):
    def get(self, request: Request) -> HTTPResponse:
        name = request.app.name
        msg = "hello!"
        data = IndexViewGetData(msg, name)
        resp = AppResponse(data)
        return json(asdict(resp))
