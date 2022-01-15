import pytest
from sanic.app import Sanic
from sraniq.app import build_app
from sraniq.config import AppContext, AppConfig


@pytest.fixture
def app() -> Sanic:
    config = AppConfig("test_sraniq_app")
    ctx = AppContext(config)
    app = build_app(ctx)
    return app
