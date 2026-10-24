# Retention und Onboarding

> Stand: 2026-10-24 · Nächste Prüfung: 2026-11-21 · Gesamt-Vertrauen: ✅ für Definitionen, Onboarding-Regeln und RFY-Signale (Creator Docs), 🟡 für Plattform-Benchmarks (GameAnalytics), 🧠 für Zeitpläne und Maßnahmen

## Kurzfassung
Retention misst, wie viele neue Spieler **nach 1, 7 und 30 Tagen** zurückkommen. ✅ Auf Roblox ist ein D1 von rund **10 %** der Median großer Spiele, D7 liegt bei 1,6 % und D30 bei 0,5 %. Selbst die Top 1 % erreichen nur 22 % / 9 % / 4,7 %. 🟡 Roblox sagt: Spieler sollen den Spaß „ideally in 5 minutes or less“ erleben, über drei Onboarding-Ziele (Wesentliches lehren, schnell zum Spaß, Lust auf mehr) und drei Techniken (visuelle Elemente, kontextuelle Tutorials, zeitgesteuerte Hinweise). ✅ Seit der Discovery-Umstellung bewertet die Home-Empfehlung Tag 1, Tag 2–7 und Tag 8–28 getrennt und wertet frühe Abgänge (< 60 s, 61–180 s) als **negatives Signal**. Ein schwaches Onboarding kostet damit direkt Reichweite. ✅

## Referenzbilder
Selbst erstellte, beschriftete Referenzbilder (frei nutzbar, Übersicht: `assets/bilder/README.md`).

![Onboarding-Trichter](../assets/bilder/retention-funnel-onboarding.png)
![Tutorial-Pfeil](../assets/bilder/ui-tutorial-pfeil.png)

Offizielle Bilder aus der Roblox Creator Documentation (CC BY 4.0, Übersicht und Lizenz: `assets/bilder/offiziell/README.md`).

![D1-Retention als Player-Funnel](../assets/bilder/offiziell/game-design/onboarding-d1-retention-pyramide.png)
*Player-Funnel: Play drücken → FTUE starten → FTUE beenden → zurückkehren. Jeder Schritt verliert Spieler. Quelle: Roblox Creator Docs, CC BY 4.0 ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding))*

![Visuelle Prominenz](../assets/bilder/offiziell/game-design/onboarding-visuelle-prominenz.png)
*Color or Die: Schild mit der Kernregel direkt in Blickrichtung. Quelle: Roblox Creator Docs, CC BY 4.0 ([Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques))*

![Highlights](../assets/bilder/offiziell/game-design/onboarding-highlights.png)
*Hello Kitty Cafe: Button umrandet, Rest abgedunkelt, Pfeil zeigt darauf. Quelle: Roblox Creator Docs, CC BY 4.0 ([Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques))*

![Kontextuelles Tutorial](../assets/bilder/offiziell/game-design/onboarding-kontext-tutorial.png)
*Squishmallows: Kombinieren wird erst erklärt, wenn der Spieler zwei gleiche Figuren besitzt. Quelle: Roblox Creator Docs, CC BY 4.0 ([Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques))*

![Funnel mit 70 % Abbruch](../assets/bilder/offiziell/analytics/funnel-pflanzenspiel-dropoff.png)
*Onboarding-Funnel des Referenzspiels „Plant“: 70 % Abbruch zwischen „In Farm“ und „Plant Seed“. Quelle: Roblox Creator Docs, CC BY 4.0 ([Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events))*

![Gegenmaßnahme: Pfeil-Prompts](../assets/bilder/offiziell/analytics/funnel-pflanzenspiel-ingame-prompts.png)
*Die Antwort im Spiel: Pfeile über den Töpfen zeigen, wo gepflanzt wird. Quelle: Roblox Creator Docs, CC BY 4.0 ([Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events))*

