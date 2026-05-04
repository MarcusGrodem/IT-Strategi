# Evidensverifikasjonsplan

Dette dokumentet er en arbeidsplan for verifisering av claims, tall og kilder før valg av endelig retning. Det er ikke en finalrapport, og det låser ikke caseperson, teori eller strategisk stance.

## Formål

Planen skal avklare hvilke påstander som må sjekkes før prosjektet kan velge mellom retninger som for eksempel:

- Martin Hasgard Olesen + hybrid governance
- Michael Tilsted + 365discount go-deep
- Thor Skov Jørgensen + investeringsstyring

Disse retningene er foreløpige arbeidsretninger, ikke valgte retninger.

## Prioriteringslogikk

| Prioritet | Betydning |
|---|---|
| A | Må verifiseres før valg av retning. Påvirker caseperson, teori, strategisk stance eller vurderingen av Martin/Michael/Thor-retningene. |
| B | Må verifiseres før finalrapport, men trenger ikke nødvendigvis være ferdig før retning velges. |
| C | Nyttig, men ikke kritisk. Kan styrke argumentet hvis kilden er enkel å lukke. |
| D | Svak eller bør droppes med mindre bedre kilde dukker opp. Må ikke være bærende. |

## A — Må Verifiseres Før Valg Av Retning

