#!/usr/bin/bash

/wait

alembic upgrade head
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload