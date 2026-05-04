# Web scraping run: Coop competitor analysis

Run started: 2026-05-03 16:19 Europe/Copenhagen.

Purpose: gather, structure and analyze public evidence about selected Coop competitors for the IT-strategy exam case. This is evidence gathering and competitor analysis only; it does not recommend what Coop should do.

## What was scraped
Crawl4AI was used for public pages from Coop Danmark, Salling Group, Netto, Bilka, føtex, REMA 1000, Lidl Denmark, Dagrofa, MENY/SPAR app pages, Nemlig, Loyalty Group and Dansk Industri. The source list is in `logs/source_urls.tsv`.

## Files created
- `raw_sources/`: one Markdown file per scraped source, with source URL and access metadata.
- `data/competitor_findings.csv`: structured competitor findings.
- `data/source_register.csv`: source register with reliability/source-criticism notes.
- `final_outputs/competitor_analysis.md`: full evidence report with clickable source links and Coop benchmark figures.
- `final_outputs/key_takeaways_summary.md`: Markdown summary fallback.
- `final_outputs/key_takeaways_summary.html`: browser/print-friendly key takeaways summary with colored KPI cards, bar charts and clickable source links.
- `final_outputs/key_takeaways_summary.pdf`: compact two-page PDF summary, but the generated PDF may render empty in some viewers; use the HTML file as the reliable version.
- `logs/crawl.log`: crawl execution log.

## Limitations
- The Dagrofa annual-report PDF URL was crawled, but Crawl4AI extracted only metadata. Dagrofa's official 2025 results article was used for extracted figures.
- The Coop annual-report PDF URL was crawled, but Crawl4AI extracted only metadata. Coop's official 2025 results page was used for extracted comparison figures, and the PDF was downloaded into `raw_sources/`.
- Some sources are official press releases or app pages and are therefore marketing-heavy.
- REMA market-share data is reported from Retail Institute via Ritzau/NI and is disputed by Salling in the same article.
- Lidl Denmark official current financial figures were not found during this run.
