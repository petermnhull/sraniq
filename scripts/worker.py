from rq import Connection, Worker
from redis import Redis

from sraniq.config import AppConfig


def main():
    config = AppConfig.from_env()

    redis = Redis(
        host=config.redis_host,
        port=config.redis_port,
        password=config.redis_password,
    )

    with Connection():
        queues = ["default"]
        w = Worker(queues, connection=redis)
        w.work()


if __name__ == "__main__":
    main()
