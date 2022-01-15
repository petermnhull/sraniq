import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    name: str

    @classmethod
    def from_env(cls):
        name = os.environ.get("APP_NAME", "sraniq")
        return cls(name)


class AppContext:
    def __init__(self, config: AppConfig):
        self.config = config
