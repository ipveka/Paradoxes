"""Vercel serverless entry point for the API.

Vercel's Python runtime serves the module-level ``app`` ASGI application. Rather
than duplicate any logic, we reuse the existing FastAPI app from ``backend/``,
which is bundled alongside this function via ``includeFiles`` in vercel.json.

Locally the backend still runs the normal way (``uvicorn app.main:app`` from
``backend/``); this file only exists for the Vercel deployment.
"""
import os
import sys

# backend/ is bundled next to this function on Vercel; add it to the import path
# so "from app.main import app" resolves the same package used in development.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from app.main import app  # noqa: E402

__all__ = ["app"]
