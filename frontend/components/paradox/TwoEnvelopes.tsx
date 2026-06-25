"use client";

import { useState } from "react";
import { postJSON, type TwoEnvelopesResult } from "@/lib/api";
import { StatCard } from "@/components/StatCard";
import { BarComparison } from "@/components/charts/BarComparison";
import { ExperimentPanel, Slider, RunButton, ErrorNote } from "./controls";

export function TwoEnvelopes() {
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
    <ExperimentPanel title="🎲 Always stay vs always switch">
      <p className="mb-4 text-sm text-slate-500">
        If switching really paid off, an always-switch player would out-earn an
        always-stay player over many rounds. Run it and compare their averages.
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
            <StatCard label="Avg. if you stay" value={result.avg_stay.toFixed(2)} accent="text-rose-500" />
            <StatCard label="Avg. if you switch" value={result.avg_switch.toFixed(2)} accent="text-emerald-600" />
            <StatCard
              label="Switching edge"
              value={`${result.switch_advantage_pct >= 0 ? "+" : ""}${result.switch_advantage_pct.toFixed(2)}%`}
              sub="≈ 0 — it's a wash"
              accent="text-slate-500"
            />
          </div>
          <BarComparison
            domain={[0, domainMax]}
            unit=""
            data={[
              { name: "Stay", value: result.avg_stay, color: "#f43f5e" },
              { name: "Switch", value: result.avg_switch, color: "#10b981" },
            ]}
          />
        </div>
      )}
    </ExperimentPanel>
  );
}
