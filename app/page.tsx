import Link from "next/link";
import { PARADOXES } from "@/lib/paradoxes";
import { IndexRow } from "@/components/IndexRow";
import { Reveal } from "@/components/Reveal";

export default function HomePage() {
  return (
    <div className="mx-auto max-w-6xl px-4 sm:px-8">
      {/* Hero wordmark */}
      <section className="pt-12 sm:pt-16">
        <Reveal>
          <h1 className="font-extrabold uppercase leading-[0.82] tracking-tightest text-[clamp(3.25rem,13vw,9.5rem)]">
            Para<span className="accent-text">dox</span>es
          </h1>
        </Reveal>
        <Reveal delay={0.05}>
          <div className="mt-6 flex flex-col gap-6 border-b-[3px] border-ink pb-8 sm:flex-row sm:items-end sm:justify-between">
            <p className="max-w-md text-lg font-medium leading-snug sm:text-xl">
              Five probability puzzles that prove your intuition wrong — with live
              simulations to settle every one.
            </p>
            <Link href={`/paradoxes/${PARADOXES[0].slug}`} className="btn-primary shrink-0">
              Start → Monty Hall
            </Link>
          </div>
        </Reveal>
      </section>

      {/* Numbered index */}
      <section id="index" className="scroll-mt-20 pb-24 pt-2">
        {PARADOXES.map((paradox, i) => (
          <Reveal key={paradox.slug} delay={i * 0.04}>
            <IndexRow paradox={paradox} index={i} />
          </Reveal>
        ))}
      </section>
    </div>
  );
}
