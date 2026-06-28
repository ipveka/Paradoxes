"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { postJSON, type TwoEnvelopesResult } from "@/lib/api";
import { StatCard } from "@/components/StatCard";
import { BarComparison } from "@/components/charts/BarComparison";
import { ExperimentPanel, Slider, RunButton, ErrorNote } from "./controls";

const BASES = [5, 10, 20, 50, 100];

type Phase = "pick" | "picked" | "revealed";

export function TwoEnvelopes() {
  // --- Interactive single round ---
  const [phase, setPhase] = useState<Phase>("pick");
  const [picked, setPicked] = useState<"A" | "B" | null>(null);
  const [amounts, setAmounts] = useState<{ A: number; B: number }>({ A: 0, B: 0 });
  const [tally, setTally] = useState({ rounds: 0, helped: 0, net: 0 });

  function pick(env: "A" | "B") {
    if (phase !== "pick") return;
    const base = BASES[Math.floor(Math.random() * BASES.length)];
    const big = Math.random() < 0.5;
    setAmounts({ A: big ? base * 2 : base, B: big ? base : base * 2 });
    setPicked(env);
    setPhase("picked");
  }

  function reveal() {
    if (phase !== "picked" || !picked) return;
    const other = picked === "A" ? "B" : "A";
    const delta = amounts[other] - amounts[picked];
    setTally((t) => ({
      rounds: t.rounds + 1,
      helped: t.helped + (delta > 0 ? 1 : 0),
      net: t.net + delta,
    }));
    setPhase("revealed");
  }

  function reset() {
    setPhase("pick");
    setPicked(null);
  }

  const other = picked === "A" ? "B" : "A";
  const delta = picked ? amounts[other] - amounts[picked] : 0;

  // --- Batch simulation ---
  const [trials, setTrials] = useState(5000);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<TwoEnvelopesResult | null>(null);

  async function runSimulation() {
    setLoading(true);
    setError(null);
    try {
      setResult(await postJSON<TwoEnvelopesResult>("/api/two-envelopes/simulate", { trials }));
    } catch (e) {
      setError(e instanceof Error ? e.message : "Request failed");
    } finally {
      setLoading(false);
    }
  }

  const max = result ? Math.max(result.avg_stay, result.avg_switch) : 1;
  const domainMax = Math.ceil((max * 1.2) / 10) * 10;

  return (
    <div className="space-y-8">
      <ExperimentPanel title="🎲 Play a round">
        <p className="mb-5 text-sm text-slate-500">
          Pick an envelope. You&apos;ll see what&apos;s inside — then find out whether
          switching would have helped.
        </p>

        <div className="grid grid-cols-2 gap-4">
          {(["A", "B"] as const).map((env) => {
            const isPicked = picked === env;
            const show = (isPicked && phase !== "pick") || phase === "revealed";
            return (
              <motion.button
                key={env}
                whileHover={phase === "pick" ? { y: -6 } : undefined}
                onClick={() => pick(env)}
                disabled={phase !== "pick"}
                className={`flex aspect-[4/3] flex-col items-center justify-center rounded-lg border-2 transition-colors ${
                  isPicked ? "border-accent bg-brand-50" : "border-slate-200 bg-white"
                } ${phase === "pick" ? "cursor-pointer hover:border-brand-300" : "cursor-default"}`}
              >
                <span className="text-5xl">✉️</span>
                <span className="mt-2 text-xs font-bold uppercase tracking-wide text-slate-400">
                  Envelope {env}
                  {isPicked ? " · yours" : ""}
                </span>
                {show ? (
                  <span className="mt-1 text-2xl font-extrabold tabular-nums">${amounts[env]}</span>
                ) : null}
              </motion.button>
            );
          })}
        </div>

        <div className="mt-5 min-h-[3rem]">
          {phase === "pick" && <p className="text-center text-slate-500">Pick an envelope to begin.</p>}
          {phase === "picked" && (
            <div className="flex flex-col items-center gap-3">
              <p className="text-center text-slate-600">
                You have <strong>${amounts[picked!]}</strong>. Curious what you passed up?
              </p>
              <button onClick={reveal} className="btn-primary">
                Reveal the other envelope
              </button>
            </div>
          )}
          {phase === "revealed" && (
            <div className="flex flex-col items-center gap-3">
              <p className={`text-center font-semibold ${delta > 0 ? "text-accent" : "text-slate-600"}`}>
                {delta > 0
                  ? `Switching would have gained you $${delta}.`
                  : `Good call — switching would have lost you $${-delta}.`}
              </p>
              <button onClick={reset} className="btn-ghost">
                Play again
              </button>
            </div>
          )}
        </div>

        {tally.rounds > 0 && (
          <div className="mt-5 border-t border-slate-200 pt-4 text-center text-sm text-slate-500">
            Over <strong>{tally.rounds}</strong> rounds, switching would have helped{" "}
            <strong>{tally.helped}</strong> time{tally.helped === 1 ? "" : "s"} — net change from
            always switching:{" "}
            <strong className={tally.net === 0 ? "" : "text-ink"}>
              {tally.net >= 0 ? "+" : ""}${tally.net}
            </strong>
            . It bounces around zero.
          </div>
        )}
      </ExperimentPanel>

      <ExperimentPanel title="📊 Always stay vs always switch">
        <p className="mb-4 text-sm text-slate-500">
          One round is luck. Let the server play thousands and compare an always-stay
          player with an always-switch player drawing from the same envelope pairs.
        </p>
        <Slider label="Number of rounds" value={trials} onChange={setTrials} min={500} max={200000} step={500} />
        <div className="mt-5">
          <RunButton onClick={runSimulation} loading={loading} />
        </div>
        <div className="mt-4">
          <ErrorNote message={error} />
        </div>

        {result && (
          <div className="mt-6 space-y-6">
            <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
              <StatCard label="Avg. if you stay" value={result.avg_stay.toFixed(2)} accent="text-slate-400" />
              <StatCard label="Avg. if you switch" value={result.avg_switch.toFixed(2)} accent="text-ink" />
              <StatCard
                label="Switching edge"
                value={`${result.switch_advantage_pct >= 0 ? "+" : ""}${result.switch_advantage_pct.toFixed(2)}%`}
                sub="≈ 0 — it's a wash"
                accent="text-accent"
              />
            </div>
            <BarComparison
              domain={[0, domainMax]}
              unit=""
              data={[
                { name: "Stay", value: result.avg_stay, color: "#cbd5e1" },
                { name: "Switch", value: result.avg_switch, color: "#0f0f0f" },
              ]}
            />
          </div>
        )}
      </ExperimentPanel>
    </div>
  );
}
