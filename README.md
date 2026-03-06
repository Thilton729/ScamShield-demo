# ScamShield Demo

Investor-ready demo: AI-powered scam and phishing detection across SMS, email, and messaging. Paste a message, get a verdict (scam/safe) plus confidence and explanation.

## Run in GitHub Codespaces

1. Open this repo in **GitHub Codespaces** (Code → Codespaces → Create codespace).
2. Wait for the dev container to build (installs Python deps via `postCreateCommand`).
3. **Ports:** Codespaces will forward **8000** (FastAPI) and **8501** (Streamlit). Accept “Open in Browser” when prompted.
4. Start the app (choose one):
   - **Two terminals:**  
     `./scripts/start-backend.sh` then `./scripts/start-frontend.sh`
   - **One terminal:**  
     `./scripts/start-all.sh`
5. Open the Streamlit port (8501) in the browser; use the FastAPI port (8000) for `/docs` or `/health`.

## Configuration

Copy `.env.example` to `.env` in the repo root. All behavior is driven by environment variables (no secrets in code).

| Variable | Purpose | Default / note |
|----------|---------|----------------|
| `DEMO_MODE` | When `true`, use mock responses only (no API keys). Safe for demos and offline. | `true` |
| `BACKEND_URL` | URL of the FastAPI backend (used by the Streamlit frontend). | `http://localhost:8000`; in Codespaces, keep this if both run in the same codespace. |
| `OPENAI_API_KEY` | Optional; for live AI when `DEMO_MODE=false`. | Not set; add when wiring real LLM. |

## Documentation

- **Product scope and boundaries** — [docs/PRODUCT_SCOPE.md](docs/PRODUCT_SCOPE.md) (in scope vs out of scope for this demo).
- **Architecture** — [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) (API, router, UI, data flow).
- **7-day build plan** — [docs/BUILD_PLAN.md](docs/BUILD_PLAN.md) (solo-founder week plan and checklist).
- **API reference** — Run the backend and open `/docs` (Swagger UI) for request/response schemas and to try `POST /analyze`.

## Repo layout

- `backend/` — FastAPI API and AI routing (mock + optional LLM).
- `frontend/` — Streamlit UI.
- `docs/` — Product scope and architecture.
- `scripts/` — Startup scripts for Codespaces.
