# Source Verification Packet

## 1. Formål

Dette dokumentet er en kompakt kildepakke for de viktigste A-prioriterte claimene som må behandles før senere syntese. Målet er ikke å skrive finalrapport, velge caseperson, velge teori eller gi anbefalinger, men å gjøre det tydelig hvilke påstander som er trygge, hvilke som er leverandørclaims, og hvilke som fortsatt bare er inferenser eller strategiske alternativer.

## 2. Hvordan Pakken Skal Brukes

- Bruk pakken som kilde- og formuleringstøtte når Opus senere skal lage syntese.
- Bruk sterke claims bare når de kan spores til årsrapport, offisiell Coop-kilde, offisiell konkurrentkilde eller annen tydelig kilde.
- Behandle Lobyco, Playable, Shortcut, Lidl/Ritzau, Dagrofa-pressemeldinger og Loyalty Group som nyttige, men delvis interesserte eller metodebegrensede kilder.
- Ikke bruk app-rekkevidde, app engagement, gamification eller retail media som bevis på lønnsomhet uten separat økonomisk evidens.
- Skill alltid mellom `Fact`, `Claim`, `Marketing claim`, `Assumption` og `Inference`.

## 3. A-prioritert Verifikasjonstabell

| Claim ID | Claim | Prioritet | Eksakt kilde hvis funnet | Lokal fil/URL hvis tilgjengelig | Kildetype | Claim label | Reliability | Trygg formulering som kan brukes | Formulering som må unngås | Hva som fortsatt må sjekkes | Strategiske retninger påvirket |
|---|---|---:|---|---|---|---|---|---|---|---|---|
| SVP-A01 | Coop 2025-finans: Coop Danmark A/S rapporterer 32,565 mrd. DKK i nettoomsetning, 313 mill. DKK EBITDA før gevinst ved eiendomssalg, og EBIT på -215 mill. DKK. Inkludert brugsforeninger oppgis 44,756 mrd. DKK. | A | Coop Danmark A/S årsrapport 2025; Coop-pressemelding "Coop forbedrer driftsindtjeningen med 350 millioner kr." | `05_evidence/coop-danmark-aarsrapport-2025.pdf`; `../../../reports/webscraping_runs/2026-05-03_1813_coop_business_model_analysis/raw_sources/local_pdf_coop_danmark_aarsrapport_2025_pdf.md`; https://coop.dk/kontakt/pressekontakt/pressemeddelelser/coop-forbedrer-driftsindtjeningen-med-350-millioner-kr/ | Årsrapport og offisiell pressemelding | Fact | High | "Coop rapporterer 32,565 mrd. DKK i 2025-nettoomsetning og et EBIT-underskudd på 215 mill. DKK, samtidig som EBITDA før eiendomsgevinster var positiv." | "Coop tapte 215 mill. DKK på bunnlinjen" eller "appen forklarer EBIT-tapet." | Eksakte regnskapsbegreper og eventuell net loss må dobbeltsjekkes i årsrapporten før finalrapport. | Thor/investeringsstyring; Martin/hybrid governance; alle retninger som vurderer investeringsrom. |
| SVP-A02 | 232 mill. DKK loss og -215 mill. DKK EBIT må ikke blandes sammen; de ser ut til å være ulike regnskapsmål eller kilder. | A | Eksamenstekst/prosjektkontekst for 232 mill. DKK; Coop 2025-årsrapport/pressemelding for -215 mill. DKK EBIT. | `05_evidence/key_numbers.md`; `05_evidence/evidence_verification_plan.md`; Coop-årsrapport/pressemelding som over. | Caseoppgave/prosjektkontekst + årsrapport | Claim / Fact-mismatch | Medium | "Prosjektet opererer med både et 232 mill. DKK loss-claim og et dokumentert EBIT-underskudd på 215 mill. DKK; disse må holdes atskilt til regnskapsmålet er verifisert." | "Coops EBIT var -232 mill. DKK" eller "232 mill. DKK og -215 mill. DKK er samme tall." | Original eksamenstekst og regnskapspost for 232 mill. DKK må verifiseres. | Thor/investeringsstyring; alle finansielle argumenter. |
| SVP-A03 | Coop.dk MAD ble lukket i 2023; kilder peker på svak eller manglende lønnsomhet. Coop.dk-webshop ble senere lukket 31. januar 2025 for å fokusere på fysisk butikk-kjerne. | A | Coop.dk MAD-side; Coop kundeservice om Coop.dk-lukking; Ritzau/NI om hjemmelevering og tapsdrift; casekontekst. | https://coop.dk/mad; https://kundeservice.shopping.coop.dk/hc/da/articles/21459967795602-Hvorfor-og-hvorn%C3%A5r-er-Coop-dk-lukket; https://ni.dk/ni-news/id/35f0f2a6-7ddc-4fee-bf00-4e127bf759ec/Coops-hjemmelevering-lukker | Offisiell Coop-side, kundeservice, bransjenyhet | Fact + Claim | High for closure; Medium for årsak | "Coop.dk MAD ble lukket i 2023, og Coop.dk-webshop ble lukket 31. januar 2025. Kildene indikerer at økonomi og fysisk butikkfokus var sentrale forklaringer." | "Coop mislyktes med all digitalisering" eller "online grocery er alltid ulønnsomt." | Eksakt ordlyd i eksamenscase og Ritzau/NI bør sjekkes før sterk årsaksformulering. | Thor/investeringsstyring; Martin/hybrid governance; Digital Business Model; Nemlig-kontrast. |
| SVP-A04 | Coop er fortsatt primært en fysisk butikkbasert dagligvareaktør. | A | Coop Danmark A/S årsrapport 2025; Coop kundeservice om fysisk butikkfokus; Coop business model scraping. | `05_evidence/coop-danmark-aarsrapport-2025.pdf`; `../../../reports/webscraping_runs/2026-05-03_1813_coop_business_model_analysis/final_outputs/coop_business_model_analysis.md`; Coop kundeservice-URL over. | Årsrapport og offisiell Coop-kilde | Fact / Inference | High | "Coops inntekts- og kanalgrunnlag er primært fysisk butikkhandel, med 536 Coop Danmark-butikker og 900 butikker inkludert brugsforeninger i 2025." | "Coop er en digital plattformvirksomhet" eller "appen er hovedkanalen." | Omfanget av app- eller Lobyco-inntekter mangler og må ikke antas. | Thor/investeringsstyring; Martin/hybrid; DVC + Digital Business Model. |
| SVP-A05 | Coop App har ifølge Lobyco mer enn 1,8 mill. brukere og omtrent 25 prosent household reach; Lobyco oppgir også ca. 880 000 MAU. | A | Lobyco case "Helping 25% of Danish households shop smarter"; Lobyco insight "Making Multi-Banner Loyalty Simple". | https://www.lobyco.com/case-studies/coop; https://www.lobyco.com/insights/making-multi-banner-loyalty-simple; `../../../reports/webscraping_runs/2026-05-03_1813_coop_business_model_analysis/data/coop_business_model_findings.csv` | Leverandør-/marketingcase | Marketing claim | Medium for tall; Low/Medium for strategisk tolkning | "Lobyco oppgir at Coop App har mer enn 1,8 mill. brukere og når omtrent 25 prosent av danske husholdninger; dette viser reach, ikke lønnsomhet." | "Coop App er lønnsom" eller "1,8 mill. brukere beviser konkurransefortrinn." | Uavhengig bekreftelse, tidsstempel, definisjon av bruker og MAU må sjekkes. | Martin/hybrid governance; Lobyco-kapasitet; Thor/investeringsstyring. |
| SVP-A06 | Lobyco hevder at appbrukere handler 50 prosent oftere eller er mer verdifulle; claimet kan være påvirket av selection bias. | A | Lobyco case om Coop. | https://www.lobyco.com/case-studies/coop; `05_evidence/claim_reliability_matrix.md` | Leverandør-/marketingcase | Marketing claim | Low/Medium | "Lobyco hevder at appbrukere handler oftere; claimet bør behandles som korrelasjon og ikke som dokumentasjon på kausal lønnsomhet." | "Appbrukere er mer lønnsomme" eller "appen får kunder til å handle 50 prosent mer." | Må verifiseres med Coop-interne KPI-er: margin, kurv, frekvens før/etter, kontrollgruppe og kostnader. | Martin/hybrid governance; Thor/investeringsstyring; app-styrking. |
| SVP-A07 | Lobyco kan forstås som spin-out/subsidiary/digital capability/OEM-logikk, men eksakt økonomisk rolle og eierskap/verdi er ikke fullstendig verifisert. | A | Casekontekst; Lobyco hjemmeside/case; Shortcut case. | https://www.lobyco.com/; https://www.lobyco.com/case-studies/coop; https://www.shortcut.io/cases/coop-denmark-app; `05_evidence/coop_business_model_evidence.md` | Case, leverandørkilder og utviklercase | Claim | Medium | "Lobyco fremstår i kildene som en mulig digital lojalitetskapabilitet og OEM-/plattformlogikk, men offentlig evidens kvantifiserer ikke verdien for Coop." | "Lobyco beviser at Coop har et varig konkurransefortrinn" eller "Lobyco bør selges." | Eierskap, inntekter, kostnader, eksterne kunder, binding til Coop App og strategisk kontroll må verifiseres. | Martin/hybrid governance; Thor/investeringsstyring; selge/beholde/govern Lobyco. |
| SVP-A08 | Retail media og supplier-funded campaigns fremstår som mulig app-verdi: leverandører kan finansiere kampanjer/spill/premier som aktiveres i butikk. | A | Playable Coop case; Lobyco-materiale; Coop Trading-kilder. | https://playable.com/cases/coop/; https://www.lobyco.com/; https://www.cooptrading.com/who-we-are/; `../../../reports/webscraping_runs/2026-05-03_1813_coop_business_model_analysis/final_outputs/coop_business_model_analysis.md` | Leverandørmarketing + offisiell partner-/sourcingkilde | Marketing claim / Inference | Medium for mekanisme; Low for økonomisk verdi | "Kildene indikerer en mulig retail-media- og supplier-funded campaign-logikk rundt Coop App, men økonomisk effekt er ikke dokumentert i offentlig materiale." | "Retail media finansierer appen" eller "leverandørkampanjer gjør appen lønnsom." | Faktisk revenue, margin, kampanjekostnader, supplier funding og nettoeffekt må verifiseres. | Martin/hybrid governance; Thor/investeringsstyring; Lobyco-kapasitet. |
| SVP-A09 | Playable rapporterer gamification-engagement, bl.a. unike spillere, spillrunder, premier og kurv-claim for premievinnere/redeemers. | A | Playable case "How Coop fueled loyalty and retail media". | https://playable.com/cases/coop/; `../../../reports/webscraping_runs/2026-05-03_1813_coop_business_model_analysis/data/coop_business_model_findings.csv` | Leverandør-/marketingcase | Marketing claim | Medium for rapporterte kampanjemål; Low for strategisk/økonomisk effekt | "Playable rapporterer høyt engagement i Coop-spill og in-store redemption, men dette er leverandørdata og ikke uavhengig effektmåling." | "Gamification øker Coops lønnsomhet" eller "spillende kunder er mer profitable." | Metode, kontrollgruppe, kampanjekostnader, margin og om tallene gjelder hele Coop eller utvalgte kampanjer må sjekkes. | Martin/hybrid; retail media-logikk; app-styrking. |
| SVP-A10 | Shortcut beskriver historikk for Coop App, inkludert OEM-/plattformutvikling og eldre download-/daily-user-tall. | A | Shortcut case "Digital transformation for the modern retail chain". | https://www.shortcut.io/cases/coop-denmark-app; `05_evidence/coop_business_model_evidence.md` | Leverandør-/utviklercase | Marketing claim / Claim | Medium for historikk; Low for strategisk evaluering | "Shortcut beskriver Coop App som en løsning som ble videreutviklet mot OEM-/plattformbruk; dette kan brukes som historikk, ikke som dokumentasjon på nåværende økonomisk verdi." | "Shortcut beviser at appstrategien er vellykket" eller "download-tall er nåværende aktive brukere." | Dato, tallgrunnlag, nåværende relevans og sammenheng med Lobyco må verifiseres. | Martin/hybrid; Lobyco-kapasitet; Thor/investeringsstyring. |
| SVP-A11 | Google Play-kilden for Coop App feilet i scraping og skal ikke brukes til nøkkelpåstander. | A | Source criticism og scraping-run: Google Play returnerte "requested URL was not found". | `05_evidence/source_criticism.md`; `../../../reports/webscraping_runs/2026-05-03_1813_coop_business_model_analysis/data/source_register.csv` | Scraping-caveat | Fact | High | "Google Play-scrapet for Coop App var ikke egnet som kilde i denne runden." | "Google Play viser at Coop App har..." uten ny verifisering. | Re-scrape eller manuell kontroll dersom app-store-tall skal brukes. | Alle app-rekkeviddeargumenter. |
| SVP-A12 | 365discount er dokumentert som Coops lavprisformat, men evidens for egen app-/go-deep-effekt mangler. | A | 365discount-side; Coop chain pages; competitor evidence/Loyalty Group som sekundær kontekst. | https://365discount.coop.dk/om-365discount/job/karriere/; `06_analysis/strategic_situation_analysis.md`; `05_evidence/competitor_evidence.md` | Offisiell kjedeside + sekundær konkurranseanalyse | Fact + Inference | High for lavprisposisjon; Low for appbehov | "365discount presenteres av Coop som et lavprisformat; dette kan støtte en analyse av kjedespesifikk digital fit, men ikke alene bevise behov for egen app." | "365discount bør ha egen app" eller "go-deep er dokumentert som beste løsning." | Kjede-KPI-er, kundesegment, appbruk for 365discount, konkurranse mot Lidl/REMA og kostnad ved differensiert app må verifiseres. | Michael/go-deep; DVC + Porter/positioning; selektiv forenkling. |
| SVP-A13 | Salling har sterk skala/profit og kjedespesifikke digitale løsninger med Scan&Go/store integration. | A | Salling Group key figures; Netto+, Bilka Plus og føtex Scan&Go-supportsider. | https://sallinggroup.com/en/stores/key-figures; https://netto.dk/netto-plus/; https://www.bilka.dk/scango/; https://support.foetex.dk/hc/da/articles/28279829727633-f%C3%B8tex-Scan-Go; `../../../reports/webscraping_runs/2026-05-03_1619_coop_competitor_analysis/final_outputs/competitor_analysis.md` | Offisielle konkurrent- og supportsider | Fact / Claim | High for finans/funksjoner; Medium for strategisk tolkning | "Salling rapporterer 83,168 mrd. DKK i revenue og 1,990 mrd. DKK i profit for 2025; kildene viser også kjedespesifikke app- og Scan&Go-funksjoner." | "Salling vinner fordi de har apper" eller "Scan&Go forklarer profitten." | Om appene bidrar økonomisk må ikke antas; eventuell app-KPI mangler. | Michael/go-deep; konkurrent-fit; Porter/positioning. |
| SVP-A14 | REMA har sekundært dokumentert revenue/profit fra Paqle, offisiell Scan Selv-funksjon, og et markedsandelsclaim som er bestridt av Salling. | A | Paqle; REMA Scan Selv; Ritzau/NI om Retail Institute-markedsandel og Salling-kontestering. | https://www.paqle.dk/p/rema-1000/227324/finance; https://rema1000.dk/information/scan-selv; https://ni.dk/ni-news/id/56662f68-b455-489a-bebe-706b19ceda1c/Analyse-giver-Rema-1000-discounttronen---Nettos-ejer-afviser-blankt | Sekundær finansdatabase, offisiell funksjonsside, bransjenyhet | Fact / Claim | Medium | "REMA-kildene indikerer sterk discountdrift og en smal Scan Selv-utility, men markedsandelsclaimet er eksplisitt bestridt." | "REMA er markedsleder" uten caveat eller "REMA vinner på app." | Offisiell årsrapport/konsernstruktur og oppdatert markedsandel må sjekkes. | Michael/go-deep; DVC + Porter; selektiv forenkling. |
| SVP-A15 | Lidl Plus er tydelig koblet til kuponger, medlemspriser og kjøpsmål; value-for-money-claim kommer fra promotert Ritzau/Lidl-kilde. | A | Lidl Plus-sider; Lidl/Ritzau value-for-money-pressemelding. | https://www.lidl.dk/c/lidl-plus/s10013731; https://www.lidl.dk/c/lidl-plus-kuponer/s10014639; https://www.lidl.dk/c/lidl-plus-kupon-plus/s10014640; https://via.ritzau.dk/pressemeddelelse/14578254/kunderne-har-talt-lidl-giver-mest-vaerdi-for-pengene-og-leverer-bedst-pa-frugt-og-gront | Offisiell app-/kampanjeside + promotert pressemelding | Claim / Marketing claim | Medium | "Lidl Plus beskrives som en app tett koblet til kuponger, medlemspriser og kjøpsmål; value-for-money-claimet bør behandles som surveybasert, promotert kommunikasjon." | "Lidl beviser at discount-apper skaper profit" eller "Lidl er objektivt best på verdi." | Metode og original surveydata bak BrancheIndex/value-for-money må sjekkes. | Michael/go-deep; 365discount; Porter/positioning. |
| SVP-A16 | Dagrofa/MENY-kilder viser revenue/earnings/profit og tydelig chain identity/loyalty-claim, men MENY/BrancheIndex er surveybasert og ikke fullstendig transparent. | A | Dagrofa 2025-resultatside; Dagrofa kjedeside; MENY/Loyalty Group BrancheIndex-pressemelding; Loyalty Group BrancheIndex-side. | https://www.dagrofa.dk/artikel/dagrofa-loefter-driftsresultatet-og-omsaetningen-naar-rekordhoeje-209-mia-kr/; https://www.dagrofa.dk/kaeder/; https://www.dagrofa.dk/artikel/meny-kaares-som-danmarks-staerkeste-dagligvarebrand/; https://loyaltygroup.dk/brancheanalyser/brancheindex/brancheindex-dagligvarer/ | Offisiell pressemelding, kjedeside, indeks/survey | Fact / Claim | Medium/High for Dagrofa-tall; Medium for loyalty-claim | "Dagrofa rapporterer 20,9 mrd. DKK i omsetning og 529 mill. DKK i driftsresultat; MENY omtales som sterkt dagligvarebrand i BrancheIndex, men surveygrunnlaget må behandles med kildekritikk." | "MENY beviser at loyalty-app er best" eller "BrancheIndex måler økonomisk effekt." | Original indeksmetode, full rangering og uavhengig årsrapport bør sjekkes. | Martin/hybrid; chain-specific digital; konkurrent-fit. |
| SVP-A17 | Nemlig viser online grocery som relevant kontrast: revenue og justert EBITDA er positive i pressemelding, mens Proff viser negativt årsresultat. | A | Nemlig/Ritzau resultatmelding; Proff regnskap. | https://via.ritzau.dk/pressemeddelelse/14710924/nemlig-fortsaetter-vaeksten-og-halverer-underskud-i-nyt-regnskabsar; https://www.proff.dk/regnskab/nemlig.com-as/odense-s/n%C3%A6rings-og-nydelsesmidler/GXIFMDI116S | Offisiell/promotert pressemelding + sekundær finansdatabase | Fact / Claim | Medium/High | "Nemlig rapporterer revenue og positiv justert EBITDA, mens Proff viser negativt årsresultat; dette indikerer at online grocery fortsatt kan ha krevende økonomi." | "Nemlig viser at online dagligvare er lønnsomt" eller "Coop burde kopiere Nemlig." | Regnskapsdefinisjoner, periode, konsernstruktur og sammenlignbarhet må sjekkes. | Thor/investeringsstyring; Digital Business Model; coop.dk-lukking. |
| SVP-A18 | DI e-commerce-claim: dansk e-commerce og mobilkjøp er stort, men dette er generell e-commerce og ikke bevis på dagligvare- eller app-lønnsomhet. | A | Dansk Industri e-commerce tracker 2025. | https://www.danskindustri.dk/vi-radgiver-dig/ecommerce/di-e-commerce-analyser/analyser/2026/danskernes-arlige-e-commerce-tracker-2025/; `../../../reports/webscraping_runs/2026-05-03_1619_coop_competitor_analysis/data/competitor_findings.csv` | Bransjeanalyse | Fact / Claim | Medium/High for generell e-commerce; Low for grocery-inferens | "DI-tall kan brukes som generell kontekst for mobil og netthandel, men ikke som dokumentasjon på Coop App-profitabilitet." | "Fordi mobilhandel øker, bør Coop investere mer i appen" eller "DI beviser grocery-app-behov." | Om tallene gjelder dagligvarer, apphandel og Coops segmenter må verifiseres separat. | Digital Business Model; Martin/hybrid; generell digital kontekst. |
| SVP-A19 | Konkurrent-fit-inferens: digitale verktøy ser ut til å fungere best når de passer forretningsmodell, kundeløfte og drift. | A | Lokal competitor analysis-syntese basert på Salling, REMA, Lidl, Dagrofa og Nemlig-kilder. | `../../../reports/webscraping_runs/2026-05-03_1619_coop_competitor_analysis/final_outputs/competitor_analysis.md`; `05_evidence/competitor_evidence.md` | Sekundær syntese/inferens | Inference | Medium | "Konkurrentevidensen antyder at digital verdi er sterkest når digitale løsninger passer kjerneposisjon og driftsmodell." | "Konkurrentene vinner fordi de har apper" eller "digital fit er bevist kausalt." | Må underbygges med konkrete eksempler og formuleres som analytisk inferens, ikke empirisk faktum. | Michael/go-deep; Martin/hybrid; DVC + Porter; Digital Business Model. |
| SVP-A20 | Lobyco selge/beholde/govern er et strategisk option-sett, ikke en evidensbasert konklusjon ennå. | A | `04_option_banks/decision_preparation.md`; `05_evidence/evidence_verification_plan.md`; Lobyco/Coop/Shortcut-kilder. | `04_option_banks/decision_preparation.md`; `05_evidence/evidence_verification_plan.md`; https://www.lobyco.com/ | Strategisk arbeidsnotat + leverandørkilder | Assumption / Inference | Unknown/Low som konklusjon | "Lobyco bør foreløpig behandles som et åpent governance- og investeringsspørsmål, ikke som et avgjort salg/behold-valg." | "Coop bør selge Lobyco" eller "Coop bør beholde Lobyco" som evidensbasert konklusjon. | Eierskap, økonomisk bidrag, kontrollbehov, ekstern markedsverdi, kostnader og strategisk avhengighet må verifiseres. | Thor/investeringsstyring; Martin/hybrid governance; selge/afhænde Lobyco; Lobyco som kontrollert kapasitet. |

