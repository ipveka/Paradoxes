"""Sleeping Beauty: counting awakenings supports the 'thirder' position."""
from __future__ import annotations

import numpy as np

HEADS = 0
TAILS = 1


def simulate(trials: int, seed: int | None = None) -> dict:
    """Run ``trials`` coin tosses; Tails wakes Beauty twice, Heads once."""
    rng = np.random.default_rng(seed)
    coins = rng.integers(0, 2, size=trials)
    heads_count = int(np.count_nonzero(coins == HEADS))
    tails_count = trials - heads_count

    # Awakenings, not coin tosses, are what Beauty conditions on.
    heads_awakenings = heads_count * 1
    tails_awakenings = tails_count * 2
    total_awakenings = heads_awakenings + tails_awakenings

    return {
        "trials": trials,
        "heads_count": heads_count,
        "tails_count": tails_count,
        "total_awakenings": total_awakenings,
        "p_heads_given_awake": heads_awakenings / total_awakenings,
        "p_tails_given_awake": tails_awakenings / total_awakenings,
        "halfer_position": 1 / 2,
        "thirder_position": 1 / 3,
    }
