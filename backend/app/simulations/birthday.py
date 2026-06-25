"""Birthday paradox: simulation plus the exact theoretical probability."""
from __future__ import annotations

import numpy as np

DAYS_IN_YEAR = 365


def theoretical_probability(group_size: int) -> float:
    """Exact probability that at least two people in a group share a birthday."""
    if group_size < 2:
        return 0.0
    if group_size > DAYS_IN_YEAR:
        return 1.0
    prob_no_match = 1.0
    for i in range(group_size):
        prob_no_match *= (DAYS_IN_YEAR - i) / DAYS_IN_YEAR
    return 1.0 - prob_no_match


def simulate(group_size: int, trials: int, seed: int | None = None) -> dict:
    """Estimate the shared-birthday probability by sampling ``trials`` groups."""
    rng = np.random.default_rng(seed)
    birthdays = rng.integers(0, DAYS_IN_YEAR, size=(trials, group_size))
    birthdays.sort(axis=1)
    # A collision exists iff two adjacent values match after sorting each row.
    has_match = np.any(birthdays[:, 1:] == birthdays[:, :-1], axis=1)
    matches = int(np.count_nonzero(has_match))
    simulated = matches / trials
    theoretical = theoretical_probability(group_size)

    return {
        "group_size": group_size,
        "trials": trials,
        "matches": matches,
        "simulated_probability": simulated,
        "theoretical_probability": theoretical,
        "difference": abs(simulated - theoretical),
    }


def curve(max_size: int = 100) -> dict:
    """Theoretical probability curve for group sizes 1..max_size."""
    points = [
        {"group_size": n, "probability": theoretical_probability(n)}
        for n in range(1, max_size + 1)
    ]
    return {"max_size": max_size, "points": points}
