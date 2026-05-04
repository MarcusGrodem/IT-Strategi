#!/usr/bin/env python3
"""Scrape a public test page with Crawl4AI and save structured JSON output."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("CRAWL4_AI_BASE_DIRECTORY", str(PROJECT_ROOT / ".crawl4ai-state"))

from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig


DEFAULT_URL = "https://quotes.toscrape.com/"
DEFAULT_OUTPUT = PROJECT_ROOT / "data/output.json"


@dataclass
class Quote:
    text: str
    author: str
    tags: list[str]


class QuotesParser(HTMLParser):
    """Extract quote cards from quotes.toscrape.com without extra dependencies."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.quotes: list[Quote] = []
        self._current: dict[str, Any] | None = None
        self._field: str | None = None
        self._tag_text: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        classes = set((dict(attrs).get("class") or "").split())

        if tag == "div" and "quote" in classes:
            self._current = {"text": "", "author": "", "tags": []}
            return

        if self._current is None:
            return

        if tag == "span" and "text" in classes:
            self._field = "text"
        elif tag == "small" and "author" in classes:
            self._field = "author"
        elif tag == "a" and "tag" in classes:
            self._field = "tag"
            self._tag_text = ""

    def handle_data(self, data: str) -> None:
        if self._current is None or self._field is None:
            return

        text = data.strip()
        if not text:
            return

        if self._field == "tag":
            self._tag_text = (self._tag_text or "") + text
        else:
            self._current[self._field] = (
                f"{self._current[self._field]} {text}".strip()
            )

    def handle_endtag(self, tag: str) -> None:
        if self._current is None:
            return

        if tag == "a" and self._field == "tag":
            if self._tag_text:
                self._current["tags"].append(self._tag_text)
            self._field = None
            self._tag_text = None
        elif tag in {"span", "small"} and self._field in {"text", "author"}:
            self._field = None
        elif tag == "div" and self._current.get("text"):
            self.quotes.append(Quote(**self._current))
            self._current = None
            self._field = None
            self._tag_text = None


def markdown_to_text(markdown: Any) -> str:
    """Handle Crawl4AI versions that return either str or MarkdownGenerationResult."""

    if isinstance(markdown, str):
        return markdown
    return getattr(markdown, "raw_markdown", "") or str(markdown or "")


async def scrape(url: str) -> dict[str, Any]:
    browser_config = BrowserConfig(headless=True)
    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        page_timeout=30_000,
        wait_for="css:.quote",
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=crawler_config)

    if not result.success:
        raise RuntimeError(f"Crawl failed: {result.error_message}")

    parser = QuotesParser()
    parser.feed(result.cleaned_html or result.html or "")

    return {
        "source_url": url,
        "scraped_at": datetime.now(timezone.utc).isoformat(),
        "status_code": result.status_code,
        "page_title": (result.metadata or {}).get("title"),
        "quote_count": len(parser.quotes),
        "quotes": [asdict(quote) for quote in parser.quotes],
        "markdown_preview": markdown_to_text(result.markdown)[:500],
        "policy": {
            "public_test_page": True,
            "login_required": False,
            "bypassed_paywall_captcha_or_rate_limit": False,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scrape a public test page with Crawl4AI."
    )
    parser.add_argument("--url", default=DEFAULT_URL, help="URL to scrape")
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Path for JSON output",
    )
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = PROJECT_ROOT / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)

    data = await scrape(args.url)
    output_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {data['quote_count']} quotes to {output_path}")


if __name__ == "__main__":
    asyncio.run(main())
