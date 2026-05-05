# Fact check: Lobyco Coop Denmark case study

Source checked: `helping_25_percent_danish_households_shop_smarter_lobyco.md` / https://www.lobyco.com/case-studies/coop

Checked on: 2026-05-05

## Bottom line

Use the Lobyco case study as a vendor/marketing source, not as a standalone factual source for precise metrics.

The broad story is credible: Coop Denmark has a large app-based loyalty program with Scan & Pay, bonus, personalised offers, local store content, and high usage. But several headline claims are either internally inconsistent, stale, or not independently verifiable from public sources.

## Claim checks

| Lobyco claim | Assessment | Evidence and notes |
|---|---:|---|
| "More than 1.8 million users" / "1.8M members" | Partly supported, but wording is imprecise | Coop itself reported 1.8m members in 2018, while its App Store version history currently says about 1.5m app users. Coopforum says the app has been downloaded by more than 2m Danes, with about 250k daily users and more than 500k weekly users. Treat "1.8m" as likely member-scale or historical user-scale, not a clearly dated active-user metric. |
| "Equivalent to 25% of all Danish households" | Weak / mathematically inconsistent | Statistics Denmark table FAM55N gives 2,878,144 households on 1 Jan 2026. 25% is about 719,536 households. 1.8m divided by 2,878,144 is about 62.5%, not 25%. The 25% figure may come from an older agency case page, but it does not reconcile with current household counts. |
| "Two years ago Coop launched the Coop app" | Stale / likely wrong if read in 2026 | Coop reported more than 800k app downloads in May 2018. The current Apple App Store page has version history and copyright context showing the app was long-established before 2024. This phrasing likely survived from an old case study and should not be reused as current chronology. |
| "50% increased traffic" / "50% growth in repeat customer rate" / "50% higher frequency" | Not independently verified | Lobyco uses multiple labels for the same 50% number. A former NoA Ignite case snippet repeats "50% higher frequency among members", but I found no public Coop primary metric or audited source confirming the method, time period, or baseline. Use only with attribution to Lobyco. |
| "21% extra in-store spend from Prepaid Food / FordelsKonto users" | Not independently verified | Public Coop pages confirm FordelsKonto exists and can give up to 15% bonus on selected Coop brands, but I did not find a public Coop source confirming the 21% uplift, sample, or time period. |
| "No. 1 in App Store and Google Play" | Not verified | The live Google Play listing shows 1M+ downloads and current app details, but not a historical No. 1 rank. App-store ranks are time- and category-sensitive; without a date, country, category, and screenshot/export, this is not usable as a factual claim. |
| Lobyco identity: A/S, CVR 41480025 | Supported | Lobyco's own footer and Danish company-data mirrors using CVR/Virk data identify Lobyco A/S with CVR 41480025. Address data has changed over time, so cite a dated source if address matters. |

## Useful replacement wording

Safer phrasing:

> Lobyco presents Coop Denmark as a major loyalty-app case, citing 1.8m+ users and uplift metrics. Public Coop sources support that the Coop app is widely adopted, with more than 2m downloads, about 250k daily users and more than 500k weekly users, but Lobyco's exact 25%-of-households and uplift claims should be treated as vendor-provided and not independently verified.

## Sources checked

- Lobyco case study: https://www.lobyco.com/case-studies/coop
- Lobyco company page: https://www.lobyco.com/company
- Statistics Denmark StatBank FAM55N, Households 1 January: https://m.statbank.dk/TableInfo/FAM55N?lang=en
- Coopforum, membership programme and Coop app: https://coopforum.dk/staerke-lokale-faellesskaber/medlemsprogram-og-medlemsapp/
- Coop/Ritzau press release, 2018 app/member figures: https://via.ritzau.dk/pressemeddelelse/12752219/coop-og-topdanmark-gar-sammen-om-digitalt-salg-af-forsikringer
- Google Play listing for Coop app: https://play.google.com/store/apps/details?hl=en&id=dk.coop.coopplus
- Apple App Store listing for Coop app: https://apps.apple.com/gb/app/coop-scan-pay-app-offers/id698632628

## Method note

The Crawl4AI skill was consulted, but the local `crwl` CLI was not installed in this environment. I used direct web retrieval and the public Statistics Denmark API instead. Household denominator calculation from FAM55N:

| Year | Danish households | 25% of households | 1.8m as share of households |
|---:|---:|---:|---:|
| 2024 | 2,834,240 | 708,560 | 63.5% |
| 2025 | 2,857,302 | 714,325 | 63.0% |
| 2026 | 2,878,144 | 719,536 | 62.5% |
