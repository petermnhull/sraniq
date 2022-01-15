from sanic import Sanic

from sraniq.views import IndexView
from sraniq.config import AppContext


def build_app(ctx: AppContext) -> Sanic:
    app = Sanic(
        name=ctx.config.name,
        ctx=ctx,
    )

    app.add_route(IndexView.as_view(), "/")
    return app
