import os
from dataclasses import dataclass
import redis
from redis import Redis

from sraniq.http_client import HTTPClient

TASK_QUEUE_NAME = "tasks"


@dataclass(frozen=True)
class AppConfig:
    name: str
    port: int
    host: str
    auto_reload: bool

    redis_host: str
    redis_port: int
    redis_password: str

    task_queue_name: str = TASK_QUEUE_NAME

    @classmethod
    def from_env(cls):
        name = os.environ.get("APP_NAME", "sraniq")
        port = int(os.environ.get("APP_PORT", 8000))
        host = os.environ.get("APP_HOST", "127.0.0.1")
        auto_reload = os.environ.get("AUTO_RELOAD_ENABLED", "false").lower() == "true"

        redis_host = os.environ.get("REDIS_HOST")
        redis_port = int(os.environ.get("REDIS_PORT"))
        redis_password = os.environ.get("REDIS_PASSWORD")

        return cls(
            name,
            port,
            host,
            auto_reload,
            redis_host,
            redis_port,
            redis_password,
        )


class AppContext:
    def __init__(self, config: AppConfig, redis: Redis, http_client: HTTPClient):
        self.config = config
        self.redis = redis
        self.http_client = http_client

    def health(self) -> bool:
        try:
            self.redis.ping()
        except redis.exceptions.ConnectionError:
            return False
        return True
