// src/app/page.tsx

import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-800 dark:text-gray-100 py-10 px-6">
      <div className="max-w-5xl mx-auto">
        <h1 className="text-4xl font-bold mb-4 text-center text-green-700 dark:text-green-300">
          Akademik Sunumlar
        </h1>
        <p className="text-center text-lg mb-10 text-gray-600 dark:text-gray-400">
          Burada akademik çalışmalarımız kapsamında hazırlanan dijital sunumları
          bulabilirsiniz.
        </p>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Sunum Kartı 1 */}
          <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-5 hover:shadow-2xl transition-all duration-300 border border-gray-200 dark:border-gray-700">
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
          </div>

          {/* Yeni sunumlar eklendikçe aşağıya yeni kartlar eklenebilir */}
        </div>

        <div className="mt-16 text-center text-xs text-gray-500 dark:text-gray-600">
          © {new Date().getFullYear()} Hazırlayanlar: Süleyman Nuri Yağcı & Sait Ramazan Gülbay
        </div>
      </div>
    </main>
  );
}