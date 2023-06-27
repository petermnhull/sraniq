from fakeredis import FakeServer, FakeStrictRedis


class MockResponse:
    def __init__(self, content: str, status_code: int):
        self.content = content
        self.status_code = status_code


def get_disconnected_redis() -> FakeStrictRedis:
    server = FakeServer()
    server.connected = False
    return FakeStrictRedis(server=server)
