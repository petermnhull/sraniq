from sanic import Sanic

from sraniq.views import IndexView, TaskView
from sraniq.config import AppContext


def build_app(ctx: AppContext) -> Sanic:
    app = Sanic(
        name=ctx.config.name,
        ctx=ctx,
    )

    app.add_route(IndexView.as_view(), "/")
    app.add_route(TaskView.as_view(), "/task")
    return app
