# Mobile-First: Safe Area, Touch, Ausrichtung, Performance

> Stand: 2026-10-24 · Nächste Prüfung: 2027-01-24 · Gesamt-Vertrauen: ✅ für ScreenInsets, Touch-Zonen, Ausrichtung, Eingabeerkennung und Performance-Werte (Creator Docs), 🟡 für Plattformanteile (Geschäftsbericht via Fachpresse) und Plattformstandards, 🟠 für Community-Faustregeln, 🧠 für Praxis

## Kurzfassung
**80 % der täglichen Roblox-Nutzer spielten 2024 auf Mobilgeräten, 17 % am PC, 3 % auf Konsole** 🟡 ([PocketGamer.biz nach Roblox-Geschäftsbericht 2024](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue)). Darum zuerst fürs Handy bauen: interaktive UI in `CoreUISafeInsets`, die **reservierten Zonen** von Thumbstick (unten links) und Sprung-Button (unten rechts) freihalten, eigene Aktionen **relativ zum Sprung-Button** platzieren und auf echter Low-End-Hardware messen ✅ ([Position and size](https://create.roblox.com/docs/ui/position-and-size), [Design for performance](https://create.roblox.com/docs/performance-optimization/design)). Der Studio-Emulator ist für Seitenverhältnis und Steuerung gut, **für Speicher aber ungenau** ✅ (ebd.).

## Warum das wichtig ist
- Mobile = Mehrheit der Spieler, aber nur **46 %** des Robux-Umsatzes über App Stores (2024) 🟡 ([PocketGamer.biz](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue)).
- Mobilgeräte haben „starke Speicherbegrenzungen“ und stürzen bei Out-of-Memory ab; Roblox bekommt nie den ganzen Gerätespeicher ✅ ([Design for performance](https://create.roblox.com/docs/performance-optimization/design)).
- Jüngere Spieler spielen eher auf Mobile/Tablet, darum polieren Spiele für diese Zielgruppe die Mobile-UX zuerst ✅ ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)).
- Alte Zahl in dieser Datei („Großteil mobil, Quote prüfen“) ist ersetzt. Eine Drittquelle mit „> 60 % von 144 Mio. DAU“ (2026) widerspricht und wird nicht verwendet 🟠 ([RoLearn](https://rolearn.dev/insights/mobile-first-design-roblox-engagement)).

## Referenzbilder
Selbst erstellte, beschriftete Referenzbilder (frei nutzbar, Übersicht: `assets/bilder/README.md`).

![HUD-Layout Mobile](../assets/bilder/ui-hud-layout-mobile.png)
![Touch-Größen](../assets/bilder/ui-touch-groessen.png)

Offizielle Bilder aus der Roblox Creator Documentation (Übersicht: `assets/bilder/offiziell/README.md`):

![Alle vier ScreenInsets-Regionen](../assets/bilder/offiziell/ui-design/safe-area-inset-regionen-uebersicht.png)
*None, DeviceSafeInsets, CoreUISafeInsets, TopbarSafeInsets auf einem Phone mit Notch. Quelle: Roblox Creator Docs, CC BY 4.0*

![CoreUISafeInsets](../assets/bilder/offiziell/ui-design/safe-area-coreui-safeinsets.png)
*Standard-Bereich für interaktive UI: unter der Top-Bar, innerhalb der Ausschnitte. Quelle: Roblox Creator Docs, CC BY 4.0*

![DeviceSafeInsets](../assets/bilder/offiziell/ui-design/safe-area-device-safeinsets.png)
*Nur Notch/Kamera-Ausschnitt berücksichtigt, reicht bis in die Top-Bar-Zeile. Quelle: Roblox Creator Docs, CC BY 4.0*

![Reservierte Touch-Zonen](../assets/bilder/offiziell/ui-design/touch-reservierte-zonen.png)
*Dynamic-Thumbstick-Zone unten links, Jump-Button-Zone unten rechts. Quelle: Roblox Creator Docs, CC BY 4.0*

![Buttons kreisförmig um den Sprung-Button](../assets/bilder/offiziell/ui-design/daumenzone-buttons-neben-sprung.png)
*Eigene Aktionen dort, wo der rechte Daumen ohnehin ruht. Quelle: Roblox Creator Docs, CC BY 4.0*

![Responsive Layout Querformat](../assets/bilder/offiziell/ui-design/responsive-layout-querformat.jpg)
![Responsive Layout Hochformat](../assets/bilder/offiziell/ui-design/responsive-layout-hochformat.jpg)
*Dieselbe Inventarleiste im Quer- (Leiste) und Hochformat (2er-Raster). Quelle: Roblox Creator Docs, CC BY 4.0*

![HUD auf Tablet ohne und mit Größenlimit](../assets/bilder/offiziell/ui-design/hud-tablet-ohne-groessenlimit.png)
![HUD auf Tablet mit Größenlimit](../assets/bilder/offiziell/ui-design/hud-tablet-mit-groessenlimit.png)
*Ohne `UISizeConstraint` wird die Leiste auf dem Tablet zu hoch, mit Constraint bleibt sie schlank. Quelle: Roblox Creator Docs, CC BY 4.0*

## Details

### 1. Safe Area und Insets ✅
Quelle: [On-screen containers](https://create.roblox.com/docs/ui/on-screen-containers), [ScreenGui](https://create.roblox.com/docs/reference/engine/classes/ScreenGui), [GuiService](https://create.roblox.com/docs/reference/engine/classes/GuiService).

| Wert von `ScreenGui.ScreenInsets` | Was frei bleibt | Wofür |
|---|---|---|
| `CoreUISafeInsets` (Standard) | Top-Bar-Buttons **und** Geräteausschnitte | Alles Interaktive (HUD, Menüs, Shop) – offiziell empfohlen |
| `DeviceSafeInsets` | Nur Ausschnitte (Notch, Kamera); kein Abstand zur Top-Bar | Elemente, die volle Höhe brauchen, aber nicht unter die Notch dürfen |
| `TopbarSafeInsets` | Bereich zwischen Top-Bar-Steuerung und rechtem Rand der Geräte-Safe-Area, wächst horizontal mit | Kleine Anzeigen in der Top-Bar-Zeile |
| `None` | Nichts | Nur nicht-interaktive Hintergründe |

- `GuiService.TopbarInset` liefert den freien Top-Bar-Bereich als `Rect`; er ändert sich (z. B. mit der Gesundheitsanzeige oder `SetCoreGuiEnabled`) → mit `GetPropertyChangedSignal` beobachten ✅.
- `IgnoreGuiInset = true` schaltet `CoreUISafeInsets` auf `DeviceSafeInsets` um ✅. `SafeAreaCompatibility` (Standard `FullscreenExtension`) für neue Arbeit vermeiden ✅.
- Hinweis: Die GuiService-Referenz beschreibt `TopbarInset` als freien Bereich zwischen den **linken** Roblox-Steuerelementen und dem Safe-Area-Rand, die Container-Seite beschreibt `TopbarSafeInsets` als Bereich zwischen Top-Bar-Steuerung und **rechtem** Rand ✅ (vermutlich ist in beiden Fällen der freie Rest der Top-Bar-Zeile gemeint 🧠; kleine Formulierungsunstimmigkeit, [GuiService](https://create.roblox.com/docs/reference/engine/classes/GuiService), [On-screen containers](https://create.roblox.com/docs/ui/on-screen-containers)).

### 2. Reservierte Zonen und Daumen-Zonen ✅
Quelle: [Position and size – Cross-platform factors](https://create.roblox.com/docs/ui/position-and-size).
- **Reserviert:** Die Standard-Steuerung belegt Teile der Ecken unten links (Thumbstick) und unten rechts (Sprung). Dort keine wichtigen Infos oder eigenen Buttons.
- **Daumen:** Die meisten Mobile-Spieler nutzen zwei Daumen, einen am Stick, einen am Sprung-Button. Zu weit von den unteren Ecken entfernt wird unbequem oder unmöglich.
- **Phone vs. Tablet:** Ein Button **40 % unter dem oberen Rand** ist auf dem Phone erreichbar, auf dem Tablet „fast unerreichbar“.
- **Lösung:** Eigene Buttons **relativ zum Sprung-Button** platzieren. Offizielles Beispiel:

```lua
-- Client-Skript in StarterPlayerScripts (gekürzt aus der Creator Docs)
local Players = game:GetService("Players")
local UserInputService = game:GetService("UserInputService")
local playerGui = Players.LocalPlayer:WaitForChild("PlayerGui")

if UserInputService.TouchEnabled then
	while not (playerGui:FindFirstChild("JumpButton", true)
		and playerGui:FindFirstChild("JumpButton", true).IsLoaded) do
		task.wait()
	end
	local jumpButton = playerGui:FindFirstChild("JumpButton", true)
	local customButton = Instance.new("ImageButton")
	customButton.AnchorPoint = Vector2.new(1, 1)
	customButton.Size = UDim2.fromOffset(jumpButton.Size.X.Offset * 0.8, jumpButton.Size.Y.Offset * 0.8)
	customButton.Position = jumpButton.Position + UDim2.fromOffset(-20, jumpButton.Size.Y.Offset)
	customButton.Parent = jumpButton.Parent
end
```
Hinweis: Für die Erkennung „spielt der Nutzer gerade per Touch?“ empfiehlt die Doku inzwischen `UserInputService.PreferredInput`, weil `TouchEnabled` auch auf Laptops mit Touchscreen `true` ist ✅ ([Input](https://create.roblox.com/docs/input)). Das Beispiel oben bleibt für das Finden des Sprung-Buttons gültig.

- **Kontext statt Dauer-Button:** Seltene Aktionen (Tür öffnen, Truhe) über `ProximityPrompt` statt eines ständigen Buttons ✅ (ebd.).
- **Praxis-Zonen 🧠:** Aktionen unten rechts um den Sprung-Button; Bewegung bleibt unten links; Seltenes (Shop, Einstellungen) an den oberen Rändern; Mitte frei (der Daumen verdeckt sonst die Sicht).

### 3. Touch-Regeln
- **Keine offizielle Roblox-Mindestgröße** für Touch-Ziele ✅ (nicht in [UI/UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)).
- Plattformstandards: **44 pt** (Apple), **48 dp** (Android) 🟡 ([W3C](https://www.w3.org/WAI/GL/mobile-a11y-tf/wiki/M2), [Deque](https://docs.deque.com/devtools-mobile/2025.7.2/en/android-touch-target-size)). Community: ≥ 44×44 px, etwa 0,06 Scale auf 1080p, mit `UISizeConstraint.MinSize` erzwingen oder kleine Icons mit unsichtbarer größerer Trefferfläche 🟠 ([creation.dev](https://www.creation.dev/blog/roblox-ui-design-best-practices)).
- **Kein Hover:** Tooltips nur bei Mouseover funktionieren auf Touch nicht → Tippen, langes Drücken oder Info-Button 🟠 (ebd.).
- **Kein Tastatur-/Rechtsklick-Zwang** für Kernfunktionen; jede Aktion per Touch, Gamepad und Tastatur auslösbar ✅ ([Adaptive design](https://create.roblox.com/docs/production/publishing/adaptive-design)).
- **Gesten** nur zusätzlich. Roblox unterstützt `UserInputService.TouchSwipe`, `TouchPinch` sowie Beschleunigungs- und Lagesensor auf Geräten mit `AccelerometerEnabled`/`GyroscopeEnabled` ✅ ([Mobile input](https://create.roblox.com/docs/input/mobile)).
- **Haptik** auf Mobile über `HapticEffect` möglich ✅ (ebd.).
- **Lange Listen:** `ScrollingFrame` mit `AutomaticCanvasSize` ✅ ([Size modifiers](https://create.roblox.com/docs/ui/size-modifiers)).
- **Versehentliches Tippen:** Bestätigung bei Kauf und Löschen 🧠.
- **Ziehbare UI:** `UIDragDetector` als Kind eines GuiObjects, begrenzt über `MinDragTranslation`/`MaxDragTranslation` oder `BoundingUI`/`BoundingBehavior` ✅ ([UI drag detectors](https://create.roblox.com/docs/ui/ui-drag-detectors)).

### 4. Bildschirmgrößen und Ausrichtung ✅
- `GuiService.ViewportDisplaySize` ordnet ein: `Small` (meist Tablet/Mobile/Handheld), `Medium` (Laptops, Monitore), `Large` (meist TVs) ✅ ([DisplaySize](https://create.roblox.com/docs/reference/engine/enums/DisplaySize)).
- **Ausrichtung** ✅ ([Mobile input](https://create.roblox.com/docs/input/mobile)): Standard ist **Querformat** (`LandscapeSensor`: dreht zwischen links/rechts, kein Hochformat). Weitere Modi: `Sensor` (quer und hoch), gesperrt `LandscapeLeft`, `LandscapeRight`, `Portrait`; kein „Portrait upside-down“. Standard über `StarterGui.ScreenOrientation`, zur Laufzeit über `PlayerGui.ScreenOrientation` (z. B. Minispiel im Hochformat), Änderungen über `PlayerGui.CurrentScreenOrientation` erkennen.
- **Responsive Layout** ✅ ([Adaptive design](https://create.roblox.com/docs/production/publishing/adaptive-design)): Weniger wichtige Buttons auf kleinen Screens in ein Menü (Hamburger) verschieben; Seitenpanels auf schmalen Screens einklappen. Hochformat braucht eine **andere Anordnung**, nicht nur Skalierung (offizielles Bild oben).
- **Dynamische Größe** ✅ (ebd.): Inhalt bestimmt Größe (`AutomaticSize`, Umbruch); Textgrößen-Einstellung der Spieler respektieren.
- Werkzeuge: `UIAspectRatioConstraint`, `UISizeConstraint`, `UITextSizeConstraint` (`MinTextSize` nicht unter 9) ✅ ([Size modifiers](https://create.roblox.com/docs/ui/size-modifiers)).
- Keine festen Pixelmaße für ganze Fenster 🧠.

### 5. Eingabewechsel auf Mobilgeräten ✅
Quelle: [Input](https://create.roblox.com/docs/input).
- `UserInputService.PreferredInput` liefert `Touch`, `KeyboardAndMouse` oder `Gamepad` und ändert sich mit der zuletzt genutzten Eingabe. Beispiele der Doku: Phone ohne Zubehör → `Touch`; Tablet mit Bluetooth-Gamepad → `Gamepad`; Mobilgerät mit Bluetooth-Tastatur/Maus → `KeyboardAndMouse`.
- `GetLastInputType()` „thrasht“ zwischen Typen und lässt Layouts flackern; `TouchEnabled` ist kein „ist mobil“-Test.
- Folge 🧠: Touch-Buttons ausblenden, wenn `PreferredInput = Gamepad`, und Gamepad-Hinweise zeigen. Ausführlich: `eingabe-und-barrierefreiheit.md`.

### 6. Performance auf Mobile ✅ (mit 🧠-Ergänzungen)
Quelle: [Design for performance](https://create.roblox.com/docs/performance-optimization/design), [Improve performance](https://create.roblox.com/docs/performance-optimization/improve).

| Thema | Offizielle Aussage | Praxis 🧠 |
|---|---|---|
| Basisgerät | Mindestens ein „baseline device“ wählen, die ganze Entwicklung darauf testen, Frame-Rate und Speicher beobachten | Ein günstiges, 3–4 Jahre altes Android-Phone |
| Beispielgrenze | „unter 1.000 Draw Calls und 1.000.000 Dreiecken“ – ausdrücklich ein **Beispiel** für ein Basisgerät, ermittelt mit Render-Stats | Eigene Grenze messen; Community-Ziel für Mobile: 500 Draw Calls, 500.000 Dreiecke, unter 1,3 GB Client-Speicher 🟡 ([DevForum](https://devforum.roblox.com/t/real-world-building-and-scripting-optimization-for-roblox/3127146), von der offiziellen Doku verlinkt) |
| Emulator | Gut für Seitenverhältnis und Steuerung, **ungenau für Speicher** (Server + Client laufen zusammen) | Speicher nur auf echtem Gerät messen (Developer Console F9) |
| Streaming | Verbessert Join-Zeit, senkt Speicher, erhöht FPS; bei neuen Places Standard | Aktiv lassen, `StreamOutBehavior = Opportunistic` erwägen |
| Frame-Budget | 60 FPS = 16,67 ms pro Frame | Ereignisgesteuert statt pro Frame rechnen |
| Transparenz | Nur 0 oder 1, teiltransparente Überlagerungen (Overdraw) vermeiden | UI-Glas-Effekte sparsam |
| Texturen | 1024² braucht **4×** so viel Grafikspeicher wie 512²; UI-Bilder meist ≤ 512², kleine < 256² | Sprite Sheets für Icons |
| Schatten | Engine schaltet Schatten unter Grafikstufe 4 ab; `CastShadow` an kleinen Teilen aus | Wenige schattenwerfende Lichter |
| Audio | Audiodateien können überraschend viel Speicher kosten, nicht alle auf einmal laden | Musik pro Zone laden |
| Partikel | Decals, Texturen, Partikel batchen schlecht; Property-Änderungen an `ParticleEmitter` teuer | Pets/Effekte bei vielen Spielern reduzieren |
| ReplicatedStorage | Wird vor Spielstart komplett geladen | Große Assets in `ServerStorage` |

- **UI-Tweens:** nicht hunderte gleichzeitig 🧠.
- **Netzwerk:** RemoteEvents bündeln 🧠 (Technik: `08-technik-luau/technik-grundlagen.md`).
- **Mehr zu Licht, Streaming, LOD:** `05-map-leveldesign/beleuchtung-und-performance.md`.

### 7. Messen ✅
Quelle: [Identify performance issues](https://create.roblox.com/docs/performance-optimization/identify), [Design for performance](https://create.roblox.com/docs/performance-optimization/design).
- **Developer Console:** F9 (Speicher, Netzwerk, Skript-Leistung).
- **Render-Stats:** Shift+F2 (Draw Calls, Dreiecke).
- **MicroProfiler:** Ctrl+Alt+F6 (Mac ⌘⌥F6); Frames länger als 16,67 ms finden, Spitzen erkennen.
- **Network Stats / Streaming-Debug:** Shift+F3 im Live-Spiel, dann Shift+1 bis zum vierten Panel ✅ ([Instance streaming](https://create.roblox.com/docs/workspace/streaming)).
- Auf echtem Low-End-Phone testen ✅ ([Test on hardware](https://create.roblox.com/docs/performance-optimization/test-on-hardware)).

## Beispiele aus echten Spielen
- *Spellbound RPG*: minimalistische UI als Vorbild für kleine Screens ✅ ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)).
- *Super Striker League*: wenige, kontextabhängige Buttons ✅ (ebd.).
- Offizielles Bild „Buttons um den Sprung-Button“ (Schwert, Buch) zeigt das empfohlene Muster ✅ ([Position and size](https://create.roblox.com/docs/ui/position-and-size)).

## Do / Don't
| Do | Don't |
|---|---|
| Zuerst auf kleinem Phone testen | Nur am PC/Emulator testen |
| `CoreUISafeInsets` für Buttons | UI unter Notch oder Top-Bar |
| Buttons relativ zum Sprung-Button | Buttons 40 % von oben (auf Tablets unerreichbar) |
| Reservierte Zonen frei lassen | Eigene UI über Stick/Sprung legen |
| `PreferredInput` für Eingabe-Layouts | `TouchEnabled` als „ist mobil“-Test |
| Proximity Prompts für seltene Aktionen | Dauer-Buttons für alles |
| Hochformat neu anordnen | Querformat-Layout nur stauchen |
| Speicher auf echtem Gerät messen | Speicherwerte aus Studio glauben |
| Tooltips per Tippen/Info-Button | Hover-only Tooltips |

## Checkliste
- [ ] Auf kleinem Phone: alles lesbar, nichts abgeschnitten
- [ ] Notch/Top-Bar verdeckt nichts Wichtiges (alle vier Inset-Arten bewusst gewählt)
- [ ] Reservierte Zonen (Stick, Sprung) frei
- [ ] Häufige Buttons mit dem rechten Daumen erreichbar, auch auf Tablet
- [ ] Kauf-Flow komplett mit Touch
- [ ] Menü ohne Tastatur schließbar
- [ ] Bluetooth-Gamepad am Tablet: Layout wechselt, Touch-Buttons verschwinden
- [ ] Ausrichtung festgelegt (`StarterGui.ScreenOrientation`), Hochformat geprüft, falls unterstützt
- [ ] Basisgerät definiert, FPS und Speicher dort gemessen
- [ ] Textgröße „Largest“ getestet

## Offene Fragen / Recherche-Bedarf
- Offizielle Geräteaufteilung 2025/2026.
- Offizielle Speicherobergrenze für Mobile: nicht in der Doku.

## Verknüpfungen
`ui-grundlagen.md`, `hud-shop-menues.md`, `eingabe-und-barrierefreiheit.md`, `05-map-leveldesign/beleuchtung-und-performance.md`, `checklisten/ui-review.md`

## Quellen
- [Creator Docs: Position and size (Cross-platform factors)](https://create.roblox.com/docs/ui/position-and-size) – Stand 2026-10-24, ✅
- [Creator Docs: On-screen UI containers](https://create.roblox.com/docs/ui/on-screen-containers), [ScreenGui](https://create.roblox.com/docs/reference/engine/classes/ScreenGui), [ScreenInsets](https://create.roblox.com/docs/reference/engine/enums/ScreenInsets), [GuiService](https://create.roblox.com/docs/reference/engine/classes/GuiService), [DisplaySize](https://create.roblox.com/docs/reference/engine/enums/DisplaySize) – ✅
- [Creator Docs: Mobile input](https://create.roblox.com/docs/input/mobile), [Input](https://create.roblox.com/docs/input) – ✅
- [Creator Docs: Adaptive design guidelines](https://create.roblox.com/docs/production/publishing/adaptive-design) – ✅
- [Creator Docs: Size modifiers](https://create.roblox.com/docs/ui/size-modifiers), [UI drag detectors](https://create.roblox.com/docs/ui/ui-drag-detectors) – ✅
- [Creator Docs: Design for performance](https://create.roblox.com/docs/performance-optimization/design), [Improve performance](https://create.roblox.com/docs/performance-optimization/improve), [Identify performance issues](https://create.roblox.com/docs/performance-optimization/identify), [Test on hardware](https://create.roblox.com/docs/performance-optimization/test-on-hardware) – ✅
- [Creator Docs: HUD-Meter-Tutorial](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) – ✅
- [PocketGamer.biz: 80 % of Roblox users are on mobile](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue) – 🟡
- [DevForum: Real World Building and Scripting Optimization](https://devforum.roblox.com/t/real-world-building-and-scripting-optimization-for-roblox/3127146) – 🟡
- [W3C](https://www.w3.org/WAI/GL/mobile-a11y-tf/wiki/M2), [Deque](https://docs.deque.com/devtools-mobile/2025.7.2/en/android-touch-target-size) – 🟡
- [creation.dev](https://www.creation.dev/blog/roblox-ui-design-best-practices), [RoLearn](https://rolearn.dev/insights/mobile-first-design-roblox-engagement) – 🟠
