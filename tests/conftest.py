import pytest
from mock import MagicMock
from fakeredis import FakeStrictRedis

from sanic.app import Sanic
from sraniq.app import build_app
from sraniq.config import AppContext, AppConfig


@pytest.fixture
def config() -> AppConfig:
    config = AppConfig(
        "test_sraniq_app",
        8080,
        "host",
        False,
        "redis",
        6379,
        "",
    )
    return config


@pytest.fixture
def redis() -> MagicMock:
    redis = FakeStrictRedis(connected=True)
    return redis


@pytest.fixture
def app(config: AppConfig, redis: MagicMock) -> Sanic:
    ctx = AppContext(config, redis)
    app = build_app(ctx)
    return app
