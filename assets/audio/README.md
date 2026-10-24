# Eigene Referenz-Sounds (selbst synthetisiert)

> Stand: 2026-10-24 · Alle Sounds in diesem Ordner sind **selbst erzeugt** (Python/numpy: additive Synthese, FM, gefiltertes Rauschen, Hall). Keine Samples aus Spielen, Bibliotheken oder dem Internet.

## Lizenz und Nutzung
- **Frei verwendbar** in deinen eigenen Roblox-Spielen und Projekten, auch kommerziell. Du darfst sie als **eigenes Audio zu Roblox hochladen** und verändern.
- Beim Hochladen gelten die **Roblox-Regeln für Audio-Uploads** (Moderation, Upload-Kontingent, erlaubte Formate und Längen, Freigabe-Einstellungen). Aktuellen Stand vor dem Upload im Creator Hub prüfen.
- Format-Tipp: `.ogg` ist klein und wird von Roblox angenommen; `.wav` ist die verlustfreie Quelle zum Weiterbearbeiten (DAW, Audacity).
- Neu erzeugen oder anpassen: `python3 tools/audio/erzeuge_audio.py` (siehe `tools/README.md`).

## Technische Daten
- WAV: 44,1 kHz, 16 Bit, **mono** (mono ist richtig für 3D-Sounds an Parts; für 2D-UI/Musik egal).
- OGG: Vorbis, Qualität 5 (ca. 100–160 kbit/s).
- Pegel: Spitze auf ca. **−1 dBFS** normalisiert. Die Lautstärke im Spiel regelst du über `Sound.Volume` und `SoundGroup.Volume`.
- One-Shots: weicher Ein- und Ausklang gegen Knackser, Subbass/Gleichanteil unter 25 Hz entfernt.
- Loops (`*-loop*`): **nahtlos** (Hall und Ausklang werden auf den Anfang zurückgefaltet). In Roblox `Sound.Looped = true` setzen.
- Angegebene Dauer = Datei-Länge **inklusive Hall-Ausklang**; der hörbare Kern ist bei Glocken/Fanfaren oft deutlich kürzer.

## Übersicht (beschrieben nach dem Hör-Raster aus `referenz-audio.md`)

![Wellenformen und Spektrogramme aller Sounds](audio-wellenformen.png)