| Claim ID | Kort claim | Hvor claimet finnes | Nåværende kilde | Kildetype | Claim label | Hvorfor viktig | Retninger som påvirkes | Hva må verifiseres | Foreslått metode | Risiko uten verifisering | Prioritet |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VP-A01 | Coop 2025: 32.565bn DKK net revenue, 313m DKK EBITDA før eiendomssalg og -215m DKK EBIT | E016, E027, E029, `key_numbers.md`, `strategic_situation_analysis.md`, `decision_preparation.md` | Coop Danmark A/S årsrapport 2025 / offisiell resultatmelding | Årsrapport / offisiell selskapskilde | Fact | Finansielt press er bærende for Thor/investeringsstyring, hybrid governance og reduksjon/forenkling | Thor, Martin, alle investeringsstances | Eksakt metric, om tallene gjelder Coop Danmark A/S eller inkl. brugsforeninger, og om EBITDA-formuleringen er "before gains on sale..." | Bruk lokal PDF `05_evidence/coop-danmark-aarsrapport-2025.pdf`; noter sidetall/årsrapporttekst; kryssjekk mot offisiell resultatmelding hvis tilgjengelig | Feil metric kan gi svak eller misvisende økonomisk analyse | A |
| VP-A02 | 232m DKK loss i case vs. -215m DKK EBIT i årsrapport/offisiell kilde | E008, E016, E029, `key_numbers.md`, `decision_preparation.md` | Eksamenscase + Coop årsrapport/resultatmelding | Offisiell case + årsrapport | Fact / metric mismatch | Kan endre hvor hardt finansielt press skal vektlegges og hvordan tall brukes i finalrapport | Thor/investeringsstyring, Martin/hybrid, reduksjon/salg | Om 232m gjelder nettoresultat, resultat etter skatt, konsernresultat eller annet; hvordan det relaterer til EBIT -215m | Les eksakt caseformulering og årsrapportens resultatoppstilling; lag en mini-reconciliation med metric-navn | Blanding av EBIT/net loss kan bli en tydelig eksamensfeil | A |
| VP-A03 | Coop.dk MAD stengte i 2023 grunnet manglende lønnsomhet; Coop.dk webshop stengte 31. januar 2025 | E001, E033, `key_numbers.md`, `strategic_situation_analysis.md` | Eksamenscase, Coop.dk MAD-side, Coop kundeservice, Ritzau/NI | Offisiell case + offisiell selskapsside + nyhetskilde | Fact | Grunnlaget for at appen bør analyseres som butikkstøttende kanal, ikke online grocery | Martin/hybrid, Thor/investering, alle DBM-perspektiver | Eksakt begrunnelse for 2023-lukkingen; presis distinksjon mellom Coop.dk MAD og Coop.dk webshop | Les case og importerte råkilder; noter nøyaktig formulering og datoer | Feil kan gjøre digital/physical-frame upresist | A |
| VP-A04 | Coop selger i dag gjennom fysiske butikker / fysisk butikknett er strategisk kjerne | E002, E028, E033, `strategic_situation_analysis.md` | Eksamenscase + Coop årsrapport 2025 | Offisiell case + årsrapport | Fact / Inference | Bærer alle argumenter om store economics, app som butikkstøtte og investeringsprioritering | Alle retninger, særlig Martin og Thor | Om "kun fysiske butikker" er absolutt korrekt etter webshop-lukking; butikkantall 536/900 og definisjon | Sjekk case, årsrapport og Coop kundeservice-lukkeside; skille Coop Danmark A/S fra brugsforeninger | Hvis feil, kan hele butikkbasert framing svekkes | A |
| VP-A05 | Coop App har mer enn 1.8m brukere, ca. 880k MAU og 25% household reach | E004, E034, `key_numbers.md`, `decision_preparation.md` | Lobyco case/insight-sider | Vendor/subsidiary marketing | Marketing claim | App-rekkevidde er bærende for Martin/hybrid og for argument mot ren reduksjon/salg | Martin, Thor, styrke/hybrid/Lobyco-kapasitet | Eksakt kilde, dato, definisjon av bruker, MAU og household reach; om tallene gjelder Danmark og hvilken periode | Les Lobyco råkilder; hvis mulig kryssjekk med Coop egne kilder eller app stores, men ikke bruk Google Play-scrapen | Kan overdrive appens strategiske verdi | A |
| VP-A06 | Appbrukere handler 50% oftere / er mer verdifulle | E009, E034, `key_numbers.md`, `claim_reliability_matrix.md` | Lobyco case | Vendor/subsidiary marketing | Marketing claim | Påvirker om appinvestering kan forsvares som value capture eller bare reach | Martin/hybrid, styrke appinvestering, DVC + DBM | Eksakt formulering; om det er frequency, basket, revenue eller annet; om det er korrelasjon eller kausal påstand | Les Lobyco-kilde; noter at intern KPI mangler; skriv som "Lobyco hevder" hvis brukt | Høy risiko for selection bias og falsk kausalitet | A |
| VP-A07 | Lobyco er spin-out/subsidiary/digital capability/OEM-kapasitet | E005, E034, E035, source register, `strategic_situation_analysis.md` | Eksamenscase, Lobyco, Shortcut | Offisiell case + vendor/developer marketing | Claim / Marketing claim / Inference | Avgjør om Lobyco kan behandles som kapasitet, plattformmulighet, governance-problem eller salgsobjekt | Martin/hybrid, Thor/investering, Lobyco behold/salg | Juridisk/organisatorisk status, eierskap, mandat, ekstern kundebase, om OEM-claim fortsatt er relevant | Les case, Lobyco corporate info og Shortcut-kilde; søk i lokale råkilder; ikke anta økonomisk verdi | Uverifisert Lobyco-status kan gjøre salgs-/governanceargument spekulativt | A |
| VP-A08 | Retail media / supplier-funded campaign value kan være verdilogikk for Coop App/Lobyco | E010, E036, E037, `source_criticism.md`, `decision_preparation.md` | Playable, Lobyco, Coop Trading/private label-kontekst | Supplier/vendor marketing + Coop-kontekst | Marketing claim / Inference | Særlig viktig hvis Martin + platform/ecosystem eller Lobyco-kapasitet blir retning | Martin, DVC + Platform, Lobyco kontrollert kapasitet | Om supplier-funded prizes faktisk gir Coop-verdi, ikke bare campaign engagement; om Coop/Lobyco har retail media-inntekter | Les Playable/Lobyco råkilder; søk etter nøytrale retail-media benchmarks; marker manglende Coop-intern revenue-data | Kan overdrive Coop som plattform eller retail-media case | A |
| VP-A09 | Kjedene har ulike kundeløfter som kan støtte "go deep" eller kjedespesifikke moduler | E038, `decision_preparation.md`, `strategic_situation_analysis.md` | Coop chain pages | Offisiell selskapsside / selvpresentasjon | Inference | Bærer Michael/go-deep, Rikke-moduler og Martin chain governance | Michael, Rikke, Martin, DVC + Porter | Eksakte kjedeposisjoner for Kvickly, SuperBrugsen, Brugsen og 365discount; om forskjellene er relevante for app | Les Coop chain pages og case; behandle som Coop-selvpresentasjon, ikke kundeoppfatning | "Go deep" kan virke antatt uten empirisk kjedestøtte | A |
| VP-A10 | Konkurrentinferens: digitale verktøy skaper verdi når de passer business model, ikke bare fordi de er digitale | E015, competitor evidence, `competitor_analysis.md`, imported competitor scrape | Lokal konkurrent-scrape med originalkilder | Sekundær syntese basert på offentlige kilder | Inference | Støtter hybrid governance, go-deep og selektiv forenkling; svekker enkel "styrk appen" | Martin/hybrid, Michael/go-deep, DVC + Porter, DBM | At inferensen faktisk støttes av Salling, Lidl, REMA, Dagrofa/MENY og Nemlig-kildene | Gå fra `competitor_evidence.md` til original-URLer i scrape source register; dokumenter 3-4 beste eksempler | Hvis bare syntese brukes, kan analysen bli kildekritisk svak | A |
| VP-A11 | Salling har høy revenue/profit og store-integrerte apper/Scan&Go | E017, E018, competitor evidence, `key_numbers.md` | Salling key figures + Netto/Bilka/foetex app/support pages | Offisiell finans + feature/support pages | Fact + Inference | Viktig benchmark for digital/store integration og mulig kjedespesifikk app-logikk | Martin, Michael, Rikke, DVC + Porter | Eksakte 2025-tall; hvilke app-/Scan&Go-funksjoner er faktisk dokumentert; ikke koble app direkte til profit | Les original Salling key figures og app/support pages fra scrape | Kan feilaktig antyde at Salling er profitabel på grunn av app | A |
| VP-A12 | Lidl Plus og REMA støtter discount-/savings-/simplicity-logikk | E019, E021, E022, competitor evidence, `decision_preparation.md` | Lidl official pages, REMA official pages, Paqle, Ritzau/NI | Blandet offisiell, sekundær og presse | Feature claim / Inference / Claim | Kritisk for Michael + 365discount go-deep | Michael/go-deep, DVC + Porter, selektiv forenkling | Lidl Plus-funksjoner, REMA Scan Selv, REMA økonomitall og eventuelle price/value claims; hold Paqle og Ritzau atskilt | Les originalkilder; ikke la REMA market share bli bærende | Michael-retningen blir svak hvis discountbeviset er tynt eller for sekundært | A |
| VP-A13 | Det finnes ikke intern Coop KPI-evidens for appens effekt på basket, margin, butikktrafikk eller lønnsomhet i nåværende filer | `source_criticism.md`, `strategic_situation_analysis.md`, daily log | Fravær i prosjektfiler | Evidence gap / Assumption | Assumption | Bærer kildekritisk språk og governance/KPI-behov | Alle retninger, særlig Martin og Thor | At det faktisk ikke finnes interne KPIer i lokale filer; om case inneholder KPIer som er oversett | Søk i `05_evidence`, `10_project_context`, rå casefiler hvis tilgjengelig | Hvis intern KPI finnes men overses, blir kildekritikken feilkalibrert | A |

