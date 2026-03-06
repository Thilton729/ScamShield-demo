"""
ScamShield demo UI: paste a message, choose channel, get scam/safe verdict.
Calls the FastAPI backend; BACKEND_URL from env or .env at repo root.
"""
import os
from pathlib import Path

import requests
import streamlit as st

# Load .env from repo root (when run as streamlit run frontend/app.py from root)
_REPO_ROOT = Path(__file__).resolve().parent.parent
_DOTENV = _REPO_ROOT / ".env"
if _DOTENV.exists():
    from dotenv import load_dotenv
    load_dotenv(_DOTENV)

BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000").rstrip("/")
ANALYZE_URL = f"{BACKEND_URL}/analyze"

CHANNELS = ["SMS", "Email", "Messaging"]
CHANNEL_TO_API = {"SMS": "sms", "Email": "email", "Messaging": "messaging"}

st.set_page_config(page_title="ScamShield Demo", page_icon="🛡️", layout="centered")
st.title("🛡️ ScamShield")
st.caption("Scam & phishing detection across SMS, email, and messaging")

channel = st.selectbox("Channel", CHANNELS, index=0)
message = st.text_area("Message", placeholder="Paste or type the message to analyze...", height=120)

if st.button("Analyze", type="primary"):
    if not message or not message.strip():
        st.warning("Enter a message to analyze.")
    else:
        with st.spinner("Analyzing..."):
            try:
                r = requests.post(
                    ANALYZE_URL,
                    json={"text": message.strip(), "channel": CHANNEL_TO_API[channel]},
                    timeout=10,
                )
                r.raise_for_status()
                data = r.json()
            except requests.exceptions.RequestException as e:
                st.error(f"Could not reach the API: {e}. Is the backend running on {BACKEND_URL}?")
                st.stop()

        verdict = data.get("verdict", "").lower()
        confidence = data.get("confidence", 0)
        explanation = data.get("explanation", "")

        if verdict == "scam":
            st.error(f"**Verdict: Scam** — confidence {confidence:.0%}")
        else:
            st.success(f"**Verdict: Safe** — confidence {confidence:.0%}")
        st.write(explanation)
