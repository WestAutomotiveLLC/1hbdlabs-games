"""Builds the translated homepages (es/, fr/, ko/, tl/) from the English index.html.

Edit the English homepage, then run:  python tools/build-languages.py
Every English sentence listed below is swapped for its translation, links are pointed one folder up, and each
page gets its own language tag, address and search description. If you change an English sentence, change it
here too, or the script stops and names the sentence it couldn't find.
"""
import os, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BASE = "https://westautomotivellc.github.io/1hbdlabs-games/"

# English text on the homepage -> translations. Order matters only for overlapping strings (longest first).
T = {
"es": {
  "<html lang=\"en\">": "<html lang=\"es\">",
  "<title>1HBDLabs Language Games</title>": "<title>Juegos para aprender idiomas gratis | 1HBDLabs</title>",
  "Learn Spanish, English, Tagalog and French through free-to-download games from 1HBDLabs: WordBust, The Last Translator, Tomato Escape and Language.io.":
    "Aprende inglés, español, francés, coreano y tagalo jugando. Juegos gratis de vocabulario de 1HBDLabs: WordBust, The Last Translator, Tomato Escape y Language.io, que se juega gratis en el navegador.",
  "content=\"1HBDLabs Language Games\"": "content=\"Juegos para aprender idiomas gratis | 1HBDLabs\"",
  "Arcade vocabulary practice and a story-driven language RPG for Spanish, English, and Tagalog learners.":
    "Juegos de vocabulario arcade, un RPG de idiomas con historia y un juego de blobs en el navegador para aprender inglés, español, francés, coreano y tagalo.",
  "Take the 30-second quiz": "Haz el test de 30 segundos",
  "Take the quiz": "Hacer el test",
  "Free-to-download language games": "Juegos de idiomas gratis",
  "Play first.<br><span>Learn along the way.</span>": "Primero juega.<br><span>Aprende por el camino.</span>",
  "Four different games. One goal: make Spanish, English, Tagalog and French vocabulary practice feel like play.":
    "Cuatro juegos distintos. Un objetivo: que practicar vocabulario de inglés, español, tagalo, francés y coreano se sienta como jugar.",
  "Explore the games": "Ver los juegos",
  "Contact 1HBDLabs": "Contactar a 1HBDLabs",
  "SPANISH · ENGLISH · TAGALOG · FRENCH": "ESPAÑOL · INGLÉS · TAGALO · FRANCÉS",
  "30-second quiz": "Test de 30 segundos",
  "Which language learner are you?": "¿Qué tipo de estudiante de idiomas eres?",
  "Perfect Until Pressure? Better With Friends? Find your type, and the game made for it. In English, Spanish or Tagalog.":
    "¿Perfecto hasta que hay presión? ¿Mejor con amigos? Descubre tu tipo y el juego hecho para ti. En inglés, español o tagalo.",
  "Choose your challenge": "Elige tu reto",
  "Arcade speed, story battles, a spy chase or a blob battle?": "¿Velocidad arcade, batallas con historia, una persecución de espías o una batalla de blobs?",
  "Falling-word language arcade": "Arcade de palabras que caen",
  "Translate fast-moving vocabulary blocks before they reach the top. Learn 600 Spanish, English, or Tagalog words through short, replayable levels.":
    "Traduce bloques de vocabulario que se mueven rápido antes de que lleguen arriba. Aprende 600 palabras en español, inglés o tagalo con niveles cortos que puedes repetir.",
  "Translate in both directions": "Traduce en ambas direcciones",
  "Six stages from Easy to Master": "Seis etapas, de Fácil a Maestro",
  "Word lists, audio, flashcards, and streaks": "Listas de palabras, audio, tarjetas y rachas",
  "See WordBust": "Ver WordBust",
  "Story-driven language RPG": "RPG de idiomas con historia",
  "Use language as your weapon. Learn English, Spanish, Tagalog, French, or Korean while fighting through ten illustrated worlds filled with encounters and bosses — plus math, friends, and friend streaks.":
    "Usa el idioma como arma. Aprende inglés, español, tagalo, francés o coreano mientras luchas por diez mundos ilustrados llenos de encuentros y jefes, además de matemáticas, amigos y rachas con amigos.",
  "90 levels and 900 words in every course": "90 niveles y 900 palabras en cada curso",
  "Story battles, practice, and Survival": "Batallas de historia, práctica y Supervivencia",
  "Private friend battles with room codes": "Batallas privadas con amigos usando códigos de sala",
  "Math, friends, and friend streaks": "Matemáticas, amigos y rachas con amigos",
  "See the adventure": "Ver la aventura",
  "Blob battle · play free in your browser": "Batalla de blobs · juega gratis en el navegador",
  "Eat or get eaten. Every time you bump another blob, you both get the same word and whoever translates it first wins, taking up to their own size from the loser. Hide in thornbushes, dodge the big blobs and work through a 900-word course in Spanish, English, French, Filipino or Korean.":
    "Come o te comen. Cada vez que chocas con otro blob, los dos reciben la misma palabra y gana quien la traduzca primero, quitándole al perdedor hasta su propio tamaño. Escóndete en arbustos de espinas, esquiva a los blobs grandes y avanza por un curso de 900 palabras en español, inglés, francés, filipino o coreano.",
  "Play right now in your browser, no download": "Juega ahora en el navegador, sin descargar nada",
  "10-word lessons with review and flashcards": "Lecciones de 10 palabras con repaso y tarjetas",
  "Streak flames and a boss with its own music": "Llamas de racha y un jefe con su propia música",
  "Play Language.io": "Jugar Language.io",
  "iPhone and Android apps coming soon": "Apps para iPhone y Android muy pronto",
  "Spy chase · adventure runner": "Persecución de espías · aventura de correr",
  "A spy tomato has discovered an illegal sauce factory. Run, jump and slide through five worlds to escape and warn the others. Every gate is locked by a word, so you learn as you run: 250 words in English, Spanish, French or Tagalog.":
    "Un tomate espía descubrió una fábrica ilegal de salsa. Corre, salta y deslízate por cinco mundos para escapar y avisar a los demás. Cada puerta se abre con una palabra, así que aprendes mientras corres: 250 palabras en inglés, español, francés o tagalo.",
  "Five worlds and 25 levels, each with its own path": "Cinco mundos y 25 niveles, cada uno con su propio camino",
  "Easy mode picks answers, Hard mode types them": "En modo Fácil eliges respuestas; en Difícil las escribes",
  "Starts in your phone's language automatically": "Empieza en el idioma de tu teléfono automáticamente",
  "See Tomato Escape": "Ver Tomato Escape",
  "Coming soon to iPhone and Android": "Muy pronto en iPhone y Android",
  "Fair by design": "Justo por diseño",
  "Learning content stays available.": "El contenido para aprender siempre está disponible.",
  "No subscriptions are required to begin learning. Our games avoid pay-to-win upgrades; WordBust and The Last Translator offer optional one-time purchases.":
    "No necesitas suscripción para empezar a aprender. Nuestros juegos evitan las mejoras de pagar para ganar; WordBust y The Last Translator ofrecen compras únicas opcionales.",
  "Independent language games built for active recall and real play.": "Juegos de idiomas independientes, hechos para recordar activamente y jugar de verdad.",
  "Privacy & support": "Privacidad y soporte",
  "Follow 1HBDLabs": "Sigue a 1HBDLabs",
},
"fr": {
  "<html lang=\"en\">": "<html lang=\"fr\">",
  "<title>1HBDLabs Language Games</title>": "<title>Jeux gratuits pour apprendre les langues | 1HBDLabs</title>",
  "Learn Spanish, English, Tagalog and French through free-to-download games from 1HBDLabs: WordBust, The Last Translator, Tomato Escape and Language.io.":
    "Apprends l'anglais, l'espagnol, le coréen et le tagalog en jouant. Jeux de vocabulaire gratuits de 1HBDLabs : WordBust, The Last Translator, Tomato Escape et Language.io, jouable gratuitement dans le navigateur.",
  "content=\"1HBDLabs Language Games\"": "content=\"Jeux gratuits pour apprendre les langues | 1HBDLabs\"",
  "Arcade vocabulary practice and a story-driven language RPG for Spanish, English, and Tagalog learners.":
    "Jeux de vocabulaire arcade, un RPG de langues à histoire et un jeu de blobs dans le navigateur pour apprendre l'anglais, l'espagnol, le français, le coréen et le tagalog.",
  "Take the 30-second quiz": "Faire le quiz de 30 secondes",
  "Take the quiz": "Faire le quiz",
  "Free-to-download language games": "Jeux de langues gratuits",
  "Play first.<br><span>Learn along the way.</span>": "Joue d'abord.<br><span>Apprends en chemin.</span>",
  "Four different games. One goal: make Spanish, English, Tagalog and French vocabulary practice feel like play.":
    "Quatre jeux différents. Un seul but : que réviser le vocabulaire anglais, espagnol, tagalog, français et coréen ressemble à un jeu.",
  "Explore the games": "Voir les jeux",
  "Contact 1HBDLabs": "Contacter 1HBDLabs",
  "SPANISH · ENGLISH · TAGALOG · FRENCH": "ESPAGNOL · ANGLAIS · TAGALOG · FRANÇAIS",
  "30-second quiz": "Quiz de 30 secondes",
  "Which language learner are you?": "Quel type d'apprenant en langues es-tu ?",
  "Perfect Until Pressure? Better With Friends? Find your type, and the game made for it. In English, Spanish or Tagalog.":
    "Parfait jusqu'à la pression ? Meilleur avec des amis ? Découvre ton profil et le jeu fait pour toi. En anglais, espagnol ou tagalog.",
  "Choose your challenge": "Choisis ton défi",
  "Arcade speed, story battles, a spy chase or a blob battle?": "Vitesse arcade, combats à histoire, course-poursuite d'espions ou bataille de blobs ?",
  "Falling-word language arcade": "Arcade de mots qui tombent",
  "Translate fast-moving vocabulary blocks before they reach the top. Learn 600 Spanish, English, or Tagalog words through short, replayable levels.":
    "Traduis des blocs de vocabulaire rapides avant qu'ils n'atteignent le haut. Apprends 600 mots d'espagnol, d'anglais ou de tagalog avec des niveaux courts et rejouables.",
  "Translate in both directions": "Traduis dans les deux sens",
  "Six stages from Easy to Master": "Six étapes, de Facile à Maître",
  "Word lists, audio, flashcards, and streaks": "Listes de mots, audio, cartes et séries",
  "See WordBust": "Voir WordBust",
  "Story-driven language RPG": "RPG de langues à histoire",
  "Use language as your weapon. Learn English, Spanish, Tagalog, French, or Korean while fighting through ten illustrated worlds filled with encounters and bosses — plus math, friends, and friend streaks.":
    "Fais de la langue ton arme. Apprends l'anglais, l'espagnol, le tagalog, le français ou le coréen en combattant à travers dix mondes illustrés pleins de rencontres et de boss, avec en plus des maths, des amis et des séries entre amis.",
  "90 levels and 900 words in every course": "90 niveaux et 900 mots dans chaque cours",
  "Story battles, practice, and Survival": "Combats d'histoire, entraînement et Survie",
  "Private friend battles with room codes": "Combats privés entre amis avec des codes de salle",
  "Math, friends, and friend streaks": "Maths, amis et séries entre amis",
  "See the adventure": "Voir l'aventure",
  "Blob battle · play free in your browser": "Bataille de blobs · joue gratuitement dans le navigateur",
  "Eat or get eaten. Every time you bump another blob, you both get the same word and whoever translates it first wins, taking up to their own size from the loser. Hide in thornbushes, dodge the big blobs and work through a 900-word course in Spanish, English, French, Filipino or Korean.":
    "Mange ou fais-toi manger. Chaque fois que tu touches un autre blob, vous recevez le même mot et le premier qui le traduit gagne, en prenant au perdant jusqu'à sa propre taille. Cache-toi dans les buissons d'épines, évite les gros blobs et avance dans un cours de 900 mots en espagnol, anglais, français, filipino ou coréen.",
  "Play right now in your browser, no download": "Joue tout de suite dans ton navigateur, sans téléchargement",
  "10-word lessons with review and flashcards": "Leçons de 10 mots avec révision et cartes",
  "Streak flames and a boss with its own music": "Flammes de série et un boss avec sa propre musique",
  "Play Language.io": "Jouer à Language.io",
  "iPhone and Android apps coming soon": "Applis iPhone et Android bientôt disponibles",
  "Spy chase · adventure runner": "Course-poursuite d'espions · aventure",
  "A spy tomato has discovered an illegal sauce factory. Run, jump and slide through five worlds to escape and warn the others. Every gate is locked by a word, so you learn as you run: 250 words in English, Spanish, French or Tagalog.":
    "Une tomate espionne a découvert une usine de sauce illégale. Cours, saute et glisse à travers cinq mondes pour t'échapper et prévenir les autres. Chaque porte s'ouvre avec un mot, donc tu apprends en courant : 250 mots en anglais, espagnol, français ou tagalog.",
  "Five worlds and 25 levels, each with its own path": "Cinq mondes et 25 niveaux, chacun avec son propre parcours",
  "Easy mode picks answers, Hard mode types them": "En mode Facile tu choisis, en mode Difficile tu écris",
  "Starts in your phone's language automatically": "Démarre automatiquement dans la langue de ton téléphone",
  "See Tomato Escape": "Voir Tomato Escape",
  "Coming soon to iPhone and Android": "Bientôt sur iPhone et Android",
  "Fair by design": "Équitable par conception",
  "Learning content stays available.": "Le contenu pour apprendre reste disponible.",
  "No subscriptions are required to begin learning. Our games avoid pay-to-win upgrades; WordBust and The Last Translator offer optional one-time purchases.":
    "Aucun abonnement n'est nécessaire pour commencer à apprendre. Nos jeux évitent les améliorations payantes pour gagner ; WordBust et The Last Translator proposent des achats uniques facultatifs.",
  "Independent language games built for active recall and real play.": "Des jeux de langues indépendants, conçus pour la mémorisation active et le vrai jeu.",
  "Privacy & support": "Confidentialité et aide",
  "Follow 1HBDLabs": "Suivre 1HBDLabs",
},
"ko": {
  "<html lang=\"en\">": "<html lang=\"ko\">",
  "<title>1HBDLabs Language Games</title>": "<title>무료 외국어 학습 게임 | 1HBDLabs</title>",
  "Learn Spanish, English, Tagalog and French through free-to-download games from 1HBDLabs: WordBust, The Last Translator, Tomato Escape and Language.io.":
    "게임으로 영어, 스페인어, 프랑스어, 타갈로그어 단어를 배워 보세요. 1HBDLabs의 무료 단어 게임: WordBust, The Last Translator, Tomato Escape, 그리고 브라우저에서 무료로 하는 Language.io.",
  "content=\"1HBDLabs Language Games\"": "content=\"무료 외국어 학습 게임 | 1HBDLabs\"",
  "Arcade vocabulary practice and a story-driven language RPG for Spanish, English, and Tagalog learners.":
    "아케이드 단어 게임, 스토리 언어 RPG, 브라우저 블롭 배틀로 영어, 스페인어, 프랑스어, 한국어, 타갈로그어를 배워요.",
  "Take the 30-second quiz": "30초 퀴즈 하기",
  "Take the quiz": "퀴즈 하기",
  "Free-to-download language games": "무료 언어 게임",
  "Play first.<br><span>Learn along the way.</span>": "먼저 놀고,<br><span>배우는 건 덤으로.</span>",
  "Four different games. One goal: make Spanish, English, Tagalog and French vocabulary practice feel like play.":
    "서로 다른 네 가지 게임, 하나의 목표: 영어, 스페인어, 타갈로그어, 프랑스어, 한국어 단어 연습을 놀이처럼.",
  "Explore the games": "게임 둘러보기",
  "Contact 1HBDLabs": "1HBDLabs에 문의",
  "SPANISH · ENGLISH · TAGALOG · FRENCH": "스페인어 · 영어 · 타갈로그어 · 프랑스어",
  "30-second quiz": "30초 퀴즈",
  "Which language learner are you?": "나는 어떤 언어 학습자일까요?",
  "Perfect Until Pressure? Better With Friends? Find your type, and the game made for it. In English, Spanish or Tagalog.":
    "압박만 없으면 완벽한 타입? 친구와 함께일 때 더 잘하는 타입? 내 유형과 나에게 맞는 게임을 찾아보세요. 영어, 스페인어, 타갈로그어로 제공돼요.",
  "Choose your challenge": "도전을 골라 보세요",
  "Arcade speed, story battles, a spy chase or a blob battle?": "아케이드 스피드, 스토리 배틀, 스파이 추격전, 아니면 블롭 배틀?",
  "Falling-word language arcade": "떨어지는 단어 아케이드",
  "Translate fast-moving vocabulary blocks before they reach the top. Learn 600 Spanish, English, or Tagalog words through short, replayable levels.":
    "빠르게 움직이는 단어 블록이 꼭대기에 닿기 전에 번역하세요. 짧고 반복할 수 있는 레벨로 스페인어, 영어, 타갈로그어 단어 600개를 배워요.",
  "Translate in both directions": "양방향 번역",
  "Six stages from Easy to Master": "쉬움부터 마스터까지 여섯 단계",
  "Word lists, audio, flashcards, and streaks": "단어 목록, 음성, 플래시카드, 연속 기록",
  "See WordBust": "WordBust 보기",
  "Story-driven language RPG": "스토리 언어 RPG",
  "Use language as your weapon. Learn English, Spanish, Tagalog, French, or Korean while fighting through ten illustrated worlds filled with encounters and bosses — plus math, friends, and friend streaks.":
    "언어를 무기로 쓰세요. 만남과 보스로 가득한 열 개의 그림 세계를 싸워 나가며 영어, 스페인어, 타갈로그어, 프랑스어, 한국어를 배워요. 수학, 친구, 친구 연속 기록도 있어요.",
  "90 levels and 900 words in every course": "코스마다 90레벨, 900단어",
  "Story battles, practice, and Survival": "스토리 배틀, 연습, 서바이벌",
  "Private friend battles with room codes": "방 코드로 하는 친구 비공개 대결",
  "Math, friends, and friend streaks": "수학, 친구, 친구 연속 기록",
  "See the adventure": "모험 보기",
  "Blob battle · play free in your browser": "블롭 배틀 · 브라우저에서 무료 플레이",
  "Eat or get eaten. Every time you bump another blob, you both get the same word and whoever translates it first wins, taking up to their own size from the loser. Hide in thornbushes, dodge the big blobs and work through a 900-word course in Spanish, English, French, Filipino or Korean.":
    "먹거나 먹히거나. 다른 블롭과 부딪힐 때마다 둘 다 같은 단어를 받고, 먼저 번역한 쪽이 이겨 진 쪽에게서 자기 크기만큼까지 가져가요. 가시덤불에 숨고, 큰 블롭을 피하며, 스페인어, 영어, 프랑스어, 필리핀어, 한국어 900단어 코스를 진행해요.",
  "Play right now in your browser, no download": "다운로드 없이 브라우저에서 바로 플레이",
  "10-word lessons with review and flashcards": "복습과 플래시카드가 있는 10단어 레슨",
  "Streak flames and a boss with its own music": "연속 기록 불꽃과 전용 음악이 있는 보스",
  "Play Language.io": "Language.io 하기",
  "iPhone and Android apps coming soon": "iPhone, Android 앱 출시 예정",
  "Spy chase · adventure runner": "스파이 추격 · 어드벤처 러너",
  "A spy tomato has discovered an illegal sauce factory. Run, jump and slide through five worlds to escape and warn the others. Every gate is locked by a word, so you learn as you run: 250 words in English, Spanish, French or Tagalog.":
    "스파이 토마토가 불법 소스 공장을 발견했어요. 다섯 개의 세계를 달리고, 뛰고, 미끄러지며 탈출해 동료들에게 알리세요. 모든 문은 단어로 잠겨 있어서 달리면서 배워요. 영어, 스페인어, 프랑스어, 타갈로그어 250단어.",
  "Five worlds and 25 levels, each with its own path": "다섯 세계, 25레벨, 레벨마다 다른 길",
  "Easy mode picks answers, Hard mode types them": "쉬움 모드는 고르고, 어려움 모드는 직접 입력",
  "Starts in your phone's language automatically": "휴대폰 언어로 자동 시작",
  "See Tomato Escape": "Tomato Escape 보기",
  "Coming soon to iPhone and Android": "iPhone, Android 출시 예정",
  "Fair by design": "처음부터 공정하게",
  "Learning content stays available.": "학습 콘텐츠는 언제나 열려 있어요.",
  "No subscriptions are required to begin learning. Our games avoid pay-to-win upgrades; WordBust and The Last Translator offer optional one-time purchases.":
    "구독 없이 바로 배울 수 있어요. 돈을 내야 이기는 업그레이드는 없고, WordBust와 The Last Translator에는 선택 사항인 1회 구매만 있어요.",
  "Independent language games built for active recall and real play.": "능동적 회상과 진짜 놀이를 위해 만든 독립 언어 게임.",
  "Privacy & support": "개인정보 및 지원",
  "Follow 1HBDLabs": "1HBDLabs 팔로우",
},
"tl": {
  "<html lang=\"en\">": "<html lang=\"tl\">",
  "<title>1HBDLabs Language Games</title>": "<title>Libreng laro para matuto ng wika | 1HBDLabs</title>",
  "Learn Spanish, English, Tagalog and French through free-to-download games from 1HBDLabs: WordBust, The Last Translator, Tomato Escape and Language.io.":
    "Matuto ng English, Spanish, French at Korean habang naglalaro. Libreng vocabulary games ng 1HBDLabs: WordBust, The Last Translator, Tomato Escape at Language.io, na libreng malalaro sa browser.",
  "content=\"1HBDLabs Language Games\"": "content=\"Libreng laro para matuto ng wika | 1HBDLabs\"",
  "Arcade vocabulary practice and a story-driven language RPG for Spanish, English, and Tagalog learners.":
    "Arcade vocabulary games, isang language RPG na may kuwento at isang blob battle sa browser para matuto ng English, Spanish, French, Korean at Tagalog.",
  "Take the 30-second quiz": "Sagutan ang 30-segundong quiz",
  "Take the quiz": "Sagutan ang quiz",
  "Free-to-download language games": "Libreng language games",
  "Play first.<br><span>Learn along the way.</span>": "Maglaro muna.<br><span>Matuto habang naglalaro.</span>",
  "Four different games. One goal: make Spanish, English, Tagalog and French vocabulary practice feel like play.":
    "Apat na magkakaibang laro. Iisang layunin: gawing parang laro ang pag-practice ng bokabularyo sa English, Spanish, Tagalog, French at Korean.",
  "Explore the games": "Tingnan ang mga laro",
  "Contact 1HBDLabs": "Kontakin ang 1HBDLabs",
  "SPANISH · ENGLISH · TAGALOG · FRENCH": "SPANISH · ENGLISH · TAGALOG · FRENCH",
  "30-second quiz": "30-segundong quiz",
  "Which language learner are you?": "Anong klaseng language learner ka?",
  "Perfect Until Pressure? Better With Friends? Find your type, and the game made for it. In English, Spanish or Tagalog.":
    "Perpekto hanggang may pressure? Mas magaling kasama ang barkada? Alamin ang type mo at ang larong para sa iyo. Sa English, Spanish o Tagalog.",
  "Choose your challenge": "Piliin ang hamon mo",
  "Arcade speed, story battles, a spy chase or a blob battle?": "Bilis ng arcade, laban na may kuwento, habulan ng espiya o blob battle?",
  "Falling-word language arcade": "Arcade ng mga nahuhulog na salita",
  "Translate fast-moving vocabulary blocks before they reach the top. Learn 600 Spanish, English, or Tagalog words through short, replayable levels.":
    "Isalin ang mabibilis na vocabulary block bago sila umabot sa itaas. Matuto ng 600 salita sa Spanish, English o Tagalog sa maiikling level na puwedeng ulitin.",
  "Translate in both directions": "Magsalin sa dalawang direksyon",
  "Six stages from Easy to Master": "Anim na stage mula Easy hanggang Master",
  "Word lists, audio, flashcards, and streaks": "Word list, audio, flashcards at streak",
  "See WordBust": "Tingnan ang WordBust",
  "Story-driven language RPG": "Language RPG na may kuwento",
  "Use language as your weapon. Learn English, Spanish, Tagalog, French, or Korean while fighting through ten illustrated worlds filled with encounters and bosses — plus math, friends, and friend streaks.":
    "Gawing sandata ang wika. Matuto ng English, Spanish, Tagalog, French o Korean habang lumalaban sa sampung illustrated na mundo na puno ng engkuwentro at boss, may math, friends at friend streaks pa.",
  "90 levels and 900 words in every course": "90 level at 900 salita sa bawat kurso",
  "Story battles, practice, and Survival": "Story battles, practice at Survival",
  "Private friend battles with room codes": "Pribadong laban kasama ang kaibigan gamit ang room code",
  "Math, friends, and friend streaks": "Math, friends at friend streaks",
  "See the adventure": "Tingnan ang adventure",
  "Blob battle · play free in your browser": "Blob battle · libreng laruin sa browser",
  "Eat or get eaten. Every time you bump another blob, you both get the same word and whoever translates it first wins, taking up to their own size from the loser. Hide in thornbushes, dodge the big blobs and work through a 900-word course in Spanish, English, French, Filipino or Korean.":
    "Kumain o kainin. Tuwing mababangga mo ang ibang blob, pareho kayong bibigyan ng parehong salita at panalo ang unang makapagsalin, at kukunin niya sa talo hanggang sa sarili niyang laki. Magtago sa matinik na halaman, iwasan ang malalaking blob at tapusin ang 900-salitang kurso sa Spanish, English, French, Filipino o Korean.",
  "Play right now in your browser, no download": "Laruin ngayon sa browser, walang download",
  "10-word lessons with review and flashcards": "10-salitang lesson na may review at flashcards",
  "Streak flames and a boss with its own music": "Streak flames at boss na may sariling music",
  "Play Language.io": "Laruin ang Language.io",
  "iPhone and Android apps coming soon": "Malapit na ang app sa iPhone at Android",
  "Spy chase · adventure runner": "Habulan ng espiya · adventure runner",
  "A spy tomato has discovered an illegal sauce factory. Run, jump and slide through five worlds to escape and warn the others. Every gate is locked by a word, so you learn as you run: 250 words in English, Spanish, French or Tagalog.":
    "Natuklasan ng isang spy tomato ang isang ilegal na pabrika ng sarsa. Tumakbo, tumalon at dumulas sa limang mundo para makatakas at babalaan ang iba. Bawat gate ay nakakandado ng salita, kaya natututo ka habang tumatakbo: 250 salita sa English, Spanish, French o Tagalog.",
  "Five worlds and 25 levels, each with its own path": "Limang mundo at 25 level, may sariling daan ang bawat isa",
  "Easy mode picks answers, Hard mode types them": "Sa Easy mode pumipili ka, sa Hard mode nagta-type ka",
  "Starts in your phone's language automatically": "Awtomatikong nagsisimula sa wika ng phone mo",
  "See Tomato Escape": "Tingnan ang Tomato Escape",
  "Coming soon to iPhone and Android": "Malapit na sa iPhone at Android",
  "Fair by design": "Patas mula umpisa",
  "Learning content stays available.": "Laging bukas ang learning content.",
  "No subscriptions are required to begin learning. Our games avoid pay-to-win upgrades; WordBust and The Last Translator offer optional one-time purchases.":
    "Hindi kailangan ng subscription para magsimulang matuto. Walang pay-to-win na upgrade sa mga laro namin; may optional na one-time purchase ang WordBust at The Last Translator.",
  "Independent language games built for active recall and real play.": "Mga independent na language game para sa active recall at tunay na laro.",
  "Privacy & support": "Privacy at suporta",
  "Follow 1HBDLabs": "I-follow ang 1HBDLabs",
},
}

