# Implementering — hvordan Coop teoretisk skal gjennomføre anbefalingene

Denne filen kobler de tre anbefalingene til pensum-litteraturen om *implementering* av IT-strategi. Bruk den til å svare på sensorspørsmålet «hvordan skal Coop faktisk gjøre dette?» — og til å demonstrere at oppgaven ikke stopper ved strategiformulering.

---

## Det teoretiske grunnlaget for implementering

### Hovedrammeverk: Tawse & Tabesh (2021) — 3C
Tawse & Tabesh identifiserer tre forutsetninger for vellykket strategi-implementering:

| C | Hva det betyr | Hvorfor det er kritisk for Coop |
|---|---|---|
| **Competency** | Organisatorisk evne — kunnskap, ferdigheter, kapasitet | Coop trenger analytisk kapasitet for KPI-hierarkiet og kjedespesifikk innholdsproduksjon |
| **Commitment** | Forpliktelse fra øverste ledelse + nedover i organisasjonen | Skov Jørgensen må eie omleggingen; ellers blir det «nok et initiativ» |
| **Coordination** | Samordning mellom enheter | Coop konsernledelse, kjedene, Lobyco-styre, leverandører — alle må jobbe innenfor samme styringsregime |

### Støttende perspektiver
- **Hedman & Bjørn-Andersen (2016):** Coops historiske *teknologiske gjeld* viser hva som skjer når IT-strategi ikke implementeres med disiplin — kompleksitet akkumuleres, ledelsen mister tillit, investeringer leverer ikke. Implementeringen må aktivt unngå denne fellen.
- **Hybrid governance:** Sentral plattform, KPI-rammeverk og Lobyco-mandat ligger sentralt. Innhold, tilbud, kjedespesifikk innovasjon ligger lokalt. Dette balanserer kontroll og lokal eierskap.
- **Pilot-først-prinsippet:** Initiativer testes i avgrensede pilotmiljøer før konsernskalering. Reduserer risikoen for legacy debt og gir KPI-hierarkiet data å bli kalibrert mot.
- **Wessel et al. (2021) — ITEOT-konsekvens:** Siden Coop driver IT-Enabled Org. Transformation, må implementeringen styrke eksisterende butikk-identitet — ikke skape ny digital identitet. Det disiplinerer scope.

---

## Implementering av Anbefaling 1 — KPI-hierarki

### Mål
Etablere et tre-nivåers målregime (bruk → atferd → lønnsomhet) som styrer videre investering i Coop App og Lobyco etter dokumentert effekt på butikkøkonomi.

### Forutsetninger (3C)
- **Competency:** Coop må bygge analytisk kapasitet — data engineering, eksperimentdesign, BI-modellering. Kan delvis ligge i Lobyco (har dataen), men *eierskapet til KPI-rammeverket* må ligge i konsernledelsen.
- **Commitment:** Skov Jørgensen formelt mandaterer KPI-hierarkiet som det styrende målregimet for digitale investeringer. Uten dette blir det skjøvet til side av kortsiktige aktivitetsmål.
- **Coordination:** Felles definisjoner og rapportering mellom kjedene, Lobyco og konsernøkonomi. Krever at finans, drift og digital deltar i samme styringsmodell.

### Implementeringssekvens (teoretisk)
1. **Mandat (uke 0–4):** CEO-beslutning og kommunikasjon i ledergruppen. Etabler KPI-styringskomite med representanter fra konsern, kjedene og Lobyco.
2. **Baseline (mnd 1–3):** Kartlegg dagens måleregime; identifiser hvor atferds- og lønnsomhetsmål mangler. Definer KPI-treet med konkrete definisjoner.
3. **Datainfrastruktur (mnd 2–6):** Bygg den analytiske kapabiliteten for å koble appbruk til butikkbesøk, kurv, retensjon, margin. Krever felles ID-grunnlag (medlemskap) og rapporteringsplattform.
4. **Inkrementalitetsdesign (mnd 4–9):** Etabler eksperimentell ramme — holdout-grupper, regional utrulling, før/etter-analyser — for å unngå seleksjonsbias.
5. **Beslutningsregime (mnd 6+):** Knyt investeringsbeslutninger formelt til KPI-treet. Initiativer som ikke kan vise vei mot nivå 2 og 3, mister budsjett.

