# Tools: Referenzbilder und Referenz-Sounds neu erzeugen

> Stand: 2026-10-24 · Alle Bilder in `assets/bilder/` (außer `offiziell/`) und alle Sounds in `assets/audio/` werden von diesen Skripten erzeugt. Du kannst Texte, Farben, Zahlen oder Klänge ändern und alles neu bauen.

## Voraussetzungen
| Werkzeug | Wofür | Hinweis |
|---|---|---|
| Python 3.10+ mit `numpy` und `Pillow` | SVG-Erzeugung, Audio-Synthese, Wellenform-Bild | `pip install numpy pillow` |
| Node.js 18+ mit `playwright` (Chromium) | SVG → PNG rendern | `npm install playwright` und `npx playwright install chromium` |
| `ffmpeg` mit libvorbis | WAV → OGG | auf den meisten Systemen per Paketmanager |
| Schriften: DejaVu Sans, Noto Color Emoji | gleiches Aussehen wie im Repo | ohne sie wird eine Ersatzschrift genutzt (Textbreiten können abweichen) |

## Bilder (`tools/bilder/`)
```bash
# aus dem Repo-Hauptordner
python3 tools/bilder/erzeuge_bilder.py                 # alle SVGs nach assets/bilder/
python3 tools/bilder/erzeuge_bilder.py ui-shop-layout  # nur ein Bild (Name ohne Endung)
node tools/bilder/render.js                            # alle SVGs -> PNG (1600 x 900)
node tools/bilder/render.js ui-shop-layout             # nur ein PNG
```
| Datei | Inhalt |
|---|---|
| `svglib.py` | Mini-Bibliothek: Grundformen, Texte (mit Breitenmessung), Roblox-Stil-Buttons, Icons (Münze, Edelstein, R$-Platzhalter), Erklär-Kästchen mit Pfeilen, Spielwelt-Hintergrund, Block-Figur, Seltenheitsfarben |
| `bilder_ui.py` | HUD mobil, HUD Simulator, Shop, Inventar, Sammelbuch, Farbpalette, Touch-Größen, Tutorial, Popups |
| `bilder_loops.py` | Core Loop, Loop-Muster, Onboarding-Trichter, Progression/Rebirth, Gacha/Pity |
| `bilder_map.py` | Map-Zonen, Wegführung, Spawn/Hub, Live-Ops-Kalender |
| `bilder_technik.py` | Audio-Mix, Client-Server, Monetarisierung |
| `bilder_konzept.py` | Ideen-Generator, Genre-Übersicht |
| `erzeuge_bilder.py` | Startet alle Bild-Funktionen (`ALLE`-Listen in den Modulen) |
| `render.js` | Öffnet jede SVG in Chromium und speichert einen Screenshot als PNG |

**Neues Bild hinzufügen:** Funktion `def mein_bild(out):` in einem der Module schreiben (Vorlage: eine bestehende Funktion kopieren), mit `sheet(...)` beginnen, am Ende `s.save(out)`, dann in das `ALLE`-Dict des Moduls eintragen. Danach erzeugen, rendern und das PNG ansehen (abgeschnittene Texte? Überlappungen?). Zum Schluss in `assets/bilder/README.md` eintragen.

**Stil-Regeln:** 1600 × 900, Titel oben links, Fußzeile mit Dateiname und Regel, deutsche Beschriftung, nummerierte Erklärungen rechts, Seltenheitsfarben aus `RARITY` in `svglib.py`. Keine Logos, Marken oder Screenshots fremder Spiele.

## Sounds (`tools/audio/`)
```bash
python3 tools/audio/erzeuge_audio.py                 # alle Sounds -> assets/audio/*.wav + *.ogg
python3 tools/audio/erzeuge_audio.py muenze-pling    # nur einen Sound
python3 tools/audio/wellenformen_bild.py             # Übersichtsbild assets/audio/audio-wellenformen.png
```
| Datei | Inhalt |
|---|---|
| `erzeuge_audio.py` | Synthese aller Sounds. Bausteine: Hüllkurven, Sinus-Gleiten, additive Glocken, FM-E-Piano, Bläser, Saw-Pad, FFT-Filter, zeitvariabler Filter (Whoosh), Hall per Faltung, `fold()` für nahtlose Loops. Jeder Sound ist eine Funktion im `SOUNDS`-Dict. |
| `wellenformen_bild.py` | Zeichnet Wellenform + Mini-Spektrogramm jedes Sounds (damit Claude Projects die Sounds „sehen“ kann). Kategorien und Kurzbeschreibungen im `KAT`-Dict. |

**Einstellungen:** 44,1 kHz, 16 Bit, mono, Spitze −1 dBFS, OGG Vorbis Qualität 5. Zufall ist mit festem Seed (`RNG`) gesetzt, d. h. jeder Lauf erzeugt dieselben Dateien.

**Eigene Variante bauen (Beispiel):** Tonhöhe der Münze ändern → in `SOUNDS` eine Zeile `"muenze-tief": lambda: muenze(2 ** (-5 / 12)),` ergänzen, Skript laufen lassen, `wellenformen_bild.py` neu starten und in `assets/audio/README.md` eintragen.

**Loops:** Loop-Namen stehen in `LOOPS`. Sie werden mit Kreis-Faltung (FFT) bzw. Zurückfalten des Ausklangs nahtlos gemacht; nicht nachträglich ein-/ausblenden, sonst entsteht eine Lücke.

## Lizenz
Die Skripte und alle damit erzeugten Bilder und Sounds sind eigene Arbeit und frei nutzbar (auch in eigenen Roblox-Spielen). Beim Hochladen zu Roblox gelten die Upload-Regeln und die Moderation von Roblox.
