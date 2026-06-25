"use client";

import { useEffect, useState } from "react";
import { getJSON, postJSON, type BirthdayCurve, type BirthdayResult } from "@/lib/api";
import { StatCard } from "@/components/StatCard";
import { ProbabilityCurve, type CurvePoint } from "@/components/charts/ProbabilityCurve";
import { ExperimentPanel, Slider, RunButton, ErrorNote } from "./controls";

export function Birthday() {
  const [groupSize, setGroupSize] = useState(23);
  const [trials, setTrials] = useState(2000);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<BirthdayResult | null>(null);
  const [curve, setCurve] = useState<CurvePoint[]>([]);

  // Fetch the exact theoretical curve once.
  useEffect(() => {
    getJSON<BirthdayCurve>("/api/birthday/curve?max_size=100")
      .then((c) => setCurve(c.points.map((p) => ({ x: p.group_size, y: p.probability * 100 }))))
      .catch(() => setError("Could not load the probability curve"));
  }, []);

  const markerY = curve.find((p) => p.x === groupSize)?.y;

  async function runSimulation() {
    setLoading(true);
    setError(null);
    try {
      setResult(
        await postJSON<BirthdayResult>("/api/birthday/simulate", {
          group_size: groupSize,
          trials,
        }),
      );
    } catch (e) {
      setError(e instanceof Error ? e.message : "Request failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-8">
      <ExperimentPanel title="📈 The probability curve">
        <p className="mb-4 text-sm text-slate-500">
          Exact probability of at least one shared birthday as the group grows. The
          dashed line marks 50% — drag the slider and watch where {groupSize} people land.
        </p>
        {curve.length > 0 ? (
          <ProbabilityCurve
            data={curve}
            xLabel="People in group"
            marker={markerY !== undefined ? { x: groupSize, y: markerY, label: `${markerY.toFixed(0)}%` } : undefined}
          />
        ) : (
          <div className="h-[340px] animate-pulse rounded-xl bg-slate-100" />
        )}
      </ExperimentPanel>

      <ExperimentPanel title="🧪 Run the experiment">
        <div className="space-y-5">
          <Slider label="People in the group" value={groupSize} onChange={setGroupSize} min={2} max={100} />
          <Slider label="Number of random groups" value={trials} onChange={setTrials} min={100} max={50000} step={100} />
        </div>
        <div className="mt-5">
          <RunButton onClick={runSimulation} loading={loading} />
        </div>
        <div className="mt-4">
          <ErrorNote message={error} />
        </div>

        {result && (
          <div className="mt-6 grid grid-cols-1 gap-3 sm:grid-cols-3">
            <StatCard
              label="Simulated"
              value={`${(result.simulated_probability * 100).toFixed(1)}%`}
              sub={`${result.matches} of ${result.trials} groups`}
            />
            <StatCard
              label="Theoretical"
              value={`${(result.theoretical_probability * 100).toFixed(1)}%`}
              accent="text-violet-600"
            />
            <StatCard
              label="Difference"
              value={`${(result.difference * 100).toFixed(2)}%`}
              accent="text-slate-500"
            />
          </div>
        )}
      </ExperimentPanel>
    </div>
  );
}
