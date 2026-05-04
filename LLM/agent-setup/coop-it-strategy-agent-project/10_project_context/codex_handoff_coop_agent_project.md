# Coop IT-Strategy Exam Project — Codex Handoff & Implementation Plan

**Purpose of this file:**  
This markdown file explains the full project setup we discussed in ChatGPT and tells Codex how to continue from here.

The goal is to build a structured, human-in-the-loop **agent workflow** for the IT-strategy exam project about **Coop, Coop App, Lobyco, digital value creation, competitors, source criticism, and strategic recommendations**.

The project should not become a random AI-generated report. It should become a controlled exam project where:
- agents create options,
- the user can review and choose,
- important decisions are logged,
- sources are treated critically,
- the final output is aligned with the exam case and course theory.

---

# 1. Project Context

The exam project is about **Coop Denmark** and its digital strategy, especially around:

- Coop App
- Lobyco
- customer loyalty
- retail media
- app-based shopping experiences
- the closing of coop.dk
- Coop’s financial pressure
- the relationship between digital initiatives and physical stores
- whether Coop should strengthen, reduce, sell, differentiate, or rethink its app/Lobyco strategy

The uploaded exam case says that Coop has invested early and significantly in the Coop App. The app was originally developed internally and was later separated into the subsidiary **Lobyco**. In 2023, Coop closed its online store, **coop.dk**, because of lack of profitability. Today, Coop sells only through physical stores.

The case also states that Coop has had declining revenue and structural deficits. In 2025, revenue fell by around **1.0 billion DKK**, and Coop had a loss of **232 million DKK**.

This means the project should not simply ask:

> “Is the Coop App good?”

It should ask something closer to:

> “What strategic role should the Coop App and Lobyco play in Coop’s turnaround, given Coop’s financial pressure, physical-store dependency, competitive situation, and the marketing-biased nature of several case sources?”

---

# 2. Very Important Exam Constraint

The exam project should not use too many theories.

The assignment asks for **1–2 selected course perspectives**.

Therefore, the system should prevent theory overload. The agents should not produce a report full of every possible model.

Recommended theory focus:

1. **DVC Framework**  
   Relevant because it analyses digital value creation through:
   - Experiences
   - Relationships
   - Evolution
   - Relevance
   - Digital competences
   - Digital infrastructure
   - Digital outputs

2. **Digital Business Model / Ecosystem / Platform perspective**  
   Relevant because it helps analyse:
   - whether Coop App is just a loyalty tool,
   - whether Lobyco is a strategic digital capability,
   - whether Coop is creating an ecosystem or supplier/customer platform,
   - whether retail media and gamification create a new value logic.

Possible alternative theories:
- Porter / positioning
- Implementation theory
- Platform Business Model Canvas
- Resource-based view
- Digital transformation theory

But the first version of the project should probably focus on:

> **DVC Framework + Digital Business Model / Ecosystem perspective**

Codex should still create option banks so the user can choose differently.

---

# 3. Core Strategic Interpretation

A useful working thesis is:

> Coop should not treat the Coop App as a separate digital prestige project. It should treat the app and Lobyco as strategic assets only if they strengthen Coop’s core business: physical stores, customer loyalty, supplier value, store traffic, differentiated chain positioning, and financial turnaround.

This can be sharpened later, but it is a strong starting position.

Important nuance:

- Coop App may be successful in terms of users, loyalty, engagement and supplier-funded campaigns.
- But digital engagement is not the same as financial success.
- The exam project must distinguish between:
  - app adoption,
  - customer engagement,
  - loyalty,
  - store traffic,
  - revenue,
  - profitability,
  - strategic differentiation,
  - long-term competitive advantage.

---

# 4. Critical Source Handling Is Mandatory

Many of the provided sources are not neutral. Some are marketing or supplier case studies.

This is central to the project.

The report should not write:

> “The Coop App is a huge success.”

Instead, it should write:

> “Lobyco presents the Coop App as successful based on user adoption and engagement metrics, but because the source is commercially connected to the app, these claims should be treated as indicators rather than neutral proof of financial success.”

## Source types

| Source | Type | Bias risk | How to use |
|---|---|---:|---|
| Exam assignment | Official exam case | Low | Use as factual foundation |
| Hedman & Bjørn-Andersen 2016 | Academic / case source | Medium | Use for historical IT debt and background |
| DVC Framework 2020 | Academic-style article / framework | Medium | Use as theory and Coop case interpretation |
| Lobyco 2026 | Subsidiary / vendor marketing | High | Use claims cautiously |
| Playable 2026 | Supplier marketing | High | Use as evidence of intended value, not neutral proof |
| Shortcut 2026 | Supplier/developer marketing | High | Use for app development history, but not as neutral evaluation |

## Required source labels

Every important claim should be tagged as one of these:

| Label | Meaning |
|---|---|
| **Fact** | Strong, neutral or official information |
| **Claim** | Source says it, but it needs caution |
| **Marketing claim** | Comes from vendor, supplier or self-promotional source |
| **Assumption** | Reasonable project assumption |
| **Inference** | Analytical conclusion based on multiple sources |

Example:

