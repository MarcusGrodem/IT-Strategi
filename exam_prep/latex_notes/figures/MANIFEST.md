# Figure Manifest

This manifest lists every figure extracted from the lecture slides. Each entry gives the lecture, source page, what the figure shows, and when it is appropriate to cite the figure in the exam-prep LaTeX notes.

Figures were rendered at 200 DPI from the original lecture PDFs in `/slides/` using PyMuPDF. The renderer is `_batch_extract.py` in this directory.

Tool used: PyMuPDF (`fitz`) — the rendering script lives next to the figures. Poppler (`pdftoppm`) is installed but the Read tool's PDF preview wouldn't find it, so all rendering was done via PyMuPDF.

---

## Lecture 1 — Introduktion til IT-strategi

### lec01-makro-meso-mikro-matrix.png
- **Lecture:** 1 — Introduktion
- **Source page:** 15 of `260203_Lektion 1_Introduktion_IT-strategi-1.pdf`
- **What it shows:** The course overview matrix that positions every topic on two axes: analysis unit (Makro / Meso / Mikro) and focus (Teknologi / Forretning).
- **When to cite:** When introducing the scope of the course or positioning a specific analytical lens (e.g. "this section operates at the meso/forretning level").

### lec01-mintzberg-5ps-strategy.png
- **Lecture:** 1 — Introduktion
- **Source page:** 17 of `260203_Lektion 1_Introduktion_IT-strategi-1.pdf`
- **What it shows:** Mintzberg's 5 Ps of strategy (Plan / Ploy / Position / Pattern / Perspective) laid out on an Instrumentelle ↔ Symbolske perspektiver continuum, with Porter (1996), Rumelt (2011), and the imitation/mimesis pole labelled.
- **When to cite:** When discussing definitions of strategy, when justifying which lens you adopt, or when contrasting Porter's positioning view with Mintzberg's emergent/symbolic view.

### lec01-chen-narrow-vs-broad-digital-strategy.png
- **Lecture:** 1 — Introduktion
- **Source page:** 19 of `260203_Lektion 1_Introduktion_IT-strategi-1.pdf`
- **What it shows:** Chen et al. (2010) on the spectrum from a narrow ("snæver") to a broad ("bred") understanding of digital strategy, with the IT-centric → Business-centric → Organisational-level → Digital → Digital X continuum, and Bharadwaj's (2013) definition pinned at the broad end.
- **When to cite:** When unpacking what counts as "digital strategy" versus "IT strategy", or when arguing that the course adopts a broad understanding.

### lec01-it-strategy-in-context.png
- **Lecture:** 1 — Introduktion
- **Source page:** 20 of `260203_Lektion 1_Introduktion_IT-strategi-1.pdf`
- **What it shows:** IT-strategi placed at the centre with three surrounding domains — IT-projektledelse, Organisationers opbygning og funktion, and IT-forandringsledelse — split by the Økonomi-blok / IT-blok line.
- **When to cite:** When situating IT strategy within the wider organisationsfagblok and arguing why human/organisational aspects matter for strategy execution.

---

## Lecture 2 — Strategisk analyse (del I) og typiske strategiske virkemidler

### lec02-pestel-and-forecasting.png
- **Lecture:** 2 — Strategisk analyse I
- **Source page:** 8 of `170226_Lektion 2_Strategisk analyse (del I) og typiske strategiske virkemidler_IT-strategi-1.pdf`
- **What it shows:** PESTEL (Politisk / Økonomisk / Socialt / Teknologi / Klima og Miljø / Lovgivning) alongside Johnson et al.'s diagram of forecasting (market/nonmarket, megatrends, weak signals) and scenario analysis as macro-environment tools.
- **When to cite:** Macro-environment analysis; explaining how PESTEL feeds into forecasting and scenario planning.

