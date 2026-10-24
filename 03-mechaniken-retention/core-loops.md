# Core Loops

> Stand: 2026-10-24 · Nächste Prüfung: 2026-11-21 · Gesamt-Vertrauen: ✅ für die offizielle Loop-Definition und Messmethoden (Creator Docs), 🟡/🟠 für Beispiele aus Hit-Spielen, 🧠 für Muster und Zeitwerte

## Kurzfassung
Roblox definiert den Core Loop offiziell in drei Teilen: **Minute-zu-Minute-Interaktion**, die **am häufigsten wiederholte Aktionsfolge** und einen **Progressionsmotor**, der beides zurückspeist. Ohne Progressionsmotor wird ein Spiel „repetitive, boring, and shallow“. ✅ Ein Roblox-Loop muss in Sekunden verständlich sein, in den ersten 5 Minuten Spaß machen und nach Tagen noch Rückkehrgründe liefern. ✅/🧠 Die Hits von 2025/26 (Grow a Garden, Steal a Brainrot, Steal An Egg) zeigen ein Muster: ein simpler, mobil-tauglicher Sammel-Loop plus Timer oder Diebstahl-Spannung plus Seltenheit und Handel. 🟡/🧠

## Referenzbilder
Selbst erstellte, beschriftete Referenzbilder (frei nutzbar, Übersicht: `assets/bilder/README.md`).

![Core Loop und Zeitebenen](../assets/bilder/core-loop-diagramm.png)
![Loop-Muster](../assets/bilder/loop-muster-uebersicht.png)

Offizielle Bilder aus der Roblox Creator Documentation (CC BY 4.0, Übersicht und Lizenz: `assets/bilder/offiziell/README.md`).

