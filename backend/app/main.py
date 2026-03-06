"""
Minimal FastAPI app for Step 4 (Codespaces setup).
Full /analyze and routing will be added in Step 5.
"""
from fastapi import FastAPI

app = FastAPI(title="ScamShield API", version="0.1.0")


@app.get("/health")
def health():
    """Health check for Codespaces and port forwarding."""
    return {"status": "ok"}


@app.get("/")
def root():
    """Root endpoint."""
    return {"message": "ScamShield API", "docs": "/docs"}
