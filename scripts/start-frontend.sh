#!/usr/bin/env bash
# Start the Streamlit frontend (port 8501).
# Run from repo root. Start backend first (scripts/start-backend.sh) in another terminal.
set -e
cd "$(dirname "$0")/.."
export STREAMLIT_SERVER_PORT=8501
streamlit run frontend/app.py --server.port 8501 --server.address 0.0.0.0
