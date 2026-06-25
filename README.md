# 🧩 Paradoxes

> Where intuition meets mathematics — an interactive, simulation-driven website
> for the most mind-bending paradoxes in probability and statistics.

Five famous paradoxes that fool almost everyone. Each one pairs a plain-language
explanation with **live Monte Carlo simulations** so you can watch the
counterintuitive answer emerge from real data.

- 🚪 **Monty Hall** — why switching doors wins twice as often
- 🎂 **Birthday Paradox** — 23 people, 50/50 odds of a shared birthday
- ✉️ **Two Envelopes** — the switch that looks profitable but isn't
- 😴 **Sleeping Beauty** — is it ½ or ⅓? Philosophers still argue
- 📊 **Simpson's Paradox** — when the parts and the whole disagree

## Stack

| Layer | Tech |
| ----- | ---- |
| Frontend | Next.js (App Router) · TypeScript · Tailwind CSS · Framer Motion · Recharts |
| Backend | FastAPI · NumPy · Pydantic |
| Deploy | Render Blueprint (two web services) |

The simulations run server-side in Python and are exposed as a small JSON API;
the frontend calls that API and animates the results. See
[`docs/architecture.md`](docs/architecture.md) for the full picture.

## Quick start

You'll need **Python 3.11+** and **Node 18+**. Run the two services in separate
terminals.

### 1. Backend (API on :8000)

```bash
cd backend
pip install -r requirements-dev.txt
uvicorn app.main:app --reload          # http://localhost:8000  (docs at /docs)
```

### 2. Frontend (website on :3000)

```bash
cd frontend
npm install
cp .env.example .env.local             # defaults to http://localhost:8000
npm run dev                            # http://localhost:3000
```

Open http://localhost:3000, head to **Monty Hall**, and hit *Run simulation*.

## Tests

```bash
cd backend && pytest                   # simulation math + API contract
cd frontend && npm run build           # type-checks and pre-renders every page
```

## Project layout

```
backend/            FastAPI service (simulations, API, tests)
frontend/           Next.js website (pages, components, design system)
legacy/streamlit/   Original Streamlit prototype (kept for reference)
docs/
├── architecture.md   How the pieces fit together
├── deploy-render.md  Step-by-step Render deployment
└── concepts.md       The mathematics behind each paradox
render.yaml         One-command deploy of both services
```

## Deploy

A [`render.yaml`](render.yaml) Blueprint provisions both services on Render's
free plan. Full walkthrough — including the two environment variables to set — is
in [`docs/deploy-render.md`](docs/deploy-render.md).

## Adding a new paradox

1. **Backend:** add a pure simulation in `backend/app/simulations/`, a schema in
   `schemas.py`, and a route in `routers/paradoxes.py` (plus a test).
2. **Frontend:** add the response type to `lib/api.ts`, an entry to
   `lib/paradoxes.ts`, and a widget in `components/paradox/` registered in
   `ParadoxView.tsx`.

The home grid, navbar, and routing update automatically from the registry.

## License

MIT — see [LICENSE](LICENSE).

**Maintained at [ipveka/paradoxes](https://github.com/ipveka/paradoxes).**
