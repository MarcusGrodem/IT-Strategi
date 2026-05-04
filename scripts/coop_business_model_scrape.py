#!/usr/bin/env python3
import asyncio
import csv
import json
import os
import re
import subprocess
import sys
import textwrap
import time
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

sys.path.insert(0, "/private/tmp/coop_scrape_pydeps")
os.environ.setdefault("CRAWL4_AI_BASE_DIRECTORY", "/private/tmp/coop_crawl4ai_home")

from bs4 import BeautifulSoup
from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)


RUN_ID = "2026-05-03_1813_coop_business_model_analysis"
RUN_DIR = Path("reports/webscraping_runs") / RUN_ID
RAW_DIR = RUN_DIR / "raw_sources"
DATA_DIR = RUN_DIR / "data"
LOG_DIR = RUN_DIR / "logs"
OUT_DIR = RUN_DIR / "final_outputs"
ACCESS_DATE = date.today().isoformat()

PDF_SOURCES = [
    {
        "path": Path("LLM/agent-setup/coop-it-strategy-agent-project/05_evidence/coop_aarsberetning_25_final.pdf"),
        "url": "local_pdf:coop_aarsberetning_25_final.pdf",
        "title": "Coop amba årsberetning 2025",
        "publisher": "Coop amba",
        "source_type": "annual report / financial source",
        "year": "2025",
    },
    {
        "path": Path("LLM/agent-setup/coop-it-strategy-agent-project/05_evidence/coop-danmark-aarsrapport-2025.pdf"),
        "url": "local_pdf:coop-danmark-aarsrapport-2025.pdf",
        "title": "Coop Danmark A/S årsrapport 2025",
        "publisher": "Coop Danmark A/S",
        "source_type": "annual report / financial source",
        "year": "2025",
    },
]

WEB_SOURCES = [
    {
        "url": "https://medlem.coop.dk/foreningen/medlem-medejer/",
        "title": "Medlemmer er medejere",
        "publisher": "Coop Medlem",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://medlem.coop.dk/",
        "title": "Coop Medlem",
        "publisher": "Coop Medlem",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://indmeld.coop.dk/",
        "title": "Bliv medlem af Coop",
        "publisher": "Coop Medlem",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://medlem.coop.dk/medlemsfordele",
        "title": "Medlemsfordele",
        "publisher": "Coop Medlem",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://medlem.coop.dk/medlemsfordele/personlige-tilbud/",
        "title": "Personlige tilbud",
        "publisher": "Coop Medlem",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://medlem.coop.dk/coop-app/kom-godt-i-gang/",
        "title": "Coop app",
        "publisher": "Coop Medlem",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://medlem.coop.dk/coop-app/scan-og-betal",
        "title": "Scan & Betal med Coop appen",
        "publisher": "Coop Medlem",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://medlem.coop.dk/spil-og-konkurrencer/",
        "title": "Spil og konkurrencer i Coop appen",
        "publisher": "Coop Medlem",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://medlem.coop.dk/coop-app/klimaaftryk/",
        "title": "Klimaaftryk i Coop appen",
        "publisher": "Coop Medlem",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://medlem.coop.dk/fordelskonto",
        "title": "Coop FordelsKonto",
        "publisher": "Coop Medlem",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://coop.dk/vores-maerker/",
        "title": "Coops egne varemærker",
        "publisher": "Coop Danmark",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://coop.dk/vores-maerker/coop/",
        "title": "Coop vareserie",
        "publisher": "Coop Danmark",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://coop.dk/vores-maerker/anglamark/",
        "title": "Änglamark",
        "publisher": "Coop Danmark",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://coop.dk/vores-maerker/irma/",
        "title": "Irma som varebrand",
        "publisher": "Coop Danmark",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://kvickly.coop.dk/",
        "title": "Kvickly front page",
        "publisher": "Kvickly / Coop Danmark",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://superbrugsen.coop.dk/om-superbrugsen/",
        "title": "Om SuperBrugsen",
        "publisher": "SuperBrugsen / Coop Danmark",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://brugsen.coop.dk/om-brugsen/daglibrugsen-bliver-til-brugsen/",
        "title": "Dagli'Brugsen bliver til Brugsen",
        "publisher": "Brugsen / Coop Danmark",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://brugsen.coop.dk/aktuelt/lavpris/",
        "title": "Lav Pris i Brugsen",
        "publisher": "Brugsen / Coop Danmark",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://365discount.coop.dk/om-365discount/job/karriere/",
        "title": "Karriere i 365discount",
        "publisher": "365discount / Coop Danmark",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://coop.dk/mad",
        "title": "Coop.dk MAD lukkede i 2023",
        "publisher": "Coop Danmark",
        "source_type": "official company source",
        "year": "2026",
    },
    {
        "url": "https://kundeservice.shopping.coop.dk/hc/da/articles/21459967795602-Hvorfor-og-hvorn%C3%A5r-er-Coop-dk-lukket",
        "title": "Hvorfor og hvornår er Coop.dk lukket?",
        "publisher": "Coop Danmark Kundeservice",
        "source_type": "official company source",
        "year": "2025",
    },
    {
        "url": "https://coop.dk/kontakt/pressekontakt/pressemeddelelser/coop-forbedrer-driftsindtjeningen-med-350-millioner-kr/",
        "title": "Coop forbedrer driftsindtjeningen med 350 millioner kr.",
        "publisher": "Coop Danmark",
        "source_type": "annual report / financial source",
        "year": "2026",
    },
    {
        "url": "https://coop.dk/kontakt/pressekontakt/pressemeddelelser/coops-resultat-for-2024-stoerre-fremgang-end-forventet/",
        "title": "Coops resultat for 2024",
        "publisher": "Coop Danmark",
        "source_type": "annual report / financial source",
        "year": "2025",
    },
    {
        "url": "https://coop.dk/kontakt/pressekontakt/pressemeddelelser/coop-og-brugsforeningernes-driftsresultat-for-2023/",
        "title": "Coop og brugsforeningernes driftsresultat for 2023",
        "publisher": "Coop Danmark",
        "source_type": "annual report / financial source",
        "year": "2024",
    },
    {
        "url": "https://www.lobyco.com/case-studies/coop",
        "title": "Helping 25% of Danish households shop smarter",
        "publisher": "Lobyco",
        "source_type": "vendor marketing source",
        "year": "2026",
    },
    {
        "url": "https://www.lobyco.com/insights/making-multi-banner-loyalty-simple",
        "title": "Making Multi-Banner Loyalty Simple",
        "publisher": "Lobyco",
        "source_type": "vendor marketing source",
        "year": "2026",
    },
    {
        "url": "https://www.lobyco.com/",
        "title": "Lobyco home page",
        "publisher": "Lobyco",
        "source_type": "vendor marketing source",
        "year": "2026",
    },
    {
        "url": "https://playable.com/cases/coop/",
        "title": "How Coop fueled loyalty and retail media",
        "publisher": "Playable",
        "source_type": "vendor marketing source",
        "year": "2026",
    },
    {
        "url": "https://www.shortcut.io/cases/coop-denmark-app",
        "title": "Digital transformation for the modern retail chain",
        "publisher": "Shortcut",
        "source_type": "vendor marketing source",
        "year": "2026",
    },
    {
        "url": "https://www.cooptrading.com/who-we-are/",
        "title": "Who we are",
        "publisher": "Coop Trading",
        "source_type": "industry source",
        "year": "2026",
    },
    {
        "url": "https://www.cooptrading.com/our-corporate-responsibility/working-with-suppliers/",
        "title": "Working with suppliers",
        "publisher": "Coop Trading",
        "source_type": "industry source",
        "year": "2026",
    },
    {
        "url": "https://ni.dk/ni-news/id/35f0f2a6-7ddc-4fee-bf00-4e127bf759ec/Coops-hjemmelevering-lukker",
        "title": "Coops hjemmelevering lukker",
        "publisher": "Ritzau / ni.dk",
        "source_type": "independent news source",
        "year": "2023",
    },
    {
        "url": "https://apps.apple.com/dk/app/coop-app/id537614968",
        "title": "Coop app in App Store",
        "publisher": "Apple App Store",
        "source_type": "app store source",
        "year": "2026",
    },
    {
        "url": "https://play.google.com/store/apps/details?id=dk.coop.members",
        "title": "Coop app in Google Play",
        "publisher": "Google Play",
        "source_type": "app store source",
        "year": "2026",
    },
]


def slugify(value):
    value = re.sub(r"https?://", "", value)
    value = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    return value[:90] or "source"


def clean_markdown(md):
    if not md:
        return ""
    markers = [
        "# Medlemmer er medejere",
        "# Coop appen",
        "# Hent Coop appen",
        "# Scan & Betal",
        "# Få personlige tilbud",
        "# Som Coop Medlem",
        "# Coops egne varemærker",
        "# Coop - hverdagsvarer",
        "# Änglamark",
        "# Irma",
        "# Om SuperBrugsen",
        "# Dagli",
        "# Coop.dk MAD",
        "# Hvorfor og hvornår",
        "# Coop forbedrer",
        "# Coops resultat",
        "# Helping 25%",
        "# Who we are",
        "# Coops hjemmelevering",
    ]
    positions = [md.find(marker) for marker in markers if md.find(marker) > 0]
    if positions:
        md = md[min(positions) :]
    md = re.sub(r"\n{4,}", "\n\n\n", md)
    return md.strip()


