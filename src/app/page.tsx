// src/app/page.tsx

import Link from "next/link";
import { motion } from "framer-motion";

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-white via-gray-100 to-gray-200 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900 text-gray-800 dark:text-gray-100 py-14 px-6">
      <div className="max-w-6xl mx-auto">
        <motion.h1
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
          className="text-5xl font-extrabold mb-6 text-center text-green-700 dark:text-green-300 tracking-tight"
        >
          📚 Akademik Sunumlar
        </motion.h1>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5, duration: 0.6 }}
          className="text-center text-xl mb-12 text-gray-600 dark:text-gray-400 max-w-3xl mx-auto"
        >
          Akademik çalışmalar kapsamında hazırlanan dijital sunumları buradan keşfedebilirsiniz.
        </motion.p>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {/* Sunum Kartı */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.4, duration: 0.5 }}
            whileHover={{ scale: 1.03 }}
            className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-6 border border-gray-200 dark:border-gray-700 transform transition-all duration-300 hover:shadow-2xl"
          >
            <h2 className="text-2xl font-semibold mb-2 text-green-700 dark:text-green-300">
              Şeyhî Sempozyumu Sunumu
            </h2>
            <p className="text-md text-gray-600 dark:text-gray-400 mb-4">
              Osmanlı Tıbbında Sirke Kullanımı: Geleneksel Bilgelik & Modern Yorumlar
            </p>
            <Link
              href="/Sunumlar/Seyhi-Sempozyum/SUNUM.html"
              target="_blank"
              className="inline-block mt-2 px-5 py-2 bg-green-600 text-white text-sm rounded-full hover:bg-green-700 shadow-md transition duration-300"
            >
              📖 Sunumu Görüntüle
            </Link>
          </motion.div>
        </div>

        <motion.footer
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1.2, duration: 0.5 }}
          className="mt-20 text-center text-sm text-gray-500 dark:text-gray-600"
        >
          © {new Date().getFullYear()} Hazırlayanlar: Süleyman Nuri Yağcı & Sait Ramazan Gülbay
        </motion.footer>
      </div>
    </main>
  );
}
