"""
Cost-aware routing: demo (mock) vs live (LLM).
Single place to decide which implementation runs.
"""
from app.config import get_settings
from app.models import AnalyzeResponse, Channel
from app.services import llm as llm_service
from app.services import mock as mock_service


def analyze(text: str, channel: Channel) -> AnalyzeResponse:
    """
    Route to mock (demo) or live LLM based on config.
    Same response shape either way.
    """
    settings = get_settings()
    if settings.demo_mode:
        return mock_service.analyze(text, channel)
    return llm_service.analyze(text, channel)
