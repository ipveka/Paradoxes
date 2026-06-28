"use client";

import type { ParadoxSlug } from "@/lib/paradoxes";
import { MontyHall } from "./MontyHall";
import { Birthday } from "./Birthday";
import { TwoEnvelopes } from "./TwoEnvelopes";
import { SleepingBeauty } from "./SleepingBeauty";
import { Simpsons } from "./Simpsons";

const WIDGETS: Record<ParadoxSlug, () => JSX.Element> = {
  "monty-hall": MontyHall,
  birthday: Birthday,
  "two-envelopes": TwoEnvelopes,
  "sleeping-beauty": SleepingBeauty,
  simpsons: Simpsons,
};

export function ParadoxView({ slug }: { slug: ParadoxSlug }) {
  const Widget = WIDGETS[slug];
  return <Widget />;
}
