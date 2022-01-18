from redis import Redis

from sraniq.app import build_app
from sraniq.config import AppConfig, AppContext
from sraniq.http_client import HTTPClient


def main():
    config = AppConfig.from_env()

    redis = Redis(
        host=config.redis_host,
        port=config.redis_port,
        password=config.redis_password,
    )
    http_client = HTTPClient()
    ctx = AppContext(
        config,
        redis,
        http_client,
    )
    app = build_app(ctx)
    app.run(
        port=config.port,
        host=config.host,
        auto_reload=config.auto_reload,
    )


if __name__ == "__main__":
    main()