### lec02-forecasting-under-uncertainty.png
- **Lecture:** 2 — Strategisk analyse I
- **Source page:** 16 of `170226_Lektion 2_Strategisk analyse (del I) og typiske strategiske virkemidler_IT-strategi-1.pdf`
- **What it shows:** Johnson et al. (2017) Figure 2.8 — three forecasting approaches plotted against increasing uncertainty: (i) Single-point forecast (low uncertainty), (ii) Range forecast with probability bands (Unlikely / Possible / Probable / Possible / Unlikely), and (iii) Alternative futures A / B / C (high uncertainty).
- **When to cite:** When discussing how strategic forecasting is chosen based on level of uncertainty — single-point, interval/range, or scenario-based "alternative futures" forecasting; useful alongside megatrends, inflexion points and weak signals.

### lec02-porter-five-forces.png
- **Lecture:** 2 — Strategisk analyse I
- **Source page:** 20 of `170226_Lektion 2_...pdf`
- **What it shows:** Porter's Five Forces (Danish: Nye indtrængere / Leverandørernes forhandlingskraft / Købernes forhandlingskraft / Substituerende produkter / Rivalisering).
- **When to cite:** Industry-level competitive analysis; sector / industry / market evaluation.

### lec02-industry-life-cycle.png
- **Lecture:** 2 — Strategisk analyse I
- **Source page:** 28 of `170226_Lektion 2_...pdf`
- **What it shows:** Johnson et al.'s industry life cycle (Development → Growth → Shake-out → Maturity → Decline) with the typical state of the five forces and competitive dynamics in each stage.
- **When to cite:** When the lifecycle stage of the industry matters for the strategic recommendation (e.g. why grocery retail has very different forces from a high-growth digital service).

### lec02-vrio-decision-matrix.png
- **Lecture:** 2 — Strategisk analyse I
- **Source page:** 36 of `170226_Lektion 2_...pdf`
- **What it shows:** The VRIO ladder (Valuable → Rare → Inimitable → Organised) with the four resulting competitive positions (vanskelig konkurrencesituation → ligeværdig → midlertidig fordel → uudnyttet fordel → bæredygtig konkurrencefordel).
- **When to cite:** Resource-based-view analysis of an organisation's resources/capabilities and the durability of competitive advantage.

### lec02-porter-value-chain.png
- **Lecture:** 2 — Strategisk analyse I
- **Source page:** 37 of `170226_Lektion 2_...pdf`
- **What it shows:** Porter's classic value chain — primary activities (Inbound logistics → Operations → Outbound logistics → Marketing & Sales → Service) and support activities (Firm infrastructure, HRM, Technology development, Procurement) with margins.
- **When to cite:** Internal value analysis; serves as the baseline against which Rosenstand & Baiyere's Digital Value Chain is contrasted.

### lec02-swot.png
- **Lecture:** 2 — Strategisk analyse I
- **Source page:** 39 of `170226_Lektion 2_...pdf`
- **What it shows:** Classic SWOT (Styrker / Svagheder / Muligheder / Trusler) split by Interne vs Eksterne forhold.
- **When to cite:** When synthesising the macro, industry, and internal analyses into a single strategic picture.

### lec02-five-building-blocks-digital-transformation.png
- **Lecture:** 2 — Strategisk analyse I
- **Source page:** 41 of `170226_Lektion 2_...pdf`
- **What it shows:** Ross et al.'s Five Building Blocks of Digital Transformation: Operational Backbone, Shared Customer Insights, Digital Platform, Accountability Framework, External Developer Platform.
- **When to cite:** When discussing the foundational digital capabilities a company needs in place before — or alongside — digital strategy execution.

---

## Lecture 3 — Digitale forretningsmodeller

### lec03-johnson-four-building-blocks.png
- **Lecture:** 3 — Digitale forretningsmodeller
- **Source page:** 10 of `260224_Lektion 3_Digitale forretningsmodeller-1.pdf`
- **What it shows:** Johnson et al.'s (2008) traditional business-model diagram with the Customer Value Proposition (Target Customer + Job to be done + Offering) connected to Profit Formula, Key Resources, and Key Processes.
- **When to cite:** When defining "what is a business model?" before introducing digital business models; baseline for the Weill & Woerner contrast.