## B — Må Verifiseres Før Finalrapport

| Claim ID | Kort claim | Hvor claimet finnes | Nåværende kilde | Kildetype | Claim label | Hvorfor viktig | Retninger som påvirkes | Hva må verifiseres | Foreslått metode | Risiko uten verifisering | Prioritet |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VP-B01 | Coop revenue falt med ca. 1.0bn DKK i 2025 | E007, `key_numbers.md` | Eksamenscase | Offisiell case | Fact | Kan støtte økonomisk press, men må ikke blandes med årsrapporttall | Thor, investeringsstyring | Eksakt formulering og metric | Les case; sammenlign med 32.565bn / 32.5bn | Feil revenue-begrep svekker finansdelen | B |
| VP-B02 | Playable gamification metrics: +100k players, 9% høyere basket for prize redeemers, 4.25m plays, 500k prizes | E037, `key_numbers.md`, `source_criticism.md` | Playable case | Supplier marketing | Marketing claim | Nyttig for retail media/gamification, men ikke beslutningskritisk hvis retningen ikke blir retail media | Martin, DVC + Platform | Eksakt metric, periode, sammenligningsgruppe og om det er korrelasjon | Les Playable-kilde; skriv som leverandørclaim; ikke inferer netto profit | Kan skape ubegrunnet lojalitets-/profitpåstand | B |
| VP-B03 | Shortcut hevder apputviklingshistorikk, OEM-løsning, 1.5m downloads og 250k daily users | E011, E035, `key_numbers.md` | Shortcut case | Supplier/developer marketing | Marketing claim | Bakgrunn for digital capability, men ikke nøytral suksess-evidens | Martin, Thor, Lobyco-kapasitet | Dato, historisk kontekst, om tallene fortsatt gjelder | Les Shortcut-kilde; sammenlign mot Lobyco-tall | Kan overdrive teknologisk modenhet og strategisk suksess | B |
| VP-B04 | Dagrofa/MENY loyalty og BrancheIndex claims | E023, E024, competitor evidence | Dagrofa/Ritzau, Loyalty Group | Offisiell/presse/survey | Claim / Inference | Støtter kjedeidentitet og Rikke/Torben, men ikke bærende for hovedvalg | Rikke, Torben, go-deep | Metode, original survey, presise ranking claims | Finn original BrancheIndex hvis mulig; ellers bruk med tydelig caveat | Kan gjøre chain-positioning for sikker | B |
| VP-B05 | Nemlig revenue / adjusted EBITDA / negativt resultat viser online grocery som vanskelig økonomi | E025, `key_numbers.md`, competitor evidence | Nemlig/Ritzau + Proff | Pressemelding + sekundær database | Claim / Fact depending metric | Nyttig kontrast til coop.dk-lukking | Thor, DBM, online grocery contrast | Metric-skille: revenue, adjusted EBITDA, profit for year | Les Nemlig/Ritzau og Proff; hold år og selskap likt | Kan feilaktig konkludere om online grocery generelt | B |
| VP-B06 | DI e-commerce/mobile purchase claims: 49% mobile share, 81% monthly online shoppers, 136bn DKK online consumption | E026, `key_numbers.md` | Dansk Industri tracker | Markedsrapport | Fact / market statistic | Gir digital kontekst, men ikke grocery profitability | DVC, Martin | Eksakt år, populasjon og om tall gjelder all e-commerce | Les DI-kilde fra scrape source register | Kan bli brukt for bredt som grocery-bevis | B |
| VP-B07 | Coop medlemseid identitet og 2m+ medlemmer/co-owners | E030, `key_numbers.md`, source register | Coop Medlem / Coop amba | Offisiell selskapsside/årsrapport | Claim / Fact | Viktig for Torben/Rikke og governance-identitet | Torben, Martin, DVC relationships | Eksakt formulering, om "members" og "co-owners" brukes likt | Les Coop Medlem og eventuelt Coop amba årsrapport | Kan gjøre member-argument for normativt uten kilde | B |
| VP-B08 | Offisielle Coop app-sider beskriver Scan & Betal, kvitteringer, handlelister, personlige tilbud, bonus, spill og lokalt butikkinnhold | E032, source register | Coop Medlem app pages | Offisiell selskapsside | Fact om funksjon / Claim om verdi | Trengs for DVC-opplevelser og app som butikkstøtte | Martin, Rikke, DVC | Hvilke funksjoner finnes nå og hvordan Coop beskriver dem | Les Coop app pages; skill funksjon fra effekt | Kan overdrive effekt av funksjoner | B |
| VP-B09 | REMA revenue/profit fra Paqle | E019, `key_numbers.md`, competitor evidence | Paqle | Sekundær finansdatabase | Claim | Benchmark for Michael, men bør ikke være bærende alene | Michael, DVC + Porter | Eksakt selskap, år, regnskapsbegrep og om bedre offisiell kilde finnes | Søk etter REMA årsrapport/offisiell kilde; hvis ikke, bruk Paqle som sekundær | Sekundær kilde kan svekke konkurrentdelen | B |
| VP-B10 | REMA market-share estimate 18.2% vs Netto 17.9%, bestridt av Salling | E020, competitor evidence | Ritzau/NI | Trade/news | Claim / contested claim | Kan illustrere discountpress, men er usikker | Michael | Eksakt claim, kilde og Salling-kontestasjon | Les Ritzau/NI-kilde; bruk kun som contested evidence | Overclaiming markedslederposisjon vil være risikabelt | B |

