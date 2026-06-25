# Paradoxes — Frontend

Next.js (App Router) + TypeScript + Tailwind CSS + Framer Motion + Recharts.

## Develop

```bash
npm install
cp .env.example .env.local   # point NEXT_PUBLIC_API_URL at your backend
npm run dev                  # http://localhost:3000
```

The frontend talks to the FastAPI backend (see `../backend`). Start that first,
or the simulation buttons will show a connection error.

## Build

```bash
npm run build
npm start
```

## Structure

```
app/                       App Router pages
  page.tsx                 Home (hero + paradox grid)
  paradoxes/[slug]/        Dynamic paradox page (SSG via generateStaticParams)
components/
  charts/                  Reusable Recharts components
  paradox/                 One interactive widget per paradox + ParadoxView switch
  PageShell, Navbar, ...   Layout + shared UI
lib/
  api.ts                   Typed fetch client (mirrors backend schemas)
  paradoxes.ts             Registry: metadata + teaching copy for every paradox
```

## Adding a paradox

1. Add a backend endpoint + response type in `lib/api.ts`.
2. Add an entry to `PARADOXES` in `lib/paradoxes.ts`.
3. Create a widget in `components/paradox/` and register it in `ParadoxView.tsx`.

The home grid and navbar update automatically from the registry.
