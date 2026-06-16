# Muntlig forsvar — Marcus' 5-minutters del: IMPLEMENTERING

> Notat til meg selv: Heller for mye stoff her enn for lite. Velg ut 3–4 hovedpoeng som henger sammen, og hold de andre i bakhånd til Q&A.

---

## 0. Hvorfor implementering er det riktige eget kapittel å eie muntlig

- Sensorvurderingen og deep-research-rapporten peker eksplisitt på at **implementeringsrealismen** er den faktiske svakheten i den skriftlige oppgaven — ikke teorien, ikke strukturen.
- Pensum (Hedman & Bjørn-Andersen, men også Wessel et al.) sier at strategi som ikke kan implementeres, ikke er strategi — den er en ønskeliste.
- Ved å eie implementering muntlig **reparerer jeg den største restrisikoen** i karakteren (7→10/12). Det er her vi enten holder oss på 10 eller drar oss mot 12.
- Det er også her **anbefalingene våre står og faller**: KPI-hierarki, modulær plattform og Lobyco-governance er alle implementeringsavhengige.

---

## 1. Ramme: implementering i en turnaround-i-progresjon (ikke en krise)

**Viktig nyansering basert på regnskapsanalysen 2020–2025:** Coop er ikke i fritt fall — de er i en *turnaround som faktisk virker, men ikke er friskmeldt*. Det er en helt annen implementeringsramme enn "krise".

- **EBITDA snur fra −37 (2024) til +313 mio DKK (2025).** Den underliggende driften er klart bedre. Operasjonell disiplin har akkurat bevist seg.
- **Men EBIT er fortsatt −215 mio DKK** og årsresultat −232. Driften bærer ikke avskrivninger og kapitalbasen ennå.
- **Capex er halvert:** 1.326 (2020) → 575 mio DKK (2025), et fall på 56 %. Det er den faktiske investeringsrammen vi opererer innenfor.
- **Soliditeten faller fra 17,8 % (2024) til 16,2 % (2025).** Kapitalbufferen som ble bygget opp i 2024 spises sakte. Vi har tid, men ikke uendelig.
- **2024 var ikke et rent normalår** — særlige poster +472 og eiendomssalg løftet resultatet. 2025 er en "renere", men svakere måling av kjernedriften.

**Fire strukturelle forhold som former implementeringen:**

1. **Halvert investeringsramme.** Capex 575 mio DKK i 2025. Alle våre anbefalinger konkurrerer om en investeringsbase som er nær halvert siden 2020. Det tvinger frem *sekvensering og piloter*, ikke big bang.
2. **2026-korridoren er smal.** Ledelsen guider omsetningsvekst 1,5–2,5 % og EBIT 0–150 mio DKK for 2026. Enhver implementering må kunne forsvares innenfor denne korridoren — pilotresultater må vises i pp-bevegelser, ikke i ambisiøse løfter.
3. **Teknologisk gjeld (Hedman & Bjørn-Andersen, 2016).** Fragmentert arkitektur, legacy POS, begrenset master data management. Mønsteret er strukturelt — det forsvinner ikke uten investering, og vi ser indirekte spor i at coop.dk ble lukket.
4. **Eierstrukturen (FDB).** Forbrukereid. Radikale endringer (f.eks. Lobyco som ren ekstern plattformspiller) ville krevd legitimitet fra medlemsdemokrati — implementeringen er ikke bare teknisk, men *politisk*.

**Konsekvens for våre tre anbefalinger:** alle tre må kunne *piloteres på én kjede* (helst 365discount eller Kvickly), måles på 6–12 måneder, og leveres innenfor EBIT-korridoren 0–150 mio. Vi rir på en pågående turnaround; vi forstyrrer den ikke.

---

## 1.5 Pensum-rammeverket for hele kapitlet

Implementering trenger sitt eget teoretiske språk — det holder ikke å si "strategien må eksekveres". Jeg bruker fire pensumlinser som diagnoseverktøy gjennom hele kapitlet:

### Linse 1 — Tawse & Tabesh: BASCP som suksessdiagnose