### Risikohåndtering
- *Risiko 1:* Måleinfrastruktur tar tid å bygge → start parallelt med fortsatt drift, ikke som «alt-eller-ingenting».
- *Risiko 2:* Strenge krav oppleves som brems → tydelig kommunikasjon: KPI-hierarkiet *muliggjør* skalering når effekt er dokumentert; det er ikke veto.
- *Risiko 3:* Lobyco-data og Coop-data lever i siloer → krever felles datamodell, eventuelt felles data warehouse.

### Hvordan dette adresserer legacy-debt-risikoen
Hedman & Bjørn-Andersen (2016) viser at Coops teknologiske gjeld delvis skyldes IT-investeringer uten klar effektmåling og uten ledelses-eierskap. KPI-hierarkiet er en direkte mottiltak: det krever effektmåling *før* skalering og *under* drift, og det forutsetter CEO-eierskap.

---

## Implementering av Anbefaling 2 — Kjedespesifikk diversifisering i felles plattform

### Mål
Innenfor én felles Coop-plattform (drevet av Lobyco) skal hver kjede ha sin egen modul som reflekterer kjedens kundeløfte og DVC-relevance for det segmentet.

### Forutsetninger (3C)
- **Competency:** Kjedene må ha (eller bygge) innholdsproduksjons- og tilbudsstyringskompetanse på digital. Konsernet må ha plattformforvaltning.
- **Commitment:** Kjededirektørene må eie sin modul som strategisk verktøy — ikke som konsernpålegg.
- **Coordination:** Hybrid governance — felles plattformregler (data, UI-kjerne, sikkerhet, KPI) sentralt; innhold, tilbud, lokal markedsføring lokalt.

### Implementeringssekvens (teoretisk)
1. **Strategisk avklaring (mnd 0–2):** Kjedene definerer sin distinkte digitale verdi-prop (basert på sin fysiske posisjonering). 365discount = pris/enkelhet; Kvickly = bredde/effektivitet; SuperBrugsen = inspirasjon/kvalitet; Brugsen = lokal/identitet.
2. **Plattform-arkitektur (mnd 1–4):** Lobyco definerer hva som er felles (Scan & Pay, bonus, kundedata, push-infrastruktur) vs. hva som er modul-spesifikt (innhold, tilbudslogikk, gamification-mekanikker, kommunikasjonstone).
3. **Pilot per kjede (mnd 3–9):** Start med én modul (anbefales 365discount, der pris-/tilbudslogikk er klarest). Mål mot KPI-hierarkiet — særlig butikkbesøk og kurv per kjede.
4. **Skalering eller redesign (mnd 9–12+):** Pilotresultater avgjør om modulen skaleres, justeres eller skrotes. KPI-hierarkiet (Anbefaling 1) er forutsetning for å kunne ta denne beslutningen.

### Risikohåndtering
- *Risiko 1:* Kompleksitet eksploderer → felles plattform (én datamodell, ett bonus-system) reduserer dette. Innholdsproduksjon kan delvis sentraliseres som tjeneste til kjedene.
- *Risiko 2:* Kjedene drar i ulike retninger → hybrid governance + felles KPI-mal disiplinerer.
- *Risiko 3:* «Felles plattform» kompromisser kjedespesifikk relevance → kjedene må ha reell modul-frihet innenfor plattformrammen.

