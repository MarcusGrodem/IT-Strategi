#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path
from textwrap import wrap

RUN_DIR = Path("reports/webscraping_runs/2026-05-03_1619_coop_competitor_analysis")
DATA_DIR = RUN_DIR / "data"
OUT_DIR = RUN_DIR / "final_outputs"
ACCESS_DATE = "2026-05-03"


sources = [
    {
        "source_url": "https://sallinggroup.com/en/stores/key-figures",
        "source_title": "The most important financial figures",
        "publisher": "Salling Group",
        "source_type": "official company key figures",
        "date_published_or_year": "2025",
        "reliability_assessment": "High: official company figures; annual-report-style key figures.",
        "marketing_source_yes_no": "no",
        "notes": "Includes 2025 revenue, EBIT, profit, stores and employees.",
    },
    {
        "source_url": "https://sallinggroup.com/nyheder/international-vaekst-loefter-salling-group-til-historisk-niveau/14899554",
        "source_title": "International vækst løfter Salling Group til historisk niveau",
        "publisher": "Salling Group",
        "source_type": "official press release",
        "date_published_or_year": "2026-04-27",
        "reliability_assessment": "Medium-high: official, but narrative framing is promotional.",
        "marketing_source_yes_no": "yes",
        "notes": "Explains 2025 growth, Rimi Baltic acquisition and investments.",
    },
    {
        "source_url": "https://netto.dk/netto-plus/",
        "source_title": "Netto+ fordelsprogram",
        "publisher": "Netto",
        "source_type": "official app/loyalty page",
        "date_published_or_year": "not found",
        "reliability_assessment": "Medium: official feature description; marketing language.",
        "marketing_source_yes_no": "yes",
        "notes": "Personal +Priser, Scan&Go, freshness guarantee, MobilePay.",
    },
    {
        "source_url": "https://support.netto.dk/hc/da/articles/30919097799057-Hvordan-bruger-jeg-Scan-Go",
        "source_title": "Hvordan bruger jeg Scan&Go?",
        "publisher": "Netto",
        "source_type": "official support page",
        "date_published_or_year": "2024-12-13 / updated",
        "reliability_assessment": "High for feature mechanics.",
        "marketing_source_yes_no": "no",
        "notes": "Explains Scan&Go flow and rollout via new store concept.",
    },
    {
        "source_url": "https://www.bilka.dk/scango/",
        "source_title": "Bilka Scan&Go",
        "publisher": "Bilka",
        "source_type": "official app/scan page",
        "date_published_or_year": "not found",
        "reliability_assessment": "High for feature mechanics; marketing tone.",
        "marketing_source_yes_no": "yes",
        "notes": "Scan, pack and pay in Bilka Plus app.",
    },
    {
        "source_url": "https://support.bilka.dk/hc/da/articles/36560426099857-Scan-Go-i-Bilka-Plus-appen",
        "source_title": "Scan&Go i Bilka Plus appen",
        "publisher": "Bilka",
        "source_type": "official support page",
        "date_published_or_year": "2025-06-26",
        "reliability_assessment": "High for feature mechanics.",
        "marketing_source_yes_no": "no",
        "notes": "States Scan&Go is integrated into Bilka Plus and replaces separate app.",
    },
    {
        "source_url": "https://support.foetex.dk/hc/da/articles/28279829727633-f%C3%B8tex-Scan-Go",
        "source_title": "føtex Scan&Go",
        "publisher": "føtex",
        "source_type": "official support page",
        "date_published_or_year": "2026-02-10 / updated",
        "reliability_assessment": "High for feature mechanics.",
        "marketing_source_yes_no": "no",
        "notes": "States Scan&Go is available in all stores except føtex Go.",
    },
    {
        "source_url": "https://rema1000.dk/information/scan-selv",
        "source_title": "REMA 1000 Scan Selv",
        "publisher": "REMA 1000 Denmark",
        "source_type": "official app/scan page",
        "date_published_or_year": "not found",
        "reliability_assessment": "High for feature mechanics.",
        "marketing_source_yes_no": "yes",
        "notes": "Scan, pay and exit QR flow.",
    },
    {
        "source_url": "https://apps.apple.com/dk/app/rema-1000/id426938378",
        "source_title": "REMA 1000 App Store page",
        "publisher": "Apple App Store / REMA 1000 Denmark",
        "source_type": "app store page",
        "date_published_or_year": "accessed 2026",
        "reliability_assessment": "Medium-high for ratings and app description.",
        "marketing_source_yes_no": "yes",
        "notes": "Shopping lists, offers, recipes and ratings.",
    },
    {
        "source_url": "https://play.google.com/store/apps/details?id=dk.rema1000.app",
        "source_title": "REMA 1000 Scan Selv Google Play page",
        "publisher": "Google Play / REMA 1000 Denmark",
        "source_type": "app store page",
        "date_published_or_year": "2025 / accessed 2026",
        "reliability_assessment": "Medium-high for downloads and app description.",
        "marketing_source_yes_no": "yes",
        "notes": "100K+ downloads and Scan Selv description.",
    },
    {
        "source_url": "https://rema1000.dk/vores-historie/reitan",
        "source_title": "REITAN - et værdidrevet selskab",
        "publisher": "REMA 1000 Denmark",
        "source_type": "official company page",
        "date_published_or_year": "not found",
        "reliability_assessment": "High for ownership structure.",
        "marketing_source_yes_no": "yes",
        "notes": "REMA Denmark is part of REITAN RETAIL.",
    },
    {
        "source_url": "https://ansvarlighed.rema1000.dk/samfundsansvar",
        "source_title": "Samfundsansvar i REMA 1000",
        "publisher": "REMA 1000 Denmark",
        "source_type": "official responsibility page",
        "date_published_or_year": "2024 report page / accessed 2026",
        "reliability_assessment": "High for store count statement.",
        "marketing_source_yes_no": "yes",
        "notes": "States more than 420 stores in Denmark.",
    },
    {
        "source_url": "https://ni.dk/ni-news/id/56662f68-b455-489a-bebe-706b19ceda1c/Analyse-giver-Rema-1000-discounttronen---Nettos-ejer-afviser-blankt",
        "source_title": "Analyse giver Rema 1000 discounttronen - Nettos ejer afviser blankt",
        "publisher": "Ritzau / NI",
        "source_type": "trade/news source",
        "date_published_or_year": "2025-11-06",
        "reliability_assessment": "Medium: reports Retail Institute figures and Salling's objection.",
        "marketing_source_yes_no": "no",
        "notes": "Useful because it includes both estimate and contestation.",
    },
    {
        "source_url": "https://www.paqle.dk/p/rema-1000/227324/finance",
        "source_title": "Rema 1000 finance",
        "publisher": "Paqle",
        "source_type": "financial database",
        "date_published_or_year": "2024",
        "reliability_assessment": "Medium: secondary database based on filed accounts.",
        "marketing_source_yes_no": "no",
        "notes": "Used where official Danish financial page was not found.",
    },
    {
        "source_url": "https://www.lidl.dk/c/lidl-plus/s10013731",
        "source_title": "Lidl Plus",
        "publisher": "Lidl Denmark",
        "source_type": "official loyalty page",
        "date_published_or_year": "2026-03-02 shown in page",
        "reliability_assessment": "Medium: official features; marketing language.",
        "marketing_source_yes_no": "yes",
        "notes": "Digital customer card, discounts, weekly offers, receipts, store finder and click-and-collect.",
    },
    {
        "source_url": "https://www.lidl.dk/c/lidl-plus-kuponer/s10014639",
        "source_title": "Lidl Plus-kuponer",
        "publisher": "Lidl Denmark",
        "source_type": "official loyalty page",
        "date_published_or_year": "accessed 2026",
        "reliability_assessment": "Medium-high for feature mechanics.",
        "marketing_source_yes_no": "yes",
        "notes": "Personal offers and weekly coupons.",
    },
    {
        "source_url": "https://www.lidl.dk/c/lidl-plus-kupon-plus/s10014640",
        "source_title": "Kupon Plus",
        "publisher": "Lidl Denmark",
        "source_type": "official loyalty page",
        "date_published_or_year": "accessed 2026",
        "reliability_assessment": "Medium-high for feature mechanics.",
        "marketing_source_yes_no": "yes",
        "notes": "Purchase goals convert into exclusive coupons.",
    },
    {
        "source_url": "https://via.ritzau.dk/pressemeddelelse/14578254/kunderne-har-talt-lidl-giver-mest-vaerdi-for-pengene-og-leverer-bedst-pa-frugt-og-gront?publisherId=13559974&lang=da",
        "source_title": "Kunderne har talt: Lidl giver mest værdi for pengene",
        "publisher": "Lidl Denmark / Ritzau",
        "source_type": "official press release",
        "date_published_or_year": "2025-09-15",
        "reliability_assessment": "Medium: reports external survey but via Lidl press release.",
        "marketing_source_yes_no": "yes",
        "notes": "BrancheIndex 2025 value-for-money result; source sample stated.",
    },
    {
        "source_url": "https://onp.dk/seneste-nyheder/lidl-vil-aabne-mere-end-60-nye-butikker-i-danmark/",
        "source_title": "Lidl vil åbne mere end 60 nye butikker i Danmark",
        "publisher": "ONP.dk / Ritzau",
        "source_type": "news source",
        "date_published_or_year": "2023-03-06",
        "reliability_assessment": "Medium: older secondary source; useful for expansion logic and store-count baseline.",
        "marketing_source_yes_no": "no",
        "notes": "No newer official Danish Lidl store-count page was found in this run.",
    },
    {
        "source_url": "https://www.dagrofa.dk/artikel/dagrofa-loefter-driftsresultatet-og-omsaetningen-naar-rekordhoeje-209-mia-kr/",
        "source_title": "Dagrofa løfter driftsresultatet og omsætningen når rekordhøje 20,9 mia. kr.",
        "publisher": "Dagrofa",
        "source_type": "official press release",
        "date_published_or_year": "2026-03-26",
        "reliability_assessment": "Medium-high: official numbers; promotional framing.",
        "marketing_source_yes_no": "yes",
        "notes": "Used because annual-report PDF crawl returned little text.",
    },
    {
        "source_url": "https://www.dagrofa.dk/kaeder/",
        "source_title": "Vores retail kæder",
        "publisher": "Dagrofa",
        "source_type": "official company page",
        "date_published_or_year": "accessed 2026",
        "reliability_assessment": "High for chain positioning.",
        "marketing_source_yes_no": "yes",
        "notes": "MENY, SPAR, Min Købmand and Let-Køb positioning.",
    },
    {
        "source_url": "https://www.dagrofa.dk/artikel/meny-kaares-som-danmarks-staerkeste-dagligvarebrand/",
        "source_title": "MENY kåres som Danmarks stærkeste dagligvarebrand",
        "publisher": "Dagrofa",
        "source_type": "official press release",
        "date_published_or_year": "2025-09-13",
        "reliability_assessment": "Medium: reports external Loyalty Group survey through Dagrofa.",
        "marketing_source_yes_no": "yes",
        "notes": "MENY wins 5 of 8 areas; 4,694 respondents.",
    },
    {
        "source_url": "https://www.dagrofa.dk/wp-content/uploads/2026/03/DAGROFA_AaRSRAPPORT_2025_144DPI_1.pdf",
        "source_title": "Dagrofa årsrapport 2025",
        "publisher": "Dagrofa",
        "source_type": "annual report PDF",
        "date_published_or_year": "2025",
        "reliability_assessment": "High in principle, but Crawl4AI extraction failed for this PDF.",
        "marketing_source_yes_no": "no",
        "notes": "Raw source contains metadata only; official press page used for extracted figures.",
    },
    {
        "source_url": "https://play.google.com/store/apps/details?id=dk.meny",
        "source_title": "MENY Danmark Google Play page",
        "publisher": "Google Play / Dagrofa",
        "source_type": "app store page",
        "date_published_or_year": "2025 / accessed 2026",
        "reliability_assessment": "Medium-high for downloads and app description.",
        "marketing_source_yes_no": "yes",
        "notes": "100K+ downloads; member prices and food inspiration.",
    },
    {
        "source_url": "https://apps.apple.com/dk/app/spar-sammen/id586234461",
        "source_title": "SPAR SAMMEN App Store page",
        "publisher": "Apple App Store / Dagrofa",
        "source_type": "app store page",
        "date_published_or_year": "accessed 2026",
        "reliability_assessment": "Medium-high for ratings and app description.",
        "marketing_source_yes_no": "yes",
        "notes": "4.6 rating, 2.3K ratings, member prices and recipes.",
    },
    {
        "source_url": "https://via.ritzau.dk/pressemeddelelse/14710924/nemlig-fortsaetter-vaeksten-og-halverer-underskud-i-nyt-regnskabsar?publisherId=13560508&lang=da",
        "source_title": "Nemlig fortsætter væksten og halverer underskud",
        "publisher": "nemlig.com / Ritzau",
        "source_type": "official press release",
        "date_published_or_year": "2026-01",
        "reliability_assessment": "Medium-high: official financial release, but promotional.",
        "marketing_source_yes_no": "yes",
        "notes": "2024/2025 revenue, adjusted EBITDA and coverage claims.",
    },
    {
        "source_url": "https://www.proff.dk/regnskab/nemlig.com-as/odense-s/n%C3%A6rings-og-nydelsesmidler/GXIFMDI116S",
        "source_title": "nemlig.com A/S regnskab",
        "publisher": "Proff.dk",
        "source_type": "financial database",
        "date_published_or_year": "2025-07",
        "reliability_assessment": "Medium: secondary database based on accounts.",
        "marketing_source_yes_no": "no",
        "notes": "Useful cross-check of official press figures.",
    },
    {
        "source_url": "https://play.google.com/store/apps/details?id=com.nemlig",
        "source_title": "nemlig.com Google Play page",
        "publisher": "Google Play / nemlig.com",
        "source_type": "app store page",
        "date_published_or_year": "2025 / accessed 2026",
        "reliability_assessment": "Medium-high for downloads, rating and app description.",
        "marketing_source_yes_no": "yes",
        "notes": "4.6 rating, 100K+ downloads and app functions.",
    },
    {
        "source_url": "https://via.ritzau.dk/pressemeddelelse/14785234/nemlig-styrker-oko-andelen-trods-pres-i-markedet?lang=da&publisherId=13560508",
        "source_title": "Nemlig styrker øko-andelen trods pres i markedet",
        "publisher": "nemlig.com / Ritzau",
        "source_type": "official press release",
        "date_published_or_year": "2026-02-06",
        "reliability_assessment": "Medium-high: official figure; promotional framing.",
        "marketing_source_yes_no": "yes",
        "notes": "Organic share increased to 23.8% in 2025.",
    },
    {
        "source_url": "https://loyaltygroup.dk/brancheanalyser/brancheindex/brancheindex-dagligvarer/",
        "source_title": "BrancheIndex Dagligvarer 2025",
        "publisher": "Loyalty Group",
        "source_type": "market/customer index",
        "date_published_or_year": "2025",
        "reliability_assessment": "Medium-high: external survey, but full methodology/data not fully open.",
        "marketing_source_yes_no": "no",
        "notes": "Meny first, Rema down, Lidl third, Coop chains mixed/weak.",
    },
    {
        "source_url": "https://www.danskindustri.dk/vi-radgiver-dig/ecommerce/di-e-commerce-analyser/analyser/2026/danskernes-arlige-e-commerce-tracker-2025/",
        "source_title": "Danskernes årlige e-commerce tracker 2025",
        "publisher": "Dansk Industri",
        "source_type": "market report",
        "date_published_or_year": "2026-02-04",
        "reliability_assessment": "Medium-high: trade association analysis; aggregate e-commerce, not grocery-specific.",
        "marketing_source_yes_no": "no",
        "notes": "136bn DKK online consumption, 81% monthly online shoppers, 49% mobile purchases.",
    },
    {
        "source_url": "LLM/CONTEXT.md and LLM/Markdown/opgavebeskrivelse_eksamen_it_strategi_2026.md",
        "source_title": "Project context and official exam assignment notes",
        "publisher": "CBS exam material / local context",
        "source_type": "local exam context",
        "date_published_or_year": "2026",
        "reliability_assessment": "High for case framing; Lobyco figures still require source criticism.",
        "marketing_source_yes_no": "mixed",
        "notes": "Used only for Coop comparison baseline.",
    },
]