Tawse & Tabesh definerer fem dimensjoner som avgjør om en strategiimplementering lykkes. Dette er *rammeverket* jeg vil bruke til å vise at vi har tenkt gjennom mer enn én dimensjon.

| Dimensjon | Hva det betyr | Hvor det treffer Coop |
|---|---|---|
| **Backing** | I hvilken grad maktpåvirkningsmønstre favoriserer implementeringen | Hvem støtter strategien? CIO/CDO, styre, FDB-medlemmer, kjedeledelser. Backing er ujevnt fordelt — derfor governance-design |
| **Assessability** | I hvilken grad suksess kan måles presist | **Direkte koblet til KPI-hierarkiet (Anbefaling 1).** Vårt design *er* en Assessability-mekanisme |
| **Specificity** | I hvilken grad detaljer er bestemt på forhånd | Vår 18-mnd roadmap + minimumsversjon på 365discount. Høy specificity i pilot, lavere på skalering — *bevisst* |
| **Cultural receptivity** | I hvilken grad organisasjonskulturen støtter implementeringen | Coop er forbrukerkooperativ — kulturen verdsetter medlem, ikke aksjonær. Endring må kobles til den kulturen, ikke kjempe mot den (se Schein nedenfor) |
| **Propitiousness** | I hvilken grad uforutsette eksterne forhold favoriserer implementeringen | 2025-turnarounden *er* propitiousness — momentum og ledelsesoppmerksomhet jobber for oss |

> **Hvis sensor spør "hva er deres implementeringsrammeverk?" — svaret er BASCP.** Hele kapitlet 2–4 nedenfor er strukturert som svar på de fem dimensjonene.

### Linse 2 — Mintzberg: deliberate vs. emergent strategi

Mintzberg skiller mellom *deliberate* (planlagt, sekvensiert) og *emergent* (oppdagelses-basert, justert underveis) strategi. Vår pilot-tilnærming er bevisst en hybrid:
- **Den overordnede retningen er deliberate:** KPI-hierarki → modulær plattform → Lobyco-governance, i den rekkefølgen.
- **Detaljene er emergent:** vi vet ikke hvilke KPI-er som faktisk vil drive butikkbidrag mest — det oppdager vi i pilot på 365discount.

Dette er *forsvaret* mot "hvorfor ikke big bang": fordi vi anerkjenner at organisasjonen ikke vet alt på forhånd. Strategi som ren plan kollapser når den møter virkeligheten — derfor designer vi for læring.

### Linse 3 — Schein & Brown / Johnson et al.: Kulturløken (4 lag)

Den klassiske Schein 3-lags-modellen er for grov for Coop. Schein & Brown (1998), videreført i Johnson et al. (2017, *Exploring Strategy*, s. 171), splitter kulturen i **fire konsentriske lag** — kulturløken. Forskjellen mellom *uttalte verdier* og *faktiske oppfatninger* er kritisk for implementering, fordi det er der retail media og Lobyco-governance bryter eller bekrefter.

| Lag | Definisjon | Coop-spesifikt innhold |
|---|---|---|
| **1. Values** (ytterste) | Formelle og uformelle verdier | Formelle: "medlemmen først", "demokratisk eierskap", "lokalsamfunn", "ansvarlig handel". Uformelle: "vi er ikke som Lidl", "Brugsen er trygg", "Coop tjener ikke penger som vanlige selskap" |
| **2. Beliefs** | Bevisste og ubevisste oppfatninger | Bevisste: "vi forstår våre medlemmer best", "digitalisering må tjene butikken". Ubevisste: at digitalt *støtter* fysisk — det erstatter det aldri; at leverandører er motpart i en marginkamp, ikke en partner i en plattform |
| **3. Behaviours** | Individuell og organisatorisk adferd | Individuell: butikksjefer prioriterer egen kjedeidentitet; medarbeidere ser appen som tillegg, ikke kjerne. Organisatorisk: kjedevise P&L-er, demokratisk eierstyring, koop.dk ble lukket fordi den ikke "passet inn" |
| **4. Paradigm** (kjerne) | Erkjente og uerkjente grunnantakelser | "Coop er vår" — eies av medlemmene. Langsiktig medlemsverdi går foran kortsiktig profitt. Hver kjede har sin egen sjel. Profitt er middel, ikke mål |