def html_to_markdown_fallback(url):
    req = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; CoopBusinessModelResearch/1.0)",
            "Accept-Language": "da,en;q=0.8",
        },
    )
    with urlopen(req, timeout=30) as response:
        html = response.read().decode("utf-8", errors="replace")
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg", "canvas", "iframe"]):
        tag.decompose()
    title = (soup.title.get_text(" ", strip=True) if soup.title else url).strip()
    lines = [
        "_Fallback extraction note: Crawl4AI was attempted first for this URL, but returned a Markdown/JSON NoneType error. Public HTML was then converted to simple Markdown with urllib and BeautifulSoup._",
        "",
        f"# {title}",
    ]
    body = soup.body or soup
    seen = set()
    for el in body.find_all(["h1", "h2", "h3", "p", "li"], recursive=True):
        text = re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()
        if not text or len(text) < 2:
            continue
        if text in seen:
            continue
        seen.add(text)
        if el.name == "h1":
            lines.append(f"\n# {text}")
        elif el.name == "h2":
            lines.append(f"\n## {text}")
        elif el.name == "h3":
            lines.append(f"\n### {text}")
        elif el.name == "li":
            lines.append(f"- {text}")
        else:
            lines.append(text)
    return clean_markdown("\n".join(lines))


def write_raw_source(meta, content):
    name = slugify(meta["url"])
    path = RAW_DIR / f"{name}.md"
    header = [
        f"source URL: {meta['url']}",
        f"access date: {ACCESS_DATE}",
        f"title: {meta['title']}",
        f"publisher: {meta['publisher']}",
        f"source type: {meta['source_type']}",
        "",
        "---",
        "",
    ]
    path.write_text("\n".join(header) + content.strip() + "\n", encoding="utf-8")
    return path


def scrape_web_sources():
    log_lines = []
    for i, meta in enumerate(WEB_SOURCES, 1):
        url = meta["url"]
        try:
            result = subprocess.run(
                ["crwl", url, "-o", "markdown"],
                capture_output=True,
                text=True,
                timeout=120,
                check=False,
            )
            md = clean_markdown(result.stdout)
            if result.returncode != 0:
                try:
                    fallback_md = html_to_markdown_fallback(url)
                    if fallback_md and len(fallback_md) > 200:
                        md = fallback_md
                        log_lines.append(
                            f"FALLBACK {i}/{len(WEB_SOURCES)} {url} crwl_rc={result.returncode} chars={len(md)} stderr={result.stderr[:300]!r}"
                        )
                    else:
                        md = md or f"[Crawl4AI crwl error for {url}]\n\nSTDERR:\n{result.stderr}"
                        log_lines.append(f"ERROR {i}/{len(WEB_SOURCES)} {url} rc={result.returncode} stderr={result.stderr[:500]!r}")
                except Exception as fallback_exc:
                    md = md or f"[Crawl4AI crwl error for {url}]\n\nSTDERR:\n{result.stderr}\n\nFallback extraction error: {fallback_exc}"
                    log_lines.append(
                        f"ERROR {i}/{len(WEB_SOURCES)} {url} rc={result.returncode} stderr={result.stderr[:300]!r} fallback={fallback_exc}"
                    )
            else:
                if not md:
                    md = f"[No extractable Markdown returned by Crawl4AI crwl for {url}]"
                log_lines.append(f"OK {i}/{len(WEB_SOURCES)} {url} chars={len(md)}")
            write_raw_source(meta, md)
        except Exception as exc:
            write_raw_source(meta, f"[Crawl4AI crwl exception: {exc}]")
            log_lines.append(f"ERROR {i}/{len(WEB_SOURCES)} {url} {exc}")
        time.sleep(1.0)
    (LOG_DIR / "crawl4ai_scrape.log").write_text("\n".join(log_lines) + "\n", encoding="utf-8")


def extract_pdf_sources():
    log_lines = []
    for meta in PDF_SOURCES:
        try:
            reader = PdfReader(str(meta["path"]))
            parts = []
            for index, page in enumerate(reader.pages, 1):
                text = page.extract_text() or ""
                if text.strip():
                    parts.append(f"\n\n## Page {index}\n\n{text.strip()}")
            content = "\n".join(parts).strip()
            if not content:
                content = "[No extractable text found in PDF.]"
            write_raw_source(meta, content)
            log_lines.append(f"OK {meta['path']} pages={len(reader.pages)} chars={len(content)}")
        except Exception as exc:
            write_raw_source(meta, f"[PDF extraction error: {exc}]")
            log_lines.append(f"ERROR {meta['path']} {exc}")
    (LOG_DIR / "pdf_extract.log").write_text("\n".join(log_lines) + "\n", encoding="utf-8")


def marketing_flag(source_type):
    return "yes" if source_type == "vendor marketing source" else "no"


def source_register_rows():
    rows = []
    for s in PDF_SOURCES + WEB_SOURCES:
        possible_bias = "low: audited/official financial reporting" if "annual report" in s["source_type"] else ""
        if s["source_type"] == "official company source":
            possible_bias = "company self-presentation; useful for claims about identity and customer promise"
        if s["source_type"] == "vendor marketing source":
            possible_bias = "promotes vendor platform capabilities; numbers useful but interpretation should be treated cautiously"
        if s["source_type"] == "independent news source":
            possible_bias = "journalistic summary; may simplify strategic context"
        if s["source_type"] == "app store source":
            possible_bias = "platform listing; useful for feature/rating signals but not strategic interpretation"
        if s["source_type"] == "industry source":
            possible_bias = "industry/cooperative sourcing perspective; partly promotional"
        reliability = {
            "annual report / financial source": "high for reported financial/store/member figures",
            "official company source": "high for Coop's own positioning; medium for performance interpretation",
            "vendor marketing source": "medium for documented platform metrics; low-medium for promotional claims",
            "independent news source": "medium-high for event reporting; verify numbers against official reports where possible",
            "industry source": "medium for sourcing model; may not disclose Coop Denmark-specific economics",
            "app store source": "medium for current app listing/functionality",
        }.get(s["source_type"], "medium")
        rows.append(
            {
                "source_url": s["url"],
                "source_title": s["title"],
                "publisher": s["publisher"],
                "source_type": s["source_type"],
                "date_published_or_year": s["year"],
                "access_date": ACCESS_DATE,
                "reliability_assessment": reliability,
                "marketing_source_yes_no": marketing_flag(s["source_type"]),
                "possible_bias": possible_bias,
                "notes": "",
            }
        )
    return rows


def finding(topic, subtopic, source_url, source_title, source_type, year, evidence_type, text, metric_name="", metric_value="", bmc="", cvp="", dbm="", dvc="", sp="", interpretation="", confidence="high", quote=""):
    return {
        "topic": topic,
        "subtopic": subtopic,
        "source_url": source_url,
        "source_title": source_title,
        "source_type": source_type,
        "year": year,
        "evidence_type": evidence_type,
        "finding": text,
        "metric_name": metric_name,
        "metric_value": metric_value,
        "business_model_component": bmc,
        "customer_value_proposition_element": cvp,
        "digital_business_model_lens": dbm,
        "dvc_lens": dvc,
        "strategic_positioning_lens": sp,
        "interpretation": interpretation,
        "confidence_level": confidence,
        "marketing_source_yes_no": marketing_flag(source_type),
        "quote_or_short_evidence": quote,
    }


