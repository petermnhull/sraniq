from unittest.mock import MagicMock
import pytest
from fakeredis import FakeRedis, FakeStrictRedis

from sanic.app import Sanic
from sraniq.app import build_app
from sraniq.config import AppContext, AppConfig
from sraniq.http_client import HTTPClient

from tests.common import MockResponse


@pytest.fixture
def config() -> AppConfig:
    config = AppConfig(
        "test_sraniq_app",
        8080,
        "host",
        False,
        False,
        False,
        "redis",
        6379,
        "",
    )
    return config


@pytest.fixture
def redis() -> FakeRedis:
    return FakeRedis(connected=True)


@pytest.fixture
def http_client() -> MagicMock:
    client = MagicMock(spec=HTTPClient)
    client.get.return_value = MockResponse("website content", 200)
    # Required to avoid pickling error in rq when creating the job
    client.__reduce__ = lambda self: (MagicMock, ())  # type: ignore
    return client


@pytest.fixture
def app_context(config: AppConfig, redis: FakeStrictRedis, http_client: MagicMock) -> AppContext:
    return AppContext(config, redis, http_client)


@pytest.fixture
def app(app_context: AppContext) -> Sanic:
    return build_app(app_context)