| Statement | Label | Better writing |
|---|---|---|
| Coop lost 232m DKK in 2025 | Fact | “Coop is financially pressured.” |
| App users shop 50% more frequently | Claim / marketing claim | “Lobyco claims app users shop more frequently, but this may reflect selection bias.” |
| Coop App is a success | Marketing claim | “The app appears to have high adoption, but this alone does not prove strategic or financial success.” |
| App should be tied to store economics | Inference | “Given Coop’s current physical-store model, app value should be assessed through store impact.” |

---

# 5. Human-in-the-Loop Principle

This project should not be fully automatic.

The user wants to be able to see options and choose.

Therefore, Codex should implement the workflow as:

```text
Agents produce options
        ↓
Options are scored and explained
        ↓
User chooses
        ↓
Choice is logged
        ↓
Agents continue based on the user’s choice
```

The system should create decision gates where the user chooses before moving forward.

## Key decision gates

| Gate | User chooses | Why it matters |
|---|---|---|
| Gate 1 | Executive to advise | Controls angle and recommendations |
| Gate 2 | Main problem framing | Controls the red thread |
| Gate 3 | Course perspectives | Prevents theory overload |
| Gate 4 | Strategic position | Determines core argument |
| Gate 5 | Final recommendations | User selects 2–5 recommendations |
| Gate 6 | Final structure and tone | Makes report exam-ready |

Codex should not skip these gates.

---

# 6. Recommended Agent Setup

We discussed at least 3 agents, but the strongest version is a **7-agent setup**.

The user should still be able to collapse this into 3 agents later.

## 7-agent setup

| Agent | Name | Main responsibility |
|---|---|---|
| 1 | Exam Architect | Keeps project aligned with exam task |
| 2 | Evidence Extractor | Extracts facts and claims from case sources |
| 3 | Source Critic / Bias Agent | Evaluates reliability, age, bias and marketing language |
| 4 | Competitor & Market Agent | Compares Coop with competitors and market trends |
| 5 | Theory Application Agent | Applies 1–2 selected course perspectives |
| 6 | Recommendation Agent | Generates recommendation options |
| 7 | Red Team Agent | Challenges argument, evidence, theory use and recommendations |

---

# 7. Agent Details

## Agent 1 — Exam Architect

### Mission
Control the project and ensure it answers the exam assignment.

### Responsibilities
- Read the exam task.
- Define the strategic problem.
- Propose executive options.
- Propose main argument options.
- Control decision gates.
- Ensure 1–2 theories only.
- Ensure the final report has a clear red thread.
- Check whether the recommendations actually answer the assignment.

### Outputs
- `00_project_brief.md`
- `01_decision_board.md`
- `02_decision_register.md`
- `08_final_report/outline.md`

### Questions this agent should ask
- Are we answering the actual exam question?
- Are we advising one specific executive?
- Are we using too many theories?
- Is the argument clear?
- Do recommendations follow from evidence and theory?

### Example output
```markdown
## Recommended executive options

| Option | Executive | Why it fits | Risk | Score |
|---|---|---|---|---:|
| 1 | CEO | Full strategic responsibility | Too broad | 7 |
| 2 | Director of Communication, Marketing & Digital | Best fit with app, loyalty, retail media | Less control over finance/store operations | 9 |
| 3 | CFO | Strong fit with financial pressure | Less direct fit with app value | 6 |
```

---

## Agent 2 — Evidence Extractor

### Mission
Extract all relevant factual claims from the uploaded case material and any approved external sources.

### Responsibilities
- Extract numbers, claims and case observations.
- Separate source facts from interpretation.
- Build an evidence register.
- Make sure both positive and negative evidence are included.
- Avoid judging source reliability; that is Agent 3’s job.

### Outputs
- `05_evidence/evidence_register.md`
- `05_evidence/raw_case_claims.md`
- `05_evidence/key_numbers.md`

### Evidence categories
- Coop financial pressure
- Coop App usage
- Lobyco spin-out
- coop.dk closure
- physical-store dependency
- chain structure
- loyalty claims
- gamification claims
- retail media claims
- competitor evidence
- app feature evidence
- customer behaviour evidence

### Example output
```markdown
| Claim | Source | Year | Evidence type | Related issue |
|---|---|---:|---|---|
| Coop closed coop.dk in 2023 due to lack of profitability | Exam case | 2026 | Fact | Digital channel limitation |
| Coop sells only through physical stores today | Exam case | 2026 | Fact | Store-based model |
| Lobyco claims the app has 1.8m users | Lobyco | 2026 | Claim | App adoption |
```

---

## Agent 3 — Source Critic / Bias Agent

### Mission
Challenge and classify every source and claim.

### Responsibilities
- Label claims as fact, claim, marketing claim, assumption or inference.
- Identify bias risk.
- Identify age problems.
- Identify selection bias.
- Identify causality problems.
- Rewrite overconfident statements in careful exam language.

### Outputs
- `05_evidence/source_register.md`
- `05_evidence/source_criticism.md`
- `05_evidence/claim_reliability_matrix.md`

### Main principle
Never allow vendor claims to be used as neutral proof.

### Example output
```markdown
| Claim | Reliability | Bias risk | Use in report? | Comment |
|---|---|---:|---|---|
| App users shop more frequently | Medium | High | Yes, cautiously | Could reflect selection bias: loyal customers may be more likely to use the app |
| Coop App is a huge success | Low as proof | High | Rewrite | Use as evidence of self-presentation, not proof |
| Coop has financial pressure | High | Low | Yes | Comes from official exam case |
```

