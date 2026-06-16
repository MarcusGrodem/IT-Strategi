# Muntlig forsvar — Marcus' 5-minutters del: IMPLEMENTERING

> Notat til meg selv: Heller for mye stoff her enn for lite. Velg ut 3–4 hovedpoeng som henger sammen, og hold de andre i bakhånd til Q&A.

---

## 0. Hvorfor implementering er det riktige eget kapittel å eie muntlig

- Sensorvurderingen og deep-research-rapporten peker eksplisitt på at **implementeringsrealismen** er den faktiske svakheten i den skriftlige oppgaven — ikke teorien, ikke strukturen.
- Pensum (Hedman & Bjørn-Andersen, men også Wessel et al.) sier at strategi som ikke kan implementeres, ikke er strategi — den er en ønskeliste.
- Ved å eie implementering muntlig **reparerer jeg den største restrisikoen** i karakteren (7→10/12). Det er her vi enten holder oss på 10 eller drar oss mot 12.
- Det er også her **anbefalingene våre står og faller**: KPI-hierarki, modulær plattform og Lobyco-governance er alle implementeringsavhengige.

---

## 1. Ramme: hvorfor implementering er vanskelig akkurat for Coop

Tre strukturelle forhold som tvinger implementeringen til å være pragmatisk, ikke ambisiøs:

1. **Økonomisk press.** Underskudd på 232 mio DKK og omsetningsfall 1,0 mia kr (oppgavens tallgrunnlag). Hver implementeringskrone konkurrerer med et nedskaleringspress. Dette betyr at *sekvensering* og *piloter* er viktigere enn store omlegginger.
2. **Teknologisk gjeld (Hedman & Bjørn-Andersen, 2016).** Coop har historisk hatt en fragmentert IT-arkitektur med legacy POS-systemer, kjedespesifikke stacker og begrenset master data management. Selv om kilden er fra 2016, er **mønsteret av teknisk gjeld i dagligvare strukturelt** — det forsvinner ikke uten investering, og vi ser indirekte spor i at coop.dk ble lukket (kompleksitet ble for dyr å vedlikeholde).
3. **Eierstrukturen.** Coop er forbrukereid (FDB). Det betyr at radikale endringer (f.eks. å gjøre Lobyco til en ren ekstern plattformspiller) ville krevd legitimitet fra medlemsdemokrati — implementeringen er ikke bare teknisk og organisatorisk, men *politisk*.

**Konsekvens for våre tre anbefalinger:** alle tre må kunne *piloteres på én kjede* (helst 365discount eller Kvickly), måles på 6–12 måneder, og skaleres bevisst. Big bang er ikke på bordet.

---

## 2. Implementering av Anbefaling 1 — KPI-hierarkiet

Denne er styringsmessig hjertet i strategien vår. Implementeringen har fire lag:

### 2a. Måleinfrastruktur — hva må finnes?

- **Bruksmål:** MAU/DAU, sesjonslengde, retensjon. Allerede tilgjengelig fra appen.
- **Atferdsmål:** Scan & Pay-bruk, kupong-redemption, bonusbruk. Krever kobling app ↔ POS, som er der teknisk gjeld ofte sitter.
- **Lønnsomhetsmål:** Butikkbidrag per medlem, basket size, kjøpsfrekvens — krever kobling mellom app, medlem og kasse i samme datamodell.

> **Implementeringsutfordringen er ikke å definere KPI-ene — det er å koble dem.** Det er der teknisk gjeld blir konkret: hvis medlemsID ikke følger transaksjonen helt gjennom POS, kan vi ikke regne butikkbidrag per medlem.

### 2b. Attribusjonsproblemet (det vanskeligste muntlige spørsmålet)

Sensor *vil* spørre: «Hvordan skiller dere appens effekt fra effekten av pris, vareplassering, kampanjer, vær og butikkleders dyktighet?»

**Svar (12-nivå):**
- Vi krever ikke perfekt kausalitet — det er ikke realistisk i en operativ kontekst.
- Vi bruker en **kombinasjon av kvasi-eksperimentelle design**:
  - Geografisk A/B på medlemmer (segmentkohorter med vs. uten push-kampanjer)
  - Før/etter-design på utrulling av nye app-funksjoner per kjede
  - Difference-in-differences mot kontrollkohorter av ikke-aktive medlemmer
