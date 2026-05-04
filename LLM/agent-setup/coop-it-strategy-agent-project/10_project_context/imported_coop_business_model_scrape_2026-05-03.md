# Importert Coop business model scrape - 2026-05-03

## Source folder

Importert fra:

`/Users/marcusgrude-grodem/Documents/GitHub/IT-Strategi/reports/webscraping_runs/2026-05-03_1813_coop_business_model_analysis`

## Scraping-filer brukt

| Fil | Bruk i prosjektet |
|---|---|
| `final_outputs/coop_business_model_analysis.md` | Hovedsyntese for Coop sin forretningsmodell, strategiske posisjonering, app/Lobyco og kildekritikk |
| `final_outputs/coop_business_model_one_page.md` | Kort oppsummering brukt til å identifisere nøkkeltall og hovedspenninger |
| `data/coop_business_model_findings.csv` | Strukturert evidens med claim type, kilde, lens og tolkning |
| `data/coop_business_model_findings.json` | Maskinlesbar versjon brukt til kontroll av funn og kildeklassifisering |
| `data/source_register.csv` | Kildetype, bias, marketing_source-merking og kildekritiske notater |
| `final_outputs/coop_key_takeaways_summary.pdf` | Kontrollert kortversjon, ikke brukt som primærkilde for sterke påstander |
| `raw_sources/*.md` | Brukt ved behov for å kontrollere ordlyd i originalscrape |
| Lokale Coop-årsrapport-PDF-er ekstrahert i runnen | Brukt som sterkeste kilde for økonomi, butikknettverk og årsrapporttall |

## Kort metodebeskrivelse

Scraping-runnen brukte Crawl4AI til å hente offentlige nettsider og lagre én Markdown-fil per kilde. To lokale Coop-årsrapport-PDF-er ble ekstrahert til tekst og behandlet som primære finansielle kilder. Kildene ble klassifisert som blant annet offisiell selskapsside, årsrapport/finansiell kilde, vendor marketing source, uavhengig nyhetskilde, bransjekilde og app-store-kilde.

Importen her er ikke en ukritisk kopiering av scraping-output. Den kuraterer funn som er relevante for casens kjerne: hvordan Coop i 2026 skal forstå Coop App og Lobyco gitt økonomisk press, fysisk butikkkjerne, kjedeforskjeller og usikre app-/plattformpåstander.

## Viktigste importerte funn

1. **Coop er fortsatt primært en fysisk dagligvareaktør.** Coop Danmark A/S rapporterte 32,565 mrd. DKK i nettoomsetning i 2025 og 536 butikker. Inkludert brugsforeninger var tallet 44,756 mrd. DKK og 900 butikker. Dette er Fact fra årsrapport/finansiell kilde.
2. **Coop er medlemseid og presenterer medlemskap som mer enn lojalitet.** Coop Medlem beskriver mer enn 2 millioner medlemmer som medeiere, ingen aksjonærer, kontante medlemsfordeler og lokal påvirkning. Dette er offisiell selvpresentasjon og bør brukes som Claim/Fact avhengig av formulering.
3. **Coop App er best dokumentert som en butikkstøttende lojalitets- og relasjonskanal.** Offisielle Coop-sider beskriver personlige tilbud, bonus, Scan & Betal, digitale kvitteringer, handleliste, spill, klimaavtrykk og lokal butikkkommunikasjon. Dette støtter appens funksjon, men ikke lønnsomhet.
4. **Netthandel er ikke dagens sentrale digitale kanal.** Coop.dk MAD ble lukket i 2023, og Coop.dk-webshop ble lukket 31. januar 2025 med henvisning til fokus på fysiske butikker. Dette styrker bricks-and-mortar-rammen.
5. **Lobyco fremstår som digital kapasitet og mulig OEM-/plattformlogikk, men evidensen er vendor-marketing.** Lobyco hevder mer enn 1,8 millioner appbrukere, 25 % av danske husholdninger, ca. 880 000 månedlige aktive brukere og 50 % høyere handlefrekvens blant appbrukere. Dette støtter app-adopsjon, men ikke nødvendigvis lønnsomhet eller kausal effekt.
6. **Playable indikerer retail media / leverandørfinansiert verdi via gamification.** Playable hevder blant annet +100 000 unike spillere per spill, 9 % høyere kurvverdi for premieinnløsere i 2023, 4,25 millioner Christmas game plays og 500 000 premier innløst i Coop-butikker. Dette bør behandles som Marketing claim.
7. **Shortcut støtter apputviklingshistorikk og OEM-fortelling, men er ikke nøytral.** Shortcut hevder over 1,5 millioner downloads, over 250 000 daglige brukere og at Coop App er blitt en OEM-løsning. Kilden kan brukes til historikk/kapabilitet, ikke som dokumentasjon på strategisk effekt.
8. **Kjedeporteføljen er strategisk kompleks.** Kvickly, SuperBrugsen, Brugsen og 365discount uttrykker ulike løfter: bredt varehus/tilbud, kvalitet/lokal mat, lokal nærhet og discount/lavpris. Dette støtter spørsmålet om én app-logikk kan passe alle kjeder.
9. **Private labels og leverandørrelasjoner er relevante for forretningsmodellen.** Coop oppgir mer enn 3 000 Coop-produkter og mer enn 1 200 Änglamark-produkter. Coop Trading oppgir 700+ leverandører. Dette støtter retail-/supplier-dimensjonen, men ikke direkte appøkonomi.
10. **Kjerneproblemet er governance og verdiomsetting.** Evidensen peker mot at Coop må vite om appinvesteringer faktisk skaper butikktrafikk, kurvverdi, margin, lojalitet, leverandørfinansiert verdi eller datadrevet relevans.

