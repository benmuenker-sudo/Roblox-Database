# Update-Prompt: Datenbank aktualisieren und verbessern

> Gib diesen Prompt in eine Claude-Code-Session mit Zugriff auf dieses Repo. Er kann auch als wöchentlich geplante Aufgabe laufen (z. B. über eine geplante Aufgabe/Routine in Claude Code).

---

Du pflegst die Roblox Database in diesem Repo. Aktualisiere sie auf den heutigen Stand.

**Ablauf**
1. Lies `INDEX.md`, `CHANGELOG.md` und `README.md` (Vertrauensgrade ✅🟡🟠🧠).
2. **Markt:** Suche per Websuche die aktuellen Roblox-Charts, Aufsteiger der letzten 30 Tage, neue Hits, Genre-Verschiebungen. Aktualisiere `01-markt-trends/aktuelle-top-spiele.md`, `genre-analyse.md`, `viral-hits-analyse.md`. Kennzeichne jede Zahl mit Quelle, Datum und Vertrauensgrad. Widersprüche zwischen Quellen offen benennen.
3. **Plattform:** Prüfe Roblox Newsroom, Creator Hub und DevForum-Ankündigungen auf Änderungen bei Discovery, Alterscheck/Chat, Zufallsregeln, Monetarisierung, DevEx. Aktualisiere `discovery-algorithmus.md`, `plattform-regeln-2026.md`, `07-monetarisierung/monetarisierung.md`. Ersetze 🟠-Angaben durch ✅, wenn offizielle Quellen sie bestätigen.
4. **Design:** Suche nach neuen Erkenntnissen zu UI, Onboarding, Retention, Sound, Leveldesign, Luau-Praxis. Ergänze nur belegte Inhalte; markiere Eigenes als 🧠.
5. **Ideen:** Überarbeite `02-spielkonzepte/zukunftsideen.md` anhand neuer Marktdaten: Ideen streichen, die überholt sind; neue mit Begründung ergänzen.
6. **Qualität:** Prüfe Verweise (Links erreichbar?), entferne Duplikate, verbessere schwache Abschnitte, ergänze fehlende Beispiele.
7. **Protokoll:** Trage in `CHANGELOG.md` ein: Datum, geänderte Dateien, was neu/geändert/entfernt, offene Fragen.
8. Aktualisiere das Stand-Datum in jeder geänderten Datei.

**Regeln**
- Keine erfundenen Zahlen oder API-Namen. Unbelegtes als 🟠 oder 🧠 markieren oder weglassen.
- Keine urheberrechtlich geschützten Bilder/Audios einfügen; nur Links und Beschreibungen.
- Schreibe auf Deutsch, klar und konkret.
- Committe mit aussagekräftiger Nachricht und pushe auf den vereinbarten Branch.

---

## Optionale Fokus-Varianten
- **Nur Trends:** Schritte 2 und 5.
- **Nur Plattform-Regeln:** Schritt 3.
- **Vertiefung:** „Recherchiere Thema X tief und schreibe eine neue Datei nach `_templates/THEMA-VORLAGE.md`."
