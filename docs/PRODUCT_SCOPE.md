# Product scope and demo boundaries

## In scope (this demo)

- **Single-message analysis:** User pastes/enters one message; system returns verdict (scam / not scam), confidence, and a short explanation.
- **Three channels in UI:** SMS, Email, Messaging app — same backend; channel is metadata for display only.
- **Cost-aware AI routing:** Cheap vs premium path (and mock path for demo); one place in code decides which runs.
- **Demo / offline mode:** Mock responses that match real API shape; no API keys required; safe for live demos.
- **Investor-facing UI:** One Streamlit screen: input, channel, Analyze, then verdict + confidence + explanation.
- **Env-driven config:** DEMO_MODE, BACKEND_URL, API keys via environment.

## Out of scope (for now)

- Real channel integrations (Twilio, Gmail, etc.) — paste/type only.
- User accounts, auth, or persistence (no DB).
- Production scale (rate limits, queues, retries, multi-region).
- Batch or real-time processing of many messages.
- Mobile app or browser extension — web UI only.
