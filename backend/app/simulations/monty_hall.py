"""Monty Hall Monte Carlo simulation.

With the standard rules (the host always opens a goat door he can choose, and
never your door), switching wins exactly when your *initial* pick was a goat —
which happens 2/3 of the time. We exploit that fact for a fully vectorized
simulation: there's no need to model the host's reveal explicitly.
"""
from __future__ import annotations

import numpy as np


def simulate(games: int, seed: int | None = None) -> dict:
    """Play ``games`` rounds and report win rates for both strategies."""
    rng = np.random.default_rng(seed)
    car = rng.integers(0, 3, size=games)
    first_choice = rng.integers(0, 3, size=games)

    # "Stay" wins iff the first choice already had the car.
    stay_wins = int(np.count_nonzero(car == first_choice))
    # "Switch" wins on exactly the complementary games.
    switch_wins = games - stay_wins

    return {
        "games": games,
        "stay_wins": stay_wins,
        "switch_wins": switch_wins,
        "stay_rate": stay_wins / games,
        "switch_rate": switch_wins / games,
        "theoretical_stay_rate": 1 / 3,
        "theoretical_switch_rate": 2 / 3,
    }
