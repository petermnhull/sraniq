import os
from dataclasses import dataclass
import redis
from redis import Redis

from sraniq.http_client import HTTPClient

TASK_QUEUE_NAME = "tasks"
TRUE_NAME = "true"

APP_NAME_DEFAULT = "sraniq"
APP_PORT_DEFAULT = 8000
APP_HOST_DEFAULT = "127.0.0.1"
AUTO_RELOAD_ENABLED_DEFAULT = "false"
ACCESS_LOG_ENABLED_DEFAULT = "false"
DEBUG_ENABLED_DEFAULT = "false"

REDIS_HOST_DEFAULT = "127.0.0.1"
REDIS_PORT_DEFAULT = "6379"
REDIS_PASSWORD_DEFAULT = ""


@dataclass(frozen=True)
class AppConfig:
    name: str
    port: int
    host: str
    auto_reload: bool
    access_log: bool
    debug: bool

    redis_host: str
    redis_port: int
    redis_password: str

    task_queue_name: str = TASK_QUEUE_NAME

    @classmethod
    def from_env(cls):
        name = os.environ.get("APP_NAME", APP_NAME_DEFAULT)
        port = int(os.environ.get("APP_PORT", APP_PORT_DEFAULT))
        host = os.environ.get("APP_HOST", APP_HOST_DEFAULT)
        auto_reload = (
            os.environ.get("AUTO_RELOAD_ENABLED", AUTO_RELOAD_ENABLED_DEFAULT).lower() == TRUE_NAME
        )
        access_log = (
            os.environ.get("ENABLE_ACCESS_LOG", ACCESS_LOG_ENABLED_DEFAULT).lower() == TRUE_NAME
        )
        debug = os.environ.get("DEBUG_ENABLED", DEBUG_ENABLED_DEFAULT).lower() == TRUE_NAME

        redis_host = os.environ.get("REDIS_HOST", REDIS_HOST_DEFAULT)
        redis_port = int(os.environ.get("REDIS_PORT", REDIS_PORT_DEFAULT))
        redis_password = os.environ.get("REDIS_PASSWORD", REDIS_PASSWORD_DEFAULT)

        return cls(
            name,
            port,
            host,
            auto_reload,
            access_log,
            debug,
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
