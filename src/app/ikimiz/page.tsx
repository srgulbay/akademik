"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";

type LevelId = "yakinlik" | "sefkat" | "romantik" | "tutku";

type Card = {
  id: string;
  level: LevelId;
  prompt: string;
  soft: string;
};

type Level = {
  id: LevelId;
  emoji: string;
  title: string;
  blurb: string;
  ring: string;
  chip: string;
  gradient: string;
  adultsOnly?: boolean;
};

const LEVELS: ReadonlyArray<Level> = [
  {
    id: "yakinlik",
    emoji: "🌱",
    title: "Yakınlık",
    blurb: "Sözle, bakışla, dinleyerek bağ kurmak.",
    ring: "ring-emerald-300 dark:ring-emerald-600",
    chip: "bg-emerald-100 text-emerald-700 dark:bg-emerald-900/50 dark:text-emerald-200",
    gradient: "from-emerald-200/70 via-emerald-100/60 to-white dark:from-emerald-900/40 dark:via-emerald-950/40 dark:to-gray-900",
  },
  {
    id: "sefkat",
    emoji: "🤍",
    title: "Şefkat",
    blurb: "Yumuşak, acelesiz dokunuş ve sıcaklık.",
    ring: "ring-sky-300 dark:ring-sky-600",
    chip: "bg-sky-100 text-sky-700 dark:bg-sky-900/50 dark:text-sky-200",
    gradient: "from-sky-200/70 via-sky-100/60 to-white dark:from-sky-900/40 dark:via-sky-950/40 dark:to-gray-900",
  },
  {
    id: "romantik",
    emoji: "🌹",
    title: "Romantik",
    blurb: "Fısıltı, yakın öpücük, küçük sürprizler.",
    ring: "ring-rose-300 dark:ring-rose-600",
    chip: "bg-rose-100 text-rose-700 dark:bg-rose-900/50 dark:text-rose-200",
    gradient: "from-rose-200/70 via-rose-100/60 to-white dark:from-rose-900/40 dark:via-rose-950/40 dark:to-gray-900",
  },
  {
    id: "tutku",
    emoji: "🔥",
    title: "Tutku",
    blurb: "Daha cesur, mahrem; yalnız ikinize ait.",
    ring: "ring-amber-300 dark:ring-amber-600",
    chip: "bg-amber-100 text-amber-700 dark:bg-amber-900/50 dark:text-amber-200",
    gradient: "from-amber-200/70 via-rose-100/60 to-white dark:from-amber-900/40 dark:via-rose-950/40 dark:to-gray-900",
    adultsOnly: true,
  },
];