![Schritt 1: Minute-zu-Minute](../assets/bilder/offiziell/game-design/core-loop-minute-zu-minute.jpg)
*Action-RPG, Schritt 1: „Explore“ als ständige Minute-zu-Minute-Interaktion. Quelle: Roblox Creator Docs, CC BY 4.0 ([Core loops](https://create.roblox.com/docs/production/game-design/core-loops))*

![Schritt 2: wiederholte Aktionen](../assets/bilder/offiziell/game-design/core-loop-wiederholte-aktionen.jpg)
*Schritt 2: „Explore → Fight“, die am häufigsten wiederholte Aktionsfolge. Quelle: Roblox Creator Docs, CC BY 4.0 ([Core loops](https://create.roblox.com/docs/production/game-design/core-loops))*

![Schritt 3: Progressionsmotor](../assets/bilder/offiziell/game-design/core-loop-progressionsmotor.jpg)
*Vollständiger Loop: Explore → Fight → Upgrade → zurück zu Explore. Quelle: Roblox Creator Docs, CC BY 4.0 ([Core loops](https://create.roblox.com/docs/production/game-design/core-loops))*

![Greybox-Prototyp](../assets/bilder/offiziell/game-design/prototyp-greybox-obby.png)
*Greybox-Obby: Den Loop zuerst ohne Deko testen. Quelle: Roblox Creator Docs, CC BY 4.0 ([Prototyping](https://create.roblox.com/docs/production/game-design/prototyping))*

## Warum das wichtig ist
- D1-Retention hängt laut Roblox an **Core Loop, FTUE und Performance**. Der Core Loop ist der erste genannte Hebel. ✅ ([Retention](https://create.roblox.com/docs/production/analytics/retention))
- Alle LiveOps-Inhalte sollen am Core Loop hängen, „so all of the game's systems remain integrated“. ✅ ([LiveOps essentials](https://create.roblox.com/docs/production/game-design/liveops-essentials))
- Content-Kadenz baut auf bestehenden Systemen auf. Ein Loop, der keine einfachen Varianten erlaubt, macht günstige Updates unmöglich. ✅ ([Content updates](https://create.roblox.com/docs/production/game-design/content-updates))

## Details

### 1. Die offizielle Definition ✅
Quelle: [Core loops](https://create.roblox.com/docs/production/game-design/core-loops)

| Teil | Bedeutung | Action-RPG-Beispiel der Doku |
|---|---|---|
| **Minute-to-minute interaction** | Ständige Grundhandlung, je nach Genre verschieden | Erkunden |
| **Most repeated set of actions** | Die definierende Mechanik; viele Einzelaktionen fallen unter eine Kernmechanik | Kämpfen (ausweichen, schlagen, blocken) |
| **Progression engine** | Treibt den Spieler voran und verändert die beiden ersten Teile | Upgrade-Baum: Level-Ups und neue Skills verbessern Erkunden und Kämpfen |

Weitere offizielle Loop-Beispiele ✅ ([Retention](https://create.roblox.com/docs/production/analytics/retention)):
- Haustierspiel: adoptieren → trainieren → leveln.
- Tycoon: Geschäft führen → Ressourcen balancieren → mit anderen konkurrieren.
- Tycoon laut Genre-Tabelle: von „Droppern“ sammeln → bauen → neue Teile und Dropper freischalten, bis nichts mehr zu bauen ist. Simulator: einfache, wiederholte Aktionen bis zum Maximallevel, dann gegen eine bessere Version tauschen. ([Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox))

**Offizieller Verbesserungsweg** ✅ ([Retention](https://create.roblox.com/docs/production/analytics/retention)):
1. Kernschritte identifizieren und klar und spaßig machen.
2. Herausforderung balancieren (weder Frust noch Langeweile).
3. Den Abschluss des Loops belohnen: Feedback, Währung, Items, Achievements.

### 2. Anatomie eines Loops (Praxis, 🧠)
1. **Aktion:** Was tut der Spieler? (klicken, pflanzen, kämpfen, bauen, laufen)
2. **Feedback:** sofortige Reaktion (Ton, Partikel, Zahl, Animation). Die Doku betont: Ohne klares Feedback fragen sich Spieler, ob sie etwas falsch gemacht haben oder das Spiel kaputt ist. ✅ ([Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques))
3. **Belohnung:** Währung, Item, Fortschrittsbalken, Fund.
4. **Verbesserung:** Der Spieler investiert die Belohnung.
5. **Neue Möglichkeit:** Die Verbesserung verändert die nächste Runde spürbar.

**Regel (🧠):** Jede Runde soll sich anders anfühlen als die letzte. Reine Wiederholung ermüdet.

### 3. Loop-Zeitebenen (🧠, an Roblox-Daten ausgerichtet)
| Ebene | Dauer | Beispiel | Zweck | Bezug zu Daten |
|---|---|---|---|---|
| **Mikro** | 2–30 s | ernten, schlagen, klicken | sofortige Befriedigung | Bounce < 60 s ✅ ([Discovery](https://create.roblox.com/docs/discovery)) |
| **Meso** | 3–15 min | Welle, Auftrag, Runde | Sitzungsziel | Median-Sitzung pro Spiel 9,8 min 🟡 ([GameDevReports](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox)) |
| **Tag** | mehrmals täglich | Timer, Restock, Tagesaufgabe | Rückkehr am selben Tag | Median 1,56 Sitzungen/Spieler/Tag, Top 1 % 8,3 🟡 ([GameDevReports](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox)) |
| **Makro** | Tage–Wochen | Rebirth, Saison, Sammelbuch | Rückkehrgrund | RFY Tag 2–7 und 8–28 ✅ ([Discovery](https://create.roblox.com/docs/discovery)) |

Jedes erfolgreiche Spiel braucht **alle Ebenen**. Nur Mikro wirkt nach 10 Minuten leer, nur Makro ist anfangs zäh. 🧠
Wichtiger Befund: 2025 kam Engagement-Wachstum auf Roblox vor allem aus **häufigerer Rückkehr**, nicht aus längeren Sitzungen. 🟡 ([GameAnalytics 2025](https://www.gameanalytics.com/reports/2025-roblox-report)) → Die „Tag“-Ebene (Timer, Restocks, Offline-Wachstum) ist auf Roblox besonders wertvoll. 🧠

### 4. Loop-Muster auf Roblox

| # | Muster | Loop | Stärke | Gefahr / Gegenmittel | Beispiele |
|---|---|---|---|---|---|
| 1 | **Sammeln–Verkaufen–Upgraden** (Simulator) | sammeln → verkaufen → Ausrüstung → mehr sammeln | sehr leicht verständlich | Monotonie → Zonen, seltene Funde, Rebirth | Bee Swarm Simulator ✅ (Doku-Genrebeispiel) |
| 2 | **Warten–Ernten** (Idle-Hybrid) | setzen → Wartezeit → Rückkehr → ernten | Rückkehr-Anker, passt zu Mobile | Spieler wartet nur → aktive Boni, Mini-Aufgaben | Grow a Garden 🟡 ([Naavik](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/)) |
| 3 | **Dropper/Tycoon** | sammeln → bauen → neue Dropper | sichtbarer Aufbau | Ende erreicht → Rebirth, Erweiterungen | Lumber Tycoon 2 ✅ (Doku) |
| 4 | **Tag/Nacht (Survival)** | Tag sammeln/bauen → Nacht überleben → stärker | natürlicher Rhythmus, Spannung | Schwierigkeit → Skalierung | 99 Nights in the Forest 🟠 |
| 5 | **Wellen-Verteidigung** | aufbauen → Welle → Belohnung → verbessern | Strategie | Balancing-Aufwand | Plants vs Brainrots 🟠 |
| 6 | **Besitz mit Risiko (Steal/Defend)** | sammeln → verteidigen → andere bestehlen | Emotion, Clips, erzwingt Rückkehr | Frust bei Neulingen → Schutzzeiten, Wiederbeschaffung | Steal a Brainrot, Steal An Egg, GAG2 (Nacht-Diebstahl) 🟡 |
| 7 | **Runden-Loop** | Lobby → Runde → Ergebnis → Belohnung | natürliche Wiederholung | leere Server → Mindestspieler, Bots | Murder Mystery 2 🟠 |
| 8 | **Kampf-Progress** | trainieren → Boss → Fähigkeit → stärkerer Boss | Identität, Sammelreiz | Pay-to-win-Vorwurf | Blox Fruits 🟠 |
| 9 | **Erkunden–Kämpfen–Upgraden** | offizielles Action-RPG-Beispiel | Tiefe | Content-Hunger | ✅ Doku |
| 10 | **Sozial-Rollenspiel** | Werkzeuge geben → Spieler erzeugen Inhalte füreinander | „evergreen sources of content“ | wenig Ziel → Jobs, Missionen | Brookhaven ✅ ([Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox)) |

Formel der Mega-Hits 2025/26 (Analyse aus Tracker- und Pressedaten, 🧠 auf Basis 🟡/🟠): (1) simpler, AFK-freundlicher Sammel-Loop, (2) soziale Konflikte durch Stehlen, (3) Seltenheitsstufen und Handel, (4) wöchentliche Updates mit Live-Events, (5) meme-fähige Ästhetik, (6) Crossovers. Viele dieser Spiele verloren aber binnen Monaten über 90 % ihrer CCU, z. B. Steal a Brainrot rund −99 % gegenüber dem Rekord. 🟠 ([RoWatcher](https://rowatcher.com/news/is-the-brainrot-trend-dying-what-ccu-data-from-three-top-games-reveals)) Details: `fallstudien.md`, `01-markt-trends/viral-hits-analyse.md`.

### 5. Loop messen ✅
- **Abschlussrate jedes Loop-Schritts** messen, auch negative Ausgänge (Kampf verloren). ([Retention](https://create.roblox.com/docs/production/analytics/retention))
- **Custom Event für die Kernaktion** mit Custom Field statt vieler Eventnamen. Doku-Beispiel *Plant*: `HarvestPlant` mit Pflanzentyp als Feld. Wenn Spieler eine Pflanze stark bevorzugen (dort: Rüben), Ungleichgewicht prüfen und Vielfalt im Loop fördern. ([Custom events](https://create.roblox.com/docs/production/analytics/custom-events))
- **Explore-Formeln:** Win-Rate (`RoundWins / RoundsPlayed`), Wirtschaftsgesundheit (`CurrencySources − CurrencySinks`), Feature-Adoption. ([Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard))
- Mehr dazu: `analytics-und-experimente.md`.

### 6. Prototyp zuerst (✅/🧠)
Die Doku zeigt den Weg vom Greybox-Obby zum ausgearbeiteten Prototyp: erst Spaß und Schwierigkeit, dann Belohnungen und Feedback. ✅ ([Prototyping](https://create.roblox.com/docs/production/game-design/prototyping)) Jüngere Spieler sind weniger empfindlich bei Grafik, wenn das Spiel Spaß macht. ✅ ([Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox))

### 7. Loop und Live-Ops verbinden (🧠, gestützt auf ✅)
- Content-Kadenz soll **bestehende Systeme** nutzen: Pets, Fahrzeuge, Waffen, Maps, Quests. ✅ ([LiveOps essentials](https://create.roblox.com/docs/production/game-design/liveops-essentials))
- Beim Loop-Design deshalb fragen: Welche Inhalte lassen sich als **einfache Variante** nachliefern (Recolor, neue Pflanze, neues Pet)? Doku-Beispiel: Pet-Varianten in *Adopt Me!*. ✅ ([Content updates](https://create.roblox.com/docs/production/game-design/content-updates))
- Events sollen den Loop ergänzen (z. B. Angelturnier im Angel-Loop, *Overlook Bay 2*). ✅ ([LiveOps planning](https://create.roblox.com/docs/production/game-design/liveops-planning))

## Beispiele aus echten Spielen
- **Grow a Garden:** pflanzen, warten, ernten, dann größere Beete und seltenere Pflanzen. Robux beschleunigen und ermöglichen Stehlen bei Nachbarn. 🟡 ([Naavik](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/))
- **Steal a Brainrot:** Brainrots kaufen, die passiv Geld erzeugen, andere bestehlen, die eigene Basis mit Fallen verteidigen, Rebirth mit Geld plus bestimmtem Brainrot. 🟡 ([Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot))
- **Grow a Garden 2 (Juni 2026):** Tages-Farming plus nächtliches Stehlen und Basisverteidigung. 🟡 ([allthings.how](https://allthings.how/grow-a-garden-2-launches-june-12-with-night-stealing-on-roblox/))
- **99 Nights in the Forest:** Koop-Survival über eine feste Zahl von Nächten. 🟠 ([Sportskeeda](https://www.sportskeeda.com/roblox-news/99-nights-forest-fishing-update-guide))
- Details und Lehren: `fallstudien.md`.

## Typische Fehler
| Fehler | Folge | Lösung |
|---|---|---|
| Belohnung zu spät | Bounce in den ersten 1–3 Minuten (negatives RFY-Signal ✅) | Erste Belohnung < 30 s |
| Kein Progressionsmotor | „repetitive, boring, and shallow“ ✅ | Upgrade verändert nächste Runde |
| Zu viele Währungen früh | Überforderung | Max. 1–2 am Anfang (🧠); Analytics trackt ohnehin nur 5 sicher ✅ |
| Upgrade ändert nichts spürbar | Frust | Spürbare Sprünge (2×, neuer Effekt) 🧠 |
| Kein Ziel in Sicht | Orientierungslos | Sichtbarer nächster Meilenstein ✅ ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding)) |
| Wartezeit ohne Alternative | Langeweile | Parallele Aktivität 🧠 |
| Loop nur mit Chat verständlich | Chat ist altersbeschränkt | Visuell erklären, Presets ✅ (siehe `social-loops.md`) |
| Neuer Content braucht neues System | Kadenz unbezahlbar | Loop auf Varianten auslegen ✅ |

## Do / Don't
| Do | Don't |
|---|---|
| Drei Teile definieren: Interaktion, Kernaktion, Progressionsmotor | Nur Interaktion ohne Fortschritt |
| Tages-Rückkehrgründe (Timer, Restock) einbauen | Marathon-Sitzungen erzwingen (RFY zählt max. 60 min/Tag ✅) |
| Loop als Greybox testen | Erst Deko, dann Spaß suchen |
| Kernaktion als Custom Event messen | Loop-Balance nach Gefühl |
| Varianten-fähige Inhalte planen | Jedes Update als neues System |

## Checkliste
- [ ] Ein-Satz-Beschreibung des Loops möglich
- [ ] Drei Teile benannt (Minute-zu-Minute, Kernaktion, Progressionsmotor)
- [ ] Erste Aktion < 10 s, erste Belohnung < 30 s
- [ ] Feedback bei jeder Aktion (Ton + visuell + Zahl)
- [ ] Mikro-, Meso-, Tages- und Makro-Ziele definiert
- [ ] Loop ohne Chat verständlich
- [ ] Inhalte als Varianten nachlieferbar
- [ ] Kernaktion als Custom Event, Loop-Schritte im Funnel

## Offene Fragen / Recherche-Bedarf
- Keine offiziellen Daten, welche Loop-Muster auf Roblox am besten halten. Genre-Retention-Tabellen von Drittseiten sind unbelegt. 🟠
- Offline-Wachstum und Luck-Formeln von Grow a Garden sind nicht aus Primärquellen belegt.

## Quellen
- [Creator Docs: Core loops](https://create.roblox.com/docs/production/game-design/core-loops) – Stand 2026-10-24, ✅
- [Creator Docs: Retention](https://create.roblox.com/docs/production/analytics/retention) – ✅
- [Creator Docs: Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox) – ✅
- [Creator Docs: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques) – ✅
- [Creator Docs: Custom events](https://create.roblox.com/docs/production/analytics/custom-events) – ✅
- [Creator Docs: LiveOps essentials](https://create.roblox.com/docs/production/game-design/liveops-essentials) und [Content updates](https://create.roblox.com/docs/production/game-design/content-updates) – ✅
- [Creator Docs: Prototyping](https://create.roblox.com/docs/production/game-design/prototyping) – ✅
- [Creator Docs: Discovery](https://create.roblox.com/docs/discovery) – ✅
- [GameDevReports: GameAnalytics 2026](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox) – 🟡
- [GameAnalytics 2025 Roblox Report](https://www.gameanalytics.com/reports/2025-roblox-report) – 🟡
- [Naavik: Predicting the next big hits on Roblox](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/) – 2025, 🟡
- [Wikipedia: Steal a Brainrot](https://en.wikipedia.org/wiki/Steal_a_Brainrot) – 🟡
- [allthings.how: Grow a Garden 2](https://allthings.how/grow-a-garden-2-launches-june-12-with-night-stealing-on-roblox/) – 2026, 🟡

## Verknüpfungen
`retention-und-onboarding.md`, `progression-rebirth.md`, `live-ops-events.md`, `analytics-und-experimente.md`, `fallstudien.md`
