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
import { ExperimentPanel, Slider, ErrorNote } from "./controls";

interface GroupRow {
  name: string;
  Men: number;
  Women: number;
}

function GroupedBars({ data }: { data: GroupRow[] }) {
  return (
    <ResponsiveContainer width="100%" height={340}>
      <BarChart data={data} margin={{ top: 16, right: 16, left: 0, bottom: 8 }}>
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
          formatter={(v: number) => [`${v.toFixed(1)}%`, ""]}
          contentStyle={{ borderRadius: 8, border: "1px solid #e2e8f0" }}
        />
        <Legend />
        <Bar dataKey="Men" fill="#0f0f0f" radius={[6, 6, 0, 0]} isAnimationActive={false} />
        <Bar dataKey="Women" fill="#ff4d17" radius={[6, 6, 0, 0]} isAnimationActive={false} />
      </BarChart>
    </ResponsiveContainer>
  );
}

// Fixed within-department acceptance rates (women edge out men in BOTH).
const RATE = { A: { m: 80, w: 85 }, B: { m: 30, w: 35 } };

export function Simpsons() {
  // --- Interactive tipping point ---
  const [menToA, setMenToA] = useState(80); // % of men applying to the easy dept
  const [womenToA, setWomenToA] = useState(20);

  const maleOverall = (menToA / 100) * RATE.A.m + (1 - menToA / 100) * RATE.B.m;
  const femaleOverall = (womenToA / 100) * RATE.A.w + (1 - womenToA / 100) * RATE.B.w;
  const paradoxOn = maleOverall > femaleOverall; // women win both depts by construction

  const interactiveData: GroupRow[] = [
    { name: "Dept A (easy)", Men: RATE.A.m, Women: RATE.A.w },
    { name: "Dept B (hard)", Men: RATE.B.m, Women: RATE.B.w },
    { name: "Overall", Men: maleOverall, Women: femaleOverall },
  ];

  // --- Canonical dataset from the API ---
  const [data, setData] = useState<SimpsonsData | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getJSON<SimpsonsData>("/api/simpsons/data")
      .then(setData)
      .catch((e) => setError(e instanceof Error ? e.message : "Request failed"));
  }, []);

  const canonical: GroupRow[] | null =
    data &&
    [
      ...data.departments.map((d) => ({ name: d.name, Men: d.male_rate, Women: d.female_rate })),
      { name: "Overall", Men: data.overall.male_rate, Women: data.overall.female_rate },
    ];

  return (
    <div className="space-y-8">
      <ExperimentPanel title="🎚️ Find the tipping point">
        <p className="mb-5 text-sm text-slate-500">
          Women are admitted at a higher rate in <strong>both</strong> departments. But
          where people apply decides the overall result. Drag the sliders and watch the
          &ldquo;Overall&rdquo; bars flip.
        </p>
        <div className="space-y-5">
          <Slider label="% of men applying to the easy dept" value={menToA} onChange={setMenToA} min={0} max={100} />
          <Slider label="% of women applying to the easy dept" value={womenToA} onChange={setWomenToA} min={0} max={100} />
        </div>

        <div className="mt-6">
          <GroupedBars data={interactiveData} />
        </div>

        <div
          className={`mt-4 border-l-4 p-4 text-sm ${
            paradoxOn ? "border-accent bg-brand-50" : "border-slate-300 bg-slate-50"
          }`}
        >
          {paradoxOn ? (
            <>
              🤯 <strong>Paradox ON:</strong> women lead in both departments
              ({maleOverall.toFixed(1)}% vs {femaleOverall.toFixed(1)}% overall for men) — yet men
              win overall, because they cluster in the easy department.
            </>
          ) : (
            <>
              ✅ <strong>Paradox OFF:</strong> with this split the overall rates agree with the
              departments (women {femaleOverall.toFixed(1)}% vs men {maleOverall.toFixed(1)}%).
              Push more men toward the easy department to bring it back.
            </>
          )}
        </div>
      </ExperimentPanel>

      <ExperimentPanel title="🏛️ The real case: UC Berkeley, 1973">
        <p className="mb-4 text-sm text-slate-500">
          The classic dataset that made this famous, served from the API.
        </p>
        <ErrorNote message={error} />
        {canonical ? (
          <GroupedBars data={canonical} />
        ) : (
          !error && <div className="h-[340px] animate-pulse rounded-lg bg-slate-100" />
        )}
      </ExperimentPanel>
    </div>
  );
}