findings = [
    ["Salling Group", "Group / Netto / føtex / Bilka", "https://sallinggroup.com/en/stores/key-figures", "official company key figures", "2025", "financial statistic", "Revenue", "83.168 bn DKK", "Netto+, Bilka Plus and føtex plus apps support offers and Scan&Go", "Scale retail group across discount, supermarket and hypermarket", "Scale and profitable operations alongside digital store utilities", "Contrasts with Coop's 2025 loss and closed online store", "Strategic positioning; Implementation", "high", "Salling reports 2025 revenue of 83,168m DKK and profit of 1,990m DKK."],
    ["Salling Group", "Netto Denmark", "https://sallinggroup.com/en/stores/key-figures", "official company key figures", "2025", "store statistic", "Netto Denmark stores", "578", "Netto+ with personal +Prices and Scan&Go", "Discount and convenience", "Dense discount footprint combined with app-based price/time savings", "Coop's 365discount is weaker in Loyalty Group's 2025 customer index", "Implementation; Strategic positioning", "high", "Salling lists 578 Netto Denmark stores at 31/12/2025."],
    ["Salling Group", "Netto+", "https://netto.dk/netto-plus/", "official app/loyalty page", "2026", "digital feature", "Netto+ features", "Personal +Priser; freshness guarantee; Scan&Go; MobilePay", "Save time and money in Netto stores", "Digital solution reinforces discount/convenience promise", "Coop also has Scan & Pay, but competitor ties app tightly to one clear chain concept", "Digital Value Creation: Experiences and Relationships", "medium", "Netto+ page lists personal prices, Scan&Go and other benefits."],
    ["Salling Group", "Bilka", "https://support.bilka.dk/hc/da/articles/36560426099857-Scan-Go-i-Bilka-Plus-appen", "official support page", "2025", "digital feature", "Scan&Go integration", "Separate Scan&Go app replaced by Bilka Plus app", "Large-format shopping made faster", "Consolidates scan functionality inside chain-specific app", "Unlike Coop's one app across heterogeneous chains, Salling uses chain-branded apps", "Implementation", "high", "Support page states Bilka Plus app replaces the previous separate Scan&Go app."],
    ["Salling Group", "føtex", "https://support.foetex.dk/hc/da/articles/28279829727633-f%C3%B8tex-Scan-Go", "official support page", "2026", "digital feature", "Scan&Go availability", "All stores except føtex Go", "Supermarket convenience and queue reduction", "Physical-store integration rather than standalone digital strategy", "Coop's app functionality is strong, but financial comparison suggests execution fit matters", "Digital Value Creation: Experiences; Implementation", "high", "føtex support states Scan&Go can be used in all stores except føtex Go."],
    ["REMA 1000 Denmark", "REMA 1000", "https://www.paqle.dk/p/rema-1000/227324/finance", "financial database", "2024", "financial statistic", "Revenue", "28.478 bn DKK", "REMA app for planning and Scan Selv app for checkout", "Hard discount with simple everyday value", "Clear discount model with strong revenue and profit", "Coop has larger app narrative but weaker group result in the case context", "Strategic positioning", "medium", "Paqle lists 2024 revenue of 28,478,327 thousand DKK."],
    ["REMA 1000 Denmark", "REMA 1000", "https://www.paqle.dk/p/rema-1000/227324/finance", "financial database", "2024", "financial statistic", "Profit for year", "515.650 m DKK", "Planning app plus Scan Selv", "Simple price-led shopping", "Operational model appears profitable without relying on broad digital ecosystem claims", "Coop's app reach does not by itself offset group losses", "Implementation; Strategic positioning", "medium", "Paqle lists 2024 profit for the year of 515,650 thousand DKK."],
    ["REMA 1000 Denmark", "REMA 1000", "https://ni.dk/ni-news/id/56662f68-b455-489a-bebe-706b19ceda1c/Analyse-giver-Rema-1000-discounttronen---Nettos-ejer-afviser-blankt", "trade/news source", "2025", "market share", "Retail Institute market share", "18.2% vs Netto 17.9%; contested by Salling", "Discount chain scale", "Reported share gain supports discount-strength interpretation but should be used cautiously", "Coop comparison should avoid overclaiming because source includes dispute", "Strategic positioning; Source criticism", "medium", "Article reports Retail Institute's 18.2%/17.9% estimate and Salling's objection."],
    ["REMA 1000 Denmark", "REMA 1000", "https://ansvarlighed.rema1000.dk/samfundsansvar", "official responsibility page", "2024", "store statistic", "Store count", "More than 420 stores", "Physical discount network supported by apps", "Strong footprint supports convenient everyday shopping", "Coop's larger/mixed chain portfolio may be less conceptually clear", "Implementation", "high", "REMA states it has more than 420 stores in Denmark."],
    ["REMA 1000 Denmark", "REMA Scan Selv", "https://rema1000.dk/information/scan-selv", "official app/scan page", "2026", "digital feature", "Scan Selv", "Scan items; pay with one swipe; exit with QR; receipts", "Simple fast self-checkout", "Digital utility is narrow and store-process oriented", "Coop's app is broader; REMA's solution appears simpler", "Digital Value Creation: Experiences", "high", "Official page says users scan, pay with one swipe and scan a QR code at exit."],
    ["REMA 1000 Denmark", "REMA 1000 app", "https://apps.apple.com/dk/app/rema-1000/id426938378", "app store page", "2026", "app metric", "App Store rating", "3.3 / 5 from approx. 702 ratings", "Shopping lists, offers, recipes and store info", "Planning app supports weekly household shopping", "Lower rating than some competitors suggests digital is not the main success claim", "Digital Business Model: customer knowledge", "medium", "App Store page shows 3.3 rating and 702 ratings."],
    ["REMA 1000 Denmark", "REMA Scan Selv", "https://play.google.com/store/apps/details?id=dk.rema1000.app", "app store page", "2026", "app metric", "Google Play downloads", "100K+", "Scan Selv for all stores", "Checkout utility supports in-store efficiency", "Coop likely has wider app reach, but REMA may win through store/price concept", "Implementation", "medium", "Google Play page shows 100K+ downloads."],
    ["Lidl Denmark", "Lidl", "https://via.ritzau.dk/pressemeddelelse/14578254/kunderne-har-talt-lidl-giver-mest-vaerdi-for-pengene-og-leverer-bedst-pa-frugt-og-gront?publisherId=13559974&lang=da", "official press release", "2025", "customer index", "BrancheIndex result", "Top in value for money and fruit/vegetables; only chain moving forward", "Low price plus quality signal", "Value-for-money perception strengthens discount position", "Coop's 365discount is mentioned as weak in Loyalty Group source", "Strategic positioning", "medium", "Lidl release reports top placement for value for money in BrancheIndex 2025."],
    ["Lidl Denmark", "Lidl", "https://onp.dk/seneste-nyheder/lidl-vil-aabne-mere-end-60-nye-butikker-i-danmark/", "news source", "2023", "store statistic", "Store count and target", "139 stores; target above 200", "Expanding discount footprint", "Expansion guided by economic viability and map discipline", "Contrasts with Coop restructuring and store concept uncertainty", "Implementation; Strategic positioning", "medium-low", "Ritzau/ONP reports 139 stores and goal above 200; source is older."],
    ["Lidl Denmark", "Lidl Plus", "https://www.lidl.dk/c/lidl-plus/s10013731", "official loyalty page", "2026", "digital feature", "Lidl Plus", "Digital card, weekly offers, coupons, receipts, store finder, Click & Collect", "Extra savings through app", "Digital features directly reinforce price promise", "Coop app has more platform breadth; Lidl app is tightly tied to savings", "Digital Value Creation: Relationships", "medium", "Lidl page says Lidl Plus is a digital customer card for discounts and benefits."],
    ["Lidl Denmark", "Lidl Plus", "https://www.lidl.dk/c/lidl-plus-kuponer/s10014639", "official loyalty page", "2026", "digital feature", "Personal coupons", "Personal offers; weekly coupons; auto redemption after scanning Lidl Plus card", "Savings with minimal friction", "Personalization is expressed as price/coupon utility", "Coop personalization exists, but Lidl links personalization to a very clear price cue", "Digital Value Creation: Relationships", "medium", "Coupon page says coupons include personal offers and are redeemed automatically when card is scanned."],
    ["Lidl Denmark", "Kupon Plus", "https://www.lidl.dk/c/lidl-plus-kupon-plus/s10014640", "official loyalty page", "2026", "digital feature", "Purchase-goal coupons", "Purchases registered toward monthly goals; coupons increase with goals reached", "Repeat shopping incentives", "Loyalty mechanic is linked to frequency and basket accumulation", "Similar to Coop gamification, but anchored in Lidl's discount economics", "Digital Value Creation: Relationships", "medium", "Kupon Plus page says each purchase with card is registered toward purchase goals."],
    ["Dagrofa", "Group / MENY / SPAR / Min Købmand / Let-Køb", "https://www.dagrofa.dk/artikel/dagrofa-loefter-driftsresultatet-og-omsaetningen-naar-rekordhoeje-209-mia-kr/", "official press release", "2025", "financial statistic", "Revenue", "20.9 bn DKK", "MENY and SPAR member apps; chain-level concepts", "Food experiences, local merchants and portfolio chains", "Growth in all business legs and record revenue", "Coop has broad chain portfolio but weaker 2025 financials in case context", "Strategic positioning; Implementation", "medium-high", "Dagrofa reports 2025 revenue of 20.9bn DKK."],
    ["Dagrofa", "Group", "https://www.dagrofa.dk/artikel/dagrofa-loefter-driftsresultatet-og-omsaetningen-naar-rekordhoeje-209-mia-kr/", "official press release", "2025", "financial statistic", "EBITDA / operating earnings", "529 m DKK", "Digital growth mentioned alongside retail and foodservice", "Operational improvement and investments", "Transformation from 2018 is presented as sustained improvement", "Contrast with Coop's recovery plan and recent loss", "Implementation", "medium-high", "Dagrofa reports 529m DKK operating earnings in 2025."],
    ["Dagrofa", "Group", "https://www.dagrofa.dk/artikel/dagrofa-loefter-driftsresultatet-og-omsaetningen-naar-rekordhoeje-209-mia-kr/", "official press release", "2025", "store statistic", "Stores", "544", "Chain-level digital/member apps", "Local and food-experience-oriented retail", "Store count grew from 511 in 2018 to 544 in 2025", "Coop's challenge is not only digital reach but chain/store economics", "Implementation", "medium-high", "Dagrofa reports 544 stores in 2025."],
    ["Dagrofa", "MENY", "https://www.dagrofa.dk/artikel/meny-kaares-som-danmarks-staerkeste-dagligvarebrand/", "official press release", "2025", "customer index", "Loyalty Group BrancheIndex", "MENY strongest grocery brand; wins 5 of 8 areas; 4,694 respondents", "Premium food market and service concept", "Clear premium/food-experience position appears valued by customers", "Coop's multiple mid-market chains may be less sharply positioned", "Strategic positioning; Digital Value Creation: Experiences", "medium", "Dagrofa reports MENY wins trust, image, product quality, organic and accessibility."],
    ["Dagrofa", "MENY", "https://www.dagrofa.dk/kaeder/", "official company page", "2026", "positioning evidence", "MENY position", "Broad assortment, gourmet/take-away/basic goods and specialist staff", "Food market with quality and service", "Differentiated activities versus discount chains", "Contrasts with Coop's brand architecture tension", "Strategic positioning", "high", "Dagrofa describes MENY as Danmarks MADmarked with broad assortment and specialist staff."],
    ["Dagrofa", "SPAR", "https://www.dagrofa.dk/kaeder/", "official company page", "2026", "positioning evidence", "SPAR position", "Over 140 stores; local supermarket with discount on everyday items", "Local convenience with value items", "Local merchant identity differentiates from central chain logic", "Coop's Brugsen has similar local heritage but financial weakness remains", "Strategic positioning", "high", "Dagrofa describes SPAR as the local supermarket with over 140 stores."],
    ["Dagrofa", "MENY app", "https://play.google.com/store/apps/details?id=dk.meny", "app store page", "2026", "app metric", "Google Play downloads", "100K+", "Member prices, food inspiration, recipes, shopping lists, payment card link", "Food inspiration plus member prices", "Digital supports premium food concept, not only checkout", "Coop app has strong loyalty but not chain-specific food-experience focus", "Digital Business Model: customer knowledge", "medium", "Google Play page shows 100K+ downloads and MENY app features."],
    ["Dagrofa", "SPAR SAMMEN", "https://apps.apple.com/dk/app/spar-sammen/id586234461", "app store page", "2026", "app metric", "App Store rating", "4.6 / 5 from approx. 2.3K ratings", "Member prices, recipes, weekly leaflet and marketing personalization", "Local loyalty and member pricing", "High app rating suggests user acceptance for SPAR's simpler app scope", "Coop has high reach but source criticism is needed on value claims", "Digital Value Creation: Relationships", "medium", "App Store page shows SPAR SAMMEN at 4.6 from 2.3K ratings."],
    ["Nemlig.com", "Nemlig", "https://via.ritzau.dk/pressemeddelelse/14710924/nemlig-fortsaetter-vaeksten-og-halverer-underskud-i-nyt-regnskabsar?publisherId=13560508&lang=da", "official press release", "2024/2025", "financial statistic", "Revenue", "2.82 bn DKK", "Online supermarket app/webshop with delivery and meal boxes", "Online-first convenience and assortment", "Purpose-built online grocery model continued growth", "Coop closed coop.dk in 2023 due to lack of profitability", "Digital Business Model: controlled value chain; Implementation", "medium-high", "Nemlig reports 2.82bn DKK revenue and 3.3% growth."],
    ["Nemlig.com", "Nemlig", "https://via.ritzau.dk/pressemeddelelse/14710924/nemlig-fortsaetter-vaeksten-og-halverer-underskud-i-nyt-regnskabsar?publisherId=13560508&lang=da", "official press release", "2024/2025", "financial statistic", "Adjusted EBITDA", "35.3 m DKK", "Online delivery infrastructure", "Convenience and wide assortment", "Improving economics, but not unambiguously profitable at bottom line", "Shows online grocery can work only with logistics/economic discipline", "Implementation", "medium-high", "Nemlig reports adjusted EBITDA of 35.3m DKK."],
    ["Nemlig.com", "Nemlig", "https://www.proff.dk/regnskab/nemlig.com-as/odense-s/n%C3%A6rings-og-nydelsesmidler/GXIFMDI116S", "financial database", "2025-07", "financial statistic", "Profit for year", "-28.090 m DKK", "Online grocery operations", "Convenience, delivery and specialty assortment", "Bottom-line loss remains despite revenue growth", "Coop should not be judged against Nemlig as if online grocery is automatically profitable", "Source criticism; Implementation", "medium", "Proff lists 2025 year's result of -28,090 thousand DKK."],
    ["Nemlig.com", "Nemlig", "https://via.ritzau.dk/pressemeddelelse/14710924/nemlig-fortsaetter-vaeksten-og-halverer-underskud-i-nyt-regnskabsar?publisherId=13560508&lang=da", "official press release", "2025", "coverage statistic", "Delivery coverage", "More than 4 of 5 households", "Home delivery and meal boxes", "Scale of delivery coverage supports online-first value proposition", "Coop no longer operates online grocery store", "Digital Business Model", "medium", "Nemlig says more than 4 of 5 households can receive groceries and meal boxes."],
    ["Nemlig.com", "Nemlig app", "https://play.google.com/store/apps/details?id=com.nemlig", "app store page", "2026", "app metric", "Google Play rating/downloads", "4.6 / 5; 100K+ downloads", "Groceries, favorites, shopping lists, recipes and meal boxes", "Mobile ordering experience", "App is core channel, not only loyalty layer", "Coop app supports stores, while Nemlig app is the store", "Digital Business Model; Digital Value Creation: Experiences", "medium", "Google Play page shows 4.6 rating and 100K+ downloads."],
    ["Nemlig.com", "Nemlig", "https://via.ritzau.dk/pressemeddelelse/14785234/nemlig-styrker-oko-andelen-trods-pres-i-markedet?lang=da&publisherId=13560508", "official press release", "2025", "differentiation statistic", "Organic share of sales", "23.8% (up from 22.8% in 2024)", "Online assortment and pricing around organic products", "Assortment differentiation beyond convenience", "Coop has heritage in values/membership, but Nemlig offers clear online assortment promise", "Strategic positioning; Digital Value Creation: Evolution", "medium", "Nemlig says organic share increased to 23.8% in 2025."],
    ["Market context", "Danish e-commerce", "https://www.danskindustri.dk/vi-radgiver-dig/ecommerce/di-e-commerce-analyser/analyser/2026/danskernes-arlige-e-commerce-tracker-2025/", "market report", "2025", "market statistic", "Online consumption", "136 bn DKK; 81% shop online monthly; 49% mobile purchases", "Supports mobile-first customer expectations", "Digital channels are normal customer behavior, but not proof of grocery profitability", "Coop app should be assessed on fit with store economics, not digital adoption alone", "Digital Value Creation: Evolution", "medium-high", "DI reports 136bn DKK online consumption and 49% mobile share of online purchases."],
    ["Market context", "Customer loyalty", "https://loyaltygroup.dk/brancheanalyser/brancheindex/brancheindex-dagligvarer/", "market/customer index", "2025", "customer index", "BrancheIndex ranking", "MENY first; Rema down; Lidl third; Netto and 365discount weak; 4,694 respondents", "Customer loyalty differs strongly by chain concept", "Strong customer perception follows clear promise more than app breadth", "Coop's 365discount weakness is direct contrast inside the discount segment", "Strategic positioning; Source criticism", "medium-high", "Loyalty Group states MENY takes first place and 365discount is isolated at the bottom."],
    ["Coop comparison baseline", "Coop Denmark", "LLM/CONTEXT.md", "local exam context", "2025/2026", "case statistic", "Coop app users", "Approx. 1.8m users / 25% of Danish households", "Personal offers, Scan & Pay, games, retail media and loyalty", "Digital relationship strength is real but must be compared with financial weakness", "Competitors show digital must reinforce the core model and operations", "Digital Value Creation; Source criticism", "medium", "Local context and Lobyco source describe 1.8m Coop app users and 25% household reach."],
    ["Coop comparison baseline", "Coop Denmark", "LLM/CONTEXT.md", "local exam context", "2023/2025", "case statistic", "Coop financial/online context", "2025 net loss 232m DKK; coop.dk closed in 2023", "No current online grocery store; physical stores are core", "Competitor evidence should not become recommendations", "Competitors' stronger fit is about price/store/logistics alignment, not generic digital maturity", "Implementation; Strategic positioning", "medium", "Local context states coop.dk closed in 2023 and Coop lost 232m DKK in 2025."],
]