- Vi måler **inkrementell effekt**, ikke total effekt. Det vi ikke kan kontrollere for, defineres som usikkerhet og rapporteres åpent.
- Dette er konsistent med pensums understreking av at strategi krever **monitorering og tilpasning**, ikke perfekt evidens.

### 2c. Organisatorisk eierskap

- Hvem eier hierarkiet? Forslag: en **felles styringskomité med representanter fra digital, butikkdrift og økonomi**, ledet av en C-level eier (CIO eller CDO).
- Uten klart eierskap blir KPI-hierarkiet til en rapport, ikke en styringsmekanisme. Dette er et klassisk Hedman & Bjørn-Andersen-poeng om at IT-strategi *implementeres gjennom organisatoriske strukturer*, ikke gjennom systemer alene.

### 2d. Sekvensering (realistisk roadmap, 18 mnd)

| Fase | Måneder | Innhold | Kostnad/risiko |
|---|---|---|---|
| 1 | 0–3 | Definer KPI-er, kartlegg datatilgang, identifiser gap | Lav |
| 2 | 3–9 | Bygg datapipeline app↔POS for én kjede (pilot, 365discount) | Middels — her sitter teknisk gjeld |
| 3 | 9–12 | Etabler styringskomité og rapporteringskadens | Lav teknisk, høy politisk |
| 4 | 12–18 | Skaler til alle kjeder + Lobyco | Høy hvis pilot ikke har avdekket integrasjonsproblemer |

**Minimumsversjon (hvis Skov Jørgensen sier "det er for dyrt"):** Pilot på 365discount med 3 KPI-er (MAU, basket size for app-brukere, butikkbidrag) i 6 måneder. Bevis verdi, så skaler.

---

## 3. Implementering av Anbefaling 2 — Modulær plattform med kjedespesifikke moduler

Den teoretisk svakeste anbefalingen — og dermed implementeringen må være ekstra konkret muntlig.

### 3a. Hva er forskjellen fra dagens personalisering?

- Personalisering i dag: én app, ulike *visninger* per kjedeprofil.
- Modulær plattform: én **kjernearkitektur** (auth, betaling, medlem, lojalitet), pluss **kjedespesifikke moduler** (Kvicklys oppskriftsmodul, 365discounts prisfokus-modul, Brugsens lokalsamfunnsmodul).
- Forskjellen er **arkitektonisk**, ikke kosmetisk: hver kjede kan utvikle og iterere sin modul uavhengig, uten å vente på koordinert release på tvers.

### 3b. Hvordan dette adresserer coop.dk-lukkingen

> **Dette er det skarpeste angrepet sensor kan komme med.** Jeg må eie svaret.

- Coop.dk feilet fordi *hele* den digitale kanalen var separat — egen logistikk, egen prisstruktur, egen kundereise. Det var en parallell virksomhet med lavere marginer.
- Modulær plattform er det **motsatte**: det er én delt infrastruktur som *forsterker fysisk butikk*. Komplexiteten er konsentrert i kjernen, ikke duplisert i kanalene.
- Det vi lærte av coop.dk er at *separat digital kanal* er dyrt. Det vi foreslår er *integrert digital støtte* med kjedespesifikk relevans.

### 3c. Governance for modulutvikling

- **Felles plattform-team** eier kjernen og setter API-kontrakter.
- **Kjedespesifikke produktteam** eier sine moduler under sine kjede-P&L.
- **Konflikthåndtering:** hvis to kjeder vil ha motstridende endringer i kjernen, prioriteres etter felles strategiske KPI-er (anbefaling 1!).

### 3d. Risikohåndtering

- Risiko 1: kostnadsoverskridelse → motvirkes ved pilot på én modul, ikke alle samtidig.
- Risiko 2: modulwildwuchs (hver kjede bygger sitt) → motvirkes av streng plattform-governance og delt designsystem.
- Risiko 3: tap av nettverksverdi (jo mer kjedespesifikt, jo mindre cross-kjede insikt) → erkjenn og aksepter trade-off.

---

## 4. Implementering av Anbefaling 3 — Lobyco-governance (Coop-først)

Den mest *politiske* implementeringsutfordringen, ikke den mest tekniske.

### 4a. Governance-mekanismer (konkret)

- **Eierskapsstrukturen** må klargjøres: hvor stor andel eier Coop direkte? Hva er prinsipalmål?
- **Styresammensetning:** Coop-representanter må ha vetomakt i strategiske spørsmål (roadmap-prioritering, datatilgang, retail media-policy).
- **SLA og prioritet:** kontraktsfestet at X % av utviklingskapasiteten i Lobyco reserveres til Coop-roadmap, uavhengig av eksterne kunder.
- **Datakontroll:** medlemsdata fra Coop forblir Coops; Lobyco kan bruke aggregerte/anonymiserte signaler.