**Hvorfor 4 lag og ikke 3 betyr noe for Coop-casen:**

Schein 3-lag ville plassert "medlemmen først" og "vi tjener ikke penger som andre" i samme bøtte (espoused values). Kulturløken skiller dem: det første er en *formell verdi* (lag 1), det andre er en *ubevisst oppfatning* (lag 2). Det skille er gull for implementeringsanalyse, fordi det forklarer hvorfor visse anbefalinger oppleves som forræderi selv om de ikke bryter noen uttalt regel.

### Implementeringsimplikasjoner per lag

- **Lag 1 (Values):** Retail media må kommuniseres som *medlemsverdi* (bedre tilbud, mer relevante kampanjer), ikke som *leverandørinntektsstrøm*. Bryter en ikke verdiene, men kan oppleves slik — og kulturløken sier oppfattelsen er det som betyr noe.
- **Lag 2 (Beliefs):** Vårt IT-Enabled-valg (Wessel) *bekrefter* den ubevisste oppfatningen om at "digitalt støtter fysisk". Det er Backing-mekanisme — vi rir på en eksisterende belief, ikke kjemper mot den. **Det er strategisk smart at vår strategi føles riktig før den argumenteres for.**
- **Lag 3 (Behaviours):** Pilot på 365discount respekterer kjedeautonomi-adferden. Modulær plattform speiler den eksisterende organisatoriske adferden (kjedevise beslutninger), ikke kjemper mot den. Conway's law fungerer i vår favør.
- **Lag 4 (Paradigm):** **Den dypeste risikoen er at retail media kolliderer med paradigmet** om at "Coop tjener medlemmene, ikke leverandørene". Dette er ikke et kommunikasjonsproblem — det er et identitetsproblem som krever paradigm-arbeid (involvering, transparens, NPS-styrt volum). Hvis paradigmet brytes, mister Coop noe som ikke kan kjøpes tilbake.

**Det viktige poenget muntlig:** Vi har designet de tre anbefalingene slik at de *bekrefter* lag 1–3 og *beskytter* lag 4. Det er kulturløken brukt som implementeringsverktøy, ikke bare som analyse.

### Linse 4 — Hedman & Bjørn-Andersen: sosioteknisk perspektiv

IT-strategi er aldri bare teknologi — den implementeres gjennom *samspillet mellom mennesker, prosesser og systemer*. Teknisk gjeld er like mye organisatorisk som teknisk: det er valgene som ikke ble tatt, eierskapet som ikke ble plassert, integrasjonene som ingen prioriterte.

### Hvordan disse fire spiller sammen i forsvaret

- **BASCP** er strukturen.
- **Mintzberg** forsvarer prosessen (pilot, emergent læring).
- **Schein/Brown** håndterer kultur-dimensjonen i BASCP.
- **Hedman/Bjørn-Andersen** binder det hele sammen som sosioteknisk.

Dette gir meg fire teorier å koble eksplisitt til implementeringen, ikke bare DVC + DBM gjenbrukt.

---

## 2. Implementering av Anbefaling 1 — KPI-hierarkiet

Denne er styringsmessig hjertet i strategien vår. Implementeringen har fire lag.

**Pensumkoblinger for dette kapitlet:**
- **BASCP — Assessability:** KPI-hierarkiet *er* Assessability-mekanismen. Uten det kan ikke implementeringen evalueres presist.
- **DVC (Duus & Cooray):** lagene gir strukturen for *hva* KPI-ene skal måle (outputs, set/situational experiences, relevance).
- **DBM (Weill & Woerner):** value creation vs. value capture-skillet gir oss to KPI-kategorier vi må holde fra hverandre.
- **Hedman & Bjørn-Andersen:** datakoblingen er sosioteknisk — like mye organisatorisk som teknisk.

### 2a. Måleinfrastruktur — DVC-lagene som rammeverk

KPI-ene skal *operasjonalisere DVC*. Det gir oss et teoretisk forankret hierarki, ikke en tilfeldig samling tall:

