# Checkliste: Release

> Stand: 2026-10-24 · Details in den verlinkten Dateien

## Veröffentlichung und Reichweite (seit 19.05.2026) → `01-markt-trends/plattform-regeln-2026.md`
- [ ] Konto: gutes Standing, mind. 2 Tage alt, Alterscheck erledigt (reicht für 16+)
- [ ] Zielgruppe unter 16 gewünscht? Dann: Verifikation, 2FA, 2 Monate Plus/Premium **oder** 1.000 Robux (rückzahlbar)
- [ ] Maturity-&-Compliance-Fragebogen vollständig (sonst Label „Content May Vary“, nur 16+)
- [ ] Plan für die Evaluationsphase: 250 Plays hoch engagierter, altersgeprüfter 16+-Nutzer in 60 Tagen, oder Expedited Review (50.000 Robux)
- [ ] Eigenes Thumbnail hochgeladen (Pflicht für Home-Empfehlungen), 2–5 Varianten für Personalisierung → `04-ui-ux/thumbnails-und-icons.md`
- [ ] Icon 512×512, lesbar bei 150×150
- [ ] Titel, Beschreibung und Thumbnails passen zum Inhalt (irreführende Metadaten begrenzen Reichweite)
- [ ] Spiel ist eigenständig (Kopien werden als „Non-unique“ gedrosselt)

## Erste Sitzung (RFY-Ranking) → `01-markt-trends/discovery-algorithmus.md`
- [ ] Spaß in unter 5 Minuten, erste Aktion in Sekunden (Bounce unter 60 s / 61–180 s ist ein negatives Signal)
- [ ] Gründe für Rückkehr an möglichst vielen der Tage 2–7 und 8–28
- [ ] Koop über Join/Einladung/private Server einfach (Co-Play-Tage sind ein Signal)
- [ ] Funnel-Events für das Onboarding eingerichtet → `03-mechaniken-retention/analytics-und-experimente.md`

## Qualität
- [ ] Onboarding getestet (Mobile + PC + Gamepad)
- [ ] Keine kritischen Bugs (Duplikate, Datenverlust, Kauf-Fehler)
- [ ] Performance auf Low-End-Android (2–4 GB RAM) akzeptabel → `05-map-leveldesign/beleuchtung-und-performance.md`
- [ ] Server-Speicher unter ca. 50 % der Zuteilung

## Technik → `08-technik-luau/`
- [ ] Alle Wert-Logik serverseitig, Remotes validiert und rate-limitiert
- [ ] DataStore: Fehlerfälle getestet, Laden-Fehlschlag sperrt Speichern, Speichern bei `BindToClose`
- [ ] Käufe: `ProcessReceipt` mit PurchaseId-Prüfung, nur `PurchaseGranted` nach erfolgreichem Speichern
- [ ] Zufall am Server, Quoten = Anzeige

## Monetarisierung und Regeln → `07-monetarisierung/`
- [ ] Zufallsitems: Quoten in % (Summe 100) vor dem Kauf, `ArePaidRandomItemsRestricted` geprüft, nicht-zufällige Alternative
- [ ] Spiel ohne Käufe fair spielbar
- [ ] Keine Fake-Timer, keine Druck-Texte, Info-Button beschriftet („Info“/„Details“)
- [ ] Managed/Regionalpreise bewusst aktiviert oder deaktiviert
- [ ] Bei 18+-DevEx-Kurs: nur R15-Avatare
- [ ] Keine Social-Media-Links im Spiel (nur auf der Detailseite)

## Chat und Social → `03-mechaniken-retention/social-loops.md`
- [ ] Spiel ohne freien Chat vollständig spielbar
- [ ] Eigene Presets regelkonform (max. 12, 10 s Rate-Limit, nur Spielkoordination) oder Quick Words
- [ ] Vor Teleports in gemeinsame Server `GetChatGroupsAsync` berücksichtigt

## Darstellung
- [ ] Trailer/Clips vorbereitet
- [ ] Audio-Mix geprüft, Musik/SFX getrennt regelbar
- [ ] Rechte an allen Assets geklärt

## Analytics
- [ ] Retention, Funnel, Economy-Events (max. 5 Währungen planen), Custom Events aktiv
- [ ] Ab 100 DAU: Benchmark-Scorecards vergleichen; ab ca. 1.000 DAU: Experiments nutzen

## Live-Ops
- [ ] Event-Kalender der ersten 8 Wochen (max. 10 aktive Events, 1 Benachrichtigung pro Nutzer und Tag)
- [ ] Update-Pipeline, Rollback-Plan, Community-Kanal
