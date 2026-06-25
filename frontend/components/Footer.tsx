export function Footer() {
  return (
    <footer className="border-t border-slate-200/70 bg-white/50">
      <div className="mx-auto max-w-6xl px-4 py-10 text-center text-sm text-slate-500">
        <p className="mx-auto max-w-2xl leading-relaxed">
          Explore the most mind-bending puzzles in probability through interactive
          simulations — and see the mathematics that reveals the truth.
        </p>
        <p className="mt-4">
          Built with Next.js &amp; FastAPI ·{" "}
          <a
            href="https://github.com/ipveka/paradoxes"
            target="_blank"
            rel="noreferrer"
            className="font-medium text-brand-600 hover:underline"
          >
            ipveka/paradoxes
          </a>
        </p>
      </div>
    </footer>
  );
}
