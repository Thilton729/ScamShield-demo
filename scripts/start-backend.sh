#!/usr/bin/env bash
# Start the FastAPI backend (port 8000).
# Run from repo root. Use in one terminal while frontend runs in another.
set -e
cd "$(dirname "$0")/../backend"
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
