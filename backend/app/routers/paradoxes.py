"""API routes for every paradox simulation and dataset."""
from __future__ import annotations

from fastapi import APIRouter, Query

from app import catalog, schemas
from app.simulations import (
    birthday,
    monty_hall,
    simpsons,
    sleeping_beauty,
    two_envelopes,
)

router = APIRouter(prefix="/api", tags=["paradoxes"])


@router.get("/paradoxes", response_model=list[schemas.ParadoxMeta])
def list_paradoxes():
    """Catalog of all paradoxes with display metadata."""
    return catalog.PARADOXES


@router.post("/monty-hall/simulate", response_model=schemas.MontyHallResult)
def monty_hall_simulate(req: schemas.MontyHallRequest):
    return monty_hall.simulate(req.games, req.seed)


@router.post("/birthday/simulate", response_model=schemas.BirthdayResult)
def birthday_simulate(req: schemas.BirthdayRequest):
    return birthday.simulate(req.group_size, req.trials, req.seed)


@router.get("/birthday/curve", response_model=schemas.BirthdayCurve)
def birthday_curve(max_size: int = Query(100, ge=2, le=365)):
    return birthday.curve(max_size)


@router.post("/two-envelopes/simulate", response_model=schemas.TwoEnvelopesResult)
def two_envelopes_simulate(req: schemas.TwoEnvelopesRequest):
    return two_envelopes.simulate(req.trials, req.max_base, req.seed)


@router.post("/sleeping-beauty/simulate", response_model=schemas.SleepingBeautyResult)
def sleeping_beauty_simulate(req: schemas.SleepingBeautyRequest):
    return sleeping_beauty.simulate(req.trials, req.seed)


@router.get("/simpsons/data", response_model=schemas.SimpsonsData)
def simpsons_data():
    return simpsons.dataset()
