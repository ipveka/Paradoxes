"use client";

import {
  Area,
  AreaChart,
  ReferenceDot,
  ReferenceLine,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

export interface CurvePoint {
  x: number;
  y: number;
}

export function ProbabilityCurve({
  data,
  xLabel,
  marker,
}: {
  data: CurvePoint[];
  xLabel?: string;
  marker?: { x: number; y: number; label: string };
}) {
  return (
    <ResponsiveContainer width="100%" height={340}>
      <AreaChart data={data} margin={{ top: 16, right: 16, left: 0, bottom: 8 }}>
        <defs>
          <linearGradient id="curveFill" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor="#8b5cf6" stopOpacity={0.35} />
            <stop offset="100%" stopColor="#8b5cf6" stopOpacity={0.02} />
          </linearGradient>
        </defs>
        <XAxis
          dataKey="x"
          tickLine={false}
          axisLine={false}
          fontSize={12}
          label={
            xLabel
              ? { value: xLabel, position: "insideBottom", offset: -4, fontSize: 12, fill: "#94a3b8" }
              : undefined
          }
        />
        <YAxis
          domain={[0, 100]}
          tickLine={false}
          axisLine={false}
          fontSize={12}
          width={44}
          tickFormatter={(v) => `${v}%`}
        />
        <Tooltip
          formatter={(v: number) => [`${v.toFixed(1)}%`, "Probability"]}
          labelFormatter={(l) => `${xLabel ?? "x"}: ${l}`}
          contentStyle={{ borderRadius: 12, border: "1px solid #e2e8f0" }}
        />
        <ReferenceLine y={50} stroke="#f43f5e" strokeDasharray="4 4" />
        <Area
          type="monotone"
          dataKey="y"
          stroke="#7c3aed"
          strokeWidth={3}
          fill="url(#curveFill)"
          isAnimationActive
        />
        {marker ? (
          <ReferenceDot
            x={marker.x}
            y={marker.y}
            r={6}
            fill="#7c3aed"
            stroke="#fff"
            strokeWidth={2}
            label={{ value: marker.label, position: "top", fontSize: 11, fill: "#7c3aed" }}
          />
        ) : null}
      </AreaChart>
    </ResponsiveContainer>
  );
}
