# Project Context: IT-strategi Exam 2026

> This file provides context for LLMs reading this repository. It describes the exam assignment, the case, the source materials, and key tensions in the material. It does not contain answers or recommendations.

---

## What this repo is

This repository contains source material, analyses, and working documents for a CBS exam in IT-strategi (course code: BINTO2011U.LA_F25). The exam was issued on 20 April 2026 by Ulrik Røhl (ubur.digi@cbs.dk).

---

## The case: Coop Denmark

The case centers on **Coop**, the largest Danish grocery conglomerate, which operates the chains **Kvickly**, **SuperBrugsen**, **Brugsen**, and **365discount**.

**Key facts about Coop:**
- Historically the largest player in the Danish grocery market
- Has experienced declining revenue and structural deficits for several years
- Launched a major financial recovery plan in early 2025
- 2025 annual results: ~1.0 billion DKK revenue decline, 232 million DKK net loss
- Closed its online store (coop.dk) in 2023 due to lack of profitability
- Today sells exclusively through physical stores

**Coop App and Lobyco:**
- Coop invested early and significantly in a customer-facing app, the **Coop App**
- The app was originally developed in-house, then spun out into a wholly owned subsidiary: **Lobyco**
- The app has approximately 1.8 million users, covering ~25% of Danish households
- Features include: personalized offers, Scan & Pay, gamification, retail media, loyalty mechanics
- Lobyco operates as a platform company and has sold its platform to other retailers outside Denmark

---

## The exam assignment

Students must:
1. **Analyze Coop's strategic situation** using the provided sources
2. **Develop 2–5 strategic recommendations** grounded in the analysis

The analysis must be based on **1–2 self-selected theoretical perspectives** from the course curriculum.

Students choose which Coop executive to advise:
- CEO: Thor Skov Jørgensen
- Director SuperBrugsen & Kvickly: Rikke Krause
- Director Brugsen: Torben B. Andersen
- Director 365discount: Michael Tilsted
- Director of Communication, Marketing & Digital: Martin Hasgard Olesen

**Central strategic question posed in the assignment:**
Should Coop continue to be a market leader in the Coop App, reduce app investments (potentially divesting Lobyco), go deeper with chain-specific apps, or pursue another path — given that Coop's physical stores remain the core of its brand?

---

## Source materials

All sources are in `Offical Exam Docs/` (PDFs) and `Markdown/` (converted markdown versions).

| Source | Year | Type | Key content |
|---|---|---|---|
| Bjørn-Andersen & Hedman: *The Challenge of Technological Debt – Coop* | 2016 | Academic case | Coop's historical IT complexity, technological debt, and governance challenges |
| Duus & Cooray: *DVC Framework* | 2020 | Article/framework | Theory on digital value creation; includes a Coop case |
| Lobyco case study | 2026 | Vendor/marketing | App usage stats, platform capabilities, Scan & Pay, repeat shopping |
| Playable case study | 2026 | Vendor/marketing | Gamification, retail media, supplier-funded rewards, store traffic |
| Shortcut case study | 2026 | Vendor/marketing | App development history, features, OEM/white-label potential |

**Source criticism is explicitly required by the exam.** The Lobyco, Playable, and Shortcut sources are promotional in nature. The 2016 Hedman & Bjørn-Andersen source describes a historical situation and cannot be used as direct evidence of Coop's current technical state.

---

## Repository structure

```
/Offical Exam Docs/         Original PDFs (exam description + additional context sources)
/Markdown/                  Markdown conversions of all PDFs
  /Reports markdown/        Analysis reports (not exam submissions)
  /Additional context markdown/  Converted source documents
  /assets/                  Images extracted from PDFs
/HTML/                      HTML versions of reports (Claude and ChatGPT generated analyses)
/Reports/                   PDF versions of analysis reports
/Slides/                    Course lecture slides (Lektion 1–9)
/scripts/                   Utility scripts (e.g., scraping)
/data/                      Data files
```

---

## Key tensions in the material

The following tensions are present in the source material and are not resolved by the sources themselves:

- **App as asset vs. app as cost center:** The marketing sources present the app as a clear success. The financial figures suggest Coop is under serious pressure. It is not obvious whether the app creates enough measurable value to justify continued investment.
- **Lobyco as strategic platform vs. divestment candidate:** Lobyco can be read as either a scalable B2B platform or as a capital-intensive subsidiary that dilutes Coop's focus.
- **One app vs. chain-specific apps:** Coop's chains have different customer profiles (price-sensitive 365discount vs. quality-oriented Kvickly). It is unclear whether a single app can serve all chains effectively.
- **Digital transformation vs. core business:** Coop's core is physical retail. The assignment explicitly raises the question of whether digital market leadership is the right priority.
- **Technological debt risk:** The 2016 source describes how Coop previously accumulated technological debt. The same risk exists for decisions made about the app today.
- **Source vintage mismatch:** The DVC Framework article was written before Coop closed coop.dk (2023) and before the 2025 deficit. Claims in that article may not reflect Coop's current situation.

---

## Theoretical frameworks referenced in the course

The slides in `/Slides/` cover the following topic areas (Lektion 1–9):
- IT strategy and strategic analysis
- Digital business models
- Digital transformation
- Digital innovation and disruption
- Digital ecosystems
- Implementation of IT strategy
- Summary and exam guidance

The specific frameworks used in any given exam submission are the student's own choice.

---

*Last updated: 2026-05-03*
