from sraniq.views.task import Task


def test_task():
    task = Task("test")
    result = task.run(10)
    assert result == "2130"