### Useful sentence patterns
- “The source claims...”
- “This indicates...”
- “This should be treated cautiously because...”
- “This is useful as evidence of intended value, but not as proof of profitability.”
- “The claim may reflect selection bias.”
- “The evidence supports app adoption, but not necessarily financial turnaround.”

---

## Agent 4 — Competitor & Market Agent

### Mission
Find out what Coop’s competitors do differently.

### Responsibilities
- Research Danish grocery competitors.
- Compare digital tools, loyalty, price positioning, store formats, retail media and omnichannel activity.
- Identify whether competitors are succeeding through digital tools or through non-digital factors such as price, logistics, simplicity or store experience.
- Add evidence to competitor register.
- Send sources to Agent 3 for source criticism.

### Outputs
- `05_evidence/competitor_evidence.md`
- `06_analysis/competitor_analysis.md`
- `04_option_banks/competitor_insight_options.md`

### Questions to answer
- Are competitors winning through apps, prices, store format, logistics or loyalty?
- Are discount competitors like Rema 1000, Lidl and Netto doing something Coop is not?
- Is 365discount positioned clearly enough?
- Do competitors use loyalty apps differently?
- Is retail media becoming strategically important in grocery?
- Are customers loyal in grocery, or mainly price-sensitive?

### Example output
```markdown
| Competitor | Strategic focus | Digital relevance | Coop implication |
|---|---|---|---|
| Rema 1000 | Simplicity, discount, local merchant model | App supports offers and convenience | Coop must ensure 365discount app value is simple and price-focused |
| Netto | Discount and scale | Digital offers and campaigns | Coop cannot rely on loyalty alone if price perception is weak |
| Lidl | International discount scale | Strong price/value campaigns | Coop must clarify whether app supports differentiation or just adds complexity |
```

---

## Agent 5 — Theory Application Agent

### Mission
Apply 1–2 course theories to the case.

### Responsibilities
- Present theory only briefly.
- Apply theory directly to Coop.
- Avoid long generic theory descriptions.
- Build bridges between theory and evidence.
- Help decide which theory combination is strongest.

### Outputs
- `04_option_banks/theory_options.md`
- `06_analysis/dvc_analysis.md`
- `06_analysis/digital_business_model_analysis.md`
- `06_analysis/theory_to_evidence_matrix.md`

### Recommended theory option bank
```markdown
| Option | Course perspective | Fit with case | Risk | Score |
|---|---|---:|---|---:|
| 1 | DVC Framework | Very strong fit with app, loyalty, customer experience | Can become too positive if source criticism is weak | 9 |
| 2 | Digital Business Model Framework | Strong fit with Lobyco and app value logic | Requires precise framing | 8 |
| 3 | Platform / ecosystem theory | Good for retail media and Lobyco | May overstate Coop as a platform | 7 |
| 4 | Implementation theory | Good for execution risk | Less direct for app strategy | 7 |
| 5 | Porter / positioning | Strong competitor framing | Less digital-specific | 6 |
```

### Example DVC analysis matrix
```markdown
| DVC concept | Coop observation | Analytical meaning |
|---|---|---|
| Experiences | Scan & Pay, offers, recipes, games | App can improve shopping experience if it solves real customer problems |
| Relationships | Bonus, personal offers, local store info | App can deepen customer relationship and loyalty |
| Evolution | Lobyco, OEM, retail media | Coop has built a digital capability beyond normal retail operations |
| Relevance | Different chains serve different needs | One app logic may not fit 365discount and Kvickly equally well |
```

---

## Agent 6 — Recommendation Agent

### Mission
Generate strategic recommendation options.

### Responsibilities
- Generate 8–12 recommendation options.
- Score them.
- Explain pros, cons and risks.
- Link each recommendation to evidence and theory.
- Let the user choose 2–5 final recommendations.

### Outputs
- `04_option_banks/recommendation_options.md`
- `07_recommendations/recommendation_bank.md`
- `07_recommendations/chosen_recommendations.md`

### Example recommendation bank
```markdown
| Option | Recommendation | Strategic logic | Risk | Score |
|---|---|---|---|---:|
| 1 | Continue investing in Coop App, but tie investments to store economics | Coop is now store-based; app value must be measured through store impact | Needs stricter KPIs | 9 |
| 2 | Do not sell Lobyco now, but clarify its strategic contribution | Lobyco may be a rare digital capability | May distract from core turnaround | 8 |
| 3 | Differentiate app experience by chain | 365discount and Kvickly need different value propositions | More operational complexity | 9 |
| 4 | Build retail media carefully | Supplier-funded campaigns can create revenue and engagement | May damage trust if over-commercialised | 7 |
| 5 | Reduce pure engagement/gamification features | Avoid digital noise and focus on utility | Could lower traffic | 6 |
| 6 | Relaunch online grocery selectively | Could regain digital channel | Risky due to coop.dk closure | 5 |
| 7 | Sell Lobyco | Could release capital and focus | May lose strategic capability | 4 |
| 8 | Use app mainly for price transparency and savings | Helps discount competition | May narrow Coop’s broader value proposition | 6 |
```

