from sraniq.app import build_app
from sraniq.config import AppConfig, AppContext


def main():
    config = AppConfig.from_env()
    ctx = AppContext(config)
    app = build_app(ctx)
    app.run()


if __name__ == "__main__":
    main()
