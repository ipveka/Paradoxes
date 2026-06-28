# Deploying to Vercel (all-in-one)

This deploys the **whole app as a single Vercel project**: the Next.js site plus
the FastAPI backend running as a Python serverless function. The simulations are
light and stateless, so serverless is a great fit — and there's only one thing
to maintain.

## How it fits together

The repo uses Vercel's canonical layout: the **Next.js app is at the repository
root**, and a Python function lives in `api/`. [`vercel.json`](../vercel.json)
ties them together:

- Zero-config: Vercel auto-detects Next.js (root) and the Python function (`api/`).
- `api/index.py` **reuses the existing `backend/` app** (bundled via
  `functions.includeFiles`), so the API logic stays in exactly one place.
- `rewrites` send `/api/*`, `/health`, `/docs`, and `/openapi.json` to the
  function; everything else is served by Next.js.

Because both run on the same domain, the browser calls the API at a relative
`/api/...` path — no CORS, and nothing to configure.

## Deploy

1. In Vercel: **Add New → Project**, import `ipveka/Paradoxes`.
2. Leave every setting at its default:
   - **Framework Preset:** Next.js (auto-detected)
   - **Root Directory:** `./` (the repo root — do **not** change it)
   - **Application Preset:** Next.js (not "Services")
3. **Deploy.** No environment variables are required — the client defaults to
   same-origin API calls.

That's it. Preview deployments work automatically too.

## Verify

- `https://<your-app>.vercel.app/health` → `{"status":"ok"}`
- `https://<your-app>.vercel.app/docs` → Swagger UI
- Open the site → **Monty Hall** → *Run simulation* → switch rate ≈ 67%.

## Notes & limits

- **Cold starts:** the Python function sleeps when idle and cold-starts on the
  next request (a second or two, including the NumPy import). Fine here because
  the simulations themselves are fast.
- **Execution time:** serverless functions have a max duration; the API caps
  simulation sizes (`backend/app/schemas.py`) so a request can't run unbounded.
- **Local dev is unchanged:** run the backend with `uvicorn app.main:app` from
  `backend/` and the site with `npm run dev` (set `NEXT_PUBLIC_API_URL` in
  `.env.local`). `api/index.py` is only used by Vercel.

## Prefer two separate services?

The repo also ships a Render Blueprint that runs the backend as a normal
long-lived service. See [`deploy-render.md`](./deploy-render.md).
