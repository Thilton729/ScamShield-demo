"""
ScamShield API: analyze messages for scam/phishing.
Demo mode uses mock responses; live mode uses LLM (when wired).
"""
from fastapi import FastAPI

from app.models import AnalyzeRequest, AnalyzeResponse
from app.router.analyzer import analyze as run_analyzer

app = FastAPI(title="ScamShield API", version="0.1.0")


@app.get("/health")
def health() -> dict:
    """Health check for Codespaces and port forwarding."""
    return {"status": "ok"}


@app.get("/")
def root() -> dict:
    """Root endpoint."""
    return {"message": "ScamShield API", "docs": "/docs"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    """
    Analyze a message for scam/phishing.
    Uses mock responses in demo mode (DEMO_MODE=true); otherwise routes to live AI.
    """
    return run_analyzer(text=request.text, channel=request.channel)
