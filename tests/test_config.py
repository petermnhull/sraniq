from pytest import MonkeyPatch

from sraniq.config import AppConfig


def test_config():
    mp = MonkeyPatch()
    mp.setenv("APP_NAME", "test name")
    mp.setenv("APP_PORT", "8000")
    mp.setenv("APP_HOST", "host")
    mp.setenv("AUTO_RELOAD_ENABLED", "false")
    mp.setenv("REDIS_HOST", "redis")
    mp.setenv("REDIS_PORT", "6379")
    mp.setenv("REDIS_PASSWORD", "")

    actual = AppConfig.from_env()
    expected = AppConfig(
        "test name",
        8000,
        "host",
        False,
        "redis",
        6379,
        "",
    )
    assert actual == expected