| DVC-lag | KPI-kategori | Konkrete eksempler |
|---|---|---|
| **Outputs (ytre lag)** | Bruksmål | MAU/DAU, sesjonslengde, retensjon |
| **Set & situational experiences (indre lag)** | Atferdsmål | Scan & Pay-bruk, kupong-redemption, bonusbruk |
| **Relevance (kjernen)** | Lønnsomhetsmål | Butikkbidrag per medlem, basket size, kjøpsfrekvens |
| **Evolution-dimensjonen** | Retningsmål | Markedsandel medlem vs. ikke-medlem over tid |

> **Implementeringsutfordringen er ikke å definere KPI-ene — det er å koble dem.** Det er der teknisk gjeld blir konkret: hvis medlemsID ikke følger transaksjonen helt gjennom POS, kan vi ikke regne butikkbidrag per medlem. Dette er Hedman & Bjørn-Andersens sosiotekniske poeng: data-integrasjonen krever både teknisk arbeid (APIer) og organisatorisk arbeid (eierskap, master data governance).

**DBM-skillet operasjonalisert:** *Value creation* måles av bruks- og atferdsmål; *value capture* måles av lønnsomhetsmål. Vi rapporterer dem separat så vi ikke forveksler engasjement med inntjening.

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

### 2c. Marginsensitiviteten gir KPI-hierarkiet sitt operasjonelle språk

Regnskapsanalysen viser at **0,3–0,5 prosentpoeng** i bruttomargin eller kostnadsnivå flytter EBIT med **100–160 mio DKK**.

Det er gull for vårt KPI-hierarki: vi kan og **må** måle appens effekt i prosentpoeng-bevegelser på driftsmotoren, ikke i abstrakte engasjementsmål.

- **Hvis app-styrte kampanjer øker bruttomarginen med 0,3 pp** på den medlems-segmenterte omsetningen → potensielt 100 mio DKK i EBIT-effekt.
- **Hvis Scan & Pay reduserer kasse-bemanningskost med 0,2 pp av omsetningen** → potensielt 65 mio DKK i EBIT-effekt.
- **Hvis Lobyco/retail media bidrar med X kroner per medlem** → må omregnes til pp på driftsmotoren for å være sammenlignbar.

Dette er den skarpeste mulige koblingen mellom DBM (value capture) og operativ målbarhet. Det gir også et naturlig forsvar mot "er ikke dette bare bruksmål?" — nei, vi *forplikter oss* til å måle EBIT-bidrag i pp.

### 2d. Organisatorisk eierskap

- Hvem eier hierarkiet? Forslag: en **felles styringskomité med representanter fra digital, butikkdrift og økonomi**, ledet av en C-level eier (CIO eller CDO).
- Uten klart eierskap blir KPI-hierarkiet til en rapport, ikke en styringsmekanisme. Dette er et klassisk Hedman & Bjørn-Andersen-poeng om at IT-strategi *implementeres gjennom organisatoriske strukturer*, ikke gjennom systemer alene.

### 2e. Sekvensering (realistisk roadmap, 18 mnd)

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

**Pensumkoblinger for dette kapitlet:**
- **BASCP — Specificity:** modulær arkitektur kjøper *både* høy specificity i kjernen (felles API-kontrakter) og lav specificity i moduler (kjedene kan iterere). Det er en bevisst designsplit.
- **DBM:** plattformen forankrer Coop i omnichannel-arketypen ved å øke kundekjennskaps-aksen uten å oppgi kontrollert verdikjede.
- **Mintzberg — konfigurasjoner:** Coop er en *divisjonalisert struktur* (kjedene som divisjoner). Modulær plattform speiler organisasjonsstrukturen i arkitekturen — det er Conway's law brukt strategisk.
- **Mintzberg — emergent strategi:** kjedespesifikke moduler er rom for emergent strategi i en deliberate kjerne.

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

