#!/usr/bin/env bash
# Start backend in background, then Streamlit in foreground.
# Run from repo root. Stop with Ctrl+C (Streamlit); backend keeps running until you kill it.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
# Start backend in background
(cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8000) &
BACKEND_PID=$!
# Give backend a moment to bind
sleep 2
# Start frontend in foreground
export STREAMLIT_SERVER_PORT=8501
streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0
# If Streamlit exits, kill backend
kill $BACKEND_PID 2>/dev/null || true
