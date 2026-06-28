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
| Deploy | Vercel (all-in-one) or Render (two services) |

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

The Next.js app lives at the repository root. From a second terminal:

```bash
npm install
cp .env.example .env.local             # defaults to http://localhost:8000
npm run dev                            # http://localhost:3000
```

Open http://localhost:3000, head to **Monty Hall**, and hit *Run simulation*.

## Tests

```bash
cd backend && pytest                   # simulation math + API contract
npm run build                          # type-checks and pre-renders every page
```

## Project layout

The Next.js app sits at the repository root (Vercel's canonical layout); the
Python lives under `backend/`.

```
app/                Next.js App Router pages
components/          React components (charts, paradox widgets, layout)
lib/                Typed API client + paradox registry
api/                Vercel Python function (reuses backend/ on Vercel)
backend/            FastAPI service (simulations, API, tests)
docs/
├── architecture.md   How the pieces fit together
├── deploy-vercel.md  All-in-one Vercel deployment
├── deploy-render.md  Two-service Render deployment
├── concepts.md       The mathematics behind each paradox
└── design/           Design system + the explored visual directions
vercel.json         All-in-one Vercel config (rewrites + the API function)
render.yaml         Two-service Render Blueprint
```

## Deploy

Two supported options:

- **Vercel (all-in-one):** one project hosting the site and the API as a Python
  serverless function. Just import the repo and deploy — `vercel.json` wires the
  API. Walkthrough in [`docs/deploy-vercel.md`](docs/deploy-vercel.md).
- **Render (two services):** a [`render.yaml`](render.yaml) Blueprint runs the
  backend as a long-lived service plus the frontend. Walkthrough in
  [`docs/deploy-render.md`](docs/deploy-render.md).

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
