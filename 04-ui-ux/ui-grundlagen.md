# UI-Grundlagen

> Stand: 2026-10-24 · Gesamt-Vertrauen: ✅ für technische Eigenschaften (Creator Hub), 🟠 für Layout-Empfehlungen aus Community-Quellen, 🧠 für Designprinzipien

## Kurzfassung
Gutes Roblox-UI ist **lesbar auf dem Handy**, **zeigt das Wichtigste zuerst**, **reagiert sofort auf Eingaben** und **passt sich jeder Bildschirmgröße an**. Die meisten Spieler sind mobil (🧠, Plattform-Beobachtung; genaue Quote bei Update prüfen), deshalb wird zuerst für Touch entworfen.

## Prinzipien (🧠)
1. **Hierarchie:** Was ist am wichtigsten? Größe, Kontrast, Position, Farbe lenken den Blick.
2. **Weniger ist mehr:** Jedes Element muss Zweck haben. Verstecke Seltenes in Menüs.
3. **Konsistenz:** Gleiche Aktion = gleiche Form/Farbe/Position überall.
4. **Feedback:** Jede Eingabe braucht Reaktion (Animation, Ton, Zustandsänderung) innerhalb von ~0,1 s.
5. **Lesbarkeit:** Kontrast, Größe, einfache Schrift, kurze Texte.
6. **Fehlertoleranz:** Große Trefferflächen, Bestätigung vor Kauf, Rückgängig wo möglich.
7. **Fokus auf Spielwelt:** UI verdeckt nicht die Spielfläche.
8. **Identität:** Eigener, wiedererkennbarer Stil (Form, Farbe, Schrift, Animationsstil).

## Technische Grundlagen (Roblox) ✅
- **ScreenGui:** Behälter für UI auf dem Bildschirm.
- **ScreenInsets** (Property von ScreenGui): steuert die Sicherheitsränder. Alle UI-Objekte werden relativ zu diesen Grenzen positioniert. Werte laut Enum: `None`, `DeviceSafeInsets`, `CoreUISafeInsets`, `TopbarSafeInsets`. `CoreUISafeInsets` (Standard) hält UI frei von Roblox-UI und Gerätesperrungen (Notch); `DeviceSafeInsets` nutzt mehr Fläche auf kleinen Bildschirmen. Roblox schiebt UI standardmäßig unter die Top-Bar, es sei denn, es wird geändert.
- Verwandte ScreenGui-Properties: `ClipToDeviceSafeArea`, `IgnoreGuiInset`, `SafeAreaCompatibility` (im offiziellen Referenzdokument prüfen, Details bei Verwendung).
- **Scale statt Offset:** Positionen/Größen mit `UDim2` in Scale (Prozent) für verschiedene Auflösungen; Offset nur für feste Abstände.
- **UI-Constraints:** `UIAspectRatioConstraint`, `UISizeConstraint`, `UITextSizeConstraint`, `UIScale`.
- **Layouts:** `UIListLayout`, `UIGridLayout`, `UIPadding`, `UICorner`, `UIStroke`, `UIGradient`.
- **Text:** `TextScaled` mit `UITextSizeConstraint` (Min/Max), sonst wird Text auf manchen Geräten winzig oder riesig.
- **Eingaben:** Touch, Maus, Tastatur, Gamepad. UI muss mit allen funktionieren (Fokus/Auswahl für Gamepad).

## Layout-Orientierung (🟠 Community-Empfehlung, testen)
- **Ecken oben:** Dauerhafte Werte (Währung, Level, Gesundheit).
- **Unten Mitte:** Aktions-Buttons, Fähigkeiten, Werkzeug-Leiste (Daumen-Reichweite).
- **Seitenränder:** Sekundäre Menüs/Shop-Buttons.
- **Mitte:** Tabu für Dauer-UI; nur kurzzeitig Popups.
- **Oben Mitte:** Ziele/Timer (sparsam).
Diese Positionen sind ein Startpunkt; **testen** auf echten Handys.

## Größen-Richtwerte (🧠 zum Testen)
| Element | Richtwert |
|---|---|
| Touch-Button | mindestens ca. 44–48 px Höhe/Breite bei 1× Skalierung, besser größer |
| Abstand zwischen Buttons | Genug Luft, dass man nicht daneben tippt |
| Schrift (Fließtext) | gut lesbar auf 6"-Handy, nicht unter ca. 14–16 pt-Äquivalent |
| Überschrift | deutlich größer und fett |
| Kontrast | Hell auf Dunkel oder umgekehrt, nie Grau auf Grau |

## Farbe
- **Palette begrenzen:** 1 Hauptfarbe, 1–2 Akzente, Neutrale.
- **Bedeutung:** Grün = positiv/bestätigen, Rot = negativ/gefahr, Gold/Gelb = Währung/Premium, Blau = Info. Konsistent halten.
- **Seltenheitsfarben** (Common grau, Uncommon grün, Rare blau, Epic lila, Legendary orange/gold) sind Konvention bei Sammelspielen, Spieler verstehen sie sofort. 🟡
- **Barrierefreiheit:** Nicht nur Farbe als Information (zusätzlich Icon/Form), wegen Farbenblindheit.

## Typografie
- Maximal 2 Schriftarten.
- Fette, klare Schrift für Zahlen und Überschriften (Spiele nutzen oft abgerundete, verspielte Schriften).
- Text kurz halten: Zahlen und Icons statt Sätze.
- Sprache: Lokalisierung planen (Deutsch, Englisch, weitere), Platz für längere Texte lassen.

## Animation und Juice (🧠)
- **Tweens** für Öffnen/Schließen (0,15–0,3 s), federnde Kurven wirken lebendig.
- **Zahlen-Zähler** statt abruptem Springen.
- **Treffer-Feedback:** Pulse, Funken, Wackeln bei Belohnung.
- **Nicht übertreiben:** Animationen dürfen Aktionen nie verzögern.
- **Performance:** Wenige gleichzeitige Tweens auf Mobile.

## Icon-Design
- Einfache, klare Silhouette, erkennbar bei kleiner Größe.
- Einheitlicher Stil (Strichstärke, Perspektive, Schatten).
- Icons + kurze Beschriftung bei neuen Funktionen.

## Do / Don't
| Do | Don't |
|---|---|
| Für Handy zuerst bauen | Nur am PC-Monitor testen |
| Scale + Constraints | Feste Pixelgrößen überall |
| `ScreenInsets` bewusst setzen | UI unter Notch/Top-Bar verstecken |
| Große, klare Buttons | Winzige Klickflächen |
| Konsistente Farben/Icons | Jedes Menü anders |
| Feedback bei jeder Aktion | Stille Buttons |

## Verknüpfungen
`hud-shop-menues.md`, `mobile-first.md`, `checklisten/ui-review.md`

## Quellen
- [Creator Hub: ScreenInsets Enum](https://create.roblox.com/docs/reference/engine/enums/ScreenInsets) ✅
- [Creator Hub: ScreenGui](https://create.roblox.com/docs/reference/engine/classes/ScreenGui) ✅
- [Creator Hub: HUD-Meter-Tutorial](https://create.roblox.com/docs/tutorials/use-case-tutorials/ui/create-hud-meters) ✅
- [DevForum: Designing UI – Tips and Best Practices](https://devforum.roblox.com/t/3074034) ✅ (Roblox Engine-UI-Team, Details dort nachlesen)
- [Roblox UI Design Best Practices – creation.dev](https://www.creation.dev/blog/roblox-ui-design-best-practices) 🟠
