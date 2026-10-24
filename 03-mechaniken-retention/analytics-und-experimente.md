# Analytics und Experimente: messen, vergleichen, testen

> Stand: 2026-10-24 · Nächste Prüfung: 2026-11-21 · Gesamt-Vertrauen: ✅ für Dashboard-Funktionen, Limits und Experiment-Regeln (Creator Docs), 🟡 für Plattform-Benchmarks (GameAnalytics), 🧠 für Zielwerte und Vorgehen

## Kurzfassung
Roblox liefert ein eigenes Analytics-System mit Retention-, Engagement-, Akquise- und Monetarisierungs-Dashboards, Benchmarks gegen ähnliche Spiele (50.–90. Perzentil), Funnel-, Economy- und Custom-Events sowie A/B-Tests („Experiments“) und Live-Werte („Configs“). ✅ Auf Roblox sind die Retention-Werte viel niedriger als in Mobile-Spielen: Der Median großer Spiele liegt bei **D1 10,3 % / D7 1,6 % / D30 0,5 %**. 🟡 Roblox rät, zuerst **D1 und durchschnittliche Sitzungszeit** auf Benchmark-Niveau zu bringen, dann D7/D30, dann Monetarisierung, und erst danach Traffic zu kaufen. ✅ Experiments laufen 14–60 Tage und brauchen in der Praxis über 1.000 DAU. Kleine Spiele arbeiten deshalb mit Funnels und Playtests statt mit A/B-Tests. ✅

## Referenzbilder
Offizielle Bilder aus der Roblox Creator Documentation (CC BY 4.0, Übersicht und Lizenz: `assets/bilder/offiziell/README.md`).

