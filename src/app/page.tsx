// src/app/page.tsx

"use client";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import LoadingOverlay from "@/components/LoadingOverlay";

// Özel Link bileşeni: Sayfa geçişlerinde loading animasyonu
function TransitionLink({ href, children }: { href: string; children: React.ReactNode }) {
  const [loading, setLoading] = useState(false);
  const handleClick = (e: React.MouseEvent) => {
    e.preventDefault();
    setLoading(true);
    setTimeout(() => (window.location.href = href), 600);
  };

  return (
    <>
      {loading && <LoadingOverlay />}
      <a href={href} onClick={handleClick} className="inline-block w-full">
        {children}
      </a>
    </>
  );
}

export default function Home() {
  const presentations = [
    {
      title: 'Şeyhî Sempozyumu',
      description: 'Derinlemesine Osmanlı Tıbbı ve Modern Bilim Analizi',
      path: '/Sunumlar/Seyhi-Sempozyum/SUNUM.html',
      date: 'Nisan 2025',
      bg: 'from-green-200 via-green-100 to-white'
    },
    {
      title: 'Antibiyotik Direnci ve Mikrobiyota',
      description: 'Dirençli bakterilere karşı yenilikçi çözümler',
      path: '/Sunumlar/Antibiyotik-Direnci/sunum.html',
      date: 'Mart 2025',
      bg: 'from-blue-200 via-blue-100 to-white'
    },
    {
      title: 'Flow Sitometri ile AML Tanısı',
      description: 'Makine öğrenmesi destekli analizler',
      path: '/Sunumlar/Flow-AML/sunum.html',
      date: 'Şubat 2025',
      bg: 'from-purple-200 via-purple-100 to-white'
    }
  ];

  return (
    <AnimatePresence>
      <motion.div
        key="home"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        transition={{ duration: 0.6 }}
        className="relative overflow-hidden"
      >
        {/* Yükleniyor animasyonu */}
        <LoadingOverlay />

        {/* Dalga SVG arka plan */}
        <div className="absolute inset-0 -z-10 overflow-hidden">
          <motion.svg
            className="w-full h-full"
            viewBox="0 0 1440 320"
            preserveAspectRatio="none"
            initial={{ y: 320 }}
            animate={{ y: 0 }}
            transition={{ duration: 1.2, ease: 'easeOut' }}
          >
            <path
              fill="#D1FAE5"
              fillOpacity="1"
              d="M0,96L60,128C120,160,240,224,360,234.7C480,245,600,203,720,181.3C840,160,960,160,1080,165.3C1200,171,1320,181,1380,186.7L1440,192L1440,320L1380,320C1320,320,1200,320,1080,320C960,320,840,320,720,320C600,320,480,320,360,320C240,320,120,320,60,320L0,320Z"
            />
          </motion.svg>
        </div>

        <main className="min-h-screen flex flex-col items-center justify-center px-6 py-16 bg-gray-50 dark:bg-gray-900 text-gray-800 dark:text-gray-100">
          <motion.h1
            className="text-5xl md:text-6xl font-extrabold text-center mb-6 text-green-700 dark:text-green-300"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8 }}
          >
            🎓 Akademik Sunumlar
          </motion.h1>

          <motion.p
            className="text-lg md:text-xl text-center max-w-2xl mb-12 text-gray-600 dark:text-gray-400"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.4, duration: 0.6 }}
          >
            Burada akademik toplantılarda sunduğum interaktif dijital sunumları keşfedebilirsiniz.
          </motion.p>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 w-full max-w-6xl">
            {presentations.map((p, i) => (
              <motion.div
                key={i}
                className={`rounded-3xl p-6 bg-gradient-to-br ${p.bg} backdrop-blur-sm border border-white/30 shadow-xl transform transition-transform duration-300 hover:scale-105`}
                initial={{ opacity: 0, y: 40 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.3 + i * 0.2, duration: 0.7 }}
                whileHover={{ scale: 1.07 }}
              >
                <h2 className="text-2xl font-semibold mb-2 text-gray-900 dark:text-gray-800">
                  {p.title}
                </h2>
                <p className="text-sm mb-4 text-gray-700 dark:text-gray-500">
                  {p.description}
                </p>
                <div className="flex items-center justify-between">
                  <span className="text-xs italic text-gray-700 dark:text-gray-500">
                    {p.date}
                  </span>
                  <TransitionLink href={p.path}>
                    <div className="inline-flex items-center space-x-2 bg-green-600 dark:bg-green-500 text-white px-4 py-2 rounded-full text-sm font-medium hover:bg-green-700 dark:hover:bg-green-600 transition-colors">
                      <span>☑️ Görüntüle</span>
                    </div>
                  </TransitionLink>
                </div>
              </motion.div>
            ))}
          </div>

          <motion.footer
            className="mt-16 text-center text-sm text-gray-500 dark:text-gray-400"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1.2, duration: 0.5 }}
          >
            © {new Date().getFullYear()} Dr. Süleyman Nuri Yağcı & Uzm. Dr. Sait Ramazan Gülbay
          </motion.footer>
        </main>
      </motion.div>
    </AnimatePresence>
  );
}