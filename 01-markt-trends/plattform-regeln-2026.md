# Plattform-Regeln 2026 (Alter, Chat, Moderation)

> Stand: 2026-10-24 · Gesamt-Vertrauen: ✅/🟡 (Roblox IR + DevForum-Ankündigungen; Zeitpläne können sich ändern, vor Umsetzung prüfen)

## Kurzfassung
Seit Anfang 2026 braucht jeder Nutzer einen **Alterscheck**, um Chat zu nutzen. Spieler werden in sechs Altersgruppen eingeteilt. Für Entwickler heißt das: Chat-Features sollten die Plattform-APIs nutzen und keine eigenen Systeme neben die Roblox-Lösungen stellen.

## Fakten
- **Alterscheck für Chat** weltweit, ab Januar 2026. Roblox erklärt, dass Funktionen wie Chat ohne abgeschlossenen Check nicht verfügbar sind. ✅
- **Sechs Altersgruppen:** unter 9, 9–12, 13–15, 16–17, 18–20, 21+. 🟡
- **Methode:** Gesichts-Altersschätzung; ID als Alternative ab 13. 🟡
- **Chat für unter 9** ist standardmäßig aus, außer ein Elternteil stimmt nach einem Alterscheck zu. 🟡
- **Erneute Prüfung** bei Kontowechsel oder auffälligem Verhalten. 🟡
- **Trusted Connections** (13+, altersgeprüft) können direkt im Spiel per Text und Voice über Altersgruppen hinweg chatten. 🟡
- **Neue API:** `GetChatGroupsAsync`, um vor dem Teleport zu prüfen, ob Spieler miteinander kommunizieren können. 🟡
- **Moderations-Berechtigung:** Gruppen können Mitgliedern (18+, altersgeprüft) Lesezugriff auf Experience-Chat geben. 🟡
- **Preset-Chat-System:** Roblox riet davon ab, ein eigenes System zu bauen, weil ein von Roblox definierter Preset-Dienst geplant war (Quelle nannte Juni) und Creators migrieren müssen. 🟡 → **Status bei Update prüfen.**
- Geplant laut Quelle: Chat-Zusammenfassungen (spät April), Kommunikationsmetriken (spät 2026). 🟡

## Konsequenzen für das Design (🧠)
1. **Nicht auf Textchat als Kernmechanik setzen.** Viele Spieler (vor allem junge) können nicht frei chatten.
2. **Koop ohne Chat funktionsfähig machen:** Emotes, Pings, Marker, Schnell-Nachrichten, Rollen.
3. **Altersgerechte Inhalte:** Horror/Gewalt/Glücksspiel-Optik bewusst gestalten, Content-Labels beachten.
4. **Zufallsmechaniken (Luck):** Roblox hat Richtlinien zu Zufallsbelohnungen (z. B. Anzeige von Wahrscheinlichkeiten). Offiziell vor Release prüfen, siehe `gacha-und-luck.md`. 🟠
5. **Keine Datensammlung** über Spieler, die Roblox-Regeln widerspricht.
6. **Eigene Preise/Shop-Texte** so formulieren, dass sie Kindern gegenüber nicht manipulativ wirken (Countdown-Druck, Fake-Knappheit vermeiden).

## Checkliste vor Release
- [ ] Chat-Funktionen nutzen die Roblox-Systeme
- [ ] Spiel ist ohne Chat vollständig spielbar
- [ ] Content-Label (Altersangaben im Creator Hub) korrekt ausgefüllt
- [ ] Zufallsmechaniken: Wahrscheinlichkeiten nach Roblox-Richtlinien offengelegt
- [ ] Reporting/Moderation-Wege vorhanden

## Quellen
- [Roblox Requires Users Worldwide to Age-Check to Chat – IR](https://ir.roblox.com/news/news-details/2026/Roblox-Requires-Users-Worldwide-to-Age-Check-to-Access-Chat/default.aspx) ✅
- [DevForum: Age Check Requirement Live Globally](https://devforum.roblox.com/t/age-check-requirement-to-chat-now-live-globally/4226101) ✅
- [DevForum, 6. Feb 2026: Age Check to Chat Fast-Follow Roadmap](https://devforum.roblox.com/t/february-6-2026-an-update-on-our-age-check-to-chat-fast-follow-roadmap/4340230) ✅
- [DevForum, 26. März 2026: Roadmap-Update](https://devforum.roblox.com/t/march-26-2026-an-update-on-our-age-check-to-chat-fast-follow-roadmap/4539685) ✅