## 4. Trygge Formuleringer

- "Coop rapporterer et EBIT-underskudd på 215 mill. DKK for 2025, samtidig som EBITDA før eiendomsgevinster var positiv."
- "Coop er fortsatt primært en fysisk butikkbasert dagligvareaktør målt på inntekter, butikker og kanalstruktur."
- "Coop.dk MAD ble lukket i 2023, og Coop.dk-webshop ble lukket 31. januar 2025."
- "Lobyco oppgir at Coop App har mer enn 1,8 mill. brukere og ca. 25 prosent household reach; dette er reach-data, ikke lønnsomhetsbevis."
- "Lobyco hevder at appbrukere handler oftere, men claimet bør behandles som leverandørclaim og mulig korrelasjon."
- "Playable rapporterer engagement- og redemption-tall for Coop-spill, men kilden er en leverandørcase."
- "Salling, REMA, Lidl, Dagrofa og Nemlig indikerer ulike digitale fit-logikker, men konkurrentdataene beviser ikke at apper alene skaper lønnsomhet."
- "Nemlig er en relevant online grocery-kontrast, men kildene viser også at justert EBITDA og bunnlinjeresultat må holdes atskilt."
- "Lobyco bør foreløpig analyseres som et åpent governance- og kapabilitetsspørsmål."

