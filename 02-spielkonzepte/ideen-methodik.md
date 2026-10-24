# Ideen-Methodik: Wie man systematisch gute Roblox-Ideen findet

> Stand: 2026-10-24 · Nächste Prüfung: bei jeder Discovery- oder Regeländerung · Gesamt-Vertrauen: 🧠 für die Methodik; die eingebauten Plattform-Fakten sind mit ✅/🟡/🟠 belegt (siehe `01-markt-trends/`)

## Kurzfassung
Gute Ideen entstehen aus **Beobachtung (Markt) → Zerlegung (Bausteine) → Neukombination (Twist) → Filter (Plattform-Signale) → schnellem Test**. Neu seit 2026: Der Filter richtet sich nach den **offiziellen RFY-Signalen** (PTR, First-Play-Bounce unter 60 s und 61–180 s, Spieltage und Spielzeit bis Tag 28, gezieltes Co-Play) ✅, nach dem **16+-Start** jedes neuen Spiels ✅ und nach den **Wachstumssegmenten** (18–34, APAC) ✅/🟡. Eine Idee, die im Thumbnail nicht klar ist, die ersten drei Minuten nicht trägt oder keinen Grund für morgen hat, fällt durch, egal wie gut sie klingt.

## Referenzbilder
Selbst erstellte, beschriftete Referenzbilder (frei nutzbar, Übersicht: `assets/bilder/README.md`).

![Ideen-Generator](../assets/bilder/ideen-generator-matrix.png)

Offizielle Bilder aus der Roblox Creator Documentation (Übersicht: `assets/bilder/offiziell/README.md`):

![Core Loop Schritt 1: Minute-zu-Minute-Interaktion](../assets/bilder/offiziell/game-design/core-loop-minute-zu-minute.jpg)
*Baustein 1 jedes Loops: die ständige Interaktion (hier „Explore“). Quelle: Roblox Creator Docs, CC BY 4.0.*

![Core Loop vollständig mit Progressionsmotor](../assets/bilder/offiziell/game-design/core-loop-progressionsmotor.jpg)
*Vollständiger Loop: Explore → Fight → Upgrade. Ohne Progressionsmotor „repetitive, boring, and shallow“. Quelle: Roblox Creator Docs, CC BY 4.0.*

![Onboarding als D1-Funnel](../assets/bilder/offiziell/game-design/onboarding-d1-retention-pyramide.png)
*Play drücken → FTUE starten → FTUE beenden → zurückkehren: Jede Idee im Schnelltest als Funnel messen. Quelle: Roblox Creator Docs, CC BY 4.0.*

![Greybox-Prototyp](../assets/bilder/offiziell/game-design/prototyp-greybox-obby.png)
*Prototyp in Greybox: Spaß und Schwierigkeit vor Optik. Quelle: Roblox Creator Docs, CC BY 4.0.*

## Warum das wichtig ist
- Die Hälfte des Erfolgs auf Roblox entscheidet sich vor der ersten Zeile Code: Ist die Fantasie im Thumbnail klar (PTR)? Trägt der Loop die ersten 3 Minuten (Bounce)? Gibt es Gründe für Tag 2–28?
- Kopieren lohnt sich weniger denn je: Nachahmer fallen schneller als Originale 🟠, „Non-unique games“ werden gedrosselt ✅, Reskins sind für die Kuratierung „a hard sell“ ✅.

## Details

### Schritt 1 – Markt beobachten (30–60 Minuten)
**Quellen in dieser Reihenfolge:**

