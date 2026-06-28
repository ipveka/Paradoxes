import Link from "next/link";

export function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-ink/10 bg-paper/90 backdrop-blur">
      <nav className="mx-auto flex max-w-6xl items-center justify-between gap-4 px-4 py-3 sm:px-8">
        <Link href="/" className="flex items-center gap-2 text-base font-extrabold tracking-tight">
          <span>🧩</span>
          <span>Paradoxes</span>
        </Link>
        <div className="flex items-center gap-5 text-xs font-bold uppercase tracking-[0.12em] text-slate-500">
          <Link href="/#index" className="transition-colors hover:text-accent">
            Index
          </Link>
          <a
            href="https://github.com/ipveka/paradoxes"
            target="_blank"
            rel="noreferrer"
            className="transition-colors hover:text-accent"
          >
            GitHub
          </a>
        </div>
      </nav>
    </header>
  );
}
