"""FastAPI entry point for the Paradoxes API."""
from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import config
from app.routers import paradoxes

app = FastAPI(
    title=config.PROJECT_NAME,
    version=config.VERSION,
    description="Monte Carlo simulations and datasets behind classic probability paradoxes.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(paradoxes.router)


@app.get("/health", tags=["meta"])
def health():
    """Liveness probe used by Render and uptime checks."""
    return {"status": "ok", "version": config.VERSION}


@app.get("/", tags=["meta"])
def root():
    return {
        "name": config.PROJECT_NAME,
        "version": config.VERSION,
        "docs": "/docs",
        "paradoxes": "/api/paradoxes",
    }
