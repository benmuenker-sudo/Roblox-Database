# Sound und Audio: Grundlagen und Gestaltung

> Stand: 2026-10-24 · Nächste Prüfung: 2027-01-24 · Gesamt-Vertrauen: ✅ für Audio-Objekte, Mixing-Hinweise, Barrierefreiheit und Upload-Limits (Creator Docs, lokal am Quelltext geprüft), 🟡 für Presse/DevForum, 🟠 für Community-Zahlen, 🧠 für Gestaltungsprinzipien

## Kurzfassung
Sound macht Aktionen **befriedigend** (Feedback), gibt Zonen **Stimmung** und lenkt **Aufmerksamkeit**. **Wichtigste Korrektur:** Roblox bezeichnet `Sound`, `SoundGroup` und `SoundEffect` inzwischen offiziell als **„discouraged“** zugunsten der neuen, per `Wire` verkabelten **Audio-Objekte** (`AudioPlayer` → Effekte → `AudioEmitter`/`AudioListener` → `AudioDeviceOutput`) ✅ ([Audio objects](https://create.roblox.com/docs/audio/objects)). Neue Projekte bauen den Mix daher mit `AudioFader`-Bussen und `AudioCompressor`-Ducking; Details und Code in `audio-api-und-upload.md`. Für das Spielgefühl gilt weiter: sofort, kurz, klar, mit Variation, wichtige Signale lauter als Ambiente, Ton nie als einziges Signal.

## Warum das wichtig ist
- Roblox: Audio „erhebt“ Spiele, gibt Feedback zu Aktionen und lenkt die Aufmerksamkeit auf das, was Spieler tun müssen ✅ ([Audio](https://create.roblox.com/docs/audio)).
- Feedback wie das „cha-ching“ beim Kauf ist ein offizielles UX-Beispiel ✅ ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)).
- Konsolen: Menünavigation mit Ton-Feedback wertet das Erlebnis auf ✅ ([Console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines)).
- Barrierefreiheit: Spieler brauchen getrennte Lautstärken (SFX, Musik, Sprache), und kein Ereignis darf **nur** über Ton vermittelt werden ✅ ([Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)).
- Audiodateien können „überraschend viel“ Client-Speicher belegen ✅ ([Improve performance](https://create.roblox.com/docs/performance-optimization/improve)).

## Referenzbilder
Selbst erstellte, beschriftete Referenzbilder (frei nutzbar, Übersicht: `assets/bilder/README.md`).

![Audio-Mix-Prioritäten und SoundGroups](../assets/bilder/audio-mix-prioritaeten.png)
![Wellenformen der Referenz-Sounds](../assets/audio/audio-wellenformen.png)

Hinweis: Das selbst erstellte Mix-Bild zeigt den Baum noch als SoundGroups. Dieselbe Hierarchie baut man heute mit `AudioFader`-Bussen (siehe `audio-api-und-upload.md`).

Offizielle Bilder aus der Roblox Creator Documentation (Übersicht: `assets/bilder/offiziell/README.md`):

![2D-Audio-Verkabelung](../assets/bilder/offiziell/audio/audio-2d-verkabelung.png)
*2D: AudioPlayer → Wire → AudioDeviceOutput. Quelle: Roblox Creator Docs, CC BY 4.0*

![3D-Audio-Verkabelung](../assets/bilder/offiziell/audio/audio-3d-verkabelung.png)
*3D: AudioPlayer → AudioEmitter (in der Welt), AudioListener → AudioDeviceOutput. Quelle: Roblox Creator Docs, CC BY 4.0*

![Distanzdämpfung](../assets/bilder/offiziell/audio/audio-distanzdaempfung-kurve.png)
*Lautstärke 1 bei 0 Studs, 0,5 bei 50, 0 bei 70 Studs. Quelle: Roblox Creator Docs, CC BY 4.0*

![Ein Effekt für viele Quellen](../assets/bilder/offiziell/audio/audio-effekte-kette.png)
*Drei AudioPlayer laufen durch einen gemeinsamen Effekt. Quelle: Roblox Creator Docs, CC BY 4.0*

![Mix-Baum mit Prioritäten](../assets/bilder/offiziell/audio/soundgroup-mix-baum.png)
*Prioritäten-Hierarchie: High (GUI, Waffen), Medium (Foley), Low (3D/2D-Ambience) – offizielles Legacy-Beispiel, als Konzept weiter gültig. Quelle: Roblox Creator Docs, CC BY 4.0*

![Volumetrisches Audio in Duvall Drive](../assets/bilder/offiziell/audio/duvall-volumetrisches-audio.jpg)
*Ambience-Zone als Volumen statt Punktquelle. Quelle: Roblox Creator Docs, CC BY 4.0*

## Referenz-Sounds
Selbst synthetisierte Beispiel-Sounds (frei nutzbar, auch zum Hochladen in eigene Spiele; Roblox-Upload-Regeln beachten). Beschreibung nach Hör-Raster und empfohlene Gruppe/Lautstärke: `assets/audio/README.md`. Jede Datei gibt es als `.ogg` und `.wav`. Wie man sie mit dem neuen Audio-API einbaut: `audio-api-und-upload.md`, Abschnitt „Eigene Sounds einsetzen“.

| Rolle | Sounds |
|---|---|
| Feedback/Belohnung | [muenze-pling](../assets/audio/muenze-pling.ogg) · [Variante 1](../assets/audio/muenze-pling-variante-1.ogg) · [Variante 2](../assets/audio/muenze-pling-variante-2.ogg) · [Variante 3](../assets/audio/muenze-pling-variante-3.ogg) · [pling-leiter](../assets/audio/pling-leiter.ogg) · [kauf-erfolg](../assets/audio/kauf-erfolg.ogg) · [checkpoint](../assets/audio/checkpoint.ogg) |
| Belohnungs-Fanfare | [level-up-fanfare](../assets/audio/level-up-fanfare.ogg) · [seltener-drop-mythic](../assets/audio/seltener-drop-mythic.ogg) (Stille vor dem Impact) |
| UI-Sounds | [ui-klick](../assets/audio/ui-klick.ogg) · [ui-oeffnen](../assets/audio/ui-oeffnen.ogg) · [ui-schliessen](../assets/audio/ui-schliessen.ogg) · [ui-fehler](../assets/audio/ui-fehler.ogg) · [pop-klein](../assets/audio/pop-klein.ogg) · [countdown-tick](../assets/audio/countdown-tick.ogg) |
| Kampf/Bewegung | [whoosh-impact](../assets/audio/whoosh-impact.ogg) · [treffer-schwer](../assets/audio/treffer-schwer.ogg) · [sprung](../assets/audio/sprung.ogg) |
| Farming/Cozy | [ernte-weich](../assets/audio/ernte-weich.ogg) · [wachstum-sparkle](../assets/audio/wachstum-sparkle.ogg) |
| Warnsignale | [nacht-beginnt-warnung](../assets/audio/nacht-beginnt-warnung.ogg) · [alarm-diebstahl](../assets/audio/alarm-diebstahl.ogg) |
| Musik (Loop) | [lofi-loop-menue](../assets/audio/lofi-loop-menue.ogg) (12 s, nahtlos) |
| Ambiente (Loop) | [horror-drone-loop](../assets/audio/horror-drone-loop.ogg) · [ambiente-wind-loop](../assets/audio/ambiente-wind-loop.ogg) · [ambiente-wasser-loop](../assets/audio/ambiente-wasser-loop.ogg) |

## Details

### 1. Technische Grundlagen: neu vs. alt ✅
Quelle: [Audio](https://create.roblox.com/docs/audio), [Audio objects](https://create.roblox.com/docs/audio/objects), [Sound objects](https://create.roblox.com/docs/sound/objects), [Sound groups](https://create.roblox.com/docs/sound/groups).

| Aufgabe | Neues Audio-API (empfohlen) | Legacy (discouraged) |
|---|---|---|
| Datei abspielen | `AudioPlayer` (`Asset`, `Looping`, `Volume` 0–10, `PlaybackSpeed` 0–20, `Play()`/`Stop()`) | `Sound` |
| Globaler Ton (Musik, UI) | `AudioPlayer` → `Wire` → `AudioDeviceOutput` | `Sound` in `SoundService`/Client |
| 3D-Ton | `AudioPlayer` → `Wire` → `AudioEmitter` (am Part/Attachment); `AudioListener` → `Wire` → `AudioDeviceOutput` | `Sound` als Kind eines Parts/Attachments |
| Hörweite | `AudioEmitter.DistanceAttenuation` / `SetDistanceAttenuation()` (Kurve, bis 400 Punkte) | `RollOffMode`, `RollOffMin/MaxDistance` |
| Gruppen/Busse | Mehrere Player per Wire in einen `AudioFader` | `SoundGroup` (Volume 0–10) |
| Ducking | `AudioCompressor` mit **Sidechain**-Pin | `CompressorSoundEffect` in SoundGroup |
| Effekte | `AudioEqualizer`, `AudioReverb`, `AudioChorus`, `AudioDistortion`, `AudioEcho`, `AudioFlanger`, `AudioPitchShifter`, `AudioTremolo`, `AudioAnalyzer` | `SoundEffect`-Unterklassen |
| Sprache | `AudioTextToSpeech`, `AudioSpeechToText`, `AudioDeviceInput` (Mikrofon) | – |
| Okklusion/Hall | `AcousticSimulationEnabled` an Emitter **und** Listener | – |

- **Achtung Toolbox:** Ein Klick auf ein Audio im Creator Store fügt in Studio einen **`Sound`** ein, kein `AudioPlayer`; besser „Copy Asset ID“ und in einen `AudioPlayer` einfügen ✅ ([Audio assets](https://create.roblox.com/docs/audio/assets)).
- **Legacy bleibt lauffähig:** Bestehende `Sound`-Systeme funktionieren weiter; für neue Arbeit aber das Audio-API nutzen 🧠 (Doku: „discouraged“, nicht „deprecated“).
- Alte Datei-Aussage „SoundGroups als Grundlage für ein Lautstärke-Menü“ ist damit überholt; dasselbe leisten `AudioFader`-Busse.

### 2. Die Rollen von Audio 🧠
| Rolle | Wirkung | Beispiel | Referenz-Sound |
|---|---|---|---|
| Feedback-SFX | Aktion fühlt sich gut an | Münzen, Treffer, Ernte, Kauf | `muenze-pling`, `ernte-weich` |
| UI-Sounds | Bedienung klar | Klick, Öffnen/Schließen, Fehler | `ui-klick`, `ui-fehler` |
| Belohnungs-Fanfare | Höhepunkt | Seltener Drop, Level-Up | `seltener-drop-mythic`, `level-up-fanfare` |
| Musik | Stimmung, Identität | Zonen-Themen, Menü | `lofi-loop-menue` |
| Ambiente | Raumgefühl | Wind, Wasser, Nacht | `ambiente-wind-loop` |
| Warnsignale | Gefahr | Nacht beginnt, Diebstahl | `nacht-beginnt-warnung` |
| Stimme | Charakter, Barrierefreiheit | NPC-Ansagen, Text-to-Speech | – (TTS, siehe API-Datei) |

### 3. Feedback-Sounds gestalten
- **Sofort** (< 0,1 s nach Aktion), **kurz** (0,1–0,5 s), **klar** 🧠.
- **Wichtiges lauter:** Im offiziellen Platformer-Beispiel ist das Münz-Geräusch lauter als der Sprung, weil es wichtigere Spielinformation trägt; das Hauptziel-Item (Gumdrop) spielt mit **dreifacher** Amplitude (`Volume = 3`) ✅ ([Add 2D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio)). Die Doku betont: „no standards or rules to achieve a great mix“ – nach eigenem Gefühl für Wichtigkeit abstimmen ✅ (ebd.).
- **Startpunkt trimmen:** `AudioPlayer.TimePosition` (Doku-Beispiel `0.15`) springt direkt zum eigentlichen Klang ✅ (ebd.).
- **Tonhöhe steigt mit Wert** 🧠: kleiner Gewinn tiefer, großer heller (`muenze-pling-variante-1` bis `-3` liegen −2, +2, +4 Halbtöne auseinander, siehe `assets/audio/README.md`).
- **Variation:** 3–5 Varianten oder zufälliges `PlaybackSpeed` (ca. 0,95–1,08) gegen Ermüdung 🧠; `PlaybackSpeed` ändert die Tonhöhe ✅ ([AudioPlayer](https://create.roblox.com/docs/reference/engine/classes/AudioPlayer)). Für Tonhöhe ohne Tempoänderung: `AudioPitchShifter` ✅ ([Audio effects](https://create.roblox.com/docs/audio/effects)).
- **Schichten bei großen Momenten:** Anstieg → kurze Stille → Impact → Nachklang (vorgemacht in `seltener-drop-mythic`, 0,28 s Stille) 🧠.
- **Haptik ergänzen** (Gamepad, Mobile): `HapticEffect` z. B. bei Explosionen oder UI-Klicks, sparsam ✅ ([Console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines)).

### 4. Musik 🧠 (mit ✅-Bausteinen)
- Nahtlose Loops (`AudioPlayer.Looping`, optional `LoopRegion`) ✅ (Properties laut [AudioPlayer](https://create.roblox.com/docs/reference/engine/classes/AudioPlayer)).
- Zonen-Themen mit sanfter Überblendung (1–3 s) über die `Volume` zweier Player oder Fader 🧠.
- Dynamik: ruhig beim Sammeln, intensiver bei Gefahr/Boss.
- Musik leiser als Feedback; im offiziellen Tutorial läuft Hintergrundmusik mit `Volume = 0.2` ✅ ([Add 2D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio)).
- Genre: hell für Simulatoren, düster für Horror, sanft für Cozy.
- Spieler-Kontrolle: Musik, SFX, (Sprache) getrennt regelbar, Mute ✅ ([Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)).
- Lizenzierte Musik aus dem Creator Store (über 100.000 Tracks und Effekte) ✅ ([Audio](https://create.roblox.com/docs/audio)); Details zu Lizenzen in `audio-api-und-upload.md`.

### 5. Ambiente und Raumklang
- Quellen in der Welt als 3D-Emitter mit passender Dämpfungskurve: Doku-Beispiel halbiert die Lautstärke bei **50 Studs** und ist bei **70 Studs** stumm ✅ ([Audio objects](https://create.roblox.com/docs/audio/objects)).
- **Okklusion, Beugung, Hall** automatisch mit `AcousticSimulationEnabled` an `AudioEmitter` und `AudioListener` ✅ ([AudioEmitter](https://create.roblox.com/docs/reference/engine/classes/AudioEmitter)).
- **Wer hört was:** `AudioInteractionGroup` an Emitter und Listener – nur gleiche Gruppen hören sich ✅ (ebd.). 🧠 Nutzbar für Räume/Instanzen oder Teams.
- **Volumen-Ambience** (Regen über einem Garten, Bühne): Im Legacy-System über `VolumetricAudio` an einem Part ✅ ([Sound objects](https://create.roblox.com/docs/sound/objects)); offizielles Beispiel aus *The Mystery of Duvall Drive* (Bild oben).
- Räume: `AudioReverb` für Innenräume (Turnhalle, Stadion), `AudioEqualizer` für gedämpften Regen oder Unterwasser ✅ ([Audio effects](https://create.roblox.com/docs/audio/effects)).
- Tag/Nacht unterscheiden, Loops mit Variation 🧠.

### 6. Mischung (Mixing)
- **Prioritäten** 🧠: Warnung > Belohnung > UI > Spieler-Aktionen > Musik > Ambiente. Offiziell: Fähigkeiten-Sounds der Spieler sind „wahrscheinlich viel wichtiger“ als Umgebungsgeräusche; Beispiel-Mix-Baum High (GUI-Benachrichtigungen, Waffen) / Medium (Foley) / Low (3D- und 2D-Ambience) ✅ ([Sound groups](https://create.roblox.com/docs/sound/groups)).
- **Ducking:** Musik leiser, sobald eine GUI-Benachrichtigung oder Dialog spielt; danach zurück ✅ (ebd.). Neu: `AudioCompressor` mit Sidechain-Eingang ✅ ([AudioCompressor](https://create.roblox.com/docs/reference/engine/classes/AudioCompressor)).
- **Busse:** pro Kategorie ein `AudioFader` (Musik, SFX, UI, Ambiente); ein Effekt kann viele Quellen bearbeiten ✅ ([Audio effects](https://create.roblox.com/docs/audio/effects)).
- **Effektreihenfolge** verändert den Klang (z. B. Chorus vor Distortion klingt anders als umgekehrt) ✅ (ebd.).
- **Kompressor** auf Haupt-Bussen gegen Übersteuern; `AudioAnalyzer` (`PeakLevel`, `RmsLevel`, `GetSpectrum()`) zum Messen ✅ (API-Referenz).
- **Normalisierung:** Referenz-Sounds liegen bei ca. −1 dBFS Spitze ✅ (`assets/audio/README.md`, eigene Angabe); offizielle LUFS-Ziele gibt es nicht ✅ (nicht gefunden).
- Auf Handy-Lautsprecher **und** Kopfhörer testen 🧠.

### 7. Barrierefreiheit ✅
Quelle: [Accessibility guidelines](https://create.roblox.com/docs/production/publishing/accessibility).
- **Lautstärkeregler** für Gruppen wie Soundeffekte, Musik und Sprache.
- **Ton nie allein:** Doku-Beispiel klingelndes Telefon – zusätzlich visuell anzeigen (Icon, Partikel, `Highlight`).
- **Text-to-Speech** (`AudioTextToSpeech`, max. 300 Zeichen pro Anfrage, deutsche Stimmen `201`/`202`) für Ansagen ✅ ([Audio objects](https://create.roblox.com/docs/audio/objects)).

### 8. Performance und Limits
- **Speicher:** Audio nicht komplett vorladen, nur was der aktuelle Spielabschnitt braucht ✅ ([Improve performance](https://create.roblox.com/docs/performance-optimization/improve)). Große Musik in `ServerStorage` und erst bei Bedarf zum Client 🧠 (gestützt auf „Keep ReplicatedStorage lean“ ✅).
- **Vorladen** nur kritischer Sounds (`ContentProvider:PreloadAsync()`), z. B. UI-Klick und Belohnung ✅ (Muster „nur nötige Assets“, ebd.).
- **Gleichzeitige Sounds begrenzen:** Eine Community-Quelle nennt ca. 4–5 gleichzeitige Tracks als Faustregel, **nicht offiziell** 🟠. Praxis 🧠: Cooldown pro Sound-Typ, Treffer anderer Spieler nach Distanz/Priorität filtern, ähnliche Sounds zusammenfassen.
- **Ein Effekt für viele Quellen** spart Objekte ✅ ([Audio effects](https://create.roblox.com/docs/audio/effects)).
- **Loops** nur für Musik/Ambiente 🧠.

### 9. Sound-Design nach Genre 🧠
| Genre | Musik | Feedback-SFX | Besonderheit | Passende Referenz-Sounds |
|---|---|---|---|---|
| Simulator | hell, rhythmisch | Münze/Pop/Pling, steigende Töne | Sehr viele Mikro-Belohnungen → Variation Pflicht | `muenze-pling`-Varianten, `pling-leiter`, `pop-klein` |
| Farming/Cozy | sanft, akustisch | weiche Töne, Rascheln | Beruhigend, kein Stress | `ernte-weich`, `wachstum-sparkle`, `lofi-loop-menue` |
| Horror | minimal, Drones | Stille als Waffe, Schreck-Stinger | Dynamik, Pausen, Okklusion | `horror-drone-loop`, `nacht-beginnt-warnung` |
| Kampf/Anime | energetisch | wuchtige Treffer, Whoosh | Impact und Tiefe | `whoosh-impact`, `treffer-schwer` |
| Tycoon | locker, Jazz/Lofi | Kassen, Maschinen | Industrieklang | `kauf-erfolg`, `lofi-loop-menue` |
| Obby | beat-getrieben | Sprung/Checkpoint | Rhythmus passt zur Bewegung | `sprung`, `checkpoint`, `countdown-tick` |
| Steal/Base-Defense | treibend | Alarm, Erfolg | Klare Warnung bei Gefahr | `alarm-diebstahl` |

### 10. Rechte und Upload (Kurzfassung) ✅
- Nur Audio, an dem man die Rechte hat (eigene Produktion, Creator Store, lizenziert) ✅ ([Audio assets](https://create.roblox.com/docs/audio/assets)).
- Upload: **2.000 kostenlose Audio-Uploads pro 30 Tage (ID-verifiziert), 100 (unverifiziert)**; Datei **< 20 MB, < 7 Minuten**, `.mp3`/`.ogg`/`.wav`/`.flac`, ≤ 48 kHz ✅ (ebd.). Die 100/Monat aus der Ankündigung 2022 für verifizierte Konten sind überholt.
- Ausführlich: `audio-api-und-upload.md`.

## Referenzmaterial pflegen
Siehe `assets/referenz-audio.md`: Referenzen sammeln (Beschreibung, was funktioniert, Link). Konkrete Audio-IDs aus dem Creator Store nur eintragen, wenn Lizenz geprüft ist.

## Do / Don't
| Do | Don't |
|---|---|
| Neues Audio-API für neue Projekte | Neue Systeme auf `Sound`/`SoundGroup` aufbauen |
| Jede wichtige Aktion mit sofortigem Feedback-Sound | Stille Buttons und Belohnungen |
| Wichtiges lauter (Münze > Sprung) | Alles gleich laut |
| Varianten / leichte Tonhöhen-Streuung | Ein identischer Sound 500-mal pro Minute |
| Musik per Sidechain-Kompressor ducken | Musik übertönt Belohnungen |
| Getrennte Regler für Musik, SFX, Sprache | Nur ein Master-Mute |
| Ton + visuelles Signal | Wichtige Ereignisse nur hörbar |
| Nur nötige Sounds vorladen | Alle Audios beim Start laden |
| Rechte prüfen, eigene oder Store-Sounds | Fremde Musik hochladen |

## Checkliste
- [ ] Audio-Architektur gewählt: Audio-API (neu) oder bewusst Legacy
- [ ] Jede wichtige Aktion hat Feedback-Sound, Belohnungen klingen nach Wert gestaffelt
- [ ] Häufige Sounds mit Varianten oder Tonhöhen-Streuung
- [ ] Busse pro Kategorie (Musik, SFX, UI, Ambiente) mit Lautstärkereglern im Menü
- [ ] Ducking für Belohnungen/Benachrichtigungen eingerichtet
- [ ] Seltene Drops haben eigenen Moment (Stille → Impact)
- [ ] 3D-Quellen mit Dämpfungskurve, Okklusion wo sinnvoll
- [ ] Kein Ereignis nur über Ton
- [ ] Mix auf Handy-Lautsprecher und Kopfhörer getestet
- [ ] Keine Überlappungs-Kakophonie (Cooldowns, Distanzfilter)
- [ ] Musik loopt sauber
- [ ] Alle Audio-Rechte geklärt, Upload-Kontingent beachtet

## Offene Fragen / Recherche-Bedarf
- Keine offiziellen Vorgaben zu LUFS, Loop-Punkten oder Crossfade-Zeiten.
- Offizielle Obergrenze gleichzeitig spielender Audio-Player: nicht in der Doku.
- RDC-2025-Audio-Neuheiten und Musik-Charts nicht ausgewertet.

## Verknüpfungen
`audio-api-und-upload.md`, `assets/audio/README.md`, `assets/referenz-audio.md`, `04-ui-ux/eingabe-und-barrierefreiheit.md`, `05-map-leveldesign/map-grundlagen.md`

## Quellen
- [Creator Docs: Audio](https://create.roblox.com/docs/audio) – Stand 2026-10-24, ✅
- [Creator Docs: Audio objects](https://create.roblox.com/docs/audio/objects), [Audio effects](https://create.roblox.com/docs/audio/effects), [Audio assets](https://create.roblox.com/docs/audio/assets) – ✅
- [Creator Docs: AudioPlayer](https://create.roblox.com/docs/reference/engine/classes/AudioPlayer), [AudioEmitter](https://create.roblox.com/docs/reference/engine/classes/AudioEmitter), [AudioCompressor](https://create.roblox.com/docs/reference/engine/classes/AudioCompressor) – ✅
- [Creator Docs: Add 2D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) – ✅
- [Creator Docs: Sound objects (Legacy)](https://create.roblox.com/docs/sound/objects), [Sound groups (Legacy)](https://create.roblox.com/docs/sound/groups) – ✅
- [Creator Docs: Accessibility guidelines](https://create.roblox.com/docs/production/publishing/accessibility), [Console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines), [UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design) – ✅
- [Creator Docs: Improve performance](https://create.roblox.com/docs/performance-optimization/improve) – ✅
- Hinweis: Mehrere SEO-Seiten zu „Roblox Sound Guide“ waren unzuverlässig (teils erfundene API-Namen) 🟠, darum hier nur offiziell bestätigte API-Namen.