### 4b. Den modulære producer-spenningen — implementeringssvar

Den åpenbare innvendingen: «modular producers tjener på bredde — Coop-først tar bort fundamentet for Lobycos egen verdiskaping.»

**Implementeringssvar (12-nivå):**
- Vi løser ikke spenningen retorisk — vi løser den **strukturelt**: Lobyco kan tjene eksterne kjeder *teknisk*, men Coops *bruksdata, kampanjelogikk og leverandørrelasjoner* fôrer ikke konkurrentene.
- Det betyr at modular-producer-økonomien beholdes (skalafordeler i utvikling, support, kostnadsbase), men *informasjonsasymmetrien* beskyttes.
- Dette er en governance-arkitektur, ikke en strategisk innskrenkning.

### 4c. Retail media — implementeringen som beskytter kundetillit

- Behov: **eksplisitte policy-regler** for hvilke kampanjer som tillates (helse, transparens, ingen «dark patterns»).
- **Måling av kundetillit:** NPS-segmentert på app-brukere vs. ikke-brukere, attityde-undersøkelser, churn-rate på medlemskap.
- Hvis NPS faller på en definert terskel, **bremses retail media-volumet** automatisk. Dette er en konkret governance-mekanisme, ikke en intensjon.

---

## 5. Wessel et al. — IT-Enabled Transformation som *implementerings-rammeverk*

Sentralt grep: bruk Wessel til å forklare hvorfor *implementeringsmodusen* er annerledes enn ved Digital Transformation.

- **IT-Enabled:** ny teknologi støtter eksisterende value proposition. Implementering = trinnvis, integrert i eksisterende organisasjon, KPI-er knyttet til kjernevirksomhet.
- **Digital Transformation:** ny value proposition. Implementering = separat enhet (skunkworks), nye KPI-er, ofte ny ledelse.

> **Coop er bevisst på IT-Enabled-sporet.** Det er *derfor* vi anbefaler integrert governance (anbefaling 1), modulær arkitektur knyttet til butikk (anbefaling 2) og Coop-først for Lobyco (anbefaling 3).

> Hvis Coop hadde gått for DT, ville implementeringen sett helt annerledes ut: Lobyco skilles ut som egen enhet med egne KPI-er, retail media blir hovedforretning, butikkene blir distribusjon. **Det er ikke det vi anbefaler — og det er et bevisst valg.**

Dette gir oss et autoritativt språk for å si: «vi vet det finnes en alternativ implementeringssti, og vi har vurdert og avvist den.»

---

## 6. Hedman & Bjørn-Andersen — teknisk gjeld konkretisert

Hva jeg vil ha klart hvis sensor presser på teknisk gjeld:

**Definisjon:** Teknisk gjeld er den akkumulerte kostnaden av kortsiktige valg som gjør fremtidige endringer dyrere.

**Konkrete tegn i Coop-konteksten:**
- Legacy POS som ikke gir sann tilgang til transaksjon på medlems-nivå
- Master data management uten felles produktkode på tvers av kjeder
- Mangel på standardiserte APIer mellom Lobyco og Coops bakomliggende systemer
- Begrenset event-streaming-infrastruktur som gjør sanntids-personalisering kostbar

**Hvorfor det matter for våre anbefalinger:**
- Anbefaling 1 (KPI-hierarki) **forutsetter** at vi kan koble app-bruk til butikk-økonomi → krever datainvestering først.
- Anbefaling 2 (modulær plattform) **forutsetter** API-modenhet i kjernen → en del av implementeringen er faktisk å betale ned teknisk gjeld i selve grunnstrukturen.
- Anbefaling 3 (Lobyco-governance) er mindre eksponert teknisk, men forutsetter klare integrasjonspunkter.

**Erkjennelse jeg vil legge åpent på bordet:** «Et stort implementeringsarbeid er å rydde i teknisk gjeld før strategien kan eksekveres. Det er noe av kostnaden vi ikke har tallfestet, men som vi flagger som forutsetning.»

---

## 7. Endringsledelse og motkrefter (kort)