### Required recommendation structure
Every chosen recommendation should follow this structure:

```markdown
## Recommendation X: [Title]

**Recommendation:**  
[Concrete recommendation]

**Why:**  
[Strategic logic]

**Evidence:**  
[Relevant case facts and source-critical claims]

**Theory link:**  
[Relevant DVC / digital business model concept]

**Risk:**  
[Main risk]

**Implementation implication:**  
[What Coop would actually need to do]
```

---

## Agent 7 — Red Team Agent

### Mission
Attack the project before the examiner does.

### Responsibilities
- Challenge the main argument.
- Check whether the report overuses marketing sources.
- Check whether theory is applied and not just described.
- Check whether recommendations follow from evidence.
- Check whether weak causal claims are removed.
- Prepare likely oral exam questions.

### Outputs
- `07_recommendations/red_team_review.md`
- `08_final_report/examiner_questions.md`
- `08_final_report/final_quality_check.md`

### Red-team questions
```markdown
| Question | Why it matters |
|---|---|
| Are we too positive about the Coop App? | Avoid repeating marketing claims |
| Are we ignoring Coop’s financial pressure? | Keep strategy realistic |
| Are we assuming app users are profitable? | Avoid unsupported causality |
| Are we using theory analytically? | Fit exam expectations |
| Are recommendations specific enough for the chosen executive? | Make it management-relevant |
| Have we explained assumptions clearly? | Required by case description |
| Have we considered competitors and dynamic reactions? | Stronger strategic analysis |
```

---

# 8. Simplified 3-Agent Version

If the user wants a simpler setup, collapse the system into 3 agents:

| Agent | Combines |
|---|---|
| 1. Exam Architect | Structure, executive, problem framing, decision gates, final report fit |
| 2. Evidence & Source Critic | Case evidence, competitor evidence, source criticism |
| 3. Theory & Recommendation Agent | Theory application, recommendation bank, red team review |

But the recommended version is still the 7-agent workflow because source criticism and red-team review are important enough to be separate.

---

# 9. Option-Based Workflow

The system must generate options for the user to choose from.

## Option bank files

Create:

```text
04_option_banks/
├── executive_options.md
├── theory_options.md
├── strategic_position_options.md
├── recommendation_options.md
├── competitor_insight_options.md
└── final_structure_options.md
```

## Option bank format

Every option bank should use this format:

```markdown
# [Name] Option Bank

| Option | Description | Pros | Cons / Risks | Score | Recommended? |
|---|---|---|---|---:|---|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |

## Agent recommendation
[Short recommendation]

## User decision
Chosen option:  
Reason:
Date:
```

---

# 10. Decision Board

Create a file:

```text
01_decision_board.md
```

It should always show the current status of the project’s major decisions.

## Template

```markdown
# Decision Board

| Decision | Status | Options file | Chosen option | Owner | Deadline |
|---|---|---|---|---|---|
| Executive to advise | Open | 04_option_banks/executive_options.md | — | User | — |
| Main problem framing | Open | 04_option_banks/strategic_position_options.md | — | User | — |
| Course perspectives | Open | 04_option_banks/theory_options.md | — | User | — |
| Final recommendations | Open | 04_option_banks/recommendation_options.md | — | User | — |
| Final report structure | Open | 04_option_banks/final_structure_options.md | — | User | — |
```

Status values:
- Open
- Proposed
- Chosen
- Locked
- Reopened

---

# 11. Decision Register

Create:

```text
02_decision_register.md
```

The decision register records all final choices.

## Template

```markdown
# Decision Register

| Date | Decision | Options considered | Chosen | Reason | Consequence |
|---|---|---|---|---|---|
| YYYY-MM-DD | Course perspectives | DVC, DBM, Platform, Porter, Implementation | DVC + Digital Business Model | Best fit with app/Lobyco issue | Limits theory section to these models |
```

Why this matters:
- It creates traceability.
- It helps the user remember why a choice was made.
- It can support oral exam preparation.
- It prevents the project from drifting.

---

# 12. Daily Logging System

The user wants a daily logging system to track progress.

Create folder:

```text
03_daily_logs/
```

Each day gets one file:

```text
03_daily_logs/YYYY-MM-DD.md
```

## Daily log template

```markdown
# Daily Log — YYYY-MM-DD

## 1. Work completed today
- 

## 2. Agent outputs produced

| Agent | Output | File | Status |
|---|---|---|---|
| Exam Architect |  |  |  |
| Evidence Extractor |  |  |  |
| Source Critic |  |  |  |
| Competitor Agent |  |  |  |
| Theory Agent |  |  |  |
| Recommendation Agent |  |  |  |
| Red Team Agent |  |  |  |

## 3. Key decisions made

| Decision | Options considered | Chosen option | Reason |
|---|---|---|---|
|  |  |  |  |

## 4. Open decisions

| Decision | Needed by | Owner | Options file |
|---|---|---|---|
|  |  |  |  |

## 5. Source criticism notes
- 

## 6. Risks / problems discovered
- 

## 7. Next actions
- [ ] 
- [ ] 
- [ ] 
```

## Daily close-down checklist

At the end of each day Codex should update the daily log with:

