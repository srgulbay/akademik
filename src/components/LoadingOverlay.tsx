"use client";
import { useEffect, useState } from "react";

export default function LoadingOverlay() {
  const [progress, setProgress] = useState(0);
  const [visible, setVisible] = useState(true);

  useEffect(() => {
    let current = 0;
    const interval = setInterval(() => {
      current += Math.random() * 15;
      if (current >= 100) {
        current = 100;
        clearInterval(interval);
        setTimeout(() => setVisible(false), 500); // Yükleme bitince kaybolur
      }
      setProgress(Math.floor(current));
    }, 250);
    return () => clearInterval(interval);
  }, []);

  if (!visible) return null;

  return (
    <div className="fixed inset-0 z-50 flex flex-col items-center justify-center bg-gray-100 dark:bg-gray-900 transition-opacity duration-500">
      <div className="text-xl font-semibold text-gray-800 dark:text-gray-100 mb-4">
        Yükleniyor...
      </div>
      <div className="w-64 h-4 bg-gray-300 dark:bg-gray-700 rounded-full overflow-hidden">
        <div
          className="h-full bg-green-600 transition-all duration-300"
          style={{ width: `${progress}%` }}
        ></div>
      </div>
      <div className="mt-2 text-sm text-gray-600 dark:text-gray-300">
        % {progress}
      </div>
    </div>
  );
}