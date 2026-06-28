import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { getParadox, paradoxSlugs } from "@/lib/paradoxes";
import { PageShell } from "@/components/PageShell";
import { ParadoxView } from "@/components/paradox/ParadoxView";

export function generateStaticParams() {
  return paradoxSlugs.map((slug) => ({ slug }));
}

export function generateMetadata({ params }: { params: { slug: string } }): Metadata {
  const paradox = getParadox(params.slug);
  if (!paradox) return {};
  return {
    title: `${paradox.name} · Paradoxes`,
    description: paradox.tagline,
  };
}

export default function ParadoxPage({ params }: { params: { slug: string } }) {
  const paradox = getParadox(params.slug);
  if (!paradox) notFound();

  return (
    <PageShell paradox={paradox}>
      <ParadoxView slug={paradox.slug} />
    </PageShell>
  );
}
