# Discovery-Algorithmus (Empfehlungen auf Roblox)

> Stand: 2026-10-24 · Nächste Prüfung: monatlich (Roblox testet laufend weiter) · Gesamt-Vertrauen: ✅ für Signale, Zeitfenster und Regeln (offizielle Creator Docs, Stand 24.10.2026), 🟡 für Geschäftsauswirkungen, 🟠 für Drittquellen zu Suche und Charts

## Kurzfassung
Die Home-Empfehlung „Recommended For You“ (RFY) arbeitet in **zwei Stufen**: Erst wählt eine **Retrieval-Stufe** Kandidaten aus allen Quellen (auch Werbung, Today's Picks, Suche, Charts, Freunde), dann entscheidet eine **Ranking-Stufe** über die Reichweite, und zwar **ausschließlich** anhand von Nutzern, die organisch über RFY kamen ✅. **Am wichtigsten** sind Play-Through-Rate (PTR), First-Play-Bounce-Rate (negativ, gemessen unter 60 s und 61–180 s), Spieltage pro Nutzer und Spielzeit pro Nutzer (gedeckelt auf 60 Min./Tag). **Wichtig** sind gezieltes Co-Play, qualifizierte Sitzungen, Kauftage und ausgegebene Robux, jeweils für Tag 1, Tag 2–7 und Tag 8–28 ✅. Seit 15.06.2026 reicht das Fenster bis Tag 28 (vorher 7), QPTR wurde durch PTR und Bounce ersetzt ✅/🟡. Neue Spiele müssen **nicht** 28 Tage warten; Werbe-Nutzer zählen nicht im Ranking und gelten danach als „already acquired“ ✅. Today's Picks ist **redaktionell**, nicht algorithmisch ✅.

## Warum das wichtig ist
- Für die meisten Spiele ist Home die größte Traffic-Quelle; laut Gamefam ist Akquise „essentially fully dependent on the algorithm“ 🟡 ([GamesBeat](https://gamesbeat.com/gamefam-sees-rapid-growth-in-making-games-for-roblox/)).
- Roblox hat bewusst kurzfristige Buchungen geopfert, um Spiele mit Langzeitbindung zu bevorzugen; das wurde als Mitursache für das Q2-2026-Wachstum von nur +8 % und die negative Q3-Prognose genannt ✅ ([Q2-2026-Brief](https://s27.q4cdn.com/984876518/files/doc_financials/2026/q2/Roblox-Q2-2026-Earnings-Shareholder-Letter.pdf)). Die Richtung wird also nicht schnell zurückgedreht.
- Die ersten drei Minuten einer Sitzung und die Rückkehr an möglichst vielen Tagen sind jetzt direkt Ranking-relevant, nicht nur „gute Praxis“.

## Referenzbilder
Offizielle Bilder aus der Roblox Creator Documentation (Übersicht: `assets/bilder/offiziell/README.md`).

![Empfehlungssystem: Candidate Generators, Ranking, Home](../assets/bilder/offiziell/discovery/empfehlung-retrieval-ranking-diagramm.png)
*Zweistufiges System: Alle Spiele → Candidate Generators (Ads, Today's Picks, Search, Charts, Friends …) → Ranking → Home „Recommended For You“. Werbung bringt dich in die Kandidatenmenge, das Ranking entscheiden RFY-Nutzer. Quelle: Roblox Creator Docs, CC BY 4.0.*

![Dashboard Home recommendation signals mit PTR und First-Play-Bounce](../assets/bilder/offiziell/discovery/home-empfehlung-signale.png)
*Dashboard „Home recommendation signals“: PTR und First-Play-Bounce-Rate mit Benchmark. Diese zwei Werte zuerst prüfen. Quelle: Roblox Creator Docs, CC BY 4.0.*

![New users funnel nach Akquisequelle](../assets/bilder/offiziell/analytics/akquise-neue-nutzer-funnel.png)
*„New users funnel“ nach Quelle (Home Recommendation, Search, Friends, Sponsored Ads …) mit Conversion, D7, Playtime, Revenue. Quellen nach Qualität vergleichen. Quelle: Roblox Creator Docs, CC BY 4.0.*

## Details

### 1. Das Zwei-Stufen-Modell ✅
Quelle: [Discovery](https://create.roblox.com/docs/discovery); [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)

| Stufe | Was passiert | Welche Nutzer zählen | Konsequenz |
|---|---|---|---|
| **1. Retrieval** | „selects a subset of games… based on key signals like engagement, retention, and monetization.“ Braucht nur „a very low minimum number of plays from any source“; „The algorithm tests your game daily.“ | Nutzer aus **allen** Quellen (Werbung, Freunde, Suche, Social Media …) | Werbung und Freunde helfen, Kandidat zu werden |
| **2. Ranking** | „How far your game goes… depends entirely on the engagement and retention of users who come to your game through Recommended for You.“ Pro Nutzer grob auf ca. 100 Spiele auf Home eingeengt | **Nur** organisch über RFY gewonnene Nutzer. Nutzer aus „ads, curation, friends, search, social media, or any other source“ zählen nicht | Reichweite lässt sich nicht kaufen; nur echtes Verhalten der RFY-Nutzer zählt |

- Signale sind **Durchschnitte pro Nutzer**, keine Summen. Das soll sicherstellen, dass „smaller experiences with highly engaged users are not disadvantaged“ ✅ ([DevForum: Improved RFY 2025](https://devforum.roblox.com/t/boost-your-discovery-with-the-improved-recommended-for-you-algorithm-and-analytics-for-creators/3587441)).
- „There is no single signal that determines ranking.“ Gewichte veröffentlicht Roblox nicht, nur „each carrying a different amount of influence“ ✅ ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)).

### 2. Die Signale mit Zeitfenstern ✅
Quelle: [Discovery](https://create.roblox.com/docs/discovery); [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)

| Stufe | Signal | Definition | Zeitfenster | Richtung |
|---|---|---|---|---|
| **Most important** | Play-Through-Rate (PTR) | „The rate at which users play your game after seeing it in the Recommended for You sort“ | N/A (erste Sitzung) | positiv |
| **Most important** | First-Play-Bounce-Rate | Anteil, der die erste Sitzung schnell verlässt; „This is a negative signal“ | < 60 s (Ø) und 61–180 s (Ø) | **negativ** |
| **Most important** | Spieltage pro Nutzer | An wie vielen Tagen gespielt wurde; Tag 2–7: „Out of the 6 days in the 2–7 window, how many days on average“ | Tag 1, Tag 2–7, Tag 8–28 | positiv |
| **Most important** | Spielzeit pro Nutzer | Minuten im Spiel; **max. 60 Minuten pro Nutzer, Spiel und Tag** | Tag 1, Tag 2–7, Tag 8–28 | positiv |
| Important | Gezielte Co-Play-Tage pro Nutzer | Tage mit gezieltem Zusammenspiel „including co-play days through join, invites, or private servers“ | Tag 1, 2–7, 8–28 | positiv |
| Important | Qualifizierte Sitzungen pro Nutzer | Sitzungen, die Fehlklicks und schnelle Abbrüche herausfiltern | Tag 1, 2–7, 8–28 | positiv |
| Important | Kauftage pro Nutzer | Tage mit Ausgaben | Tag 1, 2–7, 8–28 | positiv |
| Important | Robux pro Nutzer | Ausgegebene Robux | Tag 1, 2–7, 8–28 | positiv |

- **PTR und Bounce messen nur neue Nutzer aus Home-Empfehlungen in ihrer ersten Sitzung.** Die Tag-2–7- und Tag-8–28-Werte verfolgen **dieselben** RFY-Nutzer weiter, auch wenn sie über „Continue“ oder andere Flächen zurückkommen ✅ ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)).
- Die drei Zeitsegmente werden „both separately and combined together to decide impression volume“ betrachtet ✅ ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)).
- Die Doku nennt weder das Datum 15.06.2026 noch die Formulierung „28-Tage-Fenster“; sie zeigt nur den aktuellen Zustand ✅ (verifiziert gegen Creator-Docs-Quelltext).

### 3. Kaltstart: Neue Spiele müssen nicht 28 Tage warten ✅
- „New games do not have to wait 28 days… Playthrough rate and bounce rate capture the first session; Then Day 1 signals…; Then Day 2–7; Then Day 8–28. Early signals kick in immediately.“ ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq))
- „There is no penalty for games that did not perform well at first. The signals use a moving window.“ ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq))
- **Korrektur:** Eine frühere Notiz folgerte, neue Spiele hätten strukturell ca. 4 Wochen Verzögerung. Das widerspricht der Doku.
- Entwickler berichten trotzdem von Impression-Einbrüchen (anekdotisch: von 2.000–3.000/Stunde auf ca. 200) und nennen es ein „Henne-Ei“-Problem 🟠 ([DevForum 4779042](https://devforum.roblox.com/t/boost-your-discovery-by-building-games-people-want-to-play/4779042); [DevForum 4568033](https://devforum.roblox.com/t/testing-more-recommended-for-you-algorithm-signals/4568033?page=4)).

### 4. Retention vs. Monetarisierung ✅
- „Games that are strong in only one area… will continue to receive Home recommendation impressions. However, games that perform well in both… might receive broader distribution.“
- „If retention is low, focus on core gameplay first. Once retention is strong, improving monetization can help you increase your Home impressions.“
- Quelle: [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)
- 🧠 Monetarisierung zählt pro Nutzer und über Kauf**tage**. Wiederkehrende kleine Käufe über viele Tage helfen vermutlich mehr als ein einmaliger Großkauf (Roblox nennt keine Gewichte).

### 5. Was die Reichweite verändert und begrenzt ✅
**Vier Faktoren für schwankende Impressions** ([Discovery](https://create.roblox.com/docs/discovery)):
1. Deine eigenen Änderungen.
2. Algorithmus-Änderungen von Roblox.
3. Home-Traffic und Saisonalität: „Weekly seasonality which usually peaks on a Saturday“.
4. Konkurrenten, die sich stärker verbessern als du.

**Probleme, die die Sichtbarkeit begrenzen** ([Discovery](https://create.roblox.com/docs/discovery); [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)):
- „Leading with giveaways“ (mit Gratis-Versprechen werben).
- „Mismatched metadata and content“ (Titel/Thumbnail versprechen etwas anderes als das Spiel).
- „Non-unique games“ (Kopien). Originalität wird dem Spiel gutgeschrieben, „the game that first added the unique metadata and/or placefile“, nicht dem zuerst erstellten.
- Ein täglich aktualisiertes Banner im Creator Dashboard zeigt den Status.

**Weitere harte Regeln** ✅:
- „A custom thumbnail is required for your game to receive impressions from homepage recommendations. If your game only has a default thumbnail, it is not eligible.“ ([Discovery](https://create.roblox.com/docs/discovery))
- Opt-out: Schalter „Exclude from recommendations“ unter Audience > Advanced Settings ([Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places)).
- „Benchmarks and benchmark games do not impact the Recommended for You algorithm in any way.“ ([Discovery](https://create.roblox.com/docs/discovery))
- „Genre and gameplay type are not explicit ranking factors.“ Endliche, storygetriebene Spiele werden für niedrigere Tag-8–28-Retention nicht bestraft ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)).
- Bestehende Thumbnails/Icons wiederzuverwenden „shouldn't negatively affect discoverability“ ([Discovery FAQ](https://create.roblox.com/docs/discovery-faq)).
- Unter 18-Jährige sehen keine Such- und Empfehlungsergebnisse für Spiele mit Label „Restricted“ ✅ ([DevForum Restricted](https://devforum.roblox.com/t/updating-age-requirements-for-experiences-with-%E2%80%98restricted%E2%80%99-content-maturity-label/3905863)). Neue Spiele erscheinen zunächst nur für altersgeprüfte 16+ (siehe `plattform-regeln-2026.md`).

### 6. Werbung und RFY ✅
- „Engagement, retention, and monetization from users acquired through ads are excluded from RFY ranking signals.“
- „When a user is acquired through an ad, Roblox considers that user already acquired. This means the user acquired through an ad will generally not subsequently see your game in RFY… Ads do not penalize or downrank your game.“
- Das Kampagnenziel **Plays** hilft, für RFY „considered“ zu werden (Retrieval-Stufe).
- Quellen: [Discovery FAQ](https://create.roblox.com/docs/discovery-faq); [Ads Manager](https://create.roblox.com/docs/production/promotion/ads-manager)
- 🧠 Folge: Ein großer Werbe-Burst kann potenzielle organische RFY-Nutzer „verbrauchen“. Gesamtakquise steigt, RFY-Impressionen können trotzdem sinken. Details und Kampagnenplanung: `ads-und-akquise.md`.

### 7. Chronik der RFY-Änderungen

| Zeitpunkt | Änderung | Quelle / Vertrauen |
|---|---|---|
| Q4 2024 | Roblox tunt die Zielfunktion „towards long-term retention“ | [Q4-2024-Brief (SEC)](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000021/ex992-q42024shareholderl.htm) ✅ |
| Ende 2024 | Tests von RFY-Verbesserungen | [DevForum 3275201](https://devforum.roblox.com/t/testing-improvements-to-the-%E2%80%9Crecommended-for-you%E2%80%9D-algorithms/3275201) ✅ |
| Januar 2025 | Dynamisches Ranking für „People You May Know“ und „Continue“ | [DevForum: 2025 Discovery Roadmap](https://devforum.roblox.com/t/roblox%E2%80%99s-2025-discovery-roadmap-and-ways-to-reach-and-engage-your-audience/3557533) ✅ |
| März 2025 | Roadmap: personalisiertes Home, dynamische Platzierung von Today's Picks, Sort „Recommended Paid Access Experiences“, Friend Referral System | [DevForum 3557533](https://devforum.roblox.com/t/roblox%E2%80%99s-2025-discovery-roadmap-and-ways-to-reach-and-engage-your-audience/3557533); [Tubefilter](https://www.tubefilter.com/2025/03/20/roblox-discovery-roadmap-2025/) ✅/🟡 |
| 2025 | RFY rankt nach Engagement + Monetarisierung (QPTR, D1/D7, Playtime, Payer-Conversion); per-Nutzer-Durchschnitte; Signal „intentional co-play“ eingeführt | [DevForum 3587441](https://devforum.roblox.com/t/boost-your-discovery-with-the-improved-recommended-for-you-algorithm-and-analytics-for-creators/3587441); [DevForum 4067565](https://devforum.roblox.com/t/tests-continuing-to-improve-the-%E2%80%98recommended-for-you%E2%80%99-algorithm/4067565) ✅ |
| Q2 2025 | Multi-Task-Learning auf „high value actions… that lead to retention, engagement, and monetization“ | [Q2-2025-Brief (SEC)](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000261/q225shletterex992.htm) ✅ |
| Ende 2025 | Retention nach Akquisequelle im Analytics-Dashboard; Wahl zwischen Similar- und Genre-Benchmark | [DevForum 4010157](https://devforum.roblox.com/t/analytics-view-retention-by-acquisition-source-and-select-your-benchmark-set/4010157) ✅ |
| Ende 2025 – Frühjahr 2026 | „Testing More RFY Algorithm Signals“; öffentliche Tests ab ca. April 2026 | [DevForum 4568033](https://devforum.roblox.com/t/testing-more-recommended-for-you-algorithm-signals/4568033?page=4) ✅; [Lensblox](https://lensblox.com/blog/roblox-algorithm-change-2026-explained/) 🟠 |
| **15.06.2026** | 7-Tage- → 28-Tage-Sicht; Signale getrennt für Tag 1 / 2–7 / 8–28; **QPTR entfernt, PTR und First-Play-Bounce neu**; Signalliste mit relativer Wichtigkeit veröffentlicht | [Roblox Newsroom](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox) ✅; [DevForum 4684575](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575) ✅ |
| 30.07.2026 | Q2-Zahlen: Bookings +8 %, RFY-Änderung als Mitursache, stärkerer Effekt bei unter 13-Jährigen in USA/Kanada; Q3-Prognose −14 bis −18 % | [Q2-2026-8-K](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm) ✅; [Investing.com Transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-roblox-q2-2026-beats-eps-but-shares-sink-on-bookings-93CH-4826338) 🟡 |
| August 2026 | Post „Boost Your Discovery by Building Games People Want to Play“ (Chief Growth Officer): Benchmarks beeinflussen den Algorithmus nicht; weitere Tests, die „long-term player value“ besser erkennen; „The most important thing is to build games people want to play, and keep playing.“ (Datum 6. oder 20.08., Quellen widersprüchlich) | [DevForum 4779042](https://devforum.roblox.com/t/boost-your-discovery-by-building-games-people-want-to-play/4779042) ✅; [ComicBook.com](https://comicbook.com/gaming/news/new-roblox-update-finally-targets-spam-slop-experiences-build-games-people-want/) 🟡 |
| RDC 2026 (Sep/Okt) | Roblox will starke 18+-Spiele über Algorithmus und eigene bezahlte UA-Kampagnen sichtbarer machen | [MaxPowerGaming](https://www.maxpowergaming.co/post/rdc-2026-roblox-is-building-for-professionals-now); [games.gg](https://games.gg/news/roblox-algorithm-adult-games-retention/) 🟡 |
| Herbst 2026 | Roadmap: „better discovery recommendations“ und verbessertes „Continue Playing“ ausgeliefert; geplant: dynamische Filter, Pass-Testversionen pro Sitzung, „deceptive game copy takedown“ | [Creator Roadmap Fall Update](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208) ✅ |

- Vlad Loktev (Chief Creator Ecosystem Officer): Ziel sei, „level the playing field for ambitious, high-quality games that keep players coming back for years“ 🟡 ([PCGamesN](https://www.pcgamesn.com/roblox/adult-games-long-term-retention)).
- Unbestätigt: Ein Blog behauptet, die Änderung habe „$9B“ Börsenwert gekostet 🟠 ([Lensblox](https://lensblox.com/blog/roblox-algorithm-change-2026-explained/)).

### 8. Andere Discovery-Flächen

| Fläche | Wie sie funktioniert | Vertrauen |
|---|---|---|
| **Today's Picks** (Home) | „a curation of the best games on a daily basis.“ Nominierung per Umfrage; „Our editorial team reviews nominations on an ongoing basis… only those selected… will be notified.“ Neu bewerben „each time your game has a notable update“. Status: offen | ✅ [Today's Picks](https://create.roblox.com/docs/creator-programs/todays-picks-home) |
| **Standout Games** (Home) | Handkuratiert für „novel games“, Nominierung per Umfrage; RPG, Strategie, Puzzle, Shooter unterversorgt; Kopien/Reskins „a hard sell“ | ✅ [Standout Games](https://create.roblox.com/docs/creator-programs/standout-games) |
| **Continue / Continue Playing** | Rückkehrer-Traffic; dynamisch gerankt seit Januar 2025, im Herbst 2026 verbessert | ✅ |
| **Charts** (roblox.com/charts) | Top Trending, Up-and-Coming, Top Playing Now, Top Revisited u. a. (Fan-Wiki: ca. 29 Sorts); Ranking-Logik nicht dokumentiert; Doku sagt nur „top and trending sorts have been updated“ | ✅ [Roblox Charts](https://www.roblox.com/charts) / 🟠 [Fandom](https://roblox.fandom.com/wiki/Charts) |
| **Trending Events** | Event gestartet in den letzten 7 Tagen, mind. 1.000 RSVPs; gerankt nach DAU des Spiels, filterbar nach Ort und Plattform | ✅ [Experience events](https://create.roblox.com/docs/production/promotion/experience-events) |
| **Suche** | „historically… focused on relevance based on exact search queries and limited metadata such as titles“; jetzt **semantische Suche** in allen offiziellen Sprachen (z. B. „food games“). Ranking-Faktoren nicht dokumentiert | ✅ [Discovery](https://create.roblox.com/docs/discovery) |
| **Suchanzeigen** | Bis zu 10 Keywords pro Ad Set; nur bei exakter Keyword-Übereinstimmung, oben oder direkt nach einem Exakt-Namen-Treffer | ✅ [Search ads](https://create.roblox.com/docs/production/promotion/search-ads) |
| **Passes außerhalb des Spiels** | „Listed“-Passes erscheinen auf Home, in der Suche und nach dem Robux-Kauf; Developer Products nur bei korrektem `ProcessReceipt` | ✅ [Passes](https://create.roblox.com/docs/production/monetization/passes); [Developer products](https://create.roblox.com/docs/production/monetization/developer-products) |

- **Korrektur:** Die Vorversion bzw. eine Notiz beschrieb Today's Picks als engagementgetrieben. Offiziell ist es redaktionell ✅. Ältere DevForum-Posts sprachen von engagementabhängiger *Platzierung* der Today's-Picks-Reihe auf Home 🟡 ([DevForum 3432124](https://devforum.roblox.com/t/building-the-future-of-roblox-home-and-search-introducing-personalized-discovery/3432124)); die *Auswahl* ist redaktionell.
- Suche laut Drittquellen: Keyword-Match in Titel/Beschreibung/Genre plus Engagement und Aktualität 🟠 ([Lensblox SEO](https://lensblox.com/blog/roblox-seo-guide/); [rolearn](https://rolearn.dev/insights/roblox-game-discovery-algorithm-2026/)).
- 🧠 Charts scheinen kurzfristige Wachstumsgeschwindigkeit zu belohnen, RFY dagegen 28-Tage-Retention. Ein viraler Spike kann also Charts gewinnen, ohne RFY zu gewinnen (siehe Steal An Egg).

### 9. Analytics-Werkzeuge für Discovery ✅
Ausführlich: `03-mechaniken-retention/analytics-und-experimente.md`; Thumbnail-/Icon-Gestaltung: `04-ui-ux/thumbnails-und-icons.md`; Werbung: `ads-und-akquise.md`.

- **Home recommendation signals** (PTR, Bounce mit Benchmark) im Creator Hub ([Discovery](https://create.roblox.com/docs/discovery)).
- **Retention nach Akquisequelle** auf Overview- und Retention-Seite ([DevForum 4010157](https://devforum.roblox.com/t/analytics-view-retention-by-acquisition-source-and-select-your-benchmark-set/4010157)).
- **Benchmarks:** 50.–90. Perzentil ähnlicher Spiele, ab 100 DAU; Beispiel D1-Band **12,11–18,73 %** (Korrektur: nicht 12,4–24,1 %) ([Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard)).
- **Funnels** (bis 10, je 100 Schritte) für FTUE-Abbrüche, **Experiments** (14–60 Tage, unter 1.000 DAU wenig aussagekräftig) ([Event types](https://create.roblox.com/docs/production/analytics/event-types); [Experiments](https://create.roblox.com/docs/production/experiments)).
- Zum Einordnen: GameAnalytics-Median über 500+ große Spiele D1 10,3 %, D7 1,6 %, D30 0,5 %; Top 1 % 22,2 / 9,1 / 4,7 % 🟡 ([GameAnalytics 2026](https://www.gameanalytics.com/reports/2026-roblox-report)).

### 10. Korrekturen gegenüber der Vorversion

| Früher hier | Jetzt verifiziert |
|---|---|
| „Roblox will Signale und Gewichtung teilen“ | Signale und **Stufen** veröffentlicht, **keine numerischen Gewichte** ✅ |
| „Freunde mitbringen“ als Signal | Konkret: „intentional co-play days“ (Join, Einladung, private Server), Stufe „Important“ ✅ |
| Zweistufig „Explore, dann ausweiten“ | Offiziell: Retrieval (alle Quellen) → Ranking (nur RFY-Nutzer) ✅ |
| Nicht erwähnt | QPTR entfernt, PTR + First-Play-Bounce (< 60 s, 61–180 s) neu ✅/🟡 |
| Nicht erwähnt | Spielzeit gedeckelt auf 60 Min./Nutzer/Spiel/Tag ✅ |
| Nicht erwähnt | Werbe-Nutzer aus Ranking ausgeschlossen, danach „already acquired“ ✅ |
| Nicht erwähnt | Eigenes Thumbnail Pflicht für Home-Impressionen ✅ |
| Today's Picks implizit algorithmisch | Redaktionell mit Nominierung ✅ |

## Beispiele aus echten Spielen
- **Steal An Egg** erreichte seinen Peak (19.09.2026) nach der RFY-Umstellung, fiel aber in 5 Wochen um ca. 90 % 🟠/🧠: Viralität kann Charts und Social Media füllen, hält aber ohne Tag-8–28-Gründe nicht.
- **Murder Mystery 2** stieg nach einem Event auf einen Allzeit-Rekord 🟠: Ein Spiel mit vielen Spieltagen pro Nutzer (Tausch, Rundenformat) profitiert vom neuen Fenster 🧠.
- **Uplift Games (Adopt Me!)** nutzt Analytics und Experiments; Crash-Rate und FPS zeigten einen defekten Sommer-Event-Teil 🟡 ([Roblox Newsroom Aug 2026](https://about.roblox.com/newsroom/2026/08/optimize-testing-live-updates-roblox-analytics-experimentation-platform)).

## Was heißt das für dich (🧠, abgeleitet aus den offiziellen Signalen)
1. **Thumbnail + Icon = PTR.** Eigenes Thumbnail ist Pflicht; 2–5 aktive Thumbnails für Personalisierung (siehe `ads-und-akquise.md`). Ehrlich bleiben: Clickbait erhöht PTR, aber auch Bounce.
2. **Die ersten 3 Minuten bauen.** Bounce wird unter 60 s und 61–180 s gemessen. Spawn mit sofortiger Handlung, erste Belohnung in 1–3 Minuten, keine Ladewand, keine Textwand.
3. **An möglichst vielen der 6 Tage im Fenster 2–7 zurückholen.** Tägliche Timer, Tagesaufgaben, Restock-Zeiten, Events. Ein langer Tag zählt maximal 60 Minuten.
4. **Woche 2–4 planen** (Tag 8–28): Sammlungen, Saison, Rebirth, Gilden, Kompetition, Tausch.
5. **Co-Play aktiv bauen:** `SocialService:PromptGameInvite`, Party-Join, bezahlbare private Server, Koop-Boni. Lobbys mit `TextChatService:GetChatGroupsAsync` so bilden, dass Gruppen miteinander reden dürfen ✅ ([TextChatService](https://create.roblox.com/docs/reference/engine/classes/TextChatService)).
6. **Monetarisierung erst, wenn Retention steht**, dann als wiederkehrende kleine Käufe (Kauftage).
7. **Keine Giveaway-Werbung, keine irreführenden Metadaten, keine Kopien.** Alle drei drosseln die Reichweite offiziell.
8. **Werbung gezielt einsetzen:** um Kandidat zu werden und um zu testen, nicht als Dauerersatz für organisches RFY.
9. **Bei Updates Today's Picks nominieren** und bei Neuheit Standout Games.
10. **Samstag nutzen:** Wochenhoch der Home-Traffic.

## Do / Don't
| Do | Don't |
|---|---|
| PTR und Bounce wöchentlich gegen Benchmark prüfen | Nur auf CCU schauen |
| Erste Belohnung in 1–3 Minuten | Lange Intros, Ladebildschirme, Texttutorials |
| Tägliche Rückkehrgründe für 6 Tage | Alles in eine 3-Stunden-Sitzung packen (Deckel 60 Min.) |
| Co-Play über Einladungen und Partys fördern | Auf freien Chat als Social-Motor setzen |
| Thumbnail ehrlich zum Spiel | Clickbait, das Bounce erhöht |
| Today's Picks bei jedem großen Update nominieren | Giveaway-Versprechen im Titel |
| Werbung für Retrieval und Tests | Werbung als Ersatz für Retention |

## Checkliste vor Launch und nach jedem großen Update
- [ ] Eigenes Thumbnail (16:9, 1920×1080), 2–5 aktiv
- [ ] Icon 512×512, ein klares Motiv
- [ ] Titel, Beschreibung und Thumbnail passen zum tatsächlichen Spiel (kein „Mismatched metadata“)
- [ ] Erste sinnvolle Aktion < 10 s, erste Belohnung < 3 Min.
- [ ] Onboarding-Funnel mit `LogOnboardingFunnelStepEvent` instrumentiert
- [ ] Tagesgründe für Rückkehr (Tag 2–7) und Wochenziele (Tag 8–28) vorhanden
- [ ] Einladungen/Party-Join eingebaut, private Server bezahlbar
- [ ] Keine Giveaway-Versprechen in Metadaten
- [ ] „Exclude from recommendations“ ist **aus**
- [ ] Today's Picks / Standout Games nominiert (wenn passend)
- [ ] Home-Recommendation-Signale nach 1, 7 und 28 Tagen geprüft

## Offene Fragen / Recherche-Bedarf
- Numerische Gewichte der Signale und der drei Zeitsegmente: nicht veröffentlicht.
- Ranking-Logik von Charts und Suche: nicht dokumentiert.
- Name des Autors des August-2026-Posts (Sekundärquellen nennen „Ciancutti“) nicht verifiziert.
- Weitere Tests zu „long-term player value“ laufen; Ergebnis offen.

## Quellen
- [Creator Docs: Discovery](https://create.roblox.com/docs/discovery) – Stand 24.10.2026, ✅
- [Creator Docs: Discovery FAQ](https://create.roblox.com/docs/discovery-faq) – Stand 24.10.2026, ✅
- [Roblox Newsroom: Optimizing Discovery](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox) – Juni 2026, ✅
- [DevForum: RFY Algorithm Improvements (4684575)](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575) – Juni 2026, ✅
- [DevForum: Boost Your Discovery by Building Games People Want to Play (4779042)](https://devforum.roblox.com/t/boost-your-discovery-by-building-games-people-want-to-play/4779042) – Aug 2026, ✅
- [DevForum: Improved RFY and Analytics (3587441)](https://devforum.roblox.com/t/boost-your-discovery-with-the-improved-recommended-for-you-algorithm-and-analytics-for-creators/3587441) – 2025, ✅
- [DevForum: 2025 Discovery Roadmap](https://devforum.roblox.com/t/roblox%E2%80%99s-2025-discovery-roadmap-and-ways-to-reach-and-engage-your-audience/3557533) – Mär 2025, ✅
- [DevForum: Creator Roadmap 2026 Fall Update](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208) – Herbst 2026, ✅
- [Creator Docs: Today's Picks](https://create.roblox.com/docs/creator-programs/todays-picks-home) – ✅
- [Creator Docs: Standout Games](https://create.roblox.com/docs/creator-programs/standout-games) – ✅
- [Creator Docs: Search ads](https://create.roblox.com/docs/production/promotion/search-ads) – ✅
- [Creator Docs: Ads Manager](https://create.roblox.com/docs/production/promotion/ads-manager) – ✅
- [Creator Docs: Experience events](https://create.roblox.com/docs/production/promotion/experience-events) – ✅
- [Creator Docs: Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard) – ✅
- [Q2-2026-Aktionärsbrief](https://s27.q4cdn.com/984876518/files/doc_financials/2026/q2/Roblox-Q2-2026-Earnings-Shareholder-Letter.pdf) – ✅
- [PCGamesN: Adult games, long-term retention](https://www.pcgamesn.com/roblox/adult-games-long-term-retention) – 2026, 🟡
- [MaxPowerGaming: RDC 2026](https://www.maxpowergaming.co/post/rdc-2026-roblox-is-building-for-professionals-now) – 2026, 🟡
- [GameAnalytics: 2026 Roblox Report](https://www.gameanalytics.com/reports/2026-roblox-report) – 2026, 🟡
- [Lensblox: Algorithm Change 2026](https://lensblox.com/blog/roblox-algorithm-change-2026-explained/) – 🟠
