"""Two envelopes paradox.

The flawed argument claims switching always raises your expected value. We put
that to the test directly: over many rounds, compare an always-stay player with
an always-switch player drawing from the *same* envelope pairs. Their averages
converge — switching yields no advantage, which is the resolution of the paradox.
"""
from __future__ import annotations

import numpy as np


def simulate(trials: int, max_base: int = 100, seed: int | None = None) -> dict:
    """Compare always-stay vs always-switch over ``trials`` rounds."""
    rng = np.random.default_rng(seed)
    # The smaller amount X; the envelopes hold X and 2X.
    base = rng.integers(1, max_base + 1, size=trials)
    picked_smaller = rng.random(trials) < 0.5

    stay_amount = np.where(picked_smaller, base, 2 * base)
    switch_amount = np.where(picked_smaller, 2 * base, base)

    avg_stay = float(np.mean(stay_amount))
    avg_switch = float(np.mean(switch_amount))

    return {
        "trials": trials,
        "avg_stay": avg_stay,
        "avg_switch": avg_switch,
        # Positive means switching helped; it should hover around zero.
        "switch_advantage": avg_switch - avg_stay,
        "switch_advantage_pct": (avg_switch - avg_stay) / avg_stay * 100,
    }
