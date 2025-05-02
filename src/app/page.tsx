// src/app/page.tsx
import MotionCard from "@/components/MotionCard";

export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50 dark:bg-gray-900 text-gray-800 dark:text-gray-100 py-10 px-6">
      <div className="max-w-5xl mx-auto">
        <h1 className="text-4xl font-bold mb-4 text-center text-green-700 dark:text-green-300">
          Akademik Sunumlar
        </h1>
        <p className="text-center text-lg mb-10 text-gray-600 dark:text-gray-400">
          Burada akademik çalışmalarımız kapsamında hazırlanan dijital sunumları bulabilirsiniz.
        </p>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <MotionCard />
        </div>

        <div className="mt-16 text-center text-xs text-gray-500 dark:text-gray-600">
          © {new Date().getFullYear()} Hazırlayanlar: Süleyman Nuri Yağcı & Sait Ramazan Gülbay
        </div>
      </div>
    </main>
  );
}