def build_findings():
    official = "official company source"
    financial = "annual report / financial source"
    vendor = "vendor marketing source"
    news = "independent news source"
    industry = "industry source"
    rows = [
        finding("Identity", "Member ownership", "https://medlem.coop.dk/foreningen/medlem-medejer/", "Medlemmer er medejere", official, "2026", "positioning claim", "Coop presents members as co-owners of the cooperative and states that Coop Danmark is owned by Coop amba's members together with OK a.m.b.a.", bmc="Customer relationships; Key resources", cvp="membership; community; influence", dbm="customer knowledge", dvc="Relationships", sp="cooperative/member-owned retailer", interpretation="Membership is not only a loyalty mechanic but part of Coop's ownership narrative.", quote="mere end 2 millioner medlemmer ... ejer Coop Danmark"),
        finding("Identity", "No shareholders", "https://medlem.coop.dk/foreningen/medlem-medejer/", "Medlemmer er medejere", official, "2026", "positioning claim", "Coop says it has no shareholders and that members receive value through cash member benefits.", bmc="Revenue streams; Customer relationships", cvp="member value; bonus", dbm="customer knowledge", dvc="Relationships", sp="cooperative/member-owned retailer", interpretation="The claim frames surplus distribution as customer/member value rather than investor return.", quote="Coop har ingen aktionærer"),
        finding("Identity", "Local role", "https://medlem.coop.dk/foreningen/medlem-medejer/", "Medlemmer er medejere", official, "2026", "positioning claim", "Coop links membership to shaping local stores, local activity and a greener, more sustainable everyday life.", bmc="Customer relationships; Channels", cvp="locality; responsibility", dbm="omnichannel customer relationship", dvc="Relationships; Relevance", sp="community retailer", interpretation="The local/community promise differentiates Coop from a pure price-only grocery proposition.", quote="sætte dit præg på din lokale butik"),
        finding("Identity", "Food responsibility", "https://medlem.coop.dk/foreningen/medlem-medejer/", "Medlemmer er medejere", official, "2026", "positioning claim", "Coop claims to set strict requirements so customers can shop safely, including work on problematic chemicals.", bmc="Key activities; Key partners", cvp="trust; responsibility", dbm="supplier", dvc="Relevance", sp="responsible retailer", interpretation="Responsibility is presented as reducing customer worry in grocery shopping.", quote="så du trygt kan fylde i kurven"),
        finding("Identity", "Member voice", "https://medlem.coop.dk/foreningen/medlem-medejer/", "Medlemmer er medejere", official, "2026", "operational claim", "Coop states that it asks 1,000 co-owners weekly about issues from liver pate prices to chemicals and listens through local boards.", metric_name="weekly member survey sample", metric_value="1,000 co-owners", bmc="Customer relationships; Key resources", cvp="influence; trust", dbm="customer knowledge", dvc="Relationships", sp="member-informed retailer", interpretation="This is a concrete customer-knowledge mechanism tied to cooperative governance.", quote="hver uge 1.000 medejere"),
        finding("Business model", "Revenue and core activity", "local_pdf:coop-danmark-aarsrapport-2025.pdf", "Coop Danmark A/S årsrapport 2025", financial, "2025", "financial metric", "Coop Danmark's main activity is grocery retail; 2025 net revenue was DKK 32.565bn for Coop Danmark A/S and DKK 44.756bn including brugsforeninger.", metric_name="net revenue", metric_value="DKK 32.565bn; DKK 44.756bn incl. brugsforeninger", bmc="Revenue streams", cvp="grocery retail", dbm="supplier/omnichannel", dvc="Digital outputs", sp="large grocery retailer", interpretation="The revenue base is still overwhelmingly physical grocery retail rather than standalone digital platform income.", quote="Nettoomsætning 2025 32.565; inkl. Brugsforeninger 44.756"),
        finding("Business model", "Stores", "local_pdf:coop-danmark-aarsrapport-2025.pdf", "Coop Danmark A/S årsrapport 2025", financial, "2025", "operational metric", "Coop Danmark reported 536 stores in 2025; including brugsforeninger, the network was 900 stores.", metric_name="number of stores", metric_value="536; 900 incl. brugsforeninger", bmc="Channels; Key resources; Cost structure", cvp="physical availability", dbm="omnichannel", dvc="Digital infrastructure", sp="store-based retailer", interpretation="Store footprint is a central resource but also a cost structure and implementation constraint.", quote="Antal butikker 2025 536 ... inkl. Brugsforeninger 900"),
        finding("Business model", "Financial performance", "https://coop.dk/kontakt/pressekontakt/pressemeddelelser/coop-forbedrer-driftsindtjeningen-med-350-millioner-kr/", "Coop forbedrer driftsindtjeningen med 350 millioner kr.", financial, "2026", "financial metric", "Coop reported EBITDA before property-sale gains of DKK 313m in 2025, up DKK 350m from 2024, while EBIT was still a DKK 215m loss.", metric_name="EBITDA / EBIT", metric_value="EBITDA DKK 313m; EBIT -DKK 215m", bmc="Revenue streams; Cost structure", cvp="", dbm="business design", dvc="", sp="turnaround under core-store focus", interpretation="Evidence supports the tension of improved operations but continuing accounting losses.", quote="driftsindtjeningen ... 313 millioner kr.; EBIT ... underskud på 215 millioner kr."),
        finding("Business model", "2024 turnaround", "https://coop.dk/kontakt/pressekontakt/pressemeddelelser/coops-resultat-for-2024-stoerre-fremgang-end-forventet/", "Coops resultat for 2024", financial, "2025", "financial metric", "Coop reported 2024 EBIT before special items of DKK 162m, an improvement of DKK 879m versus 2023, with the statement attributing progress partly to renewed focus on the core business.", metric_name="EBIT before special items", metric_value="DKK 162m; +DKK 879m vs 2023", bmc="Cost structure; Key activities", dbm="business design", sp="core-business focus", interpretation="The official turnaround story emphasises store retail basics rather than online growth.", quote="fornyet og stærkt fokus på kerneforretningen"),
        finding("Business model", "2023 weakness", "https://coop.dk/kontakt/pressekontakt/pressemeddelelser/coop-og-brugsforeningernes-driftsresultat-for-2023/", "Coop og brugsforeningernes driftsresultat for 2023", financial, "2024", "financial metric", "In 2023 Coop Danmark EBIT before special impairments was -DKK 717m, while Coop and brugsforeninger revenue was DKK 46.6bn despite closures of Irma and Coop.dk MAD.", metric_name="2023 EBIT / revenue", metric_value="-DKK 717m; DKK 46.6bn incl. brugsforeninger", bmc="Revenue streams; Cost structure", dbm="business design", sp="financially pressured retailer", interpretation="The scale of revenue coexisted with weak profitability, making cost-to-serve and store portfolio important.", quote="EBIT-resultatet blev -717 mio. kr."),
        finding("Business model", "Online grocery closure", "https://coop.dk/mad", "Coop.dk MAD lukkede i 2023", official, "2026", "operational fact", "Coop.dk MAD is closed and Coop states that home delivery of groceries is no longer available; customers are directed to physical Coop chains.", bmc="Channels", cvp="physical store availability", dbm="omnichannel retreat", dvc="Digital outputs", sp="store-first retailer", interpretation="This is direct evidence that Coop's customer-facing digital model is not currently online grocery delivery.", quote="Coop.dk MAD lukkede i 2023"),
        finding("Business model", "Coop.dk webshop closure", "https://kundeservice.shopping.coop.dk/hc/da/articles/21459967795602-Hvorfor-og-hvorn%C3%A5r-er-Coop-dk-lukket", "Hvorfor og hvornår er Coop.dk lukket?", official, "2025", "operational fact", "Coop states that Coop.dk closed on 31 January 2025 to increase focus on the core business: physical stores.", metric_name="webshop closure date", metric_value="31 January 2025", bmc="Channels; Key activities", dbm="business design", sp="core-store focus", interpretation="The closure reinforces a strategic pullback from standalone e-commerce.", quote="øge fokus på kerneforretningen, som er de fysiske butikker"),
        finding("Business model", "Online grocery economics", "https://ni.dk/ni-news/id/35f0f2a6-7ddc-4fee-bf00-4e127bf759ec/Coops-hjemmelevering-lukker", "Coops hjemmelevering lukker", news, "2023", "news report", "Ritzau reported Coop.dk MAD had run with losses for ten years and that Coop saw no economically sustainable model for online supermarkets under its conditions.", metric_name="Coop.dk MAD loss period", metric_value="10 years with losses (reported)", bmc="Cost structure; Channels", dbm="business design", sp="digital ambition vs grocery economics", interpretation="Independent reporting supports the contradiction between digital ambition and online grocery economics.", confidence="medium-high", quote="har de seneste ti år kørt med underskud"),
        finding("Business model", "Private labels", "https://coop.dk/vores-maerker/", "Coops egne varemærker", official, "2026", "portfolio evidence", "Coop positions private labels as covering discount, everyday products and premium/responsible products, with strict supplier requirements.", bmc="Key resources; Revenue streams; Key partners", cvp="price; quality; trust; responsibility", dbm="supplier", dvc="Relevance", sp="multi-tier private-label retailer", interpretation="Private labels let Coop express several value propositions under one group: value, responsibility and quality.", quote="discount, hverdagsvarer eller ... ekstra lækkert"),
        finding("Business model", "Coop private label size", "https://coop.dk/vores-maerker/coop/", "Coop vareserie", official, "2026", "portfolio metric", "The Coop private-label series is described as Denmark's largest product series with more than 3,000 everyday products.", metric_name="Coop private-label products", metric_value="more than 3,000", bmc="Key resources; Revenue streams", cvp="fair price; everyday quality", dbm="supplier", dvc="Relevance", sp="scale private-label retailer", interpretation="This is a scale resource in procurement, margin and customer trust.", quote="mere end 3.000 varer"),
        finding("Business model", "Änglamark", "https://coop.dk/vores-maerker/anglamark/", "Änglamark", official, "2026", "portfolio metric", "Änglamark has more than 1,200 products and is positioned around organic, allergy-friendly and environmentally friendlier products.", metric_name="Änglamark products", metric_value="more than 1,200", bmc="Key resources; Value propositions", cvp="responsibility; organic; trust", dbm="supplier", dvc="Relevance", sp="responsible private-label brand", interpretation="Änglamark carries Coop's responsibility proposition in a productized form.", quote="over 1200 produkter"),
        finding("Business model", "Supplier platform", "https://www.cooptrading.com/who-we-are/", "Who we are", industry, "2026", "industry claim", "Coop Trading describes itself as the largest private-brand purchasing organization in the Nordics, sourcing and developing Xtra, Coop and Änglamark products for cooperative retailers.", bmc="Key partners; Key activities", cvp="price-quality ratio", dbm="supplier", dvc="Digital infrastructure", sp="Nordic purchasing scale", interpretation="The sourcing model points to scale advantages behind Coop's private labels.", quote="largest private brand purchasing organization in the Nordics"),
        finding("Business model", "Supplier relationships", "https://www.cooptrading.com/our-corporate-responsibility/working-with-suppliers/", "Working with suppliers", industry, "2026", "industry metric", "Coop Trading reports 700+ suppliers and says about 10% are partner suppliers focused on category development, quality and operational excellence.", metric_name="supplier base", metric_value="700+ suppliers; approx. 10% partner suppliers", bmc="Key partners", cvp="quality; value", dbm="supplier", dvc="Digital competences", sp="scale sourcing and category partnerships", interpretation="Supplier relationships are part of Coop's business model, especially for private labels and category development.", quote="700+ suppliers ... Approximately 10 % ... partner suppliers"),
        finding("Customer value proposition", "Member benefits", "https://medlem.coop.dk/medlemsfordele", "Medlemsfordele", official, "2026", "feature evidence", "Coop's member proposition includes bonus, personal offers, member offers, partner bonus and Samvirke.", bmc="Value propositions; Customer relationships", cvp="loyalty benefits; savings; content", dbm="customer knowledge", dvc="Relationships; Experiences", sp="loyalty-led grocery retailer", interpretation="The value proposition is not a single attribute; it combines savings, membership and everyday services.", quote="Optjen bonus ... Personlige tilbud ... Medlemspartnere"),
        finding("Customer value proposition", "5% fruit and veg bonus", "https://indmeld.coop.dk/", "Bliv medlem af Coop", official, "2026", "loyalty metric", "Coop states that members earn 5% bonus on fresh fruit and vegetables in all Coop stores when registering the purchase with the app or member card.", metric_name="member bonus", metric_value="5% on fresh fruit and vegetables", bmc="Customer relationships; Revenue streams", cvp="savings; fresh food", dbm="customer knowledge", dvc="Relationships", sp="member-value retailer", interpretation="The bonus links price value to healthier/fresh categories and reinforces registration/data capture.", quote="5 % medlemsbonus på frisk frugt og grønt"),
        finding("Customer value proposition", "Personalized offers", "https://medlem.coop.dk/medlemsfordele/personlige-tilbud/", "Personlige tilbud", official, "2026", "feature evidence", "Coop states that weekly personal offers are based on the products the member buys most and must be activated before purchase.", metric_name="personal offers per week", metric_value="up to 20 offers", bmc="Customer relationships; Channels", cvp="personalized savings", dbm="customer knowledge", dvc="Relationships; Relevance", sp="data-driven loyalty", interpretation="Personalization converts transaction data into customer-facing price relevance.", quote="baseret på de varer, du køber mest af"),
        finding("Customer value proposition", "FordelsKonto", "https://medlem.coop.dk/fordelskonto", "Coop FordelsKonto", official, "2026", "feature metric", "Coop FordelsKonto is presented as a food account in the app where members transfer DKK 100-7,000 monthly and receive 5-15% bonus on selected brands when paying through the account.", metric_name="FordelsKonto bonus and transfer range", metric_value="5-15%; DKK 100-7,000/month", bmc="Revenue streams; Customer relationships", cvp="bonus; budgeting; selected brands", dbm="customer knowledge", dvc="Relationships; Digital outputs", sp="loyalty/payment integration", interpretation="FordelsKonto blends grocery budgeting, payment, brand selection and repeat purchase economics.", quote="en slags madkonto i Coop appen"),
        finding("Digital model", "App functions", "https://medlem.coop.dk/coop-app/kom-godt-i-gang/", "Coop app", official, "2026", "feature evidence", "Coop says the app gathers functions for SuperBrugsen, Kvickly, 365discount and Brugsen, including digital receipts, shopping list, recipes, newspapers, offers, Scan & Betal, games, climate footprint and local store content.", bmc="Channels; Customer relationships; Key resources", cvp="convenience; savings; inspiration; control", dbm="omnichannel; customer knowledge", dvc="Experiences; Relationships; Digital outputs", sp="store-supporting loyalty app", interpretation="The app is designed as a store companion and relationship layer rather than an online grocery channel.", quote="Alle relevante funktioner ... samlet til dig i Coop appen"),
        finding("Digital model", "Scan & Betal", "https://medlem.coop.dk/coop-app/scan-og-betal", "Scan & Betal med Coop appen", official, "2026", "feature evidence", "Scan & Betal lets customers scan items, pack while shopping and pay through the phone in Coop chains, using MobilePay, FordelsKonto, bonus or card.", bmc="Channels; Customer relationships", cvp="convenience; queue avoidance", dbm="omnichannel", dvc="Experiences; Digital outputs", sp="digital enhancement of physical stores", interpretation="The feature directly supports physical-store throughput and convenience.", quote="scan dine varer og betaler med mobilen"),
        finding("Digital model", "Receipts and shopping lists", "https://medlem.coop.dk/coop-app/kom-godt-i-gang/", "Coop app", official, "2026", "feature evidence", "The app offers digital receipts, a categorized/shareable shopping list, digital circulars and the ability to add offers to lists.", bmc="Channels; Customer relationships", cvp="planning; convenience", dbm="customer knowledge", dvc="Experiences; Digital outputs", sp="store-supporting app", interpretation="These features create value before and after the transaction, not only at checkout.", quote="indkøbslisten er opdelt efter kategorier"),
        finding("Digital model", "Climate footprint", "https://medlem.coop.dk/coop-app/klimaaftryk/", "Klimaaftryk i Coop appen", official, "2026", "feature evidence", "The app lets users track the development of their grocery climate footprint and organic share from week to week after consenting and registering purchases.", bmc="Customer relationships; Key resources", cvp="responsible shopping insight", dbm="customer knowledge", dvc="Experiences; Relevance", sp="responsibility plus data-driven loyalty", interpretation="This extends the app beyond price and convenience into values-based customer engagement.", quote="se udviklingen i dit klimaaftryk fra uge til uge"),
        finding("Digital model", "Gamification", "https://medlem.coop.dk/spil-og-konkurrencer/", "Spil og konkurrencer i Coop appen", official, "2026", "feature evidence", "Coop app games let users participate for free and win prizes such as products to collect in local Coop stores, discounts or bonus.", bmc="Customer relationships; Channels", cvp="engagement; rewards", dbm="customer knowledge", dvc="Experiences; Relationships", sp="loyalty gamification", interpretation="Gamification is used to increase app visits and connect digital engagement back to stores.", quote="varer, som du selv kan hente nede i din lokale Coop-butik"),
        finding("Digital model", "App user scale", "https://www.lobyco.com/case-studies/coop", "Helping 25% of Danish households shop smarter", vendor, "2026", "vendor metric", "Lobyco states that Coop app has more than 1.8m users, equivalent to 25% of Danish households, and that app users shop 50% more frequently than other customers.", metric_name="app users / frequency uplift", metric_value="1.8m users; 25% households; 50% higher frequency", bmc="Key resources; Customer relationships", cvp="digital ease; loyalty", dbm="customer knowledge; omnichannel", dvc="Relationships; Digital outputs", sp="digital frontrunner claim", interpretation="Useful as documented vendor/client case metrics, but the source sells Lobyco's platform, so the causal interpretation should be treated cautiously.", confidence="medium", quote="more than 1.8 million users ... 50% higher frequency"),
        finding("Digital model", "Monthly active users", "https://www.lobyco.com/insights/making-multi-banner-loyalty-simple", "Making Multi-Banner Loyalty Simple", vendor, "2026", "vendor metric", "Lobyco states that Coop runs Denmark's largest membership programme on Lobyco and that the Coop app has approximately 880,000 monthly active users across four banners.", metric_name="monthly active users", metric_value="approx. 880,000", bmc="Key resources; Customer relationships", cvp="one app across banners", dbm="customer knowledge; omnichannel", dvc="Digital infrastructure; Relationships", sp="multi-banner loyalty platform", interpretation="This supports the app as a shared loyalty layer across a complex chain portfolio; it is vendor marketing evidence.", confidence="medium", quote="approximately 880,000 monthly active users"),
        finding("Digital model", "Lobyco role", "https://www.lobyco.com/", "Lobyco home page", vendor, "2026", "vendor positioning", "Lobyco presents itself as born from retail and building digital-first loyalty experiences for retailers.", bmc="Key resources; Key partners", cvp="platform-enabled loyalty", dbm="modular producer/platform provider", dvc="Digital infrastructure; Digital competences", sp="retailer plus loyalty platform/OEM logic", interpretation="Lobyco gives Coop a role beyond retailer when its loyalty technology is offered to other retailers.", confidence="medium", quote="Born from retail. Building the future of loyalty."),
        finding("Digital model", "Playable gamification", "https://playable.com/cases/coop/", "How Coop fueled loyalty and retail media", vendor, "2026", "vendor metric", "Playable states that Coop uses gamification as part of loyalty and retail media, with app games featuring branded prizes funded by suppliers and redeemed in stores.", bmc="Customer relationships; Key partners; Revenue streams", cvp="engagement; rewards; supplier-funded prizes", dbm="customer knowledge; ecosystem/supplier monetization", dvc="Experiences; Relationships; Digital outputs", sp="gamified loyalty and retail media", interpretation="This supports the view that games create value for customers, stores and suppliers, but the source is a vendor case selling gamification.", confidence="medium", quote="branded prizes funded by suppliers"),
        finding("Digital model", "Playable results", "https://playable.com/cases/coop/", "How Coop fueled loyalty and retail media", vendor, "2026", "vendor metric", "Playable reports +100,000 unique players per game, 9% higher basket value for prize redeemers in 2023, 4.25m Christmas game plays, 500,000 Christmas prizes redeemed in store, and 68% of winners redeeming a prize in a Coop store.", metric_name="gamification engagement and redemption", metric_value="+100,000 unique players/game; +9% basket; 4.25m Christmas game plays; 500,000 prizes; 68% redemption", bmc="Customer relationships; Channels; Key partners", cvp="engagement; rewards; store traffic", dbm="customer knowledge; ecosystem", dvc="Experiences; Digital outputs; Relevance", sp="digital engagement feeding physical stores", interpretation="These numbers are useful for the app/store link and retail-media model, but are vendor-reported and should not be treated as independent proof of profitability.", confidence="medium", quote="+100,000 unique players per game"),
        finding("Digital model", "Shortcut app/OEM case", "https://www.shortcut.io/cases/coop-denmark-app", "Digital transformation for the modern retail chain", vendor, "2026", "vendor metric", "Shortcut describes the Coop App as transformed into an OEM solution and core of several large retail-chain customer apps; it reports over 1.5m downloads and daily users above 250,000.", metric_name="app downloads / daily users", metric_value="over 1.5m downloads; daily users above 250,000", bmc="Key resources; Channels; Customer relationships", cvp="economic benefits; easier grocery shopping; food inspiration", dbm="modular producer; omnichannel", dvc="Digital infrastructure; Experiences", sp="retailer app becoming OEM solution", interpretation="The case reinforces Lobyco's modular-producer/platform logic but is vendor marketing and includes older e-commerce functionality now contradicted by Coop's closure of online grocery.", confidence="medium", quote="turned into an OEM solution"),
        finding("Chain portfolio", "Kvickly", "https://kvickly.coop.dk/", "Kvickly front page", official, "2026", "chain evidence", "Kvickly foregrounds weekly offers, member discounts, nonfood categories such as bikes, 5% produce bonus, discount match and the Coop app.", bmc="Channels; Value propositions", cvp="large-store assortment; offers; member value", dbm="omnichannel", dvc="Experiences", sp="large-format supermarket/hypermarket with loyalty and price signals", interpretation="Kvickly appears to combine broad assortment/nonfood with price/member mechanics.", quote="Discountmatch ... Hent appen og få flere fordele"),
        finding("Chain portfolio", "SuperBrugsen", "https://superbrugsen.coop.dk/om-superbrugsen/", "Om SuperBrugsen", official, "2026", "chain evidence", "SuperBrugsen positions itself around taste, quality, everyday and special occasions, while also promising discount match and local goods.", bmc="Channels; Value propositions", cvp="quality; taste; local; value", dbm="omnichannel", dvc="Relevance", sp="quality supermarket with local and price elements", interpretation="SuperBrugsen carries a more quality/local position than pure discount.", quote="En bid bedre. Hver dag"),
        finding("Chain portfolio", "Brugsen", "https://brugsen.coop.dk/om-brugsen/daglibrugsen-bliver-til-brugsen/", "Dagli'Brugsen bliver til Brugsen", official, "2026", "chain evidence", "Brugsen presents itself as the local grocery store close to everyday life, with fair prices, support for local communities and local customer knowledge.", bmc="Channels; Customer relationships", cvp="locality; convenience; fair prices", dbm="customer knowledge", dvc="Relationships; Relevance", sp="local community grocery store", interpretation="Brugsen is Coop's strongest explicit community/locality format.", quote="lever vi af og for at være tæt på dig og din hverdag"),
        finding("Chain portfolio", "Brugsen low price", "https://brugsen.coop.dk/aktuelt/lavpris/", "Lav Pris i Brugsen", official, "2026", "chain evidence", "Brugsen says almost 300 selected products are part of its Lav Pris programme, chosen based on purchase data from store tills.", metric_name="Lav Pris products", metric_value="almost 300", bmc="Value propositions; Customer relationships", cvp="local everyday low price", dbm="customer knowledge", dvc="Relevance", sp="local store with data-informed price programme", interpretation="This shows a hybrid of local identity and price sensitivity.", quote="udvalgt på baggrund af købsdata fra kasserne"),
        finding("Chain portfolio", "365discount", "https://365discount.coop.dk/om-365discount/job/karriere/", "Karriere i 365discount", official, "2026", "chain evidence", "365discount is described as a low-price supermarket with discount prices, quality, organic everyday economy, Danish goods, no-unnecessary-chemistry products, easy meal solutions and fresh produce.", bmc="Channels; Value propositions", cvp="discount; quality; green/organic", dbm="business design", dvc="Relevance", sp="discount with green/responsibility overlay", interpretation="365discount adds a price-led position inside the cooperative portfolio.", quote="discountpriser og høj kvalitet"),
        finding("Strategic positioning", "Multi-banner complexity", "https://www.lobyco.com/insights/making-multi-banner-loyalty-simple", "Making Multi-Banner Loyalty Simple", vendor, "2026", "vendor interpretation", "Lobyco frames Coop's four banners as connected through one app, one loyalty setup and one shared bonus/reward structure.", bmc="Channels; Customer relationships; Key resources", cvp="one membership across chains", dbm="omnichannel; customer knowledge", dvc="Digital infrastructure; Relationships", sp="multi-banner loyalty platform", interpretation="The shared app may reduce customer-facing complexity, but the claim is vendor marketing and does not prove economic simplicity.", confidence="medium", quote="Four distinct banners are connected through one app"),
        finding("Strategic positioning", "Mixed model", "local_pdf:coop-danmark-aarsrapport-2025.pdf", "Coop Danmark A/S årsrapport 2025", financial, "2025", "analysis from metrics", "Coop is simultaneously a large physical grocery retailer, a member organisation, a multi-chain portfolio and a loyalty/app platform owner.", bmc="Full canvas", cvp="mixed: price, quality, membership, locality, responsibility, digital ease", dbm="omnichannel with modular producer element via Lobyco", dvc="Experiences; Relationships; Infrastructure; Relevance", sp="mixed strategic position", interpretation="The evidence suggests no single pure position; Coop blends cooperative identity, store retail and digital loyalty.", quote="synthesis of reported stores, membership and app evidence"),
        finding("Tension", "Digital success vs store economics", "https://www.lobyco.com/case-studies/coop", "Helping 25% of Danish households shop smarter", vendor, "2026", "vendor metric plus analysis", "Lobyco's app engagement metrics coexist with Coop's recent financial weakness and store/webshop rationalisation.", bmc="Customer relationships; Cost structure", cvp="digital ease vs price/store economics", dbm="customer knowledge vs business design", dvc="Relationships; Digital outputs", sp="digital frontrunner vs retailer economics", interpretation="The central tension is not whether digital works for engagement, but whether it changes the economics of grocery retail enough.", confidence="medium", quote="1.8 million users ... 50% higher frequency"),
        finding("Tension", "App success vs online grocery closure", "https://coop.dk/mad", "Coop.dk MAD lukkede i 2023", official, "2026", "operational contradiction", "Coop can have a strong app while its online grocery delivery channel is closed; digital is mainly a store-supporting relationship layer.", bmc="Channels; Customer relationships", cvp="convenience in store, not home delivery", dbm="omnichannel retreat", dvc="Digital outputs", sp="digital store companion", interpretation="This distinction prevents overclaiming Coop as an e-commerce grocery player.", quote="ikke længere muligt at få leveret dagligvarer til døren"),
        finding("Tension", "Member value vs price market", "https://indmeld.coop.dk/", "Bliv medlem af Coop", official, "2026", "analysis from loyalty claims", "The member promise emphasizes bonus, ownership and personal offers, while chain evidence shows strong price mechanisms such as discount match, Lav Pris and 365discount.", bmc="Value propositions; Customer relationships", cvp="membership plus price", dbm="customer knowledge", dvc="Relevance", sp="loyalty/member retailer in price-sensitive market", interpretation="Coop's value proposition appears to compete on both values and price, which can create strategic complexity.", quote="5 % bonus ... personlige tilbud ... Lav Pris / discount"),
    ]
    return rows