def build(lang, src):
    s = src
    for en, tr in sorted(T[lang].items(), key=lambda kv: -len(kv[0])):
        if en not in s:
            raise SystemExit(f"[{lang}] English text not found on the homepage: {en[:80]}")
        s = s.replace(en, tr)
    # point relative links and images one folder up
    s = re.sub(r'(href|src)="(?!https?:|mailto:|#|\.\./|data:)([^"]*)"', lambda m: f'{m.group(1)}="../{m.group(2)}"', s)
    s = s.replace('href=".././"', 'href="../"')
    # this page's own address
    s = s.replace(f'<link rel="canonical" href="{BASE}">', f'<link rel="canonical" href="{BASE}{lang}/">')
    s = s.replace(f'<meta property="og:url" content="{BASE}">', f'<meta property="og:url" content="{BASE}{lang}/">')
    # only the English homepage redirects; translated pages just remember a choice
    s = s.replace('<script src="../assets/lang.js" data-home-redirect></script>', '<script src="../assets/lang.js"></script>')
    # language switcher: mark this language, fix its links
    s = s.replace('href="../" data-setlang="en" aria-current="true"', 'href="../" data-setlang="en"')
    s = s.replace(f'href="../{lang}/" data-setlang="{lang}"', f'href="./" data-setlang="{lang}" aria-current="true"')
    # open the game in this language
    s = s.replace('href="../language-io/"', f'href="../language-io/?lang={lang}"')
    return s

if __name__ == "__main__":
    src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    for lang in T:
        out = os.path.join(ROOT, lang)
        os.makedirs(out, exist_ok=True)
        open(os.path.join(out, "index.html"), "w", encoding="utf-8", newline="\n").write(build(lang, src))
        print(f"wrote {lang}/index.html")
