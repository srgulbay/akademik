"use client";

import { useEffect, useMemo, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";

type Cell = "X" | "O" | null;
type Player = "X" | "O";

const WINNING_LINES: ReadonlyArray<readonly [number, number, number]> = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6],
];

function calculateWinner(board: Cell[]): { winner: Player; line: readonly number[] } | null {
  for (const line of WINNING_LINES) {
    const [a, b, c] = line;
    if (board[a] && board[a] === board[b] && board[a] === board[c]) {
      return { winner: board[a] as Player, line };
    }
  }
  return null;
}

export default function GizliOyun() {
  const [names, setNames] = useState<{ X: string; O: string }>({ X: "Sen", O: "Eşim" });
  const [namesLocked, setNamesLocked] = useState(false);
  const [board, setBoard] = useState<Cell[]>(Array(9).fill(null));
  const [turn, setTurn] = useState<Player>("X");
  const [scores, setScores] = useState<{ X: number; O: number; draws: number }>({
    X: 0,
    O: 0,
    draws: 0,
  });
  const [startingPlayer, setStartingPlayer] = useState<Player>("X");

  const result = useMemo(() => calculateWinner(board), [board]);
  const isDraw = !result && board.every((cell) => cell !== null);
  const gameOver = !!result || isDraw;

  useEffect(() => {
    if (result) {
      setScores((prev) => ({ ...prev, [result.winner]: prev[result.winner] + 1 }));
    } else if (isDraw) {
      setScores((prev) => ({ ...prev, draws: prev.draws + 1 }));
    }
  }, [result, isDraw]);

  const handleCellClick = (index: number) => {
    if (gameOver || board[index]) return;
    const next = [...board];
    next[index] = turn;
    setBoard(next);
    setTurn(turn === "X" ? "O" : "X");
  };

  const nextRound = () => {
    const newStarter: Player = startingPlayer === "X" ? "O" : "X";
    setStartingPlayer(newStarter);
    setBoard(Array(9).fill(null));
    setTurn(newStarter);
  };

  const resetAll = () => {
    setBoard(Array(9).fill(null));
    setTurn("X");
    setStartingPlayer("X");
    setScores({ X: 0, O: 0, draws: 0 });
  };

  const statusText = result
    ? `🎉 ${names[result.winner]} kazandı!`
    : isDraw
      ? "🤝 Berabere — bir sonraki rauntta!"
      : `Sıra: ${names[turn]} (${turn})`;

  return (
    <main className="min-h-screen bg-gradient-to-br from-pink-50 via-rose-50 to-amber-50 dark:from-gray-900 dark:via-rose-950 dark:to-gray-900 text-gray-800 dark:text-gray-100 px-4 py-10 flex flex-col items-center">
      <motion.div
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="text-center mb-6"
      >
        <h1 className="text-4xl md:text-5xl font-extrabold text-rose-600 dark:text-rose-300">
          💞 İkimizin XOX&apos;u
        </h1>
        <p className="mt-2 text-sm md:text-base text-gray-600 dark:text-gray-400">
          Sırayla dokun, üç tane yan yana getiren kazanır.
        </p>
      </motion.div>

      {!namesLocked ? (
        <motion.form
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          onSubmit={(e) => {
            e.preventDefault();
            setNamesLocked(true);
          }}
          className="bg-white/70 dark:bg-gray-800/60 backdrop-blur rounded-2xl shadow-lg p-6 w-full max-w-md flex flex-col gap-4"
        >
          <label className="flex flex-col gap-1">
            <span className="text-sm font-medium">X oyuncusu</span>
            <input
              className="rounded-lg border border-rose-200 dark:border-rose-800 bg-white dark:bg-gray-900 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-rose-400"
              value={names.X}
              onChange={(e) => setNames((n) => ({ ...n, X: e.target.value.slice(0, 16) }))}
            />
          </label>
          <label className="flex flex-col gap-1">
            <span className="text-sm font-medium">O oyuncusu</span>
            <input
              className="rounded-lg border border-rose-200 dark:border-rose-800 bg-white dark:bg-gray-900 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-rose-400"
              value={names.O}
              onChange={(e) => setNames((n) => ({ ...n, O: e.target.value.slice(0, 16) }))}
            />
          </label>
          <button
            type="submit"
            className="mt-2 rounded-full bg-rose-500 hover:bg-rose-600 text-white font-semibold py-2 transition-colors"
          >
            Hadi başlayalım ✨
          </button>
        </motion.form>
      ) : (
        <>
          <div className="flex gap-3 md:gap-6 mb-6 w-full max-w-md justify-between">
            <ScoreCard label={names.X} sub="X" value={scores.X} active={turn === "X" && !gameOver} color="rose" />
            <ScoreCard label="Berabere" sub="—" value={scores.draws} active={false} color="gray" />
            <ScoreCard label={names.O} sub="O" value={scores.O} active={turn === "O" && !gameOver} color="amber" />
          </div>

          <AnimatePresence mode="wait">
            <motion.p
              key={statusText}
              initial={{ opacity: 0, y: 6 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -6 }}
              transition={{ duration: 0.25 }}
              className="text-lg md:text-xl font-semibold mb-4 text-center"
            >
              {statusText}
            </motion.p>
          </AnimatePresence>

          <div className="grid grid-cols-3 gap-2 md:gap-3 bg-white/60 dark:bg-gray-800/50 backdrop-blur p-3 md:p-4 rounded-2xl shadow-xl">
            {board.map((cell, i) => {
              const isWinning = result?.line.includes(i);
              const disabled = !!cell || gameOver;
              return (
                <button
                  key={i}
                  onClick={() => handleCellClick(i)}
                  disabled={disabled}
                  className={`w-20 h-20 md:w-24 md:h-24 rounded-xl flex items-center justify-center text-4xl md:text-5xl font-extrabold transition-colors
                    ${isWinning
                      ? "bg-rose-300 dark:bg-rose-700"
                      : "bg-white/90 dark:bg-gray-900/70 hover:bg-rose-100 dark:hover:bg-rose-900/40"}
                    ${disabled && !isWinning ? "cursor-not-allowed" : "cursor-pointer"}
                  `}
                  aria-label={`Hücre ${i + 1}`}
                >
                  <AnimatePresence>
                    {cell && (
                      <motion.span
                        key={cell + i}
                        initial={{ scale: 0, rotate: -90 }}
                        animate={{ scale: 1, rotate: 0 }}
                        transition={{ type: "spring", stiffness: 260, damping: 18 }}
                        className={cell === "X" ? "text-rose-500" : "text-amber-500"}
                      >
                        {cell}
                      </motion.span>
                    )}
                  </AnimatePresence>
                </button>
              );
            })}
          </div>

          <div className="flex flex-wrap gap-3 mt-6 justify-center">
            <button
              onClick={nextRound}
              disabled={!gameOver}
              className="px-5 py-2 rounded-full bg-rose-500 disabled:bg-rose-300 disabled:cursor-not-allowed hover:bg-rose-600 text-white font-medium shadow"
            >
              Sonraki raund
            </button>
            <button
              onClick={resetAll}
              className="px-5 py-2 rounded-full bg-white/80 dark:bg-gray-800 hover:bg-white dark:hover:bg-gray-700 text-rose-600 dark:text-rose-300 font-medium border border-rose-200 dark:border-rose-700 shadow"
            >
              Skoru sıfırla
            </button>
            <button
              onClick={() => setNamesLocked(false)}
              className="px-5 py-2 rounded-full bg-transparent hover:bg-white/60 dark:hover:bg-gray-800 text-gray-600 dark:text-gray-300 font-medium"
            >
              İsimleri değiştir
            </button>
          </div>

          <p className="mt-8 text-xs text-gray-500 dark:text-gray-500 text-center max-w-sm">
            İpucu: Her yeni raundda başlayan oyuncu değişir, böylece adil olur. 💕
          </p>
        </>
      )}
    </main>
  );
}

