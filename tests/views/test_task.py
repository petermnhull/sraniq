import json
from sanic import Sanic


def test_task_post(app: Sanic):
    _, response = app.test_client.post("/task")
    assert response.status == 202

    actual = json.loads(response.body)
    assert actual["status"] == "queued"
    assert not actual["result"]


def test_task_get(app: Sanic):
    # Add job to queue
    _, response = app.test_client.post("/task")
    assert response.status == 202

    # Find the job with get endpoint
    post_response = json.loads(response.body)
    job_id = post_response["job_id"]
    _, response = app.test_client.get(f"/task?id={job_id}")
    assert response.status == 200

    # Check response is just queued, as there's no worker
    get_response = json.loads(response.body)
    assert get_response["job_id"] == job_id
    assert get_response["status"] == "queued"
    assert not get_response["result"]


def test_task_get_no_job(app: Sanic):
    _, response = app.test_client.get("/task?id=123abc")
    assert response.status == 404

    actual = json.loads(response.body)
    assert actual["message"] == "no job associated to id"
