# Changelog

## 2026-10-24 – Version 2: Deep Research, offizielle Doku, Bilder und Sounds
**Recherche**
- Tiefe Recherche in 6 Bereichen (Markt, Plattform/Discovery/Regeln, Monetarisierung, Retention/Live-Ops, UI/Map/Sound, Luau-Technik), Notizen in `research_notes/`
- Alle Kernaussagen gegen den Quelltext der **offiziellen Roblox Creator Documentation** geprüft (GitHub `Roblox/creator-docs`, Commit 4e795e6); Ergebnis in `research_notes/.../offizielle_doku_verifikation.md`
- Recherchebericht: `reports/Roblox Markt und Game Design.md`

**Neue Dateien (13)**
- 01: `plattform-kennzahlen.md`, `ads-und-akquise.md`
- 03: `analytics-und-experimente.md`, `fallstudien.md`
- 04: `thumbnails-und-icons.md`, `eingabe-und-barrierefreiheit.md`
- 05: `beleuchtung-und-performance.md`
- 06: `audio-api-und-upload.md`
- 07: `einnahmequellen-und-auszahlungen.md`, `preisgestaltung-und-shop-design.md`, `ethik-und-recht.md`
- 08: `datenspeicherung.md`, `kaeufe-und-sicherheit.md`, `performance-und-tooling.md`

**Stark erweitert:** alle bisherigen Themendateien (von ca. 15.000 auf rund 100.000 Wörter insgesamt)

**Bilder und Audio**
- 23 selbst erstellte Referenzbilder (SVG + PNG) in `assets/bilder/`
- 121 offizielle Doku-Bilder (CC BY 4.0) in `assets/bilder/offiziell/`
- 26 selbst synthetisierte Sounds (WAV + OGG) und Wellenform-Übersicht in `assets/audio/`
- Generator-Skripte in `tools/`

**Wichtigste Korrekturen gegenüber Version 1**
- DevEx 0,0035 → **0,0038 $/Robux** (seit 05.09.2025); neu: US-18+-Kurs 0,0054 $ (nur R15)
- Premium Payouts → **Creator Rewards** (seit 24.07.2025)
- Neue Spiele starten **16+** (seit 19.05.2026); unter-16-Freischaltung 250 Plays in 60 Tagen
- Discovery: nur organische RFY-Nutzer zählen, PTR + Bounce statt QPTR, Today's Picks redaktionell
- Gesamtauszahlungen 2025: 1,503 Mrd. $ (10-K)
- Survival-Anteil „20 %“ nicht bestätigt, entfernt; Obby-D1 „25–35 %“ entfernt (über Top-1-%-Wert)
- Sound/SoundGroup → neues **Audio-API** empfohlen
- DataStore-Limits: Budget pro Spiel (300 + 40×CCU Lesen) **und** pro Server

**Dringender Hinweis (Stand 24.10.2026):** Ab 01.11.2026 gelten DevEx-Auszahlungen in den USA steuerlich als Lizenzgebühren; Creator außerhalb der USA ohne gültige Steuerangaben bis **31.10.2026** riskieren 24 % Einbehalt. → `07-monetarisierung/einnahmequellen-und-auszahlungen.md`

**Offene Lücken:** siehe `SOURCES.md` → „Bekannte Lücken"

## 2026-10-24 – Erstversion
- Gesamtstruktur `01`–`08`, Checklisten, Assets-Referenzlisten, Automation
- Nur Websuche verfügbar, viele Zahlen 🟠
