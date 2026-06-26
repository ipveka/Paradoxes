# Design System — "Big-Type Editorial"

The shipped visual direction (exploration **X**). The goal: make statistics feel
confident and uncluttered, letting bold typography and a single accent carry the
personality. No gradients, no decoration for its own sake.

## Principles

1. **Type is the design.** Oversized, tight, uppercase grotesque headings do the
   heavy lifting. Everything else stays quiet.
2. **One accent.** A single orange is the only color besides ink and paper. It
   marks the *one* thing that matters in any view (the winning strategy, the live
   value, the call to action).
3. **Flat, not glossy.** Thin hairline borders and thick structural rules instead
   of shadows, blur, or gradients.
4. **Restraint in charts.** Data is monochrome; the accent highlights the result
   the paradox is about.

## Tokens

| Token | Value | Use |
| ----- | ----- | --- |
| `ink` | `#0f0f0f` | Primary text, "losing"/neutral chart series, thick rules |
| `paper` | `#fdfdfb` | Page background |
| `accent` (`brand-500`) | `#ff4d17` | The single highlight color |
| `brand-50` | `#fff1ec` | Accent callout backgrounds |
| `slate-400/500` | Tailwind | Muted labels, secondary text, "loser" bars |

Defined in `frontend/tailwind.config.ts` (the `brand` ramp is the orange accent)
and `frontend/app/globals.css`.

## Typography

- Family: Inter (a neutral grotesque), falling back to Helvetica Neue / Arial.
- Display headings: `font-extrabold`, `uppercase`, `tracking-tightest`
  (`-0.04em`), `leading-[0.82]`. The home wordmark uses
  `text-[clamp(3.25rem,13vw,9.5rem)]`.
- Section labels: the `.label` utility — `text-xs font-bold uppercase
  tracking-[0.12em] text-slate-400`.

## Components (`globals.css`)

- `.card` — flat white panel with a hairline border, lightly rounded.
- `.btn-primary` — solid accent fill, white uppercase bold text.
- `.btn-ghost` — ink outline, fills ink on hover.
- `.accent-text` — colors one word of a heading.
- `.label` — the uppercase kicker/metadata style.

## Charts

Recharts, recolored to the palette:

- **Winner / the point** → accent `#ff4d17`.
- **Loser / neutral** → `#cbd5e1` (muted) or `#0f0f0f` (ink).
- Reference lines → ink dashed.

See `frontend/components/charts/` and the per-paradox widgets.

## Applying it elsewhere

Adding a new surface? Lead with a big uppercase title, separate sections with a
`border-t-2 border-ink` rule and a `.label` kicker, keep everything ink-on-paper,
and spend the accent on exactly one element.
