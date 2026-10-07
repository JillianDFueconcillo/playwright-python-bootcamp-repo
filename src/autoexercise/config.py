"""Central settings. Override any value with an environment variable."""

import os
from dataclasses import dataclass


def _with_trailing_slash(url: str) -> str:
    # Playwright joins relative paths ("productsList") onto the base URL only when
    # the base ends with a slash. Without it, "/api" would be dropped.
    return url if url.endswith("/") else url + "/"


@dataclass(frozen=True)
class Settings:
    ui_base_url: str = os.getenv("UI_BASE_URL", "https://automationexercise.com").rstrip("/")
    api_base_url: str = _with_trailing_slash(
        os.getenv("API_BASE_URL", "https://automationexercise.com/api/")
    )


settings = Settings()