### Pensum-knytning
- **Yoo et al. (2010):** Modulær arkitektur er *digital innovation som rekombinasjon* — felles digitale komponenter + kjedespesifikke + fysiske.
- **Lektion 6 — plattform-økosystem:** Felles plattform med moduler er en intern økosystem-arkitektur som gir network effects på medlemsnivå uten å fragmentere data.
- **Tawse & Tabesh (2021):** *Coordination* er den krevende dimensjonen her — konsern, kjeder, Lobyco må synkronisere release-sykluser, datadefinisjoner, governance.

---

## Implementering av Anbefaling 3 — Lobyco & Retail Media som Coop-først-kapabilitet

### Mål
Etablere et formelt styringsregime der Lobyco primært utvikles for å støtte Coops butikk- og medlemsverdi, mens ekstern omsetning (modular-producer-rollen) og retail media er sekundære og bare videreutvikles under eksplisitte krav.

### Forutsetninger (3C)
- **Competency:** Konsernledelsen må ha kapasitet til å evaluere Lobycos faktiske bidrag til butikkøkonomi — krever KPI-hierarkiet på plass.
- **Commitment:** Skov Jørgensen og styret må formelt definere Lobycos mandat som «Coop-først». Ellers risikerer Lobyco å utvikle egne mål.
- **Coordination:** Lobyco-styret, Coop-konsernledelsen og retail media-funksjonen må koordineres rundt felles KPI-er og mandat.

### Implementeringssekvens (teoretisk)
1. **Mandat-avklaring (mnd 0–2):** Skov Jørgensen utsteder formell *Coop-først*-direktiv til Lobyco. Definer hvilken andel av Lobycos kapasitet som er reservert for Coop-leveranser (eksempel fra prosjektet: fast andel).
2. **Lobyco-KPI-rammeverk (mnd 1–4):** Bygg KPI-er som kobler Lobycos arbeid til *Coops* butikkøkonomi (ikke Lobycos egne aktivitetstall). Ekstern omsetning rapporteres separat og evalueres som tilleggsverdi.
3. **Retail media-pilot (mnd 3–9):** Avgrenset pilot med eksplisitte krav: *netto* økt verdi for Coop (leverandørinntekt > kostnad ved redusert kundetillit/relevans). Måle på både inntekt og kundetilfredshet/retensjon.
4. **Beslutningspunkt (mnd 9–12):** Pilotresultater avgjør om retail media videreutvikles, holdes på pilot-skala eller avvikles. Lobycos overordnede strategi revurderes på grunnlag av Coop-bidraget.

### Risikohåndtering
- *Risiko 1:* Strenge rammer svekker Lobycos innovasjonsevne → tillat ekstern omsetning innenfor rammene; ikke kvel modular-producer-potensialet, men subordinér det.
- *Risiko 2:* Retail media reduserer relevance → bygg KPI-er på begge sider (leverandørverdi *og* kundetillit/relevans). Hvis cross-side-effekten blir negativ, krymp retail media.
- *Risiko 3:* Spenningen mellom omnichannel og modular-producer-rollen blir konfliktfylt → eksplisitt mandat fra CEO + styret er forutsetning.

### Pensum-knytning
- **Wessel et al. (2021):** Coop driver ITEOT → Lobyco må styres mot eksisterende identitet. En DT-tolkning ville styrt motsatt — så valget her er *teoridrevet*, ikke vilkårlig.
- **Lektion 6:** Network effects — single-sided er positiv, cross-side via retail media kan bli negativ. KPI-måling må fange begge sider.
- **Christensen:** Lobyco/retail media er sustaining innovation. Ikke disruptiv.
- **Tawse & Tabesh (2021):** Krever alle 3C — *commitment* (mandat fra CEO/styret), *competency* (måle Lobycos Coop-bidrag), *coordination* (mellom Coop og Lobyco).

---

## Tverrgående implementeringsprinsipper

### Hybrid governance
**Sentralt:**
- KPI-hierarkiet og målestandarder
- Felles plattform-arkitektur (Lobyco)
- Lobyco-mandat (Coop-først)
- Retail media-rammeverk og krav

