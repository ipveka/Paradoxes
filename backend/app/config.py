"""Application settings, configurable via environment variables."""
from __future__ import annotations

import os


def _split_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


# Comma-separated list of allowed CORS origins. In development the Next.js dev
# server runs on :3000; set ALLOWED_ORIGINS in production (e.g. on Render) to
# your deployed frontend URL.
ALLOWED_ORIGINS: list[str] = _split_csv(
    os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000")
)

PROJECT_NAME = "Paradoxes API"
VERSION = "1.0.0"