const CARDS: ReadonlyArray<Card> = [
  // 🌱 Yakınlık
  { id: "y1", level: "yakinlik", prompt: "Son zamanlarda seni en çok mutlu eden üç küçük şeyi anlat.", soft: "Sadece bir tanesini söyle." },
  { id: "y2", level: "yakinlik", prompt: "İlk tanıştığımızda dikkatini ilk çeken şey neydi?", soft: "Tek kelimeyle yanıtla." },
  { id: "y3", level: "yakinlik", prompt: "Birlikte yaşadığımız anılardan en çok hangisini yeniden yaşardın?", soft: "Adını söylemen yeterli." },
  { id: "y4", level: "yakinlik", prompt: "Bende seni en çok hangi an kendine yakın hissediyorsun?", soft: "Aklına gelen ilk sahneyi tarif et." },
  { id: "y5", level: "yakinlik", prompt: "Bu hafta seninle gurur duyduğum bir şeyi paylaşmama izin ver.", soft: "Sadece 'gurur duyuyorum' demek de yeter." },
  { id: "y6", level: "yakinlik", prompt: "Hayatımızda asla değişmesini istemediğin bir şey nedir?", soft: "Kısaca, gerekçesiz söyle." },
  { id: "y7", level: "yakinlik", prompt: "Bana son zamanlarda söyleyemediğin küçük bir teşekkür var mı?", soft: "İçinden geçen ilk şeyi söyle." },
  { id: "y8", level: "yakinlik", prompt: "Gözlerine 30 saniye sessizce bak; ardından ne hissettiğini söyle.", soft: "Sadece 10 saniye bakın, konuşmak şart değil." },

  // 🤍 Şefkat
  { id: "s1", level: "sefkat", prompt: "Eşini 30 saniye sımsıkı sarıl, hiçbir şey söyleme.", soft: "10 saniyelik bir sarılma da güzel." },
  { id: "s2", level: "sefkat", prompt: "Avucunun içine başparmağıyla yavaşça daireler çizmesine izin ver.", soft: "Sadece ellerinizi birleştirin." },
  { id: "s3", level: "sefkat", prompt: "Sırtına 2 dakika hafif bir masaj yap.", soft: "Sadece omuzlarına dokun." },
  { id: "s4", level: "sefkat", prompt: "Saçlarını okşa; hiçbir şey söyleme.", soft: "Alnına nazikçe dokun." },
  { id: "s5", level: "sefkat", prompt: "Alnından bir öpücük ver, sonra gözlerine bak.", soft: "Sadece alnını alnına dayayın." },
  { id: "s6", level: "sefkat", prompt: "Yan yana uzanın, kalp atışlarını dinleyene kadar bekleyin.", soft: "Sadece yan yana oturun, ellerinizi tutun." },
  { id: "s7", level: "sefkat", prompt: "Bir battaniyenin altında iki dakika boyunca sessizce sarılın.", soft: "Sadece elini tut." },

  // 🌹 Romantik
  { id: "r1", level: "romantik", prompt: "Boynuna en yumuşak şekilde bir öpücük ver.", soft: "Yanağına bir öpücük yeter." },
  { id: "r2", level: "romantik", prompt: "Kulağına en sevdiği şekilde 'seni seviyorum' fısılda.", soft: "Sadece gözlerine bakarak söyle." },
  { id: "r3", level: "romantik", prompt: "Onu yavaşça öp; en az 5 saniye sürsün.", soft: "Kısa, hafif bir öpücük de olur." },
  { id: "r4", level: "romantik", prompt: "Bedeninde en sevdiğin bir özelliği söyle, ardından oraya hafifçe dokun.", soft: "Sadece söyle, dokunmasan da olur." },
  { id: "r5", level: "romantik", prompt: "Birlikte slow yapmak için bir şarkı seç; ilk dakikayı dans edin.", soft: "Sadece ayakta sarılarak sallanın." },
  { id: "r6", level: "romantik", prompt: "Gözleri kapalıyken yüzünü parmak uçlarınla yavaşça tarif et.", soft: "Sadece elinin tersiyle yanağına dokun." },
  { id: "r7", level: "romantik", prompt: "Ona bugün senin için neden özel olduğunu üç cümlede söyle.", soft: "Tek cümleyle özetle." },

  // 🔥 Tutku (yetişkin — ima yoluyla)
  { id: "t1", level: "tutku", prompt: "Onun bedeninde en çok sevdiğin yeri kulağına fısılda.", soft: "Sadece 'çok güzelsin' fısılda." },
  { id: "t2", level: "tutku", prompt: "Gözlerini kapasın; bir dakika boyunca sadece sen dokun.", soft: "Sadece elini ve kolunu okşa." },
  { id: "t3", level: "tutku", prompt: "Bir dakika boyunca sıra sende: nasıl dokunulmasını istediğini söyle, o dinlesin.", soft: "Sadece 'şu an iyi hissettiren bir şey' söyle." },
  { id: "t4", level: "tutku", prompt: "Birlikte hayalini kurduğunuz bir akşamı bir cümleyle paylaş — yargısız.", soft: "Aklındaki yeri/atmosferi anlat, gerisini sakla." },
  { id: "t5", level: "tutku", prompt: "Onun bu an için bir isteği var mı, sor ve sadece dinle.", soft: "İsteğini sormak yerine, onu rahat ettirecek bir şeyi söyle." },
  { id: "t6", level: "tutku", prompt: "Gözlerini kapatsın; dokunduğun yeri tahmin etmesini iste.", soft: "Sadece eline ve koluna dokun." },
  { id: "t7", level: "tutku", prompt: "Bu akşam birlikte denemek istediğin küçük bir şeyi söyle; o evet/hayır/sonra desin.", soft: "Sadece 'yakınlaşmak istiyorum' demen yeter." },
];

