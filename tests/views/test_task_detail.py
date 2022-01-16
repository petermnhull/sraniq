import json
from sanic import Sanic


class TestTaskDetail:
    @staticmethod
    def test_get(app: Sanic):
        # Add task to queue
        _, response = app.test_client.post("/task")
        assert response.status == 202

        # Find the task with get endpoint
        post_response = json.loads(response.body)
        id = post_response["id"]
        _, response = app.test_client.get(f"/task/{id}")
        assert response.status == 200

        # Check response is just queued, as there's no worker
        get_response = json.loads(response.body)
        assert get_response["id"] == id
        assert get_response["status"] == "queued"
        assert not get_response["result"]

    @staticmethod
    def test_get_no_job(app: Sanic):
        _, response = app.test_client.get("/task/123abc")
        assert response.status == 404

        actual = json.loads(response.body)
        assert actual["message"] == "no task associated to id"
