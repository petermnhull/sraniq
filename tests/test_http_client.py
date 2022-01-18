from typing import Callable
from unittest.mock import patch

from sraniq.http_client import HTTPClient
from tests.common import MockResponse


class TestHTTPClient:
    def _mocked_requests_get(self):
        return MockResponse("response content", 200)

    @staticmethod
    @patch("requests.get", side_effect=_mocked_requests_get)
    def test_get(mock_get: Callable):
        client = HTTPClient()
        response = client.get("https://url.com")
        assert response.status_code == 200
