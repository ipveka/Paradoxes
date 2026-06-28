# Architecture

Paradoxes is a small monorepo: a Next.js frontend and a FastAPI backend that can
be deployed either as one Vercel project or as two Render services.

The Next.js app sits at the repository root (Vercel's canonical layout); the
Python lives under `backend/`.

```
Paradoxes/
├── app/              Next.js App Router pages
├── components/       React components (charts, paradox widgets, layout)
├── lib/              Typed API client + paradox registry
├── backend/          FastAPI + NumPy — the simulation engine and HTTP API
├── api/              Vercel Python function that reuses backend/ (Vercel only)
├── docs/             This documentation (incl. design/ system + explorations)
├── vercel.json       All-in-one Vercel config (rewrites + the API function)
└── render.yaml       Two-service Render Blueprint
```

## Why a separate backend?

The Monte Carlo simulations are the "real" artifact — they're the proof that the
counterintuitive answers are correct. Running them in Python keeps the math in
one tested place, lets the browser stay light, and makes the API reusable
(notebooks, CLIs, other frontends). The frontend is then a pure presentation
layer that calls the API and animates the results.

The backend is the single source of truth regardless of host: on Render it runs
as a long-lived service; on Vercel the same `backend/app` is served by a Python
serverless function (`api/index.py`). See the deploy guides in `docs/`.

## Backend (`backend/`)

```
app/
├── main.py            FastAPI app: CORS, router include, /health
├── config.py          Env-driven settings (ALLOWED_ORIGINS)
├── catalog.py         Static metadata for every paradox (served at /api/paradoxes)
├── schemas.py         Pydantic request/response models
├── routers/
│   └── paradoxes.py   All /api/* endpoints
└── simulations/       Pure, testable simulation functions (one file per paradox)
tests/                 pytest suite asserting each statistical claim
```

**Design rule:** `simulations/*.py` are pure functions of their inputs (with an
optional RNG `seed`) and have no FastAPI imports. The router is the only layer
that knows about HTTP. This keeps the math unit-testable in isolation.

### API surface

| Method | Path | Purpose |
| ------ | ---- | ------- |
| GET  | `/health` | Liveness probe |
| GET  | `/api/paradoxes` | Catalog + display metadata |
| POST | `/api/monty-hall/simulate` | `{games, seed?}` → win rates |
| POST | `/api/birthday/simulate` | `{group_size, trials, seed?}` |
| GET  | `/api/birthday/curve` | Exact probability curve |
| POST | `/api/two-envelopes/simulate` | `{trials, seed?}` |
| POST | `/api/sleeping-beauty/simulate` | `{trials, seed?}` |
| GET  | `/api/simpsons/data` | Illustrative admissions dataset |

Interactive docs are auto-generated at `/docs` (Swagger UI).

## Frontend (repository root)

Next.js App Router with static generation for each paradox page.

```
app/
├── page.tsx                  Home: hero + paradox grid
├── paradoxes/[slug]/page.tsx Dynamic page, SSG via generateStaticParams
└── layout.tsx, globals.css   Shell + design system
components/
├── charts/                   Reusable Recharts wrappers
├── paradox/                  One widget per paradox + ParadoxView switch
└── PageShell, Navbar, ...    Layout + shared UI
lib/
├── api.ts                    Typed fetch client (mirrors backend schemas)
└── paradoxes.ts              Registry: metadata + teaching copy
```

**Single source of truth:** `lib/paradoxes.ts` drives the home grid, the navbar,
and each page's copy. `lib/api.ts` types mirror `backend/app/schemas.py` — keep
them in sync when changing a response shape.

## Data flow

```
Browser ──(fetch JSON)──▶ Next.js page ──(NEXT_PUBLIC_API_URL)──▶ FastAPI ──▶ NumPy
   ▲                                                                          │
   └──────────────── Recharts renders the returned numbers ◀─────────────────┘
```

The frontend reads `NEXT_PUBLIC_API_URL` (baked at build time) to find the API.
The backend reads `ALLOWED_ORIGINS` to permit the frontend's origin via CORS.
