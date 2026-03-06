# 7-day solo-founder build plan

Realistic week-long plan to get from zero to an investor-ready demo. Optimized for clarity and demo reliability, not production scale.

---

## Day 1 — Scope and structure

- [x] Define product scope and demo boundaries (what’s in / out).
- [x] Document high-level architecture (API, router, UI).
- [x] Define repo structure (backend, frontend, docs, scripts).
- **Outcome:** `docs/PRODUCT_SCOPE.md`, `docs/ARCHITECTURE.md`, folder layout agreed.

---

## Day 2 — Dev environment and backend shell

- [x] GitHub Codespaces setup: `.devcontainer/devcontainer.json`, ports 8000/8501.
- [x] Startup scripts (backend, frontend, start-all).
- [x] FastAPI app shell: `/health`, `/`, minimal `main.py`.
- [x] Env-driven config: `.env.example`, load from repo root.
- **Outcome:** Open in Codespaces, run scripts, see both ports respond.

---

## Day 3 — Analyze API and demo mode

- [x] Request/response models (`AnalyzeRequest`, `AnalyzeResponse`).
- [x] Router: demo mode → mock, else → LLM stub.
- [x] Mock service: keyword-based, deterministic verdicts for demos.
- [x] `POST /analyze` wired and testable via `/docs`.
- **Outcome:** API returns scam/safe + confidence + explanation in demo mode.

---

## Day 4 — Frontend and end-to-end demo

- [x] Streamlit UI: message input, channel selector, Analyze button.
- [x] Call backend `POST /analyze`, show verdict, confidence, explanation.
- [x] BACKEND_URL from env; error handling when backend unavailable.
- [x] README and docs: configuration table, documentation section, CHANGELOG.
- **Outcome:** Full paste → analyze → result flow working in Codespaces.

---

## Day 5 — Polish and reliability

- [ ] Rehearse demo flow: 2–3 example messages (clear scam, clear safe, edge case).
- [ ] Optional: add 1–2 sentences in UI explaining “Demo mode” when `DEMO_MODE=true`.
- [ ] Tag a demo-ready version: `git tag -a v0.1-demo -m "Investor demo"`.
- **Outcome:** Confident live run; one tagged commit to revert to if needed.

---

## Day 6 — Optional: live AI path

- [ ] Wire real LLM in `app/services/llm.py` (e.g. one cheap model) when `DEMO_MODE=false`.
- [ ] Document in README: set `DEMO_MODE=false` and `OPENAI_API_KEY` for live mode.
- [ ] Keep mock as default so demos never depend on API keys or network.
- **Outcome:** Option to show “real” AI without changing demo flow.

---

## Day 7 — Investor prep and wrap-up

- [ ] Final pass on README: one-paragraph pitch, how to run, link to docs.
- [ ] Ensure `.env` is never committed; `.env.example` is the only env template.
- [ ] Optional: short `docs/DECISIONS.md` (e.g. “mock first”, “Streamlit for demo only”).
- **Outcome:** Repo is shareable; anyone can open in Codespaces and run the demo.

---

## Methodology

- **One logical change per commit;** push to `main` after each step.
- **Document as you go:** scope, architecture, config, CHANGELOG.
- **Demo mode first:** mock responses so the product is always showable.
- **No overengineering:** add auth, DB, or scale only when needed for the next milestone.
