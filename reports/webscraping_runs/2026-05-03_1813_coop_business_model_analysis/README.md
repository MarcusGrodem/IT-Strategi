# 2026-05-03_1813_coop_business_model_analysis

## Purpose

This run investigates Coop Denmark's business model, strategic positioning, customer value proposition, member organisation, app/Lobyco model and evidence-based tensions for a CBS IT-strategy exam project. It does not contain recommendations.

## Method

- Crawl4AI scraped public web sources on 2026-05-04. Where Crawl4AI returned a Markdown/JSON `NoneType` error for accessible public HTML pages, a documented urllib/BeautifulSoup fallback was used and marked inside the raw source file.
- The two user-supplied Coop annual-report PDFs were extracted locally with `pypdf`.
- Raw sources were saved as one Markdown file per source in `raw_sources/`.
- Structured findings and source criticism were written to `data/`.
- Final Markdown and PDF summaries were written to `final_outputs/`.

## Files created

- `raw_sources/*.md`: raw extracted source Markdown/text with URL, access date, title, publisher and source type.
- `data/coop_business_model_findings.csv` and `.json`: structured evidence rows mapped to business model, IT-strategy and positioning lenses.
- `data/source_register.csv` and `.json`: source classification, reliability and bias assessment.
- `final_outputs/coop_business_model_analysis.md`: full evidence-based analysis.
- `final_outputs/coop_key_takeaways_summary.pdf`: two-page exam summary.
- `final_outputs/coop_business_model_one_page.md`: one-page summary.
- `logs/crawl4ai_scrape.log`: Crawl4AI run log.
- `logs/pdf_extract.log`: PDF extraction log.

## Notes

Marketing/vendor sources, especially Lobyco, are marked as such in the CSV files. Their numbers are included where useful but interpreted cautiously. App-store extraction may be partial and is not used for key strategic claims. No login, paywall, CAPTCHA or private data was used.
