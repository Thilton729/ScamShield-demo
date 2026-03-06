# High-level architecture

## Overview

- **FastAPI backend:** HTTP API; `/analyze` accepts message + channel, returns verdict, confidence, explanation.
- **AI / routing layer:** Inside backend; chooses mock vs cheap vs premium, returns unified response shape.
- **Streamlit frontend:** One page; calls `POST /analyze`, displays result.

## Data flow

```
[Streamlit UI]  -->  POST /analyze  -->  [FastAPI]
                                              |
                                              v
                                      [Router: demo? / cheap? / premium?]
                                              |
              +-------------------------------+-------------------------------+
              v                               v                               v
        [Mock handler]                 [Cheap LLM]                     [Premium LLM]
              |                               |                               |
              +-------------------------------+-------------------------------+
                                              |
                                              v
                                      [Unified response]
                                              |
[Streamlit UI]  <--  JSON (verdict, confidence, explanation)  <--  [FastAPI]
```

## Components

- **Backend:** Single process; route layer + analyzer (router + implementations). No auth, no DB.
- **Frontend:** Single Streamlit script; backend URL from env.
- **Config:** Env vars only (DEMO_MODE, BACKEND_URL, API keys).