KEY_NUMBERS = [
    ("Net revenue, Coop Danmark A/S", "DKK 32.565bn", "2025", "Coop Danmark A/S årsrapport 2025", "Core operating scale; down from 2024", "high"),
    ("Net revenue incl. brugsforeninger", "DKK 44.756bn", "2025", "Coop Danmark A/S årsrapport 2025", "Broader Coop-family retail scale", "high"),
    ("Stores, Coop Danmark A/S", "536", "2025", "Coop Danmark A/S årsrapport 2025", "Core physical channel footprint", "high"),
    ("Stores incl. brugsforeninger", "900", "2025", "Coop Danmark A/S årsrapport 2025", "National store reach and cost base", "high"),
    ("EBITDA before property gains", "DKK 313m", "2025", "Coop press release / annual report", "Improved operation, still turnaround context", "high"),
    ("EBIT", "-DKK 215m", "2025", "Coop press release / annual report", "Accounting loss despite better operations", "high"),
    ("Members", "More than 2m", "2026", "Coop Medlem", "Ownership and loyalty base", "high"),
    ("Coop app users", "More than 1.8m", "2026", "Lobyco case", "Vendor-reported digital reach", "medium"),
    ("Coop app monthly active users", "Approx. 880,000", "2026", "Lobyco insight", "Vendor-reported active engagement", "medium"),
    ("Coop app daily users", "Above 250,000", "2026", "Shortcut case", "Vendor-reported app engagement; likely older than current Lobyco figures", "medium"),
    ("Danish households using app", "25%", "2026", "Lobyco case", "Vendor-reported reach", "medium"),
    ("App customer frequency uplift", "50% higher frequency", "2026", "Lobyco case", "Correlation/claim; not independently verified", "medium"),
    ("Gamification unique players", "+100,000 per game", "2026", "Playable case", "Vendor-reported game engagement", "medium"),
    ("Christmas game plays", "4.25m", "2023", "Playable case", "Vendor-reported seasonal engagement", "medium"),
    ("Christmas prizes redeemed in stores", "500,000", "2023", "Playable case", "Vendor-reported store-redemption outcome", "medium"),
    ("Coop private-label products", "More than 3,000", "2026", "Coop vareserie", "Private-label scale", "high"),
    ("Änglamark products", "More than 1,200", "2026", "Coop / Änglamark", "Responsibility-oriented private-label scale", "high"),
    ("Coop Trading suppliers", "700+", "2026", "Coop Trading", "Supplier/sourcing ecosystem", "medium"),
    ("Coop.dk MAD closure", "2023", "2023", "Coop.dk MAD page / Ritzau", "Online grocery delivery discontinued", "high"),
]


