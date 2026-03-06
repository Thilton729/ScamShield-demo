"""
Live AI analyzer (stub). When demo_mode=False, router can call this.
Real LLM integration (cheap vs premium) can be added here later.
"""
from app.models import AnalyzeResponse, Channel, Verdict


def analyze(text: str, channel: Channel) -> AnalyzeResponse:
    """
    Placeholder when running without an API key.
    Replace with real cheap/premium LLM calls when ready.
    """
    # No API key or real model wired yet; return a safe placeholder
    return AnalyzeResponse(
        verdict=Verdict.safe,
        confidence=0.5,
        explanation="Live AI not configured. Set DEMO_MODE=true for mock responses, or add LLM integration in app.services.llm.",
    )