function ScoreCard({
  label,
  sub,
  value,
  active,
  color,
}: {
  label: string;
  sub: string;
  value: number;
  active: boolean;
  color: "rose" | "amber" | "gray";
}) {
  const colorMap = {
    rose: "from-rose-200 to-rose-100 dark:from-rose-800 dark:to-rose-900 text-rose-700 dark:text-rose-200",
    amber: "from-amber-200 to-amber-100 dark:from-amber-800 dark:to-amber-900 text-amber-700 dark:text-amber-200",
    gray: "from-gray-200 to-gray-100 dark:from-gray-700 dark:to-gray-800 text-gray-700 dark:text-gray-200",
  } as const;
  return (
    <motion.div
      animate={{ scale: active ? 1.05 : 1 }}
      transition={{ type: "spring", stiffness: 300, damping: 20 }}
      className={`flex-1 rounded-2xl p-3 md:p-4 bg-gradient-to-br ${colorMap[color]} shadow ${active ? "ring-2 ring-rose-400 dark:ring-rose-500" : ""}`}
    >
      <div className="text-xs md:text-sm uppercase tracking-wide opacity-80 truncate">{label}</div>
      <div className="text-2xl md:text-3xl font-extrabold leading-tight">{value}</div>
      <div className="text-xs opacity-70">{sub}</div>
    </motion.div>
  );
}