| Datei (.wav + .ogg) | Dauer | Tonhöhe | Schichten | Gefühl | Einsatzzweck | SoundGroup · Volume (Start) |
|---|---|---|---|---|---|---|
| `muenze-pling` | 0,49 s | hell, 2 Töne aufwärts (C6 → G6) | kurzer Anschlag → glockiger Ton mit FM-Glanz | belohnend, leicht | Münze einsammeln, Verkauf | SFX/Belohnung · 0,5 |
| `muenze-pling-variante-1` | 0,48 s | wie oben, −2 Halbtöne | wie oben | etwas ruhiger | Variation gegen Wiederholung | SFX/Belohnung · 0,5 |
| `muenze-pling-variante-2` | 0,48 s | wie oben, +2 Halbtöne | wie oben | heller | Variation, mittlere Menge | SFX/Belohnung · 0,5 |
| `muenze-pling-variante-3` | 0,48 s | wie oben, +4 Halbtöne | wie oben | am hellsten | große Menge, Kombo-Ende | SFX/Belohnung · 0,5 |
| `pling-leiter` | 2,03 s | 5 Glocken steigend (Pentatonik C6–A6) | Ton-Leiter → Funkeln → kurzer Hall | steigende Freude | Kombo, Serie, „mehr und mehr“ | SFX/Belohnung · 0,6 |
| `pop-klein` | 0,14 s | tief, schnell fallend (620 → 170 Hz) | ein runder Plopp + Klick | weich, freundlich | kleine Interaktion, Item aufheben, Blase | SFX · 0,5 |
| `ui-klick` | 0,05 s | mittel-hoch, kurz | Klick-Rauschen + Mini-Ton | trocken, neutral | jeder Button-Klick | UI · 0,4 |
| `ui-oeffnen` | 0,24 s | gleitet aufwärts (420 → 950 Hz) | Gleiten + kleiner Ton + Luft | „auf“, einladend | Menü/Fenster öffnen | UI · 0,5 |
| `ui-schliessen` | 0,24 s | gleitet abwärts (950 → 420 Hz) | Spiegel von `ui-oeffnen` | „zu“, abschließend | Menü/Fenster schließen | UI · 0,5 |
| `ui-fehler` | 0,33 s | tief, 2 Töne fallend (B♭3 → G3) | zwei gedämpfte Summ-Töne | „nein“, aber nicht hart | zu wenig Münzen, Aktion nicht möglich | UI · 0,5 |
| `kauf-erfolg` | 2,44 s | hell, Dur-Akkord aufwärts | Münze → Arpeggio (C-Dur) → Funkeln → Hall | erfolgreich, wertig | Kauf abgeschlossen (nach Roblox-Kaufdialog) | SFX/Belohnung · 0,6 |
| `level-up-fanfare` | 4,11 s | aufsteigende Bläser (G4–C5–E5–G5) → C-Dur-Akkord | Auftakt → Pauke/Becken + Akkord → Funkeln → Hall | triumphal | Level-Up, Rebirth, Zone freigeschaltet | SFX/Belohnung · 0,7 |
| `seltener-drop-mythic` | 6,72 s | Riser steigt → Stille → großer Akkord (C-Dur add9) | Rauschen-Riser + Ton-Riser → **0,28 s Stille** → Boom + Crack → Pad/Bläser → Funkeln → langer Hall | Spannung, dann Gänsehaut | Mythic/Legendary-Fund, Server-Meldung | SFX/Belohnung · 0,8 (Musik kurz ducken) |
| `whoosh-impact` | 1,86 s | Rauschen schwingt hoch/runter → tiefer Schlag | Whoosh → Wumms + Knacken → kurzer Hall | wuchtig, dynamisch | Schwertschlag, Wurf, Dash | SFX · 0,6 |
| `treffer-schwer` | 1,10 s | sehr tief (95 → 38 Hz) mit metallischem Rest | Wumms + verzerrtes Knacken + leiser Klang | hart, schwer | schwerer Treffer, Boss-Schlag, Landung | SFX · 0,6 |
| `ernte-weich` | 0,49 s | mittel, weicher Marimba-Ton (G5) | Plopp + Blätter-Rascheln + Marimba | ruhig, zufrieden | Pflanze ernten, Frucht pflücken (Cozy) | SFX · 0,5 |
| `wachstum-sparkle` | 3,34 s | hoch, zufällige Glöckchen, steigend | Funkeln wird dichter + Schimmer + leises Gleiten | magisch, erwartungsvoll | Pflanze wächst, Mutation, Verzauberung | SFX · 0,5 |
| `nacht-beginnt-warnung` | 5,63 s | sehr tief, Gong + fallende kleine Terz (D4 → H3) | Gong → zwei Bläser-Töne → tiefe Drone → Hall | bedrohlich, ernst | Nacht beginnt, Boss erscheint, Welle startet | SFX/Warnung · 0,8 |
| `alarm-diebstahl` | 2,00 s | Zwei-Ton-Sirene 880/660 Hz, wechselt alle 0,25 s | Sirene mit Tremolo | dringend, alarmierend | Basis wird bestohlen, Gefahr in der Nähe | SFX/Warnung · 0,6 |
| `horror-drone-loop` | 8,00 s (Loop) | sehr tief (55 Hz) mit Schwebung, leiser Tritonus | Drone + Wind-Rauschen + Hall | unheimlich, beklemmend | Horror-Zone, Höhle, Nacht | Ambiente · 0,3 |
| `lofi-loop-menue` | 12,00 s (Loop) | ruhig, Fmaj7–Em7–Dm7–Cmaj7, 80 BPM | E-Piano + Bass + sanfte Drums (Swing) + Vinyl-Knistern | entspannt, cozy | Menü, Lobby, Farming/Cozy-Zonen | Musik · 0,4 |
| `ambiente-wind-loop` | 10,00 s (Loop) | tief bis mittel, Rauschen mit Böen und leisem Heulen | gefärbtes Rauschen + schwankende Böen | offen, kühl, einsam | Berg, Wüste, Eis-Zone, Nacht draußen | Ambiente · 0,3 |
| `ambiente-wasser-loop` | 10,00 s (Loop) | mittel-hoch, Plätschern | Bach-Rauschen + viele kleine Blubber-Töne | frisch, lebendig | Fluss, Brunnen, Wasserfall (als 3D-Sound an einem Part) | Ambiente · 0,35 |
| `countdown-tick` | 0,09 s | mittel-hoch, Holzblock | kurzer Klick + zwei Töne | sachlich, Zeitdruck | Countdown, Timer läuft ab (jede Sekunde) | UI · 0,5 |
| `checkpoint` | 2,19 s | hell, 2 Glocken aufwärts (E6 → H6) | zwei Glocken → Funkeln → Hall | erleichtert, positiv | Obby-Checkpoint, Ziel erreicht | SFX/Belohnung · 0,6 |
| `sprung` | 0,20 s | gleitet aufwärts (240 → 720 Hz) | Gleiten + Oktav-Glanz | federnd, verspielt | Springen, Trampolin, Doppelsprung | SFX · 0,4 |

## So setzt du sie in Roblox ein
1. Datei hochladen (Creator Hub / Asset-Manager in Studio), Moderation abwarten, Asset-ID kopieren.
2. `Sound` anlegen: UI/Musik in `SoundService` oder im Client, Raumklang als Kind eines Parts.
3. `Sound.SoundGroup` setzen (Musik, Ambiente, UI, SFX; darunter optional Belohnung/Warnung), siehe `../bilder/audio-mix-prioritaeten.png`.
4. Häufige Sounds (Münze, Klick) mit Varianten oder zufälligem `PlaybackSpeed` (ca. 0,95–1,08) abspielen, damit sie nicht nerven.
5. Wichtige Sounds vorladen (`ContentProvider:PreloadAsync`) und gleichzeitige Wiedergabe begrenzen (Cooldown pro Sound-Typ).
6. Beim Mythic-Drop die Musik-Gruppe kurz leiser stellen (Ducking), damit Stille und Impact wirken.

## Verknüpfungen
- `06-sound-audio/audio-grundlagen.md` (Prinzipien, Mixing, Genres)
- `assets/referenz-audio.md` (Hör-Raster, Klangmuster, Slots für eigene Notizen)
- `tools/audio/erzeuge_audio.py` (Synthese-Code, jeder Sound ist eine eigene Funktion)
