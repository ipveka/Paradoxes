"use client";

import { MotionConfig } from "framer-motion";

// `reducedMotion="user"` makes Framer Motion honor the OS-level
// "reduce motion" setting — transform-based animations are skipped for users
// who ask for less motion (better accessibility, gentler on mobile).
export function Providers({ children }: { children: React.ReactNode }) {
  return <MotionConfig reducedMotion="user">{children}</MotionConfig>;
}