## Viktigste kildekritiske caveats

- Lobyco, Playable og Shortcut er kommersielt interesserte kilder. De kan brukes til å vise hva aktørene hevder, hvilke metrics de fremhever og hvordan verdilogikken presenteres, men ikke som nøytral dokumentasjon på lønnsomhet.
- Coop egne sider og pressemeldinger er offisielle og nyttige for faktiske tall, identitet og selvpresentasjon, men de har også omdømme- og turnaround-interesse.
- App-adopsjon, månedlige aktive brukere, daglige brukere, spilldeltakelse og handlefrekvens må ikke behandles som dokumentasjon på profitabilitet.
- Lobyco-claim om høyere handlefrekvens kan ha seleksjonsbias: appbrukere kan allerede være mer lojale Coop-kunder.
- Playable sine tall kan vise kampanjeengasjement og mulig store-redemption-logikk, men de dokumenterer ikke netto lønnsomhet etter kampanjekostnader, leverandørbetalinger eller kannibalisering.
- Shortcut nevner e-handel som appfunksjon, men dette må historiseres fordi Coop.dk MAD og Coop.dk-webshop senere er lukket.
- Google Play-URL-en returnerte “requested URL was not found” under scraping. Den er derfor en svak app-store-kilde og skal ikke brukes til nøkkelpåstander.
- Kjedespesifikke resultat-/margin-/app-KPI-er ble ikke funnet i offentlige kilder.

## Hvordan funnene bør brukes i oppgaven

Funnene bør brukes til å styrke analysen av Coop sin strategiske situasjon før anbefalinger velges:

- som dokumentasjon på at Coop sin økonomiske og operasjonelle kjerne er fysisk dagligvarehandel,
- som evidens for at Coop App må vurderes som butikkstøttende digital infrastruktur, ikke som separat e-commerce-transformasjon,
- som grunnlag for Digital Business Model-spørsmål om value proposition, value creation, value capture, key resources, channels og governance/KPI-er,
- som kildekritisk grunnlag for å skille mellom app reach, app engagement, butikkadferd, inntekter og lønnsomhet,
- som støtte for at kjedeforskjeller kan være strategisk relevante uten å konkludere med separate apper,
- som støtte for at Lobyco kan være en digital kapabilitet eller mulig plattform/OEM-ressurs uten å konkludere med behold/salg.

## Hva funnene ikke kan dokumentere sikkert

Scraping-runnen kan ikke dokumentere sikkert:

- at Coop App er lønnsom,
- at Coop App kausalt øker handlefrekvens, kurvstørrelse eller margin,
- hvilken Lobyco-eierskapslogikk som er riktig,
- at retail media er en stor eller varig inntektskilde for Coop,
- at gamification gir langsiktig lojalitet,
- at én felles app eller kjedespesifikke appmoduler er riktig løsning,
- hvilke interne investeringer Coop bør prioritere,
- hvilken caseaktør som bør rådgives.

## Google Play-caveat

Google Play-kilden i scraping-runnen returnerte “requested URL was not found”. Den skal derfor ikke brukes som kilde for app-rating, downloads, funksjonalitet eller strategisk verdi. Hvis Google Play-data trengs senere, må kilden hentes på nytt eller erstattes med en mer stabil app-store-/metadata-kilde.
