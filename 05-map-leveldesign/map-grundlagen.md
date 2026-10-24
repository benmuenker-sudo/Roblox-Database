# Map- und Leveldesign

> Stand: 2026-10-24 · Nächste Prüfung: 2027-01-24 · Gesamt-Vertrauen: ✅ für Greybox-Maße, Laser-Tag-Layout, Onboarding-Techniken und Streaming-Regeln (Creator Docs, lokal am Quelltext geprüft), 🧠 für allgemeines Leveldesign (Wegführung, Zonen, Rhythmus)

## Kurzfassung
Eine gute Roblox-Map **führt ohne Text**, zeigt **sofort, wo die erste Aktion wartet**, hat **Zonen mit eigener Identität** und läuft **flüssig auf Handys**. Roblox empfiehlt, zuerst eine **Greybox** zu bauen und dauernd zu testen; die offiziellen Beispielwerte: Gänge und Türen **mindestens 10 Studs breit**, Wände **mindestens 10 Studs hoch** (Standard-Sprunghöhe 5 Studs), Raster **5 Studs** ✅ ([Greybox your environment](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment)). Der Spawn folgt dem Onboarding-Prinzip „get to the fun quickly“: kurzer, sichtbarer Weg zur ersten Core-Loop-Aktion ✅ ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding)). Licht, Streaming, LOD und Budgets stehen in `beleuchtung-und-performance.md`.

