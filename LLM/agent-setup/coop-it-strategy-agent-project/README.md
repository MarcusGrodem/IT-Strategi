# Coop IT-Strategy Agent Project — How To Use This Setup

This folder is a controlled workspace for the Coop IT-strategy exam project.

The setup is designed so the project does not jump straight into writing a final paper. Instead, it keeps options open, builds evidence, criticises sources and lets the user make informed choices later.

## The Basic Workflow

Use the project in this order:

```text
1. Read project context
2. Build evidence and source criticism
3. Analyse Coop's strategic situation
4. Compare open advisory/theory/stance options
5. User chooses the direction
6. Log decisions
7. Develop 2-5 recommendations that follow from the analysis
8. Red-team the argument
9. Draft final paper
```

The assignment logic is:

```text
Strategic situation analysis -> 2-5 recommendations in continuation of that analysis
```

## Current Important Rule

The user has explicitly decided not to choose executive, theory or strategic position yet.

These are still open:

- executive to advise,
- course perspectives,
- main strategic position.

Do not treat recommended options as chosen options.

Also: do not generate final recommendations before the strategic situation analysis is developed.

## Key Files

| File / folder | Purpose |
|---|---|
| `00_project_brief.md` | Short overview of the project, case and exam constraints |
| `01_decision_board.md` | Shows which major choices are open, proposed or chosen |
| `02_decision_register.md` | Records final user decisions only |
| `03_daily_logs/` | Daily progress and decision logs |
| `04_option_banks/` | Alternatives the user can choose between later |
| `05_evidence/` | Claims, sources, reliability and source criticism |
| `06_analysis/` | Analysis files, created after enough evidence exists |
| `07_recommendations/` | Recommendation options and red-team review |
| `08_final_report/` | Outline, drafts, final quality check and AI-use statement |
| `09_codex_prompts/` | Reusable prompts for later Codex/LLM sessions |
| `10_project_context/` | Handoff, exam-quality addendum and workflow policy |

## Decision Gates

The project has decision gates. Do not skip them.

| Gate | User eventually chooses | Current status |
|---|---|---|
| Gate 1 | Executive to advise | Under evaluation |
| Gate 2 | Main strategic position | Under evaluation |
| Gate 3 | Course perspectives | Under evaluation |
| Gate 4 | Competitor focus | Open |
| Gate 5 | Final recommendations | Open |
| Gate 6 | Final structure and tone | Open |

## How The Agents Should Be Used

### 1. Exam Architect

Use this agent to:

- keep the project aligned with the exam assignment,
- maintain the decision board,
- ensure there is one overall argument,
- prevent theory overload,
- check that advice is aimed at one actor.

Main files:

- `00_project_brief.md`
- `01_decision_board.md`
- `04_option_banks/*.md`
- `08_final_report/final_quality_check.md`

### 2. Evidence Extractor

Use this agent to:

- extract facts and claims,
- separate source claims from interpretation,
- collect key numbers,
- avoid judging reliability.

Main files:

- `05_evidence/evidence_register.md`
- `05_evidence/raw_case_claims.md`
- `05_evidence/key_numbers.md`

### 3. Source Critic / Bias Agent

Use this agent to:

- classify sources and claims,
- identify marketing bias,
- identify weak causality,
- rewrite overconfident claims cautiously.

Main files:

- `05_evidence/source_register.md`
- `05_evidence/source_criticism.md`
- `05_evidence/claim_reliability_matrix.md`

### 4. Competitor & Market Agent

Use this agent to:

- compare Coop with relevant competitors,
- check whether competitors win through apps, price, logistics, loyalty, store formats or simplicity,
- make sure competitor evidence sharpens the Coop argument without making the paper too broad.

Main files:

- `05_evidence/competitor_evidence.md`
- `06_analysis/competitor_analysis.md`
- `04_option_banks/competitor_insight_options.md`

### 5. Theory Application Agent

Use this agent to:

- compare theory options,
- explain what each theory reveals and misses,
- apply theory directly to Coop,
- avoid long generic theory sections.

Main files:

- `04_option_banks/theory_options.md`
- `04_option_banks/theory_comparison.md`
- `06_analysis/dvc_analysis.md`
- `06_analysis/digital_business_model_analysis.md`
- `06_analysis/theory_to_evidence_matrix.md`

### 6. Recommendation Agent

Use this agent later, not yet.

Use it after evidence and analysis are stronger, to:

- generate 8-12 recommendation options,
- link each recommendation to evidence and theory,
- let the user choose 2-5 final recommendations.

Main files:

- `04_option_banks/recommendation_options.md`
- `07_recommendations/recommendation_bank.md`
- `07_recommendations/chosen_recommendations.md`

### 7. Red Team Agent

Use this agent before drafting and before final submission.

It should challenge:

- overuse of marketing sources,
- weak causality,
- unclear actor,
- too many theories,
- generic recommendations,
- lack of critical reflection,
- missing references,
- missing AI-use transparency.

Main files:

- `07_recommendations/red_team_review.md`
- `08_final_report/final_quality_check.md`
- `08_final_report/examiner_questions.md`

## How To Continue In A Later LLM/Codex Session

Start by asking the LLM to read:

1. `README.md`
2. `10_project_context/workflow_decision_policy.md`
3. `01_decision_board.md`
4. `03_daily_logs/2026-05-03.md`
5. relevant files in `04_option_banks/` and `05_evidence/`

Suggested prompt:

```markdown
Read README.md, workflow_decision_policy.md, the decision board and today's daily log first.

Important: executive, theory and strategic position are not chosen yet. Use the remaining agents to build evidence and comparisons before asking me to choose.

Continue with the next small step only, update the daily log, and do not write the final paper.
```

## Prompt For Multi-Angle Overview

Use this prompt when you want a later LLM to create a broad overview of possible case angles before choosing:

`09_codex_prompts/multi_angle_html_case_report_prompt.md`

It asks the LLM to create an HTML report grouped by advised actor, with at least three possible angles per actor, supporting evidence, counterarguments, theory use and source-use notes.

## When To Ask The User To Choose

Ask the user to choose only after:

- evidence has been extracted,
- source criticism has been completed,
- competitor evidence has been outlined,
- theory options have been compared,
- the consequences of each strategic position are clear.

Until then, keep choices marked as `Under evaluation`.
