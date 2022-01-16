from dataclasses import dataclass


@dataclass(frozen=True)
class AppError:
    message: str
