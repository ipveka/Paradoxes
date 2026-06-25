import Link from "next/link";
import { PARADOXES } from "@/lib/paradoxes";
import { ParadoxCard } from "@/components/ParadoxCard";
import { Reveal } from "@/components/Reveal";

export default function HomePage() {
  return (
    <div className="mx-auto max-w-6xl px-4">
      {/* Hero */}
      <section className="py-20 text-center sm:py-28">
        <Reveal>
          <span className="inline-block rounded-full border border-brand-100 bg-white/70 px-4 py-1.5 text-sm font-medium text-brand-600 shadow-sm">
            🧩 Interactive probability, powered by live simulations
          </span>
        </Reveal>
        <Reveal delay={0.05}>
          <h1 className="mx-auto mt-6 max-w-3xl text-5xl font-extrabold tracking-tight sm:text-6xl">
            Where intuition meets <span className="gradient-text">mathematics</span>
          </h1>
        </Reveal>
        <Reveal delay={0.1}>
          <p className="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-slate-600">
            Five famous paradoxes that fool almost everyone. Run real Monte Carlo
            simulations, watch the charts move, and discover why your gut is wrong.
          </p>
        </Reveal>
        <Reveal delay={0.15}>
          <div className="mt-8 flex items-center justify-center gap-3">
            <Link href={`/paradoxes/${PARADOXES[0].slug}`} className="btn-primary">
              Start with Monty Hall
            </Link>
            <a href="#paradoxes" className="btn-ghost">
              Browse all five
            </a>
          </div>
        </Reveal>
      </section>

      {/* Grid */}
      <section id="paradoxes" className="scroll-mt-20 pb-24">
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {PARADOXES.map((paradox, i) => (
            <Reveal key={paradox.slug} delay={i * 0.05}>
              <ParadoxCard paradox={paradox} />
            </Reveal>
          ))}
        </div>
      </section>
    </div>
  );
}