## C — Nyttig, Men Ikke Kritisk

| Claim ID | Kort claim | Hvor claimet finnes | Nåværende kilde | Kildetype | Claim label | Hvorfor viktig | Retninger som påvirkes | Hva må verifiseres | Foreslått metode | Risiko uten verifisering | Prioritet |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VP-C01 | Coop spør 1,000 medeiere hver uke om priser, produkter m.m. | `key_numbers.md`, source register | Coop Medlem | Offisiell selskapsside | Claim | Kan støtte member/customer listening, men ikke appstrategi direkte | Torben, Martin | Eksakt formulering og om dette er aktiv praksis | Les Coop Medlem-kilde | Liten risiko hvis brukt som selvpresentasjon | C |
| VP-C02 | Medlemsfordeler: 5% bonus på frukt/grønt, opptil 20 personlige tilbud, 5-15% FordelsKonto | E031, `key_numbers.md` | Coop Medlem pages | Offisiell selskapsside | Claim | Kan beskrive value proposition og personalisering | DVC, Martin/Rikke | Vilkår og om tall er gjeldende | Les relevante Coop-sider | Kan bli detaljstøy hvis ikke knyttet til app/Lobyco | C |
| VP-C03 | Coop private labels: 3,000+ Coop-produkter og 1,200+ Änglamark | E039, `key_numbers.md` | Coop official private-label pages | Offisiell selskapsside | Fact / Claim | Kan støtte business model og supplier/value proposition | DBM, Martin | Eksakt produktantall og dato | Les Coop private-label pages | Lav risiko, men kan trekke analysen bort fra app | C |
| VP-C04 | Coop Trading: 700+ suppliers og ca. 10% partner suppliers | E040, `key_numbers.md` | Coop Trading | Bransje/promotional | Claim | Kan støtte supplier-network kontekst, ikke retail-media proof | DVC + Platform | Eksakt definisjon av supplier/partner supplier | Les Coop Trading-sider | Kan overtolkes som retail-media kapasitet | C |
| VP-C05 | Apple App Store kan brukes til svak feature/availability-sjekk | Source register | Apple App Store | App store metadata | Claim / metadata | Kan hjelpe ved funksjonssjekk, men ikke bærende | DVC | Nåværende appmetadata, ratings og versjon hvis relevant | Re-sjekk manuelt hvis app store-data skal brukes | App store-data kan bli feilaktig brukt som adopsjonsbevis | C |

