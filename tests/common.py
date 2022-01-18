class MockResponse:
    def __init__(self, content: str, status_code: int):
        self.content = content
        self.status_code = status_code
