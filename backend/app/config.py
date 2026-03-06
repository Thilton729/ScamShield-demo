"""
Environment-driven configuration.
All settings from env vars; no secrets in code.
Loads .env from repo root so it works when running from backend/.
"""
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Repo root: app/ -> backend/ -> repo root
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(_REPO_ROOT / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # When True, use mock responses only (no LLM calls). Safe for demos and offline.
    demo_mode: bool = True

    # Optional: for live AI when demo_mode=False
    openai_api_key: str | None = None


def get_settings() -> Settings:
    return Settings()