**Pensumkoblinger for dette kapitlet:**
- **BASCP — Backing:** Lobyco-governance handler i bunn og grunn om å sikre at maktpåvirkningsmønstre favoriserer Coops strategiske retning, ikke Lobycos kommersielle bredde.
- **DBM:** vi velger bevisst å holde Lobyco i *modular producer*-rommet, og hindrer drift mot *ecosystem driver* — en eksplisitt arketype-disiplin.
- **Økosystemteori (Lektion 6) + nettverkseffekter:** se 4d.
- **Two-sided market / prinsipal-agent:** retail media skaper en interessekonflikt mellom leverandører og medlemmer som må styres, ikke ignoreres.
- **Porter (5F):** retail media endrer maktbalansen mot leverandører — det er en strukturell endring av bransjekreftene, ikke bare en inntektsstrøm.

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

### 4c. Retail media — to-sidig marked og kundetillit

Retail media er ikke bare en inntektsstrøm — det er et **two-sided market** der Lobyco/Coop er plattformen, leverandørene er den ene siden, og medlemmene er den andre. Den teoretiske implikasjonen:

- **Prinsipal-agent-problem:** leverandørene betaler, men medlemmene er produktet. Det er en klassisk plattformkonflikt som krever *governance*, ikke god intensjon.
- **Porter-perspektivet:** retail media flytter forhandlingsmakt fra leverandører til Coop (Coop kontrollerer hyllen og oppmerksomheten i appen). Det er en strukturell endring av leverandørmakts-kraften i 5F-rammeverket.
- **Implementeringsbeskyttelse av kundetillit:**
  - **Eksplisitte policy-regler** for hvilke kampanjer som tillates (helse, transparens, ingen «dark patterns»).
  - **Måling av kundetillit:** NPS-segmentert på app-brukere vs. ikke-brukere, attityde-undersøkelser, churn-rate på medlemskap.
  - Hvis NPS faller på en definert terskel, **bremses retail media-volumet** automatisk. Dette er en konkret governance-mekanisme, ikke en intensjon.

### 4d. Plattform- og økosystemperspektivet (Lektion 6)

Lobyco har latent plattformpotensial: nettverkseffekter virker hvis flere kjeder kobles på (cross-side: flere leverandører → mer attraktivt for medlemmene → mer data → mer attraktivt for leverandører).

**Hvorfor vi *ikke* anbefaler å hoppe på den dynamikken:**

- Full ecosystem driver-rolle ville krevd at Coop oppga datakontroll og governance-makt — det er det motsatte av strategien vår.
- Nettverkseffektene ville også jobbet for *konkurrentene*: hvis Lobyco vokser eksternt, blir den teknologiske fordelen tilgjengelig for Lidl/Netto til samme pris som for Coop.
- Vi velger derfor å *kappe nettverkseffekten med vilje* der den ville eroderet Coops informasjonsasymmetri — dette er kostnaden ved omnichannel-disiplinen.

**Det autoritative svaret muntlig:** "Vi ser plattformpotensialet, og vi avviser det bevisst. Det er en strategisk avveiing mellom plattformverdi og kontroll — ikke et oversett alternativ."

---

## 5. Wessel et al. + Christensen — IT-Enabled som *implementerings-rammeverk*

Sentralt grep: bruk Wessel til å forklare hvorfor *implementeringsmodusen* er annerledes enn ved Digital Transformation.

- **IT-Enabled:** ny teknologi støtter eksisterende value proposition. Implementering = trinnvis, integrert i eksisterende organisasjon, KPI-er knyttet til kjernevirksomhet.
- **Digital Transformation:** ny value proposition. Implementering = separat enhet (skunkworks), nye KPI-er, ofte ny ledelse.

> **Coop er bevisst på IT-Enabled-sporet.** Det er *derfor* vi anbefaler integrert governance (anbefaling 1), modulær arkitektur knyttet til butikk (anbefaling 2) og Coop-først for Lobyco (anbefaling 3).

> Hvis Coop hadde gått for DT, ville implementeringen sett helt annerledes ut: Lobyco skilles ut som egen enhet med egne KPI-er, retail media blir hovedforretning, butikkene blir distribusjon. **Det er ikke det vi anbefaler — og det er et bevisst valg.**

Dette gir oss et autoritativt språk for å si: «vi vet det finnes en alternativ implementeringssti, og vi har vurdert og avvist den.»

