"use client";

import { useEffect, useState } from "react";
import {
  Bar,
  BarChart,
  CartesianGrid,
  Legend,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { getJSON, type SimpsonsData } from "@/lib/api";
import { ExperimentPanel, ErrorNote } from "./controls";

export function Simpsons() {
  const [data, setData] = useState<SimpsonsData | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getJSON<SimpsonsData>("/api/simpsons/data")
      .then(setData)
      .catch((e) => setError(e instanceof Error ? e.message : "Request failed"));
  }, []);

  const chartData =
    data &&
    [
      ...data.departments.map((d) => ({
        name: d.name,
        Men: Number(d.male_rate.toFixed(1)),
        Women: Number(d.female_rate.toFixed(1)),
      })),
      {
        name: "Overall",
        Men: Number(data.overall.male_rate.toFixed(1)),
        Women: Number(data.overall.female_rate.toFixed(1)),
      },
    ];

  return (
    <ExperimentPanel title="📊 Acceptance rates by department">
      <p className="mb-4 text-sm text-slate-500">
        Watch the bars: women lead in <strong>both</strong> departments, yet the
        rightmost &ldquo;Overall&rdquo; group flips — men come out ahead once the
        data is pooled.
      </p>

      <ErrorNote message={error} />

      {chartData ? (
        <>
          <ResponsiveContainer width="100%" height={360}>
            <BarChart data={chartData} margin={{ top: 16, right: 16, left: 0, bottom: 8 }}>
              <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#eef2f7" />
              <XAxis dataKey="name" tickLine={false} axisLine={false} fontSize={13} />
              <YAxis
                domain={[0, 100]}
                tickLine={false}
                axisLine={false}
                fontSize={12}
                width={44}
                tickFormatter={(v) => `${v}%`}
              />
              <Tooltip
                formatter={(v: number) => [`${v}%`, ""]}
                contentStyle={{ borderRadius: 12, border: "1px solid #e2e8f0" }}
              />
              <Legend />
              <Bar dataKey="Men" fill="#0f0f0f" radius={[8, 8, 0, 0]} />
              <Bar dataKey="Women" fill="#ff4d17" radius={[8, 8, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>

          {data?.paradox && (
            <div className="mt-4 border-l-4 border-accent bg-brand-50 p-4 text-sm">
              🤯 <strong>Paradox confirmed:</strong> women are admitted at a higher rate
              in every department, but men have the higher overall rate — because women
              applied mostly to the more selective department.
            </div>
          )}
        </>
      ) : (
        !error && <div className="h-[360px] animate-pulse rounded-xl bg-slate-100" />
      )}
    </ExperimentPanel>
  );
}
