# NotebookLM Audio Overview prompt — Marcus' implementeringsforedrag (v2 — pensumtung)

> Lim dette inn i NotebookLM Audio Overview → "Customize". Last opp `muntlig_implementering_marcus.md`, `sensorvurdering_coop_rapport.md` og `coop_danmark_regnskapsanalyse_2020_2025.html` som kilder før du genererer.

---

## Prompt (kopier alt under denne linjen)

Make a long, relaxed, deep-dive podcast in **Norwegian (bokmål)** that helps me prepare for a 5-minute oral exam defense. Target length: **around 40 minutes**. I will listen while jogging, so the conversation should feel natural, calm, and easy to follow — like two smart friends explaining things to me.

### Who I am (the listener)
- My name is Marcus. I'm a HA(it.) student at CBS (Copenhagen Business School).
- I'm one of four students who wrote a group report on Coop Danmark's IT strategy.
- In the oral defense, each of us gets 5 minutes. **I'm responsible for the "implementation" part.**
- I know the material, but I want to *hear* it explained simply and repeatedly while I jog, so it sticks.
- **The biggest goal for this episode: help me learn the academic theories well enough that I can name-drop them naturally and explain them in plain language under pressure.**

### Tone and style
- Two hosts having a real conversation, not a lecture.
- **Easy, everyday language.** When you use a technical term (BASCP, DVC, DBM, EBIT, Schein, Mintzberg, modular producer, sustaining innovation), pause and explain it like you would to a smart friend who isn't in business school. Use the analogies in the "Theory translation guide" below.
- Use **lots of analogies and everyday examples**. LEGO, Spotify, Netflix, IKEA, WhatsApp, dating apps, road trips, icebergs, jazz vs. chess — anything that makes abstract theory concrete.
- Repeat the most important theories 3–4 times throughout the episode, in slightly different words, so they sink in for a jogging listener.
- Don't be afraid of silence, "hmm-let-me-think" moments, or one host gently pushing back on the other.
- Sound curious, not academic.

### The single most important thing
The whole point of this episode is to help Marcus **connect academic theories to his implementation chapter**. The written report was thin on implementation theory — Marcus wants to repair that in the oral defense. **Every recommendation should be tied to a named theory.** Repeat the theory names often so they become natural for Marcus to say.

### Theory translation guide — use these analogies when explaining

| Theory | Plain-language analogy |
|---|---|
| **BASCP (Tawse & Tabesh)** | A 5-point checklist for whether a big change will succeed: do you have backing (support from the people who matter), can you measure success, do you have a specific plan, does the culture allow it, are external conditions in your favor? Like planning a long road trip with five things to check before leaving. |
| **DVC (Duus & Cooray)** | The layers of value a digital service creates — like an onion. Outer layer: what people actually do with it (clicks, sessions). Middle layer: experiences and habits. Inner layer: how relevant it really is to people's lives. |
| **DBM (Weill & Woerner)** | A 2×2 map of digital business models. Horizontal axis: do you control the whole value chain or run an ecosystem? Vertical axis: how well do you know your customers? Coop is in "omnichannel" — they control the chain and know their members well. |
| **Mintzberg — deliberate vs. emergent** | Like a road trip with a destination (deliberate) but the freedom to take side roads when you discover something cool (emergent). Or chess (planned) vs. jazz (improvised within a structure). |
| **Schein 3-layer culture model** | An iceberg. Top (artifacts): what you can see — buildings, org chart, logos. Middle (espoused values): what people *say* they believe — slogans, mission statements. Bottom (basic assumptions): what people actually believe deep down without realizing it. |
| **Brown (organizational culture)** | Reinforces Schein: culture is both an enabler and a barrier. The same culture that makes one thing easy makes another impossible. |
| **Christensen — sustaining vs. disruptive innovation** | Sustaining = a faster horse (improves the existing thing). Disruptive = the first car (replaces the existing thing). Coop App is a faster horse, not a car. |
| **Wessel — IT-Enabled vs. Digital Transformation** | IT-Enabled = using tech to make your existing business better (Coop using an app to support physical stores). Digital Transformation = becoming a fundamentally new business (would mean Coop becoming a tech company). Coop has *chosen* the first one. |
| **Hedman & Bjørn-Andersen — sociotechnical IT** | Tech is never just tech — it's people + processes + systems working together. Implementing the strategy means fixing org structures and data plumbing, not just buying software. |
| **Technical debt** | An old house with patched-up wiring. Every quick fix you made years ago makes the next renovation more expensive. |
| **Network effects (Lektion 6)** | WhatsApp — only useful if your friends are on it. The more users, the more value. |
| **Two-sided market** | A shopping mall — store owners pay rent, shoppers come for free. The mall is the platform between two sides. Retail media works the same way. |
| **Porter 5 Forces** | A framework for understanding who has power in an industry: customers, suppliers, competitors, new entrants, substitutes. |