```markdown
## Daily close-down

1. What did we complete today?
2. What options were created?
3. What did the user choose?
4. What is still open?
5. What should be done tomorrow?
```

---

# 13. Source Register

Create:

```text
05_evidence/source_register.md
```

## Template

```markdown
# Source Register

| Source | Type | Year | Main claims | Bias risk | Age risk | How we use it |
|---|---|---:|---|---:|---:|---|
| Exam case description | Official exam source | 2026 | Coop financial pressure, app/Lobyco strategic question | Low | Low | Factual foundation |
| Lobyco case | Marketing / subsidiary | 2026 | App users, traffic, loyalty | High | Low | Use claims cautiously |
| Playable case | Supplier marketing | 2026 | Gamification, retail media | High | Low | Use as evidence of intended value, not proof |
| Shortcut case | Supplier marketing | 2026 | App development and features | High | Low | Use for background, not neutral evaluation |
| DVC article | Academic-style / framework | 2020 | Digital value creation | Medium | Medium | Use as theory and case framing |
| Hedman & Bjørn-Andersen | Academic case | 2016 | Historical technological debt | Medium | High | Use for historical background |
```

Bias risk:
- Low
- Medium
- High

Age risk:
- Low
- Medium
- High

---

# 14. Evidence Register

Create:

```text
05_evidence/evidence_register.md
```

## Template

```markdown
# Evidence Register

| ID | Claim | Source | Year | Source type | Claim label | Reliability | Notes |
|---|---|---|---:|---|---|---|---|
| E001 | Coop closed coop.dk in 2023 due to lack of profitability | Exam case | 2026 | Official case | Fact | High | Shows digital channel failure/limitation |
| E002 | Coop sells only through physical stores today | Exam case | 2026 | Official case | Fact | High | Important for store-based strategy |
| E003 | Lobyco claims the Coop App has 1.8m users | Lobyco | 2026 | Marketing | Claim | Medium | Adoption metric, not proof of profitability |
```

---

# 15. Folder Structure to Create

Codex should create this folder structure:

```text
coop-it-strategy-agent-project/
│
├── 00_project_brief.md
├── 01_decision_board.md
├── 02_decision_register.md
│
├── 03_daily_logs/
│   └── YYYY-MM-DD.md
│
├── 04_option_banks/
│   ├── executive_options.md
│   ├── theory_options.md
│   ├── strategic_position_options.md
│   ├── recommendation_options.md
│   ├── competitor_insight_options.md
│   └── final_structure_options.md
│
├── 05_evidence/
│   ├── evidence_register.md
│   ├── source_register.md
│   ├── source_criticism.md
│   ├── claim_reliability_matrix.md
│   ├── competitor_evidence.md
│   └── key_numbers.md
│
├── 06_analysis/
│   ├── dvc_analysis.md
│   ├── digital_business_model_analysis.md
│   ├── competitor_analysis.md
│   └── theory_to_evidence_matrix.md
│
├── 07_recommendations/
│   ├── recommendation_bank.md
│   ├── chosen_recommendations.md
│   └── red_team_review.md
│
├── 08_final_report/
│   ├── outline.md
│   ├── draft_v1.md
│   ├── draft_v2.md
│   ├── final.md
│   ├── examiner_questions.md
│   └── final_quality_check.md
│
└── 09_codex_prompts/
    ├── first_prompt_to_codex.md
    ├── agent_prompts.md
    ├── daily_log_prompt.md
    └── red_team_prompt.md
```

---

# 16. Terminal Setup

The user cannot directly open the exact ChatGPT conversation inside the Codex terminal interface. The practical approach is to move the context into files and run Codex from that project folder.

Codex CLI is intended to run locally from the terminal and can read, change and run code in the selected directory. It can also run in interactive mode with `codex`, or with an initial prompt such as `codex "Explain this codebase to me"`.

## Suggested terminal commands

```bash
mkdir coop-it-strategy-agent-project
cd coop-it-strategy-agent-project

mkdir -p 03_daily_logs
mkdir -p 04_option_banks
mkdir -p 05_evidence
mkdir -p 06_analysis
mkdir -p 07_recommendations
mkdir -p 08_final_report
mkdir -p 09_codex_prompts

touch 00_project_brief.md
touch 01_decision_board.md
touch 02_decision_register.md
touch 05_evidence/source_register.md
touch 05_evidence/evidence_register.md
touch 09_codex_prompts/first_prompt_to_codex.md
```

Then copy this file into the project folder.

Start Codex:

```bash
codex
```

Or start with an initial prompt:

```bash
codex "Read the markdown files in this folder and implement the Coop IT-strategy exam agent workflow. Start by creating the folder structure, decision board, source register, option banks, and today's daily log. Do not write the final report yet."
```

---

# 17. First Prompt to Give Codex

Save this as:

```text
09_codex_prompts/first_prompt_to_codex.md
```

## Prompt

