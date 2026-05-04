# Prompt — Multi-Angle HTML Case Report

Use this prompt with a later LLM/Codex session when the user wants an overview of possible angles for the Coop case.

```markdown
You are helping me explore possible angles for an IT-strategy exam paper about Coop Denmark, Coop App and Lobyco.

Read these files first:

1. `README.md`
2. `10_project_context/workflow_decision_policy.md`
3. `10_project_context/agent_usage_guide.md`
4. `01_decision_board.md`
5. latest file in `03_daily_logs/`
6. all files in `04_option_banks/`
7. all files in `05_evidence/`
8. relevant starter analysis files in `06_analysis/`
9. `10_project_context/imported_competitor_scrape_2026-05-03.md`

Important:

- Do not lock the executive, theory or strategic position.
- The purpose is to create overview and choice material.
- Do not write the final exam paper.
- Do not present recommended options as final decisions.
- Follow the official assignment logic: first analyse Coop's strategic situation, then develop possible 2-5 recommendations that would follow from each angle.

## Task

Create an HTML report that maps many possible angles for analysing the Coop case.

The report must be grouped by who the paper could advise.

Use exactly these case-specified advised actors:

1. Adm. direktor / CEO: Thor Skov Jorgensen
2. Direktør SuperBrugsen og Kvickly: Rikke Krause
3. Direktør Brugsen: Torben B. Andersen
4. Direktør 365discount: Michael Tilsted
5. Direktør for Kommunikation, Marketing og Digital: Martin Hasgard Olesen

For each advised actor, give at least 3 different analytical angles.

For each angle, include:

- angle title,
- short strategic question,
- possible main claim,
- facts/evidence that support the claim,
- facts/evidence that can be used to argue against or nuance the claim,
- relevant theory/perspective from the course,
- which of the five lecturer-provided supplementary sources are relevant,
- source criticism notes,
- what kind of 2-5 recommendations this angle would likely lead to after the strategic situation analysis,
- exam risk,
- what additional evidence is needed before choosing this angle.

## Required Source Rule

Use the five supplementary sources provided by the lecturer as the starting point.

The five expected source categories are:

1. Exam/case material about Coop
2. DVC Framework source
3. Hedman & Bjoern-Andersen 2016 / historical Coop IT source
4. Lobyco source
5. Supplier/developer/marketing sources such as Playable and Shortcut, if these are part of the provided source package

If the actual folder/project identifies a different list of five lecturer-provided sources, use that actual list instead.

For every angle, explicitly state which of the five supplementary sources are used.

If one of the five sources is not used for an angle, state explicitly:

> Not used: [source name] — reason: [brief reason]

If one of the five sources cannot be found in the project, state:

> Source missing/unverified: [source name] — cannot be used as evidence until located.

Do not invent source details, page numbers or exact quotations.

## Evidence And Counterargument Rule

For every angle, include both:

1. Evidence supporting the angle.
2. Evidence or criticism that weakens the angle.

Examples of useful counterargument evidence:

- app adoption does not prove profitability,
- Lobyco/Playable/Shortcut are commercially interested sources,
- competitor evidence suggests digital tools matter only when fitted to business model,
- Coop's financial pressure may make broad app investment risky,
- Nemlig shows online grocery still has difficult economics,
- REMA/Lidl may win through price and simplicity, not app sophistication.

## Theory Rule

Apply theory from the course. Do not only describe theory.

Use relevant theories from these options:

- DVC Framework
- Digital Business Model perspective
- Platform / ecosystem perspective
- Porter / positioning
- Implementation perspective
- Resource-based view, only if appropriate and course-relevant

For every angle, show:

```text
Theory concept -> Coop observation -> analytical meaning -> strategic implication
```

Do not use more than 1-2 theories per angle.

## HTML Output Requirements

Create a standalone HTML file:

`08_final_report/multi_angle_case_overview.html`

The HTML must include:

- title,
- short executive summary,
- a section explaining the official assignment logic: strategic situation analysis before recommendations,
- table of contents with anchor links,
- one section per advised actor,
- at least 3 angle cards/tables per actor,
- source-use table,
- comparison table of the strongest possible angles,
- final "open decisions" section,
- final "missing evidence" section.

Design requirements:

- Clean academic style.
- Easy to scan.
- Use tables where useful.
- No decorative fluff.
- Use CSS inside the HTML file.

## Tone

Write in clear English or Danish/Norwegian-friendly academic English.

Use careful source language:

- "claims"
- "indicates"
- "suggests"
- "should be treated cautiously"
- "supports adoption, but not necessarily profitability"

Avoid:

- "proves"
- "the app is a huge success"
- "digital transformation is important" without case-specific meaning
- unsupported profitability claims

## Final Reminder

This HTML report is an overview tool for choosing a direction later.

It must not make final choices for the user.
It must not present final recommendations before explaining the strategic situation analysis behind them.
```
