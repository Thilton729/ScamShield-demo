# Changelog

All notable changes to the ScamShield demo are listed here.

## [Unreleased]

- (Future: optional live LLM wiring, polish, investor prep.)

## 2025-03 (initial build)

- **Step 1–2:** Product scope and high-level architecture documented.
- **Step 3:** Repo structure (backend, frontend, docs, scripts).
- **Step 4:** GitHub Codespaces setup (devcontainer, port forwarding 8000/8501, startup scripts).
- **Step 5:** FastAPI backend — `POST /analyze`, config (DEMO_MODE), router (mock vs LLM stub), mock service (keyword-based), LLM stub.
- **Step 6:** Streamlit UI — message input, channel selector (SMS/Email/Messaging), Analyze button, verdict and explanation display; BACKEND_URL from env.
- **Docs:** README configuration table and documentation section; CHANGELOG.
