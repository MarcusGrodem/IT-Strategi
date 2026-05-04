# Minimal Crawl4AI Scraper

This project contains a small Python scraper that uses Crawl4AI to scrape the public test site [Quotes to Scrape](https://quotes.toscrape.com/) and save structured results to `data/output.json`.

The script is intentionally limited to a public test page. Do not use it to bypass logins, paywalls, CAPTCHA, robots/rate limits, or access controls.

Crawl4AI local state is stored under `.crawl4ai-state/`, which is ignored by git.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
crawl4ai-setup
```

Optional health check:

```bash
crawl4ai-doctor
```

## Run

```bash
python scripts/scrape.py
```

The command writes:

```text
data/output.json
```

You can override the URL and output path if needed:

```bash
python scripts/scrape.py --url https://quotes.toscrape.com/ --output data/output.json
```

## Troubleshooting

If macOS shows "Google Chrome for Testing quit unexpectedly", it usually means Playwright's browser process was blocked or killed by the local execution environment. Run the command from a normal terminal with the virtual environment activated:

```bash
source .venv/bin/activate
python scripts/scrape.py
```

If the browser dependency is missing or unhealthy, rerun:

```bash
crawl4ai-setup
crawl4ai-doctor
```
