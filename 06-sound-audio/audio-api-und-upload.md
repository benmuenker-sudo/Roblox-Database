# Audio-API, Mixing-Technik und Upload-Regeln

> Stand: 2026-10-24 · Nächste Prüfung: 2027-01-24 · Gesamt-Vertrauen: ✅ für Klassen, Properties, Wertebereiche, Upload-Limits (Creator Docs und Engine-Referenz, lokal am Quelltext geprüft), 🟡 für Ankündigungen/Presse (Privatsphäre-Datum 2022, Musikpartner), 🟠 für Community-Aussagen, 🧠 für eigene Rezepte und Beispielwerte

## Kurzfassung
Roblox' neues, **modulares Audio-API** funktioniert wie ein Mischpult: Objekte **erzeugen** (`AudioPlayer`, `AudioDeviceInput`, `AudioTextToSpeech`), **verändern** (Effekte wie `AudioFader`, `AudioCompressor`, `AudioEqualizer`, `AudioReverb`), **verbrauchen** (`AudioEmitter`, `AudioDeviceOutput`, `AudioSpeechToText`) und **transportieren** (`Wire`) Audioströme. `Sound`, `SoundGroup` und `SoundEffect` sind offiziell **„discouraged“** ✅ ([Audio objects](https://create.roblox.com/docs/audio/objects)). Upload: **2.000 kostenlose Audio-Imports pro 30 Tage für ID-verifizierte, 100 für unverifizierte Konten**, jede Datei **unter 20 MB und unter 7 Minuten**, `.mp3`/`.ogg`/`.wav`/`.flac`, **≤ 48 kHz**, Mono/Stereo/3.0/5.1 ✅ ([Audio assets](https://create.roblox.com/docs/audio/assets)). Der Creator Store bietet über **100.000** professionell produzierte, frei nutzbare Sounds und Musikstücke ✅ ([Audio](https://create.roblox.com/docs/audio)).

