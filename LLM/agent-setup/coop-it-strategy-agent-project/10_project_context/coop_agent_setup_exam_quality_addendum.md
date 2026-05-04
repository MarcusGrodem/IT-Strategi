# Coop Agent Setup — Exam Quality Addendum

This addendum must be applied before creating the Coop IT-strategy agent project setup.

It incorporates the written assignment requirements and informal quality criteria from the exam slides. The goal is to make the agent workflow evaluate the project as an exam paper, not only as a strategy analysis.

---

# 1. Assignment Requirements To Build Into The Workflow

The written exam paper should:

- Be 5-25 pages in Danish or English.
- Analyse a company where digital opportunities are central.
- Treat the company as being in a strategically interesting situation, for example due to changed customer needs, changed competition, or new technological opportunities.
- Demonstrate that the students can apply theory, concepts and perspectives meaningfully and in detail to a real case.
- Use 1-2 self-selected course perspectives only.
- Use these perspectives to formulate strategic advice to an actor in the case.

For the Coop project, this means:

- The paper must advise a clearly chosen actor, not "Coop" in general.
- The paper must stay focused on the strategic role of Coop App and Lobyco in Coop's current situation.
- Digital opportunity must be connected to strategic tension: financial pressure, physical-store dependency, customer loyalty, competitor pressure and the uncertain value contribution of the app.
- Theoretical perspectives must be applied to Coop, not described generically.

---

# 2. Writing And Argumentation Rules

Every analytical section should use this structure:

```text
Claim -> Reasoning -> Empirical observations -> Strategic implication
```

Use the exam-slide version as a writing rule:

```text
i) Paastand
ii) Begrundelse
iii) Empiriske observationer
```

In practice:

| Element | Meaning | Example |
|---|---|---|
| Claim | What the section argues | "The Coop App should be evaluated through store economics, not adoption alone." |
| Reasoning | Why this follows analytically | "Coop has closed coop.dk and now sells through physical stores." |
| Empirical observations | What case/source material supports it | "The exam case states that coop.dk closed due to lack of profitability." |
| Strategic implication | What this means for the advised actor | "The digital director should require KPIs tied to store traffic, basket size and supplier-funded value." |

Agents must avoid unsupported jumps from evidence to recommendation.

Bad:

> Lobyco claims many app users, therefore Coop should invest more in the app.

Better:

> Lobyco claims high app adoption. This indicates potential customer reach, but it does not by itself prove profitability. Therefore, further app investment should be tied to store-level value indicators.

---

# 3. Depth Over Breadth Rule

The exam explicitly rewards depth over breadth.

Therefore:

- Do not include many theories.
- Do not include long lists of generic digital trends.
- Do not create a broad "digital transformation" paper.
- Prefer one overall convincing argument with source-critical nuance.
- Use competitors only where they sharpen the Coop analysis.
- Use theory only where it changes the interpretation of the case.

Recommended depth focus:

```text
Main argument:
Coop should keep Coop App/Lobyco as strategic assets only if they are governed as instruments for physical-store value creation, chain differentiation and customer relevance under financial pressure.
```

---

# 4. Required Paper Structure

The final report should use a traditional academic/strategy structure:

1. Introduction and case presentation
2. Chosen actor and strategic question
3. Choice and justification of 1-2 theoretical perspectives
4. Source criticism and assumptions
5. Analysis using the selected perspectives
6. Analytical results
7. Strategic recommendations
8. Limitations and critical reflection
9. Conclusion
10. References, using a systematic citation style such as APA 7

The perspectives may be handled:

- separately, if this gives clarity, or
- interwoven, if this gives a stronger argument.

The chosen approach must be explained briefly in the paper.

---

# 5. Perspective Choice Must Be Justified

The paper must explicitly justify why the selected course perspectives are used.

Each chosen theory should answer:

| Question | Required answer |
|---|---|
| Why this perspective? | Explain why it fits the Coop App/Lobyco problem. |
| What does it reveal? | Explain what analytical insight it gives. |
| What does it not reveal? | Explain its limitation. |
| How is it used? | Explain that it structures the analysis, not just the theory section. |

Example:

> The DVC Framework is relevant because the case concerns digital value creation through customer experience, relationships, relevance and digital infrastructure. However, it may overemphasise digital value potential if it is not combined with source criticism and financial realism.

---

# 6. Critical Reflection Rule

The paper must openly discuss doubt, limitations and criticism of its own analysis.

This must include:

