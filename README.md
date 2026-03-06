# ScamShield Demo

Investor-ready demo: AI-powered scam and phishing detection across SMS, email, and messaging (paste-in analysis).

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

## Environment

- Copy `.env.example` to `.env` and adjust if needed.
- **Demo mode:** `DEMO_MODE=true` uses mock responses (no API keys). Set `DEMO_MODE=false` when using live AI.

## Repo layout

- `backend/` — FastAPI API and AI routing
- `frontend/` — Streamlit UI
- `docs/` — Product scope and architecture
- `scripts/` — Startup scripts for Codespaces

See `docs/PRODUCT_SCOPE.md` and `docs/ARCHITECTURE.md` for scope and design.