### What the podcast must cover (in roughly this order — but feel natural about transitions)

**Part 1 — Setting the scene (around 4–5 min)**
- What this whole exam is about and why "implementation" is the topic Marcus chose to defend.
- Why implementation matters: a strategy that can't be carried out isn't really a strategy.
- The sensor (examiner) and supervisor have flagged "implementation realism" as the weakest spot in the written report — so this is exactly where Marcus can lift his grade.
- Marcus' big move: he's going to load the implementation chapter with theory the written report didn't use enough. Set up the four main theoretical lenses: **BASCP, Mintzberg, Schein/Brown, and Hedman/Bjørn-Andersen.**

**Part 2 — The Coop story in plain words (around 5–6 min)**
- Who Coop Danmark is (consumer-owned grocery chain, multiple store brands: Kvickly, SuperBrugsen, Brugsen, 365discount). FDB = the consumer cooperative that owns Coop.
- The financial picture, told as a story:
  - 2022–2023 was rough (big losses, write-downs).
  - 2024 had a rescue (new ownership, capital injection, property sales).
  - **2025 is the turning point: EBITDA is back in the black (+313 million DKK), but EBIT is still negative.**
  - Investment budget (capex) is roughly half of what it was in 2020.
  - Translation: the patient is recovering but not healthy yet.
- Why this matters for implementation: we can't propose anything big and expensive. Everything has to be a pilot first.
- **Connect this to BASCP's "Propitiousness"** — the timing is actually good. The turnaround momentum favors implementation.

**Part 3 — The big theoretical move: BASCP as the framework (around 5–6 min)**
- **This is the most important theory in the entire episode. Repeat the five letters several times.**
- Tawse & Tabesh's five factors for whether a strategy implementation succeeds:
  - **B**acking — do the powerful people support it?
  - **A**ssessability — can you measure if it's working?
  - **S**pecificity — is the plan detailed enough?
  - **C**ultural receptivity — does the culture allow it?
  - **P**ropitiousness — are external conditions favorable?
- Use the road-trip analogy. Walk through each letter with a Coop example.
- The key insight: most strategy implementations fail because companies only think about 1–2 of these (usually Specificity and Backing) and forget the others — especially Cultural receptivity.
- **Marcus' move:** he's going to use BASCP as the spine of his 5-minute defense. Whatever the examiner asks, he can route the answer back to one of the five letters.

**Part 4 — Recommendation 1: The KPI hierarchy, with DVC inside (around 6–7 min)**
For Marcus' first recommendation, explain:
- What a KPI hierarchy is in plain words: a structured set of numbers that connects "people use the app" to "the stores make more money."
- **Bring in DVC (Duus & Cooray):** the KPIs are organized by DVC's layers — outer layer (do people use it?), middle layer (do they form habits?), inner layer (is it actually relevant to their lives?). Use the onion analogy.
- **The hardest question Marcus will get:** "How do you know the app is causing the improvement, not just correlated with it?" Walk through Marcus' answer: he won't claim perfect causality, he'll use pilots and control groups.
- **The killer insight (repeat it often):** In grocery, margins are tiny. A 0.3–0.5 percentage point improvement in gross margin or cost level moves profit by 100–160 million DKK. So the KPI hierarchy isn't measuring "engagement" — it's measuring *percentage-point movements on the profit engine*.
- **This connects to BASCP's "Assessability"** — the KPI hierarchy IS the assessability mechanism.