## D — Svak / Dropp Med Mindre Bedre Kilde Dukker Opp

| Claim ID | Kort claim | Hvor claimet finnes | Nåværende kilde | Kildetype | Claim label | Hvorfor viktig | Retninger som påvirkes | Hva må verifiseres | Foreslått metode | Risiko uten verifisering | Prioritet |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VP-D01 | Google Play-scrapen støtter Coop App-påstander | E041, source register, source criticism | Google Play raw scrape | Failed app-store source | Failed source / weak claim | Ikke viktig nok før den er re-scrapet | Alle app-adopsjonsclaims hvis misbrukt | Om Google Play-siden faktisk finnes og kan hentes | Re-scrape manuelt eller dropp | Høy risiko for feil; skal ikke brukes nå | D |
| VP-D02 | Coop App er strategisk eller finansielt suksessfull | Decision risks, source criticism | Lobyco/Playable/Shortcut claims | Marketing/supplier claims | Inference / unsupported claim | Ville påvirket styrke app-investering, men er ikke støttet | Styrke app, Martin | Intern KPI, revenue/margin, kausal effekt, uavhengig dokumentasjon | Ikke bruk før intern eller sterk ekstern evidens finnes | Overclaiming; kan ødelegge kildekritisk troverdighet | D |
| VP-D03 | Lobyco bør selges / afhændes | Strategic stance options | Analyseidé, ikke kilde | Assumption / recommendation direction | Assumption | Case-option, men ikke evidensbasert claim ennå | Thor, salg/afhændelse | Salgsverdi, kostnader, strategisk alternativverdi, ekstern kundebase | Må undersøkes som scenario, ikke påstand | Spekulativ og for tidlig anbefaling | D |
| VP-D04 | Lobyco bør beholdes fordi det beviser konkurransefortrinn | Ikke eksplisitt som fakta; risiko i analyse | Lobyco/Shortcut marketing | Marketing-based inference | Weak inference | Kan påvirke Martin/Thor, men bevisgrunnlaget er svakt | Martin, Thor, Lobyco-kapasitet | Unikhet, imiterbarhet, økonomisk bidrag og strategisk nødvendighet | Krever sterkere data; skriv bare "kan være kapasitet" | Overdriver RBV/plattformargument | D |
| VP-D05 | Konkurrenter vinner fordi de har apper | Competitor risk | Lokal konkurrent-syntese hvis feiltolket | Overforenklet inference | Weak inference | Må unngås; riktig inferens er fit, ikke app i seg selv | Michael, DVC + Porter | Uavhengig bevis på appens kausale effekt på konkurrenters suksess | Ikke bruk; erstatt med "digitale verktøy ser ut til å passe business model" | Feil kausalitet og for bred konkurrentanalyse | D |
| VP-D06 | Appbrukere er mer lønnsomme | Lobyco frequency claim hvis overtolket | Lobyco | Marketing claim | Unsupported inference | Kan friste til app-styrking, men mangler profitdata | Martin, styrke app | Profit/margin per appbruker vs kontrollgruppe | Dropp inntil intern KPI finnes | Sterk kausalitets- og selection-bias-risiko | D |

