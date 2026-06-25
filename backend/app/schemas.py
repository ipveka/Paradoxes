"""Pydantic request/response models for the paradox API."""
from __future__ import annotations

from pydantic import BaseModel, Field

# --- Shared --------------------------------------------------------------

SeedField = Field(
    default=None,
    description="Optional RNG seed for reproducible runs.",
)


# --- Monty Hall ----------------------------------------------------------

class MontyHallRequest(BaseModel):
    games: int = Field(1000, ge=1, le=1_000_000, description="Number of games to simulate.")
    seed: int | None = SeedField


class MontyHallResult(BaseModel):
    games: int
    stay_wins: int
    switch_wins: int
    stay_rate: float
    switch_rate: float
    theoretical_stay_rate: float
    theoretical_switch_rate: float


# --- Birthday ------------------------------------------------------------

class BirthdayRequest(BaseModel):
    group_size: int = Field(23, ge=1, le=365, description="People in the group.")
    trials: int = Field(2000, ge=1, le=500_000, description="Number of random groups.")
    seed: int | None = SeedField


class BirthdayResult(BaseModel):
    group_size: int
    trials: int
    matches: int
    simulated_probability: float
    theoretical_probability: float
    difference: float


class BirthdayCurvePoint(BaseModel):
    group_size: int
    probability: float


class BirthdayCurve(BaseModel):
    max_size: int
    points: list[BirthdayCurvePoint]


# --- Two Envelopes -------------------------------------------------------

class TwoEnvelopesRequest(BaseModel):
    trials: int = Field(5000, ge=1, le=1_000_000, description="Number of rounds.")
    max_base: int = Field(100, ge=1, le=10_000, description="Max value of the smaller amount.")
    seed: int | None = SeedField


class TwoEnvelopesResult(BaseModel):
    trials: int
    avg_stay: float
    avg_switch: float
    switch_advantage: float
    switch_advantage_pct: float


# --- Sleeping Beauty -----------------------------------------------------

class SleepingBeautyRequest(BaseModel):
    trials: int = Field(2000, ge=1, le=1_000_000, description="Number of coin tosses.")
    seed: int | None = SeedField


class SleepingBeautyResult(BaseModel):
    trials: int
    heads_count: int
    tails_count: int
    total_awakenings: int
    p_heads_given_awake: float
    p_tails_given_awake: float
    halfer_position: float
    thirder_position: float


# --- Simpson's -----------------------------------------------------------

class SimpsonsDepartment(BaseModel):
    name: str
    male_applied: int
    male_admitted: int
    male_rate: float
    female_applied: int
    female_admitted: int
    female_rate: float


class SimpsonsOverall(BaseModel):
    male_applied: int
    male_admitted: int
    male_rate: float
    female_applied: int
    female_admitted: int
    female_rate: float


class SimpsonsData(BaseModel):
    departments: list[SimpsonsDepartment]
    overall: SimpsonsOverall
    paradox: bool


# --- Catalog -------------------------------------------------------------

class ParadoxMeta(BaseModel):
    id: str
    name: str
    emoji: str
    tagline: str
    blurb: str
    wikipedia: str
