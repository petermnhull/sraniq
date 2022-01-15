from pytest import MonkeyPatch

from sraniq.config import AppConfig


def test_config():
    mp = MonkeyPatch()
    mp.setenv("APP_NAME", "test name")
    actual = AppConfig.from_env()
    expected = AppConfig(
        "test name",
    )
    assert actual == expected