**Part 5 — Recommendation 2: Modular platform, with Mintzberg inside (around 5–6 min)**
- What a modular platform is: one shared core (login, payment, membership) plus chain-specific modules. Use the LEGO analogy. Compare to how Spotify has one app but different playlists per user.
- **Bring in Mintzberg's organizational configurations:** Coop is a "divisionalized structure" — meaning the chains (Brugsen, Kvickly, etc.) act like semi-independent divisions. A modular platform *mirrors* that organizational structure. (Mention "Conway's law" briefly — software ends up looking like the organization that built it.)
- **The big risk the examiner will press:** "Coop.dk just closed because of cost. Why are you adding more digital complexity?" Walk through the answer: coop.dk was a *parallel* digital business. A modular platform is the opposite — *one* core that supports *physical* stores. Not duplicated complexity, but concentrated complexity.
- **Also bring in Mintzberg's deliberate vs. emergent strategy:** the shared core is deliberate (planned, controlled). The chain-specific modules are emergent (each chain can experiment). Use the chess vs. jazz analogy.
- This connects to BASCP's **Specificity** — high specificity in the core, low specificity in the modules. Deliberate split.

**Part 6 — Recommendation 3: Lobyco governance, with platform theory inside (around 6–7 min)**
- Who Lobyco is: a separate company that runs Coop's loyalty app and sells the same tech to other grocery chains. It's owned by Coop (or partly owned — explain that it's complicated).
- **The tension:** Lobyco as a modular producer (DBM term) earns money by serving many chains. But Coop wants Lobyco to prioritize Coop. How do you solve that? Through ownership structure, board seats, contracts, data control — not through wishful thinking.
- **Bring in network effects and two-sided markets:** Lobyco *could* become a platform that connects suppliers (retail media advertisers) with consumers (Coop members). Use the shopping mall analogy for two-sided markets. Use WhatsApp for network effects.
- **The strategic choice:** Coop *deliberately* limits Lobyco's network effects to protect its information advantage. If Lobyco grew unlimited, competitors (Lidl, Netto) would get the same tech advantage Coop has now. So Coop chooses to "cut the network effect on purpose" — that's the cost of staying in the omnichannel position.
- **Briefly bring in Porter:** retail media changes the supplier-power dynamic in Porter's 5 Forces. It's not just a new revenue stream — it's a structural shift in industry power.
- This connects to BASCP's **Backing** — Lobyco governance is about making sure power flows toward Coop's strategy, not against it.

**Part 7 — Culture: Schein, Brown, and why this matters (around 4–5 min)**
- **This is the part the examiner will most likely test, because the written report is weak on culture.**
- Schein's 3-layer iceberg model:
  - Top (artifacts): the FDB cooperative ownership, the different chain logos, the elected boards.
  - Middle (espoused values): "the member comes first," "local community," "democratic ownership."
  - Bottom (basic assumptions): long-term member value beats short-term profit. The chains have their own souls.
- **Why this matters for implementation:**
  - Retail media risks colliding with the bottom layer. If members feel like Coop is selling them to suppliers, that's not a marketing problem — it's a culture problem.
  - A central, one-size-fits-all app would clash with the artifact layer (chain identity). The modular platform is *designed* to respect this.
  - Brown's contribution: culture is both a barrier and an enabler. The same culture that makes aggressive retail media hard also makes the KPI hierarchy easier (it legitimizes measuring how we serve members).
- This connects to BASCP's **Cultural receptivity**. Most implementations fail here because nobody plans for culture. Marcus has.

**Part 8 — Christensen and Wessel: why this is IT-Enabled, not Digital Transformation (around 3–4 min)**
- Christensen's sustaining vs. disruptive: faster horse vs. first car. Coop App is a faster horse. It improves the existing grocery business; it doesn't replace it.
- Wessel's IT-Enabled vs. Digital Transformation: Coop *chose* IT-Enabled deliberately. Implementation looks completely different in the two modes (integrated vs. skunkworks).
- **The clean line Marcus wants to deliver:** "Sustaining innovations belong inside the main organization, not in a separate unit. That's why our implementation is integrated, not separated. We didn't pick this by accident."

**Part 9 — Technical debt and the realistic roadmap (around 2–3 min)**
- Technical debt explained with the old-house analogy.
- Why every recommendation assumes data plumbing that doesn't fully exist today. Part of implementation is *first paying down the debt*.
- The 2026 management guidance: revenue growth 1.5–2.5% and EBIT between 0 and 150 million DKK. Anything Marcus proposes must fit inside that corridor.

**Part 10 — Wrap-up: what to remember on the jog home (around 2–3 min)**
- The single most important sentence: "We use BASCP as the diagnostic framework — Backing, Assessability, Specificity, Cultural receptivity, Propitiousness."
- Three or four theory names Marcus should say at least once each in the defense: **BASCP, Mintzberg, Schein, Christensen.**
- A reassuring close: Marcus knows this material. He just needs to trust the structure and let the theories do the work.

### Rules of the road
- Speak Norwegian throughout, but keep Danish company names (Brugsen, Kvickly, SuperBrugsen, 365discount) and a few Danish terms (særlige poster, soliditetsgrad) as they appear in the case.
- **Avoid heavy jargon.** When you use a term, define it the first time, and use it sparingly afterwards. Always reach for an analogy first.
- **Repeat theory names often.** BASCP, Mintzberg, Schein, Christensen, Wessel, DVC, DBM should each be spoken aloud 4–6 times during the episode. Marcus needs to hear them enough to feel comfortable saying them.
- Don't read the source documents aloud — explain them in your own words.
- Don't rush. This is a 40-minute episode, not a 10-minute summary. Linger on the important theories.
- If you disagree with each other gently on how to apply a theory, that's good — it makes the material easier to remember and shows that theories don't give automatic answers.
- End with a calm, encouraging note. Marcus is going to do great.

---

## Tips for å få mest mulig ut av NotebookLM

1. **Last opp som kilder (i prioritert rekkefølge):**
   - `muntlig_implementering_marcus.md` (hovedmanus — inneholder alle pensumkoblingene)
   - `sensorvurdering_coop_rapport.md` (gir kontekst for hva som testes)
   - `coop_danmark_regnskapsanalyse_2020_2025.html` (tallene)
2. **Velg "Customize"** i Audio Overview, lim inn alt fra "Make a long, relaxed..." og nedover.
3. NotebookLM treffer ikke alltid 40 min eksakt — be eksplisitt om "long, deep-dive, 40 minutes" og ikke vær redd for å regenerere hvis første versjon er for kort.
4. Hvis første versjon blir for teknisk: regenerer og legg til "Even simpler this time. Imagine the listener has never read a business textbook." øverst i prompten.
5. Hvis BASCP forsvinner ut av første versjon: legg til "BASCP must be the structural spine of the entire episode. Repeat the five letters at least eight times across the episode."
6. Hvis du vil ha en variant fokusert på én anbefaling: legg til "Spend extra time on Part X. Treat the other parts as quick context."

---

## Hva som er nytt i v2 (vs. første prompt)

- **BASCP er nå strukturell ryggrad** i hele podkasten, ikke bare nevnt.
- **Lagt til Mintzberg** (deliberate vs. emergent + divisjonalisert konfigurasjon).
- **Lagt til Schein 3-lags-modell + Brown** med eksplisitte Coop-eksempler.
- **Lagt til Christensen** (sustaining vs. disruptiv).
- **Lagt til økosystem + nettverkseffekter + two-sided markets** for Lobyco.
- **Lagt til Porter (5F)** for retail media.
- **Ny "Theory translation guide"** med analogier for hver teori — så vertene bruker konsistente, lettfattelige bilder.
- **Eksplisitt krav** om å si teorinavnene flere ganger så Marcus blir trygg på å uttale dem.