- **Butikkledere** kan oppleve at app-styrte KPI-er flytter makt fra butikknivå til hovedkvarter — motstand må håndteres med involvering, ikke pålegg.
- **Kjedeledelser** kan motsette seg felles plattform fordi det reduserer deres autonomi — løses med kjedespesifikke moduler (= anbefaling 2 er også organisatorisk smør).
- **Lobycos ledelse** har egne kommersielle mål — løses gjennom eierstruktur, ikke ved retorikk.
- **Medlemmene (FDB-eiere)** kan motsette seg retail media hvis kundetillit svekkes — løses gjennom transparens og NPS-styrte volummekanismer.

Pensumkoblingen: implementering av IT-strategi er **sosioteknisk**, ikke ren teknologi. Dette er Hedman & Bjørn-Andersens hovedargument.

---

## 8. Hva jeg *ikke* skal si (hold disse i bakhånd)

- Ikke gå dypt i konkrete kostnadstall — vi har ikke evidens, og det blir gjettet.
- Ikke love perfekt kausalitet i KPI-målingen.
- Ikke kall Coop App «transformativ» — det åpner Wessel-fellen.
- Ikke ignorer at en del av implementeringen er **å betale ned teknisk gjeld før vi kan høste**.

---

## 9. Forslag til struktur for de 5 minuttene

Hvis jeg må velge, vekt slik:

| Minutt | Tema | Hvorfor |
|---|---|---|
| 0:00–0:45 | Rammen: implementering er der strategien står og faller, og der vi er mest eksponert | Setter agendaen, viser modenhet |
| 0:45–2:00 | Implementering av KPI-hierarkiet — inkl. attribusjonsproblemet og pilot på 365discount | Sterkeste anbefaling, sterkeste teoritilknytning |
| 2:00–3:15 | Teknisk gjeld (Hedman) som forutsetning — konkret om datainfrastruktur og API-modenhet | Reparerer rapportens største svakhet, demonstrerer pensumbredde |
| 3:15–4:15 | Wessel — vårt valg av IT-Enabled implementeringsmodus, og hvordan det former anbefaling 2 og 3 | Demonstrerer pensumbredde + autoritativ stemme |
| 4:15–5:00 | Sekvensering og governance i sum: 6–12–18 mnd, pilot → skalering, organisatorisk eierskap | Lukker sirkelen, viser realisme |

**Alternativ åpning (mer dristig):** Start med spenningen *omnichannel ↔ modular producer* i Lobyco og bruk implementering (governance, eierstruktur, SLA) som *løsningen* på den teoretiske spenningen. Treffer hjertet i den største analytiske svakheten i rapporten — men risikabelt fordi det inviterer hardt motspørsmål.

---

## 10. Tre setninger jeg vil huske å si

1. «Vår implementeringssti er bevisst trinnvis: pilot → mål → skaler, fordi økonomien tvinger frem realisme og fordi teknisk gjeld må håndteres parallelt.»
2. «Vi løser ikke modular producer-spenningen retorisk — vi løser den strukturelt, gjennom governance over data og kapasitet.»
3. «Hvis vi hadde valgt Digital Transformation som modus (Wessel), ville implementeringen sett helt annerledes ut. Vi har valgt IT-Enabled bevisst — og det former hver av de tre anbefalingene.»

---

## 11. Forventede oppfølgningsspørsmål jeg må kunne svare på

| Spørsmål | Kort svar |
|---|---|
| Hva koster dette? | Pilot på 365discount er begrenset (anslagsvis 8–12 mnd team-innsats). Full utrulling forutsetter teknisk gjeld-investering vi ikke har tallfestet — det er en åpen kostnad vi flagger transparent. |
| Hvem eier implementeringen? | En styringskomité ledet av CIO/CDO, med butikk-, økonomi- og digital-representasjon. Lobyco har egen styrelinje. |
| Hva hvis pilotering på 365discount feiler? | Da har vi spart full utrulling. Det er hele poenget med sekvensering — vi kjøper informasjon billig før vi forplikter oss. |
| Er ikke dette bare «kjør forsiktig»? | Nei. Det er et bevisst valg om IT-Enabled implementeringsmodus fordi Coops økonomi og struktur ikke tillater DT-modus. Forsiktighet her er strategisk, ikke fryktbasert. |
| Hvorfor ikke bare kjøpe en standardplattform? | Fordi kjernen i anbefaling 2 er at relevans varierer mellom kjeder. Standardplattform ville gitt motsatt effekt: lavere kompleksitet, men også lavere differensiering. Vi velger bevisst mer kompleks vei. |

---

*Sist oppdatert: 2026-06-16*