def write_csv(path: Path, rows: list[dict] | list[list], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        if fieldnames is None:
            raise ValueError("fieldnames required")
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


source_fields = [
    "source_url",
    "source_title",
    "publisher",
    "source_type",
    "date_published_or_year",
    "access_date",
    "reliability_assessment",
    "marketing_source_yes_no",
    "notes",
]
for source in sources:
    source["access_date"] = ACCESS_DATE

finding_fields = [
    "competitor",
    "chain_or_brand",
    "source_url",
    "source_type",
    "year",
    "evidence_type",
    "metric_name",
    "metric_value",
    "digital_solution",
    "customer_value_proposition",
    "observed_success_factor",
    "comparison_to_coop",
    "relevant_theory_lens",
    "confidence_level",
    "quote_or_short_evidence",
]
finding_dicts = [dict(zip(finding_fields, row)) for row in findings]

write_csv(DATA_DIR / "source_register.csv", sources, source_fields)
write_csv(DATA_DIR / "competitor_findings.csv", finding_dicts, finding_fields)

overview_rows = [
    ("Salling Group", "Scale leader with discount, supermarket and hypermarket formats", "Netto+, Bilka Plus and føtex plus with Scan&Go/offers", "83.168bn DKK revenue; 1.990bn DKK profit; 578 Netto DK stores", "Scale, store integration and chain-specific digital tools", "Salling key figures / app pages"),
    ("REMA 1000", "Focused hard discount", "Planning app and Scan Selv checkout app", "28.478bn DKK revenue and 515.650m DKK profit in 2024; >420 stores; reported 18.2% market share contested", "Simple value proposition and profitable discount operations", "Paqle, REMA, Ritzau/NI"),
    ("Lidl Denmark", "International discount challenger", "Lidl Plus digital card, coupons, goals, receipts, store finder", "Top value-for-money in BrancheIndex 2025; 139 stores in older Ritzau source with >200 target", "App reinforces price/value promise", "Lidl/Ritzau, ONP/Ritzau"),
    ("Dagrofa", "Portfolio of premium/local/convenience chains", "MENY and SPAR member apps with prices, recipes and inspiration", "20.9bn DKK revenue; 529m DKK EBITDA; 99m DKK profit; 544 stores", "Clear chain identities and customer loyalty around food/locality", "Dagrofa, Loyalty Group"),
    ("Nemlig.com", "Online-first grocery and meal-box player", "App/webshop with delivery, lists, recipes, favorites and meal boxes", "2.82bn DKK revenue; 35.3m DKK adjusted EBITDA; -28.090m DKK result", "Purpose-built online model but still tight economics", "Nemlig, Proff, Google Play"),
]

report = """# Competitor evidence report: Coop Denmark IT-strategy case

## 1. Purpose and limitation
This report gathers and structures evidence about selected Coop competitors in the Danish grocery and retail market. It is not a recommendation report for Coop. The purpose is to identify empirical patterns in competitors' strategic positions, customer-facing digital solutions, business results and possible reasons they may appear to perform better than Coop in specific areas.

Coop is used only as a comparison point: the local exam context states that Coop has a strong app with approximately 1.8 million users and 25% household reach, but also a 2025 net loss of 232m DKK and a closed online grocery store since 2023. Those facts create the central tension for this evidence review.

## 2. Executive summary
- Competitors that look stronger than Coop do not simply appear “more digital”; their digital tools support clearer business models.
- Salling combines scale, profitability and chain-specific apps with in-store Scan&Go rather than presenting digital as a separate strategic story.
- REMA's strongest evidence is strategic focus: discount, high revenue/profit in secondary accounts data, dense store footprint and a narrow Scan Selv utility.
- Lidl's Lidl Plus is tightly linked to price, coupons and repeat shopping; the app reinforces the discount promise rather than broadening the model.
- Dagrofa and MENY show a different success path: customer loyalty and food-experience positioning, supported by member apps and local/quality concepts.
- Nemlig.com is the clearest online-first contrast to Coop, but the evidence is mixed: revenue and adjusted EBITDA improved, while bottom-line profit remains negative in Proff data.
- Across competitors, the recurring pattern is fit between digital solution, customer promise and operating model.

## 3. Method
Crawl4AI was used to scrape public web sources into Markdown. The crawl prioritized official company key figures, annual/report pages, official app/support pages, app store pages, customer-index sources, and credible Danish trade/news sources. No login, paywall, CAPTCHA bypassing or private data access was used.

Source criticism is important. Official company and press pages are reliable for what the company says, but often promotional. App store pages are useful for ratings, downloads and feature descriptions, but they do not prove business impact. Market/customer-index sources help compare brands but often do not expose full raw survey data. The Dagrofa annual-report PDF was included in the crawl list, but Crawl4AI extracted only metadata; therefore the extracted Dagrofa figures rely on Dagrofa's official 2025 results page.

## 4. Competitor overview table

| Competitor | Main position | Digital solution | Key statistics | Apparent success factor | Strongest source |
|---|---|---|---|---|---|
"""
for row in overview_rows:
    report += "| " + " | ".join(row) + " |\n"

report += """

## 5. Competitor-by-competitor analysis

### Salling Group: Netto, føtex and Bilka
Salling Group appears as the strongest scale competitor in this evidence set. Its 2025 key figures show revenue of 83.168bn DKK, EBIT of 3.245bn DKK and profit for the year of 1.990bn DKK. It also reports 578 Netto stores in Denmark, 119 føtex/føtex food/føtex city stores and 19 Bilka stores.

The digital pattern is chain-specific and store-integrated. Netto+ offers personal +Prices, Scan&Go, freshness guarantee and MobilePay. Bilka has integrated Scan&Go into Bilka Plus and discontinued the separate Scan&Go app. føtex reports Scan&Go availability in all stores except føtex Go. This suggests digital is implemented as a utility inside the physical shopping model.

The contrast with Coop is not that Salling has more advanced digital features. Coop's app is also strong. The contrast is that Salling's digital tools sit inside a profitable and clearly scaled operating model, while Coop's exam context combines app reach with financial weakness and a closed online grocery store.

### REMA 1000 Denmark
REMA is the clearest focused-discount case. Secondary financial data from Paqle lists 2024 revenue of 28.478bn DKK and profit for the year of 515.650m DKK. REMA's own responsibility page states more than 420 Danish stores. A Ritzau/NI article reports Retail Institute figures in which REMA reaches 18.2% market share in 2025 versus Netto's 17.9%, but the same article states that Salling disputes those numbers. The market-share figure should therefore be treated as indicative, not settled fact.

Digitally, REMA's solution is narrower than Coop's. The main app supports offers, recipes and shopping lists. The Scan Selv app lets customers scan items, pay with one swipe and exit with a QR code. Google Play shows 100K+ downloads for Scan Selv. This is digital as in-store process support rather than a broad loyalty/media platform.

The possible success factor relative to Coop is strategic simplicity: discount promise first, digital utility second. The evidence does not show that REMA's app is superior to Coop's; it shows that REMA may need less digital complexity to support its customer promise.

### Lidl Denmark
Lidl's position is international discount challenger. The strongest customer evidence is the 2025 BrancheIndex result reported by Lidl/Ritzau: Lidl is placed highest on value for money and fruit/vegetables, and the release says it is the only chain moving forward in that year's survey. An older Ritzau/ONP source reports 139 Danish stores and a goal above 200; this source is useful for expansion logic but should not be treated as a current 2026 store count.

Lidl Plus is tightly linked to discount behavior: digital customer card, weekly offers, coupons, digital receipts, store finder and Click & Collect. The coupon pages describe personal offers, automatic redemption after scanning the Lidl Plus card and Kupon Plus purchase goals.

The contrast with Coop is again fit. Lidl Plus supports a simple price/value promise. Coop's app is broader and more advanced in loyalty mechanics, but the competitor evidence suggests that app breadth is less important than alignment with a clear customer proposition.

### Dagrofa: MENY, SPAR, Min Købmand and Let-Køb
Dagrofa is not mainly a discount success story. Its evidence points to a portfolio based on food experiences, local merchants and chain identity. Dagrofa reports 2025 revenue of 20.9bn DKK, operating earnings of 529m DKK, profit of 99m DKK and 544 stores. Dagrofa says the transformation from 2018 has increased revenue and operating earnings substantially.

MENY is positioned as "Danmarks MADmarked" with broad assortment, gourmet and basic goods, take-away and specialist staff. Dagrofa reports that MENY became Denmark's strongest grocery brand in Loyalty Group's BrancheIndex 2025, winning 5 of 8 areas: trust, image, product quality, organic and accessibility. The survey involved 4,694 Danish grocery customers.

Digital solutions support the chain concepts. MENY's Google Play page shows 100K+ downloads and describes member prices, food inspiration, recipes, shopping lists and payment-card linkage. SPAR SAMMEN has a 4.6 App Store rating from around 2.3K ratings and provides member prices, recipes and weekly leaflet access. Compared with Coop, Dagrofa's evidence points to sharper chain-level identity rather than one broad digital narrative across chains.

### Nemlig.com
Nemlig.com is the online-first comparator because Coop closed coop.dk in 2023. Nemlig reports 2024/2025 revenue of 2.82bn DKK, 3.3% growth and adjusted EBITDA of 35.3m DKK. It also states that more than four out of five Danish households can receive groceries and meal boxes from Nemlig.

The digital solution is the core business, not a loyalty layer. Google Play shows a 4.6 rating and 100K+ downloads. The app provides groceries, meal boxes, favorites, shopping lists and recipes. Nemlig also reports an organic sales share of 23.8% in 2025, up from 22.8% in 2024.

The evidence is mixed, which is analytically useful. Proff lists 2025 year's result as -28.090m DKK. Nemlig may show that online grocery can be made more viable through scale, logistics and assortment, but it does not show that online grocery is an easy profit pool. This is a direct caution against treating Coop's closed online store as simply a digital capability failure.

## 6. Cross-competitor patterns
- Digital supports a clear core strategy: price at Lidl/REMA, scale and store flow at Salling, food/locality at Dagrofa, delivery convenience at Nemlig.
- Apps are strongest where they are operationally anchored: Scan&Go, coupons, member prices, lists, receipts and delivery ordering.
- Customer-facing digital value is often mundane but important: queue reduction, automatic discounts, reminders, lists and receipts.
- Strong competitors do not necessarily have one common digital model. Discount, premium/local and online-first players use different digital mechanisms.
- The evidence repeatedly points to implementation fit: stores, logistics, chain identity and economics matter more than digital feature breadth.
- Coop's app reach is a real asset in the case context, but competitors show that reach alone does not prove strategic or financial fit.

## 7. Statistics table

| Competitor | Metric | Value | Year | Source |
|---|---:|---:|---:|---|
| Salling Group | Revenue | 83.168bn DKK | 2025 | Salling key figures |
| Salling Group | Profit for year | 1.990bn DKK | 2025 | Salling key figures |
| Salling Group | Netto Denmark stores | 578 | 2025 | Salling key figures |
| REMA 1000 | Revenue | 28.478bn DKK | 2024 | Paqle |
| REMA 1000 | Profit for year | 515.650m DKK | 2024 | Paqle |
| REMA 1000 | Market share estimate | 18.2% | 2025 | Ritzau/NI, Retail Institute; contested |
| REMA 1000 | Danish stores | >420 | 2024/2026 access | REMA responsibility page |
| Lidl | Value-for-money ranking | #1 in BrancheIndex category | 2025 | Lidl/Ritzau |
| Lidl | Stores | 139; target >200 | 2023 | Ritzau/ONP; older source |
| Dagrofa | Revenue | 20.9bn DKK | 2025 | Dagrofa |
| Dagrofa | Operating earnings | 529m DKK | 2025 | Dagrofa |
| Dagrofa | Profit | 99m DKK | 2025 | Dagrofa |
| Dagrofa | Stores | 544 | 2025 | Dagrofa |
| MENY | Stores | 116 | 2025 | Dagrofa/Ritzau |
| SPAR | Stores | >140 | 2026 access | Dagrofa chains page |
| MENY app | Google Play downloads | 100K+ | 2026 access | Google Play |
| SPAR SAMMEN | App Store rating | 4.6 / 5, approx. 2.3K ratings | 2026 access | Apple App Store |
| Nemlig | Revenue | 2.82bn DKK | 2024/2025 | Nemlig/Ritzau |
| Nemlig | Adjusted EBITDA | 35.3m DKK | 2024/2025 | Nemlig/Ritzau |
| Nemlig | Profit for year | -28.090m DKK | 2025 | Proff |
| Nemlig | Delivery coverage | >4 of 5 households | 2025 | Nemlig/Ritzau |
| Nemlig app | Google Play rating/downloads | 4.6 / 5; 100K+ | 2026 access | Google Play |
| Danish e-commerce | Online consumption | 136bn DKK | 2025 | Dansk Industri |
| Danish e-commerce | Monthly online shoppers | 81% | 2025 | Dansk Industri |
| Danish e-commerce | Mobile share of online purchases | 49% | 2025 | Dansk Industri |
| Coop baseline | App users / household reach | approx. 1.8m / 25% | 2026 case context | Local context / Lobyco source |
| Coop baseline | Net loss | 232m DKK | 2025 | Local exam context |

## 8. Theory mapping

**Digital Business Model Framework.** Salling behaves as an omnichannel/physical-retail scale player where digital tools support the chain and store process. REMA and Lidl use digital primarily to reinforce discount value. Dagrofa uses customer knowledge and member pricing to support differentiated chain identities. Nemlig is the clearest online-first controlled-value-chain case.

**Digital Value Creation Framework.** Experiences are improved through Scan&Go, receipts, delivery and app-based lists. Relationships are built through member prices, personal offers, coupons and app-based repeat interaction. Evolution is visible in mobile-first behavior, Lidl Plus, Nemlig's online model and Salling's consolidation of Scan&Go into chain apps.

**Strategic positioning.** Competitors appear to perform different activities or similar activities in clearer ways: REMA and Lidl focus discount, Dagrofa focuses food/locality, Nemlig focuses delivery, and Salling combines scale with chain-level tools. Coop's tension is that digital strength coexists with financial and chain-architecture weakness.

**Implementation.** Evidence is strongest where digital is aligned with stores, payments, logistics or customer adoption. Scan&Go and coupons are implementation-heavy store tools. Nemlig shows the logistics burden of online grocery. Dagrofa shows transformation and chain identity. The implementation lens is weaker for sources that only describe marketing benefits.

## 9. Gaps and uncertainties
- Lidl Denmark official financial figures were not found in this run. The Lidl store-count source is older and secondary.
- REMA financial data came from Paqle rather than a scraped official REMA Denmark annual report.
- The REMA market-share figure is explicitly contested by Salling in the same article that reports it.
- Dagrofa's annual-report PDF did not extract via Crawl4AI; the report uses Dagrofa's official results article for extracted figures.
- App ratings and downloads indicate user adoption/visibility, not business impact.
- Vendor/press sources are promotional and should not be read as neutral proof of strategic success.
- Nemlig's official release and Proff financial table use slightly different profit formulations; the report therefore separates adjusted EBITDA from bottom-line result.

## 10. Source list
See `data/source_register.csv` for the full source register. Raw Crawl4AI markdown files are saved in `raw_sources/`.
"""

(OUT_DIR / "competitor_analysis.md").write_text(report, encoding="utf-8")

summary_md = """# Coop competitor analysis - key takeaways

## 1. Absolute key takeaways
- Stronger competitors do not just have digital tools; their digital tools fit their core business model.
- Salling shows scale plus store-integrated apps: 83.168bn DKK revenue and 1.990bn DKK profit in 2025.
- REMA's success evidence is mostly discount focus and operational strength, not app sophistication.
- Lidl Plus is tightly linked to the discount promise through coupons, member prices and purchase goals.
- Dagrofa/MENY show that customer loyalty can come from clear food and local-store positioning.
- Nemlig is a useful online-first contrast, but its bottom-line result remains negative in Proff's 2025 table.
- Coop's app reach is strong, but competitor evidence suggests digital value depends on operational fit.

## 2. Key numbers

| Competitor | Metric | Value | Year | Source |
|---|---|---:|---:|---|
| Salling Group | Revenue / profit | 83.168bn / 1.990bn DKK | 2025 | Salling |
| REMA 1000 | Revenue / profit | 28.478bn / 515.650m DKK | 2024 | Paqle |
| Dagrofa | Revenue / operating earnings | 20.9bn / 529m DKK | 2025 | Dagrofa |
| Nemlig | Revenue / adjusted EBITDA | 2.82bn / 35.3m DKK | 2024/25 | Nemlig |
| Nemlig | Profit for year | -28.090m DKK | 2025 | Proff |
| Danish e-commerce | Mobile share of online purchases | 49% | 2025 | DI |

## 3. What competitors seem to do differently

| Competitor | Digital/customer-facing solution | Apparent success factor | Contrast with Coop |
|---|---|---|---|
| Salling | Chain apps + Scan&Go | Scale and store integration | Strong digital utility inside profitable operations |
| REMA | Planning app + Scan Selv | Clear discount promise | Less broad digital ambition, clearer model |
| Lidl | Lidl Plus coupons/goals | Price/value reinforcement | App directly supports discount economics |
| Dagrofa | MENY/SPAR member apps | Chain identity and loyalty | Sharper chain-specific positioning |
| Nemlig | Online grocery app/webshop | Purpose-built online logistics | Coop closed online grocery in 2023 |

## 4. Exam-ready conclusion
Competitors appear to succeed when their digital solutions clearly support their core business model, customer promise and operational setup. Salling uses digital to make scaled physical retail easier. REMA and Lidl use apps to reinforce discount value. Dagrofa links member apps to food/local identity. Nemlig shows that online grocery requires a dedicated logistics model and still has difficult economics. The main insight is not that Coop should copy a competitor, but that digital reach only creates strategic value when it fits the store, chain and economic model.
"""
(OUT_DIR / "key_takeaways_summary.md").write_text(summary_md, encoding="utf-8")


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def make_pdf(path: Path) -> None:
    pages = [
        [
            ("Coop competitor analysis - key takeaways", 16),
            ("1. Absolute key takeaways", 12),
            ("- Digital tools matter when they fit the operating model, not as standalone digital maturity.", 10),
            ("- Salling: 83.168bn DKK revenue and 1.990bn DKK profit in 2025; app features support stores.", 10),
            ("- REMA: focused discount model; Paqle lists 28.478bn DKK revenue and 515.650m DKK profit in 2024.", 10),
            ("- Lidl: Lidl Plus reinforces price/value through coupons, digital card, receipts and purchase goals.", 10),
            ("- Dagrofa/MENY: strong food/local identity; Dagrofa reports 20.9bn DKK revenue in 2025.", 10),
            ("- Nemlig: online-first model improved revenue/EBITDA, but Proff still lists -28.090m DKK result.", 10),
            ("2. Key numbers", 12),
            ("Salling: 83.168bn DKK revenue; 1.990bn DKK profit (2025, Salling).", 10),
            ("REMA: 28.478bn DKK revenue; 515.650m DKK profit (2024, Paqle).", 10),
            ("Dagrofa: 20.9bn DKK revenue; 529m DKK operating earnings; 544 stores (2025, Dagrofa).", 10),
            ("Nemlig: 2.82bn DKK revenue; 35.3m DKK adjusted EBITDA; -28.090m DKK result (2024/25).", 10),
            ("DI: 136bn DKK online consumption; 81% monthly online shoppers; 49% mobile purchases (2025).", 10),
        ],
        [
            ("3. What competitors seem to do differently", 12),
            ("Salling: chain apps plus Scan&Go support scaled physical retail; contrast is profitability plus utility.", 10),
            ("REMA: planning app and Scan Selv support a simple discount promise; digital scope is narrower than Coop's.", 10),
            ("Lidl: Lidl Plus turns loyalty into coupons, member prices and purchase goals tied to value-for-money.", 10),
            ("Dagrofa: MENY/SPAR apps support chain identity, member prices, food inspiration and local loyalty.", 10),
            ("Nemlig: app/webshop is the store; delivery/logistics are core, not add-ons.", 10),
            ("4. Exam-ready conclusion", 12),
            ("Competitors appear to succeed when digital solutions clearly support the core business model, customer promise", 10),
            ("and operational setup. Salling uses digital to make scaled physical retail easier. REMA and Lidl use apps", 10),
            ("to reinforce discount value. Dagrofa links apps to food/local identity. Nemlig shows online grocery requires", 10),
            ("dedicated logistics and still has difficult economics. The main insight is evidence of fit, not a recommendation.", 10),
        ],
    ]
    objects: list[str] = []
    contents = []
    for page in pages:
        y = 800
        lines = ["BT", "/F1 10 Tf"]
        for text, size in page:
            if size >= 12:
                y -= 22
                wrapped = wrap(text, width=78)
            else:
                y -= 16
                wrapped = wrap(text, width=92)
            for idx, segment in enumerate(wrapped):
                if idx:
                    y -= 13
                lines.append(f"/F1 {size} Tf 50 {y} Td ({pdf_escape(segment)}) Tj 0 0 Td")
            if size >= 12:
                y -= 4
        lines.append("ET")
        contents.append("\n".join(lines))

    # Object layout: catalog, pages, font, then page/content pairs.
    objects.append("<< /Type /Catalog /Pages 2 0 R >>")
    kids = []
    for i in range(len(pages)):
        page_obj = 4 + i * 2
        kids.append(f"{page_obj} 0 R")
    objects.append(f"<< /Type /Pages /Kids [{' '.join(kids)}] /Count {len(pages)} >>")
    objects.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    for i, content in enumerate(contents):
        page_obj = 4 + i * 2
        content_obj = page_obj + 1
        objects.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 3 0 R >> >> /Contents {content_obj} 0 R >>")
        objects.append(f"<< /Length {len(content.encode('latin-1', errors='replace'))} >>\nstream\n{content}\nendstream")

    pdf = ["%PDF-1.4\n"]
    offsets = [0]
    for idx, obj in enumerate(objects, start=1):
        offsets.append(sum(len(part.encode("latin-1", errors="replace")) for part in pdf))
        pdf.append(f"{idx} 0 obj\n{obj}\nendobj\n")
    xref = sum(len(part.encode("latin-1", errors="replace")) for part in pdf)
    pdf.append(f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.append(f"{offset:010d} 00000 n \n")
    pdf.append(f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n")
    path.write_bytes("".join(pdf).encode("latin-1", errors="replace"))


make_pdf(OUT_DIR / "key_takeaways_summary.pdf")

readme = f"""# Web scraping run: Coop competitor analysis

Run started: 2026-05-03 16:19 Europe/Copenhagen.

Purpose: gather, structure and analyze public evidence about selected Coop competitors for the IT-strategy exam case. This is evidence gathering and competitor analysis only; it does not recommend what Coop should do.

## What was scraped
Crawl4AI was used for public pages from Salling Group, Netto, Bilka, føtex, REMA 1000, Lidl Denmark, Dagrofa, MENY/SPAR app pages, Nemlig, Loyalty Group and Dansk Industri. The source list is in `logs/source_urls.tsv`.

## Files created
- `raw_sources/`: one Markdown file per scraped source, with source URL and access metadata.
- `data/competitor_findings.csv`: structured competitor findings.
- `data/source_register.csv`: source register with reliability/source-criticism notes.
- `final_outputs/competitor_analysis.md`: full evidence report.
- `final_outputs/key_takeaways_summary.md`: Markdown summary fallback.
- `final_outputs/key_takeaways_summary.pdf`: compact two-page PDF summary.
- `logs/crawl.log`: crawl execution log.

## Limitations
- The Dagrofa annual-report PDF URL was crawled, but Crawl4AI extracted only metadata. Dagrofa's official 2025 results article was used for extracted figures.
- Some sources are official press releases or app pages and are therefore marketing-heavy.
- REMA market-share data is reported from Retail Institute via Ritzau/NI and is disputed by Salling in the same article.
- Lidl Denmark official current financial figures were not found during this run.
"""
(RUN_DIR / "README.md").write_text(readme, encoding="utf-8")

index_path = Path("reports/webscraping_runs/index.md")
if index_path.exists():
    existing = index_path.read_text(encoding="utf-8")
else:
    existing = "# Web scraping runs\n\n"
entry = "- 2026-05-03_1619_coop_competitor_analysis: Coop competitor evidence scrape for IT-strategy exam; outputs include raw sources, CSV findings, Markdown report and PDF summary.\n"
if entry not in existing:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(existing.rstrip() + "\n" + entry, encoding="utf-8")

print(f"Wrote outputs to {RUN_DIR}")
