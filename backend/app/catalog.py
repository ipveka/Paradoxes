"""Static metadata describing each paradox, served at /api/paradoxes."""
from __future__ import annotations

PARADOXES = [
    {
        "id": "monty-hall",
        "name": "Monty Hall",
        "emoji": "🚪",
        "tagline": "Why switching doors wins twice as often",
        "blurb": (
            "Pick one of three doors, the host reveals a goat, then you decide: "
            "stick or switch? Switching wins 2/3 of the time — and most people "
            "refuse to believe it."
        ),
        "wikipedia": "https://en.wikipedia.org/wiki/Monty_Hall_problem",
    },
    {
        "id": "birthday",
        "name": "Birthday Paradox",
        "emoji": "🎂",
        "tagline": "23 people, 50/50 odds of a shared birthday",
        "blurb": (
            "It feels like you'd need hundreds of people for a birthday match, "
            "but the number of *pairs* grows fast — just 23 people cross the "
            "50% line."
        ),
        "wikipedia": "https://en.wikipedia.org/wiki/Birthday_problem",
    },
    {
        "id": "two-envelopes",
        "name": "Two Envelopes",
        "emoji": "✉️",
        "tagline": "The switch that looks profitable but isn't",
        "blurb": (
            "One envelope holds twice the other. A tempting calculation says you "
            "should always switch — forever. Simulation shows switching gains you "
            "nothing."
        ),
        "wikipedia": "https://en.wikipedia.org/wiki/Two_envelopes_problem",
    },
    {
        "id": "sleeping-beauty",
        "name": "Sleeping Beauty",
        "emoji": "😴",
        "tagline": "Is it 1/2 or 1/3? Philosophers still argue",
        "blurb": (
            "Woken once on Heads and twice on Tails (with memory wiped), what "
            "should Beauty believe about the coin? Counting awakenings points "
            "to 1/3."
        ),
        "wikipedia": "https://en.wikipedia.org/wiki/Sleeping_Beauty_problem",
    },
    {
        "id": "simpsons",
        "name": "Simpson's Paradox",
        "emoji": "📊",
        "tagline": "When the parts and the whole disagree",
        "blurb": (
            "A trend that holds in every subgroup can flip when you pool the "
            "data. Hidden variables make aggregated statistics lie."
        ),
        "wikipedia": "https://en.wikipedia.org/wiki/Simpson%27s_paradox",
    },
]