type Phase =
  | "onboarding"
  | "level-vote"
  | "playing"
  | "break"
  | "ended";

type VoteState = {
  level: LevelId;
  partner: "A" | "B";
  choices: Record<"A" | "B", "yes" | "no" | null>;
};

function shuffle<T>(arr: ReadonlyArray<T>): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export default function IkimizOyun() {
  // --- onboarding state ---
  const [names, setNames] = useState<{ A: string; B: string }>({ A: "Sen", B: "Eşim" });
  const [boundariesOk, setBoundariesOk] = useState(false);
  const [safeWord, setSafeWord] = useState("Mola");
  const [unlocked, setUnlocked] = useState<Record<LevelId, boolean>>({
    yakinlik: true, // ilk seviye baştan açık
    sefkat: false,
    romantik: false,
    tutku: false,
  });

  // --- play state ---
  const [phase, setPhase] = useState<Phase>("onboarding");
  const [activeLevel, setActiveLevel] = useState<LevelId>("yakinlik");
  const deckRef = useRef<Card[]>([]);
  const [currentCard, setCurrentCard] = useState<Card | null>(null);
  const [turn, setTurn] = useState<"A" | "B">("A");
  const [softened, setSoftened] = useState(false);
  const [stats, setStats] = useState({ done: 0, soft: 0, passed: 0 });
  const passStreakRef = useRef(0);
  const [breakReason, setBreakReason] = useState<"safeword" | "streak" | "manual">("manual");

  // --- level vote state ---
  const [vote, setVote] = useState<VoteState | null>(null);

  // --- safe-word listener ---
  const safeWordRef = useRef(safeWord);
  useEffect(() => {
    safeWordRef.current = safeWord;
  }, [safeWord]);

  // Build & shuffle deck when level changes
  useEffect(() => {
    if (phase !== "playing") return;
    deckRef.current = shuffle(CARDS.filter((c) => c.level === activeLevel));
    setCurrentCard(null);
    setSoftened(false);
  }, [activeLevel, phase]);

  const drawCard = () => {
    if (deckRef.current.length === 0) {
      deckRef.current = shuffle(CARDS.filter((c) => c.level === activeLevel));
    }
    const [next, ...rest] = deckRef.current;
    deckRef.current = rest;
    setCurrentCard(next ?? null);
    setSoftened(false);
  };

  const onCardDone = () => {
    setStats((s) => ({ ...s, done: s.done + (softened ? 0 : 1), soft: s.soft + (softened ? 1 : 0) }));
    passStreakRef.current = 0;
    setTurn((t) => (t === "A" ? "B" : "A"));
    drawCard();
  };

  const onSoften = () => {
    setSoftened(true);
  };

  const onPass = () => {
    setStats((s) => ({ ...s, passed: s.passed + 1 }));
    passStreakRef.current += 1;
    if (passStreakRef.current >= 3) {
      passStreakRef.current = 0;
      setBreakReason("streak");
      setPhase("break");
      return;
    }
    setTurn((t) => (t === "A" ? "B" : "A"));
    drawCard();
  };

  const triggerSafeWord = () => {
    setBreakReason("safeword");
    setPhase("break");
  };

  const startVote = (level: LevelId) => {
    setVote({ level, partner: "A", choices: { A: null, B: null } });
    setPhase("level-vote");
  };

  const submitVote = (choice: "yes" | "no") => {
    if (!vote) return;
    const choices = { ...vote.choices, [vote.partner]: choice };
    if (vote.partner === "A") {
      setVote({ ...vote, partner: "B", choices });
      return;
    }
    // both voted — anonymous result
    const bothYes = choices.A === "yes" && choices.B === "yes";
    if (bothYes) {
      setUnlocked((u) => ({ ...u, [vote.level]: true }));
      setActiveLevel(vote.level);
      setPhase("playing");
      setStats({ done: 0, soft: 0, passed: 0 });
      passStreakRef.current = 0;
      setTurn("A");
    } else {
      // anonymity: do not reveal who said no
      setPhase("onboarding");
    }
    setVote(null);
  };

  const startGame = () => {
    setActiveLevel("yakinlik");
    setPhase("playing");
    setStats({ done: 0, soft: 0, passed: 0 });
    passStreakRef.current = 0;
    setTurn("A");
  };

  const resumeFromBreak = () => setPhase("playing");
  const endFromBreak = () => setPhase("ended");
  const restart = () => {
    setUnlocked({ yakinlik: true, sefkat: false, romantik: false, tutku: false });
    setStats({ done: 0, soft: 0, passed: 0 });
    setActiveLevel("yakinlik");
    setPhase("onboarding");
  };

  const activeLevelMeta = useMemo(
    () => LEVELS.find((l) => l.id === activeLevel) ?? LEVELS[0],
    [activeLevel],
  );

  const voteJustRejected = phase === "onboarding" && stats.done + stats.soft + stats.passed > 0;

  return (
    <main className={`min-h-screen px-4 py-8 md:py-12 flex flex-col items-center bg-gradient-to-br ${activeLevelMeta.gradient} text-gray-800 dark:text-gray-100 transition-colors`}>
      <header className="w-full max-w-2xl text-center mb-6">
        <motion.h1
          initial={{ opacity: 0, y: -8 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-3xl md:text-4xl font-extrabold text-rose-600 dark:text-rose-300"
        >
          💞 İkimiz
        </motion.h1>
        <p className="mt-2 text-sm md:text-base text-gray-600 dark:text-gray-300">
          Acelesiz, isteyerek, birlikte. Her zaman <em>{safeWord}</em> diyerek durabilirsin.
        </p>
      </header>

      {/* always-on safe word bar (visible in playing/level-vote) */}
      {(phase === "playing" || phase === "level-vote") && (
        <button
          onClick={triggerSafeWord}
          className="fixed bottom-4 left-1/2 -translate-x-1/2 z-40 rounded-full bg-white/90 dark:bg-gray-900/80 backdrop-blur shadow-lg border border-rose-200 dark:border-rose-800 px-5 py-2 text-sm font-semibold text-rose-600 dark:text-rose-300 hover:bg-white"
          aria-label="Mola ver"
        >
          ⏸️ {safeWord}
        </button>
      )}

      <AnimatePresence mode="wait">
        {phase === "onboarding" && (
          <motion.section
            key="onboarding"
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            className="w-full max-w-md bg-white/80 dark:bg-gray-900/60 backdrop-blur rounded-2xl shadow-xl p-6 flex flex-col gap-4"
          >
            {voteJustRejected && (
              <div className="rounded-xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800 p-3 text-sm text-amber-800 dark:text-amber-200">
                Bu seviyeyi şimdilik atlıyoruz. Kimsenin “hayır”ı paylaşılmaz — başka zaman tekrar deneyebilirsiniz. 💛
              </div>
            )}

            <h2 className="text-xl font-bold">Başlamadan önce</h2>

            <div className="grid grid-cols-2 gap-3">
              <label className="flex flex-col gap-1">
                <span className="text-xs font-medium opacity-70">1. kişi</span>
                <input
                  className="rounded-lg border border-rose-200 dark:border-rose-800 bg-white dark:bg-gray-900 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-rose-400"
                  value={names.A}
                  onChange={(e) => setNames((n) => ({ ...n, A: e.target.value.slice(0, 16) }))}
                />
              </label>
              <label className="flex flex-col gap-1">
                <span className="text-xs font-medium opacity-70">2. kişi</span>
                <input
                  className="rounded-lg border border-rose-200 dark:border-rose-800 bg-white dark:bg-gray-900 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-rose-400"
                  value={names.B}
                  onChange={(e) => setNames((n) => ({ ...n, B: e.target.value.slice(0, 16) }))}
                />
              </label>
            </div>

            <label className="flex flex-col gap-1">
              <span className="text-xs font-medium opacity-70">Güvenli kelime (her an söyleyebilirsin)</span>
              <input
                className="rounded-lg border border-rose-200 dark:border-rose-800 bg-white dark:bg-gray-900 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-rose-400"
                value={safeWord}
                onChange={(e) => setSafeWord(e.target.value.slice(0, 20) || "Mola")}
              />
            </label>

            <label className="flex items-start gap-2 text-sm mt-1">
              <input
                type="checkbox"
                className="mt-1 accent-rose-500"
                checked={boundariesOk}
                onChange={(e) => setBoundariesOk(e.target.checked)}
              />
              <span>
                İkimiz de konuştuk: birbirimizin <strong>“şu an istemem”</strong> hakkını kabul ediyoruz.
                Her karta <em>Pas</em> diyebiliriz, kimseden açıklama beklenmez.
              </span>
            </label>

            <div className="rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-100 dark:border-rose-900 p-3 text-xs text-rose-700 dark:text-rose-200 leading-relaxed">
              <strong>Çıkış yolu nasıl çalışır?</strong> Her seviye, ikinizin gizli oyuyla açılır.
              Telefonu sırayla tutarsınız; “hazır değilim” derseniz <em>kimin dediği</em> görünmez.
              Hiç utanma ya da açıklama gerekmez.
            </div>

            <button
              onClick={startGame}
              disabled={!boundariesOk}
              className="mt-2 rounded-full bg-rose-500 disabled:bg-rose-200 disabled:cursor-not-allowed hover:bg-rose-600 text-white font-semibold py-2.5 shadow"
            >
              Hadi başlayalım 💞
            </button>
          </motion.section>
        )}

        {phase === "playing" && (
          <motion.section
            key="playing"
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            className="w-full max-w-2xl flex flex-col items-center gap-5"
          >
            {/* level pills */}
            <div className="flex flex-wrap gap-2 justify-center">
              {LEVELS.map((lvl) => {
                const isActive = lvl.id === activeLevel;
                const isUnlocked = unlocked[lvl.id];
                return (
                  <button
                    key={lvl.id}
                    onClick={() => {
                      if (isActive) return;
                      if (isUnlocked) {
                        setActiveLevel(lvl.id);
                        setStats({ done: 0, soft: 0, passed: 0 });
                        passStreakRef.current = 0;
                        setTurn("A");
                      } else {
                        startVote(lvl.id);
                      }
                    }}
                    className={`px-3 py-1.5 rounded-full text-xs md:text-sm font-medium border transition
                      ${isActive ? `${lvl.chip} ring-2 ${lvl.ring} border-transparent` : "bg-white/70 dark:bg-gray-800/60 border-gray-200 dark:border-gray-700 hover:bg-white"}
                      ${!isUnlocked && !isActive ? "opacity-70" : ""}
                    `}
                    aria-label={`${lvl.title} seviyesi`}
                  >
                    {lvl.emoji} {lvl.title} {!isUnlocked && "🔒"}
                  </button>
                );
              })}
            </div>

            <div className="text-center">
              <p className="text-sm opacity-70">
                Sıra: <strong>{turn === "A" ? names.A : names.B}</strong>
              </p>
              <p className="text-xs opacity-60 mt-0.5">
                {activeLevelMeta.emoji} {activeLevelMeta.blurb}
              </p>
            </div>

            {/* card */}
            <div className="w-full max-w-md">
              {!currentCard ? (
                <motion.button
                  onClick={drawCard}
                  whileTap={{ scale: 0.97 }}
                  className={`w-full rounded-2xl shadow-xl p-8 bg-white/90 dark:bg-gray-900/70 border-2 border-dashed ${activeLevelMeta.ring.replace("ring-", "border-").replace("dark:ring-", "dark:border-")} text-lg font-semibold`}
                >
                  Kart çek ✨
                </motion.button>
              ) : (
                <AnimatePresence mode="wait">
                  <motion.div
                    key={currentCard.id + (softened ? "-soft" : "")}
                    initial={{ opacity: 0, rotateY: -15, y: 10 }}
                    animate={{ opacity: 1, rotateY: 0, y: 0 }}
                    exit={{ opacity: 0, rotateY: 15, y: -10 }}
                    transition={{ duration: 0.35 }}
                    className="rounded-2xl shadow-2xl bg-white/95 dark:bg-gray-900/85 backdrop-blur p-6 md:p-8 flex flex-col gap-4"
                  >
                    <div className={`self-start text-xs px-2 py-1 rounded-full ${activeLevelMeta.chip}`}>
                      {activeLevelMeta.emoji} {activeLevelMeta.title}
                      {softened && " · yumuşatıldı"}
                    </div>
                    <p className="text-lg md:text-xl leading-relaxed">
                      {softened ? currentCard.soft : currentCard.prompt}
                    </p>

                    <div className="grid grid-cols-3 gap-2 mt-2">
                      <button
                        onClick={onCardDone}
                        className="rounded-xl bg-emerald-500 hover:bg-emerald-600 text-white font-semibold py-2.5 shadow"
                      >
                        ✅ Yap
                      </button>
                      <button
                        onClick={onSoften}
                        disabled={softened}
                        className="rounded-xl bg-sky-100 dark:bg-sky-900/50 text-sky-700 dark:text-sky-200 font-semibold py-2.5 shadow disabled:opacity-50"
                      >
                        🌿 Yumuşat
                      </button>
                      <button
                        onClick={onPass}
                        className="rounded-xl bg-white dark:bg-gray-800 border border-rose-200 dark:border-rose-800 text-rose-600 dark:text-rose-300 font-semibold py-2.5 shadow"
                      >
                        ⏭️ Pas
                      </button>
                    </div>
                    <p className="text-xs opacity-60 text-center">
                      Pas için açıklama gerekmez. Aşağıdaki <strong>{safeWord}</strong> tuşuyla istediğin an mola ver.
                    </p>
                  </motion.div>
                </AnimatePresence>
              )}
            </div>

            <div className="flex gap-3 text-xs opacity-70">
              <span>✅ {stats.done}</span>
              <span>🌿 {stats.soft}</span>
              <span>⏭️ {stats.passed}</span>
            </div>
          </motion.section>
        )}

        {phase === "level-vote" && vote && (
          <motion.section
            key="vote"
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            className="w-full max-w-md bg-white/90 dark:bg-gray-900/70 backdrop-blur rounded-2xl shadow-xl p-6 flex flex-col gap-5 text-center"
          >
            <h2 className="text-lg font-bold">
              {LEVELS.find((l) => l.id === vote.level)?.emoji}{" "}
              {LEVELS.find((l) => l.id === vote.level)?.title} seviyesi için gizli oy
            </h2>
            <p className="text-sm opacity-80">
              Telefonu <strong>{vote.partner === "A" ? names.A : names.B}</strong> tutsun.
              Diğeri başka tarafa baksın. Cevabın gizli kalacak — kimin “hazır değilim” dediği görünmez.
            </p>
            <div className="grid grid-cols-2 gap-3">
              <button
                onClick={() => submitVote("yes")}
                className="rounded-xl bg-emerald-500 hover:bg-emerald-600 text-white font-semibold py-3 shadow"
              >
                💞 Hazırım
              </button>
              <button
                onClick={() => submitVote("no")}
                className="rounded-xl bg-white dark:bg-gray-800 border border-rose-200 dark:border-rose-800 text-rose-600 dark:text-rose-300 font-semibold py-3 shadow"
              >
                🌿 Hazır değilim
              </button>
            </div>
            <p className="text-xs opacity-60">
              {vote.partner === "A" ? "Sıra: 1. kişi" : "Sıra: 2. kişi (gizli oy)"}
            </p>
          </motion.section>
        )}

        {phase === "break" && (
          <motion.section
            key="break"
            initial={{ opacity: 0, scale: 0.98 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.98 }}
            className="w-full max-w-md bg-white/95 dark:bg-gray-900/80 backdrop-blur rounded-2xl shadow-2xl p-6 flex flex-col gap-4 text-center"
          >
            <h2 className="text-xl font-bold text-rose-600 dark:text-rose-300">Mola 🍵</h2>
            {breakReason === "safeword" && (
              <p className="text-sm opacity-80">
                Güvenli kelimeyi söyledin. Şimdi sadece nefes alalım. İstersen burada bitirebilir, istersen devam edebiliriz.
              </p>
            )}
            {breakReason === "streak" && (
              <p className="text-sm opacity-80">
                Birkaç kart üst üste pas geçildi — bu son derece normal. Belki şimdi bir çay/kahve molası, sohbet,
                ya da seviyeyi bir basamak aşağı çekmek iyi gelir. ✨
              </p>
            )}
            <div className="grid grid-cols-2 gap-3">
              <button
                onClick={resumeFromBreak}
                className="rounded-xl bg-emerald-500 hover:bg-emerald-600 text-white font-semibold py-2.5 shadow"
              >
                Devam edelim
              </button>
              <button
                onClick={endFromBreak}
                className="rounded-xl bg-white dark:bg-gray-800 border border-rose-200 dark:border-rose-800 text-rose-600 dark:text-rose-300 font-semibold py-2.5 shadow"
              >
                Bugünlük bitirelim
              </button>
            </div>
            {breakReason === "streak" && (
              <button
                onClick={() => {
                  // step one level down if possible
                  const order: LevelId[] = ["yakinlik", "sefkat", "romantik", "tutku"];
                  const idx = order.indexOf(activeLevel);
                  if (idx > 0) setActiveLevel(order[idx - 1]);
                  setPhase("playing");
                }}
                className="text-xs underline opacity-70 hover:opacity-100"
              >
                Bir basamak aşağı in
              </button>
            )}
          </motion.section>
        )}

        {phase === "ended" && (
          <motion.section
            key="ended"
            initial={{ opacity: 0, y: 8 }}
            animate={{ opacity: 1, y: 0 }}
            className="w-full max-w-md bg-white/95 dark:bg-gray-900/80 backdrop-blur rounded-2xl shadow-xl p-6 flex flex-col gap-4 text-center"
          >
            <h2 className="text-xl font-bold">Bugünlük buraya kadar 💞</h2>
            <p className="text-sm opacity-80">
              Birbirinize zaman ayırdığınız için teşekkürler. <strong>{stats.done}</strong> kart tamamladınız,{" "}
              <strong>{stats.soft}</strong> yumuşatıldı, <strong>{stats.passed}</strong> pas geçildi.
              Her seçim aynı derecede değerli.
            </p>
            <button
              onClick={restart}
              className="rounded-full bg-rose-500 hover:bg-rose-600 text-white font-semibold py-2.5 shadow"
            >
              Baştan başla
            </button>
          </motion.section>
        )}
      </AnimatePresence>

      <footer className="mt-10 text-[11px] opacity-60 max-w-md text-center leading-relaxed pb-20">
        Tasarım ilhamları: Gottman Card Decks, Betty Martin&apos;in Rıza Çarkı ve Three-Minute Game,
        çift terapisinde kullanılan kademeli yakınlık yaklaşımları. Hepsi rıza ve karşılıklı saygı temelli.
      </footer>
    </main>
  );
}
