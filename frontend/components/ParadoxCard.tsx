import Link from "next/link";
import type { Paradox } from "@/lib/paradoxes";

export function ParadoxCard({ paradox }: { paradox: Paradox }) {
  return (
    <Link
      href={`/paradoxes/${paradox.slug}`}
      className="group card flex flex-col gap-3 p-6 transition-all hover:-translate-y-1 hover:shadow-xl"
    >
      <div
        className={`flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br ${paradox.gradient} text-3xl shadow-md transition-transform group-hover:scale-110`}
      >
        {paradox.emoji}
      </div>
      <h3 className="text-lg font-bold text-slate-900">{paradox.name}</h3>
      <p className="text-sm font-medium text-brand-600">{paradox.tagline}</p>
      <p className="text-sm leading-relaxed text-slate-500">{paradox.blurb}</p>
      <span className="mt-auto pt-2 text-sm font-semibold text-slate-700 transition-colors group-hover:text-brand-600">
        Explore →
      </span>
    </Link>
  );
}
