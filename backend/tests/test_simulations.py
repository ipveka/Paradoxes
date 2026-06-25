"""Tests for the simulation math and the API surface.

These lock in the *statistical* claims each paradox makes. We seed the RNG so
the assertions are deterministic, and use generous tolerances so they assert the
phenomenon (e.g. "switching wins ~2/3") rather than a brittle exact value.
"""
from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app
from app.simulations import (
    birthday,
    monty_hall,
    simpsons,
    sleeping_beauty,
    two_envelopes,
)

client = TestClient(app)


# --- Monty Hall ----------------------------------------------------------

def test_monty_hall_switch_beats_stay():
    res = monty_hall.simulate(games=20000, seed=42)
    assert abs(res["switch_rate"] - 2 / 3) < 0.02
    assert abs(res["stay_rate"] - 1 / 3) < 0.02
    assert res["stay_wins"] + res["switch_wins"] == res["games"]


def test_monty_hall_is_seed_reproducible():
    assert monty_hall.simulate(1000, seed=7) == monty_hall.simulate(1000, seed=7)


# --- Birthday ------------------------------------------------------------

def test_birthday_theoretical_known_values():
    # The textbook 50.7% at 23 people.
    assert abs(birthday.theoretical_probability(23) - 0.507) < 0.001
    assert birthday.theoretical_probability(1) == 0.0
    assert birthday.theoretical_probability(366) == 1.0


def test_birthday_simulation_tracks_theory():
    res = birthday.simulate(group_size=23, trials=20000, seed=1)
    assert res["difference"] < 0.02


def test_birthday_curve_is_monotonic():
    points = birthday.curve(100)["points"]
    probs = [p["probability"] for p in points]
    assert probs == sorted(probs)
    assert probs[-1] > 0.99


# --- Two Envelopes -------------------------------------------------------

def test_two_envelopes_switching_has_no_edge():
    res = two_envelopes.simulate(trials=50000, seed=3)
    # Switching advantage should be statistical noise around zero.
    assert abs(res["switch_advantage_pct"]) < 5.0


# --- Sleeping Beauty -----------------------------------------------------

def test_sleeping_beauty_supports_thirder():
    res = sleeping_beauty.simulate(trials=20000, seed=9)
    assert abs(res["p_heads_given_awake"] - 1 / 3) < 0.02


# --- Simpson's -----------------------------------------------------------

def test_simpsons_paradox_present():
    data = simpsons.dataset()
    assert data["paradox"] is True
    # Women lead in each department...
    for dept in data["departments"]:
        assert dept["female_rate"] > dept["male_rate"]
    # ...yet trail overall.
    assert data["overall"]["male_rate"] > data["overall"]["female_rate"]


# --- API -----------------------------------------------------------------

def test_health_ok():
    assert client.get("/health").json()["status"] == "ok"


def test_list_paradoxes():
    res = client.get("/api/paradoxes")
    assert res.status_code == 200
    ids = {p["id"] for p in res.json()}
    assert ids == {"monty-hall", "birthday", "two-envelopes", "sleeping-beauty", "simpsons"}


def test_monty_hall_endpoint():
    res = client.post("/api/monty-hall/simulate", json={"games": 5000, "seed": 1})
    assert res.status_code == 200
    assert abs(res.json()["switch_rate"] - 2 / 3) < 0.03


def test_validation_rejects_out_of_range():
    res = client.post("/api/birthday/simulate", json={"group_size": 9999, "trials": 10})
    assert res.status_code == 422
