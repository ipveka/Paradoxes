"""Simpson's paradox: a fixed, illustrative admissions dataset.

This isn't a Monte Carlo simulation — the point is a deterministic dataset where
a trend reverses on aggregation. The numbers mirror the classic 1973 UC Berkeley
case: women have a higher acceptance rate in *every* department, yet a lower rate
overall, because they applied disproportionately to the more selective one.
"""
from __future__ import annotations

# (department name, male applied/admitted, female applied/admitted)
_DEPARTMENTS = [
    {"name": "Department A", "male": (100, 80), "female": (20, 18)},
    {"name": "Department B", "male": (20, 10), "female": (100, 60)},
]


def _rate(admitted: int, applied: int) -> float:
    return admitted / applied * 100 if applied else 0.0


def dataset() -> dict:
    """Return per-department and aggregated acceptance rates."""
    departments = []
    totals = {"male": [0, 0], "female": [0, 0]}  # [applied, admitted]

    for dept in _DEPARTMENTS:
        m_applied, m_admitted = dept["male"]
        f_applied, f_admitted = dept["female"]
        totals["male"][0] += m_applied
        totals["male"][1] += m_admitted
        totals["female"][0] += f_applied
        totals["female"][1] += f_admitted
        departments.append(
            {
                "name": dept["name"],
                "male_applied": m_applied,
                "male_admitted": m_admitted,
                "male_rate": _rate(m_admitted, m_applied),
                "female_applied": f_applied,
                "female_admitted": f_admitted,
                "female_rate": _rate(f_admitted, f_applied),
            }
        )

    male_rate = _rate(totals["male"][1], totals["male"][0])
    female_rate = _rate(totals["female"][1], totals["female"][0])

    # The paradox: women win every department but lose overall (or vice versa).
    female_wins_all = all(d["female_rate"] > d["male_rate"] for d in departments)
    male_wins_overall = male_rate > female_rate

    return {
        "departments": departments,
        "overall": {
            "male_applied": totals["male"][0],
            "male_admitted": totals["male"][1],
            "male_rate": male_rate,
            "female_applied": totals["female"][0],
            "female_admitted": totals["female"][1],
            "female_rate": female_rate,
        },
        "paradox": female_wins_all and male_wins_overall,
    }
