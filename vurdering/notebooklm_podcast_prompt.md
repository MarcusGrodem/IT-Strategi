# NotebookLM Audio Overview prompt — Marcus' implementeringsforedrag

> Lim dette inn i NotebookLM Audio Overview → "Customize". Last opp `muntlig_implementering_marcus.md`, `sensorvurdering_coop_rapport.md` og gjerne `coop_danmark_regnskapsanalyse_2020_2025.html` som kilder før du genererer.

---

## Prompt (kopier alt under denne linjen)

Make a long, relaxed, deep-dive podcast in **Norwegian (bokmål)** that helps me prepare for a 5-minute oral exam defense. Target length: **around 40 minutes**. I will listen while jogging, so the conversation should feel natural, calm, and easy to follow — like two smart friends explaining things to me.

### Who I am (the listener)
- My name is Marcus. I'm a HA(it.) student at CBS (Copenhagen Business School).
- I'm one of four students who wrote a group report on Coop Danmark's IT strategy.
- In the oral defense, each of us gets 5 minutes. **I'm responsible for the "implementation" part.**
- I know the material, but I want to *hear* it explained simply and repeatedly while I jog, so it sticks.

### Tone and style
- Two hosts having a real conversation, not a lecture.
- **Easy, everyday language.** When you use a technical term (EBIT, EBITDA, modular producer, IT-Enabled Transformation, technical debt), pause and explain it like you would to a smart friend who isn't in business school.
- Use **analogies and everyday examples**. Comparisons to other companies (Netflix, Spotify, IKEA, local grocery stores) are very welcome.
- Repeat the most important points 2–3 times throughout the episode, in slightly different words, so they sink in for a jogging listener.
- Don't be afraid of silence, "hmm-let-me-think" moments, or one host pushing back gently on the other.
- Sound curious, not academic.

### What the podcast must cover (in roughly this order — but feel natural about transitions)

**Part 1 — Setting the scene (around 5–7 min)**
- What this whole exam is about and why "implementation" is the topic Marcus chose to defend.
- Why implementation matters: a strategy that can't be carried out isn't really a strategy.
- The sensor (examiner) and supervisor have flagged "implementation realism" as the weakest spot in the written report — so this is exactly where Marcus can lift his grade.

**Part 2 — The Coop story in plain words (around 6–8 min)**
- Who Coop Danmark is (consumer-owned grocery chain, multiple store brands: Kvickly, SuperBrugsen, Brugsen, 365discount).
- The financial picture, told as a story:
  - 2022–2023 was rough (big losses, write-downs).
  - 2024 had a rescue (new ownership, capital injection, some property sales).
  - **2025 is the turning point: EBITDA is back in the black (+313 million DKK), but EBIT is still negative.**
  - Investment budget (capex) is roughly half of what it was in 2020.
  - Translation: the patient is recovering but not healthy yet.
- Why this matters for implementation: we can't propose anything big and expensive. Everything has to be a pilot first.

**Part 3 — The three recommendations explained simply (around 8–10 min)**
For each, explain in plain language what it is and what implementing it really means in practice:

1. **A KPI hierarchy** (a structured set of measurements). Why? Because right now Coop probably measures the app on "how many people use it" — not "does the app actually help the stores make money?". The implementation challenge is connecting app data to store cash registers, which is harder than it sounds.
2. **A modular platform with chain-specific modules.** One shared core (login, payment, membership) plus modules tailored to each store brand. Compare to LEGO or to how Spotify has one app but different playlists per user.
3. **"Coop-first" governance of Lobyco** (Lobyco is a separate company that runs Coop's loyalty app and sells the same tech to other grocery chains). The tension: Lobyco makes money by selling to many customers, but Coop wants Lobyco to prioritize Coop. How do you solve that? Through ownership structure, board seats, and contracts — not through wishful thinking.

**Part 4 — The killer insight: margin sensitivity (around 4–5 min)**
- In grocery, margins are tiny. A 0.3–0.5 percentage point improvement in gross margin or cost level moves profit by 100–160 million DKK.
- That means the app doesn't need to be revolutionary — it just needs to push a few small numbers in the right direction.
- This is the language Marcus should use in his defense: not "the app is engaging" but "the app moves the margin needle by X percentage points."
- Repeat this point. It's the single most important thing.

**Part 5 — Technical debt and why it matters (around 4–5 min)**
- Explain technical debt with an analogy (an old house with patched-up wiring you keep meaning to fix).
- Coop's specific debt: old cash register systems, no clean connection between membership data and store transactions, weak APIs to Lobyco.
- Why it matters: every recommendation assumes you can connect data that today doesn't connect. Part of implementing the strategy is *first paying down the debt*.

**Part 6 — Wessel's framework, made simple (around 3–4 min)**
- Two ways a company can change with technology:
  - **IT-Enabled Transformation**: use tech to make the existing business better. Coop using an app to support physical stores.
  - **Digital Transformation**: tech creates a whole new business. Like if Coop turned Lobyco into a standalone tech company.
- Coop is doing the first one *on purpose*. That's a strategic choice. Explain why this matters for how implementation should be organized.

**Part 7 — A realistic roadmap (around 3–4 min)**
- Pilot first (on one chain, probably 365discount), measure for 6 months, then scale.
- The 2026 management guidance: revenue growth 1.5–2.5% and EBIT between 0 and 150 million DKK. Anything Marcus proposes has to fit inside that corridor.
- Why "go big or go home" is the wrong answer here.

**Part 8 — What the examiner will ask, and how to handle it (around 3–4 min)**
Walk through 3–4 likely tough questions and what a confident answer sounds like:
- "How do you actually know the app is causing the improvement?"
- "Aren't you just adding cost and complexity to a company that's already losing money?"
- "If Lobyco is supposed to be a modular producer that earns from breadth, why limit it to Coop?"
- "What if your pilot fails?"

**Part 9 — Wrap-up (around 2–3 min)**
- Three sentences Marcus should remember to say in the defense.
- A reassuring close: he knows this material, he just needs to trust the structure.

### Rules of the road
- Speak Norwegian throughout, but it's fine to keep Danish company names and a few Danish terms (Brugsen, Kvickly, særlige poster) as they appear in the case.
- **Avoid heavy jargon.** When you use a term, define it the first time, and use it sparingly afterwards.
- Don't read the source documents aloud — explain them in your own words.
- Don't rush. This is a 40-minute episode, not a 10-minute summary. Linger on the important points.
- If you disagree with each other gently, that's good — it makes the material easier to remember.
- End with a calm, encouraging note. Marcus is going to do great.

---

## Tips for å få mest mulig ut av NotebookLM

1. **Last opp som kilder:**
   - `muntlig_implementering_marcus.md` (hovedmanus)
   - `sensorvurdering_coop_rapport.md` (sensorens vurdering — gir kontekst for hva som testes)
   - `coop_danmark_regnskapsanalyse_2020_2025.html` (tallene)
   - Eventuelt selve rapporten hvis du har den som PDF/MD
2. **Velg "Customize"** i Audio Overview, lim inn alt fra "Make a long, relaxed..." og nedover.
3. NotebookLM treffer ikke alltid 40 min eksakt — be eksplisitt om "long, deep-dive, 40 minutes" og ikke vær redd for å regenerere hvis første versjon er for kort.
4. Hvis første versjon blir for teknisk: regenerer og legg til "Even simpler this time. Imagine the listener has never taken a business class." øverst i prompten.
5. Hvis du vil ha mer fokus på et bestemt tema (f.eks. mer om Lobyco-spenningen): legg til "Spend extra time on Part 3, recommendation 3 (Lobyco governance)."