def write_csvs():
    source_fields = [
        "source_url",
        "source_title",
        "publisher",
        "source_type",
        "date_published_or_year",
        "access_date",
        "reliability_assessment",
        "marketing_source_yes_no",
        "possible_bias",
        "notes",
    ]
    with (DATA_DIR / "source_register.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=source_fields)
        writer.writeheader()
        source_rows = source_register_rows()
        writer.writerows(source_rows)
    (DATA_DIR / "source_register.json").write_text(
        json.dumps(source_rows, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    fields = [
        "topic",
        "subtopic",
        "source_url",
        "source_title",
        "source_type",
        "year",
        "evidence_type",
        "finding",
        "metric_name",
        "metric_value",
        "business_model_component",
        "customer_value_proposition_element",
        "digital_business_model_lens",
        "dvc_lens",
        "strategic_positioning_lens",
        "interpretation",
        "confidence_level",
        "marketing_source_yes_no",
        "quote_or_short_evidence",
    ]
    with (DATA_DIR / "coop_business_model_findings.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        finding_rows = build_findings()
        writer.writerows(finding_rows)
    (DATA_DIR / "coop_business_model_findings.json").write_text(
        json.dumps(finding_rows, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        escaped = [str(cell).replace("\n", " ").replace("|", "\\|") for cell in row]
        out.append("| " + " | ".join(escaped) + " |")
    return "\n".join(out)


def write_analysis():
    source_links = [f"- {s['title']} ({s['publisher']}): {s['url']}" for s in PDF_SOURCES + WEB_SOURCES]
    numbers_table = md_table(
        ["metric", "value", "year", "source", "interpretation", "confidence level"],
        KEY_NUMBERS,
    )
    theory_rows = [
        ("Business Model Canvas", "Customer segments", "Danish grocery shoppers, Coop members/co-owners, local community customers, price-sensitive discount shoppers, quality/local-food shoppers, app users and supplier/partner audiences."),
        ("Business Model Canvas", "Value propositions", "Membership and bonus, physical proximity, fair/low prices, quality/taste, local community role, responsible/private-label shopping, Scan & Betal and app convenience."),
        ("Business Model Canvas", "Channels", "536 Coop Danmark stores and 900 stores incl. brugsforeninger, plus Coop app, newsletters, member pages, partner channels and discontinued online grocery/webshop channels."),
        ("Business Model Canvas", "Customer relationships", "Member ownership, local boards, weekly member listening, personal offers, bonus, games, app content and partner benefits."),
        ("Business Model Canvas", "Revenue streams", "Primarily physical grocery retail sales; member-related repeat purchase and private-label margin; partner/bonus ecosystem; possible platform revenue through Lobyco not quantified in public sources."),
        ("Business Model Canvas", "Key resources", "Store footprint, membership base above 2m, Coop app user base, private labels, data infrastructure, Lobyco, supplier network and brand portfolio."),
        ("Business Model Canvas", "Key activities", "Store operations, assortment/procurement, private-label development, campaigns/offers, loyalty operation, app development, data personalization and supplier/category collaboration."),
        ("Business Model Canvas", "Key partners", "OK a.m.b.a. as co-owner, brugsforeninger, Coop Trading, suppliers, member partners, Lobyco clients/technology ecosystem, payment partners such as MobilePay/Coop Bank."),
        ("Business Model Canvas", "Cost structure", "Store operations, employees, inventory/logistics, IT platforms, app/loyalty operations, and restructuring/closure costs; online grocery economics were explicitly problematic."),
        ("Digital Business Model", "Customer knowledge", "Strong: members, app registration, purchase-data based personal offers, Lav Pris selected from till data, climate footprint and local content."),
        ("Digital Business Model", "Business design", "Omnichannel mainly in the sense of digital support for physical stores, not full online grocery. Lobyco adds modular producer/platform logic."),
        ("Digital Business Model", "Archetype", "Coop appears primarily omnichannel/store-supporting retailer; Lobyco partially shifts Coop toward modular producer/OEM loyalty platform."),
        ("Digital Value Creation", "Experiences", "Scan & Betal, digital receipts, shopping lists, games, recipes, app offers and local store content."),
        ("Digital Value Creation", "Relationships", "Membership, bonus, personal offers, app engagement, partner benefits and co-owner identity."),
        ("Digital Value Creation", "Evolution", "Shift from analogue member organisation to app-enabled loyalty; closure of online grocery/webshop shows selective digital evolution."),
        ("Digital Value Creation", "Digital competences", "Lobyco loyalty platform, personalization, multi-banner campaign management, app feature development and data-based pricing/offer logic."),
        ("Digital Value Creation", "Digital infrastructure", "One app across four banners, Coop One IT foundation in annual-report context, loyalty/payment data, supplier/category systems."),
        ("Digital Value Creation", "Digital outputs", "Personal offers, bonus balances, receipts, climate footprint, games, Scan & Betal, shared loyalty structure."),
        ("Digital Value Creation", "Relevance", "Personalized offers, local store communication, climate/organic insights and everyday price/bonus mechanisms."),
        ("Strategic positioning", "Different activities / same activities differently", "Coop performs grocery retail like rivals but frames it through cooperative ownership, multi-banner loyalty, local boards, private-label responsibility and app-enabled member data."),
        ("Implementation", "Alignment evidence", "Digital initiatives mostly support stores; online grocery and webshop closures indicate implementation/economic limits outside core store model."),
    ]
    theory_table = md_table(["lens", "mapping area", "Coop evidence fit"], theory_rows)
    content = f"""# Coop Denmark business model and positioning analysis

## 1. Purpose and limitation

This report is evidence gathering and business model analysis for a CBS IT-strategy exam project. It investigates Coop Denmark's current business model, strategic positioning and customer value proposition. It does not make strategic recommendations and does not try to solve Coop's strategic problems.

## 2. Executive summary

- Coop presents itself as a member-owned cooperative grocery retailer where more than 2 million members are co-owners, not just loyalty-card users.
- Coop's revenue logic remains store-based grocery retail: Coop Danmark A/S reported DKK 32.565bn in 2025 net revenue and 536 stores; including brugsforeninger, the network was DKK 44.756bn and 900 stores.
- Coop's value proposition is mixed rather than singular: member benefits, local/community role, responsible food standards, price/bonus mechanics, quality formats and digital convenience all appear in the evidence.
- The chain portfolio spans different positions: Kvickly combines broad assortment and member/price mechanics; SuperBrugsen stresses quality, taste and local goods; Brugsen stresses local community proximity; 365discount stresses low prices with a green/responsible overlay.
- Coop App is best understood as a store-supporting loyalty and relationship layer, not as proof that Coop is an online grocery business. It supports personal offers, bonus, Scan & Betal, receipts, shopping lists, games, climate footprint and local store content.
- Lobyco and Shortcut turn Coop's digital loyalty capability into a potential modular/OEM platform asset. Vendor sources report more than 1.8m Coop app users, about 880,000 monthly active users and 50% higher shopping frequency among app users, but these are vendor-marketing claims and should be treated cautiously.
- There is a clear tension between strong digital engagement and grocery economics: Coop closed Coop.dk MAD in 2023 and later Coop.dk webshop in 2025 to focus on the physical-store core.
- Financially, Coop improved materially but was still in turnaround territory: 2025 EBITDA before property gains was DKK 313m, while EBIT was -DKK 215m.

## 3. Method and source criticism

Crawl4AI was used to scrape public web pages into clean Markdown. Two local annual-report PDFs supplied by the user were extracted as primary financial evidence. Sources were prioritized as requested: Coop official pages and reports first; chain, member and app pages next; then Lobyco, Coop Trading, app-store pages and independent/trade news.

No login-only, paywalled, CAPTCHA-gated or private data was used. Marketing and vendor sources are marked in the source register and findings CSV. For these sources, documented figures are separated from promotional interpretation. Lobyco sources are useful for app metrics and platform positioning, but they also sell loyalty technology, so claims about causality and superiority should be treated as medium-confidence unless verified elsewhere.

Some current app-store pages can be difficult for crawlers and may return partial content; where extraction was weak, the source is retained in raw sources but not used for key strategic claims. Statistics not found in public sources are listed in section 12.

## 4. What Coop appears to stand for

Coop presents itself as a cooperative/member organisation, a Danish grocery retailer and a community actor. The official member page states that members are co-owners and that more than 2 million members, together with OK a.m.b.a., own Coop Danmark and the chains Brugsen, SuperBrugsen, Kvickly and 365discount. Coop also says it has no shareholders and that members receive value through cash member benefits.

The brand promise is not only price. Coop repeatedly connects grocery shopping with fewer worries, strict product requirements, removal of problematic chemicals, local goods and a greener/more sustainable everyday life. The phrase "Det gi'r mening" is used as a broad meaning frame: it connects membership, local stores, responsible products, bonus and everyday grocery practicality.

The digital ambition is expressed through the app and Lobyco rather than through online grocery delivery. Coop presents the app as a single place for offers, Scan & Betal, receipts, shopping lists, games, recipes, climate footprint and member benefits. The ambiguity is that Coop presents itself as both a community-owned grocery retailer and a data-driven digital loyalty actor.

## 5. Coop's business model

### Customer segments

Coop serves Danish grocery shoppers across multiple needs: price-sensitive households, local convenience shoppers, quality/taste-oriented supermarket customers, responsible/organic shoppers, families using app planning tools, and members/co-owners seeking bonus and influence. Supplier and partner audiences are also relevant through private labels, Coop Trading, partner benefits and Lobyco's platform business.

### Value propositions

Coop's value propositions include everyday grocery availability, member bonus, personal offers, fair/low prices, local stores, quality/taste, responsible products and digital convenience. Evidence does not support one single proposition. Instead, Coop carries several propositions across chains and the shared membership/app layer.

### Channels

The dominant channel is physical retail: 536 Coop Danmark stores in 2025 and 900 stores including brugsforeninger. Digital channels are the Coop App, member site, chain sites, newsletters, digital circulars and partner channels. Coop.dk MAD closed in 2023 and Coop.dk webshop closed on 31 January 2025, so digital commerce is no longer the central grocery channel.

### Customer relationships

Customer relationships are built through membership/co-ownership, member bonus, personal offers, local boards, app engagement, games, FordelsKonto, Scan & Betal, partner benefits and Samvirke. Coop says it asks 1,000 co-owners every week about topics from prices to chemicals, which links customer knowledge to cooperative identity.

### Revenue streams

Public evidence points to physical grocery retail sales as the primary revenue stream. Private labels likely support margin and differentiation, but exact margin data was not found. Coop Danmark reported DKK 32.565bn in 2025 net revenue; including brugsforeninger, net revenue was DKK 44.756bn. Lobyco may create platform/OEM revenue, but public Coop Denmark sources do not quantify this.

### Key resources

Key resources are the store network, more than 2 million members, Coop App data and engagement, private-label brands such as Coop, Xtra, Änglamark and Irma, supplier relationships, Coop Trading, Lobyco, the Coop One IT foundation and brand equity from the cooperative/Brugsen history.

### Key activities

Key activities are grocery store operations, procurement, category management, private-label development, campaigns, member/bonus administration, app development, data personalization, supplier collaboration, store-format management and turnaround execution focused on the core physical business.

### Key partners

Key partners include OK a.m.b.a. as co-owner, brugsforeninger, Coop Trading, 700+ suppliers in Coop Trading's supplier base, partner-benefit companies, Coop Bank/FordelsKonto infrastructure, payment providers and Lobyco's external retail clients.

### Cost structure

The cost structure is store-heavy: employees, rent/property, logistics, inventory, energy, IT platforms, app/loyalty operations and restructuring. The closure of Coop.dk MAD and Coop.dk webshop is important evidence that some digital channels did not fit the economics of Coop's core business.

## 6. Coop's chain portfolio and brand architecture

Kvickly appears as the broad large-store format. Its page shows weekly offers, member discounts, 5% fruit and vegetable bonus, Discountmatch and nonfood categories such as bikes, suggesting a value proposition of broad assortment plus price/member benefits.

SuperBrugsen presents itself around quality and taste: "En bid bedre. Hver dag." It also claims local goods and discount match. This is a quality/local supermarket position with price pressure still visible.

Brugsen is the local-community format. It says it lives "af og for" being close to the customer's everyday life, supports local community life and learns local customers. Its Lav Pris programme uses store till data to choose almost 300 low-price products.

365discount is the price-led format. It describes itself as a low-price supermarket with discount prices, quality, organic everyday economy, Danish goods, no-unnecessary-chemistry products, easy meal solutions and fresh produce.

The chain portfolio suggests strategic breadth but also complexity. Coop is not positioned only as discount, quality, local, responsible or digital. The shared membership/app layer appears to be the mechanism that tries to hold the portfolio together.

## 7. Coop App, Lobyco and digital value creation

The Coop App functions as a digital companion to physical grocery shopping. Official sources describe Scan & Betal, payment, bonus balance, personal offers, member offers, digital receipts, shareable shopping lists, recipes, digital circulars, Samvirke, games, climate footprint, organic share and local store content. These are mostly store-supporting features.

Lobyco and Shortcut change the interpretation of Coop's digital capability. Lobyco presents Coop's loyalty platform as a reusable retail technology product, and Shortcut describes the Coop App as transformed into an OEM solution and core of several large retail-chain customer apps. Lobyco vendor sources say Coop has more than 1.8m app users, reaches 25% of Danish households, has about 880,000 monthly active users and sees 50% higher shopping frequency among app users. Shortcut reports over 1.5m downloads and daily users above 250,000. These are useful numbers, but because Lobyco and Shortcut sell digital retail services, their interpretation should be treated cautiously.

Playable adds evidence on how games and retail media fit into the digital model. Its vendor case says Coop uses app games with supplier-funded branded prizes, linking customer engagement, supplier exposure and in-store redemption. It reports +100,000 unique players per game, 9% higher basket value among prize redeemers in 2023, 4.25m Christmas game plays and 500,000 Christmas prizes redeemed in Coop stores. These figures are useful for understanding the app-store-supplier triangle, but they are vendor-reported.

### DVC mapping

- Experiences: Scan & Betal, games, recipes, digital circulars, receipts and shopping lists.
- Relationships: membership, co-ownership, bonus, personal offers, partner benefits and app engagement.
- Evolution: shift from analogue member organisation to app-enabled loyalty, while closing online grocery and webshop channels.
- Digital competences: personalization, loyalty mechanics, app development, multi-banner campaign management, gamification/retail-media campaign execution and data-based offer selection.
- Digital infrastructure: one app across four banners, Coop One, purchase data, payment integrations, FordelsKonto and Lobyco.
- Digital outputs: personal offers, bonus balances, climate footprint, receipts, games, Scan & Betal and campaign activation.
- Relevance: customer-specific offers, local store content, organic/climate insight and price/bonus relevance.

## 8. Strategic positioning

Coop performs many standard grocery activities: store operations, weekly offers, price campaigns, private labels and supplier management. It performs some of these in a different way by linking them to cooperative ownership, local store influence, responsible-product claims and a shared app/loyalty platform.

Coop's position is internally complex. It is primarily a physical grocery retailer by revenue, stores and channel logic. It is also a member organisation by ownership and customer relationship. It is a loyalty platform through Coop App and Lobyco. It is a discount player through 365discount, but also a quality/local player through SuperBrugsen and Brugsen. It is therefore best described as a mixed model: cooperative store-based grocery retail with a shared digital loyalty layer.

## 9. Key numbers

{numbers_table}

## 10. Tensions and contradictions

- App success vs financial weakness: vendor sources report strong app reach and engagement, while financial sources show Coop was recently loss-making and still reported EBIT of -DKK 215m in 2025.
- Digital frontrunner vs closed online grocery: Coop.dk MAD closed in 2023 and Coop.dk webshop closed in 2025, while the app remains central.
- Member value vs price-sensitive grocery market: Coop emphasizes co-ownership, responsibility and bonus, while chain pages emphasize Discountmatch, Lav Pris and 365discount.
- Many chain concepts vs clarity: Kvickly, SuperBrugsen, Brugsen and 365discount each carry different value propositions; the app and membership try to connect them.
- Lobyco/Shortcut OEM platform vs store logic: vendor cases point to platform capability, but Coop's disclosed economics and closures point back to physical stores as the core.
- Marketing claims vs outcomes: Lobyco, Shortcut and Playable claim strong app/gamification outcomes, but public sources do not prove causality or disclose app profitability.

## 11. Theory mapping

{theory_table}

## 12. Gaps and uncertainties

- Retail media data for Coop Denmark was found mainly in Playable vendor material, not in strong public Danish financial sources.
- Exact revenue or profit contribution from Coop App, Lobyco, retail media, games or personalization was not found.
- App-store ratings/download counts were searched and scraped, but crawler extraction may be partial and they are not used as primary evidence.
- Chain-specific revenue/profit/store counts for Kvickly, SuperBrugsen, Brugsen and 365discount were not found in extractable public sources during this run.
- The source set verifies Coop.dk MAD closure and Coop.dk webshop closure, but public sources do not quantify total savings from each closure.
- Lobyco app metrics are useful but not independently verified; they should be cited as vendor-reported figures.
- Spending/basket uplift from games, retail media and individual app features was found only in vendor marketing sources, not independent/financial sources.

## 13. Source list

{chr(10).join(source_links)}
"""
    (OUT_DIR / "coop_business_model_analysis.md").write_text(content, encoding="utf-8")


def write_one_page():
    content = f"""# Coop business model one-page summary

## Coop in one sentence

Coop Denmark is a member-owned, store-based grocery retailer with four main banners and a shared digital loyalty/app layer that tries to connect price, locality, responsibility and member value.

## Business model in 5 bullets

- Core revenue is physical grocery retail: DKK 32.565bn in Coop Danmark A/S revenue in 2025; DKK 44.756bn including brugsforeninger.
- Core channel is stores: 536 Coop Danmark stores and 900 stores including brugsforeninger in 2025.
- Membership is a key resource: more than 2m members/co-owners and DKK 200 member capital contribution.
- Private labels are central: Coop has 3,000+ products; Änglamark has 1,200+ responsibility-oriented products.
- Digital supports loyalty and stores more than e-commerce: Coop.dk MAD closed in 2023 and Coop.dk webshop closed in 2025.

## Customer value proposition in 5 bullets

- Member value: bonus, member offers, personal offers and partner benefits.
- Price value: 365discount, Discountmatch, Lav Pris and 5% bonus on fresh fruit and vegetables.
- Convenience: local stores, app planning, Scan & Betal, receipts and shopping lists.
- Quality/locality: SuperBrugsen and Brugsen emphasize taste, local goods and community.
- Responsibility: strict product requirements, chemical avoidance, Änglamark and climate/organic app insights.

## Digital model in 5 bullets

- Coop App is a store companion: offers, bonus, Scan & Betal, receipts, shopping list, recipes and local content.
- Personal offers use purchase data and must be activated before purchase.
- Games create engagement and send prizes/bonus/discounts back into the store relationship.
- Lobyco makes Coop's loyalty capabilities reusable for other retailers; vendor-reported numbers include 1.8m users and 880,000 MAU.
- Digital does not currently mean online grocery delivery; Coop's digital strength is customer relationship and store support.

## Main tension in 5 bullets

- Coop has strong digital engagement but the economic core is still physical grocery stores.
- Coop presents cooperative/member values while also competing in a price-sensitive market.
- The chain portfolio gives reach but creates a mixed strategic position.
- Lobyco suggests platform/OEM potential, while Coop's disclosed turnaround focuses on core store operations.
- App metrics are promising but mostly vendor-reported; financial outcomes remain store-economics driven.

## Best numbers to cite in the exam

{md_table(["metric", "value", "year", "source"], [(m, v, y, s) for m, v, y, s, _, _ in KEY_NUMBERS[:12]])}
"""
    (OUT_DIR / "coop_business_model_one_page.md").write_text(content, encoding="utf-8")


def write_pdf_summary():
    pdf_path = OUT_DIR / "coop_key_takeaways_summary.pdf"
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        rightMargin=1.2 * cm,
        leftMargin=1.2 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
    )
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontSize=7.5, leading=9))
    styles.add(ParagraphStyle(name="Tiny", parent=styles["BodyText"], fontSize=6.5, leading=8))
    story = []
    story.append(Paragraph("Coop business model - key takeaways", styles["Title"]))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("1. Absolute key takeaways", styles["Heading2"]))
    bullets = [
        "Coop is primarily a physical grocery retailer with a cooperative/member ownership layer.",
        "The shared Coop App connects four banners through offers, bonus, Scan & Betal, receipts, shopping lists and games.",
        "The customer promise mixes price, membership, convenience, locality, quality and responsibility.",
        "Lobyco makes Coop's loyalty capability look like a platform/OEM asset, but public revenue impact is not disclosed.",
        "Online grocery delivery is closed; digital is mainly store-supporting, not e-commerce-led.",
        "Financial performance improved in 2025, but EBIT remained negative.",
    ]
    for b in bullets:
        story.append(Paragraph(f"- {b}", styles["Small"]))
    story.append(Spacer(1, 0.15 * cm))
    story.append(Paragraph("2. Key numbers", styles["Heading2"]))
    key_rows = [["metric", "value", "year", "source"]] + [[m, v, y, s] for m, v, y, s, _, _ in KEY_NUMBERS[:10]]
    table = Table(key_rows, colWidths=[5.4 * cm, 3.3 * cm, 1.4 * cm, 7.0 * cm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E7E1D7")),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONT", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 6.3),
                ("LEADING", (0, 0), (-1, -1), 7.2),
            ]
        )
    )
    story.append(table)
    story.append(PageBreak())
    story.append(Paragraph("3. What Coop appears to stand for", styles["Heading2"]))
    stance_rows = [
        ["element", "evidence", "interpretation"],
        ["Member ownership", "More than 2m members/co-owners; no shareholders claim.", "Membership is identity and loyalty, not only discounts."],
        ["Local/community", "Brugsen local-store language; local boards; weekly member listening.", "Coop positions stores as community infrastructure."],
        ["Responsible food", "Änglamark 1,200+ products; strict product/chemical claims.", "Responsibility is productized through private labels and app insight."],
        ["Price/member value", "5% fresh produce bonus; Discountmatch; Lav Pris; 365discount.", "Coop must also answer a price-sensitive market."],
        ["Digital convenience", "Scan & Betal, personal offers, receipts, shopping list, games.", "Digital strengthens the physical-store relationship."],
    ]
    table2 = Table(stance_rows, colWidths=[3.6 * cm, 7.2 * cm, 6.2 * cm])
    table2.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E7E1D7")),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONT", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 6.5),
                ("LEADING", (0, 0), (-1, -1), 7.5),
            ]
        )
    )
    story.append(table2)
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph("4. Main strategic tension", styles["Heading2"]))
    tension = (
        "Coop appears to have a strong digital customer relationship through the Coop App and Lobyco. "
        "Vendor sources report more than 1.8m app users and about 880,000 monthly active users. "
        "But the core of the business is still physical stores and grocery retail economics: 536 Coop Danmark stores, "
        "900 stores including brugsforeninger, and DKK 44.756bn revenue including brugsforeninger in 2025. "
        "The closure of Coop.dk MAD in 2023 and Coop.dk webshop in 2025 shows that digital ambition has been narrowed "
        "toward store support and loyalty rather than full online grocery commerce. This is an analytical tension, not a recommendation."
    )
    story.append(Paragraph(tension, styles["Small"]))
    story.append(Spacer(1, 0.15 * cm))
    mini_rows = [
        ["apparent business model", "value proposition", "strategic tension"],
        ["Store-based grocery retail plus cooperative membership and app loyalty.", "Price, member value, convenience, locality, quality and responsibility.", "Digital loyalty/platform strength versus physical-store economics and chain complexity."],
    ]
    table3 = Table(mini_rows, colWidths=[5.5 * cm, 5.6 * cm, 5.9 * cm])
    table3.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E7E1D7")),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("FONT", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 6.5),
                ("LEADING", (0, 0), (-1, -1), 7.5),
            ]
        )
    )
    story.append(table3)
    doc.build(story)