## Warum das wichtig ist
- Das neue API bietet laut Roblox „robustere Funktionalität“; nur damit gibt es z. B. Sidechain-Ducking, Text-to-Speech, Speech-to-Text, akustische Simulation (Okklusion, Beugung, Hall) und Interaktionsgruppen ✅ ([Audio objects](https://create.roblox.com/docs/audio/objects), [AudioEmitter](https://create.roblox.com/docs/reference/engine/classes/AudioEmitter)).
- Upload-Kontingente begrenzen, wie viele eigene Sounds man pro Monat nachlegen kann; die Regeln haben sich seit 2022 geändert (früher 100/Monat auch für verifizierte Konten) ✅/🟡.
- Falsch lizenzierte Musik kann Assets und Spiel gefährden 🧠.

## Referenzbilder
Offizielle Bilder aus der Roblox Creator Documentation (Übersicht: `assets/bilder/offiziell/README.md`):

![2D-Verkabelung](../assets/bilder/offiziell/audio/audio-2d-verkabelung.png)
*AudioPlayer → Wire → AudioDeviceOutput. Quelle: Roblox Creator Docs, CC BY 4.0*

![3D-Verkabelung](../assets/bilder/offiziell/audio/audio-3d-verkabelung.png)
*AudioPlayer → Wire → AudioEmitter; AudioListener → Wire → AudioDeviceOutput. Quelle: Roblox Creator Docs, CC BY 4.0*

![Distanzdämpfungskurve](../assets/bilder/offiziell/audio/audio-distanzdaempfung-kurve.png)
*1,0 bei 0 Studs, 0,5 bei 50 Studs, 0 bei 70 Studs. Quelle: Roblox Creator Docs, CC BY 4.0*

![Mehrere Quellen durch einen Effekt](../assets/bilder/offiziell/audio/audio-effekte-kette.png)
*Drei AudioPlayer über Wires durch einen gemeinsamen Effekt. Quelle: Roblox Creator Docs, CC BY 4.0*

![Effekte in Serie](../assets/bilder/offiziell/audio/audio-effekte-parallel.png)
*Player → Effekt 1 → Effekt 2 → Ausgang; die Reihenfolge verändert den Klang. Quelle: Roblox Creator Docs, CC BY 4.0*

![Legacy-Mix-Baum](../assets/bilder/offiziell/audio/soundgroup-mix-baum.png)
*Legacy-SoundGroup-Baum mit Prioritäten; im neuen API als Fader-Busse nachbauen. Quelle: Roblox Creator Docs, CC BY 4.0*

![RollOff-Kurven (Legacy)](../assets/bilder/offiziell/audio/sound-rolloff-modi-kurven.png)
*Linear, Linear Square, Inverse, Inverse Tapered – im neuen API heißen die Modi `DistanceAttenuationMode`. Quelle: Roblox Creator Docs, CC BY 4.0*

![Volumetrischer Sound (Legacy)](../assets/bilder/offiziell/audio/sound-volumetrisch-diagramm.jpg)
*Klangvolumen umhüllt den Spieler innen, wird außen gerichtet. Quelle: Roblox Creator Docs, CC BY 4.0*

Selbst erstellt: ![Mix-Prioritäten](../assets/bilder/audio-mix-prioritaeten.png) · ![Wellenformen der Referenz-Sounds](../assets/audio/audio-wellenformen.png)

## Details

### 1. Die Objekte im Überblick ✅
Quelle: [Audio](https://create.roblox.com/docs/audio), [Audio objects](https://create.roblox.com/docs/audio/objects), Engine-Referenz.

| Objekt | Rolle | Wichtige Members (aus der Referenz) |
|---|---|---|
| `AudioPlayer` | Lädt und spielt eine Audiodatei (Output-Pin) | `Asset`, `AudioContent`, `AutoLoad`, `AutoPlay`, `Looping`, `LoopRegion`, `PlaybackRegion`, `PlaybackSpeed` (0–20, ändert Tonhöhe), `Volume` (0–10), `TimePosition`, `TimeLength`, `IsPlaying`, `IsReady`, `Play()`, `Stop()`, `GetWaveformAsync()`, Events `Ended`, `Looped` |
| `AudioEmitter` | Virtueller Lautsprecher am Elternobjekt in der 3D-Welt | `DistanceAttenuation`, `SetDistanceAttenuation()`, `DistanceAttenuationMode`, `AngleAttenuation`, `AcousticSimulationEnabled`, `AudioInteractionGroup`, `SimulationFidelity` |
| `AudioListener` | Virtuelles Mikrofon (an Kamera, Attachment oder PVInstance) | `AcousticSimulationEnabled`, `AudioInteractionGroup`, `GetInteractingEmitters()` |
| `AudioDeviceOutput` | Echte Lautsprecher/Kopfhörer; alles, was hier ankommt, ist hörbar | `Player` (optional: nur dieser Spieler hört es; leer = alle) |
| `AudioDeviceInput` | Echtes Mikrofon (Voice) | – |
| `AudioTextToSpeech` | Text → Sprache | `Text` (max. **300 Zeichen** pro Anfrage), `VoiceId` (z. B. `"201"` Deutsch männlich, `"202"` Deutsch weiblich), `Volume` |
| `AudioSpeechToText` | Sprache → Text | – |
| `Wire` | Verbindet Pins | `SourceInstance`, `TargetInstance`, `SourceName`, `TargetName` (meist „Input“, beim Kompressor zusätzlich „Sidechain“), `Connected` (nur `true`, wenn alles gesetzt ist und kein Kreis entsteht) |

- **Listener automatisch:** `SoundService.DefaultListenerLocation` (in Studio setzen; Plugin-Sicherheit, nicht per normalem Skript): `Character` (Attachment an der PrimaryPart, Ausrichtung der Kamera), `Camera` (an `CurrentCamera`), `Default` (bei aktivem Voice über das Audio-API ähnlich `Camera`), `None` (Listener selbst per Skript). Bei `Character`/`Camera` legt die Engine **automatisch** einen `AudioListener`, einen `AudioDeviceOutput` unter `SoundService` und den verbindenden `Wire` an ✅ ([ListenerLocation](https://create.roblox.com/docs/reference/engine/enums/ListenerLocation)).
- **Text-to-Speech als Asset:** wiederholte Ansagen einmal mit `AssetService:CreateAssetAsync()` als Audio-Asset erzeugen, statt jedes Mal die API aufzurufen ✅ ([Audio objects](https://create.roblox.com/docs/audio/objects)).
- Weitere wire-fähige Objekte laut `Wire`-Referenz: `AudioLimiter` (begrenzt Lautstärke), `AudioFilter` (Frequenzen), `AudioGate` (stummt leise Signale), `AudioChannelMixer`/`AudioChannelSplitter`, `AudioRecorder`, `VideoPlayer` ✅ ([Wire](https://create.roblox.com/docs/reference/engine/classes/Wire)).

### 2. Effekte und Wertebereiche ✅
Quelle: [Audio effects](https://create.roblox.com/docs/audio/effects), Engine-Referenz.

| Effekt | Wofür (Doku) | Kern-Properties |
|---|---|---|
| `AudioFader` | Lautstärke vieler Ströme auf einmal → **Bus/Gruppe** | `Volume` 0–10, `Bypass` |
| `AudioCompressor` | Dynamik verringern, konstante Lautstärke, **Ducking** über Sidechain | `Threshold` −60 bis 0 dB, `Ratio` 1–50, `Attack` 0,0001–0,5 s, `Release` 0,01–5 s, `MakeupGain` −30 bis 30 dB, Pins Input + **Sidechain** |
| `AudioEqualizer` | Frequenzbänder, z. B. gedämpfter Regen, Unterwasser | `LowGain`, `MidGain`, `HighGain`, `MidRange` |
| `AudioReverb` | Hall in Innenräumen (Turnhalle, Stadion) | `DecayTime`, `Density`, `Diffusion`, `DryLevel`, `WetLevel`, … |
| `AudioChorus` | Mehrere Stimmen/robotisch | – |
| `AudioDistortion` | Übersteuerung, „Fuzz“ | – |
| `AudioEcho` | Echo (Wände, Höhlen) | – |
| `AudioFlanger` | Sweep/Sci-Fi | – |
| `AudioPitchShifter` | Tonhöhe ohne Tempoänderung (klein ↔ riesig) | – |
| `AudioTremolo` | Lautstärke-Zittern, Wetter-Schwellen | – |
| `AudioAnalyzer` | Lautstärke und Spektrum messen | `PeakLevel`, `RmsLevel`, `SpectrumEnabled`, `WindowSize`, `GetSpectrum()` |

- **Ein Effekt für viele Quellen**: mehrere Player in denselben Effekt verkabeln, statt Effekte zu duplizieren ✅.
- **Reihenfolge zählt**: Chorus → Distortion klingt anders als Distortion → Chorus ✅.
- Zum Vergleich Legacy-Ducking (`CompressorSoundEffect`): `Threshold` −80 bis 0, `Attack`/`Release` 0,001–1 s, `Ratio` 1–50 ✅ ([Sound groups](https://create.roblox.com/docs/sound/groups)).

### 3. Dämpfung und Raumklang ✅
Quelle: [AudioEmitter](https://create.roblox.com/docs/reference/engine/classes/AudioEmitter), [DistanceAttenuationMode](https://create.roblox.com/docs/reference/engine/enums/DistanceAttenuationMode).
- `DistanceAttenuationMode`: `Inverse`, `InverseTapered`, `Linear`, `LinearSquared`, `Custom`. Die Kurve aus `SetDistanceAttenuation()` gilt nur bei `Custom`.
- Kurve = Tabelle `{[Distanz] = Lautstärke}`, Distanzen ≥ 0, Lautstärken 0–1, **bis 400 Punkte**, linear interpoliert, außerhalb der Endpunkte konstant; wird mit allen anderen Dämpfungen multipliziert.
- `AcousticSimulationEnabled` an **Emitter und Listener**: Okklusion (dumpf durch Wände), Beugung (um Ecken), Hall (von Wänden).
- `AudioInteractionGroup`: Emitter und Listener mit gleicher Gruppe hören sich. 🧠 Für getrennte Räume, Minispiele, Team-Funk.

### 4. Code-Rezepte (nur Members aus der Referenz)

**a) 2D-UI-Sound mit eigenem Bus** (LocalScript, z. B. in `StarterPlayerScripts`)
```lua
local SoundService = game:GetService("SoundService")

local function wire(source, target, targetPin)
	local w = Instance.new("Wire")
	w.SourceInstance = source
	w.TargetInstance = target
	if targetPin then
		w.TargetName = targetPin -- z. B. "Sidechain" beim AudioCompressor
	end
	w.Parent = source
	return w
end

local output = Instance.new("AudioDeviceOutput")
output.Parent = SoundService

local uiBus = Instance.new("AudioFader") -- Bus für alle UI-Sounds
uiBus.Name = "UIBus"
uiBus.Volume = 1
uiBus.Parent = SoundService
wire(uiBus, output)

local click = Instance.new("AudioPlayer")
click.Asset = "rbxassetid://0" -- eigene ID von ui-klick eintragen
click.Volume = 0.4
click.Parent = SoundService
wire(click, uiBus)

script.Parent.Activated:Connect(function() -- Script sitzt hier beispielhaft in einem Button
	click.PlaybackSpeed = 0.95 + math.random() * 0.13 -- leichte Variation (🧠 Wertebereich)
	click:Play()
end)
```

**b) 3D-Quelle mit eigener Hörweite** (Wasserfall, `ambiente-wasser-loop`)
```lua
local part = workspace.Wasserfall -- beliebiger Part
local player = Instance.new("AudioPlayer")
player.Asset = "rbxassetid://0"
player.Looping = true
player.Volume = 0.35
player.Parent = part

local emitter = Instance.new("AudioEmitter")
emitter.DistanceAttenuationMode = Enum.DistanceAttenuationMode.Custom
emitter:SetDistanceAttenuation({ [0] = 1, [50] = 0.5, [70] = 0 }) -- Kurve aus der Doku
emitter.Parent = part

local w = Instance.new("Wire")
w.SourceInstance = player
w.TargetInstance = emitter
w.Parent = player
player:Play()
```
Voraussetzung: Ein Listener existiert (z. B. `SoundService.DefaultListenerLocation = Character` in Studio).

**c) Musik ducken, wenn Belohnungen spielen** (Sidechain, Werte 🧠 innerhalb der Doku-Bereiche)
```lua
-- musicBus und rewardBus sind AudioFader, output ein AudioDeviceOutput (siehe a)
local ducker = Instance.new("AudioCompressor")
ducker.Threshold = -30 -- dB, Bereich -60..0
ducker.Ratio = 8       -- Bereich 1..50
ducker.Attack = 0.02   -- s, Bereich 0.0001..0.5
ducker.Release = 0.6   -- s, Bereich 0.01..5
ducker.Parent = SoundService

wire(musicBus, ducker)               -- Musik läuft durch den Kompressor
wire(ducker, output)
wire(rewardBus, output)              -- Belohnungen normal hörbar
wire(rewardBus, ducker, "Sidechain") -- und steuern zugleich das Ducking
```
Doku-Grundlage: Sind Wires am **Sidechain**-Pin angeschlossen, analysiert `Threshold` diese Ströme statt des Inputs – „kann genutzt werden, um einen Strom abhängig von einem anderen zu ducken“ ✅ ([AudioCompressor](https://create.roblox.com/docs/reference/engine/classes/AudioCompressor)). Dass ein Ausgang mehrere Wires speist (hier `rewardBus`), ist im Graph-Modell vorgesehen, steht aber nicht wörtlich in der Doku 🧠 → nach dem Aufbau `Wire.Connected` prüfen.

**d) Lautstärkeregler im Menü** 🧠
```lua
-- slider liefert 0..1; Fader-Volume darf 0..10 sein
local function setBusVolume(bus, value01)
	bus.Volume = math.clamp(value01, 0, 1)
end
```
Werte pro Spieler speichern (DataStore) und beim Join setzen; Regler für Musik, SFX, UI/Sprache getrennt ✅ (Barrierefreiheits-Empfehlung, [Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)).

**e) Ansage per Text-to-Speech** (Deutsch)
```lua
local tts = Instance.new("AudioTextToSpeech")
tts.Text = "Die Nacht beginnt in zehn Sekunden!" -- max. 300 Zeichen
tts.VoiceId = "202" -- Deutsch weiblich laut Stimmenliste
tts.Volume = 1
tts.Parent = game:GetService("SoundService")
-- per Wire an einen AudioFader/AudioDeviceOutput anschließen, dann:
local status = tts:LoadAsync() -- blockiert, bis die Sprache erzeugt ist
if status == Enum.AssetFetchStatus.Success then
	tts:Play()
end
```
`LoadAsync()` erzeugt die Sprachdatei und liefert `Enum.AssetFetchStatus` (`Success`/`Failure`); `Play()`, `Pause()`, `Unload()` existieren laut Referenz ✅ ([AudioTextToSpeech](https://create.roblox.com/docs/reference/engine/classes/AudioTextToSpeech)). Alle TTS-Texte unterliegen den Community Standards ✅ ([Audio objects](https://create.roblox.com/docs/audio/objects)).

### 5. Mix-Architektur (Empfehlung) 🧠 auf Basis offizieller Bausteine
```
AudioPlayer (Musik) ──► Fader "Musik" ──► Compressor (Sidechain ◄── Fader "Belohnung") ──► Fader "Master" ──► AudioDeviceOutput
AudioPlayer (UI)    ──► Fader "UI"    ─────────────────────────────────────────────────► Fader "Master"
AudioPlayer (SFX 3D) ─► AudioEmitter … AudioListener ──► Fader "Welt" ────────────────► Fader "Master"
AudioPlayer (Belohnung) ► Fader "Belohnung" ──────────────────────────────────────────► Fader "Master"
```
| Bus | Startlautstärke (aus `assets/audio/README.md`) | Ducking |
|---|---|---|
| Musik | 0,4 (offizielles Tutorial: Hintergrundmusik 0,2 ✅) | wird von Belohnung/Warnung geduckt |
| Ambiente | 0,3–0,35 | optional von Dialog geduckt |
| UI | 0,4–0,5 | – |
| SFX | 0,4–0,6 | – |
| Belohnung | 0,5–0,8 | duckt Musik |
| Warnung | 0,6–0,8 | duckt Musik und Ambiente |

Prioritäten laut Doku: Spieler-Fähigkeiten wichtiger als Umgebung; offizielles Beispiel High = GUI-Benachrichtigungen/Waffen, Low = Ambience ✅ ([Sound groups](https://create.roblox.com/docs/sound/groups)).

### 6. Upload und Formate ✅
Quelle: [Audio assets](https://create.roblox.com/docs/audio/assets).
| Regel | Wert |
|---|---|
| Kontingent ID-verifiziert | **2.000** kostenlose Audio-Imports pro **30 Tage** |
| Kontingent unverifiziert | **100** pro 30 Tage |
| Tageslimit | entfällt, ersetzt durch das Monatslimit |
| Formate | `.mp3`, `.ogg`, `.wav`, `.flac`; **eine** Spur/ein Stream |
| Größe / Länge | **< 20 MB**, **< 7 Minuten** |
| Samplerate | **≤ 48 kHz** |
| Kanäle | Mono, Stereo 2.0, 3.0 oder 5.1 Surround |
| Wege | Asset Manager in Studio, Creator Dashboard (Development Items → Audio → Upload Asset), Open Cloud (`POST https://apis.roblox.com/assets/v1/assets`, `assetType: "Audio"`) |
| Verarbeitung | Studio **transkodiert** beim Import; Fehler meist durch ungültige Header alter Audio-Tools |
| Moderation | Nach dem Upload in der Warteschlange, zunächst nur für den Uploader sichtbar |

- **Korrekturen:** Die Ankündigung von 2022 nannte 100 Uploads/Monat für verifizierte Konten – überholt. Eine Drittquelle mit „7 MB“ widerspricht den offiziellen 20 MB 🟠.
- **Privatsphäre:** Seit dem **22. März 2022** sind neue Audios standardmäßig privat, bestehende über **6 Sekunden** wurden privat gesetzt 🟡 ([DevForum-Ankündigung](https://devforum.roblox.com/t/1701697); Datum nicht in der aktuellen Doku). Ob kurze Clips < 6 s öffentlich sein können, ist in Community-Threads umstritten 🟠 ([DevForum](https://devforum.roblox.com/t/1-second-long-sfx-cant-be-made-public/1991394)). Aktuell gilt laut Doku: Das **Asset-Privacy-System** sorgt dafür, dass IDs importierter Audios nicht ohne Berechtigung nutzbar sind; man kann Nutzungsrechte an bestimmte Freunde und Spiele vergeben; Audio hat eigene Standardeinstellungen ✅ ([Audio assets](https://create.roblox.com/docs/audio/assets), [Asset privacy](https://create.roblox.com/docs/projects/assets/privacy)).
- **Song oder Soundeffekt:** Uploads werden automatisch klassifiziert. Soundeffekte erscheinen nicht auf der Spielseite, können aber im Creator Store verteilt werden. Ein **Song** erscheint auf der Spielseite, wenn er Moderation und Copyright-Prüfung besteht, Mindestdauer/-wiedergaben/-plattformalter erfüllt, einen sinnvollen Titel hat, der Uploader **ID-verifiziert** ist und die **Audio Terms of Use** akzeptiert hat; Spieler hören dort eine **15-Sekunden-Vorschau**; Sichtbarkeit unter „Configure“ abschaltbar, Feld „Song Artist“ für Mitwirkende ✅ ([Audio assets](https://create.roblox.com/docs/audio/assets)).

### 7. Lizenzierte Musik und Rechte
- **Creator Store:** über 100.000 professionell produzierte Effekte und Tracks „von Top-Audio- und Musikpartnern“, frei nutzbar ✅ ([Audio](https://create.roblox.com/docs/audio)). Im Toolbox-Tab Creator Store → Kategorie Audio → Rechtsklick → **Copy Asset ID** → in `AudioPlayer.Asset` einfügen ✅ ([Audio assets](https://create.roblox.com/docs/audio/assets)).
- **Partnernamen stehen nicht in der Doku.** Laut DevForum/Presse: **APM Music** (seit Mai 2018), **Monstercat** (seit Juli 2020), **DistroKid** (Sep. 2024: Künstler mit eigenen Rechten können zu Roblox vertreiben, Bereich „DistroKid Hits“; vor Nutzung ins Inventar übernehmen), außerdem Pro Sound Effects, Nettwerk, Position Music 🟡 ([DevForum](https://devforum.roblox.com/t/amplify-your-experiences-with-new-music/3164792), [Music Ally](https://musically.com/2024/09/09/roblox-moves-into-music-discovery-with-charts-and-distrokid/)). DistroKid-Konditionen laut Presse: in der Beta keine Tantiemen, 100 % Verlagsrechte nötig, keine PRO-Registrierung 🟡 (ebd.).
- **Video-Thumbnails** dürfen Musik aus dem Roblox-Katalog enthalten, aber keine Musik mit Gesang ✅ ([Thumbnails](https://create.roblox.com/docs/production/publishing/thumbnails)).
- **YouTube-Videos:** Auch lizenzierte APM-Tracks können automatische Copyright-Claims auslösen 🟠 (Community); Roblox-Hilfe dazu: [Using Licensed Music in Videos](https://en.help.roblox.com/hc/en-us/articles/360038525351-Using-Licensed-Music-in-Videos) 🟡.
- Nur hochladen, woran man die Rechte hat, und Community Rules/Terms of Use einhalten ✅ ([Audio assets](https://create.roblox.com/docs/audio/assets)).

### 8. Eigene Sounds aus `assets/audio/` einsetzen
Die Referenz-Sounds dieser Datenbank sind **selbst synthetisiert und frei nutzbar** (auch kommerziell, auch zum Hochladen) – siehe `assets/audio/README.md`.

1. **Datei wählen:** `.ogg` (klein, wird angenommen) für den Upload; `.wav` (44,1 kHz, 16 Bit, mono, Spitze ≈ −1 dBFS) zum Weiterbearbeiten. Beide liegen unter den Limits (< 20 MB, < 7 min, ≤ 48 kHz, Mono erlaubt) ✅.
2. **Hochladen:** Studio → Asset Manager → Import (oder Creator Dashboard). Moderation abwarten, Asset-ID kopieren.
3. **Einbauen (neu):** `AudioPlayer.Asset = "rbxassetid://<ID>"`, per `Wire` an den passenden Fader-Bus (Rezept a/b). Loops (`*-loop`): `Looping = true`.
4. **Lautstärke:** Startwerte aus der Tabelle in `assets/audio/README.md` übernehmen (dort noch als „SoundGroup · Volume“ benannt – gleiche Zahl als `AudioPlayer.Volume` bzw. Fader-Volume verwenden).
5. **Variation:** `muenze-pling` + Varianten 1–3 zufällig wählen oder `PlaybackSpeed` 0,95–1,08 🧠.
6. **Mythic-Drop:** `seltener-drop-mythic` auf den Belohnungs-Bus legen, der per Sidechain die Musik duckt (Rezept c) – so wirken die 0,28 s Stille und der Impact.
7. **3D-Ambiente:** `ambiente-wasser-loop` an einen Part mit `AudioEmitter` (Rezept b); `ambiente-wind-loop` oder `horror-drone-loop` als 2D-Loop auf dem Ambiente-Bus.
8. **Vorladen:** nur `ui-klick`, `ui-oeffnen`, Belohnungs-Sounds; Rest bei Bedarf ✅ (Ladezeit-Empfehlungen, [Improve performance](https://create.roblox.com/docs/performance-optimization/improve)).
9. **Kontingent:** 26 Sounds × 1 Upload liegen weit unter 100 bzw. 2.000 pro 30 Tage ✅.

| Referenz-Sound | Bus | Startwert | Verkabelung |
|---|---|---|---|
| `ui-klick`, `ui-oeffnen`, `ui-schliessen`, `ui-fehler`, `countdown-tick` | UI | 0,4–0,5 | 2D |
| `muenze-pling` (+3 Varianten), `pling-leiter`, `kauf-erfolg`, `checkpoint`, `level-up-fanfare`, `seltener-drop-mythic` | Belohnung | 0,5–0,8 | 2D, duckt Musik |
| `pop-klein`, `sprung`, `ernte-weich`, `wachstum-sparkle`, `whoosh-impact`, `treffer-schwer` | SFX | 0,4–0,6 | eigene Aktionen 2D, fremde Aktionen 3D |
| `nacht-beginnt-warnung`, `alarm-diebstahl` | Warnung | 0,6–0,8 | 2D, duckt Musik/Ambiente |
| `lofi-loop-menue` | Musik | 0,4 | 2D, Loop |
| `horror-drone-loop`, `ambiente-wind-loop` | Ambiente | 0,3 | 2D, Loop |
| `ambiente-wasser-loop` | Ambiente/Welt | 0,35 | 3D am Part, Loop |

### 9. Migration von Legacy-Sound 🧠
| Legacy | Neu |
|---|---|
| `Sound` in `SoundService` | `AudioPlayer` + `Wire` → Fader → `AudioDeviceOutput` |
| `Sound` unter Part | `AudioPlayer` + `AudioEmitter` am Part (Listener per `DefaultListenerLocation`) |
| `Sound.SoundGroup = Musik` | `Wire` vom Player in den Fader „Musik“ |
| `SoundGroup.Volume` | `AudioFader.Volume` |
| `CompressorSoundEffect` zum Ducken | `AudioCompressor` mit Sidechain-Wire |
| `ReverbSoundEffect` / `EqualizerSoundEffect` | `AudioReverb` / `AudioEqualizer` im Signalweg |
| `RollOffMode` | `AudioEmitter.DistanceAttenuationMode` / `SetDistanceAttenuation()` |
| `Sound.PlaybackSpeed`, `Sound.Looped` | `AudioPlayer.PlaybackSpeed`, `AudioPlayer.Looping` |

Schrittweise umstellen (zuerst Musik und UI, dann 3D), alte Systeme laufen weiter.

## Do / Don't
| Do | Don't |
|---|---|
| Neues Audio-API mit Fader-Bussen | Neue Systeme mit `SoundGroup` |
| Ein Effekt für viele Quellen | Pro Sound eigene identische Effekte |
| Sidechain-Ducking für Belohnungen/Warnungen | Musik manuell auf 0 setzen und vergessen |
| Dämpfungskurve passend zur Spielrelevanz | Alles überall hörbar |
| Creator-Store-Audio per Asset-ID in `AudioPlayer` | Store-Audio per Klick als `Sound` einfügen |
| Upload-Limits einplanen (2.000/100 pro 30 Tage) | Hunderte Varianten am Releasetag hochladen |
| Rechte klären, Song-Sichtbarkeit bewusst setzen | Fremde Musik hochladen |
| TTS-Ansagen als Asset speichern | Dieselbe Ansage hundertfach live erzeugen |

## Checkliste
- [ ] `DefaultListenerLocation` in Studio gesetzt (Character oder Camera)
- [ ] Busse: Master, Musik, UI, SFX, Belohnung, Warnung, Ambiente
- [ ] Sidechain-Ducking eingerichtet und mit `Wire.Connected` geprüft
- [ ] 3D-Quellen mit `Custom`-Kurve oder passendem Modus, Okklusion wo sinnvoll
- [ ] Lautstärkeregler pro Bus im Menü, Werte gespeichert
- [ ] Uploads: Format, < 20 MB, < 7 min, ≤ 48 kHz, Kontingent geprüft
- [ ] Rechte und Song-Sichtbarkeit geklärt
- [ ] Referenz-Sounds aus `assets/audio/` mit Startwerten eingebunden

## Offene Fragen / Recherche-Bedarf
- Offizielle Bestätigung, dass ein Pin beliebig viele ausgehende Wires speisen darf (praktisch üblich, Doku-Wortlaut fehlt).
- Grenzen für gleichzeitig spielende `AudioPlayer` und Speicherbedarf pro Stream: nicht in der Doku.
- RDC-2025-Audio-Neuheiten und Musik-Charts nicht ausgewertet.
- Mindestdauer und Mindestwiedergaben für Songs auf der Spielseite: in der Doku nicht beziffert.

## Verknüpfungen
`audio-grundlagen.md`, `assets/audio/README.md`, `assets/referenz-audio.md`, `04-ui-ux/eingabe-und-barrierefreiheit.md`, `04-ui-ux/thumbnails-und-icons.md`

## Quellen
- [Creator Docs: Audio](https://create.roblox.com/docs/audio) – Stand 2026-10-24, ✅
- [Creator Docs: Audio objects](https://create.roblox.com/docs/audio/objects), [Audio effects](https://create.roblox.com/docs/audio/effects), [Audio assets](https://create.roblox.com/docs/audio/assets) – ✅
- [Engine-Referenz: AudioPlayer](https://create.roblox.com/docs/reference/engine/classes/AudioPlayer), [AudioEmitter](https://create.roblox.com/docs/reference/engine/classes/AudioEmitter), [AudioListener](https://create.roblox.com/docs/reference/engine/classes/AudioListener), [AudioDeviceOutput](https://create.roblox.com/docs/reference/engine/classes/AudioDeviceOutput), [AudioFader](https://create.roblox.com/docs/reference/engine/classes/AudioFader), [AudioCompressor](https://create.roblox.com/docs/reference/engine/classes/AudioCompressor), [AudioTextToSpeech](https://create.roblox.com/docs/reference/engine/classes/AudioTextToSpeech), [Wire](https://create.roblox.com/docs/reference/engine/classes/Wire), [SoundService](https://create.roblox.com/docs/reference/engine/classes/SoundService), [ListenerLocation](https://create.roblox.com/docs/reference/engine/enums/ListenerLocation), [DistanceAttenuationMode](https://create.roblox.com/docs/reference/engine/enums/DistanceAttenuationMode) – ✅
- [Creator Docs: Add 2D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio), [Add 3D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) – ✅
- [Creator Docs: Sound groups (Legacy)](https://create.roblox.com/docs/sound/groups), [Sound objects (Legacy)](https://create.roblox.com/docs/sound/objects) – ✅
- [Creator Docs: Asset privacy](https://create.roblox.com/docs/projects/assets/privacy), [Thumbnails](https://create.roblox.com/docs/production/publishing/thumbnails), [Accessibility](https://create.roblox.com/docs/production/publishing/accessibility), [Improve performance](https://create.roblox.com/docs/performance-optimization/improve) – ✅
- [DevForum: Action Needed – Asset Privacy for Audio](https://devforum.roblox.com/t/1701697) – März 2022, 🟡
- [DevForum: Amplify Your Experiences with New Music](https://devforum.roblox.com/t/amplify-your-experiences-with-new-music/3164792) – Sep. 2024, 🟡
- [Music Ally: Roblox moves into music discovery](https://musically.com/2024/09/09/roblox-moves-into-music-discovery-with-charts-and-distrokid/) – Sep. 2024, 🟡
- [Roblox Help: Using Licensed Music in Videos](https://en.help.roblox.com/hc/en-us/articles/360038525351-Using-Licensed-Music-in-Videos) – 🟡
- [DevForum: A simple guide to the Audio API](https://devforum.roblox.com/t/a-simple-guide-to-the-audio-api/3132049), [DevForum: 1 second SFX can't be made public](https://devforum.roblox.com/t/1-second-long-sfx-cant-be-made-public/1991394) – 🟠
