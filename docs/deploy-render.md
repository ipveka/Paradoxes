# Deploying to Render

The repo ships a [`render.yaml`](../render.yaml) Blueprint that provisions both
services at once: a Python web service for the API and a Node web service for the
website. Both run on Render's free plan.

## One-time setup

1. Push this repository to GitHub (already done if you're reading this on GitHub).
2. In the Render dashboard, click **New → Blueprint**.
3. Connect the repository. Render detects `render.yaml` and shows two services:
   `paradoxes-api` and `paradoxes-web`.
4. Click **Apply**. The first build starts immediately.

## Set the two cross-references

The services need to know each other's URLs. They're marked `sync: false` in the
Blueprint, so Render will prompt you for them (or set them under each service's
**Environment** tab). After the first deploy you'll have two URLs like:

- API: `https://paradoxes-api.onrender.com`
- Web: `https://paradoxes-web.onrender.com`

Set:

| Service | Variable | Value |
| ------- | -------- | ----- |
| `paradoxes-api` | `ALLOWED_ORIGINS` | the **web** URL, e.g. `https://paradoxes-web.onrender.com` |
| `paradoxes-web` | `NEXT_PUBLIC_API_URL` | the **API** URL, e.g. `https://paradoxes-api.onrender.com` |

> ⚠️ `NEXT_PUBLIC_API_URL` is compiled into the frontend **at build time**. After
> changing it, trigger a redeploy/clear-build-cache of `paradoxes-web` so the new
> value is baked in. `ALLOWED_ORIGINS` is read at runtime, so the API only needs a
> restart.

`ALLOWED_ORIGINS` accepts a comma-separated list, so you can include a custom
domain too: `https://paradoxes-web.onrender.com,https://paradoxes.example.com`.

## Verify

1. Open `https://paradoxes-api.onrender.com/health` → `{"status":"ok"}`.
2. Open `https://paradoxes-api.onrender.com/docs` → Swagger UI.
3. Open the web URL, go to **Monty Hall**, and click **Run simulation** — the
   switch win rate should land near 67%. If it errors, re-check the two variables
   above (most failures are a CORS mismatch or a stale `NEXT_PUBLIC_API_URL`).

## Notes on the free plan

Free web services sleep after inactivity and cold-start on the next request, so
the first simulation after a while may take a few seconds while the API wakes up.
Upgrade either service to a paid instance to keep it warm.

## Alternative: Docker / other hosts

`backend/Dockerfile` builds a standalone API image if you'd rather deploy the
backend as a container (Fly.io, Railway, a VM, etc.):

```bash
docker build -t paradoxes-api ./backend
docker run -p 8000:8000 -e ALLOWED_ORIGINS=https://your-frontend paradoxes-api
```

The frontend is a standard Next.js app and can be hosted anywhere that runs
`npm run build && npm start` (or on Vercel) — just set `NEXT_PUBLIC_API_URL`.