**Christensen-kobling:** Coop App er en *sustaining-innovasjon* — den forsterker eksisterende verdiløfte (god, lokal dagligvarehandel), den endrer det ikke. Det er en naturlig forklaring på *hvorfor* IT-Enabled er riktig modus: sustaining-innovasjoner implementeres best integrert i hovedorganisasjonen, mens disruptive innovasjoner krever separasjon. Vi velger struktur etter innovasjonstype.

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

## 7. Organisasjonskultur, endringsledelse og motkrefter — Kulturløken og BASCP

Dette er kulturelle motkrefter sett gjennom Schein & Brown / Johnson et al. sin kulturløk og BASCPs Cultural receptivity-dimensjon.

### 7a. Coops kultur i kulturløkens fire lag

> Modellen er Schein & Brown (1998), videreført i Johnson et al. (2017, *Exploring Strategy*, s. 171). Fire konsentriske lag — fra ytterste *values* til kjerne *paradigm*.

**Lag 1 — Values (formelle og uformelle verdier)**
- *Formelle:* "medlemmen først", "demokratisk eierskap", "bæredyktighet", "lokalt forankret".
- *Uformelle:* "vi er ikke som Lidl", "Brugsen er trygg", "vi tar vare på lokalsamfunnene".
- **Implementeringsimplikasjon:** Retail media kan ikke selges som "ny inntektsstrøm" — det må rammes som "mer relevante tilbud for medlemmene". Hvis vi snubler i kommunikasjonen, treffer vi formelle verdier feil.

**Lag 2 — Beliefs (bevisste og ubevisste oppfatninger)**
- *Bevisste:* "vi forstår våre medlemmer best", "digitalisering må tjene butikken".
- *Ubevisste:* at digitalt *støtter* fysisk — det erstatter det aldri; at leverandører er motpart i marginkamp.
- **Implementeringsimplikasjon:** Vårt IT-Enabled-valg (Wessel) *bekrefter* den ubevisste oppfatningen. Strategien føles riktig før den argumenteres for — det er stillas under Backing.

**Lag 3 — Behaviours (individuell og organisatorisk adferd)**
- *Individuell:* butikksjefer prioriterer egen kjedeidentitet; medarbeidere ser appen som tillegg.
- *Organisatorisk:* kjedevise P&L-er, demokratisk eierstyring, coop.dk ble lukket fordi den ikke "passet" inn i adferdsmønsteret.
- **Implementeringsimplikasjon:** Pilot på 365discount og kjedespesifikke moduler speiler eksisterende adferd. Vi designer ikke om organisasjonen — vi følger den.

**Lag 4 — Paradigm (erkjente og uerkjente grunnantakelser)**
- "Coop er vår" — eies av medlemmene.
- Langsiktig medlemsverdi går foran kortsiktig profitt.
- Hver kjede har sin egen sjel.
- Profitt er middel, ikke mål.
- **Implementeringsimplikasjon:** **Den dypeste risikoen** er at retail media kolliderer med paradigmet om medlemmen-først. Bryter vi paradigmet, mister Coop noe som ikke kan kjøpes tilbake. NPS-styrt volum og transparens er paradigm-beskyttelse, ikke PR.

### 7b. Hvorfor kulturløken er overlegen Schein 3-lag for Coop

Den klassiske 3-lags-modellen ville samlet både "medlemmen først" (formell verdi) og "Coop tjener ikke penger som andre" (ubevisst oppfatning) i samme bøtte (espoused values). Det skjuler den viktigste implementeringsfaren: at en anbefaling kan være *konsistent med formelle verdier* og samtidig *kollidere med ubevisste oppfatninger*.

Retail media er nettopp et slikt tilfelle: ingen verdi-erklæring sier at "vi ikke skal samarbeide kommersielt med leverandører", men den ubevisste oppfatningen om at "leverandører er motpart" gjør at retail media kan oppleves som forræderi internt — *uten at noen kan peke på regelen som ble brutt*.

**Det er denne typen subtil kulturanalyse muntlig forsvar vinner karakter på.**

