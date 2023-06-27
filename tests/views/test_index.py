import json
from sanic import Sanic

from tests.common import get_disconnected_redis


def test_index_healthy(app: Sanic):
    request, response = app.test_client.get("/")
    assert request.method.lower() == "get"
    assert response.status == 200

    expected = {
        "app": "test_sraniq_app",
        "alive": True,
    }
    assert json.loads(response.body) == expected


def test_index_redis_ping_fails(app: Sanic):
    app.ctx.redis = get_disconnected_redis()
    _, response = app.test_client.get("/")
    assert response.status == 500

    expected = {
        "app": "test_sraniq_app",
        "alive": False,
    }
    assert json.loads(response.body) == expected
