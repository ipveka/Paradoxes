"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { postJSON, type SleepingBeautyResult } from "@/lib/api";
import { StatCard } from "@/components/StatCard";
import { BarComparison } from "@/components/charts/BarComparison";
import { ExperimentPanel, Slider, RunButton, ErrorNote } from "./controls";

type Run = { coin: "heads" | "tails"; awakenings: number };

function Step({ label, children, accent }: { label: string; children: React.ReactNode; accent?: boolean }) {
  return (
    <div
      className={`flex flex-col items-center justify-center rounded-lg border-2 px-3 py-3 ${
        accent ? "border-accent bg-brand-50" : "border-slate-200 bg-white"
      }`}
    >
      <span className="text-2xl">{children}</span>
      <span className="mt-1 text-[10px] font-bold uppercase tracking-wide text-slate-400">{label}</span>
    </div>
  );
}

export function SleepingBeauty() {
  // --- Single experiment ---
  const [run, setRun] = useState<Run | null>(null);
  const [tally, setTally] = useState({ experiments: 0, awakenings: 0, headsAwakenings: 0 });

  function runOnce() {
    const coin = Math.random() < 0.5 ? "heads" : "tails";
    const awakenings = coin === "heads" ? 1 : 2;
    setRun({ coin, awakenings });
    setTally((t) => ({
      experiments: t.experiments + 1,
      awakenings: t.awakenings + awakenings,
      headsAwakenings: t.headsAwakenings + (coin === "heads" ? 1 : 0),
    }));
  }

  const runningP = tally.awakenings ? tally.headsAwakenings / tally.awakenings : 0;

  // --- Batch simulation ---
  const [trials, setTrials] = useState(2000);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<SleepingBeautyResult | null>(null);

  async function runSimulation() {
    setLoading(true);
    setError(null);
    try {
      setResult(await postJSON<SleepingBeautyResult>("/api/sleeping-beauty/simulate", { trials }));
    } catch (e) {
      setError(e instanceof Error ? e.message : "Request failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-8">
      <ExperimentPanel title="🪙 Run one experiment">
        <p className="mb-5 text-sm text-slate-500">
          Flip the coin. Heads wakes Beauty once; Tails wakes her twice. Keep going and
          watch how often an awakening happens in a Heads world.
        </p>

        <div className="flex flex-wrap items-stretch gap-2">
          <Step label="Sunday">😴</Step>
          <span className="self-center text-slate-300">→</span>
          <Step label="Coin" accent>
            {run ? (run.coin === "heads" ? "🪙" : "🪙") : "❔"}
          </Step>
          <span className="self-center text-slate-300">→</span>
          <Step label="Monday" accent={!!run}>
            {run ? "👁️" : "❔"}
          </Step>
          {run?.coin === "tails" && (
            <>
              <span className="self-center text-slate-300">→</span>
              <motion.div initial={{ opacity: 0, x: -8 }} animate={{ opacity: 1, x: 0 }}>
                <Step label="Tuesday" accent>
                  👁️
                </Step>
              </motion.div>
            </>
          )}
          <div className="ml-auto flex items-center">
            {run && (
              <span className="text-sm font-semibold">
                {run.coin === "heads" ? "Heads → 1 awakening" : "Tails → 2 awakenings"}
              </span>
            )}
          </div>
        </div>

        <div className="mt-5">
          <RunButton onClick={runOnce} loading={false}>
            🪙 Flip &amp; run one experiment
          </RunButton>
        </div>

        {tally.experiments > 0 && (
          <div className="mt-6 grid grid-cols-1 gap-3 sm:grid-cols-3">
            <StatCard label="Experiments" value={String(tally.experiments)} accent="text-slate-400" />
            <StatCard label="Total awakenings" value={String(tally.awakenings)} accent="text-ink" />
            <StatCard
              label="P(Heads | awake) so far"
              value={`${(runningP * 100).toFixed(1)}%`}
              sub="heading toward 33%"
              accent="text-accent"
            />
          </div>
        )}
      </ExperimentPanel>

      <ExperimentPanel title="📊 Let the server run thousands">
        <Slider label="Number of coin tosses" value={trials} onChange={setTrials} min={100} max={200000} step={100} />
        <div className="mt-5">
          <RunButton onClick={runSimulation} loading={loading} />
        </div>
        <div className="mt-4">
          <ErrorNote message={error} />
        </div>

        {result && (
          <div className="mt-6 space-y-6">
            <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
              <StatCard
                label="P(Heads | awake)"
                value={`${(result.p_heads_given_awake * 100).toFixed(1)}%`}
                sub="≈ 33% (thirder)"
                accent="text-accent"
              />
              <StatCard label="Total awakenings" value={result.total_awakenings.toLocaleString()} accent="text-ink" />
              <StatCard
                label="Heads / Tails tosses"
                value={`${result.heads_count} / ${result.tails_count}`}
                accent="text-slate-400"
              />
            </div>
            <BarComparison
              domain={[0, 60]}
              data={[
                { name: "Halfer (1/2)", value: result.halfer_position * 100, color: "#cbd5e1" },
                { name: "Thirder (1/3)", value: result.thirder_position * 100, color: "#ff4d17" },
                { name: "Simulation", value: result.p_heads_given_awake * 100, color: "#0f0f0f" },
              ]}
            />
          </div>
        )}
      </ExperimentPanel>
    </div>
  );
}
