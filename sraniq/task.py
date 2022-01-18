from sraniq.http_client import HTTPClient


class Task:
    def __init__(self, http_client: HTTPClient):
        self._http_client = http_client

    def run(self, search: str) -> str:
        """
        Simulates long-running task.
        Returns the number of words returned from the Google search page of the input parameter
        """
        url = f"https://google.co.uk?q={search}"
        response = self._http_client.get(url)
        return str(len(response.content))
