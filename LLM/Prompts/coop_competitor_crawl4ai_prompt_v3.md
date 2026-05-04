# Web scraping prompt – Coop competitor analysis with Crawl4AI

Use this prompt in Codex after starting Codex in your project folder.

First activate the relevant skill, for example:

```text
$crawl4ai
```

Then paste the full prompt below.

---

```text
Use the crawl4ai skill.

Context:
This is for an IT-strategy exam project at CBS about Coop Denmark. The case is not asking for a general business report, but an IT-strategy analysis. Coop has invested heavily in the Coop App and Lobyco, but closed coop.dk as an online grocery store in 2023 due to lack of profitability. The exam project must use course theory meaningfully, with empirical observations, and must be critical toward marketing-heavy sources.

Important limitation:
Do NOT write strategic recommendations for Coop yet.
Do NOT propose what Coop should do.
The purpose of this task is only to gather, structure, and analyze evidence about Coop’s competitors:
- who they are
- why they may be succeeding relative to Coop
- what their customer-facing digital solutions do differently
- what the statistics say
- what patterns can be observed across competitors

Main research question:
Why do selected competitors in the Danish grocery/retail market appear to succeed better than Coop, and what do their digital/customer-facing solutions do differently?

Use Crawl4AI to research and scrape public web sources.

Target companies:
1. Salling Group: Netto, Føtex, Bilka
2. Rema 1000 Denmark
3. Lidl Denmark
4. Dagrofa: MENY, SPAR, Min Købmand, Let-Køb
5. Nemlig.com
6. Any other clearly relevant Danish grocery competitor or digital grocery player if evidence suggests relevance

Research focus:
For each competitor, investigate:

1. Strategic position
- How is the competitor positioned in the Danish grocery market?
- Is the competitor mainly discount, omnichannel, online-first, convenience, premium, or ecosystem-oriented?
- What is the customer value proposition?

2. Digital customer solution
- App features
- Loyalty program
- Personalized offers
- Scan/self-checkout
- Online shopping/e-commerce
- Delivery/click-and-collect
- Retail media
- Data use and personalization
- Integration between physical stores and digital channels

3. Business results and statistics
Find recent and reliable statistics where available:
- revenue
- profit/loss
- market share
- growth/decline
- store count
- app downloads/users/rankings if available
- e-commerce growth
- customer satisfaction or loyalty indicators
- basket size, frequency, or repeat purchase indicators if available

4. Why they may succeed relative to Coop
Do not make loose claims.
For each competitor, identify evidence-based reasons such as:
- simpler and clearer value proposition
- stronger discount positioning
- better operational execution
- better omnichannel integration
- stronger e-commerce model
- better loyalty/app economics
- better alignment between digital solution and core business
- better implementation discipline
- stronger economies of scale
- clearer brand architecture
- stronger use of data/customer relationships

5. Compare specifically to Coop
Use Coop as comparison point, but do not solve Coop.
Look for contrasts such as:
- Coop app success vs Coop group financial weakness
- Coop digital frontrunner narrative vs closed online grocery store
- Coop’s multiple chains vs competitors’ clearer chain concepts
- Coop’s app/loyalty focus vs competitors’ pricing, logistics, scale, store model, or online model
- Coop’s digital relationship strength vs possible lack of operational/profitability fit

Course theory lenses:
Use the following IT-strategy perspectives as analytical lenses, but do not over-explain theory. Use them to structure observations.

A. Digital Business Model Framework / digital business models
Look especially for:
- customer knowledge
- controlled value chain vs ecosystem/network
- whether the competitor behaves like omnichannel, supplier, ecosystem driver, or modular producer
- whether the digital solution creates something new and compelling for customers, not just “being digital”

B. Digital Value Creation framework
Structure observations around:
- Experiences: how the solution improves the shopping experience
- Relationships: how the solution builds loyalty, personalization, and repeat interaction
- Evolution: how the competitor adapts to changing customer behavior
- Digital competences, digital infrastructure, and digital outputs

C. Strategic positioning
Look for whether competitors perform different activities from Coop, or similar activities in different ways.

D. Implementation
Only use this where evidence exists.
Look for signs that the competitor’s digital solution is better aligned with stores, logistics, organization, economics, or customer adoption.

Source strategy:
Prefer sources in this order:
1. Annual reports and official company reports
2. Company websites and app pages
3. Official app store pages
4. Statistics Denmark, Dansk Erhverv, Dagligvarehandlen, trade associations, or reliable market reports
5. Credible Danish business/news sources
6. Marketing/vendor case studies only if clearly marked as marketing and checked critically

Scraping method:
1. Start by finding official pages, annual reports, press pages, and app pages.
2. Use Crawl4AI to extract clean Markdown from each relevant public URL.
3. Save raw scraped content.
4. Extract structured findings into CSV/JSON.
5. Do not bypass logins, paywalls, CAPTCHAs, or robots restrictions.
6. Use polite rate limits.
7. Do not invent statistics.
8. If a statistic cannot be found, write “not found” and explain where you searched.

Create a separate folder inside /reports for each web scraping run:

Run folder:
reports/webscraping_runs/YYYY-MM-DD_HHMM_coop_competitor_analysis/

Rules:
- Create a new timestamped folder for every new scraping run.
- Do not overwrite previous scraping runs.
- Save all outputs from the current scraping run inside this folder.
- Use clear subfolders: data/, raw_sources/, logs/, and final_outputs/.
- Add a README.md inside the run folder explaining what was scraped, when, and what files were created.
- Also create or update reports/webscraping_runs/index.md with a short list of all scraping runs and their purpose.

Create these files inside the run folder:

1. reports/webscraping_runs/YYYY-MM-DD_HHMM_coop_competitor_analysis/raw_sources/
- Save one markdown file per scraped source.
- Include source URL, access date, title, and extracted content.

2. reports/webscraping_runs/YYYY-MM-DD_HHMM_coop_competitor_analysis/data/competitor_findings.csv
Columns:
- competitor
- chain_or_brand
- source_url
- source_type
- year
- evidence_type
- metric_name
- metric_value
- digital_solution
- customer_value_proposition
- observed_success_factor
- comparison_to_coop
- relevant_theory_lens
- confidence_level
- quote_or_short_evidence

3. reports/webscraping_runs/YYYY-MM-DD_HHMM_coop_competitor_analysis/data/source_register.csv
Columns:
- source_url
- source_title
- publisher
- source_type
- date_published_or_year
- access_date
- reliability_assessment
- marketing_source_yes_no
- notes

4. reports/webscraping_runs/YYYY-MM-DD_HHMM_coop_competitor_analysis/final_outputs/competitor_analysis.md

5. reports/webscraping_runs/YYYY-MM-DD_HHMM_coop_competitor_analysis/final_outputs/key_takeaways_summary.pdf

Create a simple PDF summary for quick exam use. The PDF must be short and easy to read, not a full report.

PDF requirements:
- Maximum 2 pages.
- Use plain layout with clear headings.
- Focus only on the absolute key takeaways and key numbers.
- Do not include long theory explanations.
- Do not include long source discussions.
- Include only the most important statistics with short source references.
- Include a final table with the most important competitor differences versus Coop.

The PDF must include:

# Coop competitor analysis – key takeaways

## 1. Absolute key takeaways
Give 5-7 short bullet points.

## 2. Key numbers
Create a compact table with:
- competitor
- metric
- value
- year
- source

## 3. What competitors seem to do differently
Create a compact table with:
- competitor
- digital/customer-facing solution
- apparent success factor
- contrast with Coop

## 4. Exam-ready conclusion
Write 5-8 lines that summarize the main insight:
Competitors appear to succeed when their digital solutions clearly support their core business model, customer promise, and operational setup. Avoid recommendations for Coop.

Technical PDF instruction:
If Python is available, generate the PDF using a simple library such as reportlab, markdown-pdf, weasyprint, or another available local tool. If PDF generation fails, create a Markdown fallback file named final_outputs/key_takeaways_summary.md inside the run folder and explain the issue in the README.

The PDF should be created from the findings in the run folder's final_outputs/competitor_analysis.md and data/competitor_findings.csv, not from unsupported assumptions.

The report must have this structure:

# Competitor evidence report: Coop Denmark IT-strategy case

## 1. Purpose and limitation
Briefly explain that this is evidence gathering and competitor analysis, not recommendations for Coop.

## 2. Executive summary
Give 5-8 key findings in bullet points.

## 3. Method
Explain:
- crawl4ai was used for public web scraping
- source prioritization
- source criticism
- limitations
- no paywalled/private data used

## 4. Competitor overview table
Create a table comparing:
- competitor
- main position
- digital solution
- key statistics
- apparent success factor
- contrast with Coop
- strongest source

## 5. Competitor-by-competitor analysis
For each competitor:
- What they do
- What digital/customer-facing solution they use
- What statistics indicate
- Why this may work
- How it differs from Coop
- Which IT-strategy lens fits best

## 6. Cross-competitor patterns
Identify recurring patterns across successful competitors.
Examples:
- digital supports a clear core strategy
- price/discount promise is simple
- app is tied to daily shopping behavior
- loyalty/data is linked to store economics
- e-commerce works only when logistics and scale fit
- clearer chain identity than Coop

## 7. Statistics table
Create a clean table of all numerical findings with source links.

## 8. Theory mapping
Map findings to:
- Digital Business Model Framework
- DVC Framework
- Strategic positioning
- Implementation

Do not explain the theories generally. Only show how the empirical findings can be interpreted through the theories.

## 9. Gaps and uncertainties
List:
- missing data
- weak sources
- possible bias in marketing/vendor sources
- statistics that could not be verified

## 10. Source list
Use a clear source list with URLs.

Quality requirements:
- Be concrete.
- Use evidence for every important claim.
- Avoid generic statements like “they are more digital”.
- Separate facts from interpretation.
- Mark uncertain claims clearly.
- Do not write recommendations for Coop.
- Focus on what competitors’ solutions actually do and why they may work.
- Make the report usable directly as input to an IT-strategy exam project.
```

---

## Kort bruk

1. Åpne terminalen i prosjektmappen.
2. Aktiver miljøet ditt:

```bash
conda activate webscrape
```

3. Start Codex:

```bash
codex
```

4. Kjør skillen:

```text
$crawl4ai
```

5. Lim inn prompten over.