## 5. Utrygge Formuleringer

- "Coop App er lønnsom."
- "Lobyco beviser at Coop har et konkurransefortrinn."
- "Appbrukere er mer profitable."
- "Appen øker handlefrekvensen med 50 prosent."
- "Retail media finansierer appinvesteringen."
- "Gamification øker Coops lønnsomhet."
- "Coop bør selge Lobyco."
- "Coop bør beholde Lobyco."
- "365discount bør ha egen app."
- "Konkurrentene vinner fordi de har apper."
- "Salling, REMA eller Lidl beviser at Coop må gå dypt med kjedeapper."
- "DI e-commerce-tall viser at Coop App bør styrkes."

## 6. Retningsavhengighet

### Martin Hasgard Olesen + hybrid governance

**Claims retningen avhenger av**

- Coop App-rekkevidde kan brukes som faktisk digital reach, men bare med Lobyco-bias.
- Lobyco kan forstås som mulig digital kapabilitet/OEM-logikk.
- Appen har flere verdilogikker: lojalitet, butikkstøtte, retail media, personalisering og kjedeportefølje.
- Konkurrent-fit-inferensen antyder at appen bør styres etter chain/business-model fit, ikke bare total reach.

**Svakeste evidenspunkter**

- Appbruker-value/frequency er leverandørclaim.
- Retail media- og Playable-effekt er marketingkilder uten offentlig nettoøkonomi.
- Lobyco-verdi, kostnad og eierskap er ikke tilstrekkelig verifisert.