def write_readme_and_index():
    readme = f"""# {RUN_ID}

## Purpose

This run investigates Coop Denmark's business model, strategic positioning, customer value proposition, member organisation, app/Lobyco model and evidence-based tensions for a CBS IT-strategy exam project. It does not contain recommendations.

## Method

- Crawl4AI scraped public web sources on {ACCESS_DATE}. Where Crawl4AI returned a Markdown/JSON `NoneType` error for accessible public HTML pages, a documented urllib/BeautifulSoup fallback was used and marked inside the raw source file.
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
"""
    (RUN_DIR / "README.md").write_text(readme, encoding="utf-8")

    index_path = Path("reports/webscraping_runs/index.md")
    existing = index_path.read_text(encoding="utf-8") if index_path.exists() else "# Webscraping runs\n\n"
    entry = f"- `{RUN_ID}`: Coop Denmark business model, strategic positioning, member/app/Lobyco analysis using Crawl4AI and local annual-report PDFs.\n"
    if RUN_ID not in existing:
        if not existing.endswith("\n"):
            existing += "\n"
        existing += entry
    index_path.write_text(existing, encoding="utf-8")


async def main():
    for d in [RAW_DIR, DATA_DIR, LOG_DIR, OUT_DIR]:
        d.mkdir(parents=True, exist_ok=True)
    extract_pdf_sources()
    scrape_web_sources()
    write_csvs()
    write_analysis()
    write_one_page()
    write_pdf_summary()
    write_readme_and_index()


if __name__ == "__main__":
    asyncio.run(main())