```markdown
You are helping me implement a structured human-in-the-loop agent workflow for my IT-strategy exam project about Coop Denmark, Coop App and Lobyco.

Read all markdown files in this folder first.

Your first task is NOT to write the final exam paper.

Your first task is to create the project control system:

1. Create the full folder structure described in `codex_handoff_coop_agent_project.md`.
2. Create these key files if they do not already exist:
   - `00_project_brief.md`
   - `01_decision_board.md`
   - `02_decision_register.md`
   - `05_evidence/source_register.md`
   - `05_evidence/evidence_register.md`
   - `04_option_banks/executive_options.md`
   - `04_option_banks/theory_options.md`
   - `04_option_banks/strategic_position_options.md`
   - `04_option_banks/recommendation_options.md`
   - today’s daily log in `03_daily_logs/YYYY-MM-DD.md`
3. Populate each file with useful starter templates.
4. Build the first option banks:
   - executive options
   - theory options
   - strategic position options
5. Do not make final decisions for me.
6. Give me options with pros, cons, risks and recommended scores.
7. Stop after creating these files and give me a short summary of what I should choose next.

Important rules:
- I must be able to choose between options.
- Every important decision must be logged.
- Many sources are marketing sources, so source criticism is central.
- Do not treat Lobyco, Shortcut or Playable claims as neutral proof.
- Use careful wording: "claims", "indicates", "suggests", "should be treated cautiously".
- The final project should use only 1–2 course perspectives.
- The likely best theory combination is DVC Framework + Digital Business Model / Ecosystem perspective, but still give me options.
```

---

# 18. Agent Prompts

Save this as:

```text
09_codex_prompts/agent_prompts.md
```

## Agent 1 Prompt — Exam Architect

```markdown
You are the Exam Architect Agent.

Your job is to keep the Coop IT-strategy exam project aligned with the exam assignment.

Do not write the final report yet.

Tasks:
1. Read the project brief.
2. Create or update the decision board.
3. Create executive options.
4. Create main problem framing options.
5. Create theory selection options.
6. Recommend a project structure.
7. Identify what must be decided by the user before moving forward.

Rules:
- The user must choose between options.
- Use max 1–2 theories in the final report.
- Keep focus on the strategic role of Coop App/Lobyco.
- Avoid broad, generic digital transformation writing.
- Make all choices traceable in the decision register.
```

## Agent 2 Prompt — Evidence Extractor

```markdown
You are the Evidence Extractor Agent.

Your job is to extract relevant facts and claims from the uploaded case sources and approved external sources.

Do not judge the claims. That is the Source Critic Agent’s job.

Tasks:
1. Extract claims about Coop’s financial situation.
2. Extract claims about Coop App.
3. Extract claims about Lobyco.
4. Extract claims about coop.dk closure.
5. Extract claims about physical stores.
6. Extract claims about app features, loyalty, retail media and gamification.
7. Put claims into the evidence register.

Rules:
- Separate claim from interpretation.
- Include source, year, type and relevant issue.
- Do not write "proves" unless the evidence is very strong.
- Include both positive and negative evidence.
```

## Agent 3 Prompt — Source Critic / Bias Agent

```markdown
You are the Source Critic / Bias Agent.

Your job is to classify and challenge all sources and claims.

Tasks:
1. Review the source register.
2. Classify each source by type, bias risk and age risk.
3. Classify each important claim as Fact, Claim, Marketing claim, Assumption or Inference.
4. Rewrite overconfident claims in careful academic/exam language.
5. Identify causality problems, selection bias and marketing language.
6. Create a claim reliability matrix.

Rules:
- Do not treat vendor/supplier/self-promotional sources as neutral proof.
- Lobyco, Playable and Shortcut should be treated cautiously.
- Marketing claims can be used, but only as claims or indications.
- Always distinguish between app adoption, engagement and profitability.
```

## Agent 4 Prompt — Competitor & Market Agent

```markdown
You are the Competitor & Market Agent.

Your job is to compare Coop with relevant competitors and market trends.

Tasks:
1. Identify relevant Danish grocery competitors.
2. Compare their positioning, digital tools, loyalty approaches, store formats and price strategies.
3. Investigate whether competitors win through digital capabilities, price, logistics, simplicity or store experience.
4. Build a competitor evidence file.
5. Create competitor insight options.

Rules:
- Do not overfocus on apps.
- Ask whether digital tools actually create strategic advantage.
- Send all external claims to the Source Critic Agent for classification.
- Use careful source language.
```

## Agent 5 Prompt — Theory Application Agent

```markdown
You are the Theory Application Agent.

Your job is to apply 1–2 course theories to the Coop case.

Tasks:
1. Create a theory option bank.
2. Score each theory for fit, risk and usefulness.
3. Apply the chosen theory/theories directly to Coop.
4. Create a theory-to-evidence matrix.
5. Avoid long generic theory summaries.

Recommended theories to consider:
- DVC Framework
- Digital Business Model Framework
- Platform / ecosystem theory
- Implementation theory
- Porter / positioning

Rules:
- Do not use more than 1–2 theories in the final report.
- Theory must be applied, not just described.
- Explain what each theory reveals and what it does not reveal.
```

## Agent 6 Prompt — Recommendation Agent

```markdown
You are the Recommendation Agent.

Your job is to create strategic recommendation options.

Tasks:
1. Generate 8–12 possible recommendations.
2. Score them by strategic fit, evidence support, theory support and implementation risk.
3. Present pros and cons.
4. Let the user choose 2–5 final recommendations.
5. After user choice, draft the chosen recommendations.

Rules:
- Every recommendation must link to evidence and theory.
- Every recommendation must include source-critical nuance.
- Do not assume app engagement equals profitability.
- Recommendations must be useful for the chosen executive.
```

