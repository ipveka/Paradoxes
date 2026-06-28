// Single source of truth for paradox metadata and teaching copy. Both the home
// page grid and each paradox page read from here, so adding a paradox is one
// entry plus a widget component.

export type ParadoxSlug =
  | "monty-hall"
  | "birthday"
  | "two-envelopes"
  | "sleeping-beauty"
  | "simpsons";

export interface Paradox {
  slug: ParadoxSlug;
  name: string;
  emoji: string;
  tagline: string;
  blurb: string;
  wikipedia: string;
  setup: string[];
  intuition: string;
  explanation: string[];
  insight: string;
}

export const PARADOXES: Paradox[] = [
  {
    slug: "monty-hall",
    name: "Monty Hall",
    emoji: "🚪",
    tagline: "Why switching doors wins twice as often",
    blurb:
      "Pick a door, the host reveals a goat, then choose: stick or switch? Switching wins 2/3 of the time.",
    wikipedia: "https://en.wikipedia.org/wiki/Monty_Hall_problem",
    setup: [
      "Behind one of three doors is a car; behind the other two, goats.",
      "You pick a door. The host — who knows where the car is — opens a different door to reveal a goat.",
      "Now the big question: do you stay with your door, or switch to the other unopened one?",
    ],
    intuition: "Two doors left, so it feels like a 50/50 coin flip. Why bother switching?",
    explanation: [
      "Your first pick had a 1/3 chance of being right — and a 2/3 chance of being wrong.",
      "The host is constrained: he can never open your door or the car. When your pick is wrong (2/3 of the time), he is forced to leave the car behind the other door.",
      "So switching is really a bet that your original guess was wrong — and that bet pays off 2/3 of the time.",
    ],
    insight: "The host's knowledge leaks information. Switching converts your likely-wrong first guess into a 2/3 win.",
  },
  {
    slug: "birthday",
    name: "Birthday Paradox",
    emoji: "🎂",
    tagline: "23 people, 50/50 odds of a shared birthday",
    blurb:
      "It feels like you'd need hundreds of people for a match, but 23 is enough to cross 50%.",
    wikipedia: "https://en.wikipedia.org/wiki/Birthday_problem",
    setup: [
      "In a group of N people, what's the chance that at least two share a birthday?",
      "Most people guess you'd need a huge crowd to get even odds.",
      "In fact, just 23 people gives you a better-than-even chance.",
    ],
    intuition: "There are 365 days, so surely you need ~180 people for a 50% chance?",
    explanation: [
      "You're not matching one specific person — you're matching any pair in the group.",
      "A group of 23 people contains 253 distinct pairs (23 × 22 / 2), and each pair is a chance for a collision.",
      "The probability of no shared birthday shrinks fast as pairs pile up, so the match probability climbs much faster than intuition expects.",
    ],
    insight: "Coincidence scales with the number of pairs, not the number of people.",
  },
  {
    slug: "two-envelopes",
    name: "Two Envelopes",
    emoji: "✉️",
    tagline: "The switch that looks profitable but isn't",
    blurb:
      "One envelope holds twice the other. A tempting calculation says always switch — forever.",
    wikipedia: "https://en.wikipedia.org/wiki/Two_envelopes_problem",
    setup: [
      "Two envelopes: one holds twice as much money as the other.",
      "You pick one. The 'expected value' argument says the other envelope averages 1.25× yours — so you should switch.",
      "But the same logic applies again after switching, and again... forever.",
    ],
    intuition: "Expected value says switching beats staying by 25%. So always switch?",
    explanation: [
      "The flawed step assumes every amount of money is equally likely, which would require an impossible infinite uniform distribution.",
      "Once you account for a real prior over the amounts, the apparent 25% edge disappears.",
      "Simulating many rounds confirms it: always-switch and always-stay earn the same on average.",
    ],
    insight: "You can't assume a flat prior over all amounts. The 'edge' was an artifact of bad bookkeeping.",
  },
  {
    slug: "sleeping-beauty",
    name: "Sleeping Beauty",
    emoji: "😴",
    tagline: "Is it 1/2 or 1/3? Philosophers still argue",
    blurb:
      "Woken once on Heads, twice on Tails with memory wiped — what should Beauty believe?",
    wikipedia: "https://en.wikipedia.org/wiki/Sleeping_Beauty_problem",
    setup: [
      "Beauty is put to sleep on Sunday and a fair coin is tossed.",
      "Heads: she's woken once (Monday). Tails: she's woken twice (Monday and Tuesday), with her memory of Monday erased.",
      "Each time she wakes, she's asked: what's the probability the coin came up Heads?",
    ],
    intuition: "The coin is fair, so the answer is obviously 1/2 — isn't it?",
    explanation: [
      "Halfers say no new information arrives on waking, so P(Heads) = 1/2.",
      "Thirders count waking moments: across many runs there are twice as many Tails awakenings as Heads ones.",
      "If Beauty bets on the coin every time she wakes, betting Tails wins twice as often — supporting the 1/3 answer.",
    ],
    insight: "Self-locating uncertainty splits 'probability of the coin' from 'probability given that you're awake right now.'",
  },
  {
    slug: "simpsons",
    name: "Simpson's Paradox",
    emoji: "📊",
    tagline: "When the parts and the whole disagree",
    blurb:
      "A trend that holds in every subgroup can reverse when you pool the data.",
    wikipedia: "https://en.wikipedia.org/wiki/Simpson%27s_paradox",
    setup: [
      "Two departments are admitting students; we compare acceptance rates by gender.",
      "In each department individually, women are accepted at a higher rate than men.",
      "Yet when you combine the departments, men come out ahead overall.",
    ],
    intuition: "If women win in every department, they must win overall. Right?",
    explanation: [
      "Men applied mostly to the easy-to-enter department; women applied mostly to the selective one.",
      "The overall rate is a weighted average, and the weights differ wildly between groups.",
      "This mirrors the real 1973 UC Berkeley admissions case, where the confounding variable was department choice.",
    ],
    insight: "Always check for a confounding variable before trusting an aggregated statistic.",
  },
];

const BY_SLUG = new Map(PARADOXES.map((p) => [p.slug, p]));

export const paradoxSlugs = PARADOXES.map((p) => p.slug);

export function getParadox(slug: string): Paradox | undefined {
  return BY_SLUG.get(slug as ParadoxSlug);
}
