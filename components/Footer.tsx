export function Footer() {
  return (
    <footer className="border-t-2 border-ink">
      <div className="mx-auto flex max-w-6xl flex-col gap-3 px-4 py-8 text-sm sm:flex-row sm:items-center sm:justify-between sm:px-8">
        <p className="font-bold uppercase tracking-[0.12em] text-ink">🧩 Paradoxes</p>
        <p className="text-slate-500">
          Built with Next.js &amp; FastAPI ·{" "}
          <a
            href="https://github.com/ipveka/paradoxes"
            target="_blank"
            rel="noreferrer"
            className="font-semibold text-accent hover:underline"
          >
            ipveka/paradoxes
          </a>
        </p>
      </div>
    </footer>
  );
}
