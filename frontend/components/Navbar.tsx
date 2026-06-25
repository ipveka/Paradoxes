import Link from "next/link";
import { PARADOXES } from "@/lib/paradoxes";

export function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-slate-200/70 bg-white/70 backdrop-blur">
      <nav className="mx-auto flex max-w-6xl items-center justify-between gap-4 px-4 py-3">
        <Link href="/" className="flex items-center gap-2 font-bold">
          <span className="text-xl">🧩</span>
          <span className="gradient-text text-lg">Paradoxes</span>
        </Link>
        <div className="hidden items-center gap-1 md:flex">
          {PARADOXES.map((p) => (
            <Link
              key={p.slug}
              href={`/paradoxes/${p.slug}`}
              className="rounded-lg px-3 py-1.5 text-sm font-medium text-slate-600 transition-colors hover:bg-slate-100 hover:text-slate-900"
            >
              <span className="mr-1">{p.emoji}</span>
              {p.name}
            </Link>
          ))}
        </div>
        <a
          href="https://github.com/ipveka/paradoxes"
          target="_blank"
          rel="noreferrer"
          className="btn-ghost text-sm"
        >
          GitHub
        </a>
      </nav>
    </header>
  );
}
