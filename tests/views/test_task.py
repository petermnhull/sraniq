import json
from fakeredis import FakeRedis
from typing import Dict
from sanic import Sanic


class TestTask:
    @staticmethod
    def test_post(app: Sanic):
        _, response = app.test_client.post("/task")
        assert response.status == 202

        actual = json.loads(response.body)
        assert actual["id"]

    @staticmethod
    def test_post_redis_error(app: Sanic):
        app.ctx.redis = FakeRedis(connected=False)
        _, response = app.test_client.post("/task")
        assert response.status == 500

        actual = json.loads(response.body)
        assert actual == {"message": "failed to connect to task broker"}

    @staticmethod
    def test_get_no_tasks(app: Sanic):
        _, response = app.test_client.get("/task")
        assert response.status == 200

        actual = json.loads(response.body)
        expected: Dict = {"ids": []}
        assert actual == expected

    @staticmethod
    def test_get_with_tasks(app: Sanic):
        # Create a new task
        _, response = app.test_client.post("/task")
        assert response.status == 202
        post_response = json.loads(response.body)
        id = post_response["id"]

        # Find tasks
        _, response = app.test_client.get("/task")
        assert response.status == 200

        actual = json.loads(response.body)
        expected: Dict = {"ids": [id]}
        assert actual == expected

    @staticmethod
    def test_get_redis_error(app: Sanic):
        app.ctx.redis = FakeRedis(connected=False)
        _, response = app.test_client.get("/task")
        assert response.status == 500

        actual = json.loads(response.body)
        assert actual == {"message": "failed to connect to task broker"}
