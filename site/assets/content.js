/* Shared content for the site versions and the poster set.
   Everything marked TBC needs confirming with the instructor. */
window.DOJO = {
  club: {
    name: "Clearwater Jiu Jitsu & Judo",        // working name (TBC)
    short: "Clearwater",
    sub: "Jiu Jitsu & Judo",
    jp: "清水道場",
    jpReading: "Shimizu Dōjō",
    jpMeaning: "清水 (shimizu) literally means “clear water”",
    venue: "52 Ridge · Clearwater Valley Resort",
    address: "373 Clearwater Valley Rd, Clearwater, BC",
    url: "jiujitsu.designspore.co",
    href: "https://jiujitsu.designspore.co"
  },

  posters: [
    /* ---------------------------------------------------------------- */
    {
      id: "counting", type: "counting",
      jp: "数え方", romaji: "Kazoekata", title: "Counting to ten",
      lede: "Warm-ups, drills and push-ups are counted in Japanese. Learn these ten and you can lead the count.",
      items: [
        { n: 1,  k: "一", r: "ichi",        kana: "いち" },
        { n: 2,  k: "二", r: "ni",          kana: "に" },
        { n: 3,  k: "三", r: "san",         kana: "さん" },
        { n: 4,  k: "四", r: "shi / yon",   kana: "し・よん" },
        { n: 5,  k: "五", r: "go",          kana: "ご" },
        { n: 6,  k: "六", r: "roku",        kana: "ろく" },
        { n: 7,  k: "七", r: "shichi / nana", kana: "しち・なな" },
        { n: 8,  k: "八", r: "hachi",       kana: "はち" },
        { n: 9,  k: "九", r: "kyū / ku",    kana: "きゅう・く" },
        { n: 10, k: "十", r: "jū",          kana: "じゅう" }
      ],
      extra: [
        { n: 11,  k: "十一", r: "jū-ichi", note: "ten + one" },
        { n: 20,  k: "二十", r: "ni-jū",   note: "two tens" },
        { n: 100, k: "百",   r: "hyaku",   note: "one hundred" }
      ],
      tip: "Bigger numbers are built like Lego: 15 is jū-go (ten-five), 30 is san-jū (three-ten), 42 is yon-jū-ni."
    },

    /* ---------------------------------------------------------------- */
    {
      id: "judo-belts", type: "belts",
      jp: "級と段", romaji: "Kyū to Dan", title: "Judo belt ranks",
      lede: "Judo counts down through the coloured kyū grades, then up through the black-belt dan grades. Shown here is the Judo Canada system.",
      groups: [
        { label: "Kyū grades · coloured belts", items: [
          { c: ["#F4F2EC"], name: "White",  rank: "6th kyū", k: "六級", r: "rokkyū" },
          { c: ["#F2C230"], name: "Yellow", rank: "5th kyū", k: "五級", r: "gokyū" },
          { c: ["#E8772E"], name: "Orange", rank: "4th kyū", k: "四級", r: "yonkyū" },
          { c: ["#2E8B4E"], name: "Green",  rank: "3rd kyū", k: "三級", r: "sankyū" },
          { c: ["#2557B8"], name: "Blue",   rank: "2nd kyū", k: "二級", r: "nikyū" },
          { c: ["#6B4226"], name: "Brown",  rank: "1st kyū", k: "一級", r: "ikkyū" }
        ]},
        { label: "Dan grades · black belt and beyond", items: [
          { c: ["#1A1A1D"], name: "Black", rank: "1st dan", k: "初段", r: "shodan" },
          { c: ["#1A1A1D"], name: "Black", rank: "2nd – 5th dan", k: "二段〜五段", r: "nidan – godan" },
          { c: ["#C8202E", "#F4F2EC"], name: "Red & white", rank: "6th – 8th dan", k: "紅白帯", r: "kōhaku-obi" },
          { c: ["#C8202E"], name: "Red", rank: "9th – 10th dan", k: "赤帯", r: "aka-obi" }
        ]}
      ],
      note: "Juniors (about 6–14) also earn half-grade belts that join two colours, such as white-yellow or orange-green, between the full grades."
    },

    /* ---------------------------------------------------------------- */
    {
      id: "bjj-belts", type: "bjjbelts",
      jp: "帯の色", romaji: "Obi no iro", title: "Jiu jitsu belt ranks",
      lede: "Brazilian jiu jitsu has fewer belts and a longer road. Each belt can carry up to four stripes before the next promotion.",
      adults: [
        { c: "#F4F2EC", name: "White",  jp: "白 shiro",     age: "Any age", time: "Where everyone starts" },
        { c: "#2557B8", name: "Blue",   jp: "青 ao",        age: "16+", time: "2 years minimum at blue" },
        { c: "#6A3FA0", name: "Purple", jp: "紫 murasaki",  age: "16+", time: "1½ years minimum at purple" },
        { c: "#6B4226", name: "Brown",  jp: "茶 cha",       age: "18+", time: "1 year minimum at brown" },
        { c: "#1A1A1D", name: "Black",  jp: "黒 kuro",      age: "19+", time: "Degrees follow, years apart", bar: "#C8202E" }
      ],
      kids: [
        { c: ["#F4F2EC"], name: "White" },
        { c: ["#8E8E92", "#F4F2EC"], name: "Grey-white" },
        { c: ["#8E8E92"], name: "Grey" },
        { c: ["#8E8E92", "#1A1A1D"], name: "Grey-black" },
        { c: ["#F2C230", "#F4F2EC"], name: "Yellow-white" },
        { c: ["#F2C230"], name: "Yellow" },
        { c: ["#F2C230", "#1A1A1D"], name: "Yellow-black" },
        { c: ["#E8772E", "#F4F2EC"], name: "Orange-white" },
        { c: ["#E8772E"], name: "Orange" },
        { c: ["#E8772E", "#1A1A1D"], name: "Orange-black" },
        { c: ["#2E8B4E", "#F4F2EC"], name: "Green-white" },
        { c: ["#2E8B4E"], name: "Green" },
        { c: ["#2E8B4E", "#1A1A1D"], name: "Green-black" }
      ],
      degrees: [
        { c: ["#1A1A1D"], label: "Black belt", sub: "1st – 6th degree" },
        { c: ["#C8202E", "#1A1A1D"], label: "Coral, red-black", sub: "7th degree" },
        { c: ["#C8202E", "#F4F2EC"], label: "Coral, red-white", sub: "8th degree" },
        { c: ["#C8202E"], label: "Red belt", sub: "9th – 10th degree" }
      ],
      note: "Ages and minimum times follow IBJJF guidelines. Your instructor decides when you are ready."
    },

    /* ---------------------------------------------------------------- */
    {
      id: "dojo-words", type: "words",
      jp: "道場の言葉", romaji: "Dōjō no kotoba", title: "Words of the dojo",
      lede: "The commands you will hear every class, in the order you will hear them.",
      groups: [
        { label: "Opening the class", seq: true, items: [
          { k: "正座",     r: "Seiza",            e: "Kneel" },
          { k: "黙想",     r: "Mokusō",           e: "Close your eyes, breathe, settle" },
          { k: "黙想止め", r: "Mokusō yame",      e: "Open your eyes" },
          { k: "正面に礼", r: "Shōmen ni rei",    e: "Bow to the front" },
          { k: "先生に礼", r: "Sensei ni rei",    e: "Bow to the teacher" },
          { k: "お互いに礼", r: "Otagai ni rei",  e: "Bow to each other" },
          { k: "起立",     r: "Kiritsu",          e: "Stand up" }
        ]},
        { label: "On the mat", items: [
          { k: "始め",     r: "Hajime",     e: "Begin" },
          { k: "待て",     r: "Matte",      e: "Stop, wait" },
          { k: "それまで", r: "Sore made",  e: "That's all, finished" },
          { k: "参った",   r: "Maitta",     e: "I give up, tap out" },
          { k: "抑え込み", r: "Osaekomi",   e: "Hold-down is on" },
          { k: "解けた",   r: "Toketa",     e: "Hold-down is broken" }
        ]},
        { label: "Around the dojo", items: [
          { k: "道場",     r: "Dōjō",       e: "Place of the way, the training hall" },
          { k: "先生",     r: "Sensei",     e: "Teacher, one who went before" },
          { k: "畳",       r: "Tatami",     e: "Mat" },
          { k: "帯",       r: "Obi",        e: "Belt" },
          { k: "柔道着",   r: "Jūdōgi",     e: "Training uniform, the gi" },
          { k: "乱取り",   r: "Randori",    e: "Free practice, live rolling" },
          { k: "お願いします", r: "Onegaishimasu", e: "Said to a partner before training: please" },
          { k: "ありがとうございました", r: "Arigatō gozaimashita", e: "Said after: thank you" }
        ]}
      ]
    },

    /* ---------------------------------------------------------------- */
    {
      id: "nage-waza", type: "techniques",
      jp: "投技", romaji: "Nage-waza", title: "Twelve throws to know",
      lede: "Judo names describe the action. O means major, ko means minor, gari is a reap, barai a sweep, goshi the hip, nage a throw.",
      items: [
        { k: "大外刈", r: "O-soto-gari",    e: "Major outer reap",     f: "Foot" },
        { k: "大内刈", r: "O-uchi-gari",    e: "Major inner reap",     f: "Foot" },
        { k: "小内刈", r: "Ko-uchi-gari",   e: "Minor inner reap",     f: "Foot" },
        { k: "小外刈", r: "Ko-soto-gari",   e: "Minor outer reap",     f: "Foot" },
        { k: "出足払", r: "De-ashi-barai",  e: "Advancing foot sweep", f: "Foot" },
        { k: "膝車",   r: "Hiza-guruma",    e: "Knee wheel",           f: "Foot" },
        { k: "大腰",   r: "O-goshi",        e: "Major hip throw",      f: "Hip" },
        { k: "払腰",   r: "Harai-goshi",    e: "Sweeping hip throw",   f: "Hip" },
        { k: "背負投", r: "Seoi-nage",      e: "Shoulder throw",       f: "Hand" },
        { k: "体落",   r: "Tai-otoshi",     e: "Body drop",            f: "Hand" },
        { k: "内股",   r: "Uchi-mata",      e: "Inner thigh throw",    f: "Foot" },
        { k: "巴投",   r: "Tomoe-nage",     e: "Circle throw",         f: "Sacrifice" }
      ],
      note: "Every throw has three parts: 崩し kuzushi (break balance), 作り tsukuri (fit in), 掛け kake (execute)."
    },

    /* ---------------------------------------------------------------- */
    {
      id: "katame-waza", type: "ground",
      jp: "固技", romaji: "Katame-waza", title: "Groundwork",
      lede: "Holds, chokes and joint locks. The same positions jiu jitsu trains, under their original names.",
      groups: [
        { k: "抑込技", r: "Osaekomi-waza", label: "Hold-downs", items: [
          { k: "袈裟固",   r: "Kesa-gatame",        e: "Scarf hold" },
          { k: "横四方固", r: "Yoko-shihō-gatame",  e: "Side control" },
          { k: "縦四方固", r: "Tate-shihō-gatame",  e: "Mount" },
          { k: "上四方固", r: "Kami-shihō-gatame",  e: "North–south" },
          { k: "肩固",     r: "Kata-gatame",        e: "Shoulder hold" },
          { k: "浮固",     r: "Uki-gatame",         e: "Knee on belly" }
        ]},
        { k: "絞技", r: "Shime-waza", label: "Chokes", items: [
          { k: "裸絞",     r: "Hadaka-jime",        e: "Rear naked choke" },
          { k: "送襟絞",   r: "Okuri-eri-jime",     e: "Sliding collar choke" },
          { k: "片羽絞",   r: "Kata-ha-jime",       e: "Single wing choke" },
          { k: "並十字絞", r: "Nami-jūji-jime",     e: "Cross collar choke" },
          { k: "三角絞",   r: "Sankaku-jime",       e: "Triangle choke" },
          { k: "袖車絞",   r: "Sode-guruma-jime",   e: "Ezekiel choke" }
        ]},
        { k: "関節技", r: "Kansetsu-waza", label: "Joint locks", items: [
          { k: "腕挫十字固", r: "Ude-hishigi-jūji-gatame", e: "Armbar" },
          { k: "腕緘",       r: "Ude-garami",              e: "Americana / Kimura" },
          { k: "腕挫腕固",   r: "Ude-hishigi-ude-gatame",  e: "Straight armlock" },
          { k: "腕挫脇固",   r: "Ude-hishigi-waki-gatame", e: "Armpit lock" },
          { k: "腕挫三角固", r: "Ude-hishigi-sankaku-gatame", e: "Triangle armlock" }
        ]}
      ],
      note: "Tap early, tap often. Tapping is how we keep training partners for years."
    },

    /* ---------------------------------------------------------------- */
    {
      id: "two-names", type: "pairs",
      jp: "同じ技", romaji: "Onaji waza", title: "Same move, two names",
      lede: "Jiu jitsu grew out of judo. Most of what you learn on the ground already had a Japanese name a century ago.",
      items: [
        { a: "Armbar",              k: "腕挫十字固", r: "Jūji-gatame" },
        { a: "Rear naked choke",    k: "裸絞",       r: "Hadaka-jime" },
        { a: "Triangle choke",      k: "三角絞",     r: "Sankaku-jime" },
        { a: "Kimura",              k: "腕緘",       r: "Ude-garami (reverse)" },
        { a: "Americana",           k: "腕緘",       r: "Ude-garami" },
        { a: "Cross collar choke",  k: "十字絞",     r: "Jūji-jime" },
        { a: "Ezekiel choke",       k: "袖車絞",     r: "Sode-guruma-jime" },
        { a: "Arm triangle",        k: "肩固",       r: "Kata-gatame" },
        { a: "Mount",               k: "縦四方固",   r: "Tate-shihō-gatame" },
        { a: "Side control",        k: "横四方固",   r: "Yoko-shihō-gatame" },
        { a: "North–south",         k: "上四方固",   r: "Kami-shihō-gatame" },
        { a: "Knee on belly",       k: "浮固",       r: "Uki-gatame" }
      ],
      note: "The Kimura is named after judoka Masahiko Kimura, who used it to beat Hélio Gracie in Rio in 1951."
    },

    /* ---------------------------------------------------------------- */
    {
      id: "ukemi", type: "ukemi",
      jp: "受身", romaji: "Ukemi", title: "Learn to fall",
      lede: "Before anyone learns to throw, everyone learns to land. Ukemi means “receiving with the body”.",
      items: [
        { k: "後ろ受身",   r: "Ushiro-ukemi",      e: "Back breakfall",  d: "Sit back, round the spine, chin to chest, slap both arms at 45°." },
        { k: "横受身",     r: "Yoko-ukemi",        e: "Side breakfall",  d: "Swing the leg through, land on your side, one arm slaps the mat." },
        { k: "前受身",     r: "Mae-ukemi",         e: "Front breakfall", d: "Fall forward onto forearms and palms, head turned, body straight." },
        { k: "前回り受身", r: "Mae-mawari-ukemi",  e: "Rolling breakfall", d: "Roll diagonally shoulder to hip, finish with a side slap or stand up." }
      ],
      rules: [
        "Tuck your chin. Your head never touches the mat.",
        "Slap the mat to spread the impact, then let the arm stay down.",
        "Breathe out as you land."
      ]
    },

    /* ---------------------------------------------------------------- */
    {
      id: "principles", type: "principles",
      jp: "心", romaji: "Kokoro", title: "Principles we train by",
      lede: "Jigorō Kanō built judo on two ideas. The rest come from the wider Japanese martial tradition.",
      items: [
        { k: "精力善用", r: "Seiryoku zen'yō", e: "Maximum efficiency", d: "Use your energy in the best possible way. Technique over strength." },
        { k: "自他共栄", r: "Jita kyōei",      e: "Mutual welfare and benefit", d: "You and your partner both improve, or neither of you does." },
        { k: "柔よく剛を制す", r: "Jū yoku gō o seisu", e: "Softness controls hardness", d: "Give way to force, then redirect it. The root idea of 柔 jū." },
        { k: "初心",     r: "Shoshin",         e: "Beginner's mind", d: "Black belts keep training like white belts: open, curious, humble." },
        { k: "守破離",   r: "Shu-ha-ri",       e: "Learn, break, transcend", d: "Copy the form, test the form, then make it your own." },
        { k: "礼",       r: "Rei",             e: "Respect", d: "Every class starts and ends with a bow." }
      ]
    },

    /* ---------------------------------------------------------------- */
    {
      id: "lineage", type: "timeline",
      jp: "系譜", romaji: "Keifu", title: "From Tokyo to Clearwater",
      lede: "Judo and Brazilian jiu jitsu share one family tree.",
      items: [
        { y: "1882", t: "Jigorō Kanō founds the Kōdōkan in Tokyo, turning older jūjutsu schools into jūdō, “the gentle way”." },
        { y: "1904", t: "Mitsuyo Maeda, one of the Kōdōkan's top students, leaves Japan to show judo to the world." },
        { y: "1914", t: "Maeda arrives in Brazil and settles in Belém." },
        { y: "c.1917", t: "Maeda teaches a young Carlos Gracie. His brothers, Hélio among them, learn from Carlos." },
        { y: "1925", t: "Carlos opens the first Gracie academy in Rio de Janeiro." },
        { y: "1951", t: "Masahiko Kimura beats Hélio Gracie with the arm lock that now carries his name." },
        { y: "1964", t: "Judo becomes an Olympic sport at the Tokyo Games." },
        { y: "1993", t: "Royce Gracie wins the first UFC and jiu jitsu spreads around the world." },
        { y: "Today", t: "Both arts share one mat in Clearwater, BC." }
      ]
    },

    /* ---------------------------------------------------------------- */
    {
      id: "dojo-code", type: "code",
      jp: "道場訓", romaji: "Dōjō-kun", title: "The dojo code",
      lede: "Seven things every member, every age, agrees to.",
      items: [
        { k: "礼", t: "Bow when you step on the mat and when you step off." },
        { k: "清", t: "Clean gi, clean feet, short nails. Sandals stay off the tatami." },
        { k: "聴", t: "When the teacher speaks, stop and listen." },
        { k: "守", t: "Look after your partner. Their safety comes before your win." },
        { k: "柔", t: "Tap early, tap often, and let go the moment your partner taps." },
        { k: "助", t: "Help newer students. You were new once." },
        { k: "和", t: "What we learn here is for the mat and for self-defence only." }
      ]
    },

    /* ---------------------------------------------------------------- */
    {
      id: "come-train", type: "promo",
      jp: "稽古", romaji: "Keiko", title: "Come train with us",
      lede: "Jiu jitsu and judo for adults, teens and kids in Clearwater. No experience needed. Wear comfortable clothes and come try a class.",
      programs: ["Brazilian jiu jitsu", "Judo", "Kids classes"],
      cta: "Schedule, location and sign-up"
    }
  ]
};