## Verifikasjonsroadmap

1. Verifiser Coop-finans og butikkfotavtrykk først: årsrapport 2025, E027-E029, 536/900 butikker, 32.565bn vs 44.756bn, EBITDA og EBIT.
2. Avklar metric-konflikten mellom 232m DKK loss og -215m DKK EBIT.
3. Verifiser eksamenscase-claims: coop.dk-lukking, fysisk butikkmodell, Lobyco/app-spørsmål og de fem casepersonene.
4. Verifiser Coop App-adopsjon: 1.8m users, 25% household reach, 880k MAU og definisjonene bak tallene.
5. Verifiser Lobyco-eierskap/rolle/business model: spin-out/subsidiary, OEM/platform claims, eksterne kunder og eventuell økonomi.
6. Verifiser Playable og Shortcut bare etter at hovedretning er snevret inn, siden de er supplier/vendor claims.
7. Verifiser konkurrent-finans og appmekanikk: Salling først, deretter Lidl/REMA for Michael-retningen, Dagrofa/MENY for kjede-/lojalitetsvinkler og Nemlig for online-grocery-kontrast.
8. Verifiser Loyalty Group / BrancheIndex og customer index-claims sist, med mindre Rikke/Torben/Michael-retningen blir avhengig av dem.
9. Lag etter verifisering en kort "usable evidence list" for finalrapport med bare claims som har originalkilde og trygg formulering.

## Retningsspesifikke Evidensbehov

### Martin Hasgard Olesen + Hybrid Governance

| Spørsmål | Vurdering |
|---|---|
| Claims som må være sterke | Coop-finans/store core (VP-A01-A04), app-rekkevidde som reach men ikke profit (VP-A05), manglende intern KPI (VP-A13), Lobyco som mulig kapasitet (VP-A07), competitor fit (VP-A10). |
| Claims som kan være svake uten at retningen faller | Playable gamification metrics, Shortcut downloads/daily users, BrancheIndex. Retningen kan fortsatt fungere hvis governance/KPI-behovet er sterkt. |
| Kilder som må verifiseres først | Coop årsrapport, case, Lobyco reach-kilder, source criticism, 2-3 beste konkurrentkilder. |
| Største kilde-/evidensrisiko | At appens verdi forblir marketingbasert. Hybrid governance kan bli en vag kompromissposisjon hvis KPIer og beslutningskriterier ikke konkretiseres. |

