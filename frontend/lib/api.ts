// Thin client for the FastAPI backend. The base URL is baked at build time from
// NEXT_PUBLIC_API_URL (see .env.example):
//   - unset            → local dev default (http://localhost:8000)
//   - "/" or ""        → same-origin relative calls (the all-in-one Vercel deploy)
//   - an absolute URL  → that backend (e.g. a separate Render service)
const configured = process.env.NEXT_PUBLIC_API_URL;
const API_BASE = (configured ?? "http://localhost:8000").replace(/\/$/, "");

async function handle<T>(res: Response): Promise<T> {
  if (!res.ok) {
    throw new Error(`API ${res.status}: ${res.statusText}`);
  }
  return res.json() as Promise<T>;
}

export async function getJSON<T>(path: string): Promise<T> {
  return handle<T>(await fetch(`${API_BASE}${path}`, { cache: "no-store" }));
}

export async function postJSON<T>(path: string, body: unknown): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
    cache: "no-store",
  });
  return handle<T>(res);
}

// --- Response types (mirror backend/app/schemas.py) ----------------------

export interface MontyHallResult {
  games: number;
  stay_wins: number;
  switch_wins: number;
  stay_rate: number;
  switch_rate: number;
  theoretical_stay_rate: number;
  theoretical_switch_rate: number;
}

export interface BirthdayResult {
  group_size: number;
  trials: number;
  matches: number;
  simulated_probability: number;
  theoretical_probability: number;
  difference: number;
}

export interface BirthdayCurve {
  max_size: number;
  points: { group_size: number; probability: number }[];
}

export interface TwoEnvelopesResult {
  trials: number;
  avg_stay: number;
  avg_switch: number;
  switch_advantage: number;
  switch_advantage_pct: number;
}

export interface SleepingBeautyResult {
  trials: number;
  heads_count: number;
  tails_count: number;
  total_awakenings: number;
  p_heads_given_awake: number;
  p_tails_given_awake: number;
  halfer_position: number;
  thirder_position: number;
}

export interface SimpsonsDepartment {
  name: string;
  male_applied: number;
  male_admitted: number;
  male_rate: number;
  female_applied: number;
  female_admitted: number;
  female_rate: number;
}

export interface SimpsonsData {
  departments: SimpsonsDepartment[];
  overall: {
    male_applied: number;
    male_admitted: number;
    male_rate: number;
    female_applied: number;
    female_admitted: number;
    female_rate: number;
  };
  paradox: boolean;
}
