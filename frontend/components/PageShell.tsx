import type { Paradox } from "@/lib/paradoxes";
import { Reveal } from "@/components/Reveal";

export function PageShell({
  paradox,
  children,
}: {
  paradox: Paradox;
  children: React.ReactNode;
}) {
  return (
    <article className="mx-auto max-w-4xl px-4 pb-24">
      {/* Hero */}
      <header className="py-12 text-center">
        <div
          className={`mx-auto flex h-20 w-20 items-center justify-center rounded-3xl bg-gradient-to-br ${paradox.gradient} text-5xl shadow-lg`}
        >
          {paradox.emoji}
        </div>
        <h1 className="mt-6 text-4xl font-extrabold tracking-tight sm:text-5xl">
          {paradox.name}
        </h1>
        <p className="mt-3 text-lg font-medium text-brand-600">{paradox.tagline}</p>
      </header>

      {/* Setup + intuition */}
      <Reveal>
        <section className="card p-6 sm:p-8">
          <h2 className="text-sm font-semibold uppercase tracking-wide text-slate-400">
            The setup
          </h2>
          <ol className="mt-4 space-y-3">
            {paradox.setup.map((line, i) => (
              <li key={i} className="flex gap-3 text-slate-700">
                <span className="flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-brand-50 text-xs font-bold text-brand-600">
                  {i + 1}
                </span>
                <span className="leading-relaxed">{line}</span>
              </li>
            ))}
          </ol>
          <div className="mt-6 rounded-xl border border-amber-200 bg-amber-50 p-4 text-amber-900">
            <span className="font-semibold">🤔 Intuition says: </span>
            {paradox.intuition}
          </div>
        </section>
      </Reveal>

      {/* Interactive widget */}
      <Reveal>
        <section className="mt-8">{children}</section>
      </Reveal>

      {/* Explanation */}
      <Reveal>
        <section className="card mt-8 p-6 sm:p-8">
          <h2 className="text-sm font-semibold uppercase tracking-wide text-slate-400">
            Why it&apos;s a paradox
          </h2>
          <div className="mt-4 space-y-3">
            {paradox.explanation.map((line, i) => (
              <p key={i} className="leading-relaxed text-slate-700">
                {line}
              </p>
            ))}
          </div>
          <div className="mt-6 rounded-xl border border-brand-100 bg-brand-50 p-4 text-brand-900">
            <span className="font-semibold">💡 Key insight: </span>
            {paradox.insight}
          </div>
          <a
            href={paradox.wikipedia}
            target="_blank"
            rel="noreferrer"
            className="mt-6 inline-block text-sm font-medium text-brand-600 hover:underline"
          >
            Further reading on Wikipedia →
          </a>
        </section>
      </Reveal>
    </article>
  );
}