### Michael Tilsted + 365discount Go-Deep

| Spørsmål | Vurdering |
|---|---|
| Claims som må være sterke | Kjedene har ulike kundeløfter (VP-A09), Lidl/REMA støtter savings/simplicity (VP-A12), competitor fit-inferens (VP-A10), fysisk butikkmodell (VP-A03-A04). |
| Claims som kan være svake uten at retningen faller | Lobyco ekstern økonomi, retail media, Playable gamification. Go-deep kan handle om modularisering og discount-fit uten retail-media bevis. |
| Kilder som må verifiseres først | Coop 365discount/kjedesider, Lidl Plus-sider, REMA Scan Selv/official pages, Paqle/Ritzau kun som sekundær støtte. |
| Største kilde-/evidensrisiko | Manglende direkte 365discount-kundedata. Retningen kan bli for mye konkurrentinferens og for lite Coop-spesifikk hvis 365discount-evidens mangler. |

### Thor Skov Jørgensen + Investeringsstyring

| Spørsmål | Vurdering |
|---|---|
| Claims som må være sterke | Coop-finans (VP-A01-A02), fysisk butikkjerne (VP-A03-A04), app reach vs. outcome-usikkerhet (VP-A05-A06), Lobyco-status/kapasitet (VP-A07), manglende KPI-data (VP-A13). |
| Claims som kan være svake uten at retningen faller | Detaljert Lidl/REMA/Dagrofa-evidens, Playable gamification, app-feature-detaljer. CEO-vinkelen trenger primært beslutnings- og porteføljelogikk. |
| Kilder som må verifiseres først | Coop årsrapport, case, Lobyco ownership/business model-kilder, eventuelt Lobyco økonomi/ekstern kundebase hvis salg/afhændelse vurderes. |
| Største kilde-/evidensrisiko | Salg/afhændelse av Lobyco er svært spekulativt uten data om kost, salgsverdi og strategisk alternativverdi. |

## Teorispesifikke Evidensbehov

### DVC + Digital Business Model

| Behov | Vurdering |
|---|---|
| Claims teorien trenger | App-funksjoner og reach (VP-A05, VP-B08), store core (VP-A03-A04), Lobyco som mulig kapabilitet (VP-A07), value capture-usikkerhet (VP-A13), competitor fit (VP-A10). |
| Claims teorien ikke kan bevise | At appen er lønnsom, at appbrukere er mer profitable, at Lobyco er konkurransefortrinn, eller at retail media fungerer økonomisk. |
| Kildekritikk som må inn | DVC-output er ikke outcome; Lobyco/Playable/Shortcut er markedsføringskilder; business model-perspektivet trenger value capture-data som mangler. |

### DVC + Porter/Positioning

| Behov | Vurdering |
|---|---|
| Claims teorien trenger | Kjedespesifikke kundeløfter (VP-A09), Lidl/REMA/Salling evidence (VP-A11-A12), competitor fit (VP-A10), app-relevans og DVC-funksjoner (VP-B08). |
| Claims teorien ikke kan bevise | At konkurrentene vinner på grunn av apper, eller at 365discount bør ha egen app uten kost-/arkitekturevidens. |
| Kildekritikk som må inn | Konkurrentkilder er ofte promotional eller sekundære; Porter må brukes til fit/trade-offs, ikke bred markedsrapport. |

### Digital Business Model + Implementation

| Behov | Vurdering |
|---|---|
| Claims teorien trenger | Finansielt press (VP-A01-A02), fysisk butikkmodell (VP-A03-A04), Lobyco-status og governance (VP-A07), manglende KPIer (VP-A13), kost/kompleksitet hvis tilgjengelig. |
| Claims teorien ikke kan bevise | Kundens opplevde digitale verdi, appens lojalitetseffekt eller at Lobyco bør selges. |
| Kildekritikk som må inn | Implementation-styring må ikke bli anbefaling før analyse; fravær av KPIer er et evidensgap, ikke bevis på at appen ikke virker. |

### DVC + Platform/Ecosystem

