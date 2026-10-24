# Roblox Database

Eine Wissensdatenbank für die Entwicklung von Roblox-Spielen. Sie ist dafür gebaut, als **Projektwissen in Claude Projects** eingebunden zu werden. Claude bekommt dadurch bei jedem Projekt das Marktwissen, die Designregeln und die Checklisten, auf die beim Bauen eines Spiels geachtet werden muss.

## Wofür ist das hier?
- Spiele planen: Markt, Trends, Konzepte, Ideen
- Spiele bauen: UI, Map, Sound, Mechaniken, Luau-Technik
- Spiele halten: Retention, Progression, Live-Ops, Monetarisierung
- Spiele prüfen: Checklisten vor Prototyp, Release und Update
- Spiele abändern: Wie man ein bestehendes Konzept variiert, ohne zu kopieren

## So bindest du es in ein Claude-Projekt ein
1. Projekt in Claude öffnen, dann **Projektwissen / Dateien**.
2. Entweder das Repo über die GitHub-Anbindung verknüpfen (falls dein Projekt sie anbietet) oder die Dateien hochladen.
3. Ins Projekt eine Anweisung schreiben, siehe `automation/projekt-anweisung.md`. Sie sagt Claude, dass es zuerst `INDEX.md` lesen soll.

Tipp: Lade nicht alles blind hoch. Für ein UI-Projekt reichen `04-ui-ux/`, `03-mechaniken-retention/` und die Checklisten.

## Wie die Datenbank aktuell bleibt
Claude lernt nicht von allein im Hintergrund. Die Datenbank wächst, wenn eine Session sie aktualisiert:
- Manuell: Prompt aus `automation/update-prompt.md` in eine Session geben.
- Automatisch: Der gleiche Prompt kann als geplante Aufgabe wöchentlich laufen.
- Jede Änderung wird in `CHANGELOG.md` eingetragen.

## Vertrauensgrade (wichtig)
Jede Aussage über Zahlen oder Marktdaten trägt einen Vertrauensgrad:

| Marker | Bedeutung |
|---|---|
| ✅ **Belegt** | Offizielle Roblox-Quelle (Creator Hub, Newsroom, Investor Relations, DevForum-Ankündigung) |
| 🟡 **Wahrscheinlich** | Mehrere unabhängige Quellen oder gut dokumentiert (z. B. Wikipedia, Fachpresse) |
| 🟠 **Unsicher** | Einzelne Blogs, Fan-Seiten, SEO-Seiten, widersprüchliche Zahlen |
| 🧠 **Designwissen** | Allgemeine Spieldesign-Erfahrung, kein Roblox-spezifischer Beleg |

Stand-Datum steht in jeder Datei. Marktdaten veralten innerhalb von Wochen.

## Bilder und Audio
Siehe `assets/`:
- **23 selbst erstellte Referenzbilder** (`assets/bilder/`): beschriftete Mockups und Diagramme (HUD, Shop, Inventar, Sammelbuch, Map-Zonen, Loops, Gacha, Live-Ops-Kalender …). Frei nutzbar.
- **121 offizielle Bilder** aus der Roblox Creator Documentation (`assets/bilder/offiziell/`), lizenziert unter CC BY 4.0. Bei Weitergabe Quelle nennen.
- **26 selbst synthetisierte Sounds** (`assets/audio/`, WAV + OGG): Münz-Pling, UI-Klicks, Fanfaren, Mythic-Drop, Warnungen, Loops. Frei nutzbar, auch zum Hochladen in deine Spiele.
- Screenshots und Musik **fremder Spiele** sind urheberrechtlich geschützt und deshalb nur als Link und Beschreibung enthalten. Eigene Screenshots kommen in `assets/eigene-referenzen/`.
- Claude Projects liest Bilder, aber keine Audiodateien. Lade für Sounds `assets/audio/README.md` und `assets/audio/audio-wellenformen.png` hoch.
- Bilder und Sounds lassen sich mit `tools/` neu erzeugen.

## Größe und Auswahl für Claude Projects
Die Datenbank hat rund 100.000 Wörter und ca. 75 MB Assets. Lade für ein Projekt gezielt hoch: `INDEX.md`, die relevanten Themenordner, die passenden Checklisten und die wichtigsten PNGs.

## Struktur
Siehe `INDEX.md`.
