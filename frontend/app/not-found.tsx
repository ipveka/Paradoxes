import Link from "next/link";

export default function NotFound() {
  return (
    <div className="mx-auto flex max-w-6xl flex-col items-start px-4 py-20 sm:px-8 sm:py-28">
      <h1 className="font-extrabold uppercase leading-[0.82] tracking-tightest text-[clamp(4rem,18vw,13rem)]">
        4<span className="accent-text">0</span>4
      </h1>
      <div className="mt-4 w-full border-t-[3px] border-ink pt-6">
        <p className="max-w-lg text-lg font-medium leading-snug sm:text-xl">
          The odds of finding this page were low. It doesn&apos;t exist — or it
          switched doors when you weren&apos;t looking.
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          <Link href="/" className="btn-primary">
            ← Back home
          </Link>
          <Link href="/paradoxes/monty-hall" className="btn-ghost">
            Play Monty Hall
          </Link>
        </div>
      </div>
    </div>
  );
}