| Behov | Vurdering |
|---|---|
| Claims teorien trenger | Retail media/supplier-funded value (VP-A08), Lobyco/OEM/platform claims (VP-A07), Coop supplier/private-label kontekst (VP-C03-C04), app reach (VP-A05). |
| Claims teorien ikke kan bevise | At Coop allerede er en moden plattform, at supplier-funded campaigns er lønnsomme, eller at network effects finnes. |
| Kildekritikk som må inn | Plattformspråk må tones ned til "mulig verdilogikk" med mindre uavhengig dokumentasjon finnes; Playable/Lobyco er high-bias kilder. |

## Formuleringer Som Bør Unngås Med Mindre De Verifiseres

Ikke bruk disse formuleringene før sterkere evidens finnes:

- "Coop App er lønnsom."
- "Coop App beviser profitabel digital transformation."
- "Lobyco beviser at Coop har et konkurransefortrinn."
- "Appbrukere er mer profitable."
- "Appbrukere handler mer på grunn av appen."
- "Gamification øker lønnsomheten."
- "Retail media er en dokumentert ny inntektsmotor for Coop."
- "Coop bør selge Lobyco."
- "Coop bør beholde Lobyco fordi det er strategisk unikt."
- "Konkurrenter vinner fordi de har apper."
- "Lidl/REMA/Salling viser at Coop må kopiere konkurrentenes app."
- "Google Play-data viser Coop App-adopsjon."
- "BrancheIndex beviser kundelojalitet."

Tryggere formuleringer:

- "Lobyco hevder ..."
- "Kilden indikerer ..."
- "Dette støtter app-adopsjon, men ikke nødvendigvis lønnsomhet."
- "Dette bør behandles som en mulig verdilogikk, ikke som dokumentert effekt."
- "Konkurrentevidensen antyder digital passform med business model, ikke at apper alene skaper suksess."

## Anbefalte Neste Verifikasjonsoppgaver

1. Les `05_evidence/coop-danmark-aarsrapport-2025.pdf` og noter eksakt tekst/sidetall for revenue, EBITDA, EBIT og butikkantall.
2. Finn og les eksakt eksamenscaseformulering for 232m DKK loss, coop.dk-lukking og "physical stores" for å avklare metric og scope.
3. Gå til Lobyco-råkildene i importen og lag en kort source note for 1.8m users, 25% household reach, 880k MAU og 50% frequency claim.
4. Søk i prosjektets råkilder etter intern eller offisiell Coop-evidens for appens effekt på butikktrafikk, basket, margin eller retention. Hvis den ikke finnes, marker "mangler".
5. Verifiser Lobycos organisasjons-/eierskapsstatus og om Lobyco har dokumenterte eksterne kunder eller inntekter.
6. Velg 3-4 konkurrentclaims fra originalkilder som best støtter digital passform: Salling app/store utility, Lidl Plus savings, REMA Scan Selv/simplicity og Dagrofa/MENY chain identity.
7. For Michael-retningen: verifiser Coop 365discount-kjedeposisjon og minst to discount-konkurrentkilder før go-deep vurderes seriøst.
8. For Martin-retningen: verifiser Lobyco/Playable-claims og skriv tydelige kildekritiske formuleringer før retail media eller governance gjøres bærende.
9. For Thor-retningen: undersøk om det finnes Lobyco-kostnader, investeringer, salgsverdi eller ekstern business model-data. Hvis ikke, behold salg/afhændelse som scenario, ikke anbefaling.
10. Oppdater `05_evidence/evidence_register.md`, `05_evidence/key_numbers.md` og denne planen etter verifisering, med status "verifisert", "delvis verifisert" eller "dropp".

## Notat Om Importfiler

Følgende importfiler er lest og bør brukes som arbeidsnotater, ikke som primærkilder i finalrapport:

- `10_project_context/imported_coop_business_model_scrape_2026-05-03.md`
- `05_evidence/coop_business_model_evidence.md`
- `10_project_context/imported_competitor_scrape_2026-05-03.md`

Coop business model-importen er representert i `05_evidence/evidence_register.md`, `05_evidence/source_register.md`, `05_evidence/source_criticism.md`, `05_evidence/key_numbers.md` og `05_evidence/coop_business_model_evidence.md`, særlig gjennom E027-E041. Disse bør spores tilbake til råkilder eller lokal PDF før finalrapport.
