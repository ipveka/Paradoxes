"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { postJSON, type MontyHallResult } from "@/lib/api";
import { StatCard } from "@/components/StatCard";
import { BarComparison } from "@/components/charts/BarComparison";
import { ExperimentPanel, Slider, RunButton, ErrorNote } from "./controls";

type Phase = "pick" | "decide" | "done";

function randomCar() {
  return Math.floor(Math.random() * 3);
}

export function MontyHall() {
  // --- Interactive single game ---
  const [car, setCar] = useState(randomCar);
  const [picked, setPicked] = useState<number | null>(null);
  const [opened, setOpened] = useState<number | null>(null);
  const [phase, setPhase] = useState<Phase>("pick");
  const [won, setWon] = useState(false);
  const [switched, setSwitched] = useState(false);
  const [score, setScore] = useState({ stayWins: 0, stayPlays: 0, switchWins: 0, switchPlays: 0 });

  function pick(door: number) {
    if (phase !== "pick") return;
    // Host opens a goat door that isn't the player's pick.
    const options = [0, 1, 2].filter((d) => d !== door && d !== car);
    const hostDoor = options[Math.floor(Math.random() * options.length)];
    setPicked(door);
    setOpened(hostDoor);
    setPhase("decide");
  }

  function decide(doSwitch: boolean) {
    if (phase !== "decide" || picked === null || opened === null) return;
    const finalDoor = doSwitch ? [0, 1, 2].find((d) => d !== picked && d !== opened)! : picked;
    const didWin = finalDoor === car;
    setSwitched(doSwitch);
    setWon(didWin);
    setPhase("done");
    setScore((s) => ({
      stayWins: s.stayWins + (!doSwitch && didWin ? 1 : 0),
      stayPlays: s.stayPlays + (!doSwitch ? 1 : 0),
      switchWins: s.switchWins + (doSwitch && didWin ? 1 : 0),
      switchPlays: s.switchPlays + (doSwitch ? 1 : 0),
    }));
  }

  function reset() {
    setCar(randomCar());
    setPicked(null);
    setOpened(null);
    setPhase("pick");
    setWon(false);
  }

  // --- Batch simulation ---
  const [games, setGames] = useState(2000);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<MontyHallResult | null>(null);

  async function runSimulation() {
    setLoading(true);
    setError(null);
    try {
      setResult(await postJSON<MontyHallResult>("/api/monty-hall/simulate", { games }));
    } catch (e) {
      setError(e instanceof Error ? e.message : "Request failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-8">
      <ExperimentPanel title="🎮 Play a round">
        <div className="grid grid-cols-3 gap-3 sm:gap-5">
          {[0, 1, 2].map((door) => {
            const isPick = picked === door;
            const isOpened = opened === door;
            const revealAll = phase === "done";
            const show = isOpened || revealAll;
            return (
              <motion.button
                key={door}
                whileHover={phase === "pick" ? { y: -6 } : undefined}
                onClick={() => pick(door)}
                disabled={phase !== "pick"}
                className={`flex aspect-[3/4] flex-col items-center justify-center rounded-2xl border-2 text-6xl transition-colors sm:text-7xl ${
                  isPick
                    ? "border-brand-500 bg-brand-50"
                    : "border-slate-200 bg-white hover:border-brand-300"
                } ${phase === "pick" ? "cursor-pointer" : "cursor-default"}`}
              >
                <span>{show ? (door === car ? "🚗" : "🐐") : "🚪"}</span>
                <span className="mt-2 text-xs font-semibold text-slate-400">
                  Door {door + 1}
                  {isPick ? " · yours" : ""}
                </span>
              </motion.button>
            );
          })}
        </div>

        <div className="mt-5 min-h-[3rem]">
          {phase === "pick" && (
            <p className="text-center text-slate-500">Pick a door to begin.</p>
          )}
          {phase === "decide" && (
            <div className="flex flex-col items-center gap-3">
              <p className="text-center text-slate-600">
                The host opened a goat door. Stay or switch?
              </p>
              <div className="flex gap-3">
                <button onClick={() => decide(false)} className="btn-ghost">
                  Stay
                </button>
                <button onClick={() => decide(true)} className="btn-primary">
                  Switch
                </button>
              </div>
            </div>
          )}
          {phase === "done" && (
            <div className="flex flex-col items-center gap-3">
              <p className={`text-center font-semibold ${won ? "text-emerald-600" : "text-rose-600"}`}>
                {won ? "🎉 You won the car!" : "🐐 A goat. Bad luck!"} You chose to{" "}
                {switched ? "switch" : "stay"}.
              </p>
              <button onClick={reset} className="btn-ghost">
                Play again
              </button>
            </div>
          )}
        </div>

        {score.stayPlays + score.switchPlays > 0 && (
          <div className="mt-5 grid grid-cols-2 gap-3 text-center text-sm">
            <div className="rounded-xl bg-slate-50 p-3">
              <div className="font-semibold text-slate-700">Stayed</div>
              <div className="text-slate-500">
                won {score.stayWins}/{score.stayPlays}
              </div>
            </div>
            <div className="rounded-xl bg-slate-50 p-3">
              <div className="font-semibold text-slate-700">Switched</div>
              <div className="text-slate-500">
                won {score.switchWins}/{score.switchPlays}
              </div>
            </div>
          </div>
        )}
      </ExperimentPanel>

      <ExperimentPanel title="📊 Simulate thousands of games">
        <p className="mb-4 text-sm text-slate-500">
          Hand-playing is slow. Let the server play both strategies across many games
          and compare the win rates.
        </p>
        <Slider label="Number of games" value={games} onChange={setGames} min={100} max={100000} step={100} />
        <div className="mt-5">
          <RunButton onClick={runSimulation} loading={loading} />
        </div>
        <div className="mt-4">
          <ErrorNote message={error} />
        </div>

        {result && (
          <div className="mt-6 space-y-6">
            <div className="grid grid-cols-2 gap-3">
              <StatCard
                label="Stay win rate"
                value={`${(result.stay_rate * 100).toFixed(1)}%`}
                sub="≈ 33% (theory)"
                accent="text-rose-500"
              />
              <StatCard
                label="Switch win rate"
                value={`${(result.switch_rate * 100).toFixed(1)}%`}
                sub="≈ 67% (theory)"
                accent="text-emerald-600"
              />
            </div>
            <BarComparison
              referenceY={50}
              referenceLabel="50%"
              data={[
                { name: "Stay", value: result.stay_rate * 100, color: "#f43f5e" },
                { name: "Switch", value: result.switch_rate * 100, color: "#10b981" },
              ]}
            />
          </div>
        )}
      </ExperimentPanel>
    </div>
  );
}
