# Mobile-First: Safe Area, Touch, Performance

> Stand: 2026-10-24 · Gesamt-Vertrauen: ✅ für ScreenInsets/Properties, 🧠 für Praxis

## Kurzfassung
Der Großteil der Roblox-Spieler nutzt Handy oder Tablet (🧠; aktuelle Quote bei Update aus Roblox-Quellen prüfen). Teste **zuerst auf dem Handy**: Safe Area, Daumen-Reichweite, Bildschirmgrößen, Performance.

## Safe Area und Insets ✅
- `ScreenGui.ScreenInsets` bestimmt, wie weit UI vom Bildschirmrand (Notch, Top-Bar, Roblox-UI) entfernt bleibt.
- **Standard `CoreUISafeInsets`:** hält UI frei von Roblox-UI und Gerätesperrungen. Sicher, nutzt aber weniger Platz.
- **`DeviceSafeInsets`:** nur Gerätesperrungen berücksichtigt, mehr Platz, dafür selbst auf Roblox-Elemente achten.
- **`TopbarSafeInsets`:** berücksichtigt die Top-Bar.
- **`None`:** keine Insets, volle Kontrolle, hohes Risiko.
- Roblox schiebt UI standardmäßig unter die Top-Bar, außer man ändert es.
- Ziel: Wichtige Elemente nie unter Notch/Home-Indikator/Roblox-Buttons.

## Daumen-Zonen (🧠)
- Beim Handy-Spiel halten Spieler das Gerät quer, Daumen an den **unteren Seiten**.
- **Leicht erreichbar:** unten links und unten rechts, Seitenränder.
- **Schwer erreichbar:** obere Mitte, Mitte (Daumen verdeckt Sicht).
- **Aktionen** (Springen, Angriff, Interaktion): unten rechts.
- **Bewegung** (Joystick): unten links (Roblox-Standard-Steuerung nicht überdecken).
- **Seltenes** (Shop, Einstellungen): Ränder oben.

## Touch-Regeln
- Mindest-Trefferfläche ca. 44–48 px, besser größer; mit Abstand.
- **Kein Hover:** Alles Wichtige ohne Mauszeiger erreichbar.
- **Kein Rechtsklick/Tastatur-Zwang** für Kernfunktionen.
- **Gesten** nur zusätzlich, nie als einzige Möglichkeit.
- **Lange Listen:** ScrollingFrame, Momentum, klare Scroll-Hinweise.
- **Versehentliches Tippen vermeiden:** Bestätigung bei Kauf/Löschen.

## Bildschirmgrößen
- Teste mehrere Emulator-Geräte im Studio (Handy klein/groß, Tablet, Seitenverhältnisse).
- `UIAspectRatioConstraint` und `UISizeConstraint` einsetzen.
- Texte mit `UITextSizeConstraint` begrenzen.
- Keine festen Pixelmaße für komplette Fenster.
- Landscape primär; Hochformat nicht vergessen (Tablets, Geräte-Rotation).

## Performance auf Mobile (🧠 + Roblox-Praxis)
- **Teile/Parts begrenzen**, `StreamingEnabled` prüfen (offizielle Doku).
- **Partikel und Effekte** sparsam, besonders bei vielen Spielern/Pets.
- **Schatten/Beleuchtung:** einfachere Einstellungen für Mobile erwägen.
- **UI-Tweens:** nicht hunderte gleichzeitig.
- **Texturen:** kleine Auflösungen, Wiederverwendung.
- **Netzwerk:** RemoteEvents sparsam, Daten bündeln.
- **Speicher:** Assets freigeben, nicht alles gleichzeitig laden.
- **Messen:** Mikroprofiler und Entwickler-Konsole nutzen; auf echtem Low-End-Handy testen.

## Gamepad und Tablet
- Auswahl-Fokus (SelectionImageObject, `NextSelection*`), klare Fokus-Hervorhebung.
- Tablets: größere Fläche, aber Touch-Reichweite bleibt.

## Test-Checkliste
- [ ] Auf kleinem Handy: alles lesbar, nichts abgeschnitten
- [ ] Notch/Top-Bar verdeckt nichts Wichtiges
- [ ] Alle Buttons mit Daumen erreichbar
- [ ] Kauf-Flow komplett mit Touch
- [ ] Menü schließbar ohne Tastatur
- [ ] Kein Element unter Roblox-UI
- [ ] Framerate akzeptabel auf Low-End-Gerät
- [ ] Hoch- und Querformat geprüft

## Quellen
- [Creator Hub: ScreenInsets](https://create.roblox.com/docs/reference/engine/enums/ScreenInsets) ✅
- [Creator Hub: ScreenGui](https://create.roblox.com/docs/reference/engine/classes/ScreenGui) ✅
- [Creator Hub: HUD-Meter-Tutorial](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) ✅