### 7c. Brown utfyller — kultur som muliggjører OG barriere

Brown's bidrag (gjennom Johnson et al.): kultur er ikke statisk verken muliggjører eller barriere — det er begge deler samtidig, avhengig av hva som foreslås.

- Den samme medlem-først-kulturen som *blokkerer* aggressiv retail media er den som *legitimerer* KPI-hierarkiet (vi måler hvordan vi tjener medlemmen bedre).
- Den samme kjedeautonomi-adferden som *forhindrer* en sentral app er den som *muliggjør* modulær plattform (kjedene får eierskap til sine moduler).
- **Strategisk implementeringsgrep:** vi designer hver anbefaling så den treffer kulturens muliggjørende side, ikke dens blokkerende side.

### 7d. Motkrefter og hvordan kulturløken forklarer dem

- **Butikkledere** opplever app-KPI-er som maktforskyvning fra butikknivå (lag 3 behaviours, lag 4 paradigm om butikkautonomi). **Kulturelt grep:** ramme KPI-ene som *støtte*, ikke *kontroll*. Inviter butikkledere inn i pilotutformingen — det respekterer behaviours-laget.
- **Kjedeledelser** motsetter seg felles plattform fordi den truer kjedeidentitet (lag 4 paradigm). Modulær plattform er ikke tilfeldig kjedespesifikk — den er designet rundt paradigmet, ikke mot det.
- **Lobycos ledelse** har egne kommersielle mål — løses gjennom eierstruktur og styresammensetning. Dette er BASCPs Backing-dimensjon, ikke kulturarbeid.
- **Medlemmene (FDB-eiere)** kan motsette seg retail media som *paradigm-brudd* — løses gjennom transparens og NPS-styrte volummekanismer. Dette er paradigm-beskyttelse i konkret form.

### 7e. Pensumets samlede budskap

- **Hedman & Bjørn-Andersen:** IT-strategi er sosioteknisk — teknologi + organisasjon + mennesker som ett system.
- **Schein & Brown / Johnson et al. (kulturløken):** kultur er ikke bare "soft stuff" — den avgjør om strategien lykkes eller blir vraket av paradigm-kollisjoner ingen kan peke konkret på.
- **BASCP — Cultural receptivity** er den dimensjonen som oftest blir oversett i strategiimplementering, ifølge Tawse & Tabesh. Vi har tenkt på den i fire lag, ikke ett, og vi har designet anbefalingene for å treffe hvert lag bevisst.

---

## 8. Hva jeg *ikke* skal si (hold disse i bakhånd)

- Ikke gå dypt i konkrete kostnadstall — vi har ikke evidens, og det blir gjettet.
- Ikke love perfekt kausalitet i KPI-målingen.
- Ikke kall Coop App «transformativ» — det åpner Wessel-fellen.
- Ikke ignorer at en del av implementeringen er **å betale ned teknisk gjeld før vi kan høste**.

---

## 9. Forslag til struktur for de 5 minuttene

Hvis jeg må velge, vekt slik:

| Minutt | Tema | Pensumkobling |
|---|---|---|
| 0:00–0:45 | Rammen: implementering er der strategien står og faller. Introduser BASCP som linsen | Tawse & Tabesh — gir kapitlet et eksplisitt rammeverk |
| 0:45–2:00 | KPI-hierarkiet (Assessability) — DVC-lagene som struktur, marginsensitiviteten som mål | DVC + DBM + Hedman |
| 2:00–3:15 | Pilot-tilnærmingen som *deliberate + emergent* hybrid. Hvorfor big bang er feil | Mintzberg + Hedman (teknisk gjeld som forutsetning) |
| 3:15–4:15 | Kultur (Cultural receptivity): hvorfor anbefalingene er designet for å treffe Coops kulturlag, ikke kjempe mot dem | Schein + Brown + BASCP |
| 4:15–5:00 | Wessel + Christensen — IT-Enabled som bevisst implementeringsmodus. Lukker autoritativt | Wessel + Christensen |

