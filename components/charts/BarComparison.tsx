"use client";

import {
  Bar,
  BarChart,
  Cell,
  LabelList,
  ReferenceLine,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

export interface BarDatum {
  name: string;
  value: number;
  color: string;
}

export function BarComparison({
  data,
  domain = [0, 100],
  unit = "%",
  referenceY,
}: {
  data: BarDatum[];
  domain?: [number, number];
  unit?: string;
  referenceY?: number;
}) {
  return (
    <ResponsiveContainer width="100%" height={320}>
      <BarChart data={data} margin={{ top: 24, right: 16, left: 0, bottom: 8 }}>
        <XAxis dataKey="name" tickLine={false} axisLine={false} fontSize={13} />
        <YAxis
          domain={domain}
          tickLine={false}
          axisLine={false}
          fontSize={12}
          width={44}
          tickFormatter={(v) => `${v}${unit}`}
        />
        <Tooltip
          cursor={{ fill: "rgba(255,77,23,0.06)" }}
          formatter={(v: number) => [`${v.toFixed(2)}${unit}`, "Value"]}
          contentStyle={{ borderRadius: 12, border: "1px solid #e2e8f0" }}
        />
        {referenceY !== undefined ? (
          // The Y axis already labels this value (e.g. "50%"), so the dashed
          // line needs no extra label — which also avoids clipping on narrow
          // (mobile) charts.
          <ReferenceLine y={referenceY} stroke="#94a3b8" strokeDasharray="4 4" />
        ) : null}
        <Bar dataKey="value" radius={[10, 10, 0, 0]} isAnimationActive>
          {data.map((d) => (
            <Cell key={d.name} fill={d.color} />
          ))}
          <LabelList
            dataKey="value"
            position="top"
            formatter={(v: number) => `${v.toFixed(1)}${unit}`}
            fontSize={13}
            fill="#475569"
          />
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
}
