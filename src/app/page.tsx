'use client';

import Link from 'next/link';

export default function Home() {
  const presentations = [
    {
      title: 'Şeyhî Sempozyumu',
      description: 'Osmanlı tıbbı ve modern bilim karşılaştırması',
      path: '/sunumlar/seyhi-sempozyumu/sunum.html',
      date: 'Nisan 2025',
    },
    {
      title: 'Antibiyotik Direnci ve Mikrobiyota',
      description: 'Modern tıpta dirençli bakteriler ve çözüm yolları',
      path: '/sunumlar/antibiyotik-direnci/sunum.html',
      date: 'Mart 2025',
    },
    {
      title: 'Flow Sitometri ile AML Tanısı',
      description: 'Makine öğrenmesi ile hematoloji uygulamaları',
      path: '/sunumlar/flow-aml/sunum.html',
      date: 'Şubat 2025',
    }
  ];

  return (
    <main className="min-h-screen bg-gradient-to-br from-gray-50 to-white text-gray-800 py-16 px-6">
      <div className="max-w-4xl mx-auto text-center">
        <h1 className="text-4xl font-bold mb-4">🎓 Akademik Sunumlarım</h1>
        <p className="text-lg mb-10">
          Bilimsel toplantılarda sunduğum HTML tabanlı interaktif sunumlar aşağıda listelenmiştir.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-5xl mx-auto">
        {presentations.map((pres, idx) => (
          <Link href={pres.path} key={idx} target="_blank" className="hover:no-underline">
            <div className="border border-gray-200 rounded-xl shadow-sm hover:shadow-lg p-6 transition-all duration-200 bg-white hover:bg-green-50">
              <h2 className="text-xl font-semibold text-green-800 mb-2">{pres.title}</h2>
              <p className="text-sm text-gray-600 mb-2">{pres.description}</p>
              <p className="text-xs text-gray-500 italic">{pres.date}</p>
            </div>
          </Link>
        ))}
      </div>

      <footer className="mt-20 text-center text-sm text-gray-400">
        © {new Date().getFullYear()} Dr. Sait Ramazan Gülbay – Tüm Hakları Saklıdır
      </footer>
    </main>
  );
}