![Benchmark-Scorecard](../assets/bilder/offiziell/analytics/benchmark-scorecard-uebersicht.png)
*Benchmark-Scorecard mit Playtime, D1/D7, Payer Conversion, ARPPU und Play-Through-Rate. Zeigt, welcher Bereich am meisten Potenzial hat. Quelle: Roblox Creator Docs, CC BY 4.0 ([Analytics](https://create.roblox.com/docs/production/analytics))*

![Benchmark-Band ähnliche Spiele](../assets/bilder/offiziell/analytics/benchmark-aehnliche-spiele-d7.png)
*Retention-Chart mit Benchmark-Band „experiences with similar players“ (50.–90. Perzentil). Quelle: Roblox Creator Docs, CC BY 4.0 ([Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard))*

![Übersichtsseite](../assets/bilder/offiziell/analytics/wachstum-uebersichtsseite.png)
*Spielübersicht mit Insights, Benchmarks und Echtzeitwerten (CCU, Crash-Rate, Frame-Rate). Quelle: Roblox Creator Docs, CC BY 4.0 ([Analytics](https://create.roblox.com/docs/production/analytics))*

![Retention-Diagramm](../assets/bilder/offiziell/analytics/retention-diagramm.png)
*D1/D7/D30 nach Kohorten-Datum. Ein Einbruch nach einer großen Neuspieler-Welle ist laut Doku typisch und vorübergehend. Quelle: Roblox Creator Docs, CC BY 4.0 ([Retention](https://create.roblox.com/docs/production/analytics/retention))*

![Kohortenanalyse](../assets/bilder/offiziell/analytics/retention-kohortenanalyse.png)
*Wöchentliche Kohortentabelle: Neue Nutzer pro Woche und Retention in Woche 1–4. Quelle: Roblox Creator Docs, CC BY 4.0 ([Retention](https://create.roblox.com/docs/production/analytics/retention))*

![Neue-Nutzer-Funnel nach Quelle](../assets/bilder/offiziell/analytics/akquise-neue-nutzer-funnel.png)
*Akquisequellen (Home, Search, Friends, Ads …) mit Conversion, D7, Playtime und Umsatz. Quelle: Roblox Creator Docs, CC BY 4.0 ([Acquisition](https://create.roblox.com/docs/production/analytics/acquisition))*

![Economy- und Funnel-Dashboards](../assets/bilder/offiziell/analytics/economy-und-funnel-dashboards.png)
*Economy- und Funnel-Dashboard, gefüllt aus wenigen Events. Quelle: Roblox Creator Docs, CC BY 4.0 ([Event types](https://create.roblox.com/docs/production/analytics/event-types))*

![Quellen und Senken](../assets/bilder/offiziell/analytics/economy-quellen-senken-gesamt.png)
*Alle Währungsquellen und -senken nach Kategorie mit Netto-Linie. Quelle: Roblox Creator Docs, CC BY 4.0 ([Economy events](https://create.roblox.com/docs/production/analytics/economy-events))*

![Durchschnittliches Wallet](../assets/bilder/offiziell/analytics/economy-durchschnittliches-wallet.png)
*Durchschnittliches Guthaben getrennt nach Zahlern, allen Nutzern und Nichtzahlern. Quelle: Roblox Creator Docs, CC BY 4.0 ([Economy events](https://create.roblox.com/docs/production/analytics/economy-events))*

![Funnel Pflanzenspiel](../assets/bilder/offiziell/analytics/funnel-pflanzenspiel-dropoff.png)
*Onboarding-Funnel des Referenzspiels „Plant“: 70 % Abbruch zwischen „In Farm“ und „Plant Seed“. Quelle: Roblox Creator Docs, CC BY 4.0 ([Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events))*

![Experiment-Ergebnisse](../assets/bilder/offiziell/analytics/experiment-ergebnisse.png)
*Ergebnisseite eines A/B-Tests mit signifikanten Metriken in Grün/Rot. Quelle: Roblox Creator Docs, CC BY 4.0 ([Experiments](https://create.roblox.com/docs/production/experiments))*

![Custom Dashboard](../assets/bilder/offiziell/analytics/custom-dashboard-beispiel.png)
*Eigenes Dashboard „Player Progression“ mit Summary-Cards und vier Charts. Quelle: Roblox Creator Docs, CC BY 4.0 ([Custom dashboards](https://create.roblox.com/docs/production/analytics/custom-dashboards))*

## Warum das wichtig ist
- Seit dem RFY-Umbau zählt Roblox für die Home-Empfehlung Signale getrennt für **Tag 1, Tag 2–7 und Tag 8–28**. Wer die eigenen Kohorten nicht liest, sieht nicht, warum Impressionen fallen. ✅ ([Discovery](https://create.roblox.com/docs/discovery))
- Roblox sagt selbst: Das RFY-Update gibt „highly retentive games“ mehr Impressionen, auf Kosten kurzfristiger Monetarisierung. ✅ ([Q2-2026-Shareholder-Letter](https://s27.q4cdn.com/984876518/files/doc_financials/2026/q2/Roblox-Q2-2026-Earnings-Shareholder-Letter.pdf))
- Benchmarks fließen **nicht** in den Algorithmus ein. Sie sind nur ein Vergleichspunkt für dich. ✅ ([Analytics](https://create.roblox.com/docs/production/analytics); [Discovery](https://create.roblox.com/docs/discovery))

## Details

### 1. Zugang und Schwellen
| Funktion | Voraussetzung | Vertrauen / Quelle |
|---|---|---|
| Alle KPIs im Analytics-Dashboard | mehr als **10 DAU und 10 Spielstunden an 7 aufeinanderfolgenden Tagen**, verifizierte E-Mail, 2FA, Nutzungsbedingungen akzeptiert | ✅ [Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard) |
| Benchmark-Scorecards (ähnliche Spiele) | **100+ DAU** | ✅ [Analytics](https://create.roblox.com/docs/production/analytics) |
| Vergleichsspiele im Benchmark-Pool | Spiele mit mindestens 100 DAU, täglich aktualisiert | ✅ [Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard) |
| Performance-Charts (Client/Server) und Alerts | **100+ DAU** | ✅ [Alerts](https://create.roblox.com/docs/production/analytics/alerts); [Performance](https://create.roblox.com/docs/production/analytics/performance) |
| Experiments mit brauchbaren Daten | Doku: unter **1.000 DAU** „might struggle to get useful data“ | ✅ [Experiments](https://create.roblox.com/docs/production/experiments) |
| Erste Event-Charts | bis zu 24 h nach dem ersten Event; „View Events“ zeigt Rohdaten fast in Echtzeit | ✅ [Event types](https://create.roblox.com/docs/production/analytics/event-types) |
| Export als CSV | erst nach 48 h Dashboard-Teilnahme und mit Daten | ✅ [Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard) |

### 2. Die Dashboards im Überblick ✅
| Seite | Was sie zeigt | Wofür du sie nutzt |
|---|---|---|
| **Overview** | Wöchentliche Bewegungen, Benchmark-Scorecards, Insights, Echtzeit (CCU, Crash-Rate, FPS) | Wochenroutine: große Bewegungen finden |
| **Retention** | D1/D7/D30 nach Erstspieldatum; Tageskohorten (10 Tage), Wochenkohorten (10 Wochen); je Kohorte 7D-Playtime, 7D-Payer-Conversion, 7D- und 30D-Umsatz pro Nutzer | Effekt von Updates/Events auf neue Kohorten |
| **Engagement** | Durchschnittliche Sitzungszeit, „New User First Session Retention“ (wer spielt nach X Minuten noch) | Onboarding-Probleme nach Updates erkennen |
| **Acquisition** | Neue/zurückkehrende Nutzer pro Quelle, Impressionen, Play-Through-Rate, Neue-Nutzer-Funnel | Qualität der Quellen vergleichen |
| **Monetization** | Umsatz (Produkte, Passes, Kommissionen), Conversion, Paying Users, ARPPU, ARPDAU | Shop- und Preisarbeit |
| **Economy / Funnel / Custom** | entstehen erst, wenn du Events sendest | Wirtschaft, Abbrüche, eigene Metriken |
| **Explore** | Freie Charts, Formeln („Use operations“), Benchmark-Overlay, Period-over-Period, 7-Tage-Durchschnitt | Eigene Fragen beantworten |

Quellen: [Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard), [Retention](https://create.roblox.com/docs/production/analytics/retention), [Engagement](https://create.roblox.com/docs/production/analytics/engagement), [Acquisition](https://create.roblox.com/docs/production/analytics/acquisition), [Monetization](https://create.roblox.com/docs/production/analytics/monetization) ✅

**Wichtige Definitionen aus der Doku** ✅
- **D1:** Anteil neuer Nutzer, die nach ihrem ersten Besuch am nächsten Tag wiederkommen. **D7** = Rückkehr am 8. Tag (Day 7), **D30** = am 31. Tag (Day 30). D7/D30-Werte der jüngsten Kohorten sind zwangsläufig noch leer. ([Retention](https://create.roblox.com/docs/production/analytics/retention))
- **Sitzungszeit:** Gesamtspielzeit geteilt durch Anzahl Sitzungen. ([Engagement](https://create.roblox.com/docs/production/analytics/engagement))
- **Conversion Rate:** Anteil der DAU, die zahlen. **ARPDAU** = Conversion × ARPPU. „Hohes ARPPU bei niedrigem ARPDAU“ heißt: Umsatz kommt von wenigen. ([Monetization](https://create.roblox.com/docs/production/analytics/monetization))
- **Platform Spender (Active):** mindestens 9,99 $ irgendwo auf Roblox in den letzten 60 Tagen, gleiche Definition wie bei Creator Rewards. ([Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard))

### 3. Filter und Segmente (Dashboard, Configs, Experiments) ✅
Dieselben Segmente gibt es als Dashboard-Filter, als Config-Bedingung und als Experiment-Targeting ([Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard); [Configs](https://create.roblox.com/docs/production/configs)):

| Segment | Stufen |
|---|---|
| Active payer status (im Spiel, perzentilbasiert) | Top 15 % (85.–100. Perzentil), Intermediate 35 %, Casual 50 %, Lapsed (30 Tage nichts gekauft), Never |
| Platform spender status | Active (≥ 9,99 $ / 60 Tage) oder Other |
| In-experience activity status | Early (erste 30 Tage), Active, Lapsed (30 Tage keine Sitzung), Reactivated (30 Tage nach Rückkehr), Never played |
| User engagement | Inactive (0 Tage), Low (1), Medium (2–3), High (4–7 Tage in den letzten 7) |
| Platform activity status | New signup (60 Tage), Active, Lapsed, Reactivated (60-Tage-Fenster) |
| When user first played | 0–30, 31–90, 91–180, 181–365, 365+ Tage, never |
| Weitere | Alter (<9, 9–12, 13–15, 18+ …), Geschlecht, Land, Sprache, Quelle, Plattform, OS, Speichergruppe (<2 GB … >8 GB) |

### 4. Benchmarks: offiziell vs. Drittanbieter

**Offizielle Benchmarks** ✅ ([Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard))
- Vergleich mit „Games with similar players“. Wenn das Modell zu wenige findet: **Genre**, dann **All experiences**. Wechsel des Sets wird im Chart annotiert.
- Benchmarked KPIs: alle Retention-KPIs, durchschnittliche Sitzungszeit, ARPPU, ARPDAU, Conversion Rate, Play-Through-Rate.
- Dargestellt als **50.–90. Perzentil**. Offizielles Beispiel: D1-Band **12,11 %–18,73 %** heißt, 50 % der ähnlichen Spiele liegen bei 12,11 % oder darunter, 10 % bei 18,73 % oder darüber.
- Für „Overall success“-KPIs: Pool sind die **Top 1.000 Spiele nach Gesamtspielzeit (rollierend 30 Tage)**, ohne Spiele unter 30 Tagen Alter, mit Stufen **Top 200 / Top 500 / Top 1000**.
- Seit Ende 2025 lassen sich D1/D7/D30 **nach Akquisequelle** ansehen, mit Wahl zwischen „similar experiences“- und Genre-Benchmark. ✅ ([DevForum-Ankündigung](https://devforum.roblox.com/t/analytics-view-retention-by-acquisition-source-and-select-your-benchmark-set/4010157))

> **Korrektur:** Ältere Notizen nannten ein D1-Band von 12,4–24,1 % und die URL `.../sales-data`. Die aktuelle Doku nennt **12,11–18,73 %** auf der Seite *Analytics dashboard*. ✅

**Plattform-Benchmarks GameAnalytics 2026** 🟡 ([GameAnalytics 2026 Roblox Report](https://www.gameanalytics.com/reports/2026-roblox-report); Zusammenfassung [GameDevReports](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox))
Stichprobe: über 500 Spiele mit mindestens 1 Mio. MAU, August 2025 bis Juli 2026, 4,76 Mrd. Sitzungen.

| Kennzahl | 25. Perzentil | Median | Top 5 % | Top 1 % |
|---|---|---|---|---|
| D1-Retention | 8,4 % | **10,3 %** | – | **22,2 %** |
| D7-Retention | – | **1,6 %** | – | **9,1 %** |
| D30-Retention | 0,3 % | **0,5 %** | – | **4,7 %** |
| Sitzungslänge pro Spiel | – | **9,8 min** | 16,6 min | 21,1 min |
| Sitzungen pro Spieler und Tag (pro Spiel) | – | 1,56 | – (Top 10 %: 3,22) | 8,3 |

Spielerebene (über alle Spiele) 🟡 ([GameDevReports](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox)): Median-Sitzung 7,28 min (Top 1 %: 74,82 min); Median-Spielzeit pro Tag 22,4 min (Top 10 %: 123,85 min, Top 1 %: 404,98 min). Roblox' eigene Zahl von rund 2,7 h/Tag enthält auch Chat und Avatar-Editor.

Einordnung:
- GameAnalytics nennt die Medianwerte „normal for the platform, not a sign of a failing game“. Die Faustregel „20 % D1 gut, 40 % exzellent“ stammt laut Bericht aus kleinen Stichproben bereits beworbener Spiele. 🟡 ([GameAnalytics 2026](https://www.gameanalytics.com/reports/2026-roblox-report))
- 2025 war der größte Wandel die **Rückkehrfrequenz** (mehr Sitzungen), nicht längere Sitzungen. Im Sitzungsband 0–3 min lag das 75. Perzentil bei etwa D1 7,4 % / D7 1,0 % / D30 0,3 %. Andere Stichprobe, nicht direkt mit 2026 vergleichbar. 🟡 ([GameAnalytics 2025](https://www.gameanalytics.com/reports/2025-roblox-report))
- Mobile-Werte wie 40/20/10 gelten **nicht** für Roblox. 🟡 ([Playio](https://blog.playio.co/d1-d7-d30-retention-benchmarks-2026))
- Genre-Tabellen von Drittseiten (z. B. „Obby D1 25–35 %“) sind methodisch unklar und liegen über dem Top-1-%-Wert von GameAnalytics. Nicht als Ziel verwenden. 🟠 ([rowatcher](https://rowatcher.com/news/retention-benchmarks-by-roblox-genre-what-good-actually-looks-like); [BLOXG](https://bloxg.com/statistics/roblox-retention-benchmarks))

### 5. KPI-Definitionen und Zielwerte

**Pragmatische Zieltabelle** (🧠, abgeleitet aus GameAnalytics 🟡 und der offiziellen Benchmark-Logik ✅; für Spiele unter 1 Mio. MAU sind niedrigere Werte normal, weil GameAnalytics sie nicht erfasst):

| KPI | Definition | Warnsignal | Solide | Stark | Elite |
|---|---|---|---|---|---|
| D1 | Rückkehr am Folgetag | < 8 % | ~10 % (Median) | ≥ 15 % | ≥ 20 % |
| D7 | Rückkehr an Tag 8 | < 1 % | ~1,6 % | ≥ 3 % | ≥ 5 % |
| D30 | Rückkehr an Tag 31 | < 0,3 % | ~0,5 % | ≥ 1 % | ≥ 2 % |
| Ø Sitzung pro Spiel | Spielzeit / Sitzungen | < 6 min | ~10 min | ≥ 16 min | ≥ 21 min |
| Sitzungen/Spieler/Tag | Rückkehr am selben Tag | < 1,2 | ~1,5 | ≥ 3 | ≥ 8 |
| First Session Retention | Anteil nach 5 min noch im Spiel | Wochenvergleich fällt deutlich | stabil | steigt | – |
| Bounce (RFY) | Abgänge < 60 s / 61–180 s | über Benchmark | auf Benchmark | darunter | – |
| Payer Conversion | zahlende DAU / DAU | – | im Benchmark-Band | oberes Band | – |

Hinweise:
- Offiziell gibt es **keine** festen Zielwerte. Roblox will, dass du gegen dein eigenes 50.–90.-Perzentil-Band arbeitest. ✅ ([Analytics](https://create.roblox.com/docs/production/analytics))
- Ein DevForum-Entwickler nannte 1,2 % Payer Conversion „fairly good“. Einzelstimme. 🟠 ([DevForum](https://devforum.roblox.com/t/very-low-arppu-in-floor-race/3566999))
- Für RFY zählt Spielzeit nur bis **60 Minuten pro Nutzer, Spiel und Tag**. Längere Sitzungen bringen dort nichts. ✅ ([Discovery](https://create.roblox.com/docs/discovery))

**Der offizielle 3-Schritte-Plan** ✅ ([Analytics](https://create.roblox.com/docs/production/analytics))
1. Retention, Engagement, Monetarisierung auf Benchmark-Niveau: zuerst **D1 und Ø Sitzungszeit**, dann **D7/D30**, dann **Payer Conversion und ARPPU**.
2. Erst dann Akquise: Quellen vergleichen, PTR verbessern (Icon, Titel, Beschreibung testen), Events und Einladungen nutzen.
3. Nach jedem Update prüfen: D1/D7, Sitzungszeit, Conversion/ARPPU/Umsatz, neue Nutzer und PTR.

### 6. Retention nach Akquisequelle ✅
Quellen im Dashboard: Home recommendations, Continue play, Today's Picks, Home other, Friends, Search, Charts, Sponsored ads, Search ads, Portal ads, Teleport, Other ([Acquisition](https://create.roblox.com/docs/production/analytics/acquisition)).
Je Quelle: Users with plays, Conversion Rate (nach Impression), D7, 7D-Playtime pro Nutzer, 30D-Payer-Conversion, 30D-Umsatz pro Nutzer (ohne Abos, Engagement-Payouts, Immersive Ads).

Was daraus folgt:
- **RFY zählt im Ranking nur organisch über Home gewonnene Nutzer.** Werbe-, Freundes-, Such- und Social-Media-Nutzer zählen dort nicht. Werbenutzer gelten danach als „already acquired“ und bekommen das Spiel meist nicht mehr in RFY angezeigt. ✅ ([Discovery](https://create.roblox.com/docs/discovery); [Discovery FAQ](https://create.roblox.com/docs/discovery-faq))
- Deshalb immer **„Home recommendations“-Kohorte** gegen Benchmark lesen, nicht nur den Gesamtwert. 🧠
- Ads liefern laut RDC-2025-Recap im typischen Fall +150 % Impressionen, +24 % Plays, +16 % Spielzeit (je nach Budget). ✅ ([DevForum Ads Recap](https://devforum.roblox.com/t/ads-for-creators-rdc-recap-and-what%E2%80%99s-next/3929106))
- Eine große Welle neuer Nutzer drückt die Retention der Kohorte vorübergehend. Das ist laut Doku normal. ✅ ([Retention](https://create.roblox.com/docs/production/analytics/retention))
- Off-Platform: **Share Links** messen Link-Besuche, qualifizierte Plays, 7D-Playtime, D7 und 30D-Umsatz pro Kanal. ✅ ([Acquisition](https://create.roblox.com/docs/production/analytics/acquisition))

### 7. Event-Tracking: Funnel, Economy, Custom

**Gemeinsame Regeln** ✅ ([Event types](https://create.roblox.com/docs/production/analytics/event-types); [AnalyticsService](https://create.roblox.com/docs/reference/engine/classes/AnalyticsService))
- Events **nur vom Server** und **nur in veröffentlichten Spielen** (nicht aus Client oder Studio).
- Events erst **nach** erfolgreicher Aktion loggen (z. B. nach dem Kauf, nicht beim Kaufversuch).
- Ein Event verschwindet 90 Tage nach den letzten Daten aus dem Dashboard. Limits werden täglich zurückgesetzt.

**Limit-Tabelle** ✅ ([Event types](https://create.roblox.com/docs/production/analytics/event-types))
| Limit | Wert |
|---|---|
| Globales Rate-Limit | **120 + 20 × CCU** AnalyticsService-Anfragen pro Minute |
| Custom Fields | **3** pro Event (Werte nur als String) |
| Wertkombinationen über alle Custom Fields | **8.000**, danach „Other“ |
| Economy: Ressourcentypen (Währungen) | **10 laut Limit-Tabelle**, aber **5 laut AnalyticsService-Referenz und Economy-Dashboard** (siehe unten) |
| Economy: transactionTypes | nach **20** → „Other“ |
| Economy: itemSkus | nach **100** → „Other“ |
| Funnels | **10** pro Spiel, **100** Schritte je Funnel |
| Custom: eventNames | **100** |

> **Widerspruch in der Doku (Währungen):** Die Limit-Tabelle auf *Event types* nennt **10** Ressourcentypen. Die Referenz zu `LogEconomyEvent` sagt „Limited to 5 unique currency types per experience“, und das Economy-Dashboard sagt „You can add up to five currencies“. ✅ ([Event types](https://create.roblox.com/docs/production/analytics/event-types); [AnalyticsService](https://create.roblox.com/docs/reference/engine/classes/AnalyticsService); [Economy events](https://create.roblox.com/docs/production/analytics/economy-events)) → Plane mit **höchstens 5** und bilde Varianten über Custom Fields ab (Doku-Beispiel: statt `WarriorXP`, `MageXP` eine Währung `XP` plus Klasse als Custom Field). 🧠

**Funnel-Events** ✅ ([Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events))
- Typen: **Onboarding** (einmalig, `LogOnboardingFunnelStepEvent`), **Progression** und **Shop** (wiederkehrend, `LogFunnelStepEvent` mit `funnelSessionId`).
- Shop-Funnel: GUID als `funnelSessionId`. Upgrade-Pfade: Schlüssel wie `<playerId>-<itemId>`.
- Schritt 1 im `PlayerAdded` loggen, wenn der Funnel beim Join starten soll.
- Wiederholte Schritte zählen nur einmal (verbrauchen aber Rate-Limit). Übersprungene Schritte gelten als erledigt.
- Filter gelten nur für den ersten Schritt. Funnels werden nach Eintrittsdatum (Kohorte) gezählt.
- Ohne Events für 180 Tage verfällt der gespeicherte Schritt. Nur die **10 jüngsten** `funnelSessionId` pro Nutzer und Funnel werden verfolgt.
- Nach einer Änderung der Schritte den Datumsbereich ab dem Änderungstag wählen.
- **Gegen Exploits absichern:** Client meldet per RemoteEvent, Server prüft die Schrittnummer.
- **Doku-Beispiel „Plant“:** 70 % Abbruch zwischen „In Farm“ (Schritt 1) und „Plant Seed“ (Schritt 2). Gegenmaßnahmen: kontextuelle Hinweise und ein Onboarding, das Pflanzen und erstes Wachstum erzwingt. ✅

**Economy-Events** ✅ ([Economy events](https://create.roblox.com/docs/production/analytics/economy-events))
- `LogEconomyEvent(player, flowType, currencyType, amount, endingBalance, transactionType, itemSku, customFields)`. Betrag immer positiv, Senken werden im Chart negativ gezeigt.
- Standard-transactionTypes: `IAP` (Quelle), `TimedReward` (Quelle), `Onboarding` (Quelle), `Shop` (beides), `Gameplay` (beides), `ContextualPurchase` (Senke).
- Dashboard: Gesamt-Quellen/-Senken nach Kategorie (Netto soll **nahe null** sein), durchschnittliches Wallet (steigt es, besonders bei Zahlern: mehr Senken), Top-Quellen/-Senken, alle Quellen/Senken.

**Custom-Events** ✅ ([Custom events](https://create.roblox.com/docs/production/analytics/custom-events))
- Zähler (ohne Wert) oder Events mit Wert. Aggregation täglich, bis zu 24 h Verzögerung.
- Aggregationen: Count, Unique Users, Average, Sum, Min, Max, Average per User.
- Werte bündeln, um unter dem Rate-Limit zu bleiben („10 Zombies besiegt“ statt 10 einzelne Events).
- Custom Fields statt vieler Eventnamen: `PlantSeed` mit Feld „Plant – Cabbage“ statt `PlantCabbage`.

**Progression-Events** (`LogProgressionEvent`, `LogProgressionCompleteEvent`, `LogProgressionFailEvent`) existieren laut API-Referenz ebenfalls. ✅ ([AnalyticsService](https://create.roblox.com/docs/reference/engine/classes/AnalyticsService))

### 8. Minimaler Tracking-Plan für ein neues Spiel (🧠)
| Event | Typ | Wann | Frage |
|---|---|---|---|
| Onboarding-Schritte 1–8 | Onboarding-Funnel | jede FTUE-Etappe | Wo brechen Neue ab? |
| Erste Belohnung, erstes Upgrade, erste Zone | Onboarding-Funnel | Meilenstein | Wie schnell kommt der Spaß? |
| Level/Zone erreicht | Progression-Funnel oder Custom mit Wert | Level-Up | Wie verteilt sich die Spielerschaft? |
| Währung Quelle/Senke | Economy | jede Transaktion | Inflation? Wallet wächst? |
| Shop geöffnet → Item angesehen → Kaufprompt → Kauf | Shop-Funnel (GUID) | Shop-Session | Wo bricht der Kauf ab? |
| Kernaktion (z. B. `HarvestPlant`) mit Custom Field Typ | Custom | jede n-te Aktion gebündelt | Welche Inhalte werden genutzt? |
| Event-Teilnahme | Custom | Event-Start/-Ziel | Wirkt das Event? |

### 9. Experiments (A/B-Tests) und Configs ✅
Quelle, wenn nicht anders angegeben: [Experiments](https://create.roblox.com/docs/production/experiments)

| Punkt | Regel |
|---|---|
| Typen | **In-game** (testet Config-Werte, bis zu **2 Varianten + Kontrolle**, Rollout in %) und **Matchmaking** (bis zu **3 Varianten**, kein Code, nur **eins gleichzeitig**, 100 % Rollout empfohlen) |
| Dauer | **14–60 Tage** |
| Gemessene Metriken | D1, D7, Playtime, ARPU, ARPPU, Payer Conversion, Session Time (täglich aktualisiert) |
| Early Harm (erste 24 h, alle 5 min) | Schwellen: **Playtime −10 %**, **ARPU −20 %**, **Payer Conversion −20 %**; Harm-Entscheidungen erst ab **10.000** Spielern über Variante + Kontrolle; Benachrichtigung per E-Mail, Creator Hub, optional Webhook |
| Statistische Signifikanz | Konfidenzintervall der Veränderung schneidet 0 % nicht (Doku-Beispiel: ARPU +2,37 %, Intervall 0,55–4,19 %) |
| Sample Ratio Mismatch | Prüfung alle 5 min in den ersten 24 h, dann täglich; bei SRM neu starten |
| Targeting | Land, Tenure, Spender-Stufen usw.; erhöht die MDE (kleinere Stichprobe); Auswertung pro Sitzung |
| Sperren | Config-Key ist während des Tests gesperrt; nur **ein** aktives Experiment pro Key |
| Ende | „Completed“ 14 Tage nach dem Entscheidungsdatum (in-game) bzw. sofort (Matchmaking); „Make decision“ rollt den Gewinner in die Configs aus |
| Code | `ConfigService:GetConfigForPlayerAsync(player)`; Einschreibung erst beim ersten `GetValue()`, also spät aufrufen |
| Mindestgröße | MDE prüfen; unter **1.000 DAU** meist keine brauchbaren Daten |

**Best Practices laut Doku:** Hypothese aufschreiben, volle Dauer laufen lassen (Novelty-Effekt), nur auf Signifikanz reagieren, während des Tests keine Inhaltsänderungen, Trade-offs bewusst entscheiden, Ergebnisse dokumentieren. Im Zweifel: **einfache 50/50-Tests mit einer Variante** bei großem Rollout. ✅

**Configs** ✅ ([Configs](https://create.roblox.com/docs/production/configs))
- Bis zu **1.000 aktive Configs**, **100 Bedingungen pro Spiel**, **20 Bedingungen pro Key**.
- Veröffentlichen „almost instantly“ (etwa 15 s bis 1 min) oder schrittweise über 15 min, ohne Server-Neustart.
- Typische Nutzung laut Onboarding-Doku: XP-Schwellen live glätten, Startwährung nach einem Test global setzen, Flash-Sales auslösen. ✅ ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding); [Balance virtual economies](https://create.roblox.com/docs/production/game-design/balance-virtual-economies))

**Was gut testbar ist (Beispiele aus der Doku):** kurzer Dialog vs. geführter Pfeil im Tutorial, Hinweis nach 5 vs. 10 Sekunden, Startwährung, Matchmaking-Parameter im FTUE, Preispunkte und Rabatte. ✅ ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding); [Onboarding techniques](https://create.roblox.com/docs/production/game-design/onboarding-techniques))

### 10. Segmente im Spiel: `GetPlayerSegmentsAsync` ✅
`AnalyticsService:GetPlayerSegmentsAsync(player)` ist **nur serverseitig**, liefert grobe Buckets und ist ausdrücklich gedacht „to personalize content or gate features“ ([AnalyticsService](https://create.roblox.com/docs/reference/engine/classes/AnalyticsService)):

| Feld | Inhalt |
|---|---|
| `HasData` | ob Daten geladen wurden; sonst alle Felder `Unknown` (kein Fehler) |
| `ActivePayerStatus` | Zahlerstatus im Spiel |
| `WhenUserFirstPlayed` | Bucket des Erstspiels |
| `PlatformSpenderStatus` | plattformweiter Spenderstatus |
| `ExperienceActivationStatus` | neu/aktiv/lapsed/reaktiviert im Spiel (30 Tage) |
| `EngagementLevel` | Spieltage in den letzten 7 Tagen |
| `PlatformActivationStatus` | neu/aktiv/lapsed/reaktiviert auf Roblox (60 Tage) |
| `UserNewReturningStatus` | neu oder schon gespielt |
| `UserAcquisitionSource` | wie der Spieler das Spiel fand |

Ergebnisse werden pro Spieler für die Server-Session gecacht. Die Doku nennt als Beispiele: günstige Einstiegsangebote für Nichtzahler, Bundles für Käufer, zusätzliche Tutorials für Spieler in ihren ersten 30 Tagen. ✅ ([Analytics](https://create.roblox.com/docs/production/analytics))
🧠 Vorsicht: Personalisierte Preise oder Angebote müssen die Regeln zu Paid Random Items und ehrlichen Rabatten einhalten (siehe `07-monetarisierung/monetarisierung.md`). Immer einen Fallback für `HasData = false` bauen.

### 11. Wochenroutine (🧠)
1. **Montag:** Overview öffnen. Insights und Scorecards lesen. Welche KPI liegt unter dem 50. Perzentil?
2. Retention-Kohorten der letzten Woche gegen die Vorwoche (Period-over-Period, 28-Tage-Offset).
3. Acquisition: Home-Kohorte getrennt prüfen (PTR, D7, 30D-Umsatz).
4. Funnel: größten Abbruchschritt suchen. Eine Hypothese pro Woche.
5. Economy: Netto-Fluss und Wallet je Segment. Wächst das Wallet der Zahler?
6. Nach jedem Update: Crash-Rate, FPS, First Session Retention (5-min-Wert) und Fehlerbericht.
7. Ab 1.000 DAU: höchstens ein Experiment pro System gleichzeitig, mit schriftlicher Hypothese.

## Beispiele aus echten Spielen
- **Adopt Me! (Uplift Games):** nutzt Analytics und Experiments. Bei einem Sommer-Event-Feature „the crash rate and frame rate clued us in that something was going wrong“ (UpliftBradB). ✅/🟡 Studio-Aussage im Roblox-Newsroom, Volltext nicht geprüft ([Roblox Newsroom, Aug. 2026](https://about.roblox.com/newsroom/2026/08/optimize-testing-live-updates-roblox-analytics-experimentation-platform))
- **Doku-Referenzspiel „Plant“:** 70-%-Abbruch im Onboarding-Funnel, behoben mit Pfeil-Prompts über den Töpfen. ✅ ([Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events))
- **Dubit:** misst D1, D7 und die **Form der Retention-Kurve** gegen interne Daten. 🟡 Studio-Marketing ([Dubit](https://dubit.io/blog/how-we-build-hit-roblox-games))

## Do / Don't
| Do | Don't |
|---|---|
| Gegen das eigene Benchmark-Band arbeiten | Mobile-Zielwerte (40/20/10) übernehmen |
| Home-Kohorte getrennt auswerten | Nur Gesamt-Retention lesen |
| Max. 5 Währungen tracken, Rest über Custom Fields | Für jede Variante eine neue Währung oder einen neuen Eventnamen |
| Events nach Erfolg loggen, Schritte serverseitig prüfen | Client-Werte ungeprüft loggen |
| Experiments volle Dauer laufen lassen | Nach drei Tagen „Gewinner“ ausrollen |
| Unter 1.000 DAU: Funnels und Playtests | A/B-Tests ohne ausreichende MDE |
| Nach jedem Update Crash-Rate und FPS prüfen | Updates ohne Vorher/Nachher-Vergleich |

## Checkliste
- [ ] Analytics aktiviert (E-Mail, 2FA, AGB), Schwelle >10 DAU / 10 h an 7 Tagen erreicht
- [ ] Onboarding-Funnel mit 5–10 Schritten, Schritt 1 in `PlayerAdded`
- [ ] Shop-Funnel mit GUID-`funnelSessionId`
- [ ] Economy-Events für alle Quellen und Senken, max. 5 Währungen
- [ ] Custom Events für Kernaktion mit Custom Field statt vieler Namen
- [ ] Rate-Limit (120 + 20 × CCU/min) eingeplant, Events gebündelt
- [ ] Scorecards ab 100 DAU wöchentlich gelesen
- [ ] Retention nach Quelle (Home vs. Ads vs. Friends) verglichen
- [ ] Experiment-Hypothese schriftlich, MDE geprüft, keine parallelen Änderungen
- [ ] `GetPlayerSegmentsAsync` mit Fallback für `HasData = false`

## Offene Fragen / Recherche-Bedarf
- Offizielle Genre-D1/D7/D30-Werte sind nur im Dashboard sichtbar, nicht öffentlich.
- Klärung, ob das Währungslimit 5 oder 10 beträgt (Doku widerspricht sich).
- Volltext des Newsroom-Artikels zu Uplift/Experiments (Aug. 2026) nicht geprüft.
- GameAnalytics deckt nur Spiele ≥ 1 Mio. MAU ab. Keine verlässlichen Benchmarks für kleine Spiele.

## Quellen
- [Creator Docs: Analytics (Übersicht, 3-Schritte-Plan)](https://create.roblox.com/docs/production/analytics) – Stand 2026-10-24, ✅
- [Creator Docs: Analytics dashboard (Benchmarks, Filter)](https://create.roblox.com/docs/production/analytics/analytics-dashboard) – ✅
- [Creator Docs: Retention](https://create.roblox.com/docs/production/analytics/retention) – ✅
- [Creator Docs: Engagement](https://create.roblox.com/docs/production/analytics/engagement) – ✅
- [Creator Docs: Acquisition](https://create.roblox.com/docs/production/analytics/acquisition) – ✅
- [Creator Docs: Monetization analytics](https://create.roblox.com/docs/production/analytics/monetization) – ✅
- [Creator Docs: Event types (Limits)](https://create.roblox.com/docs/production/analytics/event-types) – ✅
- [Creator Docs: Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events) – ✅
- [Creator Docs: Economy events](https://create.roblox.com/docs/production/analytics/economy-events) – ✅
- [Creator Docs: Custom events](https://create.roblox.com/docs/production/analytics/custom-events) – ✅
- [Creator Docs: Experiments](https://create.roblox.com/docs/production/experiments) – ✅
- [Creator Docs: Configs](https://create.roblox.com/docs/production/configs) – ✅
- [Engine-Referenz: AnalyticsService](https://create.roblox.com/docs/reference/engine/classes/AnalyticsService) – ✅
- [Creator Docs: Discovery](https://create.roblox.com/docs/discovery) und [Discovery FAQ](https://create.roblox.com/docs/discovery-faq) – ✅
- [DevForum: Retention by acquisition source](https://devforum.roblox.com/t/analytics-view-retention-by-acquisition-source-and-select-your-benchmark-set/4010157) – 2025, ✅
- [GameAnalytics 2026 Roblox Benchmark Report](https://www.gameanalytics.com/reports/2026-roblox-report) – 2026, 🟡
- [GameDevReports: Zusammenfassung GameAnalytics 2026](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox) – 2026, 🟡
- [GameAnalytics 2025 Roblox Report](https://www.gameanalytics.com/reports/2025-roblox-report) – 2025, 🟡
- [Roblox Newsroom: Analytics & Experimentation (Uplift)](https://about.roblox.com/newsroom/2026/08/optimize-testing-live-updates-roblox-analytics-experimentation-platform) – Aug. 2026, ✅ (nur Ausschnitt geprüft)
- [rowatcher: Retention Benchmarks by Genre](https://rowatcher.com/news/retention-benchmarks-by-roblox-genre-what-good-actually-looks-like) – 🟠