**Lokalt (kjedene):**
- Innhold, tilbud, gamification per kjede
- Kommunikasjonstone og kampanjer
- Operativ butikk-integrasjon

**Hvorfor:** Balanserer DVC-relevance (lokalt) mot DBM-omnichannel-konsistens (sentralt).

### Pilot-først, skalering etter dokumentert effekt
Alle initiativer går gjennom pilot → måling mot KPI-hierarkiet → beslutning.
- Reduserer risiko for legacy debt (Hedman & Bjørn-Andersen-presedensen)
- Gir KPI-rammeverket data å kalibreres mot
- Disiplinerer mot å skalere «på følelse» eller på leverandørrapporterte tall

### Endrings-sekvens på konsernnivå
1. **Anbefaling 1 først.** KPI-hierarkiet er *forutsetning* for at Anbefaling 2 og 3 kan evalueres. Uten det fortsetter Coop å styre på aktivitetstall.
2. **Anbefaling 3 parallelt.** Lobyco-mandat avklares tidlig — det gir KPI-rammeverket den styringsmodellen det skal måle innenfor.
3. **Anbefaling 2 sekvensielt.** Kjedespesifikke moduler piloteres etter at plattform og KPI-rammeverk er etablert. Ellers piloteres moduler uten å kunne måle om de virker.

### Kommunikasjonsstrategi (commitment-bygging)
- Skov Jørgensen kommuniserer reframingen — fra «mer/mindre app» til «styring av app» — som strategisk valg, ikke nedprioritering.
- Kjedene gis eierskap i sine moduler — ikke konsernpålegg.
- Lobyco-ansatte mottar tydelig signal: Coop-først-mandat, men modular-producer-potensial bevares innenfor rammene.

### Måling av implementeringen selv
Implementeringen evalueres på samme prinsipp som anbefalingene: bruksmål (er rammeverket tatt i bruk?), atferdsmål (endrer det beslutninger?) og effektmål (gir det bedre KPI-utvikling i butikk over tid?).

---

## Pensum-knytning: Implementeringsteorien anvendt

| Pensum-konsept | Hvordan det styrer implementeringen |
|---|---|
| **Tawse & Tabesh (2021) — 3C** | Strukturerer hva hver anbefaling krever: competency, commitment, coordination |
| **Hedman & Bjørn-Andersen (2016)** | Advarsel mot legacy debt → pilot-først-prinsipp + KPI-disiplin |
| **Wessel et al. (2021) — ITEOT** | Disiplinerer scope: implementeringen skal styrke eksisterende identitet, ikke skape ny |
| **Porter (1996) — trade-offs** | Implementeringen *velger* hva som ikke skal optimaliseres (aktivitetstall) |
| **Yoo et al. (2010) — rekombinasjon** | Modulær arkitektur er implementeringsuttrykk for digital innovation-prinsippet |
| **Lektion 6 — hybrid governance** | Sentralt/lokalt-split = implementeringens organisasjonsmodell |

---

## Hvis sensor spør: «Hva er det vanskeligste ved implementeringen?»

**Sannsynlig svar:** Den vanskeligste dimensjonen er *commitment* — å holde KPI-hierarkiet og Coop-først-mandatet over tid, særlig når kortsiktige aktivitetstall ser bedre ut enn dokumentert butikkbidrag. Hedman & Bjørn-Andersen viser at Coop historisk har feilet på akkurat denne disiplinen. Det er derfor CEO-eierskap er en forutsetning — ikke en kosmetisk detalj.

## Hvis sensor spør: «Hvor lang tid tar dette?»

**Sannsynlig svar:** KPI-hierarkiet kan etableres på 6–12 måneder. Kjedemoduler piloteres innen ett år og evalueres på 12–18 måneders horisont. Lobyco-mandatet kan settes umiddelbart; pilot av retail media-krav løper 6–12 måneder. Realistisk full omlegging: 18–24 måneder før Coop kan styre etter robuste interne data. Det er en langsiktig styringsreform, ikke et prosjekt.