### lec03-adjustment-vs-reinvention-curve.png
- **Lecture:** 3 — Digitale forretningsmodeller
- **Source page:** 17 of `260224_Lektion 3_...pdf`
- **What it shows:** Johnson et al. graph contrasting a "justeret forretningsmodel" (incremental adjustment) with a "ny forretningsmodel" (genuine reinvention) over time, plus the four diagnostic questions for whether reinvention is warranted.
- **When to cite:** When arguing whether a case requires incremental change or a fundamentally new business model.

### lec03-weill-woerner-digital-business-model-framework.png
- **Lecture:** 3 — Digitale forretningsmodeller
- **Source page:** 24 of `260224_Lektion 3_...pdf`
- **What it shows:** Weill & Woerner's (2018) Digital Business Model Framework — the 2×2 matrix of Business design (Value chain ↔ Ecosystem) × Knowledge of end customer (Partial ↔ Complete) with the four archetypes Supplier, Modular producer, Omnichannel, and Ecosystem driver, populated with examples.
- **When to cite:** Core DBM classification tool. Use whenever placing a firm (e.g. Coop) in one of the four quadrants or arguing about strategic moves between them.

### lec03-business-model-canvas.png
- **Lecture:** 3 — Digitale forretningsmodeller
- **Source page:** 30 of `260224_Lektion 3_...pdf`
- **What it shows:** Osterwalder & Pigneur's Business Model Canvas with the nine blocks (Key Partners, Key Activities, Key Resources, Value Proposition, Customer Relationships, Channels, Customer Segments, Cost Structure, Revenue Streams) and arrows highlighting how Value Proposition links every block.
- **When to cite:** When asked to analyse or design a firm's business model. Especially useful as the structural skeleton of the report's strategic recommendation.

### lec03-business-model-canvas-airbnb.png
- **Lecture:** 3 — Digitale forretningsmodeller
- **Source page:** 31 of `260224_Lektion 3_...pdf`
- **What it shows:** A worked example of the BMC applied to Airbnb — useful illustration of how each block is populated for a digital business.
- **When to cite:** As a concrete reference when teaching how to fill in the canvas or when comparing Coop's blocks to a platform-style firm.

---

## Lecture 4 — Strategi og digital transformation

### lec04-digital-transformation-vs-it-enabled.png
- **Lecture:** 4 — Digital transformation
- **Source page:** 11 of `260305_Lektion 4_Digital transformation_IT-strategi (1).pdf`
- **What it shows:** Wessel et al.'s (2021) two-circle diagram showing Digital Transformation as redefinition of value proposition + emergence of new organisational identity, versus IT-Enabled Organisational Transformation as digital tech reinforcing an existing value proposition and identity.
- **When to cite:** When the distinction between DT and IT-enabled OT is load-bearing for the argument (e.g. determining what kind of change Coop is actually pursuing).

### lec04-wessel-transformation-full-model.png
- **Lecture:** 4 — Digital transformation
- **Source page:** 19 of `260305_Lektion 4_...pdf`
- **What it shows:** "Det store billede" — Wessel et al.'s full process model: Technological Change (Environmental & Organisational context) → Transformation Agenda (Existing Org Identity → New Identity Claim) → Transformation Activity (Digital Technology ↔ Value Proposition) ↔ Imposition & Reconciliation (Work Practice Change ↔ Reconciliation Action) → emergence of New / Reinforced Organisational Identity.
- **When to cite:** Whenever applying Wessel et al.'s framework end-to-end to a case. This is the canonical lec-4 figure.

### lec04-kemp-situating-ai-grounding-bounding-recasting.png
- **Lecture:** 4 — Digital transformation
- **Source page:** 24 of `260305_Lektion 4_...pdf`
- **What it shows:** Kemp's (2024) three "situating activities" for capturing strategic value from AI — Grounding, Bounding, and Recasting — with definitions and the broader claim that situating AI means contextualising AI's agency in a firm's experiential, relational, and strategic systems.
- **When to cite:** When the case involves AI adoption and the question is "how does a firm move from AI hype to actual strategic advantage?"