**Alternativ åpning (mer dristig):** Start med spenningen *omnichannel ↔ modular producer* i Lobyco og bruk implementering (governance, eierstruktur, SLA) som *løsningen* på den teoretiske spenningen. Treffer hjertet i den største analytiske svakheten i rapporten — men risikabelt fordi det inviterer hardt motspørsmål.

**Den røde tråden muntlig:** "BASCP gir oss fem dimensjoner. Vi har designet for hver av dem — ikke bare for målbarheten."

---

## 10. Setninger jeg vil huske å si

1. «Vi bruker Tawse & Tabesh sitt BASCP-rammeverk som diagnose: Backing, Assessability, Specificity, Cultural receptivity, Propitiousness. Hver av våre anbefalinger er designet for å treffe minst én av dimensjonene eksplisitt.»
2. «Coop er ikke i krise — de er i en turnaround som faktisk virker. EBITDA snur fra −37 til +313 mio DKK i 2025. Vår implementering rir på den bølgen — det er Propitiousness.»
3. «Marginsensitiviteten gir oss et felles språk: 0,3–0,5 pp i bruttomargin eller kost = 100–160 mio EBIT. Det er der KPI-hierarkiet vårt måles — det er Assessability operasjonalisert gjennom DVCs relevance-lag.»
4. «Mintzberg gir oss forsvaret for pilot-tilnærmingen: vi designer for både deliberate retning og emergent læring. Det er ikke forsiktighet, det er epistemisk realisme.»
5. «Anbefaling 2 (modulær plattform) er ikke tilfeldig kjedespesifikk — den speiler Coops divisjonaliserte struktur og treffer Scheins artefakt-lag, der kjedeidentitet bor.»
6. «Vi løser ikke modular producer-spenningen retorisk — vi løser den strukturelt, gjennom governance over data og kapasitet. Det er BASCPs Backing-dimensjon.»
7. «Hvis vi hadde valgt Digital Transformation som modus (Wessel), ville implementeringen sett helt annerledes ut. Coop App er sustaining (Christensen) — vi har valgt IT-Enabled bevisst, og det former hver av de tre anbefalingene.»

---

## 11. Forventede oppfølgningsspørsmål jeg må kunne svare på

| Spørsmål | Kort svar |
|---|---|
| Hva koster dette? | Pilot på 365discount er begrenset (anslagsvis 8–12 mnd team-innsats). Full utrulling forutsetter teknisk gjeld-investering vi ikke har tallfestet — det er en åpen kostnad vi flagger transparent. |
| Hva er realistisk leveranse i 2026? | Ledelsen guider EBIT 0–150 mio DKK for 2026. Implementeringsinitiativene må passe innenfor denne korridoren — pilotresultater må kunne dokumenteres i pp-bevegelser på bruttomargin eller kostnadsnivå (0,3–0,5 pp ≈ 100–160 mio EBIT). Alt over er ikke kredibelt. |
| Konkurrerer dere ikke med en investeringsramme som allerede er halvert? | Jo, og det er nettopp derfor pilot-tilnærmingen er riktig. Capex har falt fra 1.326 (2020) til 575 mio DKK (2025). Vi kan ikke be om en kapex-økning vi ikke har dekning for — vi må vinne ressursene gjennom å bevise pp-effekt i pilot. |
| Hvem eier implementeringen? | En styringskomité ledet av CIO/CDO, med butikk-, økonomi- og digital-representasjon. Lobyco har egen styrelinje. |
| Hva hvis pilotering på 365discount feiler? | Da har vi spart full utrulling. Det er hele poenget med sekvensering — vi kjøper informasjon billig før vi forplikter oss. |
| Er ikke dette bare «kjør forsiktig»? | Nei. Det er et bevisst valg om IT-Enabled implementeringsmodus fordi Coops økonomi og struktur ikke tillater DT-modus. Forsiktighet her er strategisk, ikke fryktbasert. |
| Hvorfor ikke bare kjøpe en standardplattform? | Fordi kjernen i anbefaling 2 er at relevans varierer mellom kjeder. Standardplattform ville gitt motsatt effekt: lavere kompleksitet, men også lavere differensiering. Vi velger bevisst mer kompleks vei. |

---

*Sist oppdatert: 2026-06-16*
