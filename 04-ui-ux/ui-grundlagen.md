# UI-Grundlagen

> Stand: 2026-10-24 · Nächste Prüfung: 2027-01-24 · Gesamt-Vertrauen: ✅ für API-Namen, Eigenschaften und Doku-Zitate (Creator Docs, lokal geprüft am Quelltext `Roblox/creator-docs`, Commit `4e795e6`), 🟡 für Plattform-Anteile aus dem Geschäftsbericht via Fachpresse, 🟠 für Community-Faustregeln, 🧠 für Designprinzipien

## Kurzfassung
Gutes Roblox-UI ist **lesbar auf dem Handy**, **zeigt das Wichtigste zuerst**, **reagiert sofort** und **passt sich jeder Bildschirmgröße und jedem Eingabegerät an**. 2024 spielten im Schnitt **80 % der täglichen Nutzer auf Mobilgeräten, 17 % am PC und 3 % auf Konsole** 🟡 ([PocketGamer.biz nach Roblox-Geschäftsbericht 2024](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue)). Roblox selbst nennt fünf UI-Prinzipien: **Priorisierung, Aufmerksamkeit, visuelle Sprache, Konventionen, Konsistenz** ✅ ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)). Technisch gilt: interaktive UI in `ScreenInsets = CoreUISafeInsets`, Scale statt Offset, Flex-Layouts und Constraints, Text ohne `TextScaled`, wenn er der Spieler-Textgröße folgen soll ✅ ([On-screen containers](https://create.roblox.com/docs/ui/on-screen-containers), [Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)).

## Warum das wichtig ist
- UI ist laut Roblox „oft der wichtigste Kommunikationsweg“ des Spiels; schlechtes UI führt zu Verwirrung und schlechter Retention, gutes UI trägt zu Engagement und Monetarisierung bei ✅ ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)).
- Mobile ist die Mehrheit (80 % DAU 2024), brachte aber nur **46 % des Robux-Umsatzes** über App Store/Google Play 🟡 ([PocketGamer.biz](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue)). Folge 🧠: Phone-first bauen, PC/Konsole als Anpassung, aber die Kauf-Flows auf allen Geräten polieren.
- Eine Drittquelle behauptet „über 60 % von 144 Mio. DAU“ seien mobil (Feb. 2026) 🟠 ([RoLearn](https://rolearn.dev/insights/mobile-first-design-roblox-engagement)). Widerspricht der 80-%-Zahl, nicht verwenden. Eine offizielle Geräteaufteilung für 2025/2026 ist in der Doku nicht zu finden ✅ (geprüft: [Roblox user base](https://create.roblox.com/docs/production/roblox-user-base) nennt keine Plattformanteile).

## Referenzbilder
Selbst erstellte, beschriftete Referenzbilder (frei nutzbar, Übersicht: `assets/bilder/README.md`).

![Farben und ihre Bedeutung](../assets/bilder/ui-farbpalette-bedeutung.png)
![Touch-Größen und Schriftgrößen](../assets/bilder/ui-touch-groessen.png)
![HUD-Layout Mobile](../assets/bilder/ui-hud-layout-mobile.png)

Offizielle Bilder aus der Roblox Creator Documentation (Übersicht: `assets/bilder/offiziell/README.md`):

![Alle vier ScreenInsets-Regionen auf einem Smartphone mit Notch](../assets/bilder/offiziell/ui-design/safe-area-inset-regionen-uebersicht.png)
*Alle vier ScreenInsets-Regionen (None, DeviceSafeInsets, CoreUISafeInsets, TopbarSafeInsets) übereinander. Quelle: Roblox Creator Docs, CC BY 4.0*

![Flex-Modi von UIListLayout](../assets/bilder/offiziell/ui-design/flex-layout-horizontal-optionen.png)
*HorizontalFlex-Modi None, Fill, SpaceAround, SpaceBetween, SpaceEvenly. Quelle: Roblox Creator Docs, CC BY 4.0*

![Styling-Ablauf Tokens, Theme, StyleSheet](../assets/bilder/offiziell/ui-design/styling-selektor-flowchart-klasse.png)
*Tokens → Theme → StyleSheet mit Klassen-Selektor → Frame. Quelle: Roblox Creator Docs, CC BY 4.0*

![9-Slice-Konzept](../assets/bilder/offiziell/ui-design/9-slice-konzept.png)
*9-Slice: Ecken bleiben fix, Kanten und Mitte strecken sich. Quelle: Roblox Creator Docs, CC BY 4.0*

![Konsistente visuelle Sprache im Stats-Menü](../assets/bilder/offiziell/ui-design/uiux-visuelle-sprache-stats.jpg)
*Jede Stat-Kategorie mit eigener Farbe und Icon-Familie (Winds of Fortune). Quelle: Roblox Creator Docs, CC BY 4.0*

![User-Flow-Diagramm](../assets/bilder/offiziell/ui-design/user-flow-diagramm.jpg)
*User Flow eines Laser-Tag-Spiels vor dem UI-Design. Quelle: Roblox Creator Docs, CC BY 4.0*

## Details

### 1. Die fünf offiziellen UI-Prinzipien ✅
Quelle aller Punkte dieses Abschnitts: [UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design).

| Prinzip | Was die Doku sagt | Praxis-Übersetzung 🧠 |
|---|---|---|
| **Priorisierung** („Hierarchy of Information“) | Das Wichtigste zuerst. Leitfragen: Was tut der Spieler gerade? Was muss er wissen? Welche Entscheidungen hat er? Wie oft? UI kann je nach Kontext Buttons austauschen. | Pro Spielzustand (Laufen, Kampf, Shop, Handel) eine eigene Button-Auswahl, nicht alles gleichzeitig |
| **Aufmerksamkeit** | Werkzeuge: **Farbe** (kräftig = wichtig), **Größe**, **Freiraum** (Padding), **Nähe** (Gruppierung), **Bewegung** (Animation, Partikel, wackelnde Buttons). „Moderation is key“. | Höchstens 1 animiertes Element pro Bildschirm gleichzeitig |
| **Visuelle Sprache** | Konsistente Formen, Farben, Stile für Icons, Buttons, Text; in einem **Style Guide** dokumentieren. Buttons brauchen einen Container (Fläche um Text/Icon), Highlights/Schatten deuten 3D-Tiefe an. | Style Guide als StyleSheet-Tokens umsetzen (siehe Abschnitt 6) |
| **Konventionen** | Beispiele: **X** schließt Dialog, **Grau** = nicht nutzbar, **Schloss-Icon** = noch nicht freigeschaltet. | Genre-Hits spielen und deren Konventionen übernehmen, bevor man eigene erfindet |
| **Konsistenz** | Beispiele: „Health“ überall grün; Item-Namen in NPC-Dialogen fett; Schließen-Buttons immer quadratisch, rot, weißes X, oben rechts; Preis rot, wenn unbezahlbar. | Diese Regeln in `checklisten/ui-review.md` abhaken |

**Offizielle Beispiele aus echten Spielen** ✅ ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)):
- *Spellbound RPG*: minimalistische UI, wichtig für kleine Mobile-Screens.
- *Super Striker League*: kontextabhängige Buttons (ohne Ball: Sprint/Tackle; mit Ball: Deke/Pass).
- *The Survival Game*: Gesundheit und Hunger immer sichtbar, Karte, Inventar, Werkzeuge schnell erreichbar.
- *Jailbreak*: goldener Streifen unter Season-Pass-exklusiven Belohnungen.
- *Dragon Adventures*: wertvollstes Münzpaket größer und mit mehr Padding.
- *Tower Defense Simulator*: Größe und Nähe trennen Daily Skins von Daily Crates.