### lec04-kemp-situated-ai-table.png
- **Lecture:** 4 — Digital transformation
- **Source page:** 25 of `260305_Lektion 4_...pdf`
- **What it shows:** Kemp's table comparing the three situating activities by Definition, Strategic Limitation of AI Addressed, Dimension of Human Agency, and Examples of Orchestrated Activities.
- **When to cite:** Companion to the previous figure; useful as concrete reference for what each activity looks like operationally.

---

## Lecture 5 — Digital innovation, disruption og strategier

### lec05-digital-innovation-strategy-framework.png
- **Lecture:** 5 — Digital innovation, disruption
- **Source page:** 12 of `10032026_Lektion 5_Digital innovation disruption og strategier (1).pdf`
- **What it shows:** A 2×2 Digital Innovation Strategy Framework with axes Invent NEW vs Enhance EXISTING and INTERNAL vs EXTERNAL Innovation, populated with sub-themes (Business Operations / Employee Experience / Business Model / Customer Facing).
- **When to cite:** When classifying a firm's innovation portfolio or recommending an innovation strategy along the internal/external × new/existing axes.

### lec05-innovation-typologies.png
- **Lecture:** 5 — Digital innovation, disruption
- **Source page:** 14 of `10032026_Lektion 5_...pdf`
- **What it shows:** Map of innovation types (Sustaining, Radical, Frugal, Disruptive, Discontinuous, Incremental, Architectural, Business Model) radiating from the central "Innovation" node.
- **When to cite:** When defining the kind of innovation in the case (and pre-empting confusion between e.g. radical and disruptive innovation).

### lec05-disruption-eye-model.png
- **Lecture:** 5 — Digital innovation, disruption
- **Source page:** 18 of `10032026_Lektion 5_...pdf`
- **What it shows:** "Øjemodel" — disruptive innovation classified by Type (Disruptive Technology / Disruptive Radical / Disruptive Business Model Innovation) crossed with Marked (Low-End / High-End / New Market Disruption).
- **When to cite:** When the analysis needs to specify what kind of disruption is at play; useful with Baiyere & Salmela's definition of disruption.

### lec05-digital-innovation-vs-disruption-venn.png
- **Lecture:** 5 — Digital innovation, disruption
- **Source page:** 19 of `10032026_Lektion 5_...pdf`
- **What it shows:** Venn-style diagram distinguishing Digital Innovation (DgI), Digital Disruption (DgD), and Disruptive Innovation (DI) and showing their overlap.
- **When to cite:** When disambiguating the three concepts; especially valuable for exam answers because the terms are easily confused.

---

## Lecture 6 — Digitale økosystemer og platforme

### lec06-uber-network-effects-napkin.png
- **Lecture:** 6 — Digitale økosystemer
- **Source page:** 17 of `170326_Lektion 6_Digitale økosystemer (1).pdf`
- **What it shows:** "The Napkin" — Uber's hand-drawn virtuous-cycle diagram (More demand → More drivers → More geographic coverage → Faster pickups / less driver downtime → Lower prices → More demand).
- **When to cite:** When explaining positive feedback loops and the flywheel logic of platform network effects.

### lec06-axes-of-network-effects.png
- **Lecture:** 6 — Digitale økosystemer
- **Source page:** 22 of `170326_Lektion 6_...pdf`
- **What it shows:** The 2×2 of network effects — Same-side vs Cross-side × Positive vs Negative — i.e. the four classes of network effects platforms must reason about.
- **When to cite:** When analysing what type(s) of network effects a platform exhibits and the implications for pricing, governance, and growth.

### lec06-three-dimensional-chess-platform-competition.png
- **Lecture:** 6 — Digitale økosystemer
- **Source page:** 28 of `170326_Lektion 6_...pdf`
- **What it shows:** Parker et al.'s "three-dimensional chess" — three levels of competition that platforms simultaneously play: platform vs platform, platform vs partner, partner vs partner; with the observation that platforms grow the pie rather than re-dividing it.
- **When to cite:** Strategy in platform ecosystems and why traditional five-forces logic underestimates platform power.