**Hva må verifiseres**

- Coop-interne app-KPI-er: aktive brukere, margin, kurv, frekvens, retention, kostnad og kampanjeinntekter.
- Lobyco-økonomi og governance: eierskap, ekstern omsetning, strategisk kontroll, avhengighet til Coop App.
- Hvor mye appfunksjonalitet som faktisk varierer eller kan varieres mellom kjedene.

### Michael Tilsted + 365discount go-deep

**Claims retningen avhenger av**

- 365discount er tydelig lavprisformat.
- Lidl Plus og REMA Scan Selv viser at discount-konkurrenter bruker smalere, mer pris-/utility-orienterte digitale løsninger.
- Salling/Netto viser kjedespesifikk app- og Scan&Go-logikk.
- Konkurrent-fit-inferensen støtter analyse av kjedetilpasset digital løsning.

**Svakeste evidenspunkter**

- Det finnes foreløpig ikke sterk evidens for at 365discount-kunder trenger eller verdsetter en egen app.
- Det finnes ikke dokumentert 365discount-spesifikk appøkonomi, kundedata eller marginlogikk.
- Lidl/REMA-data viser funksjoner og posisjon, ikke kausal app-effekt.

**Hva må verifiseres**

- 365discounts kundesegment, appbruk, konkurranseflate og nøkkel-KPI-er.
- Om Coop App i dag oppleves som for bred eller lite discount-fit for 365discount.
- Kostnad og governance-konsekvens av egen app, egen app-modul eller forenklet discount-modus.