### 2. UX: Interaktionen und Flows ✅
Quelle: [UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design).
- **Zielgruppe verstehen:** Demografie (jüngere Spieler eher auf Mobile/Tablet), Erfahrungslevel, Genre-Vertrautheit, Spielstil.
- **Interaktionen** stützen sich auf **Konventionen** (z. B. „E“-Proximity-Prompt, „C“ zum Ducken, Zahlentasten für die Hotbar, in Kreise laufen zum Anstellen), **Metaphern** (Zauber als Kartendeck in *Spellbound RPG*) und **Feedback** (Treffer-Animation, Button-Zustände Hover/Gedrückt/Losgelassen, „cha-ching“ beim Kauf, Fortschrittsbalken).
- **Flows** mit wenig **Reibung** (friction = Aufwand bis zum Ziel). Beispiel *Berry Avenue RP*: Avatar-Button → Kategorie → scrollen → Item antippen → Done. Vor dem Bau ein **Flussdiagramm** zeichnen.
- Roblox empfiehlt, Button-Platzierungen und HUD-Layouts mit **Experiments** zu testen und plattformspezifische UI oder saisonale Themes mit **Configs** live umzuschalten ✅.

### 3. Container: ScreenGui richtig einsetzen ✅
Quelle: [On-screen containers](https://create.roblox.com/docs/ui/on-screen-containers), [ScreenGui](https://create.roblox.com/docs/reference/engine/classes/ScreenGui).

| Eigenschaft | Verhalten laut Doku | Empfehlung |
|---|---|---|
| `ScreenGui.ScreenInsets` | `CoreUISafeInsets` (Standard): frei von Top-Bar-Buttons und Ausschnitten, „empfohlen, wenn der ScreenGui interaktive Elemente enthält“. `DeviceSafeInsets`: nur Ausschnitte (Notch), kein Abstand zur Top-Bar. `TopbarSafeInsets`: zwischen Top-Bar-Steuerung und rechtem Rand der Geräte-Safe-Area, passt sich horizontal an. `None`: keine Insets, nur für nicht-interaktive Inhalte wie Hintergründe. | Ein ScreenGui pro Zweck; HUD und Menüs in `CoreUISafeInsets` |
| `ScreenGui.IgnoreGuiInset` (alt) | Standard `false` = `CoreUISafeInsets`. Wird es auf `true` gesetzt, während `CoreUISafeInsets` aktiv ist, springt `ScreenInsets` auf `DeviceSafeInsets`. | Für neue Arbeit `ScreenInsets` nutzen |
| `ScreenGui.SafeAreaCompatibility` | Standard `FullscreenExtension` (automatische Anpassung „fullscreen“ GuiObjects an Ausschnitte); Doku rät, das für neue Arbeit zu vermeiden und stattdessen `ScreenInsets` zu nutzen. | Bewusst setzen |
| `ScreenGui.ClipToDeviceSafeArea` | Schneidet an der Geräte-Safe-Area ab. | Für Hintergründe ggf. aus |
| `ScreenGui.DisplayOrder` | Z-Reihenfolge mehrerer ScreenGuis; Modal braucht höheren Wert als Haupt-UI. | HUD 0, Menüs 10, Modals 20, Toasts 30 🧠 |
| `ScreenGui.Enabled` | `false`: kein Rendern, keine Eingabe, keine Updates. | Menüs per `Enabled` schalten statt per Transparenz |
| `ScreenGui.ResetOnSpawn` | Standard `true`: UI wird bei jedem Respawn neu geklont. Nur wenn `false` **und** direktes Kind von `StarterGui`, bleibt sie erhalten. | Für HUD/Shop `false`, sonst gehen Zustände beim Tod verloren 🧠 |
| `GuiService.TopbarInset` | `Rect` des freien Bereichs in der Top-Bar; ändert sich dynamisch, deshalb mit `GetPropertyChangedSignal` beobachten. | Für Elemente in der Top-Bar-Zeile |

Standard-UI von Roblox, die man mit `StarterGui:SetCoreGuiEnabled()` ausblenden kann ✅ ([On-screen containers](https://create.roblox.com/docs/ui/on-screen-containers)): `PlayerList`, `Health` (nur sichtbar, wenn nicht volle Gesundheit), `Backpack` (nur mit Tools), `Chat`, `EmotesMenu`, `SelfView`, `Captures`, `AvatarSwitcher`. Touch-Steuerung: `GuiService.TouchControlsEnabled = false`.

```lua
-- LocalScript: eigene Lebensleiste und eigenes Inventar statt Standard-UI (APIs laut Creator Docs)
local StarterGui = game:GetService("StarterGui")
StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.Health, false)
StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.Backpack, false)
```

### 4. Position und Größe ✅
Quelle: [Position and size](https://create.roblox.com/docs/ui/position-and-size), [Size modifiers](https://create.roblox.com/docs/ui/size-modifiers).
- `UDim2` besteht pro Achse aus **Scale** (Prozent des Containers) plus **Offset** (Pixel). Studio interpretiert `0.5` als Scale und `20` als Offset.
- `AnchorPoint` (0–1) ist der Ursprung für Position und Größe; `(0.5, 0.5)` = Mitte. Für Elemente an Rändern: Anker in die passende Ecke, z. B. `(1, 1)` unten rechts 🧠.
- `ZIndex` plus `ScreenGui.ZIndexBehavior` steuern Überlagerung.
- **Constraints:**
  - `UISizeConstraint` (`MinSize`/`MaxSize` in Pixeln, z. B. 200×200 bis 400×400). Überschreibt Layouts.
  - `UITextSizeConstraint` (`MinTextSize`/`MaxTextSize`). Die Doku warnt: **`MinTextSize` nicht unter 9**, sonst für viele schwer lesbar ✅.
  - `UIAspectRatioConstraint` (`AspectRatio` 2 = 2:1; 1 verhindert Verzerrung quadratischer Bilder). Überschreibt Layouts.
  - `UIScale` multipliziert die `AbsoluteSize` (z. B. 2 = doppelt).
- `GuiObject.AutomaticSize` (`X`, `Y`, `XY`) passt Container an den Inhalt an; `Size` ist dann die **Mindestgröße**. Bei `ScrollingFrame` heißt das Gegenstück `AutomaticCanvasSize`. Mit `TextWrapped` + `AutomaticSize = Y` wächst ein Label mit umbrechendem Text nach unten.
- Offizielles Vorher/Nachher: Eine nur prozentual skalierte Lebensleiste wird auf dem Tablet zu hoch; mit `UISizeConstraint` bleibt sie schlank ✅ ([HUD-Meter-Tutorial](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters)).

### 5. Layouts: List, Flex, Grid, Table, Page ✅
Quelle: [List and flex layouts](https://create.roblox.com/docs/ui/list-flex-layouts), [Position and size](https://create.roblox.com/docs/ui/position-and-size).

| Layout | Zweck |
|---|---|
| `UIListLayout` | Zeilen oder Spalten. `Wraps` bricht in neue Zeilen um. `HorizontalFlex`/`VerticalFlex` verteilen Restplatz (None, Fill, SpaceAround, SpaceBetween, SpaceEvenly). `ItemLineAlignment` richtet quer zur Richtung aus (z. B. `Stretch`). |
| `UIFlexItem` | Kind eines einzelnen Elements: `FlexMode` = `Fill`, `Grow`, `Shrink` oder `Custom`. Beispiel aus der Doku: Slider mit festen Endlabels und flexibler Leiste. |
| `UIGridLayout` | Gleich große Kacheln (Inventar, Sammelbuch). |
| `UITableLayout` | Tabellen (Ranglisten, Stat-Vergleich). |
| `UIPageLayout` | Seiten, zwischen denen per Skript gewechselt wird (Tutorial-Seiten, Shop-Kategorien). |

Offizieller Anwendungsfall: **Tab-Leiste mit `HorizontalFlex = Fill`** füllt die Breite gleichmäßig, egal ob 3 oder 6 Tabs ✅. Weitere Bausteine: `UIPadding`, `UICorner`, `UIStroke`, `UIGradient` (Appearance Modifiers, [Doku](https://create.roblox.com/docs/ui/appearance-modifiers)) und **9-Slice** für skalierbare Rahmen ohne verzerrte Ecken ([9-slice](https://create.roblox.com/docs/ui/9-slice)).

### 6. Styling-System: StyleSheets, Tokens, Themes ✅
Quelle: [UI styling](https://create.roblox.com/docs/ui/styling), [Style Editor](https://create.roblox.com/docs/ui/styling/editor).
- `StyleSheet` enthält `StyleRule`s. Jede Regel wirkt auf alle Instanzen, die ihrem `Selector` entsprechen (Klassenname, Instanzname, Tag mit `.`, Hierarchie). Ähnlich CSS.
- **Tokens** = Attribute eines Token-StyleSheets (wie CSS-Variablen), z. B. eine Farbe für `BackgroundColor3`, `TextColor3` und `UIStroke.Color`.
- **Themes** = austauschbare Token-Sätze (z. B. hell/dunkel); verwandte Themes müssen **dieselben Tokens** haben.
- `StyleDerive` erbt Tokens/Themes, `StyleLink` hängt ein StyleSheet an einen ScreenGui-Baum. **Nur ein StyleSheet pro Baum.**
- **Style Queries** (`@`-Präfix, `StyleQuery`) wenden Stile nur in bestimmten Zuständen an (ähnlich CSS-Media-Queries).
- Visueller **Style Editor** in Studio.

```lua
-- Kurzform des offiziellen Beispiels: ein Token, eine Regel für alle Frames
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local screenGui = script.Parent

local tokens = Instance.new("StyleSheet")
tokens.Name = "Tokens"
tokens:SetAttribute("Gold", Color3.fromHex("FFCC00"))
tokens.Parent = ReplicatedStorage

local design = Instance.new("StyleSheet")
local derive = Instance.new("StyleDerive")
derive.StyleSheet = tokens
derive.Parent = design
design.Parent = ReplicatedStorage

local link = Instance.new("StyleLink")
link.StyleSheet = design
link.Parent = screenGui

local rule = Instance.new("StyleRule")
rule.Selector = "Frame"
rule:SetProperties({ BackgroundColor3 = "$Gold", BorderSizePixel = 0 })
rule.Parent = design
```
🧠 Nutzen: Die Seltenheitsfarben, Signalfarben und Schriftgrößen einmal als Tokens anlegen; ein Event-Theme (z. B. Halloween) tauscht dann nur den Token-Satz.

### 7. Text, Schrift, Rich Text
- **Preferred Text Size** ✅ ([Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)): `GuiService.PreferredTextSize` = `Medium` (Standard), `Large`, `Larger`, `Largest`. **Bei `TextScaled = true` wird der Text nicht skaliert.** `AutomaticSize`-Elemente wachsen mit, `TextWrapped` bricht in mehr Zeilen um, `UITextSizeConstraint`-Grenzen werden respektiert, `TextService:GetTextSize()`/`GetTextBoundsAsync()` berücksichtigen die Einstellung.
- Folge 🧠: Für Fließtext, Beschreibungen, Shop-Karten **`TextSize` + `TextWrapped` + `AutomaticSize`** statt `TextScaled`. `TextScaled` nur für kurze Zahlen in festen Boxen (Währungsanzeige), dort mit `UITextSizeConstraint`.
- Entwickler-Kritik: Ein DevForum-Thread (31. Aug. 2025) forderte die Rücknahme, weil eigene UIs ab „Large“ brechen 🟡 ([DevForum](https://devforum.roblox.com/t/preferred-text-scaling-needs-to-be-reverted-abrupt-release-with-no-concerns-addressed-are-disruptive/3911199)). Ankündigung als Studio-Beta am 25. Aug. 2025 🟡 ([DevForum](https://devforum.roblox.com/t/introducing-text-scaling-setting-studio-beta/3136967)). → Layouts mit „Largest“ testen.
- **Rich Text** ✅ ([Rich text](https://create.roblox.com/docs/ui/rich-text)): auf `TextLabel`, `TextButton`, `TextBox` mit `RichText = true`; Tags wie `<b>`, `<i>`, `<u>`, `<s>`, `<font color/size/face/family/weight>`, `<stroke>`; verschachtelt in umgekehrter Reihenfolge schließen.
- Maximal 2 Schriftarten, fett und klar für Zahlen 🧠. Doku: „Always prioritize legibility when choosing a font“; dekorative oder dünne Schriften vermeiden ✅ ([Adaptive design](https://create.roblox.com/docs/production/publishing/adaptive-design)).

### 8. Farbe und Kontrast
- **Kontrast**: helle Schrift auf hellem oder dunkle auf dunklem Grund vermeiden ✅ ([Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)).
- **Nicht nur Farbe**: „Über 5 % der Menschen weltweit haben eine Form von Farbenblindheit“; zusätzlich **Symbole** nutzen ✅ (ebd.).
- **Preferred Transparency**: `GuiService.PreferredTransparency` (1 = Standard, 0 = voll deckend). Empfohlen: `BackgroundTransparency × PreferredTransparency` ✅ (ebd.).
- Palette 🧠: 1 Hauptfarbe, 1–2 Akzente, Neutrale. Grün = bestätigen/positiv, Rot = Gefahr/Fehler/unbezahlbar, Gold = Währung/Premium, Blau = Info, Grau = deaktiviert (Grau als Konvention ✅ laut [UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)).
- **Seltenheitsfarben** (Common grau, Uncommon grün, Rare blau, Epic lila, Legendary orange/gold) sind verbreitete Sammelspiel-Konvention 🟡; immer mit Rahmenform/Symbol kombinieren.

### 9. Animation und Juice
- Technik ✅ ([UI animation](https://create.roblox.com/docs/ui/animation)): `TweenService:Create(objekt, TweenInfo, ziele):Play()`, Ketten über `.Completed`; typische Anwendungen: Button bei Auswahl vergrößern, Menüs vom Rand einfliegen lassen.
- **Reduced Motion** ✅ ([Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)): `GuiService.ReducedMotionEnabled`; offizielle Muster: Tween-Zeit 0 (sofort springen) oder Fade über `CanvasGroup.GroupTransparency` statt Bewegung. Details in `eingabe-und-barrierefreiheit.md`.
- Richtwerte 🧠: Öffnen/Schließen 0,15–0,3 s (das offizielle Reduced-Motion-Beispiel nutzt 0,75 s `Cubic Out` ✅), Zahlen hochzählen statt springen, Belohnung mit Puls/Funken, Animation darf Eingaben nie blockieren.

### 10. Feedback-Zeit und Performance
- 🧠 Jede Eingabe braucht eine sichtbare Reaktion; Ziel unter ~0,1 s (allgemeine UX-Faustregel, kein Roblox-Wert).
- Bei 60 FPS hat ein Frame **16,67 ms** Budget ✅ ([Design for performance](https://create.roblox.com/docs/performance-optimization/design)). Viele gleichzeitige Tweens und UI-Updates pro Frame kosten Budget.
- UI-Bilder: meist **höchstens 512×512**, kleine Bilder **unter 256×256**; viele kleine UI-Bilder als **Sprite Sheet** mit `ImageLabel.ImageRectOffset`/`ImageRectSize` ✅ ([Improve performance](https://create.roblox.com/docs/performance-optimization/improve)).

### 11. Layout-Orientierung (Startpunkt, testen)
| Bereich | Inhalt | Beleg |
|---|---|---|
| Unten links / unten rechts | Reservierte Zonen für Thumbstick und Sprung-Button, freihalten | ✅ [Position and size](https://create.roblox.com/docs/ui/position-and-size) |
| Um den Sprung-Button | Häufige Aktionen (relativ zum Sprung-Button positionieren) | ✅ ebd. |
| Ecken oben | Dauerwerte (Währung, Level, Gesundheit) | 🟠 Community / 🧠 |
| Seitenränder | Menü-Buttons (Shop, Inventar, Quests) | 🟠 / 🧠 |
| Mitte | Frei halten, nur kurz für Popups | 🟠 [creation.dev](https://www.creation.dev/blog/roblox-ui-design-best-practices) |
| Oben Mitte | Ziel, Timer (sparsam) | ✅ Laser-Tag-Wireframe zeigt Ziel-Info oben ([Wireframe your layouts](https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/wireframe-your-layouts)) |

### 12. Touch-Ziele
- **Eine offizielle Roblox-Mindestgröße gibt es nicht** ✅ (die Seite [UI/UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design) nennt keinen Pixelwert).
- Plattformstandards: Apple **44 pt**, Android **48 dp** 🟡 ([W3C Mobile A11y](https://www.w3.org/WAI/GL/mobile-a11y-tf/wiki/M2)). Community: ≥ 44×44 px, per `UISizeConstraint.MinSize` erzwingen oder unsichtbare größere Trefferfläche 🟠 ([creation.dev](https://www.creation.dev/blog/roblox-ui-design-best-practices)).
- Mehr dazu in `mobile-first.md`.

### 13. Icon-Design (In-Game-Icons)
- Klare Silhouette, erkennbar in klein; einheitliche Strichstärke, Perspektive, Schatten 🧠.
- Stat-Icons einer Familie teilen Farbe und Form ✅ (Beispiel *Winds of Fortune* in [UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)).
- Neue Funktionen: Icon **plus** kurzes Wort. Bei Lootbox-Infos verlangt Roblox sogar ein beschreibendes Wort („Info“/„Details“); ein alleinstehendes (i) reicht nicht ✅ ([Paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items)).
- Spiel-Icon und Thumbnails: siehe `thumbnails-und-icons.md`.

### 14. Workflow für ein neues Interface 🧠 (gestützt auf offizielle Tutorials)
1. **User Flow** zeichnen (alle Screens und Zustände) ✅ ([Wireframe your layouts](https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/wireframe-your-layouts)).
2. **Belegten Platz kennen**: Roblox-Standard-UI (Chat, Self View, Emotes, Backpack, Spielerliste, Lebensleiste, Captures) und Touch-Zonen ✅ (ebd.).
3. **Wireframe** mit grauen Boxen, getrennt für Mobile und PC ✅ (ebd.).
4. **Visuelle Hierarchie** festlegen (Zentrum = Aktion, Ränder = Peripherie) ✅ (ebd.).
5. Style Guide als Tokens/StyleSheet anlegen.
6. Im **Device Emulator** auf Phone, Tablet, Konsole, HD-Monitor prüfen ✅ ([DevForum Staff](https://devforum.roblox.com/t/designing-ui-tips-and-best-practices/3074034)); Controller Emulator für Gamepad ✅ ([Input Action System](https://create.roblox.com/docs/input/input-action-system)).
7. Textgröße „Largest“, Reduced Motion, Preferred Transparency testen.
8. Mit Experiments A/B testen ✅ ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)).

## Beispiele aus echten Spielen
Siehe Abschnitt 1 (alle von Roblox selbst genannt). Beobachtete Stilrichtung 2025: „Stud UI“ mit Noppen-Optik und Schlagschatten hinter Text bei *Grow a Garden* und *Plants vs Brainrots* 🟠 ([DevForum](https://devforum.roblox.com/t/how-do-you-make-stud-ui/4020877), [DevForum](https://devforum.roblox.com/t/grow-a-garden-dialog-ui/3736124)). Kommerzielle UI-Packs listen als Standard-Set: Shop, Bestätigung, Codes, Limited Shop, Pet-/Kosmetik-Shop, HUD, Inventar, Hotbar, Benachrichtigung, Quests, Einstellungen 🟠 ([BuiltByBit](https://builtbybit.com/resources/grow-a-ui-pack.79298/)). Nur als Inspiration, nicht kopieren.

## Do / Don't
| Do | Don't |
|---|---|
| Phone-first bauen, auf Tablet/Konsole anpassen | Nur am PC-Monitor testen |
| `CoreUISafeInsets` für alles Interaktive | Buttons in `None` oder unter die Top-Bar |
| Scale + `UISizeConstraint`/`UIAspectRatioConstraint` | Reine Pixelgrößen oder reine Scale-Größen ohne Grenzen |
| Flex-Layouts für Tab-Leisten und Button-Reihen | Breiten von Hand rechnen |
| Tokens/StyleSheet für Farben und Schriften | Farben in jedem Frame einzeln setzen |
| `TextWrapped` + `AutomaticSize` für Fließtext | `TextScaled` für alles (ignoriert Textgröße der Spieler) |
| `MinTextSize` ≥ 9 | Winzige Schrift auf kleinen Screens |
| Farbe + Symbol als Information | Nur Farbe (über 5 % farbenblind) |
| Kontextbuttons statt Dauerbuttons | Alle Aktionen gleichzeitig anzeigen |
| Konventionen (X, Grau, Schloss) nutzen | Eigene Symbolsprache ohne Grund |
| Reduced Motion respektieren | Pflicht-Animationen, die Eingaben blockieren |

## Checkliste
- [ ] User Flow und Wireframes (Mobile + PC) existieren
- [ ] Interaktive UI in `CoreUISafeInsets`, Hintergründe ggf. `None`
- [ ] `ResetOnSpawn` bewusst gesetzt, `DisplayOrder` für Modals höher
- [ ] Standard-UI bewusst behalten oder per `SetCoreGuiEnabled` ersetzt
- [ ] Scale + Constraints, auf Tablet geprüft (nichts zu groß)
- [ ] Text: `MinTextSize` ≥ 9, mit „Largest“ getestet, kein `TextScaled` bei Fließtext
- [ ] Farbe nie alleiniger Informationsträger, Kontrast geprüft
- [ ] Style Guide / Tokens dokumentiert
- [ ] Jede Interaktion hat Feedback (visuell + Ton)
- [ ] Reduced Motion und Preferred Transparency unterstützt
- [ ] UI-Bilder ≤ 512 px, kleine ≤ 256 px, wiederverwendet

## Offene Fragen / Recherche-Bedarf
- Offizielle Geräteaufteilung 2025/2026 fehlt (letzter Stand: 80/17/3 für 2024).
- Volltext des Staff-Posts „Designing UI – Tips and Best Practices“ (eventuelle Pixelwerte) nicht gelesen.
- Datum des Top-Bar-Redesigns (Einführung `TopbarInset`) nicht verifiziert.

## Verknüpfungen
`hud-shop-menues.md`, `mobile-first.md`, `eingabe-und-barrierefreiheit.md`, `thumbnails-und-icons.md`, `checklisten/ui-review.md`

## Quellen
- [Creator Docs: UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design) – Stand 2026-10-24, ✅
- [Creator Docs: On-screen UI containers](https://create.roblox.com/docs/ui/on-screen-containers) – ✅
- [Creator Docs: ScreenGui](https://create.roblox.com/docs/reference/engine/classes/ScreenGui), [ScreenInsets](https://create.roblox.com/docs/reference/engine/enums/ScreenInsets), [GuiService](https://create.roblox.com/docs/reference/engine/classes/GuiService) – ✅
- [Creator Docs: Position and size](https://create.roblox.com/docs/ui/position-and-size), [Size modifiers](https://create.roblox.com/docs/ui/size-modifiers) – ✅
- [Creator Docs: List and flex layouts](https://create.roblox.com/docs/ui/list-flex-layouts) – ✅
- [Creator Docs: UI styling](https://create.roblox.com/docs/ui/styling) – ✅
- [Creator Docs: Rich text](https://create.roblox.com/docs/ui/rich-text), [UI animation](https://create.roblox.com/docs/ui/animation), [9-slice](https://create.roblox.com/docs/ui/9-slice) – ✅
- [Creator Docs: Accessibility guidelines](https://create.roblox.com/docs/production/publishing/accessibility) – ✅
- [Creator Docs: Adaptive design guidelines](https://create.roblox.com/docs/production/publishing/adaptive-design) – ✅
- [Creator Docs: Wireframe your layouts](https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/wireframe-your-layouts), [HUD-Meter-Tutorial](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) – ✅
- [Creator Docs: Design for performance](https://create.roblox.com/docs/performance-optimization/design), [Improve performance](https://create.roblox.com/docs/performance-optimization/improve) – ✅
- [DevForum (Roblox Staff): Designing UI – Tips and Best Practices](https://devforum.roblox.com/t/designing-ui-tips-and-best-practices/3074034) – ca. Mitte 2024, ✅
- [PocketGamer.biz: 80 % of Roblox users are on mobile](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue) – 2025, 🟡 (zitiert Roblox-Geschäftsbericht 2024)
- [W3C Mobile Accessibility: Touch target size](https://www.w3.org/WAI/GL/mobile-a11y-tf/wiki/M2) – 🟡
- [creation.dev: Roblox UI Design Best Practices](https://www.creation.dev/blog/roblox-ui-design-best-practices) – 🟠
