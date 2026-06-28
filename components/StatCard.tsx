export function StatCard({
  label,
  value,
  sub,
  accent = "text-brand-600",
}: {
  label: string;
  value: string;
  sub?: string;
  accent?: string;
}) {
  return (
    <div className="card flex flex-col gap-1 p-5">
      <span className="text-xs font-medium uppercase tracking-wide text-slate-400">
        {label}
      </span>
      <span className={`text-3xl font-extrabold tabular-nums ${accent}`}>{value}</span>
      {sub ? <span className="text-sm text-slate-500">{sub}</span> : null}
    </div>
  );
}
