import Link from "next/link";
import type { Paradox } from "@/lib/paradoxes";

export function IndexRow({ paradox, index }: { paradox: Paradox; index: number }) {
  return (
    <Link
      href={`/paradoxes/${paradox.slug}`}
      className="group grid grid-cols-[3rem_1fr_auto] items-center gap-5 border-b border-slate-200 py-5 sm:grid-cols-[5rem_1fr_auto] sm:py-6"
    >
      <span className="text-3xl font-extrabold tabular-nums tracking-tight text-slate-300 transition-colors group-hover:text-accent sm:text-5xl">
        {String(index + 1).padStart(2, "0")}
      </span>
      <span>
        <span className="block text-2xl font-extrabold uppercase tracking-tight transition-colors group-hover:text-accent sm:text-4xl">
          {paradox.name}
        </span>
        <span className="mt-1 block text-sm text-slate-500 sm:text-base">{paradox.tagline}</span>
      </span>
      <span className="text-3xl transition-transform group-hover:scale-110 sm:text-4xl">
        {paradox.emoji}
      </span>
    </Link>
  );
}
