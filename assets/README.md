# Assets: Referenzbilder und Referenzaudio

> Stand: 2026-10-24

## Wichtig: Urheberrecht und unser Ansatz
- Spiel-Screenshots und Soundtracks sind **urheberrechtlich geschützt**. Sie gehören nicht ohne Erlaubnis in ein Repo.
- Die Sandbox, in der diese Datenbank erstellt wurde, konnte außerdem keine Bilder/Audios von Roblox-Spielseiten herunterladen.
- Lösung: Wir haben **eigenes Referenzmaterial erstellt**. Die Bilder in `bilder/` sind selbst gezeichnete, beschriftete Mockups und Diagramme (fiktive Spiele, deutsche Erklärungen). Die Sounds in `audio/` sind selbst synthetisiert. Beides ist frei nutzbar, auch in deinen eigenen Spielen.
- Für echte Spiele bleiben die **Referenzlisten und Beschreibungen** (`referenz-bilder.md`, `referenz-audio.md`): Claude kann damit gezielt prüfen, woran man ein Muster erkennt. Eigene Screenshots kommen in `eigene-referenzen/`.
- Alles lässt sich mit den Skripten in `tools/` neu erzeugen und anpassen (siehe `tools/README.md`).

## Dateien und Ordner
- `bilder/`: **23 eigene Referenzbilder** (je `.svg` + `.png`, 1600 × 900): Ideen-Generator, Genre-Übersicht, HUD, Shop, Inventar, Sammelbuch, Farben, Touch-Größen, Tutorial, Popups, Core Loop, Loop-Muster, Onboarding-Trichter, Progression/Rebirth, Gacha/Pity, Map-Zonen, Wegführung, Spawn/Hub, Live-Ops-Kalender, Audio-Mix, Client-Server, Monetarisierung. Übersicht: `bilder/README.md`
- `bilder/offiziell/`: Bilder aus der offiziellen Roblox Creator Documentation (CC BY 4.0, Lizenzhinweis dort beachten)
- `audio/`: **26 eigene Sounds** (je `.wav` + `.ogg`): Münz-Pling mit Varianten, Pling-Leiter, UI-Klicks, Kauf-Erfolg, Level-Up-Fanfare, Mythic-Drop, Kampf, Ernte, Warnungen, Loops (Lo-Fi-Menü, Horror-Drone, Wind, Wasser). Übersicht mit Hör-Raster: `audio/README.md`, Bild aller Wellenformen: `audio/audio-wellenformen.png`
- `referenz-bilder.md`: Was man sich bei welchem Spiel/UI ansehen soll, mit Link und Erkennungsmerkmalen
- `referenz-audio.md`: Hörbeispiele-Liste, Beschreibung von Klangmustern, Lizenz-Hinweise
- `eigene-referenzen/`: Hier legst du **eigene** Screenshots (PNG/JPG) und Audio-Notizen ab. Eigene Aufnahmen aus deinen Spielen und eigenen Tests sind rechtlich unproblematisch.

## Für Claude Projects
- Lade die PNGs aus `bilder/` und `audio/audio-wellenformen.png` zusammen mit den Markdown-Dateien hoch. Claude liest Bilder, aber keine Audiodateien; die Wellenform-Übersicht und `audio/README.md` beschreiben die Sounds deshalb in Worten und Bildern.

## So nutzt du eigene Bilder
1. Mache Screenshots in Studio/Spiel (nur für eigene Referenz, nicht veröffentlichen, wenn fremdes Material).
2. Lege sie in `eigene-referenzen/<thema>/` ab (z. B. `hud/`, `shop/`, `map-zonen/`).
3. Trage sie in `referenz-bilder.md` in die Slot-Tabelle ein: Dateiname, Quelle, was sie zeigt, was man lernt.
4. Claude Projects kann Bilder lesen. Lade die wichtigsten zusammen mit den Markdown-Dateien hoch.
