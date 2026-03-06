"""
Request and response schemas for the analyze API.
Unified shape so mock and real LLM responses look the same.
"""
from enum import Enum

from pydantic import BaseModel, Field


class Channel(str, Enum):
    sms = "sms"
    email = "email"
    messaging = "messaging"


class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Message content to analyze")
    channel: Channel = Field(default=Channel.sms, description="Source channel (metadata)")


class Verdict(str, Enum):
    scam = "scam"
    safe = "safe"


class AnalyzeResponse(BaseModel):
    verdict: Verdict = Field(..., description="scam or safe")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score 0–1")
    explanation: str = Field(..., min_length=1, description="Short human-readable explanation")