## Agent 7 Prompt — Red Team Agent

```markdown
You are the Red Team Agent.

Your job is to attack the project before the examiner does.

Tasks:
1. Review the argument.
2. Review source use.
3. Review theory application.
4. Review recommendations.
5. Identify weak claims, missing evidence and unsupported assumptions.
6. Create likely oral exam questions.
7. Suggest fixes.

Rules:
- Be critical but constructive.
- Focus on exam risk.
- Challenge overpositive app claims.
- Challenge weak causality.
- Challenge model dumping.
- Challenge generic recommendations.
```

---

# 19. Daily Log Prompt

Save this as:

```text
09_codex_prompts/daily_log_prompt.md
```

## Prompt

```markdown
Update today’s daily log.

Use the file:
`03_daily_logs/YYYY-MM-DD.md`

Include:

1. Work completed today.
2. Agent outputs produced.
3. Key decisions made.
4. Open decisions.
5. Source criticism notes.
6. Risks or problems discovered.
7. Next actions.

Do not invent decisions. If the user has not chosen, mark the decision as Open.

At the end, write:
- What the user should choose next.
- Which file contains the options.
```

---

# 20. Red Team Prompt

Save this as:

```text
09_codex_prompts/red_team_prompt.md
```

## Prompt

```markdown
Run a red-team review of the current Coop IT-strategy project.

Review these files:
- `00_project_brief.md`
- `01_decision_board.md`
- `05_evidence/evidence_register.md`
- `05_evidence/source_register.md`
- `06_analysis/*.md`
- `07_recommendations/*.md`
- `08_final_report/outline.md` if it exists

Check for:
1. Overuse of marketing sources.
2. Unsupported claims.
3. Weak causality.
4. Missing competitor comparison.
5. Too many theories.
6. Theory descriptions instead of theory application.
7. Recommendations that do not follow from analysis.
8. Lack of connection to the chosen executive.
9. Missing assumptions.
10. Missing source criticism.

Create:
`07_recommendations/red_team_review.md`

Use this structure:
- Executive summary
- Main risks
- Claim-level problems
- Source-level problems
- Theory problems
- Recommendation problems
- Concrete fixes
- Likely oral exam questions
```

---

# 21. Suggested Final Report Structure

The final report should probably follow this structure:

```markdown
# Final Report Outline

## 1. Introduction
- Present Coop’s strategic situation.
- Explain why Coop App/Lobyco matters.
- Introduce selected executive.
- Present the main strategic question.

## 2. Case Background and Assumptions
- Coop App history.
- Lobyco spin-out.
- coop.dk closure.
- Physical-store dependency.
- Financial pressure.
- Assumptions about source age and relevance.

## 3. Source Criticism
- Explain that several sources are marketing sources.
- Explain how claims are used cautiously.
- Separate facts, claims and assumptions.

## 4. Strategic Situation
- Coop’s current challenge.
- App value vs financial pressure.
- Physical stores vs digital ambition.
- Competitor and market context.

## 5. Theory Application
- Apply DVC Framework.
- Apply Digital Business Model / Ecosystem perspective.
- Do not give long theory summaries.

## 6. Analysis
- What value does the app create?
- Where is evidence weak?
- What does Lobyco represent strategically?
- Is the app aligned with Coop’s store-based model?
- How should Coop think about chain differentiation?

## 7. Strategic Recommendations
- 2–5 recommendations.
- Each recommendation links to evidence, theory and source criticism.

## 8. Limitations and Critical Reflection
- Marketing-biased sources.
- Uncertain causality.
- Limited financial data.
- Unclear contribution of app to profitability.
- Need for assumptions.

## 9. Conclusion
- Clear answer to strategic question.
- Restate what Coop should do and why.
```

---

# 22. Possible Main Strategic Positions

Create this in:

```text
04_option_banks/strategic_position_options.md
```

## Options

| Option | Position | Pros | Cons / risks | Score |
|---|---|---|---|---:|
| 1 | Strengthen Coop App significantly | Builds on existing digital capability | May ignore financial pressure and marketing-biased evidence | 6 |
| 2 | Reduce app investment | Saves resources and focuses on core retail | May waste valuable digital capability | 5 |
| 3 | Sell Lobyco | Could release capital and simplify focus | May lose strategic capability and future retail media potential | 4 |
| 4 | Differentiate app strategy by chain | Fits different customer needs across 365discount, Kvickly, SuperBrugsen | More complexity | 9 |
| 5 | Hybrid: keep app/Lobyco but tie investment strictly to physical-store economics | Balanced, realistic and source-critical | Requires strong KPIs and governance | 10 |

Recommended starting position:

> Option 5: Keep the app/Lobyco capability, but tie further investment strictly to store economics, customer relevance, supplier-funded value and chain-specific differentiation.

---

# 23. Possible Executive Options

Create this in:

```text
04_option_banks/executive_options.md
```

## Options

| Option | Executive | Why it fits | Risk | Score |
|---|---|---|---|---:|
| 1 | CEO | Owns overall turnaround and strategic direction | Too broad; recommendations may become generic | 7 |
| 2 | Director of Communication, Marketing and Digital | Strong fit with app, loyalty, retail media and customer relationship | Less direct control over store operations and finance | 9 |
| 3 | CFO | Strong fit with financial pressure and investment discipline | Less direct fit with app strategy | 6 |
| 4 | Commercial Director / chain management | Strong fit with store traffic and chain differentiation | May underplay Lobyco and digital platform logic | 7 |

Recommended starting option:

> Director of Communication, Marketing and Digital.

Why:
- The issue is digital customer relationship, loyalty, app value, retail media and communication.
- The role can connect app strategy with customer relevance and brand/chain differentiation.
- Financial discipline can still be included through KPIs and governance.

---

# 24. Possible Theory Options

Create this in:

```text
04_option_banks/theory_options.md
```

## Options

| Option | Theory | Why it fits | Risk | Score |
|---|---|---|---|---:|
| 1 | DVC Framework | Direct fit with digital value creation, customer experience, relationship and relevance | Can become too positive if source criticism is weak | 9 |
| 2 | Digital Business Model Framework | Helps analyse app/Lobyco as business model capability | Requires clear explanation | 8 |
| 3 | Platform / ecosystem theory | Fits retail media, Lobyco and supplier/customer interactions | May overstate Coop’s platform maturity | 7 |
| 4 | Implementation theory | Fits execution risk and financial pressure | Less direct for app value | 7 |
| 5 | Porter / positioning | Good for competitor differentiation | Less digital-specific | 6 |
| 6 | Resource-based view | Good for Lobyco as capability | May be less central in course framing depending on slides | 6 |

Recommended starting combination:

> DVC Framework + Digital Business Model / Ecosystem perspective.

---

# 25. Quality Rules for Writing

The final writing should follow these rules:

## Avoid
- “Coop App is a huge success”
- “The sources prove”
- “Digital transformation is important”
- “Coop should use more AI”
- “The app increases profitability” unless evidence supports it
- Long theory explanations
- Too many models
- Generic recommendations

## Prefer
- “The source claims”
- “This indicates”
- “This suggests”
- “This should be treated cautiously”
- “The evidence supports app adoption, but not necessarily financial contribution”
- “Given Coop’s physical-store model...”
- “The strategic value depends on whether...”
- “The recommendation follows from...”

---

# 26. Progress Tracking Rules

Codex should update these files after meaningful work:

| Event | File to update |
|---|---|
| New option created | Relevant option bank |
| User chooses an option | Decision board + decision register + daily log |
| New source added | Source register |
| New claim added | Evidence register |
| Claim criticized | Claim reliability matrix |
| Recommendation generated | Recommendation bank |
| Recommendation chosen | Chosen recommendations + decision register |
| End of workday | Daily log |

---

# 27. What Codex Should Do First

Codex should proceed in this order:

## Step 1 — Build structure
Create the folder structure and starter files.

## Step 2 — Create decision system
Create:
- decision board
- decision register
- today’s daily log

## Step 3 — Create first option banks
Create:
- executive options
- theory options
- strategic position options

## Step 4 — Stop for user decision
Codex should not proceed to final analysis before the user chooses:
1. executive
2. theory combination
3. main strategic position

## Step 5 — Build evidence system
Create:
- source register
- evidence register
- source criticism file

## Step 6 — Extract case evidence
Use uploaded source material and user-provided notes.

## Step 7 — Build recommendation bank
Create 8–12 recommendations and let the user choose 2–5.

## Step 8 — Draft outline
Only after decisions are made.

## Step 9 — Draft report
After outline approval.

## Step 10 — Red-team review
Before final version.

---

# 28. Do Not Do This Yet

Codex should NOT immediately:
- write the final exam paper,
- choose all recommendations for the user,
- use many theories,
- accept marketing claims as facts,
- make claims without evidence,
- create a polished final report before the decision gates are completed.

---

# 29. Suggested First User Choices

The next useful choices for the user are:

1. **Who should the report advise?**
   - CEO
   - Director of Communication, Marketing and Digital
   - CFO
   - Commercial Director / chain management

2. **Which theories should be used?**
   - DVC only
   - DVC + Digital Business Model
   - DVC + Platform/ecosystem
   - Digital Business Model + implementation
   - Porter + DVC

3. **What strategic position should the paper take?**
   - Strengthen app
   - Reduce app
   - Sell Lobyco
   - Differentiate by chain
   - Hybrid: keep app/Lobyco but tie to physical-store economics

Recommended initial choices:
- Executive: Director of Communication, Marketing and Digital
- Theory: DVC + Digital Business Model / Ecosystem perspective
- Strategic position: Hybrid — keep app/Lobyco, but tie investments to store economics and customer relevance

But the system must let the user choose.

---

# 30. Final Reminder to Codex

The user wants control.

The workflow must therefore be:

```text
Generate options → explain pros/cons → recommend → wait for user choice → log decision → continue
```

The strongest feature of this project is not just the agents.

It is the combination of:

1. **agent roles,**
2. **decision gates,**
3. **option banks,**
4. **daily logging,**
5. **source criticism,**
6. **red-team review,**
7. **final exam alignment.**

This is what will make the exam project more controlled, defensible and high quality.
