# Checkliste: Release

## Qualität
- [ ] Onboarding getestet (Mobile + PC), Funnel-Schritte messbar
- [ ] Keine kritischen Bugs (Duplikate, Datenverlust, Kauf-Fehler)
- [ ] Performance auf Low-End-Handy akzeptabel
- [ ] Server- und Client-Fehler geloggt

## Technik
- [ ] Alle Wert-Logik serverseitig, Remotes validiert
- [ ] DataStore: Fehlerfälle getestet, `BindToClose`
- [ ] Käufe: `ProcessReceipt` idempotent, Gamepass-Prüfung
- [ ] Zufall am Server, Wahrscheinlichkeiten = Anzeige

## Plattform und Regeln
- [ ] Altersangaben/Content-Labels im Creator Hub korrekt
- [ ] Chat-Features nutzen Roblox-Systeme, Spiel ohne Chat spielbar
- [ ] Zufallsmechaniken nach aktuellen Roblox-Richtlinien (Wahrscheinlichkeiten offen)
- [ ] Keine fremden Assets/Marken ohne Recht

## Darstellung
- [ ] Icon, Thumbnails, Titel, Beschreibung: ehrlich und klar
- [ ] Trailer/Clips vorbereitet
- [ ] Audio-Mix geprüft, Musik/SFX regelbar

## Analytics
- [ ] Retention, Funnel, Sitzungsdauer, Monetarisierungs-Events aktiv
- [ ] Ziele für D1/D7/D30 aus Benchmark-Scorecards abgeleitet (ab ca. 100 DAU)

## Live-Ops
- [ ] Event-Kalender der ersten 8 Wochen
- [ ] Update-Pipeline, Rollback-Plan, Community-Kanal
