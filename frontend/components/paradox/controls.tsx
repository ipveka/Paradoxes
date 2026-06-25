"use client";

export function ExperimentPanel({
  title,
  children,
}: {
  title: string;
  children: React.ReactNode;
}) {
  return (
    <div className="card p-6 sm:p-8">
      <h2 className="mb-5 text-sm font-semibold uppercase tracking-wide text-slate-400">
        {title}
      </h2>
      {children}
    </div>
  );
}

export function Slider({
  label,
  value,
  onChange,
  min,
  max,
  step = 1,
}: {
  label: string;
  value: number;
  onChange: (v: number) => void;
  min: number;
  max: number;
  step?: number;
}) {
  return (
    <label className="block">
      <div className="mb-1 flex items-center justify-between text-sm">
        <span className="font-medium text-slate-600">{label}</span>
        <span className="font-bold tabular-nums text-brand-600">{value.toLocaleString()}</span>
      </div>
      <input
        type="range"
        min={min}
        max={max}
        step={step}
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
        className="h-2 w-full cursor-pointer appearance-none rounded-full bg-slate-200 accent-brand-600"
      />
    </label>
  );
}

export function RunButton({
  onClick,
  loading,
  children = "🚀 Run simulation",
}: {
  onClick: () => void;
  loading: boolean;
  children?: React.ReactNode;
}) {
  return (
    <button onClick={onClick} disabled={loading} className="btn-primary w-full">
      {loading ? "Simulating…" : children}
    </button>
  );
}

export function ErrorNote({ message }: { message: string | null }) {
  if (!message) return null;
  return (
    <div className="rounded-xl border border-rose-200 bg-rose-50 p-4 text-sm text-rose-700">
      ⚠️ {message}. Is the API running? Check{" "}
      <code className="font-mono">NEXT_PUBLIC_API_URL</code>.
    </div>
  );
}