## Warum das wichtig ist
- Neue Spieler entscheiden laut Roblox „innerhalb von Minuten“, ob sie bleiben; die First-Play-Bounce-Rate ist ein negatives Home-Signal ✅ ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding), [Discovery](https://create.roblox.com/docs/discovery)).
- Visuelle Hinweise in der Welt werden schwerer übersehen als Text-Popups und brauchen keine Übersetzung ✅ ([Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques)).
- Greyboxing findet Layout-Probleme (schwer begehbare Stellen, unfaire Aussichtspunkte, falscher Maßstab), bevor teure Assets entstehen ✅ ([Greybox your environment](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment)).

## Referenzbilder
Selbst erstellte, beschriftete Referenzbilder (frei nutzbar, Übersicht: `assets/bilder/README.md`).

![Map-Zonen-Layout](../assets/bilder/map-zonen-layout.png)
![Wegführung ohne Text](../assets/bilder/map-wegfuehrung.png)
![Spawn und Hub](../assets/bilder/map-spawn-hub.png)

Offizielle Bilder aus der Roblox Creator Documentation (Übersicht: `assets/bilder/offiziell/README.md`):

![Laser-Tag: Spawnzonen](../assets/bilder/offiziell/level-design-umgebung/lasertag-layout-spawnzonen.jpg)
*Schritt 1: Spawnzonen beider Teams an gegenüberliegenden Enden. Quelle: Roblox Creator Docs, CC BY 4.0*

![Laser-Tag: drei Hauptwege](../assets/bilder/offiziell/level-design-umgebung/lasertag-layout-drei-hauptwege.jpg)
*Interior, Middle, Exterior Primary Lane verbinden die Spawns. Quelle: Roblox Creator Docs, CC BY 4.0*

![Laser-Tag: Querwege](../assets/bilder/offiziell/level-design-umgebung/lasertag-layout-querwege.jpg)
*Blaue Querwege erlauben Spurwechsel. Quelle: Roblox Creator Docs, CC BY 4.0*

![Laser-Tag: Kreuzungspunkte](../assets/bilder/offiziell/level-design-umgebung/lasertag-layout-kreuzungspunkte.jpg)
*Kreuzungen von Haupt- und Querwegen = Combat Pockets. Quelle: Roblox Creator Docs, CC BY 4.0*

![Laser-Tag: Greybox gesamt](../assets/bilder/offiziell/level-design-umgebung/lasertag-greybox-gesamt.jpg)
*Wegeschema direkt in Greybox-Wände übersetzt. Quelle: Roblox Creator Docs, CC BY 4.0*

![Laser-Tag: farbcodierte Platzhalter](../assets/bilder/offiziell/level-design-umgebung/lasertag-greybox-platzhalter-materialien.jpg)
*Farbcodierte Böden (Teamseiten rot/blau, Spawns grün, Außenbereich gelb). Quelle: Roblox Creator Docs, CC BY 4.0*

![Laser-Tag: Spawn-Ausgänge](../assets/bilder/offiziell/level-design-umgebung/lasertag-spawnzone-ausgaenge.jpg)
*Zwei Ausgänge pro Spawnzone gegen Engpässe und Spawn-Camping. Quelle: Roblox Creator Docs, CC BY 4.0*

![Laser-Tag: Moodboard](../assets/bilder/offiziell/level-design-umgebung/lasertag-artstyle-referenzcollage.jpg)
![Laser-Tag: fertige Welt](../assets/bilder/offiziell/level-design-umgebung/lasertag-fertige-welt.jpg)
*Vom Moodboard zur fertigen Arena. Quelle: Roblox Creator Docs, CC BY 4.0*

![Island Jump: Höhenstufen](../assets/bilder/offiziell/level-design-umgebung/insel-sprungspiel-hoehenstufen.jpg)
*Zylinder-Plattformen in sieben Höhenstufen als vertikale Progression. Quelle: Roblox Creator Docs, CC BY 4.0*

![Greybox-Obby](../assets/bilder/offiziell/game-design/prototyp-greybox-obby.png)
![Ausgearbeiteter Obby](../assets/bilder/offiziell/game-design/prototyp-obby-ausgearbeitet.png)
*Prototyp aus grauen Parts vs. weiterentwickelte Version. Quelle: Roblox Creator Docs, CC BY 4.0*

![Onboarding: prominentes Schild](../assets/bilder/offiziell/game-design/onboarding-visuelle-prominenz.png)
*Color or Die: „How to Play!“-Schild direkt in Blickrichtung. Quelle: Roblox Creator Docs, CC BY 4.0*

![Streaming-freundlicher gewundener Weg](../assets/bilder/offiziell/performance/duvall-gewundener-weg.png)
*Gewundener Pfad und blockierende Waldflächen verbergen nicht geladene Bereiche. Quelle: Roblox Creator Docs, CC BY 4.0*

![Terrain-Wüste](../assets/bilder/offiziell/level-design-umgebung/terrain-wueste-showcase.jpg)
*Große organische Landschaft mit Terrain statt Parts. Quelle: Roblox Creator Docs, CC BY 4.0*

## Details

### 1. Prinzipien 🧠
1. **Lesbarkeit:** Auf einen Blick erkennbar, was begehbar, interaktiv, gefährlich ist.
2. **Führung:** Licht, Farbe, Linien, Wege, Höhe lenken Blick und Schritte.
3. **Rhythmus:** Ruhe ↔ Aktion, eng ↔ weit, hoch ↔ tief.
4. **Identität:** Jede Zone hat Farbwelt, Form und Ton.
5. **Belohnte Neugier:** Abseits liegt etwas (Fund, Geheimnis, Abkürzung).
6. **Performance von Anfang an:** Teile, Effekte, Sichtweite kontrollieren ✅ (Roblox: „designing for performance early“ spart Zeit, [Design for performance](https://create.roblox.com/docs/performance-optimization/design)).

### 2. Offizielle Greybox-Maße ✅
Quelle: [Greybox your environment](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment), [Greybox a playable area](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area).

| Wert | Laut Doku | Grund |
|---|---|---|
| Türen und Gänge | **≥ 10 Studs breit** | Zwei Spieler passen gleichzeitig durch |
| Wände | **≥ 10 Studs hoch** | Standard-Sprunghöhe **5 Studs** reicht nicht drüber; Kamera kollidiert nicht |
| Raster (Transform Snapping) | **5 Studs** und **90°** | Gleichmäßige Abstände |
| Ausgänge pro Spawnzone | **2** | 1 = Engpass, 3 = zu wenig Deckung |
| Ein-/Ausgänge pro Combat Pocket | **höchstens 3** | Keine Entscheidungsüberforderung |
| Laser-Tag-Gesamtlayout | **2 Spawnzonen, 3 Hauptwege, 5 Querwege**, gespiegelt an der Mittellinie | Symmetrie = Fairness |
| Höhenunterschiede | Wedges für Anstieg (Mezzanine bricht Sichtlinien) und Abfall (Außenweg ist tiefster Punkt) | Sichtlinien steuern |
| Island Jump (Obby) | Flache Zylinder als Landeflächen, Höhenunterschied steigt schrittweise | Vertikale Progression |

🧠 Ableitungen für andere Genres: Simulator-Wege für Gruppen eher **15–20 Studs** breit (mehrere Spieler plus Pets); Türrahmen in Hubs ≥ 10 Studs; Plattform-Abstände im Obby zuerst unter der 5-Stud-Sprunghöhe beginnen und langsam steigern.

### 3. Das Drei-Wege-Layout (Laser-Tag-Beispiel) ✅
Quelle: [Greybox your environment](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment).
- **Spawnzonen** an gegenüberliegenden Enden, damit Spieler sich orientieren können, bevor sie den Gegner sehen; als eigene Räume abgetrennt (Deckung beim Respawn). Dezentrale Spawns nahe Kampfzonen erhöhen die Schwierigkeit stark.
- **Drei Hauptwege** (Interior, Middle, Exterior). Der **mittlere Weg** hat den meisten Kampf, weil er von beiden Seiten angreifbar ist.
- **Querwege** verbinden alle Hauptwege; sie haben wenig Deckung, damit niemand dort campt („transitory spaces“).
- **Combat Pockets** = Kreuzungen von Querwegen und Mittelweg; dort passiert am meisten. Sie unterteilen die Distanz zwischen den Spawns und helfen, die Map schnell zu lernen.
- Hallway-Ergänzungen brechen lange Sichtlinien auf dem Innenweg.
- **Playtest-Fragen der Doku:** Vor- oder Nachteile für ein Team? Können sich Spieler jederzeit orientieren? Gibt es Bereiche mit zu vielen Wahlmöglichkeiten? Was macht Spaß, was frustriert? Fühlen sich Spieler so, wie beabsichtigt? Kann man Teile umgehen und trotzdem das Ziel erreichen?
- Workflow der Lernreihe: Greybox → Moodboard/Art Style → Asset-Bibliothek → fertige Welt → Optimierung ✅ ([Environmental art curriculum](https://create.roblox.com/docs/tutorials/curriculums/environmental-art)).

### 4. Spawn und Hub (die ersten Minuten)
| Regel | Beleg |
|---|---|
| Spawn nahe der ersten Aktion, Weg kurz und sichtbar | 🧠 auf Basis „Get to the fun quickly“ ✅ ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding)) |
| Kernmechanik als **großes Schild/Bild in Blickrichtung** (Color or Die) statt Textpopup | ✅ ([Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques)) |
| **Leuchtende Spur** oder Pfeile zum Ziel, Partikel über interessanten Items | ✅ (ebd., *Hello Kitty Cafe*, *Creatures of Sonaria*, *Winds of Fortune*) |
| **Hinweise in der Welt** statt Anweisung (Fußspuren zum Fluchtweg in *Jailbreak*) | ✅ (ebd.) |
| **Kontextuelle Tutorials** beim Betreten einer neuen Zone oder beim ersten Item | ✅ (ebd.) |
| Ziele (kurz/mittel/lang) gut sichtbar in Welt oder UI | ✅ ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding)) |
| Starter-Items/-Währung früh nutzbar | ✅ (ebd.) |
| Wiedererkennbarer Hub: Shop, Verkaufen, Teleporter, Rangliste an einem Ort | 🧠 |
| Lobby-Shop als 3D-Objekt mit „Open Shop“ | ✅ (*Super Striker League*, [Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases)) |
| In Kreise laufen zum Anstellen für Matches (bekannte Konvention) | ✅ ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)) |
| Keine Gefahr am Spawn, Spawnraum mit Deckung | ✅ (Laser-Tag-Spawnräume) / 🧠 |
| Großes, unverwechselbares Wahrzeichen zur Orientierung | 🧠 |
| Interaktion per `ProximityPrompt` (zeigt Taste je Gerät) | ✅ ([Proximity prompts](https://create.roblox.com/docs/ui/proximity-prompts)) |

### 5. Zonen-Design (Simulator/Progression) 🧠
| Zone | Zweck | Gestaltung |
|---|---|---|
| Start | Lernen, Sicherheit | Hell, freundlich, einfach |
| Zone 2–3 | Erste Vertiefung | Neue Farbwelt, neue Ressource |
| Mittelzonen | Abwechslung | Jede mit eigenem Gimmick |
| Späte Zonen | Prestige | Dramatischer, gefährlicher, seltener Loot |
| Endzone / Hub 2 | Rebirth-Anker | Spektakel, Belohnung |

- **Nächste Zone sichtbar machen** (Tor, Berg, Leuchten), Preis/Level am Tor.
- Schwierigkeit steigt sanft, Belohnung steigt sichtbar (vgl. Island-Jump-Höhenstufen ✅).
- Jede Zone mindestens ein eigenes Merkmal (Ressource, Gegner, Mechanik, Look); reines Umfärben vermeiden.
- Zonen eignen sich als **Streaming-Einheiten** (siehe Abschnitt 9).

### 6. Wegführung 🧠
| Werkzeug | Wirkung |
|---|---|
| Licht | Helle Bereiche ziehen den Blick; lokale Lichter markieren Ziele in dunklen Szenen ✅ ([Light sources](https://create.roblox.com/docs/effects/light-sources)) |
| Farbe | Warm (Gold/Orange) = Ziel, kalt = Hintergrund |
| Linien | Wege, Zäune, Flüsse, Baumreihen zeigen Richtung |
| Höhe | Hohe Objekte als Landmarken; Höhenstufen = Fortschritt |
| Engpass ↔ Weite | Eng = Spannung, weit = Erholung |
| Spuren/Pfeile | Im Tutorial, später abbauen ✅ (temporäre Visual Elements) |
| Atmosphäre | Ferne Dinge verblassen (`Atmosphere.Density`) → Fokus auf Nähe ✅ ([Atmosphere](https://create.roblox.com/docs/environment/atmosphere)) |
| Highlight | Quest-Objekte/Teammitglieder durch Wände sichtbar (`Highlight.DepthMode`) ✅ ([Highlighting](https://create.roblox.com/docs/effects/highlighting)) |
| Minimap/Wegmarken | In großen Maps gegen Verlaufen |

Offizielle Wayfinding-Regeln (Schilder, Sichtachsen, Landmarken) als eigenes Kapitel gibt es in der Doku nicht ✅ (nicht gefunden); die Tabelle ist Designwissen.

### 7. Maßstab und Navigation
- Standard-Sprunghöhe **5 Studs** ✅ ([Greybox your environment](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment)); Durchgänge **≥ 10 Studs** ✅ (ebd.).
- 🧠 Laufzeiten messen: lange Wege ohne Inhalt sind der häufigste Langeweile-Faktor; ab Mittelspiel Teleporter/Schnellreise.
- 🧠 Sprung-/Kletter-Mechaniken nur, wenn sie zum Spiel passen und auf Touch bedienbar sind.
- Teleport zwischen Places kann **Erst-Ladezeiten** senken, kostet aber Wartezeit beim Wechsel ✅ ([Design for performance](https://create.roblox.com/docs/performance-optimization/design)).

### 8. Multiplayer-Aspekte
- 🧠 Platz pro Spieler (Farm-Plots, Basen), Plot-Systeme für Besitzgefühl, Servergröße passend zur Map, sichtbare Mitspieler als Social Proof.
- ✅ **Fairness:** Symmetrie und gleich weit entfernte Spawns (Laser-Tag-Layout gespiegelt).
- ✅ Häufig besuchte Orte (z. B. „Home Base“ und „Trading Hub“) können mit **zusätzlichen Replication Foci** (`Player:AddReplicationFocus()`) gestreamt bleiben; jeder Fokus erhöht aber die Serverlast (9 bewegliche Foci ≈ 10 Spieler) ✅ ([Instance streaming](https://create.roblox.com/docs/workspace/streaming)).
- ✅ **Predictive Streaming** (`Workspace.PredictiveStreamingMode = Enabled`) lädt mögliche Respawn-Orte vor und hält verlassene Orte nach einem Teleport kurz geladen, praktisch für Hub ↔ Shop ↔ Zone (ebd.).

### 9. Streaming-freundliches Leveldesign ✅
Quelle: [The Mystery of Duvall Drive – Stream in immersion](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion), [Streaming techniques](https://create.roblox.com/docs/workspace/streaming/techniques).
- Mit kleinem Streaming-Radius fehlt Ferne → **gewundene Wege** und **blockierende Geometrie** (Bäume, Hügel) entlang des Pfads, damit der Spieler immer von geladenen Assets umgeben ist.
- Sehr große Fernziele (Sturm am Himmel) so groß und nah bauen, dass sie innerhalb der Streaming-Distanz liegen.
- **Modelle räumlich klein halten:** Ausdehnung pro Modell unter **~64 Kubik-Studs**, damit es zusammen streamt; große Modelle in kleinere Module teilen.
- Zusammengehörige Teile gruppieren (z. B. alle Teile eines Autos); **Container-Modelle** (ein Riesenmodell mit allen NPCs) zerlegen; tiefe Verschachtelungen vermeiden.
- Modelle, auf die Skripte komplett zugreifen müssen, als **Atomic** markieren; **Persistent** nur in Ausnahmefällen.
- Statische Weltmodelle mit `Model.LevelOfDetail = SLIM` als Fern-Platzhalter (Details in `beleuchtung-und-performance.md`).
- Spawns/Hubs: `Player:RequestStreamAroundAsync()` für Vorladen vor einem Teleport ✅ ([Instance streaming](https://create.roblox.com/docs/workspace/streaming)).

### 10. Umweltgeschichten und Kunst-Stil
- Objekte erzählen (Spuren, Ruinen, Beschriftungen); keine Textmauern 🧠.
- Vor dem Asset-Bau einen **Art Style mit Moodboard** festlegen ✅ (Laser-Tag-Moodboard, [Develop polished assets](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/develop-polished-assets)).
- Mit **Trim Sheets** und wiederverwendeten Meshes entstehen vielfältige Umgebungen mit wenigen Draw Calls ✅ ([Design for performance](https://create.roblox.com/docs/performance-optimization/design)).
- **Terrain** für große organische Landschaften ✅ (Wüsten-Showcase, Doku-Bild).

### 11. Map-Workflow
1. **Konzept + User Flow:** Was tut der Spieler in Minute 1, 5, 30? 🧠
2. **Greybox** mit 5-Stud-Raster, Maßen aus Abschnitt 2, farbcodierten Platzhalter-Materialien ✅.
3. **Playtest** „bei fast jedem Schritt“ mit den Doku-Fragen ✅.
4. **Moodboard / Art Style** ✅.
5. **Asset-Bibliothek** (einmal hochladen, dann duplizieren; Packages gegen Duplikate) ✅ ([Improve performance](https://create.roblox.com/docs/performance-optimization/improve)).
6. **Gameplay-Pass:** Interaktionen, Gefahren, Belohnungen, Proximity Prompts 🧠.
7. **Licht- und Ton-Pass** (`beleuchtung-und-performance.md`, `06-sound-audio/`).
8. **Performance-Pass** auf dem Basisgerät ✅.
9. **Funnel messen:** Wo brechen neue Spieler ab? Doku-Beispiel: 70 % Abbruch zwischen „In Farm“ und „Plant Seed“, gelöst mit Pfeil-Prompts über den Töpfen ✅ ([Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events)).
10. **Testlauf mit Fremden**, beobachten ohne zu erklären 🧠.

### 12. KI-Werkzeuge für Blockouts (Kurzüberblick)
- `GenerationService:GenerateModelAsync()` erzeugt Modelle aus Text, derzeit mit den festen Schemas `Car5` (Karosserie + 4 Räder) und `Body1` (ein MeshPart); optional Bounding Box und maximale Dreieckszahl ✅ ([Model generation](https://create.roblox.com/docs/parts/model-generation)).
- Assistant in Studio kann Objekte einfügen/ändern und Skripte schreiben; externer Zugriff über den offenen Studio-MCP-Server ✅ ([Assistant MCP](https://create.roblox.com/docs/assistant/mcp)).
- Details und Ankündigungen (Cube 3D, 4D): `beleuchtung-und-performance.md`.

## Beispiele aus echten Spielen
- *Color or Die*: Regelschild in Blickrichtung ✅. *Jailbreak*: Fußspuren als Fluchtweg-Hinweis ✅. *Hello Kitty Cafe*: leuchtende Spur ✅ (alle [Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques)).
- *The Mystery of Duvall Drive*: gewundene Auffahrt als Streaming-Trick ✅ ([Stream in immersion](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion)).
- *Super Striker League*: 3D-Shop-Automat in der Lobby ✅ ([Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases)).

## Do / Don't
| Do | Don't |
|---|---|
| Spawn nahe der ersten Aktion | Langer Weg bis zum Spaß |
| Greybox mit 5-Stud-Raster und ≥ 10-Stud-Gängen | Erst Kunst, dann Gameplay |
| 2 Ausgänge pro Spawnraum | Ein einziger Ausgang (Engpass, Spawn-Camping) |
| Max. 3 Eingänge pro Kampfraum | Räume mit 6 Türen |
| Regeln als Bild/Schild in der Welt | Textmauern im Popup |
| Landmarken und sichtbare nächste Zone | Gleichförmige Landschaft |
| Zonen mit eigener Identität | Zonen nur umfärben |
| Gewundene Wege + Sichtblocker bei Streaming | Endlose Sichtachsen ins Leere |
| Modelle klein und thematisch gruppiert | Ein Riesenmodell für die ganze Map |
| Playtest bei fast jedem Schritt | Erst am Ende testen |
| Mobil testen | Nur am PC prüfen |

## Checkliste
- [ ] Greybox steht; Gänge ≥ 10 Studs, Wände ≥ 10 Studs, 5-Stud-Raster
- [ ] Spawn: sicher, nahe der ersten Aktion, Ziel sichtbar, Kernregel als Bild
- [ ] Wegführung ohne Text funktioniert (Testperson findet erstes Ziel allein)
- [ ] Jede Zone hat eigenes Merkmal, nächste Zone ist sichtbar
- [ ] Laufzeiten gemessen, Schnellreise ab Mittelspiel
- [ ] Fairness: symmetrische Spawns/Ressourcen (bei PvP)
- [ ] Streaming: Modelle < ~64 Kubik-Studs, Container zerlegt, Sichtblocker an langen Achsen
- [ ] Funnel-Events für die ersten Schritte eingerichtet
- [ ] Performance auf Basisgerät geprüft (siehe `beleuchtung-und-performance.md`)

## Offene Fragen / Recherche-Bedarf
- Offizielle Wayfinding-Leitlinien (Beschilderung, Sichtachsen) fehlen in der Doku.
- Terrain-Werkzeuge und `MaterialVariant` im Detail noch nicht ausgewertet.

## Verknüpfungen
`beleuchtung-und-performance.md`, `03-mechaniken-retention/retention-und-onboarding.md`, `03-mechaniken-retention/core-loops.md`, `04-ui-ux/hud-shop-menues.md`, `06-sound-audio/audio-grundlagen.md`

## Quellen
- [Creator Docs: Greybox your environment](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment) – Stand 2026-10-24, ✅
- [Creator Docs: Greybox a playable area](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area) – ✅
- [Creator Docs: Environmental art curriculum](https://create.roblox.com/docs/tutorials/curriculums/environmental-art), [Develop polished assets](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/develop-polished-assets) – ✅
- [Creator Docs: Onboarding](https://create.roblox.com/docs/production/game-design/onboarding), [Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques) – ✅
- [Creator Docs: Discovery](https://create.roblox.com/docs/discovery) – ✅
- [Creator Docs: Instance streaming](https://create.roblox.com/docs/workspace/streaming), [Streaming techniques](https://create.roblox.com/docs/workspace/streaming/techniques) – ✅
- [Creator Docs: The Mystery of Duvall Drive – Stream in immersion](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion) – ✅
- [Creator Docs: Design for performance](https://create.roblox.com/docs/performance-optimization/design), [Improve performance](https://create.roblox.com/docs/performance-optimization/improve) – ✅
- [Creator Docs: Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases), [UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design), [Proximity prompts](https://create.roblox.com/docs/ui/proximity-prompts) – ✅
- [Creator Docs: Atmosphere](https://create.roblox.com/docs/environment/atmosphere), [Light sources](https://create.roblox.com/docs/effects/light-sources), [Highlighting](https://create.roblox.com/docs/effects/highlighting) – ✅
- [Creator Docs: Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events) – ✅
- [Creator Docs: Model generation](https://create.roblox.com/docs/parts/model-generation), [Assistant MCP](https://create.roblox.com/docs/assistant/mcp) – ✅
