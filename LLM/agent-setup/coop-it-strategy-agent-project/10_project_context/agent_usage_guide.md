# Agent Usage Guide

This guide explains how to use the Coop agent structure without losing overview.

## What This Project Is

This is not a single automated writing task.

It is a staged exam-writing workflow:

```text
Evidence -> source criticism -> strategic situation analysis -> comparison -> user choice -> 2-5 recommendations -> final report
```

The main value is that the user can choose later after seeing how different perspectives affect the strategic situation analysis and the recommendations that follow from it.

## Where To Start Each Time

When returning to the project, read these files first:

1. `README.md`
2. `01_decision_board.md`
3. latest file in `03_daily_logs/`
4. `10_project_context/workflow_decision_policy.md`
5. the relevant option/comparison files in `04_option_banks/`

## Current Stage

The project is currently in the setup and evidence-building stage.

Completed:

- folder structure,
- project brief,
- decision board,
- daily log,
- option banks,
- comparison files,
- starter evidence register,
- source criticism,
- competitor starter structure,
- exam-quality checklist.
- official assignment alignment,
- strategic situation analysis starter.

Not completed:

- final executive choice,
- final theory choice,
- final strategic position,
- verified source extraction,
- sourced competitor research,
- full analysis,
- recommendation bank,
- final report.

## How To Use The Seven Agents

### Step 1: Exam Architect

Use when the project needs structure or decisions.

Ask:

> Does the current work still fit the exam assignment and decision gates?

Output:

- update decision board,
- update project brief,
- update option banks,
- update final quality check.

### Step 2: Evidence Extractor

Use when reading case material or sources.

Ask:

> What facts and claims can be extracted, without judging them yet?

Output:

- update evidence register,
- update raw case claims,
- update key numbers.

### Step 3: Source Critic

Use after evidence extraction.

Ask:

> Which claims are facts, claims, marketing claims, assumptions or inferences?

Output:

- update source criticism,
- update claim reliability matrix,
- rewrite risky statements carefully.

### Step 4: Competitor & Market Agent

Use before choosing strategic position.

Ask:

> What competitor evidence changes how we should understand Coop App and Lobyco?

Output:

- competitor evidence,
- competitor analysis,
- competitor insight options.

### Step 5: Theory Application Agent

Use before choosing theories.

Ask:

> What does each theory reveal, and what does it miss?

Output:

- theory comparison,
- theory-to-evidence matrix,
- draft theory application files.

### Step 6: Recommendation Agent

Use only after evidence, source criticism and strategic situation analysis.

Ask:

> What strategic recommendations follow from the evidence and selected theory?

Output:

- recommendation options,
- recommendation bank,
- chosen recommendations after user choice.

### Step 7: Red Team Agent

Use before final decisions and before final submission.

Ask:

> What would an examiner criticize?

Output:

- red team review,
- examiner questions,
- final quality check updates.

## The Most Important Discipline

Do not move too fast from claims to recommendations. The assignment requires analysis first, then recommendations in continuation of that analysis.

Always use:

```text
Claim -> Reasoning -> Empirical observations -> Strategic implication
```

## How To Know When The User Should Choose

The user should choose executive, theory and strategic position only when these files are reasonably developed:

- `05_evidence/evidence_register.md`
- `05_evidence/source_criticism.md`
- `05_evidence/claim_reliability_matrix.md`
- `05_evidence/competitor_evidence.md`
- `06_analysis/competitor_analysis.md`
- `04_option_banks/theory_comparison.md`
- `04_option_banks/strategic_position_comparison.md`

## Suggested Next Prompt

```markdown
Continue with one small step.

Read README.md, agent_usage_guide.md, workflow_decision_policy.md and the latest daily log first.

Do not lock executive, theory or strategic position.

Use the relevant agent for the next step, update the relevant files, and update the daily log.
```
