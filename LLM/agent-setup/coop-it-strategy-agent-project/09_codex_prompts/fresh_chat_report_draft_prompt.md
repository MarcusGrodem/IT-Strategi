# Prompt - Fresh Chat Som Skal Skrive Rapportutkast

Bruk denne prompten i en ny/fresh LLM-chat som skal begynne å skrive videre på rapportutkastet. Prompten er laget for at den nye chatten skal bruke agentmodellen, lese prosjektgrunnlaget og skrive på norsk.

```markdown
Du skal hjelpe meg å skrive et akademisk rapportutkast til en IT-strategioppgave om Coop Danmark, Coop App og Lobyco.

VIKTIG SPRÅKKRAV:

- All output skal være på norsk.
- Rapportutkastet skal skrives på norsk.
- Alle forklaringer, mellomnotater, overskrifter, tabeller og anbefalinger skal være på norsk.
- Ikke skriv på engelsk eller dansk med mindre du siterer en tittel, et navn, et begrep eller en kilde.

VIKTIG ARBEIDSFORM:

- Du starter i et eksisterende repo/prosjektgrunnlag.
- Ikke begynn fra blanke ark.
- Ikke velg ny caseperson, ny teori, ny strategisk stance eller nye anbefalinger.
- De sentrale valgene er allerede låst og skal brukes.
- Bruk agentmodellen som prosjektet har satt opp.
- Skriv litt om gangen, men skriv faktisk rapporttekst, ikke bare plan.

## 1. Start Med Å Lese Disse Filene

Les disse filene først, i denne rekkefølgen:

1. `README.md`
2. `00_project_brief.md`
3. `01_decision_board.md`
4. `02_decision_register.md`
5. `10_project_context/workflow_decision_policy.md`
6. `10_project_context/agent_usage_guide.md`
7. `03_daily_logs/2026-05-04.md`
8. `08_final_report/outline.md`
9. `08_final_report/draft_v1.md`
10. `07_recommendations/chosen_recommendations.md`
11. `07_recommendations/chosen_recommendations_red_team.md`
12. `06_analysis/theory_application_plan.md`
13. `06_analysis/strategic_situation_analysis.md`
14. `05_evidence/source_verification_packet.md`
15. `05_evidence/key_numbers.md`
16. `05_evidence/source_criticism.md`
17. `05_evidence/claim_reliability_matrix.md`
18. `05_evidence/coop_business_model_evidence.md`
19. `05_evidence/competitor_evidence.md`

Hvis en fil mangler, noter det kort på norsk og fortsett med de filene som finnes.

## 2. Låste Prosjektvalg

Du skal bruke disse valgene:

- Rådgivningsaktør: Martin Hasgard Olesen, Direktør for Kommunikation, Marketing og Digital.
- Teorier/perspektiver: DVC Framework + Digital Business Model-perspektivet.
- Strategisk stance: hybrid governance.
- Rapportens hovedlogikk: Først analyser Coops strategiske situasjon; deretter gi 2-5 anbefalinger i forlengelse av analysen.
- Valgte anbefalinger:
  1. Redefiner Coop App-suksess rundt forretningsmodell-fit og butikkverdi.
  2. Utvikle kjedespesifikke app-value propositions innenfor én styrt Coop-plattform.
  3. Gjennomgå og redesign gamification-/engagement-funksjoner hvis de ikke viser kunde- eller butikkverdi.
  4. Bruk Coop App til å styrke medlemsrelasjonen, men skill lojalitet fra lønnsomhet.
  5. Pilotér kjedenivå-initiativer før større appinvesteringer skaleres.

Ikke endre disse valgene med mindre brukeren eksplisitt ber deg om det.

## 3. Bruk Agentmodellen Aktivt

Du skal eksplisitt bruke agentmodellen i arbeidet ditt. Tenk som om følgende agenter samarbeider, men skriv én samlet rapporttekst:

### Exam Architect

Oppgave:

- Sikre at rapporten følger eksamensoppgaven.
- Pass på at analysen kommer før anbefalingene.
- Pass på at anbefalingene faktisk følger fra analysen.
- Pass på at rapporten har ett samlet, overbevisende argument.

### Evidence Extractor

Oppgave:

- Hent relevante fakta fra evidensfilene.
- Bruk nøkkeltall med presise regnskapsbegreper.
- Skill mellom fakta, claims, marketing claims, antagelser og inferenser.

### Fact Verification Agent

Oppgave:

- Sjekk at konkrete fakta, tall, datoer, navn, regnskapsbegreper og kildehenvisninger stemmer med prosjektets kildegrunnlag før de brukes i rapporttekst.
- Start med `05_evidence/source_verification_packet.md`, `05_evidence/key_numbers.md`, `05_evidence/source_criticism.md`, `05_evidence/claim_reliability_matrix.md`, `05_evidence/coop_business_model_evidence.md` og `05_evidence/competitor_evidence.md`.
- For hvert nytt faktapunkt som skrives inn i rapportutkastet, vurder om det er:
  - verifisert fakta,
  - kildeclaim,
  - marketingclaim,
  - antagelse,
  - inferens,
  - eller fortsatt usikkert.
- Hvis et faktapunkt ikke kan verifiseres i prosjektfilene, ikke skriv det som fakta. Skriv det enten med TODO-markør eller dropp det.
- Sjekk spesielt at regnskapstall ikke blandes: nettoomsetning, EBITDA, EBIT, loss/nettoresultat og case-/prosjektclaims skal holdes atskilt.
- Sjekk at datoer stemmer, særlig Coop.dk MAD-lukking i 2023 og Coop.dk-webshop-lukking 31. januar 2025.
- Sjekk at Lobyco-, Playable-, Shortcut- og konkurrentclaims ikke oppgraderes fra kildeclaim til uavhengig dokumentert effekt.

### Source Critic

Oppgave:

- Vær kildekritisk.
- Marker forsiktig der kildene er Lobyco, Playable, Shortcut eller andre leverandør-/marketingkilder.
- Ikke la appbruk, engagement eller gamification bli fremstilt som lønnsomhetsbevis.
- Skill mellom adoption, engagement, kundeatferd, butikkøkonomi og profitabilitet.

### Competitor & Market Agent

Oppgave:

- Bruk konkurrentevidens for å vise digital/business-model fit.
- Ikke påstå at konkurrenter vinner fordi de har apper.
- Bruk Salling, REMA, Lidl, Dagrofa/MENY og Nemlig som kontekst der det er relevant.

### Theory Application Agent

Oppgave:

- Bruk DVC og Digital Business Model som de eneste fulle teoriperspektivene.
- Ikke introduser flere teorier som fullverdige perspektiver.
- Vis anvendelse, ikke bare teorioppsummering.
- Bruk denne logikken:

```text
Teoribegrep -> Coop-observasjon -> analytisk betydning -> strategisk implikasjon
```

### Recommendation Agent

Oppgave:

- Bygg anbefalingene fra analysen.
- Bruk de fem valgte anbefalingene.
- Gjør anbefalingene konkrete nok til at Martin kan bruke dem i direksjonsdiskusjonen.

### Red Team Agent

Oppgave:

- Se etter svake påstander, overlapp, ubegrunnede slutninger og eksamensrisiko.
- Pass spesielt på:
  - Lobyco må behandles eksplisitt.
  - Retail media må behandles som mulig value capture, ikke bevist lønnsomhet.
  - Anbefaling 2 og 5 må ikke overlappe for mye.
  - Gamification må formuleres som review/redesign, ikke som en påstand om at gamification ikke virker.
  - Medlemslojalitet må skilles fra lønnsomhet.

## 4. Kilde- Og Formuleringsdisiplin

Bruk trygge formuleringer som:

- "kildene indikerer"
- "Coop rapporterer"
- "Lobyco oppgir"
- "dette viser reach/adoption, men ikke lønnsomhet"
- "dette bør behandles forsiktig"
- "det offentlige kildegrunnlaget kan ikke dokumentere kausal effekt"
- "konkurrentevidensen antyder digital fit, ikke direkte årsakssammenheng"

Unngå formuleringer som:

- "Coop App er lønnsom"
- "Lobyco beviser at Coop har et konkurransefortrinn"
- "appbrukere er mer profitable"
- "appen øker handlefrekvensen med 50 prosent"
- "retail media finansierer appinvesteringen"
- "gamification øker Coops lønnsomhet"
- "konkurrentene vinner fordi de har apper"
- "365discount bør ha egen app" uten forbehold

## 5. Viktige Evidenspunkter Som Må Behandles Forsiktig

Bruk disse som arbeidsgrunnlag, men sjekk prosjektfilene for detaljer:

- Coop rapporterer 32,565 mrd. DKK i nettoomsetning i 2025.
- Coop rapporterer EBITDA før eiendomsgevinster på 313 mill. DKK.
- Coop rapporterer EBIT på -215 mill. DKK.
- Prosjektet har også et 232 mill. DKK loss-claim fra case-/prosjektkontekst; dette må ikke blandes med -215 mill. DKK EBIT.
- Coop er en fysisk butikkbasert dagligvareaktør med 536 Coop Danmark-butikker og 900 butikker inkludert brugsforeninger.
- Coop.dk MAD ble lukket i 2023, og Coop.dk-webshop ble lukket 31. januar 2025.
- Coop har mer enn 2 millioner medlemmer/medeiere.
- Lobyco oppgir mer enn 1,8 millioner Coop App-brukere og ca. 25 prosent household reach, men dette er leverandør-/marketingclaim og ikke lønnsomhetsbevis.
- Playable- og Shortcut-kilder kan brukes til å vise mulig app-/gamification-/utviklingslogikk, men ikke som uavhengig dokumentasjon på strategisk eller økonomisk effekt.
- Google Play-scrapet feilet og skal ikke brukes som nøkkelkilde.

## 6. Rapportstrukturen Du Skal Skrive Mot

Bruk denne strukturen:

1. Innledning
2. Metode, avgrensning og antagelser
3. Casebakgrunn: Coop, Coop App og Lobyco
4. Kildekritikk
5. Teorivalg og anvendelse
6. Strategisk situasjonsanalyse
7. Strategisk stance
8. Strategiske anbefalinger
9. Begrensninger og kritisk refleksjon
10. Konklusjon
11. Referanser
12. AI-bruk

`08_final_report/draft_v1.md` har allerede startet seksjon 1 og 2. Du skal bygge videre på dette.

## 7. Din Første Konkrete Oppgave

Lag neste rapportutkast på norsk.

Anbefalt arbeidsmåte:

1. Les filene listet over.
2. Kjør et eksplisitt Fact Verification Agent-trinn før du skriver:
   - list kort hvilke faktapunkter du kommer til å bruke,
   - angi om de er verifisert fakta, claim, marketingclaim, antagelse eller inferens,
   - marker alle usikre punkter med TODO i rapportutkastet,
   - ikke bruk nye tall eller datoer uten at de finnes i prosjektets kilde-/verifikasjonsfiler.
3. Skriv en kort intern status på norsk:
   - hva som allerede er låst,
   - hva `draft_v1.md` inneholder,
   - hvilke seksjoner du nå skal skrive.
4. Skriv videre på rapporten ved å fullføre eller utvide disse seksjonene:
   - `3. Casebakgrunn: Coop, Coop App og Lobyco`
   - `4. Kildekritikk`
   - start gjerne `5. Teorivalg og anvendelse` hvis det passer, men ikke skriv hele rapporten i én omgang.
5. Lag eller oppdater en fil:
   - anbefalt: `08_final_report/draft_v2.md`
6. Oppdater `03_daily_logs/2026-05-04.md` med en kort norsk logg over hva du gjorde, inkludert at Fact Verification Agent-trinnet ble kjørt.

## 8. Kvalitetskrav Til Utkastet

Utkastet skal:

- være akademisk, men klart skrevet,
- ha tydelig argumentasjon,
- være kildekritisk,
- bruke DVC og Digital Business Model anvendt på casen,
- ikke bli en generell tekst om digital transformasjon,
- ikke gi anbefalingene før den strategiske situasjonen er analysert,
- bruke norske overskrifter,
- skrive i sammenhengende avsnitt, ikke bare punkter,
- inkludere TODO-markører der kilder eller presise referanser må sjekkes,
- unngå å finne på kilder, sidetall eller sitater.
- ikke inneholde faktapåstander som mangler støtte i kilde-/verifikasjonsfilene uten eksplisitt TODO-forbehold.

## 9. Før Du Avslutter

Før du gir endelig svar til brukeren:

- Sjekk at all ny rapporttekst er på norsk.
- Sjekk at agentmodellen faktisk er brukt.
- Sjekk at Fact Verification Agent-trinnet faktisk er kjørt, og at nye fakta/tall/datoer er kontrollert mot kildegrunnlaget.
- Sjekk at du ikke har introdusert nye teorier som fulle perspektiver.
- Sjekk at du ikke har skrevet utrygge app-/profitabilitetspåstander.
- Sjekk at `draft_v2.md` finnes eller at du tydelig forklarer hvorfor den ikke ble opprettet.
- Sjekk at daily log er oppdatert.

Svar brukeren kort på norsk med:

- hvilken fil du opprettet/oppdaterte,
- hvilke seksjoner du skrev,
- hvilke viktigste forbehold som fortsatt står igjen.
```
