import Link from 'next/link';

export default function Home() {
  return (
    <main className="min-h-screen bg-gray-100 text-gray-800 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-6">📚 Akademik Sunumlar</h1>
        <p className="mb-8 text-lg text-gray-600">Bu sayfada akademik sunumlarımı bulabilirsiniz.</p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Link
            href="/Sunumlar/Seyhi-Sempozyum/sunum.html"
            className="block border border-gray-300 rounded-lg p-6 hover:bg-green-50 hover:shadow-lg transition"
          >
            <h2 className="text-xl font-semibold mb-2">Şeyhî Sempozyumu</h2>
            <p className="text-sm text-gray-500">Osmanlı tıbbında sirke ve sirkencübinin kullanımı</p>
          </Link>

          {/* Yeni sunumlar eklendikçe buraya yeni <Link /> bileşenleri eklenebilir */}
        </div>
      </div>
    </main>
  );
}
