"use client";

import { useState } from "react";
import { postJSON, type SleepingBeautyResult } from "@/lib/api";
import { StatCard } from "@/components/StatCard";
import { BarComparison } from "@/components/charts/BarComparison";
import { ExperimentPanel, Slider, RunButton, ErrorNote } from "./controls";

export function SleepingBeauty() {
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
    <ExperimentPanel title="💤 Count the awakenings">
      <p className="mb-4 text-sm text-slate-500">
        Each run tosses a fair coin. Heads wakes Beauty once; Tails wakes her twice.
        Among all awakenings, how often was the coin actually Heads?
      </p>
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
              accent="text-emerald-600"
            />
            <StatCard label="Total awakenings" value={result.total_awakenings.toLocaleString()} accent="text-violet-600" />
            <StatCard label="Heads / Tails tosses" value={`${result.heads_count} / ${result.tails_count}`} accent="text-slate-500" />
          </div>
          <BarComparison
            domain={[0, 60]}
            data={[
              { name: "Halfer (1/2)", value: result.halfer_position * 100, color: "#f43f5e" },
              { name: "Thirder (1/3)", value: result.thirder_position * 100, color: "#10b981" },
              { name: "Simulation", value: result.p_heads_given_awake * 100, color: "#6366f1" },
            ]}
          />
        </div>
      )}
    </ExperimentPanel>
  );
}
