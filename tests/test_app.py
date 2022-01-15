import json
from sanic import Sanic


def test_app(app: Sanic):
    request, response = app.test_client.get("/")

    assert request.method.lower() == "get"
    assert response.status == 200

    expected = {
        "data": {"message": "hello!", "app": "test_sraniq_app"},
        "status": "success",
        "code": 200,
    }
    assert json.loads(response.body) == expected
