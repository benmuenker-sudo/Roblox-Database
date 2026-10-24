# Checkliste: UI-Review

## Mobile
- [ ] Alles auf kleinem Handy lesbar und erreichbar
- [ ] `ScreenInsets` bewusst gesetzt; nichts unter Notch/Top-Bar/Roblox-UI
- [ ] Trefferflächen groß genug, Abstand ausreichend
- [ ] Kein Hover/Rechtsklick/Tastatur-Zwang

## Layout
- [ ] Scale + Constraints, keine festen Pixelfenster
- [ ] Text mit `UITextSizeConstraint`
- [ ] HUD ≤ ca. 6–8 Dauer-Elemente
- [ ] Zahlen im Kurzformat

## Inhalt
- [ ] Hierarchie klar (wichtig = groß/kontrastreich)
- [ ] Farben und Icons konsistent
- [ ] Farbe nie alleiniger Informationsträger
- [ ] Texte kurz, lokalisierbar

## Interaktion
- [ ] Feedback (Animation + Ton) bei jeder Aktion
- [ ] Menüs max. 2 Ebenen, großer Schließen-Button
- [ ] Kauf: Bestätigung mit Preis, Fehlerfälle abgedeckt
- [ ] Gamepad-Navigation funktioniert

## Performance
- [ ] Nicht hunderte gleichzeitige Tweens
- [ ] UI-Elemente wiederverwendet
