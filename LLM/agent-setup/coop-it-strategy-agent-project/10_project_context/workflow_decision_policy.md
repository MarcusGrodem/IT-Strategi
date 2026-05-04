# Workflow Decision Policy

## Important User Preference

The user does not want to choose executive, theory or strategic position immediately.

The purpose of the agent setup is to preserve alternatives and let the user weigh them later after more evidence, source criticism, competitor comparison and theory evaluation.

Therefore:

- Do not treat recommended options as chosen options.
- Do not lock the executive, theory or strategic position without explicit user confirmation.
- Do not begin writing the final report as if the recommended options were final.
- Use the remaining agents to create comparison material before asking the user to choose.

## Current Open Decision Gates

| Decision | Status | Why still open |
|---|---|---|
| Executive to advise | Under evaluation | User wants to compare how each actor changes the paper |
| Course perspectives | Under evaluation | User wants to understand what each theory reveals and hides |
| Strategic position | Under evaluation | User wants to weigh options after evidence and source criticism |

## How Remaining Agents Should Be Used

### Evidence Extractor

Collect case facts and claims relevant to each open option. Do not judge reliability.

### Source Critic / Bias Agent

Classify evidence reliability, bias and claim type. This is essential before choosing a strategic position.

### Competitor & Market Agent

Clarify whether competitor pressure supports a digital, price, store-format, loyalty or hybrid argument.

### Theory Application Agent

Compare theory options by showing:

- what each perspective reveals,
- what it misses,
- how well it fits the Coop case,
- how well it supports exam criteria.

### Recommendation Agent

Do not create final recommendations yet. First create possible recommendation directions linked to each strategic position.

### Red Team Agent

Challenge each option and identify which ones risk producing a weak exam paper.

## Next Best Step

Create comparison files that help the user choose later:

```text
04_option_banks/executive_comparison.md
04_option_banks/theory_comparison.md
04_option_banks/strategic_position_comparison.md
```

These files should compare the consequences of each choice, not lock a choice.