![Retention-Diagramm](../assets/bilder/offiziell/analytics/retention-diagramm.png)
*D1/D7/D30 nach Erstspieldatum der Kohorte. Quelle: Roblox Creator Docs, CC BY 4.0 ([Retention](https://create.roblox.com/docs/production/analytics/retention))*

## Warum das wichtig ist
- **Discovery hängt an Retention.** Die Home-Empfehlung („Recommended For You“, RFY) bewertet als wichtigste Signale Play-Through-Rate, First-Play-Bounce-Rate, Spieltage pro Nutzer und Spielzeit pro Nutzer, jeweils für Tag 1, Tag 2–7 und Tag 8–28. ✅ ([Discovery](https://create.roblox.com/docs/discovery))
- Roblox hat am 15. Juni 2026 von einem 7-Tage- auf ein **28-Tage-Fenster** umgestellt. ✅ ([Roblox Newsroom](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox))
- Roblox selbst empfiehlt, **vor** dem Einkauf von Traffic D1 und Sitzungszeit auf Benchmark-Niveau zu bringen. ✅ ([Analytics](https://create.roblox.com/docs/production/analytics))
- Joinen und Verlassen kosten auf Roblox fast nichts. Lange Tutorials führen dazu, dass Spieler „bounce off your game in search of something more immediately engaging“. ✅ ([Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox))

## Details

### 1. Definitionen ✅
- **D1:** Anteil neuer Nutzer, die am Tag nach dem ersten Besuch zurückkommen. **D7:** Rückkehr am 8. Tag. **D30:** am 31. Tag. Die x-Achse im Dashboard ist das **Erstspieldatum** der Kohorte. ([Retention](https://create.roblox.com/docs/production/analytics/retention))
- **Kohorte:** Spieler mit demselben Erstspieldatum. Tageskohorten über 10 Tage, Wochenkohorten (Mo–So) über 10 Wochen. ([Retention](https://create.roblox.com/docs/production/analytics/retention))
- **New User First Session Retention:** Wie viele neue Nutzer X Minuten nach dem ersten Join noch spielen, im Vergleich zur Vorperiode. ([Engagement](https://create.roblox.com/docs/production/analytics/engagement))
- **FTUE / Onboarding:** „the first few minutes of gameplay“. Erfolg wird an **D1** und an den **Onboarding-Zielen** gemessen. ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding))
- Details zu Dashboards, Benchmarks und Events: `analytics-und-experimente.md`.

### 2. Benchmarks: Was „gut“ auf Roblox heißt
| Kennzahl | Median | Top 1 % | Vertrauen / Quelle |
|---|---|---|---|
| D1 | 10,3 % (25. Perzentil: 8,4 %) | 22,2 % | 🟡 [GameAnalytics 2026](https://www.gameanalytics.com/reports/2026-roblox-report) |
| D7 | 1,6 % | 9,1 % | 🟡 [GameAnalytics 2026](https://www.gameanalytics.com/reports/2026-roblox-report) |
| D30 | 0,5 % (25. Perzentil: 0,3 %) | 4,7 % | 🟡 [GameAnalytics 2026](https://www.gameanalytics.com/reports/2026-roblox-report) |
| Sitzung pro Spiel | 9,8 min (Top 5 %: 16,6 min) | 21,1 min | 🟡 [GameDevReports](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox) |
| Sitzungen/Spieler/Tag pro Spiel | 1,56 (Top 10 %: 3,22) | 8,3 | 🟡 [GameDevReports](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox) |
| Offizielles Beispiel-Benchmarkband D1 | 50. Perzentil 12,11 % | 90. Perzentil 18,73 % | ✅ [Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard) |

- Stichprobe GameAnalytics: 500+ Spiele mit ≥ 1 Mio. MAU, Aug. 2025 bis Juli 2026. Kleine Spiele liegen typischerweise darunter. 🟡
- Ältere GameAnalytics-Zusammenfassung (2023): nur 12–15 % der Nutzer kommen nach Tag 1 zurück. 🟡, veraltet ([GameDevReports 2023](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-games))
- 2025 kam das Wachstum vor allem aus **häufigerer Rückkehr**, nicht aus längeren Sitzungen. 🟡 ([GameAnalytics 2025](https://www.gameanalytics.com/reports/2025-roblox-report))

> **Korrektur zur alten Fassung:** Die früher hier genannten Drittanbieter-Werte „Obby D1 25–35 %, D7 10–15 %“ (🟠, rowatcher) liegen **über** dem Top-1-%-Wert von GameAnalytics und sind als Ziel unbrauchbar. Nutze das Benchmark-Band im eigenen Dashboard (ab 100 DAU). ✅/🟡

**Faustregel (🧠, aus den Zahlen oben):** D1 ≈ 10 % ist normal, ≥ 15 % klar überdurchschnittlich, ≥ 20 % Spitze. D7 ≥ 5 % und D30 ≥ 2 % sind Elite.

### 3. Was die 28-Tage-RFY-Logik für Retention-Design bedeutet
**Fakten** ✅ ([Discovery](https://create.roblox.com/docs/discovery); [Discovery FAQ](https://create.roblox.com/docs/discovery-faq))
- Signale gelten nur für Nutzer, die **organisch über RFY** kamen. Tag 2–7 und Tag 8–28 verfolgen dieselben Nutzer weiter, auch wenn sie über „Continue“ zurückkehren.
- **First-Play-Bounce** wird in zwei Fenstern gemessen: **< 60 s** und **61–180 s**.
- **Spieltage Tag 2–7:** „Out of the 6 days in the 2–7 window, how many days on average did those users play.“
- **Spielzeit** zählt maximal **60 Minuten pro Nutzer, Spiel und Tag**.
- Wichtige Signale zusätzlich: **intentional co-play days** (Spieltage mit Freunden über Join, Einladung, privaten Server), qualified play sessions, spend days, Robux pro Nutzer.
- Die drei Zeitfenster werden „both separately and combined“ betrachtet. Ein starkes Tag-8–28-Signal bei schwachem Tag 1 ist laut FAQ „very unlikely“.
- Neue Spiele müssen nicht 28 Tage warten: Erst zählen PTR und Bounce, dann Tag 1, dann 2–7, dann 8–28. Kein Malus für einen schwachen Start, die Signale nutzen ein gleitendes Fenster.
- Story-getriebene und endliche Spiele werden für niedrigere Tag-8–28-Werte **nicht** bestraft.
- Wöchentliche Saisonalität: Home-Traffic hat meist samstags die Spitze.

**Ableitungen für das Design** (🧠)
| RFY-Signal | Designfolge |
|---|---|
| Bounce < 60 s | In der ersten Minute muss etwas passieren: Spawn neben der ersten Interaktion, kein Ladebildschirm-Text, keine Pflicht-Cutscene |
| Bounce 61–180 s | Erste Belohnung und erstes „Aha“ vor Minute 3 |
| Spieltage Tag 2–7 (von 6) | Gründe für **tägliche** Rückkehr: wachsende Timer, Tagesaufgaben, Restocks, Tagesboni ohne Strafen |
| Spielzeit max. 60 min/Tag | Lieber mehrere kurze Rückkehrer als Marathon-Sitzungen. Kein Grund, Spielzeit künstlich zu strecken |
| Co-play days | Freunde-Einladung, Party-Boni, Koop-Ziele (siehe `social-loops.md`) |
| Spend days | Kleine, wiederkehrende Angebote statt eines einzigen großen Kaufs |
| Tag 8–28 | Endgame, Sammlungen, Saisons, Rebirth, regelmäßige Updates |

### 4. Die drei offiziellen Onboarding-Ziele ✅
Quelle: [Onboarding](https://create.roblox.com/docs/production/game-design/onboarding)

**Ziel 1: Das Wesentliche lehren**
- Steuerung für Navigation und Interaktion, bei Bedarf auf dem Bildschirm (Beispiel: *Super Striker League* zeigt Maus-/Tastenbelegung).
- Den **Core Loop** vermitteln: Spieler müssen verstehen, „what they are expected to do and why“.

**Ziel 2: Schnell zum Spaß**
- „New players typically decide their interest in a game within minutes.“
- **Progression:** niedrige XP-Schwellen in den ersten Leveln, live mit **Configs** feinjustierbar.
- **Soziale Motivation:** für soziale Spiele Matchmaking-Parameter im FTUE per **Experiments** testen.
- **Start-Items und Startwährung:** verschiedene Startbeträge per Experiment testen, den Gewinner per Config global setzen.
- Die Analytics-Doku ergänzt: **„ideally in 5 minutes or less“**, kurzes Tutorial oder Tooltips, ein **„joyful moment“** nach dem ersten Loop-Durchlauf, eine **Vorschau** auf den Fortschritt bei mehrfachem Durchlauf. ([Retention](https://create.roblox.com/docs/production/analytics/retention))
- Die Engagement-Doku: „Ensure users have fun within the first five minutes“, lange Tutorials vermeiden, Lernen kontextuell, Start-Items geben, Hürden für soziale Interaktion entfernen. ([Engagement](https://create.roblox.com/docs/production/analytics/engagement))

**Ziel 3: Lust auf mehr machen**
- Kurz-, mittel- und langfristige **Ziele** sichtbar machen (Skill Trees, Season Pass, Quests, Sammlungen). Beispiel: Season Pass in *Jailbreak*.
- **„Moments of joy“**: Belohnungen, Animationen, Effekte bei Meilensteinen. Das Onboarding mit einem bewusst gestalteten Freudenmoment beenden.

### 5. Die drei offiziellen Onboarding-Techniken ✅
Quelle: [Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques)

| Technik | Was | Beispiele aus der Doku | Faustregel |
|---|---|---|---|
| **Visuelle Elemente** | Pfeile, Partikel, leuchtende Pfade, Schilder in der Welt, Spotlights | *Color or Die* (Regel-Schild in Blickrichtung), *Hello Kitty Cafe* (Spotlight + Pfeil, Pfad), *Jailbreak* (Fußspuren als Fluchtweg-Hinweis), *Winds of Fortune* (Pfeile; Kampf-Feedback mit Schadenszahlen, rotem Bildschirmpuls, fliegenden Münzen), *Creatures of Sonaria* (Richtungspfeile) | Zeigen statt beschreiben; funktioniert ohne Übersetzung, für Kinder vor dem Lesealter und auf kleinen Displays |
| **Kontextuelle Tutorials** („just in time“) | Erklärung erst, wenn ein Feature relevant wird | *Squishmallows*: Kombinier-Tutorial, sobald zwei gleiche Figuren im Inventar sind; Marktplatz (Mid-/Late-Game) wird erst erklärt, wenn Spieler ihn selbst finden | Weniger kognitive Last in der ersten Sitzung, besseres Behalten |
| **Zeitgesteuerte Hinweise** | Hilfe nur für Spieler, die hängen | Referenzspiel *Plant*: Die meisten drücken „PLANT CABBAGE SEED“ innerhalb von 10 s → Highlight bei **11 s**; Pfeil über dem richtigen Marktstand nach etwas Erkundungszeit; Handels-Button hervorheben, wenn jemand in den **ersten zwei Sitzungen** nicht gehandelt hat | Knapp nach der Zeit der Mehrheit; nur einmal; nur für die, die es brauchen; Timing per Experiment testen (5 vs. 10 s) |

Warum visuell? Die Doku vergleicht das *Color-or-Die*-Schild mit einem dreisätzigen Erklärtext und schreibt: „Players generally don't like to read instructions and skip through text prompts.“ ✅

### 6. Onboarding messen: der Funnel ✅
- Schritte des Core Loops auflisten (Doku-Beispiel Haustierspiel: adoptieren, trainieren, leveln), **Abschlussrate jedes Schritts** messen, positive und negative Ausgänge erfassen (z. B. NPC-Kampf gewonnen oder verloren), größte Abbrüche beheben. ([Retention](https://create.roblox.com/docs/production/analytics/retention))
- Technisch: `LogOnboardingFunnelStepEvent`, Schritt 1 in `PlayerAdded`, serverseitig validieren. ([Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events))
- **Doku-Fall „Plant“:** **70 %** der Spieler brachen zwischen „In Farm“ und „Plant Seed“ ab. Vorgeschlagene Lösung: kontextuelle Indikatoren und ein Onboarding, das Pflanzen und ein erfolgreiches Wachstum erzwingt, bevor der Rest öffnet, plus positive Feedback-Elemente. ✅ ([Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events))
- Wenn der 5-Minuten-Wert der First Session Retention im Wochenvergleich fällt: neue Onboarding-Schritte oder Texte prüfen, Fehler- und Performance-Berichte checken. ✅ ([Engagement](https://create.roblox.com/docs/production/analytics/engagement))
- Ab 1.000 DAU einzelne Tutorial-Schritte per A/B-Test vergleichen (z. B. kurzer Dialog vs. geführter Pfeil). ✅ ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding); [Experiments](https://create.roblox.com/docs/production/experiments))

**Beispiel-Funnel für ein Sammel-/Farmspiel** (🧠)
| Schritt | Event | Zielzeit | Wenn Abbruch hoch |
|---|---|---|---|
| 1 | Join (`PlayerAdded`) | 0 s | Ladezeit, Performance prüfen |
| 2 | Erste Kernaktion | < 10 s | Spawn näher, visueller Pfeil |
| 3 | Erste Belohnung gesehen | < 30 s | Feedback stärker (Ton, Zahl, Partikel) |
| 4 | Erster Verkauf/Einsatz | < 90 s | Zeitgesteuerter Hinweis bei Mehrheitszeit + 1 s |
| 5 | Erstes Upgrade gekauft | < 3 min | Erstes Upgrade billiger, Effekt sichtbarer |
| 6 | Zweite Zone / zweites System | < 5 min | „Spaß-Moment“ vorziehen |
| 7 | Feier am Ende des Onboardings | < 5–8 min | Freudenmoment bewusst inszenieren |
| 8 | Rückkehrgrund gesetzt (Timer, Tagesziel) | Sitzungsende | Unfertiges Ziel sichtbar machen |

### 7. Zeitplan als Startpunkt (🧠 zum Testen, keine Regel)
| Zeit | Ziel | Maßnahme |
|---|---|---|
| 0–10 s | Spieler handelt | Kein Cutscene-Zwang, Spawn nah an erster Interaktion |
| 10–30 s | Erste Belohnung | Sichtbares Feedback: Ton, Zahl, Partikel |
| 30–90 s | Loop verstanden | Pfeil/Highlight, max. ein kurzer Satz pro Schritt |
| 1–3 min | Erstes Upgrade | Spürbare Verbesserung (deckt das 61–180-s-Bounce-Fenster ab) |
| 3–5 min | Spaß erreicht | Kernmoment des Spiels erlebt (offizielle 5-Minuten-Marke ✅) |
| 5–10 min | Feier + nächstes Ziel | Freudenmoment, Ziele sichtbar |
| 10–30 min | Meta-Einstieg | Erste Sammlung, Rebirth-Vorschau, Social-Hook |
| Sitzungsende | Rückkehrgrund | Timer, Tagesbelohnung, unvollendeter Fortschritt |

### 8. Onboarding-Regeln
- **Zeige, erkläre nicht.** Eine Handlung ist besser als ein Textblock. ✅ (Doku-Tenor, s. o.)
- **Genre-Normen nutzen:** Je näher am Muster beliebter Spiele des Genres, desto weniger muss erklärt werden. ✅ ([Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox))
- **Ein Konzept zur Zeit.** Nicht Währung, Inventar, Handel und Rebirth gleichzeitig. 🧠 (gestützt durch „Reduced cognitive load“ ✅)
- **Kein Scheitern in den ersten Minuten**, keine Strafen. 🧠
- **Mobile zuerst testen:** Die meisten Nutzer spielen auf Mobilgeräten und reagieren empfindlich auf Reibung und Ladezeiten. ✅ ([Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox))
- **Überspringen erlauben** für Wiederkehrer, z. B. über `GetPlayerSegmentsAsync` (`UserNewReturningStatus`). 🧠 (API ✅)
- **Metadaten ehrlich:** Falsche Genre-Tags oder irreführende Beschreibungen führen zu Bounces. ✅ ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq))
- **Nicht alle Inhalte hinter Progression sperren:** „make sure there is still enough content available upfront“. ✅ ([Engagement](https://create.roblox.com/docs/production/analytics/engagement))

### 9. Retention-Hebel nach Zeitraum
Offizielle Zuordnung ✅ ([Retention](https://create.roblox.com/docs/production/analytics/retention)):

| Zeitraum | Offizieller Fokus | Offizielle Maßnahmen | Ergänzung (🧠) |
|---|---|---|---|
| **D1** | Core Loop, FTUE, Performance | Kernschritte klar und spaßig, Herausforderung ausbalancieren, Belohnung nach dem Loop; kurzes Tutorial; Crash-Rate, FPS, Fehler nach jedem Update prüfen; Community für Bug-Meldungen | Unfertiges Ziel hinterlassen (wachsende Pflanze, Timer), „Komm morgen wieder“-Bonus ohne Strafe |
| **D7** | Progressionssystem | Klare kurz- und langfristige Ziele, Abwechslung (Modi, Items, Social), Schwierigkeit balancieren; Verteilung der Spieler auf Level messen (Spezial-Item pro Level als Marker) | Neue Zone/Mechanik nach 3–5 Tagen, erste Sammlung mit Fortschritt |
| **D30** | „Ending system“ | Mehr Inhalt: **kleinere Updates alle 2–4 Wochen, größere alle 2–3 Monate**; Social-Mechaniken: Handel, Partys, Gilden, PvP, Turniere, Ranglisten | Rebirth/Prestige, Saisons, Identität (Titel, Showcase) |

Dailies laut Quest-Design-Doku: kurze Aufgaben mit kleinen Belohnungen, innerhalb von 24 h zu erledigen, „a reliable source of soft currency“ und Anreiz, täglich einzuloggen. ✅ ([Quest design](https://create.roblox.com/docs/production/game-design/introduction-to-quest-design))

### 10. Touristen und Locals ✅
- **Touristen** springen zwischen Spielen und wollen Abwechslung. **Locals** bleiben bei wenigen Spielen und bilden fast die gesamte engagierte Basis. Viele Locals waren vorher Touristen. ([Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox))
- Ältere Nutzer investieren mehr Zeit und Geld und werden eher zu Locals. ([Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox))
- 🧠 Folge: Das Onboarding ist für Touristen, die Tag-8–28-Systeme sind für Locals. Beide müssen funktionieren.

### 11. Retention-Fallen und Anti-Patterns
| Falle | Warum schädlich | Besser | Beleg |
|---|---|---|---|
| Langes Pflicht-Tutorial | Bounce, negatives RFY-Signal | Kontextuell, visuell, < 5 min zum Spaß | ✅ [Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox) |
| Kein Progressionsmotor | „repetitive, boring, and shallow“ | Upgrades, die die nächste Runde verändern | ✅ [Core loops](https://create.roblox.com/docs/production/game-design/core-loops) |
| Schlechte Performance auf Low-End | D1 sinkt | Crash-Rate/FPS nach jedem Update | ✅ [Retention](https://create.roblox.com/docs/production/analytics/retention) |
| Zu schnelle oder zu langsame Progression | Inhalt leer oder Frust | Spielerverteilung pro Level messen | ✅ [Retention](https://create.roblox.com/docs/production/analytics/retention) |
| Kein Endgame | D30 bricht weg | Ending System, Social, Updates | ✅ [Retention](https://create.roblox.com/docs/production/analytics/retention) |
| Streak-Bestrafung | Druck, Frust | Streak mit Puffer, „Rettungstag“ | 🧠 |
| Login-Belohnung ohne Spielbezug | kurzfristig | Belohnung führt zu Spielzielen | 🧠 |
| Fake-Dringlichkeit, künstliche Verknappung | Eltern-, Regulierungs- und Rufrisiko | Echte Events, ehrliche Fristen | 🟡 [Fortune, Mai 2026](https://fortune.com/2026/05/20/exclusive-advocacy-groups-file-complaint-roblox-manipulative-design/) |
| Monetarisierung, die Spieler ablehnen | Downvotes | Fair, transparent | ✅ [Monetization](https://create.roblox.com/docs/production/monetization) |
| Irreführendes Thumbnail/Icon | Hoher Bounce | Erwartung = Spiel | ✅ [Discovery FAQ](https://create.roblox.com/docs/discovery-faq) |

Eine Studie der University of Sydney fand manipulative Kaufgestaltung in **14 von 15** untersuchten Roblox-Spielen. 🟡 ([ACS Information Age](https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html))

### 12. Diagnose-Tabelle
| Symptom | Mögliche Ursache | Maßnahme |
|---|---|---|
| Bounce < 60 s hoch | Ladezeit, unklarer Start, irreführendes Thumbnail | Spawn/Performance prüfen, Metadaten angleichen |
| Bounce 61–180 s hoch | Kein früher Spaß | Erste Belohnung und erstes Upgrade vorziehen |
| D1 niedrig, Sitzung kurz | FTUE schwach | Funnel-Abbrüche finden, visuelle Hinweise |
| D1 ok, D7 niedrig | Mittelspiel leer | Ziele, Abwechslung, Sammlungen |
| D7 ok, D30 niedrig | Endgame fehlt | Ending System, Social, Update-Kadenz |
| Kohorte nach großer Welle schlechter | Normaler Effekt laut Doku | Beobachten, nicht überreagieren ✅ |
| Hoher Drop auf Mobile | UI/Performance | `04-ui-ux/mobile-first.md`, Speichergruppen-Filter |
| D1 nur bei Ads schlecht | Zielgruppe der Kampagne passt nicht | Retention nach Quelle vergleichen |

## Beispiele aus echten Spielen
- **Grow a Garden:** Analysten führen den Erfolg auf ein sanftes Onboarding und Idle-Timer im Stil von FarmVille/Hay Day zurück, für viele Roblox-Spieler „entirely fresh“. 🟡 ([Naavik](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/))
- **Squishmallows, Color or Die, Hello Kitty Cafe, Jailbreak, Winds of Fortune:** offizielle Beispiele für die Onboarding-Techniken (s. o.). ✅
- **Brookhaven:** „Creator Cam“ blendet das UI für Video-Aufnahmen aus, soziale Interaktion ist der Inhalt. ✅ ([Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox))
- Ausführliche Fallstudien: `fallstudien.md`.

## Do / Don't
| Do | Don't |
|---|---|
| Spaß in ≤ 5 Minuten | Spaß hinter Tutorial-Wand |
| Visuelle Hinweise, kontextuelle Tutorials | Textblöcke, die alle wegklicken |
| Zeitgesteuerte Hinweise nur für Hängende | Hinweise für alle nach 2 Sekunden |
| Onboarding-Funnel messen | Nach Gefühl umbauen |
| Gegen eigenes Benchmark-Band arbeiten | Mobile- oder Fan-Seiten-Zielwerte übernehmen |
| Tägliche Rückkehrgründe ohne Strafe | Streak-Verlust als Druckmittel |
| Freudenmoment am Ende des Onboardings | Onboarding endet ohne Feier und ohne nächstes Ziel |

## Checkliste
- [ ] Erste Kernaktion < 10 s, erste Belohnung < 30 s
- [ ] Spaß-Moment spätestens nach 5 Minuten
- [ ] Onboarding-Funnel (5–10 Schritte) live, größter Abbruch bekannt
- [ ] Mindestens zwei der drei Techniken eingesetzt (visuell, kontextuell, zeitgesteuert)
- [ ] Zeitgesteuerte Hinweise auf Mehrheitszeit + 1 s kalibriert
- [ ] Feier am Ende des Onboardings, nächste Ziele sichtbar
- [ ] Rückkehrgrund für morgen gesetzt
- [ ] Mobile-Test auf Low-End-Gerät, Crash-Rate/FPS geprüft
- [ ] D1/D7/D30 der Home-Kohorte gegen Benchmark-Band gelesen
- [ ] Metadaten (Titel, Thumbnail, Genre) passen zum Spiel

## Offene Fragen / Recherche-Bedarf
- Offizielle Genre-Benchmarks sind nur im Dashboard sichtbar.
- Numerische Gewichte der RFY-Signale veröffentlicht Roblox nicht.
- Keine verlässlichen Retention-Zahlen einzelner Hit-Spiele (Studios veröffentlichen sie nicht).
- Push-Benachrichtigungen: Experience Notifications nur für opt-in-Nutzer ab 13, **eine pro Tag und Spiel** ✅ ([User notifications](https://create.roblox.com/docs/cloud/guides/experience-notifications)). Wirkung auf Retention unbelegt.

## Quellen
- [Creator Docs: Retention](https://create.roblox.com/docs/production/analytics/retention) – Stand 2026-10-24, ✅
- [Creator Docs: Onboarding](https://create.roblox.com/docs/production/game-design/onboarding) – ✅
- [Creator Docs: Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques) – ✅
- [Creator Docs: Engagement](https://create.roblox.com/docs/production/analytics/engagement) – ✅
- [Creator Docs: Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events) – ✅
- [Creator Docs: Analytics](https://create.roblox.com/docs/production/analytics) und [Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard) – ✅
- [Creator Docs: Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox) – ✅
- [Creator Docs: Quest design](https://create.roblox.com/docs/production/game-design/introduction-to-quest-design) – ✅
- [Creator Docs: Discovery](https://create.roblox.com/docs/discovery) und [Discovery FAQ](https://create.roblox.com/docs/discovery-faq) – ✅
- [Roblox Newsroom: Optimizing Discovery](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox) – Juni 2026, ✅
- [GameAnalytics 2026 Roblox Report](https://www.gameanalytics.com/reports/2026-roblox-report) – 2026, 🟡
- [GameDevReports: GameAnalytics-Zusammenfassung](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox) – 2026, 🟡
- [GameAnalytics 2025 Roblox Report](https://www.gameanalytics.com/reports/2025-roblox-report) – 2025, 🟡
- [Naavik: Predicting the next big hits on Roblox](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/) – 2025, 🟡
- [ACS Information Age: Studie zu Dark Patterns](https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html) – 2026, 🟡
- [rowatcher: Retention Benchmarks by Genre](https://rowatcher.com/news/retention-benchmarks-by-roblox-genre-what-good-actually-looks-like) – 🟠 (nicht als Ziel verwenden)