- source bias from Lobyco, Shortcut and Playable,
- uncertainty about whether app engagement creates profitability,
- possible selection bias in claims about app users,
- limited access to internal Coop financial and KPI data,
- risk that Coop App creates complexity rather than differentiation,
- risk that digital initiatives distract from price, logistics and store execution.

Useful wording:

- "This interpretation is limited by..."
- "The source is useful for understanding intended value, but not as proof of realised profitability."
- "An alternative interpretation is..."
- "This recommendation depends on the assumption that..."

---

# 7. Reference And AI Transparency Requirements

The workflow must include reference discipline.

Rules:

- Maintain a source register.
- Maintain an evidence register.
- Use a systematic citation style, preferably APA 7.
- Separate references for case sources and theory sources if useful.
- Track where generative AI contributed to structure, option generation or wording.
- Do not invent sources or page numbers.
- Mark missing bibliographic data as unresolved instead of guessing.

Create or update these files in the project setup:

```text
05_evidence/source_register.md
05_evidence/evidence_register.md
05_evidence/reference_needs.md
08_final_report/ai_use_statement.md
08_final_report/final_quality_check.md
```

---

# 8. Informal Quality Criteria Checklist

The final paper should be checked against these criteria:

| Criterion | Required check |
|---|---|
| Learning objectives | Does the paper show mastery of course learning objectives? |
| Independent voice | Does the paper present the authors as independent and authoritative, rather than repeating source claims? |
| Course material | Does it use relevant course concepts or frameworks? |
| Clear focus | Does it have a clear focus and relevant limitations? |
| Overall argument | Does it contain one convincing overall argument? |
| Critical approach | Does it discuss advantages and limitations? |
| Application | Does it apply, discuss and reflect, not only present and explain? |
| Meta communication | Does each major section explain what happens next and why? |

This checklist must be included in:

```text
08_final_report/final_quality_check.md
07_recommendations/red_team_review.md
```

---

# 9. Agent Setup Changes

Do not add an eighth agent unless necessary. Instead, strengthen Agent 1 and Agent 7.

## Agent 1 — Exam Architect: Add Responsibilities

Agent 1 must also:

- Convert the exam assignment into project constraints.
- Ensure the paper advises one clear actor.
- Ensure the paper has one overall argument.
- Ensure each section follows Claim -> Reasoning -> Evidence -> Strategic implication.
- Ensure the selected perspectives are justified.
- Ensure depth over breadth.
- Maintain a final report structure that matches exam expectations.
- Create `08_final_report/final_quality_check.md` early, not only at the end.

## Agent 7 — Red Team Agent: Add Responsibilities

Agent 7 must also check:

- Is the paper too broad?
- Does it lack one overall argument?
- Are theories merely described instead of applied?
- Is the actor unclear?
- Are the recommendations generic?
- Does the paper contain enough critical reflection?
- Does it have meta communication between sections?
- Are references and AI-use transparency handled?

---

# 10. New Files To Add To The Initial Setup

When the project structure is created, include these additional files:

```text
05_evidence/reference_needs.md
08_final_report/ai_use_statement.md
08_final_report/final_quality_check.md
09_codex_prompts/exam_quality_prompt.md
```

---

# 11. Exam Quality Prompt

Save this as:

```text
09_codex_prompts/exam_quality_prompt.md
```

Prompt:

```markdown
Review the current Coop IT-strategy project against the exam assignment and informal quality criteria.

Check:
1. Does the project advise one clear actor in the case?
2. Does it use only 1-2 course perspectives?
3. Are the chosen perspectives justified?
4. Does the project have one overall convincing argument?
5. Does each analytical section use claim, reasoning and empirical observations?
6. Does the analysis apply, discuss and reflect instead of only presenting theory?
7. Is the paper critical about source bias, weak causality and limitations?
8. Is the scope deep rather than broad?
9. Are strategic recommendations connected to evidence and theory?
10. Are references and AI-use transparency handled according to the course rules?

Update:
- 08_final_report/final_quality_check.md
- 07_recommendations/red_team_review.md, if relevant

Do not write new analysis unless the check identifies a specific gap.
```

---

# 12. Updated First Codex Task

The first setup prompt should be amended with this rule:

```markdown
Before creating the first option banks, apply `coop_agent_setup_exam_quality_addendum.md`.

The setup must include:
- the original decision system,
- the source criticism system,
- the daily logging system,
- the option banks,
- the exam quality checklist,
- reference tracking,
- AI-use transparency tracking,
- and a final quality gate based on the exam slides.

Do not write the final paper yet.
Do not make final choices for the user.
Stop after creating the setup and first option banks.
```