### Thor Skov Jørgensen + investment governance

**Claims retningen avhenger av**

- Coop har økonomisk press og fortsatt negativ EBIT i 2025.
- Fysisk butikkhandel er dokumentert kjerne.
- Coop.dk MAD og Coop.dk-webshop-lukking viser at digital investering må vurderes mot økonomisk fit.
- Lobyco/app har reach, men ikke dokumentert offentlig lønnsomhet.

**Svakeste evidenspunkter**

- Lobyco-verdi, kostnader og avhendingsmulighet er ukjent.
- App-profitabilitet og retail media-inntekter er ikke verifisert.
- 232 mill. DKK loss og -215 mill. DKK EBIT må holdes regnskapsmessig atskilt.

**Hva må verifiseres**

- Offisielle finansielle tall og regnskapsmål.
- App- og Lobyco-kostnader, capex/opex, inntekter og governance.
- Hvilke investeringer som er nødvendige for butikk-kjernen, og hvilke som er opsjonelle eller kan forenkles.

## 7. Klar For Opus?

**Sterkt nok til syntese**

- Coop 2025-finans kan brukes, med presise regnskapsbegreper og uten å blande EBIT/net loss.
- Coop som fysisk butikkbasert kjerne kan brukes.
- Coop.dk MAD-lukking i 2023 og Coop.dk-webshop-lukking i 2025 kan brukes som indikasjon på selektiv digital tilbaketrekning.
- Salling, REMA, Lidl, Dagrofa og Nemlig kan brukes som konkurrentkontekst, så lenge funksjons- og finansclaims holdes adskilt fra kausale apppåstander.

**Må behandles som usikkert**

- Coop App-rekkevidde og Lobyco-tall er nyttige, men hovedsakelig leverandørrapporterte.
- Appbruker-frequency/value, Playable-effekt og retail media-verdi er ikke uavhengig dokumentert.
- Lobyco som salgsobjekt, strategisk plattform eller kontrollert kapabilitet er foreløpig et åpent strategisk spørsmål.
- Konkurrent-fit er en analytisk inferens, ikke en direkte observert kausalitet.

**Bør ikke bære hovedargumentet alene**

- "App users shop more often / are more valuable."
- "1,8 mill. brukere / 25 prosent household reach."
- Playable gamification- og kurvclaims.
- Shortcut download-/daily-user-claims.
- Google Play-data fra denne scraping-runden.
- REMA markedsandel uten contestation-caveat.
- Lidl value-for-money eller MENY BrancheIndex som om de var økonomisk effekt.
- Alle påstander om at Lobyco bør selges, beholdes eller styres på én bestemt måte uten mer økonomisk/governance-evidens.
