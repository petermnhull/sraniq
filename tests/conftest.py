import pytest
from mock import MagicMock
from redis import Redis


from sanic.app import Sanic
from sraniq.app import build_app
from sraniq.config import AppContext, AppConfig


@pytest.fixture
def redis() -> MagicMock:
    redis = MagicMock(spec=Redis)
    return redis


@pytest.fixture
def app(redis: MagicMock) -> Sanic:
    config = AppConfig(
        "test_sraniq_app",
        8080,
        "host",
        False,
        "redis",
        6379,
        "",
    )
    ctx = AppContext(config, redis)
    app = build_app(ctx)
    return app
