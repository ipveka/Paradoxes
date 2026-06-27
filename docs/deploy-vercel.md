# Deploying to Vercel (all-in-one)

This deploys the **whole app as a single Vercel project**: the Next.js site plus
the FastAPI backend running as a Python serverless function. The simulations are
light and stateless, so serverless is a great fit — and there's only one thing
to maintain.

## How it fits together

[`vercel.json`](../vercel.json) declares two builds and routes between them:

- `frontend/` → the Next.js site (`@vercel/next`).
- `api/index.py` → a Python function (`@vercel/python`) that **reuses the
  existing `backend/` app** (bundled via `includeFiles`), so the API logic still
  lives in exactly one place. No code is duplicated.

Requests route like this:

| Path | Served by |
| ---- | --------- |
| `/api/*`, `/health`, `/docs`, `/openapi.json` | the FastAPI function |
| everything else | the Next.js site |

Because both run on the same domain, the browser calls the API at a relative
`/api/...` path — no CORS, no second URL to configure.

## Deploy

1. In Vercel: **Add New → Project**, import `ipveka/Paradoxes`.
2. Leave **Root Directory = repository root** (the `vercel.json` handles
   locating the Next app in `frontend/`). Do *not* set it to `frontend`.
3. Add one environment variable (Production **and** Preview):
   - `NEXT_PUBLIC_API_URL` = `/`  ← a single slash, meaning "same origin"
4. **Deploy.**

That's it. Preview deployments work automatically too, since the API rides along
on the same deployment.

> Why `NEXT_PUBLIC_API_URL=/`? It's baked into the frontend at build time and
> tells the client to call the API at a relative path. Left unset, the app
> defaults to `http://localhost:8000` for local development. See
> `frontend/lib/api.ts`.

## Verify

- `https://<your-app>.vercel.app/health` → `{"status":"ok"}`
- `https://<your-app>.vercel.app/docs` → Swagger UI
- Open the site → **Monty Hall** → *Run simulation* → switch rate ≈ 67%.

## Notes & limits

- **Cold starts:** the Python function sleeps when idle and cold-starts on the
  next request (a couple of seconds, including the NumPy import). Fine here
  because the simulations themselves are fast.
- **Execution time:** serverless functions have a max duration. The default
  request sizes are well within it; the API also caps simulation sizes
  (`backend/app/schemas.py`) so a request can't run unbounded.
- **Local dev is unchanged:** run the backend with `uvicorn app.main:app`
  from `backend/` and the frontend with `npm run dev`. `api/index.py` is only
  used by Vercel.

## Prefer two separate services?

The repo also ships a Render Blueprint that runs the backend as a normal
long-lived service. See [`deploy-render.md`](./deploy-render.md).
