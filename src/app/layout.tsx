/* src/app/layout.tsx */
import React, { ReactNode } from "react";
import "./globals.css";

export const metadata = {
  title: "Akademik Sunumlar",
  description: "Dr. Yağcı & Dr. Gülbay'ın akademik sunum platformu",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="tr">
      <head />
      <body className="bg-gray-50 dark:bg-gray-900 text-gray-800 dark:text-gray-100">
        {children}
      </body>
    </html>
  );
}