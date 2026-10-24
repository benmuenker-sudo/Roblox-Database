# HUD, Shop, Menüs und Popups

> Stand: 2026-10-24 · Nächste Prüfung: 2027-01-24 · Gesamt-Vertrauen: ✅ für API-Namen, Kauf- und Lootbox-Regeln, Ladezeit-Empfehlungen (Creator Docs), 🟡 für Konventionen bei Sammel-/Simulator-Spielen, 🟠 für Drittquellen, 🧠 für Designwissen

## Kurzfassung
Das **HUD** zeigt dauerhaft nur das, was der Spieler *gerade* braucht, und tauscht Buttons je nach Kontext aus. **Menüs** halten alles Weitere, mit Tabs, maximal zwei Ebenen und großem Schließen-Button. Der **Shop** lenkt den Blick über Größe, Abstand und Labels auf das gewünschte Angebot (offizielles Beispiel: „Best Value“-Paket in *Dragon Adventures*), zeigt Preise **dynamisch** über `MarketplaceService:GetProductInfoAsync()` statt hart codiert und erfüllt bei Zufallsprodukten die **Quoten-Offenlegungspflicht** ✅ ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design), [Regional pricing](https://create.roblox.com/docs/production/monetization/regional-pricing), [Paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items)). Popups unterbrechen nie das Spielen ohne Grund.

## Warum das wichtig ist
- Das HUD ist die meistgesehene Fläche des Spiels; auf Handys mit 80 % Nutzeranteil (2024) 🟡 ([PocketGamer.biz](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue)) ist jeder Pixel knapp.
- Hart codierte Preise zeigen bei Managed/Regional Pricing **falsche Beträge an**, obwohl der richtige regionale Preis abgebucht wird ✅ ([Regional pricing](https://create.roblox.com/docs/production/monetization/regional-pricing)). Das kostet Vertrauen.
- Lootbox-UI ohne korrekte Quotenanzeige verstößt gegen Roblox-Richtlinien ✅ ([Paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items)).

## Referenzbilder
Selbst erstellte, beschriftete Referenzbilder (frei nutzbar, Übersicht: `assets/bilder/README.md`).

![HUD-Beispiel Simulator](../assets/bilder/ui-hud-beispiel-simulator.png)
![Shop-Layout](../assets/bilder/ui-shop-layout.png)
![Inventar mit Seltenheitsrahmen](../assets/bilder/ui-inventar-seltenheit.png)
![Sammelbuch](../assets/bilder/ui-sammelbuch.png)
![Toast, Banner, Modal](../assets/bilder/ui-popup-toast-hierarchie.png)
![Tutorial-Pfeil](../assets/bilder/ui-tutorial-pfeil.png)

Offizielle Bilder aus der Roblox Creator Documentation (Übersicht: `assets/bilder/offiziell/README.md`):

![HUD-Priorisierung in The Survival Game](../assets/bilder/offiziell/ui-design/uiux-priorisierung-hud-survival.png)
*Lebens- und Hungerleiste oben rechts, Hotbar unten, Menü-Shortcuts an den Rändern, Mitte frei. Quelle: Roblox Creator Docs, CC BY 4.0*

![Shop mit hervorgehobenem Best-Value-Paket](../assets/bilder/offiziell/ui-design/uiux-aufmerksamkeit-shop-bundles.png)
*Das wertvollste Münzpaket ist größer, abgesetzt und mit „Best Value“ markiert (Dragon Adventures). Quelle: Roblox Creator Docs, CC BY 4.0*

![Visuelle Hierarchie im Wireframe](../assets/bilder/offiziell/ui-design/wireframe-visuelle-hierarchie.png)
*Ziel-Info oben, Waffen-Info in der Mitte, Spielerstatus an den Seiten. Quelle: Roblox Creator Docs, CC BY 4.0*

![Wireframe Block-in Mobile](../assets/bilder/offiziell/ui-design/wireframe-blockin-mobile.png)
![Wireframe Block-in PC](../assets/bilder/offiziell/ui-design/wireframe-blockin-pc.png)
*Dasselbe HUD als graue Boxen für Mobile (mit Touch-Steuerung) und PC. Quelle: Roblox Creator Docs, CC BY 4.0*

![HUD-Lebensleiste Bausteine](../assets/bilder/offiziell/ui-design/hud-lebensleiste-bauteile.png)
*HUD-Meter aus ImageLabel (Herz) und Frame (Balken). Quelle: Roblox Creator Docs, CC BY 4.0*

![Standard-CoreGui-Elemente](../assets/bilder/offiziell/ui-design/standard-coregui-elemente.jpg)
*Platz, den Roblox-Standard-UI bereits belegt. Quelle: Roblox Creator Docs, CC BY 4.0*

![Shop mit Top-Picks-Tab](../assets/bilder/offiziell/monetarisierung-liveops/shop-top-picks-tab.png)
*Kuratierter „Top Picks“-Tab als erste Shop-Seite. Quelle: Roblox Creator Docs, CC BY 4.0*

![Shop mit personalisierter Reihenfolge](../assets/bilder/offiziell/monetarisierung-liveops/shop-items-nach-spieler-gerankt.png)
*Pro Spieler gerankte Items (RankProductsAsync). Quelle: Roblox Creator Docs, CC BY 4.0*

![Kontextkauf vor dem Run](../assets/bilder/offiziell/monetarisierung-liveops/kontextkauf-vor-dem-spiel.jpg)
*Pre-Run-Shop in Doors: Verbrauchsgüter direkt vor der Runde. Quelle: Roblox Creator Docs, CC BY 4.0*

![Season Pass im Store-Tab](../assets/bilder/offiziell/monetarisierung-liveops/season-pass-integriert-store-tab.png)
*Season Pass gut auffindbar im eigenen Tab. Quelle: Roblox Creator Docs, CC BY 4.0*

## HUD (Heads-up-Display)

### Was hineingehört
| Element | Regel | Beleg |
|---|---|---|
| Währung(en) | 1–2 sichtbar, Icon + Zahl, Kurzformat | 🧠 |
| Fortschritt | Level/XP, Zonenfortschritt; frühe Level schnell erreichbar | ✅ Onboarding empfiehlt niedrige frühe XP-Schwellen ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding)) |
| Gesundheit / Ressourcen | Nur wenn spielrelevant; Survival: immer sichtbar | ✅ *The Survival Game* ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)) |
| Aktuelles Ziel | Kurzer Text/Icon, gut sichtbar | ✅ Ziele „in highly visible places“ ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding)) |
| Kontextaktionen | Nur zeigen, wenn möglich (Tür, Truhe, Ball) | ✅ Proximity Prompt statt Dauer-Button ([Position and size](https://create.roblox.com/docs/ui/position-and-size)) |
| Boosts/Effekte | Kleine Icons mit Timer | 🧠 |

### Was nicht hineingehört
- Alles Seltene → Menü. Drittquellen: Desktop-HUDs (Leben, Mana, Minimap, Inventar, Chat, Quest-Tracker) verdecken auf dem Handy die halbe Fläche; **2–3 Kernelemente** sichtbar lassen, Top-Mobile-Spiele nutzen **1–3 Aktionsbuttons plus virtuellen Stick** 🟠 ([creation.dev](https://www.creation.dev/blog/roblox-ui-design-best-practices)).
- Mehr als ca. 6–8 Dauerelemente überfordern 🧠 (Faustregel).
- Roblox-Standard-UI nicht überdecken (Top-Bar, Chat, Spielerliste, Touch-Steuerung) ✅ ([DevForum Staff](https://devforum.roblox.com/t/designing-ui-tips-and-best-practices/3074034)).

### Kontextabhängiges HUD ✅
Die Doku empfiehlt, Buttons je nach Kontext zu tauschen (Rolle, Ort, gehaltenes Item). Beispiel *Super Striker League*: ohne Ball Sprint/Tackle, mit Ball Deke/Pass ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)). Für Interaktionen in der Welt: `ProximityPrompt` mit `KeyboardKeyCode`, `GamepadKeyCode`, `MaxActivationDistance`, `RequiresLineOfSight` (Standard `true`), `HoldDuration` ✅ ([Proximity prompts](https://create.roblox.com/docs/ui/proximity-prompts)). Vorteil 🧠: funktioniert automatisch auf Touch, Tastatur und Gamepad.

### HUD-Regeln 🧠
- Zahlen kurz formatieren (1,2K, 3,4M, 1B), animiert hochzählen.
- Menü-Buttons als Icon-Spalte am Rand, mit Benachrichtigungspunkt bei Neuem.
- Jedes HUD-Meter aus wenigen Bausteinen: Hintergrund-Frame, Füll-Frame, Icon ✅ (Muster aus dem [HUD-Meter-Tutorial](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters)).
- Mit `UISizeConstraint` begrenzen, sonst wird das Meter auf Tablets zu groß ✅ (ebd.).
- Niedrige Gesundheit zusätzlich mit `ColorCorrectionEffect` (Bildschirm rot tönen) signalisieren ✅ ([Post-processing](https://create.roblox.com/docs/environment/post-processing-effects)).

## Menüs

### Struktur
- **Hauptbereiche:** 5–7 (Inventar, Shop, Quests, Sammlung, Einstellungen, Freunde) 🧠.
- **Tiefe:** höchstens 2 Ebenen, Zurück immer sichtbar 🧠. Konsole: **Progressive Disclosure** – seltene Funktionen auf zweite Screens; „rein und raus“ ist dort schneller als alles auf einem Screen ✅ ([Console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines)).
- **Tabs** mit `UIListLayout.HorizontalFlex = Fill` füllen die Leiste gleichmäßig, egal wie viele Tabs ✅ ([List and flex layouts](https://create.roblox.com/docs/ui/list-flex-layouts)).
- **Schließen:** Konvention „X schließt den Dialog“ ✅; konsistent quadratisch, rot, weißes X, oben rechts (Konsistenz-Beispiel der Doku) ✅ ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)). Zusätzlich Zurück-Taste (Gamepad B) und ggf. Tippen außerhalb 🧠.
- **Ein Menü zur Zeit**, Modals über höhere `ScreenGui.DisplayOrder` ✅ ([On-screen containers](https://create.roblox.com/docs/ui/on-screen-containers)).
- **Hintergrund beruhigen:** `BlurEffect` unscharf stellen, solange ein Menü offen ist ✅ ([Post-processing](https://create.roblox.com/docs/environment/post-processing-effects)); im Shop kann `DepthOfFieldEffect` den Fokus auf ein Item legen ✅ (ebd.).
- **Eingabe trennen:** Beim Öffnen einen Menü-`InputContext` aktivieren (Sink), beim Schließen zurück zum Spiel-Kontext ✅ ([Input Action System](https://create.roblox.com/docs/input/input-action-system)). Details: `eingabe-und-barrierefreiheit.md`.
- Konsole: Navigationssounds bei Auswahl/Wechsel einsetzen ✅ ([Console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines)); Haptik `HapticEffect` vom Typ `UIClick` möglich ✅ ([Gamepad input](https://create.roblox.com/docs/input/gamepad)).

### Inventar 🧠 / 🟡
- `UIGridLayout`-Raster mit Seltenheitsrahmen (Farbe **und** Form/Symbol).
- Sortieren und Filtern (Seltenheit, Neu, Typ), Vergleich neu vs. ausgerüstet.
- Mehrfachauswahl zum Verkaufen/Löschen mit **Sicherheitsabfrage bei seltenen Items**.
- Platzanzeige (z. B. 47/60), `ScrollingFrame` mit `AutomaticCanvasSize` ✅ ([Size modifiers](https://create.roblox.com/docs/ui/size-modifiers)).

### Sammelbuch / Katalog 🧠
- Alles sichtbar: gesammelt hell, fehlend als Silhouette.
- Fortschritt (z. B. 34/120), Teilbelohnungen bei Meilensteinen. Offiziell: Sammlungen sind eine Form von mittel- und langfristigen Zielen ✅ ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding)).

### Quests / Ziele
- 1–3 aktive Ziele mit Fortschrittsbalken 🧠; der füllende Balken ist ein offizielles Feedback-Beispiel ✅ ([UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)).
- „Gehe zu“-Pfeil oder leuchtende Spur in der Welt ✅ (Visual Elements in [Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques)).

## Shop

### Aufbau
| Baustein | Empfehlung | Beleg |
|---|---|---|
| Startseite | Kuratierter „Top Picks“-Tab vor Passes und Coins | ✅ Bild aus [Developer products](https://create.roblox.com/docs/production/monetization/developer-products) |
| Personalisierung | Reihenfolge pro Spieler mit `MarketplaceService:RankProductsAsync()` | ✅ API existiert in der Referenz ([MarketplaceService](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService)) |
| Highlight | Wertvollstes Paket größer, mehr Padding, Label | ✅ *Dragon Adventures* |
| Gruppierung | Größe + Nähe trennen Kategorien | ✅ *Tower Defense Simulator* |
| Karten | Bild, Name, Nutzen in einem Satz, Preis, Button | 🧠 |
| Unbezahlbar | Preis rot anzeigen | ✅ Konsistenz-Beispiel der Doku |
| Gesperrt | Schloss-Icon | ✅ Konvention |
| Season Pass | Eigener, gut auffindbarer Tab; Free- und Premium-Spur nebeneinander | ✅ ([Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations), [Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design)) |
| Kontextkäufe | Verbrauchsgüter dann anbieten, wenn ihr Nutzen am klarsten ist (vor dem Run, in der Lobby über 3D-Automat) | ✅ ([Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases)) |
| Roblox-Systemshop | Roblox-Menü hat einen Standard-Eintrag „Shop“; bei eigener Shop-UI bewusst entscheiden | ✅ ([Shop](https://create.roblox.com/docs/production/monetization/shop)) |

### Preise dynamisch anzeigen ✅
- Managed Pricing und Price Optimization können **hart codierte Preise nicht ändern**; das Dynamic-Price-Check-Werkzeug erkennt sie mit Fake-Preisen und bis zu **5 Testkonten** ([Price optimization](https://create.roblox.com/docs/production/monetization/price-optimization)).
- Regionalen Preis eines Produkts oder Passes mit `MarketplaceService:GetProductInfoAsync()` holen ([Regional pricing](https://create.roblox.com/docs/production/monetization/regional-pricing)). `GetProductInfo()` ist durch `GetProductInfoAsync()` ersetzt ([MarketplaceService](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService)).

```lua
-- LocalScript: Preis dynamisch in eine Shop-Karte schreiben (APIs laut Creator Docs)
local MarketplaceService = game:GetService("MarketplaceService")
local PRODUCT_ID = 0 -- eigene Developer-Product-ID eintragen

local ok, info = pcall(function()
	return MarketplaceService:GetProductInfoAsync(PRODUCT_ID, Enum.InfoType.Product)
end)
if ok and info then
	script.Parent.PriceLabel.Text = tostring(info.PriceInRobux)
else
	script.Parent.PriceLabel.Text = "–" -- Fallback, nie einen alten Preis zeigen
end
```

### Kauf-Ablauf
1. Auswahl → 2. eigene Bestätigung (Name, Preis, Wirkung) 🧠 → 3. Roblox-Kaufdialog (`PromptProductPurchase`, `PromptGamePassPurchase`) ✅ → 4. Erfolgs-Feedback (Animation + Ton, z. B. `kauf-erfolg` aus `assets/audio/`) → 5. sofort nutzbar.
- Die Vergabe von Developer Products läuft serverseitig über `MarketplaceService.ProcessReceipt`; die UI reagiert erst, wenn der Server die Vergabe bestätigt hat ✅ (API laut [MarketplaceService](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService); Technik-Details in `08-technik-luau/technik-grundlagen.md`).
- `PromptProductPurchaseFinished`/`PromptGamePassPurchaseFinished` für UI-Zustand (Abbruch, Erfolg) nutzen ✅ (API-Referenz ebd.).
- Fehlerfälle abdecken: abgebrochen, zu wenig Robux, Fehler → verständliche Meldung (`ui-fehler`-Sound), kein Absturz 🧠.
- Nie einen Kauf auslösen, ohne dass der Preis klar sichtbar war 🧠.

### Zufallsprodukte (Lootboxen, Eier, Spins) ✅
Quelle: [Paid random items policy](https://create.roblox.com/docs/production/monetization/paid-random-items).
- **Alle möglichen Ergebnisse** und die **tatsächlichen numerischen Quoten** als Prozent anzeigen, Summe genau **100 %**.
- Info-Popup braucht ein sichtbares **„Info“- oder „Details“-Icon mit Wort**; ein alleinstehendes (i) reicht nicht.
- Luck-Boosts: Wirkung numerisch erklären, Quoten **dynamisch aktualisieren**, solange aktiv.
- Indirekte Käufe (Schlüssel, Reroll-Token, Spin-Tickets): Quoten **vor** dem Ausgeben der In-Game-Währung zeigen.
- Kann ein Ergebnis nur einmal erhalten werden, die übrigen Quoten aktualisieren.
- Kostenlose Zufallsbelohnungen ohne Robux/Währung brauchen keine Offenlegung.
- Mehr: `03-mechaniken-retention/gacha-und-luck.md`, `07-monetarisierung/monetarisierung.md`.

### Shop-Ethik (🧠, relevant bei jungem Publikum)
- Keine Fake-Timer, keine Schuld-Texte, keine versteckten Käufe.
- Kein Pay-to-win-Zwang für Grundfortschritt.
- Jedes verkaufte Item braucht einen klaren Zweck im Gameplay ✅ (Beispiel Taschenlampe in *Doors*, [Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations)).

## Popups und Benachrichtigungen
| Typ | Einsatz | Dauer / Regel |
|---|---|---|
| Toast | Belohnung, Fortschritt | 2–4 s, Warteschlange statt Stapel 🧠 |
| Banner | Event startet, Server-Meldung (Mythic-Drop) | 3–5 s, oben 🧠 |
| Modal | Kauf, Löschen, Fehler | Nur für Wichtiges, höchste `DisplayOrder` ✅/🧠 |
| Hinweis in der Welt | Tutorial-Schritt, Ziel | Bleibt sichtbar, bis Schritt erledigt ✅ ([Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques)) |

- Nicht beim Spielen mit Kaufwerbung unterbrechen 🧠.
- Ton nie als einziges Signal (Hörgeschädigte, stumm geschaltete Geräte) ✅ ([Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)).
- Streaming-Pause: Bei `StreamingIntegrityMode = PauseOutsideLoadedArea` kann man das Standard-Pause-Modal mit `GuiService:SetGameplayPausedNotificationEnabled(false)` ersetzen und `Player.GameplayPaused` beobachten ✅ ([Instance streaming](https://create.roblox.com/docs/workspace/streaming)).

## Ladebildschirm ✅
Quelle: [Improve performance – Load times](https://create.roblox.com/docs/performance-optimization/improve), [Loading screens](https://create.roblox.com/docs/players/loading-screens).
- `ReplicatedFirst` nur für den Ladebildschirm (einfache UI, keine großen Texturen/3D-Modelle), dann `ReplicatedFirst:RemoveDefaultLoadingScreen()` nutzen.
- `ContentProvider:PreloadAsync()` **nur** für: Bilder des Ladebildschirms, wichtige Menü-Bilder (Button-Hintergründe, Icons), wichtige Assets am Spawn. **Nicht** den ganzen Workspace vorladen; `ContentProvider.RequestQueueSize` als Warte-Bedingung ist unzuverlässig.
- Bei vielen Assets einen **„Skip Loading“-Button** anbieten.
- `ReplicatedStorage` schlank halten: Alles darin lädt jeder Client vor dem Spielstart.
- 🧠 Fortschrittsanzeige, ein Tipp, Markenidentität, Animation gegen „hängt“-Gefühl.

## Tutorial-UI
- **Pfeile, Highlights, abgedunkelter Rest des Bildschirms** statt Textmauern ✅ (Beispiel *Hello Kitty Cafe*, [Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques)).
- **Kontextuelle Tutorials** („just in time“), ausgelöst durch normales Spielen ✅ (ebd.).
- **Timed Hints** mit per Experiment getesteter Verzögerung (Doku-Beispiel: 5 s vs. 10 s) ✅ (ebd.).
- Eine Anweisung zur Zeit, Überspringen für Wiederkehrer 🧠.

## Barrierefreiheit und Sprache (Kurzfassung)
- Kontrast, Icon zusätzlich zu Farbe, Textgröße der Spieler respektieren ✅ ([Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)).
- Getrennte Lautstärkeregler (Musik, SFX, Sprache) ✅ (ebd.).
- Lokalisierung: Platz für längere Texte, kein Text in Bildern (Automatic Text Capture erfasst Bilder mit eingebettetem Text nicht) ✅ ([Automatic translation](https://create.roblox.com/docs/production/localization/automatic-translations)).
- Gamepad-Navigation testen. Ausführlich: `eingabe-und-barrierefreiheit.md`.

## Typische Fehler
| Fehler | Folge | Lösung |
|---|---|---|
| Zu viele HUD-Elemente | Überladen, Mobile unspielbar | Kontextbuttons, Rest ins Menü |
| Kauf-Button ohne Bestätigung | Versehentliche Käufe, Beschwerden | Eigene Bestätigung mit Preis |
| Hart codierte Robux-Preise | Falscher Preis bei Regional Pricing | `GetProductInfoAsync()` |
| Lootbox ohne Quoten oder mit (i) ohne Wort | Richtlinienverstoß | Quoten in %, Summe 100 %, „Info“-Button |
| Menü verdeckt Spielwelt dauerhaft | Frust | Halbtransparent, Blur, nur kurz |
| Winzige X-Buttons | Spieler kommen nicht raus | Große Fläche, B-Taste |
| Zahlen laufen aus Feld | Unlesbar | Kurzformat, `UITextSizeConstraint` |
| UI-Zustand weg nach Tod | Shop schließt, Auswahl weg | `ResetOnSpawn = false` |
| Ganzer Workspace in `PreloadAsync` | Lange Ladezeit | Nur Spawn/Menü-Assets vorladen |

## Checkliste
- [ ] HUD zeigt pro Zustand nur Relevantes (Kontextbuttons / Proximity Prompts)
- [ ] Roblox-Standard-UI und Touch-Zonen nicht überdeckt
- [ ] Menüs: max. 2 Ebenen, X oben rechts, B-Taste schließt, ein Menü zur Zeit
- [ ] Shop-Preise dynamisch, Dynamic Price Check durchgeführt
- [ ] Kauf-Flow mit Bestätigung, Erfolgs- und Fehlerfeedback
- [ ] Zufallsprodukte: Quoten vollständig, 100 %, „Info“-Button mit Wort, dynamisch bei Luck
- [ ] Toasts in Warteschlange, Modals nur für Wichtiges
- [ ] Ladebildschirm schlank, nur nötige Assets vorgeladen, Skip-Button bei langer Ladezeit
- [ ] Tutorial zeigt statt erklärt, überspringbar

## Offene Fragen / Recherche-Bedarf
- Keine offiziellen Benchmarks, wie viele HUD-Elemente optimal sind.
- Keine screenshotbasierte Analyse der Top-100-HUDs gefunden.

## Verknüpfungen
`ui-grundlagen.md`, `mobile-first.md`, `eingabe-und-barrierefreiheit.md`, `07-monetarisierung/monetarisierung.md`, `03-mechaniken-retention/gacha-und-luck.md`, `checklisten/ui-review.md`

## Quellen
- [Creator Docs: UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design) – Stand 2026-10-24, ✅
- [Creator Docs: Onboarding](https://create.roblox.com/docs/production/game-design/onboarding), [Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques) – ✅
- [Creator Docs: Paid random items policy guidelines](https://create.roblox.com/docs/production/monetization/paid-random-items) – ✅
- [Creator Docs: Regional pricing](https://create.roblox.com/docs/production/monetization/regional-pricing), [Price optimization](https://create.roblox.com/docs/production/monetization/price-optimization) – ✅
- [Creator Docs: MarketplaceService](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService), [Developer products](https://create.roblox.com/docs/production/monetization/developer-products), [Shop](https://create.roblox.com/docs/production/monetization/shop) – ✅
- [Creator Docs: Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases), [Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations), [Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design) – ✅
- [Creator Docs: Proximity prompts](https://create.roblox.com/docs/ui/proximity-prompts), [On-screen containers](https://create.roblox.com/docs/ui/on-screen-containers), [List and flex layouts](https://create.roblox.com/docs/ui/list-flex-layouts) – ✅
- [Creator Docs: Post-processing effects](https://create.roblox.com/docs/environment/post-processing-effects) – ✅
- [Creator Docs: Improve performance](https://create.roblox.com/docs/performance-optimization/improve), [Loading screens](https://create.roblox.com/docs/players/loading-screens), [Instance streaming](https://create.roblox.com/docs/workspace/streaming) – ✅
- [Creator Docs: Console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines), [Gamepad input](https://create.roblox.com/docs/input/gamepad) – ✅
- [Creator Docs: Wireframe your layouts](https://create.roblox.com/docs/tutorials/curriculums/user-interface-design/wireframe-your-layouts), [HUD-Meter-Tutorial](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) – ✅
- [DevForum (Roblox Staff): Designing UI – Tips and Best Practices](https://devforum.roblox.com/t/designing-ui-tips-and-best-practices/3074034) – ✅
- [PocketGamer.biz](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue) – 🟡
- [creation.dev: Roblox UI Design Best Practices](https://www.creation.dev/blog/roblox-ui-design-best-practices) – 🟠