### lec06-platform-business-model-canvas-compact.png
- **Lecture:** 6 — Digitale økosystemer
- **Source page:** 39 of `170326_Lektion 6_...pdf`
- **What it shows:** A compact one-page Platform Business Model Canvas with Producer/Consumer segments, Stimuli, Interaction, Producer/Consumer Value Propositions, Producer/Consumer Substitutes, Facilitation, Metrics, Cost Model, and Monetization.
- **When to cite:** When analysing or recommending a two-sided platform business; alternative to Osterwalder when value is co-created between distinct platform sides.

### lec06-platform-business-model-canvas-details.png
- **Lecture:** 6 — Digitale økosystemer
- **Source page:** 41 of `170326_Lektion 6_...pdf`
- **What it shows:** The three-section breakdown of the Platform Business Model Canvas: (1) Platform Users / Stakeholders, (2) Value Proposition (Job / Pain / Gain / Core Value Unit / Transaction), and (3) Access and Usage (Resources, Activities, Access Channel, Filter, Promotion Channel, Governance).
- **When to cite:** Companion figure to the compact PBMC when more textual detail per block is helpful.

---

## Lecture 7 — Implementering af IT-strategier

### lec07-miller-four-success-factors.png
- **Lecture:** 7 — Implementering
- **Source page:** 10 of `260324_Lektion 7_Implementering (1).pdf`
- **What it shows:** Miller's (1997) four key success factors for implementing strategic decisions: Completion, Achievement, Acceptability (and Propitiousness, partly cut off — see the Miller-5 figure for the fuller picture).
- **When to cite:** When defining what "successful" implementation means; baseline definitions before the Tawse & Tabesh model.

### lec07-tawse-tabesh-implementation-framework.png
- **Lecture:** 7 — Implementering
- **Source page:** 13 of `260324_Lektion 7_...pdf`
- **What it shows:** Tawse & Tabesh's (2021) integrated implementation framework. Three layers: (1) Conditions (Competency, Commitment, Coordination) that determine Strategy Implementation Effectiveness; (2) Managerial Actions (Structural and Interpersonal) that produce those conditions; (3) Dynamic Managerial Capabilities (Cognition, Social Capital, Human Capital) that enable the right combination of conditions and actions.
- **When to cite:** Primary analytical lens for any "how should the strategy actually be implemented?" question. Anchor diagram for lecture 7.

### lec07-kotter-eight-step-leading-change.png
- **Lecture:** 7 — Implementering
- **Source page:** 18 of `260324_Lektion 7_...pdf`
- **What it shows:** Kotter's (2015) eight-step Leading Change model: Forøg presset → Etablér ledende koalition → Få visionen og strategien klar → Kommunikér visionen → Gør det! → Skab synlige resultater → Konsolidér forbedringer → Implementér nye procedurer i kulturen. Plus the top-down org cartoon emphasising leadership.
- **When to cite:** When recommending a concrete change-management sequence or contrasting Kotter's prescriptive top-down model with Tawse & Tabesh's more emergent view.

### lec07-schein-culture-model.png
- **Lecture:** 7 — Implementering
- **Source page:** 23 of `260324_Lektion 7_...pdf`
- **What it shows:** Schein & Brown's (1998) / Johnson et al.'s (2017) nested-circles model of culture: Paradigm (taken-for-granted assumptions) → Behaviours → Beliefs → Values, mapped to formelle/uformelle værdier, bevidste/ubevidste opfattelser, individuel/organisatorisk adfærd, erkendte/uerkendte antagelser.
- **When to cite:** When culture is part of the implementation argument — e.g. why a strategically sound plan can fail because of paradigm-level assumptions.

### lec07-miller-five-implementation-factors.png
- **Lecture:** 7 — Implementering
- **Source page:** 32 of `260324_Lektion 7_...pdf`
- **What it shows:** Miller's five implementation factors — Backing, Assessability, Specificity, Cultural receptivity, Propitiousness — each with a one-line definition.
- **When to cite:** When summarising cross-cutting determinants of implementation success or running a quick checklist against a case.

---

## Lecture 9 — Opsummering

No new figures extracted. Lecture 9 consists of recap collages of slides from Lectures 1–7 and exam-format material; the underlying models are already captured in this manifest under their original lectures.
