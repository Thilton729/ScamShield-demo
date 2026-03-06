"""
Demo-mode analyzer: deterministic mock responses.
No API calls; safe for offline and live investor demos.
"""
from app.models import AnalyzeResponse, Channel, Verdict


# Simple keyword-based logic so demo behavior is predictable and demo-able
DEMO_SCAM_INDICATORS = (
    "urgent", "click here", "verify", "suspended", "winner", "prize",
    "wire transfer", "bitcoin", "password", "account locked", "confirm your identity",
)
DEMO_SAFE_INDICATORS = ("meeting", "thanks", "reminder", "invoice", "receipt")


def analyze(text: str, channel: Channel) -> AnalyzeResponse:
    """
    Return a deterministic verdict based on keywords.
    Gives investors a consistent, believable demo without any LLM.
    """
    lower = text.lower().strip()
    scam_score = sum(1 for w in DEMO_SCAM_INDICATORS if w in lower)
    safe_score = sum(1 for w in DEMO_SAFE_INDICATORS if w in lower)

    if scam_score > safe_score:
        verdict = Verdict.scam
        confidence = min(0.95, 0.6 + 0.05 * scam_score)
        explanation = (
            "This message shows several signs of a scam or phishing attempt "
            "(e.g. urgency, requests to click or verify)."
        )
    else:
        verdict = Verdict.safe
        confidence = min(0.92, 0.65 + 0.05 * safe_score) if safe_score else 0.7
        explanation = (
            "No strong scam indicators detected. Content appears routine for this channel."
        )

    return AnalyzeResponse(verdict=verdict, confidence=round(confidence, 2), explanation=explanation)
