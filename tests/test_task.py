from sraniq.http_client import HTTPClient
from sraniq.views.task import Task


class TestTask:
    def test_task(self, http_client: HTTPClient):
        task = Task(http_client)
        result = task.run("hello")
        assert result == "15"
