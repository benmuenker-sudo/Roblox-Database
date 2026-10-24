# Eingabe und Barrierefreiheit: Input Action System, Gamepad, Konsole, VR, Textgröße, Lokalisierung

> Stand: 2026-10-24 · Nächste Prüfung: 2027-01-24 · Gesamt-Vertrauen: ✅ für alle API-Namen, Werte und Regeln (Creator Docs, lokal am Quelltext geprüft), 🟡 für Ankündigungen und Presse, 🧠 für eigene Schlussfolgerungen

## Kurzfassung
Roblox ist **cross-platform**: Spieler wechseln zwischen Phone, PC, Konsole und VR, und ein Tablet kann gleichzeitig Touch, Gamepad und Tastatur haben ✅ ([Adaptive design](https://create.roblox.com/docs/production/publishing/adaptive-design)). Eingaben laufen am besten über das **Input Action System** (`InputContext` → `InputAction` → `InputBinding` für Tastatur, Gamepad und Touch) und `UserInputService.PreferredInput` ✅ ([Input Action System](https://create.roblox.com/docs/input/input-action-system), [Input](https://create.roblox.com/docs/input)). Für Konsolen plant man aus **8–10 Fuß** Abstand zum TV, mit TV-sicheren Rändern und kurzen Navigationswegen; VR auf Quest zielt auf mindestens **72 FPS** ✅ ([Console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines), [VR guidelines](https://create.roblox.com/docs/production/publishing/vr-guidelines)). Barrierefreiheit heißt: `PreferredTextSize` (ignoriert `TextScaled`), `ReducedMotionEnabled`, `PreferredTransparency`, Farbe nie allein, Ton nie allein, getrennte Lautstärken ✅ ([Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)).

## Warum das wichtig ist
- „Über 26 % der Menschen“ haben laut aktuellen Statistiken eine Form von Behinderung; Barrierefreiheit vergrößert die Zielgruppe ✅ ([Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)).
- „Über 5 % der Menschen weltweit“ haben eine Form von Farbenblindheit ✅ (ebd.).
- Roblox nennt **200 Mio.+ Xbox- und PlayStation-Spieler** als Chance für Konsolen-Releases ✅ ([Console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines)). 2024 lag der Konsolenanteil der Roblox-DAU bei **3 %**, PC 17 %, Mobile 80 % 🟡 ([PocketGamer.biz](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue)).
- Spieler mit aktivierter **automatischer Übersetzung** sehen Spielnamen, Beschreibungen und In-Game-Text übersetzt, selbst wenn der Entwickler nichts eingerichtet hat ✅ ([Localization](https://create.roblox.com/docs/production/localization)).

## Referenzbilder
Offizielle Bilder aus der Roblox Creator Documentation (Übersicht: `assets/bilder/offiziell/README.md`):

![Wireframe Mobile](../assets/bilder/offiziell/ui-design/wireframe-blockin-mobile.png)
![Wireframe PC](../assets/bilder/offiziell/ui-design/wireframe-blockin-pc.png)
*Plattformspezifische Wireframes: auf PC fallen die Touch-Steuerelemente weg. Quelle: Roblox Creator Docs, CC BY 4.0*

![Responsive Layout Hochformat](../assets/bilder/offiziell/ui-design/responsive-layout-hochformat.jpg)
*Hochformat braucht eine andere Anordnung. Quelle: Roblox Creator Docs, CC BY 4.0*

![Flex-Layout-Optionen](../assets/bilder/offiziell/ui-design/flex-layout-horizontal-optionen.png)
*Flex verteilt Restplatz automatisch, ideal für wachsende Texte nach Übersetzung. Quelle: Roblox Creator Docs, CC BY 4.0*

![Styling mit Tokens](../assets/bilder/offiziell/ui-design/styling-selektor-flowchart-klasse.png)
*Tokens und Themes als Grundlage für Style Queries pro Gerät. Quelle: Roblox Creator Docs, CC BY 4.0*

![Highlight durch Wände](../assets/bilder/offiziell/effekte/highlight-immer-sichtbar.jpg)
*Highlight mit `DepthMode = AlwaysOnTop` macht Ziele auch ohne Farbe/Ton auffindbar. Quelle: Roblox Creator Docs, CC BY 4.0*

Selbst erstellt: ![Farben und Bedeutung inkl. Farbenblind-Test](../assets/bilder/ui-farbpalette-bedeutung.png)

## Details

### 1. Die vier Prinzipien des adaptiven Designs ✅
Quelle: [Adaptive design guidelines](https://create.roblox.com/docs/production/publishing/adaptive-design).

| Prinzip | Kern laut Doku | Umsetzung |
|---|---|---|
| **Input fluidity** | Jede Aktion per Gamepad-Taste/D-Pad, Tastatur und Touch auslösbar; Steuerelemente per D-Pad/Stick fokussierbar; Hinweise passen sich an („Press A“, „Pinch“, „Shift+A“) | Input Action System + `InputActionLabel`/`PreferredBinding` |
| **Responsive layout** | Layout ordnet sich nach Größe und Ausrichtung neu, weniger Wichtiges ins Menü, Seitenpanels klappen auf schmalen Screens ein | Flex-Layouts, Style Queries |
| **Dynamic sizing** | Inhalt bestimmt Größe, automatischer Umbruch, Spieler-Einstellungen (Textgröße) respektieren | `AutomaticSize`, `TextWrapped` |
| **Legibility & visual clarity** | Lesbare Schriftgrößen auf kleinen Screens und fernen TVs, hoher Kontrast, klare Hierarchie | Kontrast prüfen, `UITextSizeConstraint` |

Roblox bietet dazu den Beispiel-Place **Interactivity Showcase** ✅ ([Adaptive design](https://create.roblox.com/docs/production/publishing/adaptive-design)).

### 2. Input Action System ✅
Quelle: [Input Action System](https://create.roblox.com/docs/input/input-action-system). Ohne Beta-Label dokumentiert; nur `InputActionLabel` und der „Input Action Manager“ sind als Beta markiert.

**Aufbau**
- `InputContext`: Sammlung zusammengehöriger Aktionen, z. B. `PlayContext` (Spielfigur) und `NavContext` (Menü). `Enabled` schaltet den Kontext. `Priority` + `Sink`: Ein Kontext mit `Sink` „verschluckt“ seine gebundenen Tasten für niedrigere Kontexte (Doku-Beispiel: `Priority = 2000`, damit der eigene `PlayContext` vor den Standard-PlayerScripts greift).
- `InputAction`: eine Spielaktion („Jump“, „Sprint“, „Shoot“). `Type` (`Enum.InputActionType`):

| Typ | Beispiel laut Doku | Rückgabewert |
|---|---|---|
| `Bool` (Standard) | Springen, Schießen, Sprinten | `true`/`false`; Trigger mit `PressedThreshold`/`ReleasedThreshold` |
| `Direction1D` | Gaspedal, Zoom | 0 bis 1 (bzw. 0 bis −1) |
| `Direction2D` | Kamera, Laufen | `Vector2` von (−1,−1) bis (1,1) |
| `Direction3D` | Fluggerät hoch/runter, vor/zurück, seitlich | `Vector3` |
| `ViewportPosition` | Eigener Cursor, Objekte anklicken | Pixelposition im Viewport |

- `InputBinding`: koppelt die Aktion an Hardware über `KeyCode`, zusammengesetzt über `Up`/`Down`/`Left`/`Right` (bei 3D auch `Forward`/`Backward`), `Scale` (z. B. `0.01` für `MouseDelta`/`TouchDelta`) oder `UIButton` (Verweis auf einen Bildschirm-Button für Touch). **Jede Aktion sollte je eine Bindung für Gamepad, Tastatur/Maus und Touch haben.**
- **Events:** `Pressed` und `Released` (nur `Bool`), `StateChanged` (alle Typen). Für dauerhafte Analogwerte (Stick gehalten) feuert `StateChanged` nur einmal → jeden Frame `GetState()` abfragen und mit Delta-Zeit multiplizieren.
- `InputAction.PreferredBinding`: liefert die Bindung, die zum aktuellen Gerät passt, und aktualisiert sich beim Gerätewechsel.
- Für die Standard-Spielerskripte: `Workspace.PlayerScriptsUseInputActionSystem = Enabled` (empfohlen im Doku-Beispiel).
- Ordnerstruktur laut Doku: Ordner `Inputs` in `ReplicatedStorage`, darin die Kontexte.

**Offizielles Sprint-Beispiel (gekürzt):** Bindungen `LeftShift` (Tastatur), `ButtonY` (Gamepad), Touch-Button `SprintButton`. Skript mit `RunContext = Client` direkt unter der Aktion:
```lua
local Players = game:GetService("Players")
local player = Players.LocalPlayer
local character = player.Character or player.CharacterAdded:Wait()
local humanoid = character:WaitForChild("Humanoid")
local defaultWalkSpeed = humanoid.WalkSpeed
local inputAction = script.Parent -- die InputAction "CharacterSprint"

inputAction.Pressed:Connect(function()
	humanoid.WalkSpeed = defaultWalkSpeed * 2
end)
inputAction.Released:Connect(function()
	humanoid.WalkSpeed = defaultWalkSpeed
end)
```

**Kontext beim Menü wechseln** 🧠 (mit offiziellen Bausteinen): Menü öffnen → `NavContext.Enabled = true` (mit `Sink`), `PlayContext.Enabled = false`; Menü schließen → umgekehrt. Die Doku zeigt dafür ein `BindableEvent` `ContextEvent` im `Inputs`-Ordner.

**Bindungen anzeigen** ✅
- Empfohlen: `InputActionLabel` (Beta) – Drag-and-drop-GuiObject; Reihenfolge der Anzeige: eigenes Bild (`InputBinding.DisplayImage`) → Plattform-Bild (`UserInputService:GetImageForKeyCode()`) → eigener Name (`InputBinding.DisplayName`) → Plattform-Text (`UserInputService:GetStringForKeyCode()`) → Platzhalter.
- Fortgeschritten: `PreferredBinding` selbst auswerten und eigene Hinweise bauen.
- Konsole: Button-Icons müssen zum Gerät passen (Xbox vs. PlayStation) ✅ ([Console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines)).

### 3. Eingabegerät erkennen ✅
Quelle: [Input](https://create.roblox.com/docs/input), [Cross-platform development](https://create.roblox.com/docs/projects/cross-platform).
- `UserInputService.PreferredInput` = `Touch`, `KeyboardAndMouse` oder `Gamepad`; richtet sich nach Gerät und zuletzt genutzter Eingabe.
- Nachteile der alten Wege: `TouchEnabled` ist auf Touch-Laptops `true`; `GetLastInputType()` springt zwischen Typen (z. B. `MouseMovement`/`Keyboard`, `Touch`/`Gamepad`) und lässt UI flackern, liefert teils `TextInput`, `Focus`, `InputMethod`.
- Alternativ für Gamepads: `UserInputService.GamepadEnabled`, Events `GamepadConnected`/`GamepadDisconnected` ✅ ([Gamepad input](https://create.roblox.com/docs/input/gamepad)).

```lua
-- LocalScript: Layout an die bevorzugte Eingabe anpassen (Muster aus der Creator Docs)
local UserInputService = game:GetService("UserInputService")

local function onPreferredInputChanged()
	local input = UserInputService.PreferredInput
	if input == Enum.PreferredInput.Touch then
		-- Touch-Buttons zeigen
	elseif input == Enum.PreferredInput.Gamepad then
		-- Touch-Buttons ausblenden, Gamepad-Hinweise zeigen, erstes Element auswählen
	elseif input == Enum.PreferredInput.KeyboardAndMouse then
		-- Tastenhinweise zeigen
	end
end
onPreferredInputChanged()
UserInputService:GetPropertyChangedSignal("PreferredInput"):Connect(onPreferredInputChanged)
```

**Style Queries pro Gerät** ✅ ([Cross-platform development](https://create.roblox.com/docs/projects/cross-platform)): Im Style Editor kann man Tokens automatisch tauschen lassen, z. B. mit `@ViewportDisplaySizeSmall` oder `@PreferredInputTouch` (Textgrößen, Containermaße). Die Doku warnt: 75 % Breite per Scale wird auf 4K-TVs riesig → Größen pro `ViewportDisplaySize` anpassen.

### 4. Gamepad und Konsole ✅
Quelle: [Console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines), [Gamepad input](https://create.roblox.com/docs/input/gamepad), [GuiService](https://create.roblox.com/docs/reference/engine/classes/GuiService), [GuiObject](https://create.roblox.com/docs/reference/engine/classes/GuiObject).

**10-Fuß-Erlebnis**
- Spieler sitzen typischerweise **8–10 Fuß (ca. 2,4–3 m)** vom TV entfernt.
- Relative Größen und Positionen; **zuerst für niedrige Auflösungen** entwickeln; `UISizeConstraint` zum Skalieren; Designs für `GuiService.ViewportDisplaySize = Large` (die meisten TVs); `ScrollingFrame` gegen Überladung beim Hochskalieren.
- **TV-sichere Bereiche:** Manche TVs zeigen den Rand nicht vollständig (Overscan) → wichtige Elemente vom Rand weg. Eine genaue Prozentzahl nennt die Doku nicht ✅; üblich im TV-Bereich sind einige Prozent Rand 🧠.

**Controller-Design**
- Grundnavigation (vier Richtungen, Auswählen, Zurück) muss **jedes** interaktive Element erreichen.
- Roblox bietet **Richtungsauswahl** und **virtuellen Cursor** standardmäßig; für eigene Layouts besser eigene Controller-Navigation.
- Navigation ist **sequenziell**: Wichtige Aktionen dürfen nur wenige Schritte entfernt sein; zusätzliche Shortcut-Tasten für Kernaktionen.
- **Chatfenster auf Konsole deaktivieren** (über `TextChatService` → `ChatWindowConfiguration.Enabled`) ✅ ([Chat window](https://create.roblox.com/docs/chat/chat-window)).
- **Progressive Disclosure:** Seltenes auf zweite Screens.
- **Audio-Feedback** bei Menü-Navigation.
- **Haptik** über `HapticEffect` (z. B. `Type = GameplayExplosion`, `UIClick`), unterstützt auf PlayStation-, Xbox-Gamepads und Quest-Touch-Controllern; sparsam einsetzen.
- **Content-Maturity-Angaben sind für Konsolen-Releases Pflicht.**

**UI-Navigation per Gamepad** ✅ (API-Namen aus der Referenz)
| API | Zweck |
|---|---|
| `GuiService.SelectedObject` | Aktuell fokussiertes GuiObject; kann auf `nil` springen, wenn es den Bildschirm verlässt |
| `GuiService:Select()` | Auswahl auf einen Bereich setzen |
| `GuiService.AutoSelectGuiEnabled` | Select-Taste (oder Backslash) wählt automatisch ein GUI-Element |
| `GuiService.GuiNavigationEnabled` | Standard-Controller-Navigation an/aus |
| `GuiObject.Selectable`, `SelectionOrder` | Ob/in welcher Reihenfolge ein Element fokussierbar ist |
| `GuiObject.NextSelectionUp/Down/Left/Right` | Feste Nachbarn für die Navigation |
| `GuiObject.SelectionImageObject` | Eigener Fokus-Rahmen |

```lua
-- LocalScript: Beim Öffnen eines Menüs per Gamepad den ersten Button fokussieren
local GuiService = game:GetService("GuiService")
local UserInputService = game:GetService("UserInputService")

local function openMenu(menuFrame, firstButton)
	menuFrame.Visible = true
	if UserInputService.PreferredInput == Enum.PreferredInput.Gamepad then
		GuiService.SelectedObject = firstButton
	end
end
```
- Spieler können mit **Backslash** in die UI-Navigation wechseln 🟡 ([Roblox Help](https://en.help.roblox.com/hc/en-us/articles/203314230-In-experience-Settings-and-Help)); die Referenz bestätigt Backslash für `AutoSelectGuiEnabled` ✅.
- **Controller Emulator** in Studio zum Testen ohne echtes Gamepad ✅ ([Gamepad input](https://create.roblox.com/docs/input/gamepad)).
- Gewohnte Belegungen: Die Doku zeigt „Common control schemas“ für Xbox und PlayStation, um über Spiele hinweg konsistent zu bleiben ✅ (ebd.).

### 5. VR ✅
Quelle: [VR guidelines](https://create.roblox.com/docs/production/publishing/vr-guidelines), [VRService](https://create.roblox.com/docs/reference/engine/classes/VRService).
- Backend **OpenXR**, plattformunabhängig (Quest und PC-VR). Tests auf PC-VR gelten auch für Quest 2. Oculus-Treiber brauchen mindestens eine **NVIDIA GTX 1060** oder vergleichbar.
- **Auto Quality Mode** auf Quest zielt auf **mindestens 72 FPS** und skaliert Details automatisch; sieht das schlecht aus, weiter optimieren.
- **Komfort:** Modi Comfort, Default, Expert, Custom; Optionen Vignette, gestufte Drehung, fixe 3rd-Person-Kamera.
- **Kamera:** Standard-Kameraskripte nutzen (bekommen künftige VR-Updates); eigene Kameras müssen Änderungen selbst nachziehen.
- **Performance-Tipps:** Streaming an, wenig Raycasting, `RunService.Heartbeat` statt `task.wait()` für präzise Updates, wenige Draw Calls, wenig Geometrie, wenige teiltransparente Objekte (Decals, Glass), wenige komplexe `SurfaceGui`s, keine tastaturabhängigen Aktionen – stattdessen `InputAction`.
- `VRService:GetUserCFrame(Enum.UserCFrame.LeftHand)` und Event `UserCFrameChanged` für Hand-/Kopfposition ✅.
- Alte Alpha-Empfehlung (2D-ScreenGui minimieren, `SurfaceGui`/`BillboardGui` bevorzugen) ist alt und evtl. überholt 🟠 ([DevForum 2016](https://devforum.roblox.com/t/vr-developer-alpha/22144)).

### 6. Textgröße, Bewegung, Transparenz ✅
Quelle: [Accessibility guidelines](https://create.roblox.com/docs/production/publishing/accessibility).

**Preferred Text Size** (`GuiService.PreferredTextSize`)
| Situation | Verhalten |
|---|---|
| Standard | `Medium`; Spieler können `Large`, `Larger`, `Largest` wählen |
| `TextScaled = true` | Text wird **nicht** nach der Einstellung skaliert |
| `UITextSizeConstraint` | Min/Max werden eingehalten, egal welche Einstellung |
| `AutomaticSize` | Element wächst/schrumpft mit dem Text |
| `TextWrapped` | Text bricht in mehr Zeilen um (innerhalb der absoluten Größe) |
| `TextService:GetTextSize()` / `GetTextBoundsAsync()` | berücksichtigen die Einstellung |

**PreferredTextSize vs. TextScaled – Entscheidungshilfe** 🧠
| Textart | Empfehlung |
|---|---|
| Fließtext, Beschreibungen, Dialoge, Shop-Texte | `TextSize` fest + `TextWrapped` + `AutomaticSize = Y`, Container in `ScrollingFrame` |
| Buttons mit kurzem Wort | `TextSize` + `AutomaticSize = X` oder großzügige Breite; Flex-Layout fängt längere Wörter auf |
| Große Zahlen in fester Box (Währung, Timer) | `TextScaled` + `UITextSizeConstraint` ist vertretbar, folgt dann aber nicht der Einstellung |
| Titel/Logo | Bild oder `TextScaled`, kein Barrierefreiheitsproblem, wenn groß genug |

- Ankündigung als Studio-Beta am 25. Aug. 2025 🟡 ([DevForum](https://devforum.roblox.com/t/introducing-text-scaling-setting-studio-beta/3136967), [Can I Play That](https://caniplaythat.com/2025/08/27/roblox-introduces-global-text-size-accessibility-setting/)); Kritik von Entwicklern, dass UIs ab „Large“ brechen 🟡 ([DevForum](https://devforum.roblox.com/t/preferred-text-scaling-needs-to-be-reverted-abrupt-release-with-no-concerns-addressed-are-disruptive/3911199)).

**Reduced Motion** (`GuiService.ReducedMotionEnabled`): Tween-Zeit auf 0 setzen oder Fade statt Bewegung.
```lua
-- Offizielles Muster (gekürzt): 0,75 s Tween, bei Reduced Motion sofort
local GuiService = game:GetService("GuiService")
local TweenService = game:GetService("TweenService")
local TWEEN_TIME = if GuiService.ReducedMotionEnabled then 0 else 0.75
local info = TweenInfo.new(TWEEN_TIME, Enum.EasingStyle.Cubic, Enum.EasingDirection.Out)
TweenService:Create(script.Parent, info, { Position = UDim2.fromScale(0.5, 0.5) }):Play()
```
Fade-Variante der Doku: Inhalt in eine `CanvasGroup` legen und `GroupTransparency` von 1 auf 0 tweenen. 🧠 Auch Kamerawackeln, Bildschirmblitze und Endlos-Wackelbuttons bei Reduced Motion abschalten.

**Preferred Transparency** (`GuiService.PreferredTransparency`): 1 = Standard, 0 = voll deckend. Empfohlen: `BackgroundTransparency × PreferredTransparency`; offizielles Muster taggt Elemente mit `TransparentBack` (CollectionService) und aktualisiert bei `GetPropertyChangedSignal("PreferredTransparency")`.

### 7. Farbe, Ton, Lautstärke ✅
Quelle: [Accessibility guidelines](https://create.roblox.com/docs/production/publishing/accessibility).
- **Kontrast:** hell auf hell und dunkel auf dunkel vermeiden.
- **Farbe nicht allein:** zusätzlich Symbole/Formen (Doku zeigt Graustufen-Vergleich).
- **Ton nicht allein:** Ereignisse (Beispiel: klingelndes Telefon) zusätzlich visuell anzeigen. Hilfsmittel: `Highlight` mit `DepthMode` ✅ ([Highlighting](https://create.roblox.com/docs/effects/highlighting)), Partikel, UI-Icon.
- **Getrennte Lautstärken** für Gruppen wie Soundeffekte, Musik, Sprache.
- **Text-to-Speech** als Hilfstechnik über `AudioTextToSpeech` (max. 300 Zeichen pro Anfrage, Stimmen u. a. Deutsch männlich `201` / weiblich `202`) ✅ ([Audio objects](https://create.roblox.com/docs/audio/objects)). Mehr in `06-sound-audio/audio-api-und-upload.md`.

### 8. Lokalisierung ✅
Quelle: [Localization](https://create.roblox.com/docs/production/localization), [Automatic translation](https://create.roblox.com/docs/production/localization/automatic-translations), [Localize with scripting](https://create.roblox.com/docs/production/localization/localize-with-scripting), [LocalizationService](https://create.roblox.com/docs/reference/engine/classes/LocalizationService).
- **Einstellungen:** Creator Dashboard → Spiel → Audience → Localization. Eine **Ausgangssprache** (Standard: Kontosprache), beliebig viele **unterstützte Sprachen**.
- **Automatic Text Capture (ATC):** sammelt Texte aus UI, während Spieler spielen oder in Studio getestet wird; neue Strings können **bis zu einige Tage** brauchen; Studio-Erfassung landet in **1–2 Minuten** in der Tabelle. Nur Objekte mit `AutoLocalize = true`; bei `TextBox` nur `PlaceholderText`.
- **ATC erfasst nicht:** Standard-Bestenliste und Chat, Items/Tools im Besitz der Spieler, **Bilder mit eingebettetem Text**, Badge- und Pass-Namen/Beschreibungen von der Plattform.
- **Automatische Übersetzung** füllt nur leere Einträge; manuelle Übersetzungen haben immer Vorrang. Anzeige aktivieren mit „Use Translated Content“.
- **Nicht übersetzen:** `AutoLocalize = false` für NPC-Namen, Straßenschilder, Spielernamen.
- **Skripting:** `LocalizationService:GetTranslatorForPlayerAsync(player)` (asynchron, in `pcall` wickeln) liefert einen `Translator` mit `Translate(kontext, text)` und `FormatByKey(key, args)`; Sprachwechsel über `GetPropertyChangedSignal("LocaleId")` am Translator erkennen.
- **Korrektur zu älteren Notizen:** Nicht die Async-Funktion ist veraltet, sondern **`GetTranslatorForPlayer()` (ohne Async)** – sie ist in der Referenz als „deprecated and should not be used in new work“ markiert ✅ ([LocalizationService](https://create.roblox.com/docs/reference/engine/classes/LocalizationService)).
- RDC 2025 kündigte zusätzliche Sprachwerkzeuge inkl. **Echtzeit-Übersetzung** an 🟡 ([DevForum RDC25](https://devforum.roblox.com/t/rdc25-what-we-announced/3920245)).

```lua
-- LocalScript: Text per Schlüssel übersetzen, mit Fallback (APIs laut Creator Docs)
local LocalizationService = game:GetService("LocalizationService")
local Players = game:GetService("Players")

local ok, translator = pcall(function()
	return LocalizationService:GetTranslatorForPlayerAsync(Players.LocalPlayer)
end)
if ok then
	script.Parent.Text = translator:FormatByKey("Key_Prize_1", { 100 })
else
	warn("Übersetzung nicht verfügbar: " .. tostring(translator))
end
```

**Layout für Übersetzungen** 🧠: Deutsche und französische Texte sind oft deutlich länger als englische → Flex-Layouts (`UIListLayout.HorizontalFlex`, `UIFlexItem`), `AutomaticSize`, keine Texte in Bildern; visuelle Hinweise (Pfeile, Partikel) brauchen keine Übersetzung ✅ (Doku-Argument in [Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques)).

### 9. Flex-Layouts und StyleSheets als Barrierefreiheits-Werkzeug ✅
- `UIListLayout.HorizontalFlex`/`VerticalFlex`, `Wraps`, `ItemLineAlignment`, `UIFlexItem.FlexMode` (Fill, Grow, Shrink, Custom) fangen größere Texte und längere Übersetzungen ab ([List and flex layouts](https://create.roblox.com/docs/ui/list-flex-layouts)).
- StyleSheets mit Tokens erlauben z. B. ein kontrastreiches Theme; Themes müssen dieselben Tokens haben ([UI styling](https://create.roblox.com/docs/ui/styling)).
- Details zu beiden: `ui-grundlagen.md`.

## Beispiele aus echten Spielen
- Konventionen wie „E“-Proximity-Prompt, „C“ zum Ducken, Zahlentasten für die Hotbar – laut Roblox bekannt aus vielen Spielen ✅ ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)). Für Gamepad/Touch braucht jede davon ein Gegenstück.
- *Hello Kitty Cafe*: Spotlight auf einen Button, Rest abgedunkelt – verständlich ohne Text ✅ ([Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques)).

## Do / Don't
| Do | Don't |
|---|---|
| Jede Aktion mit Tastatur-, Gamepad- und Touch-Bindung | Tastatur-only-Aktionen |
| `PreferredInput` / `PreferredBinding` | `TouchEnabled` / `GetLastInputType()` für Layoutwechsel |
| `InputActionLabel` oder plattformgerechte Icons | Xbox-Symbole für PlayStation-Spieler |
| Menü-Kontext mit `Sink` | Spielfigur läuft, während man im Menü navigiert |
| Für 10 Fuß Abstand und `DisplaySize.Large` testen | Phone-Layout 1:1 auf den TV |
| Chatfenster auf Konsole aus | Chatfenster überall lassen |
| `TextWrapped` + `AutomaticSize` für Fließtext | `TextScaled` überall |
| Reduced Motion: Tween-Zeit 0 oder Fade | Pflicht-Kamerawackeln |
| Farbe + Symbol, Ton + Bild | Information nur über Farbe oder nur über Ton |
| `GetTranslatorForPlayerAsync` in `pcall` | Veraltetes `GetTranslatorForPlayer` |
| `AutoLocalize = false` für Namen | Spielernamen automatisch übersetzen lassen |

## Checkliste
- [ ] Alle Aktionen im Input Action System mit drei Bindungen (Gamepad, Tastatur/Maus, Touch)
- [ ] Layout reagiert auf `PreferredInput` (Tablet + Gamepad getestet)
- [ ] Tastenhinweise passen zum Gerät
- [ ] Gamepad: jedes Element erreichbar, erstes Element beim Öffnen fokussiert, B schließt
- [ ] Konsole: TV-Rand frei, `DisplaySize.Large` geprüft, Chatfenster aus, Content Maturity ausgefüllt
- [ ] VR (falls unterstützt): Standard-Kamera, 72 FPS auf Quest, keine Tastaturabhängigkeit
- [ ] Textgröße „Largest“: nichts abgeschnitten
- [ ] Reduced Motion und Preferred Transparency unterstützt
- [ ] Farbe nie allein, Ton nie allein, getrennte Lautstärkeregler
- [ ] Lokalisierung: ATC an, `AutoLocalize` für Namen aus, keine Texte in Bildern, Flex-Layouts

## Offene Fragen / Recherche-Bedarf
- Konkrete Prozentwerte für TV-sichere Ränder nennt die Doku nicht.
- Details zur RDC-2025-Echtzeit-Übersetzung (Verfügbarkeit, Kosten) nicht in der lokalen Doku geprüft.
- Wie viele Spieler `PreferredTextSize` > Medium nutzen: keine Daten.

## Verknüpfungen
`ui-grundlagen.md`, `mobile-first.md`, `hud-shop-menues.md`, `06-sound-audio/audio-api-und-upload.md`, `checklisten/ui-review.md`

## Quellen
- [Creator Docs: Input Action System](https://create.roblox.com/docs/input/input-action-system) – Stand 2026-10-24, ✅
- [Creator Docs: Input](https://create.roblox.com/docs/input), [Gamepad input](https://create.roblox.com/docs/input/gamepad), [Mobile input](https://create.roblox.com/docs/input/mobile) – ✅
- [Creator Docs: Cross-platform development](https://create.roblox.com/docs/projects/cross-platform), [Adaptive design guidelines](https://create.roblox.com/docs/production/publishing/adaptive-design) – ✅
- [Creator Docs: Console development guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines), [Chat window](https://create.roblox.com/docs/chat/chat-window) – ✅
- [Creator Docs: VR guidelines](https://create.roblox.com/docs/production/publishing/vr-guidelines), [VRService](https://create.roblox.com/docs/reference/engine/classes/VRService) – ✅
- [Creator Docs: GuiService](https://create.roblox.com/docs/reference/engine/classes/GuiService), [GuiObject](https://create.roblox.com/docs/reference/engine/classes/GuiObject) – ✅
- [Creator Docs: Accessibility guidelines](https://create.roblox.com/docs/production/publishing/accessibility) – ✅
- [Creator Docs: Localization](https://create.roblox.com/docs/production/localization), [Automatic translation](https://create.roblox.com/docs/production/localization/automatic-translations), [Localize with scripting](https://create.roblox.com/docs/production/localization/localize-with-scripting), [LocalizationService](https://create.roblox.com/docs/reference/engine/classes/LocalizationService) – ✅
- [Creator Docs: List and flex layouts](https://create.roblox.com/docs/ui/list-flex-layouts), [UI styling](https://create.roblox.com/docs/ui/styling), [Highlighting](https://create.roblox.com/docs/effects/highlighting), [Audio objects](https://create.roblox.com/docs/audio/objects) – ✅
- [DevForum: Introducing Text Scaling Setting (Studio Beta)](https://devforum.roblox.com/t/introducing-text-scaling-setting-studio-beta/3136967) – Aug. 2025, 🟡
- [DevForum: Preferred text scaling needs to be reverted](https://devforum.roblox.com/t/preferred-text-scaling-needs-to-be-reverted-abrupt-release-with-no-concerns-addressed-are-disruptive/3911199) – Aug. 2025, 🟡
- [DevForum: RDC25 What we announced](https://devforum.roblox.com/t/rdc25-what-we-announced/3920245) – Sep. 2025, 🟡
- [Roblox Help: In-experience Settings](https://en.help.roblox.com/hc/en-us/articles/203314230-In-experience-Settings-and-Help) – 🟡
- [PocketGamer.biz](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue) – 🟡
- [DevForum: VR developer alpha (2016)](https://devforum.roblox.com/t/vr-developer-alpha/22144) – 🟠 (veraltet)