| Quelle | Was du dort findest | Vertrauen |
|---|---|---|
| [Roblox Charts](https://www.roblox.com/charts) (Top Trending, Up-and-Coming, Top Playing Now, Top Revisited) | Aufsteiger und Dauerbrenner | ✅ (Ranking-Logik nicht dokumentiert) |
| Tracker (RoWatcher, Rolimons, RoVitals, Statroblox) | CCU-Verlauf, Peaks mit Datum, Genre-Anteile | 🟠 (Abweichung 5–30 %) |
| [Standout Games](https://create.roblox.com/docs/creator-programs/standout-games) | Welche Genres Roblox als unterversorgt ansieht (RPG, Strategie, Puzzle, Shooter) | ✅ |
| Aktionärsbriefe (siehe `01-markt-trends/plattform-kennzahlen.md`) | Wohin Roblox steuert (Alter, Regionen, Retention) | ✅ |
| DevForum-Ankündigungen und Creator Roadmap | Neue Features, die Ideen ermöglichen | ✅ |
| Kommentare, Fan-Wikis, Discords | Was Spieler loben und was nervt | 🟠 |

**Für jedes interessante Spiel notieren:**
- Genre und Core Loop in einem Satz
- Launch-Datum, Peak mit Datum, heutiger Monatsdurchschnitt, 30-Tage-Trend
- Session-Struktur (Runden, Timer, Idle)
- Update-Takt und Event-Tag (meist Samstag)
- Monetarisierung (Passes, Produkte, Zufallsitems mit Quoten?)
- Social-Mechanik (Koop, Handel, Stehlen, Kompetition) und ob sie ohne Chat funktioniert
- Zielalter und vermutliches Maturity-Label

**Lücken-Suche:**
- Welche Spielerwünsche tauchen immer wieder auf, ohne erfüllt zu werden?
- Welche Genres haben alte Top-10 (3+ Jahre)? Welche haben 30 Klone in den Top 100?
- Welche Regionen/Sprachen werden kaum bedient? (APAC = ein Drittel der DAU 🟡)

### Schritt 2 – In Bausteine zerlegen
Jedes Spiel besteht aus austauschbaren Bausteinen:

| Baustein | Fragen | Beispiel (Hit 2025/26) |
|---|---|---|
| **Fantasie** | Was fühlt sich der Spieler wie? | Gärtner (GAG), Dieb (SaB), Überlebender (99 Nights) |
| **Core Loop** | Aktion → Belohnung → Verbesserung → neue Aktion | Pflanzen → warten → ernten → größere Beete 🟡 |
| **Spannungsquelle** | Zeitdruck, Gefahr, Konkurrenz, Zufall, Knappheit | Diebstahl durch andere (SaB, Steal An Egg) |
| **Zeitstruktur** | Echtzeit-Timer, Runden, Tag/Nacht, Saisons | Feste Zahl an Nächten (99 Nights) |
| **Meta-Schicht** | Sammlung, Rebirth, Ranking, Saison | Rebirth mit Bedingung (SaB) |
| **Social** | Koop, Handel, Konkurrenz, Zuschauen, Co-Play | Admin-Events auf öffentlichen Servern 🟠 |
| **Live-Takt** | Update-Rhythmus, Event-Format | Samstags-Update + Admin Abuse 🟠 |
| **Ästhetik** | Stil, Humor, Sound, Meme-Identität | Brainrot (gesättigt) |
| **Monetarisierung** | Boosts, Slots, Skins, Passes, Zufallsitems | Robux beschleunigen und ermöglichen Stehlen (GAG) 🟡 |

### Schritt 3 – Neu kombinieren (Ideen-Generator)
Wähle je 1 Element aus 3–4 Kategorien und prüfe, ob eine **in einem Satz erklärbare** Idee entsteht.

**Fantasie × Loop × Spannung × Meta**
- Fantasie: Bäcker / Archäologe / Fischer / Hacker / Hausmeister / Tierarzt / Geisterjäger / Wetterforscher / Pirat / Expeditionsleiter / Detektiv / Stratege
- Loop: Farmen und Verkaufen / Erkunden und Sammeln / Bauen und Verteidigen / Craften und Liefern / Aufziehen und Kämpfen / Runden mit Rollen / Taktik-Gefecht / Rätsel lösen
- Spannung: Nachtgefahr / Diebstahl durch andere / Zeitlimit / Zufalls-Mutation / Wetter-Events / Konkurrenz-Rangliste / Asymmetrie (1 gegen viele) / begrenzte Tragkraft
- Meta: Sammelbuch / Rebirth / Saisonpass / Gilden / Museum / Handelsmarkt / Ranglisten-Saison / Basisausbau / Kapitel

**Neu 2026 – Filter-Achsen beim Kombinieren** (🧠, aus offiziellen Signalen):
- **Zielgruppe:** 16–34 (Midcore) vs. 9–15 (Select) vs. 5–8 (Kids). Startet ohnehin 16+ ✅.
- **Co-Play ohne Chat:** Rollen, Pings, Presets, strukturierter Tausch.
- **Region:** universell vs. lokalisiert (Japanisch, Hindi, Portugiesisch).

**Beispiel-Kombinationen (Rohideen, ungeprüft 🧠):**
1. *Archäologe × Erkunden × Mutation × Museum*: Fundstücke ausgraben, mutieren lassen, im Museum ausstellen; andere besuchen und bewerten.
2. *Fischer × Farmen × Wetter-Events × Sammelbuch*: Seltene Fische nur bei Sturm; Fischbuch zeigt Vollständigkeit.
3. *Geisterjäger × Verteidigen × Nachtgefahr × Gilden*: Tagsüber Fallen bauen, nachts Geister jagen; Gilden teilen sich ein Haus.
4. *Bäcker × Craften × Diebstahl × Saisonpass*: Nachbarn können Gebäck klauen, wenn du keine Alarmanlage hast.
5. *Expeditionsleiter × Erkunden × begrenzte Tragkraft × Basisausbau* (Midcore-Koop): Was nimmst du mit zurück?
6. *Stratege × Taktik-Gefecht × Rangliste × Ranglisten-Saison* (16–34, Shooter/Taktik-Lücke).
7. *Detektiv × Rätsel lösen × Asymmetrie × Kapitel* (Puzzle-Lücke, endlich erlaubt ✅).

### Schritt 4 – Die Filterfragen (vor Prototyp)
Die klassischen 7 Fragen, ergänzt um 5 Plattform-Fragen für 2026:

| # | Test | Frage | Bezug |
|---|---|---|---|
| 1 | Ein-Satz-Test | „Du ___, um ___ zu bekommen.“ Geht das in einem Satz? | 🧠 |
| 2 | **Thumbnail-Test (PTR)** | Lässt sich die Fantasie in einem 16:9-Bild ohne Text am unteren Rand zeigen? Würde jemand darauf klicken? | ✅ PTR „most important“; eigenes Thumbnail Pflicht ([Discovery](https://create.roblox.com/docs/discovery)) |
| 3 | 10-Sekunden-Test | Was macht der Spieler in den ersten 10 Sekunden? | 🧠 |
| 4 | **3-Minuten-Test (Bounce)** | Gibt es vor Minute 3 eine erste Belohnung/einen Aha-Moment? | ✅ Bounce < 60 s und 61–180 s; „to the fun in 5 minutes or less“ ([Retention](https://create.roblox.com/docs/production/analytics/retention)) |
| 5 | Wiederhol-Test | Macht die Kernhandlung nach 30 Minuten noch Spaß? | 🧠 |
| 6 | **6-Tage-Test** | Warum kommt jemand an möglichst vielen der 6 Tage im Fenster 2–7 zurück? | ✅ Spieltage pro Nutzer ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)) |
| 7 | **Woche-2–4-Test** | Was hält Spieler in Tag 8–28 (Progression, Saison, Tausch, Gilde)? Oder ist es bewusst endlich? | ✅ (endliche Spiele nicht bestraft) |
| 8 | **Co-Play-Test** | Warum spielt jemand gezielt mit Freunden, und klappt das ohne freien Chat? | ✅ Co-Play-Signal; Preset-Regeln ([Preset system guidelines](https://create.roblox.com/docs/chat/preset-system-guidelines)) |
| 9 | Content-Test | Kannst du 8 Wochen lang Inhalte liefern (klein alle 2–4 Wochen, Aufwand je < 3 Wochen)? | ✅ ([Content updates](https://create.roblox.com/docs/production/game-design/content-updates)) |
| 10 | Monetarisierungs-Test | Gibt es einen fairen, wiederkehrenden Kauf, der den Loop beschleunigt, aber nicht zerstört? Odds-pflichtig? | ✅ Kauftage-Signal; Odds-Pflicht |
| 11 | **Zielgruppen-Test** | Funktioniert die Idee als 16+-Start? Wenn Kids-Zielgruppe: Plan für 250 hoch engagierte 16+-Plays oder Expedited Review? | ✅ ([Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)) |
| 12 | **Originalitäts-Test** | Würde Roblox es als „Non-unique game“ werten? Ist es Standout-Games-tauglich? | ✅ ([Discovery](https://create.roblox.com/docs/discovery); [Standout Games](https://create.roblox.com/docs/creator-programs/standout-games)) |

**Regel:** Fällt die Idee bei **4 oder mehr** der 12 Fragen durch (oder bei Frage 2, 4 oder 6 allein) → verwerfen oder umbauen 🧠.

### Schritt 5 – Schnelltest
- **Greybox-Prototyp (1–3 Tage):** nur Core Loop, hässliche Teile, keine Meta ✅ (Greybox-Empfehlung der Doku).
- **Testspieler:** 5–10 Personen. Auf Roblox selbst dürfen Early Tester bis zu **10 gleichaltrige Freunde** sein (z. B. 18+-Creator → 16+-Tester) ✅ ([Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places)). Beobachten, nicht erklären.
- **Messen statt raten:** Onboarding-Funnel mit `LogOnboardingFunnelStepEvent` (Schritt 1 in `PlayerAdded`) ✅ ([Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events)). Beispiel der Doku: ca. 70 % Abbruch zwischen „In Farm“ und „Plant Seed“, behoben mit Hinweisen und Pflicht-Tutorial.
- **Kennzahlen:** Zeit bis zur ersten Aktion, Anteil nach 1 und 3 Minuten noch im Spiel, „noch eine Runde?“, Rückkehr am nächsten Tag.
- **Realistische Messlatte (große Spiele, GameAnalytics 2026):** D1 Median 10,3 %, Top 1 % 22,2 %; D7 1,6 % / 9,1 %; D30 0,5 % / 4,7 %; Sitzung Median 9,8 Min. 🟡 ([GameAnalytics](https://www.gameanalytics.com/reports/2026-roblox-report)). Kleine Tests liegen oft anders; Trend wichtiger als absolute Zahl.
- **A/B-Tests erst später:** Experiments laufen 14–60 Tage; unter 1.000 DAU kaum aussagekräftig ✅ ([Experiments](https://create.roblox.com/docs/production/experiments)). Davor: Funnels und Beobachtung.
- **Entscheiden:** bauen / ändern / stoppen. Siehe `checklisten/idee-validieren.md`.

### Schritt 6 – Idee schärfen für die Kuratierung
- Ist die Idee neuartig genug für **Standout Games**? Passt ein großes Update für **Today's Picks**? Beide nehmen Nominierungen per Umfrage an ✅ ([Today's Picks](https://create.roblox.com/docs/creator-programs/todays-picks-home)).
- Formuliere den Pitch so, wie ein Redakteur ihn liest: Fantasie, was ist neu, für wen.

## Beispiele aus echten Spielen
- **Grow a Garden** = Gärtner × Farmen × Diebstahl (gegen Robux) × Seltenheit + Samstags-Event 🟡/🟠.
- **Steal a Brainrot** = Sammler × Passiveinkommen × Diebstahl × Rebirth + Meme-Ästhetik 🟡.
- **99 Nights** = Überlebender × Koop-Survival × Nachtgefahr × feste Zahl an Nächten 🟡.
- **Murder Mystery 2** = Detektiv/Mörder × Runden mit Rollen × Asymmetrie × Tauschmarkt 🟠.
- Zerlegung im Detail: `01-markt-trends/viral-hits-analyse.md`.

## Typische Denkfehler
- „Das Spiel X hat Millionen, also kopiere ich es.“ → Du kommst zu spät, ohne deren Event-Maschine, und wirst als „Non-unique“ gedrosselt ✅.
- „Ich kaufe Reichweite mit Werbung.“ → Werbe-Nutzer zählen nicht im RFY-Ranking ✅.
- „Lange Sitzungen = gute Retention.“ → Spielzeit ist auf 60 Min./Tag gedeckelt; Spieltage zählen ✅.
- „Ich baue erst alles, dann teste ich.“ → Prototyp zuerst.
- „Mehr Features = besser.“ → Ein starker Loop schlägt zehn mittelmäßige Systeme.
- „Spieler wollen genau das, was sie sagen.“ → Beobachte Verhalten.
- „Kinder sind die Zielgruppe, also starte ich für Kinder.“ → Jedes Spiel startet 16+ ✅.

## Was heißt das für dich (🧠)
- Nutze die 12 Filterfragen als Gate vor jedem Prototyp; dokumentiere die Antworten in `konzept-vorlage.md`.
- Investiere die erste Woche in Thumbnail-Skizze + 3-Minuten-Prototyp, nicht in Systeme.
- Plane die Retention-Schicht (Tag 2–28) gleichzeitig mit dem Core Loop.

## Do / Don't
| Do | Don't |
|---|---|
| Hits in Bausteine zerlegen | Hits 1:1 nachbauen |
| Ein-Satz-Pitch + Thumbnail-Skizze | Mit Systemlisten beginnen |
| Früh mit echten Spielern (16+) testen | Monatelang im Geheimen bauen |
| Retention über 4 Wochen planen | Nur Launch-Woche planen |
| Offizielle Signale als Filter | Tracker-Peaks als Beweis |

## Checkliste
- [ ] Markt beobachtet (Charts, 2 Tracker, Standout-Liste), mit Datum notiert
- [ ] Mindestens 3 Spiele in Bausteine zerlegt
- [ ] 5+ Kombinationen erzeugt
- [ ] 12 Filterfragen beantwortet, Ergebnis dokumentiert
- [ ] Greybox-Prototyp mit Funnel-Events
- [ ] 5–10 Testspieler (16+) beobachtet
- [ ] Entscheidung bauen/ändern/stoppen getroffen

## Offene Fragen / Recherche-Bedarf
- Keine öffentlichen Genre-Retentionswerte, um Filterfragen 6/7 quantitativ zu prüfen.
- Ranking-Logik der Charts unbekannt, daher „Aufsteiger“ nur qualitativ deutbar.

## Verknüpfungen
- Zerlegung von Hits: `01-markt-trends/viral-hits-analyse.md`
- Discovery-Signale: `01-markt-trends/discovery-algorithmus.md`
- Regeln (16+-Start, Odds, Chat): `01-markt-trends/plattform-regeln-2026.md`
- Zielgruppen und Regionen: `01-markt-trends/plattform-kennzahlen.md`
- Ideenliste: `zukunftsideen.md` · Vorlage: `konzept-vorlage.md` · Variation: `spiele-abaendern.md`

## Quellen
- [Creator Docs: Discovery](https://create.roblox.com/docs/discovery) / [Discovery FAQ](https://create.roblox.com/docs/discovery-faq) – Stand 24.10.2026, ✅
- [Creator Docs: Retention](https://create.roblox.com/docs/production/analytics/retention) – ✅
- [Creator Docs: Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events) – ✅
- [Creator Docs: Experiments](https://create.roblox.com/docs/production/experiments) – ✅
- [Creator Docs: Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places) – ✅
- [Creator Docs: Standout Games](https://create.roblox.com/docs/creator-programs/standout-games) / [Today's Picks](https://create.roblox.com/docs/creator-programs/todays-picks-home) – ✅
- [Creator Docs: Content updates](https://create.roblox.com/docs/production/game-design/content-updates) – ✅
- [Creator Docs: Preset system guidelines](https://create.roblox.com/docs/chat/preset-system-guidelines) – ✅
- [GameAnalytics: 2026 Roblox Report](https://www.gameanalytics.com/reports/2026-roblox-report) – 🟡
