// src/components/MotionCard.tsx
"use client";

import { motion } from "framer-motion";
import Link from "next/link";

export default function MotionCard() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 40 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
      className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-5 hover:shadow-2xl transition-all duration-300 border border-gray-200 dark:border-gray-700"
    >
      <h2 className="text-xl font-semibold mb-2 text-green-700 dark:text-green-300">
        Şeyhî Sempozyumu Sunumu
      </h2>
      <p className="text-sm text-gray-600 dark:text-gray-400 mb-4">
        Osmanlı Tıbbında Sirke Kullanımı - Geleneksel ve Modern Yorumlar
      </p>
      <Link
        href="/Sunumlar/Seyhi-Sempozyum/SUNUM.html"
        target="_blank"
        className="inline-block mt-2 px-4 py-2 bg-green-600 text-white text-sm rounded hover:bg-green-700 transition-colors"
      >
        Sunumu Görüntüle
      </Link>
    </motion.div>
  );
}