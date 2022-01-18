import requests


class HTTPClient:
    @staticmethod
    def get(url: str) -> requests.Response:
        return requests.get(url)
