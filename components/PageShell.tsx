import Link from "next/link";
import type { Paradox } from "@/lib/paradoxes";
import { paradoxSlugs } from "@/lib/paradoxes";
import { Reveal } from "@/components/Reveal";

export function PageShell({
  paradox,
  children,
}: {
  paradox: Paradox;
  children: React.ReactNode;
}) {
  const number = String(paradoxSlugs.indexOf(paradox.slug) + 1).padStart(2, "0");

  return (
    <article className="mx-auto max-w-4xl px-4 pb-24 sm:px-8">
      {/* Hero */}
      <header className="pt-10 sm:pt-14">
        <Link href="/#index" className="label transition-colors hover:text-accent">
          ← All paradoxes
        </Link>
        <div className="mt-5 flex items-start justify-between gap-4 border-b-[3px] border-ink pb-6">
          <div>
            <span className="text-sm font-bold tabular-nums text-slate-300">No. {number}</span>
            <h1 className="mt-1 text-4xl font-extrabold uppercase leading-[0.9] tracking-tight sm:text-6xl">
              {paradox.name}
            </h1>
            <p className="mt-3 text-lg font-medium accent-text">{paradox.tagline}</p>
          </div>
          <span className="text-5xl sm:text-7xl">{paradox.emoji}</span>
        </div>
      </header>

      {/* Setup + intuition */}
      <Reveal>
        <section className="mt-10">
          <h2 className="label">The setup</h2>
          <ol className="mt-4 space-y-3">
            {paradox.setup.map((line, i) => (
              <li key={i} className="flex gap-4 text-lg leading-relaxed">
                <span className="font-extrabold tabular-nums text-slate-300">{i + 1}</span>
                <span>{line}</span>
              </li>
            ))}
          </ol>
          <div className="mt-6 border-l-4 border-accent bg-brand-50 px-5 py-4">
            <span className="font-bold">🤔 Intuition says: </span>
            {paradox.intuition}
          </div>
        </section>
      </Reveal>

      {/* Interactive widget */}
      <Reveal>
        <section className="mt-12">{children}</section>
      </Reveal>

      {/* Explanation */}
      <Reveal>
        <section className="mt-12 border-t-2 border-ink pt-8">
          <h2 className="label">Why it&apos;s a paradox</h2>
          <div className="mt-4 space-y-3">
            {paradox.explanation.map((line, i) => (
              <p key={i} className="text-lg leading-relaxed">
                {line}
              </p>
            ))}
          </div>
          <div className="mt-6 border-l-4 border-ink bg-slate-50 px-5 py-4">
            <span className="font-bold">💡 Key insight: </span>
            {paradox.insight}
          </div>
          <a
            href={paradox.wikipedia}
            target="_blank"
            rel="noreferrer"
            className="label mt-6 inline-block transition-colors hover:text-accent"
          >
            Further reading on Wikipedia →
          </a>
        </section>
      </Reveal>
    </article>
  );
}
