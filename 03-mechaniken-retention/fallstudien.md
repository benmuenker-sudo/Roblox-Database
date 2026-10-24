# Fallstudien: Was Hits und Studios bei Retention und Live-Ops tun

> Stand: 2026-10-24 · Nächste Prüfung: 2026-11-07 (Marktdaten veralten schnell) · Gesamt-Vertrauen: 🟡 für Presse- und Studiodaten, 🟠 für Tracker- und Fan-Wiki-Zahlen, ✅ nur wo Roblox selbst zitiert wird, 🧠 für alle „Lehren“

## Kurzfassung
Die Mega-Hits 2025/26 (Grow a Garden, Steal a Brainrot, 99 Nights in the Forest, Steal An Egg) kombinieren einen extrem einfachen Sammel- oder Survival-Loop mit Timern oder Diebstahl-Spannung, wöchentlichen Samstags-Updates mit Live-„Admin Abuse“-Events, limitierten Items und Handel. 🟡/🟠 Sie erreichten 14–26 Mio. gleichzeitige Spieler, verloren aber oft über 90 % binnen Monaten. 🟠 Evergreens zeigen das Gegenmodell: Pet Simulator 99 (inhaltsgetriebene statt wöchentliche Updates), Murder Mystery 2 (Handelsökonomie plus saisonale Events, laut Trackern ältestes Spiel über 1 Mio. CCU) und Adopt Me! (Pet-Varianten, Analytics und Experiments). 🟡/🟠 Studios veröffentlichen fast nie Retention- oder Umsatzzahlen. Viele Mechanik-Details stammen aus Fan-Wikis und Trackern. Behandle sie als Hinweise, nicht als Fakten. 🟠

## Referenzbilder
Offizielle Bilder aus der Roblox Creator Documentation (CC BY 4.0, Übersicht und Lizenz: `assets/bilder/offiziell/README.md`).

![Content-Kadenz Jailbreak](../assets/bilder/offiziell/monetarisierung-liveops/liveops-content-kadenz.png)
*Jailbreak: Update-Banner mit Feature-Liste. Offizielles Beispiel für Kadenz plus große Updates. Quelle: Roblox Creator Docs, CC BY 4.0 ([LiveOps essentials](https://create.roblox.com/docs/production/game-design/liveops-essentials))*

![Unbalanciertes Event](../assets/bilder/offiziell/monetarisierung-liveops/wirtschaft-event-unbalanciert.png)
*Event ohne Wirtschaftsmodell: Ausgaben steigen, Käufe bleiben flach. Die Lehre hinter limitierten Admin-Event-Items. Quelle: Roblox Creator Docs, CC BY 4.0 ([Balance virtual economies](https://create.roblox.com/docs/production/game-design/balance-virtual-economies))*

Selbst erstelltes Referenzbild: ![Live-Ops-Kalender 8 Wochen](../assets/bilder/live-ops-kalender-8-wochen.png)

## Warum das wichtig ist
- Roblox selbst sagt: 2025 dominierten hochmonetarisierende Viral-Hits, 2026 verlagerte sich das Engagement zu neueren und Evergreen-Spielen, die pro Stunde weniger monetarisieren. ✅ ([Q2-2026-Shareholder-Letter](https://s27.q4cdn.com/984876518/files/doc_financials/2026/q2/Roblox-Q2-2026-Earnings-Shareholder-Letter.pdf))
- Die Home-Empfehlung belohnt seit Juni 2026 28-Tage-Retention. Viral-Spitzen ohne Bindung bringen weniger als früher. ✅ ([Roblox Newsroom](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox))
- Marktüberblick und Rangliste: `01-markt-trends/viral-hits-analyse.md`, `01-markt-trends/aktuelle-top-spiele.md`.

## Übersicht
| Spiel | Studio | Start | Rekord-CCU | Kernmuster | Status Okt. 2026 | Vertrauen |
|---|---|---|---|---|---|---|
| Grow a Garden | BMWLux + Splitting Point | März 2025 | 22,3 Mio. (23.08.2025) | Pflanzen–Warten–Ernten, Wetter, Admin Abuse | Nachfolger GAG2 schwach | 🟡 |
| Steal a Brainrot | SpyderSammy / DoBig | 16.05.2025 | 25,2–25,8 Mio. (Okt. 2025) | Kaufen–Verteidigen–Stehlen, Rebirth, Handel | ca. 215 K (−99 %) | 🟡/🟠 |
| 99 Nights in the Forest | Grandma's Favourite Games | ca. März 2025 | 14,2 Mio. | Koop-Survival, Themen-Updates | ca. 289 K, Film angekündigt | 🟡/🟠 |
| Plants vs Brainrots | Yo Gurt Studio | ca. Aug. 2025 | 3,2 Mio. | Tower Defense + Brainrot | ca. 1 Mio. (Jan. 2026) | 🟠 |
| Steal An Egg | (Misfits beansprucht Beteiligung) | 25.07.2026 | 14,2–14,3 Mio. (Sept. 2026) | Eier/Pets stehlen und ausbrüten | #1 im Okt. 2026 | 🟡/🟠 |
| Pet Simulator 99 | BIG Games | – | – | Pets, Gebiete, Rebirths, Huges | Update ~92 | 🟡 |
| Murder Mystery 2 | – | (Evergreen) | 1.349.555 (Aug. 2026) | Runden + Handelsökonomie | Top 2 im Okt. 2026 | 🟠 |
| Adopt Me! | Uplift Games | (Evergreen) | – | Pets, Rollenspiel, Handel | ca. 209 K (#7) | ✅/🟠 |

Quellen in den einzelnen Abschnitten.

---

## 1. Grow a Garden (BMWLux / Splitting Point Studios)

**Steckbrief**
- Von einem anonymen 16-Jährigen („BMWLux“) gebaut, laut Jandel in **drei Tagen**. Miteigentum von Splitting Point Studios (Janzen „Jandel“ Madsen), DoBig Studios hält eine Minderheit. 🟡 ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden); [NBC](https://www.nbcbayarea.com/entertainment/entertainment-news/virtual-gardens-viral-roblox-game-created-teenager/3926104/?amp=1))
- Splitting Point stieg bei etwa **1.000 CCU** ein, setzte rund **12 der 19 Entwickler** darauf und „started weekly updates“. 🟡 ([GamesBeat](https://gamesbeat.com/janzen-madsen-interview/); [games.gg](https://games.gg/es/news/roblox-grow-a-garden-alcanza-16-millones-de-ccu/))
- Splitting Points früheres Spiel *Field Trip Z* erreichte 45 Mio. Spieler in einem Jahr. 🟡, älter ([GameAnalytics Blog](https://www.gameanalytics.com/blog/splitting-point-how-field-trip-z-got-45m-players))
- RIA 2025: die meisten Preise, u. a. Best New Experience; Splitting Point „Best Studio“. 🟡 ([Variety](https://variety.com/2025/digital/news/grow-a-garden-roblox-innovation-awards-2025-winners-1236510387))

**CCU-Verlauf** 🟡 ([Insider Gaming](https://insider-gaming.com/roblox-grow-a-garden-shatters-all-time-player-record-for-second-week-in-a-row/); [PocketGamer.biz](https://www.pocketgamer.biz/robloxs-grow-a-garden-hits-industry-record-213m-concurrent-users-surpassing-pubg-fortnite-and-more/); [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden))
| Datum | CCU | Anlass |
|---|---|---|
| 24.05.2025 | 8,9 Mio. | – |
| 31.05.2025 | 11,7 Mio. | Update-Samstag |
| 14.06.2025 | 16,4 Mio. | Update-Samstag |
| 21.06.2025 | 21,3 Mio. (Roblox: 21,6 Mio.) | „Summer Harvest“-Update |
| 23.08.2025 | 22,3 Mio. | Admin-Events; Plattformrekord 47,3 Mio. am selben Tag |
Neue Spitzen fielen jeweils mit Update-Releases zusammen. Im September 2025 übernahm Steal a Brainrot den Rekord. 🟡

**Umsatz:** Eine Drittquelle nannte rund **12 Mio. $** Item-Verkäufe im Mai 2025. Jandel lehnte Angaben ab. Ein Tracker-Modell schätzt später ca. 1,75 Mio. $/Monat. Stark abweichend. 🟡/🟠 ([Calcalist](https://www.calcalistech.com/ctechnews/article/dj4lxef8r); [RoWatcher](https://rowatcher.com/games/7436755782/grow-a-garden))

**Mechaniken**
- Loop: pflanzen → warten → ernten → größere Beete und seltenere Pflanzen. Robux beschleunigen und ermöglichen Stehlen bei Nachbarn. Sanftes Onboarding und Idle-Timer wie FarmVille/Hay Day, für viele Roblox-Spieler „entirely fresh“. 🟡 ([Naavik](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/))
- **Admin Abuse:** wöchentlich, typischerweise samstags mit dem großen Update; Jandel oder Teammitglieder lösen Wetter-Events aus und steuern Shop-Bestände; zweiter Termin „Watering Wednesday“ (Jhailatte); nur auf öffentlichen Servern. Angaben zur Startzeit widersprechen sich. 🟠 ([GAG Wiki](https://growagarden.fandom.com/wiki/Admin_Abuse); [Sportskeeda](https://www.sportskeeda.com/roblox-news/when-admin-abuse-start-grow-garden))
- Bot-Vorwurf: TD Cowen vermutete Bots, die die Sichtbarkeit aufblähten. Roblox sagte, die Analyse zeige echte Beliebtheit. 🟡 ([Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden))

**Grow a Garden 2 (2026)**
- Start 12.06.2026 (veröffentlicht unter „Strawberreh Squad“). Neu: Tages-Farming plus nächtliches Stehlen und Basisverteidigung. Über 400 K CCU 20 Minuten nach Start, Server-Engpässe. 🟡 ([allthings.how](https://allthings.how/grow-a-garden-2-launches-june-12-with-night-stealing-on-roblox/); [GosuGamers](https://www.gosugamers.net/entertainment/news/78614-grow-a-garden-2-has-launched-on-roblox-here-s-everything-new-added-in-this-sequel))
- Spitze 929.371 (Rolimons, 19.06.2026) bzw. 976 K (RoWatcher). Im Spätsommer lag die 24-h-Spitze nur noch bei **5.384**. Also rund 4 % des Originals und etwa −99 % in zwei Monaten. 🟠 ([Rolimons](https://www.rolimons.com/game/97598239454123); [RoVitals](https://rovitals.com/game/97598239454123))
- Wöchentliches Admin Abuse laut Community ersetzt durch über die Woche verteilte kleinere Drops und unregelmäßige **„Admin Parties“**. Die erste (ca. 01.–02.08.2026) brachte ein „Jandel Monkey“-Pet, das nach dem 30-Minuten-Fenster unerhältlich wurde. Eine „Fall World“-Migration gab 60 Tage, um Items per „Magic Mail“ in den Hauptgarten zu schicken. 🟠 ([roonby](https://roonby.com/2026/07/03/does-grow-a-garden-2-have-admin-abuse-everything-we-know-so-far/); [gameboost](https://gameboost.com/blog/grow-a-garden-2-admin-abuse); [mygagcalculator](https://mygagcalculator.com/grow-a-garden-2-event-tracker/))

**Lehren (🧠)**
1. Ein in Tagen gebauter, sofort verständlicher Loop kann reichen, wenn er für das Publikum neu ist (Idle-Farming war auf Roblox frisch).
2. Ein Studio mit LiveOps-Kapazität (12 Entwickler, wöchentliche Updates) macht aus einem kleinen Spiel einen Rekord. Ohne Team ist das nicht kopierbar.
3. Update-Tage als Termine bündeln CCU. Das passt zur offiziellen Samstags-Spitze im Home-Traffic. ✅ ([Discovery](https://create.roblox.com/docs/discovery))
4. Ein Nachfolger übernimmt das Publikum nicht automatisch. Der zweite Teil braucht einen eigenen Grund zu existieren.
5. 30-Minuten-Exklusives erzeugen Hype, aber auch genau die „manufactured urgency“, die Regulierer kritisieren (siehe `live-ops-events.md`).

---

## 2. Steal a Brainrot (SpyderSammy / DoBig Studios)

**Steckbrief**
- Start **16.05.2025**, entwickelt in der brasilianischen Spyder-Community, produziert von DoBig Studios. 🟡 ([Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot))
- Loop: Brainrot-Figuren kaufen, die passiv Geld erzeugen → die eigene Basis mit Fallen und Shop-Items verteidigen → andere bestehlen → Rebirth (Geld **plus** ein bestimmter Brainrot). 🟡 ([Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot); [BloxInformer](https://bloxinformer.com/wikis/steal-a-brainrot/))

**CCU-Verlauf** 🟠 ([RoWatcher](https://rowatcher.com/news/is-the-brainrot-trend-dying-what-ccu-data-from-three-top-games-reveals); [PocketGamer.biz](https://www.pocketgamer.biz/robloxs-steal-a-brainrot-becomes-first-game-to-surpass-25m-concurrent-players))
| Zeitpunkt | CCU | Anlass |
|---|---|---|
| Juli 2025 | 5 Mio. | – |
| Aug. 2025 | 20 Mio. | „Admin War“-Crossover mit Grow a Garden |
| Sept. 2025 | 24 Mio. | Event; übernimmt CCU-Rekord |
| Okt. 2025 | 25,2–25,8 Mio. | „Yin Yang“-Event; erstes Spiel über 25 Mio. (Quellen uneinig) |
| Jan. 2026 | 12,8 Mio. | virtuelles Bruno-Mars-Konzert |
| 2026 | ca. 215 K | −99,2 % gegenüber Rekord |
Jeder Peak wurde von einem schärferen Abfall gefolgt. 🟠 Im August 2026 fiel der Monatsdurchschnitt um 9 % gegenüber dem Vormonat. 🟠 ([MaxPowerGaming](https://www.maxpowergaming.co/post/roblox-s-top-games-in-august-2026-murder-mystery-2-and-steal-an-egg-take-over))

**Umsatz:** Bloomberg schätzt **über 64 Mio. $** Echtgeldkäufe seit Launch. 🟡 (über [RoWatcher](https://rowatcher.com/news/is-the-brainrot-trend-dying-what-ccu-data-from-three-top-games-reveals))

**LiveOps**
- Update „almost every Saturday“ mit neuen Brainrots, Events, **Mutationen** und Traits; nummerierte Updates bis Update 62 (15.08.2026). Ein anderer Tracker schätzt neue Brainrot-Wellen etwa alle 2 Wochen. 🟠 ([playbrainrot](https://www.playbrainrot.org/en/updates/); [allthings.how](https://allthings.how/steal-a-brainrot-new-brainrots-schedule/))
- Wöchentliches Admin-Abuse-Event; wer den Samstag verpasst, wartet eine Woche. 🟠 ([Eldorado](https://www.eldorado.gg/blog/steal-a-brainrot-en/steal-a-brainrot-admin-abuse-schedule-explained/))
- Codes sind selten. Eine Guide-Seite führt die Retention auf die Steal-and-Defend-Spannung und den Handel mit seltenen Brainrots zurück. 2026 kamen dauerhafter Handel und Trade-Plaza-Verbesserungen. 🟠 ([timesaver.gg](https://timesaver.gg/blog/steal-a-brainrot-codes-october-2026); [Eldorado Update Log](https://www.eldorado.gg/blog/steal-a-brainrot-update-log/))
- RIA 2025 „Best Creative Direction“, umstritten wegen KI-generierter Assets. Port nach Fortnite UEFN, Film angekündigt. 🟡 ([Sportskeeda](https://www.sportskeeda.com/roblox-news/roblox-innovation-awards-2025-all-winners); [Beebom](https://beebom.com/robloxs-steal-a-brainrot-delivered-a-2025-masterclass-in-player-engagement-and-gave-uefn-a-second-wind/))

**Lehren (🧠)**
1. Verlustangst ist ein starker Rückkehrgrund: Wer etwas besitzt, das gestohlen werden kann, schaut nach. Das erzeugt die „Tages“-Ebene der Rückkehr.
2. Rebirth an ein Sammelobjekt zu binden verknüpft Progression, Sammeln und Stehlen.
3. Crossovers zwischen Hits (Admin War) heben beide Spiele.
4. Der −99-%-Verlauf zeigt: Spitzen aus Events und Memes sind keine Retention. Ohne tieferes Endgame bleibt wenig.
5. KI-Assets bringen Reputationsrisiken, auch bei Erfolg.

---

## 3. 99 Nights in the Forest (Grandma's Favourite Games)

**Steckbrief**
- Entwickler Alec Kieft, Matt Hufton, Cameron Angland. Sie sagten PCGamesN im September 2026, „the numbers don't feel real“, bleiben lieber anonym und sind „not keen“ auf KI in ihren Spielen. 🟡 ([PCGamesN](https://www.pcgamesn.com/roblox/99-nights-in-the-forest-interview))
- Rekord **14,2 Mio. CCU** (Datum nicht gefunden). Snapshot 2026 ca. 288.558. Rund 29–30 Mrd. Besuche, Gruppe mit über 10 Mio. Mitgliedern. 🟡/🟠 ([Wikipedia](https://en.wikipedia.org/wiki/List_of_Roblox_games); [RoWatcher](https://rowatcher.com/games/7326934954); [Roblox Fandom](https://roblox.fandom.com/wiki/Grandma's_Favourite_Games))
- RIA 2025: Best Adventure und Best Horror. 🟡 ([Variety](https://variety.com/2025/digital/news/grow-a-garden-roblox-innovation-awards-2025-winners-1236510387))

**Update-Rhythmus** 🟠 ([Sportskeeda Fishing](https://www.sportskeeda.com/roblox-news/99-nights-forest-fishing-update-guide); [Sportskeeda Volcanic](https://www.sportskeeda.com/roblox-news/when-next-99-nights-forest-update-volcanic-biome-part-1); [Stealthy Gaming](https://stealthygaming.com/99-nights-in-the-forest-christmas-week-3-update-release-date-and-details/))
| Datum | Update |
|---|---|
| 11.07.2025 | Furniture |
| 15.08.2025 | Fishing + Klassen + **wöchentliche Quests** |
| 13.09.2025 | Volcanic Biome |
| Dez. 2025 | wöchentliche Weihnachts-Updates |
| 20.08.2026 | Fortnite-Crossover |

**IP-Erweiterung:** Realfilm bei 20th Century Studios (Drehbuch Josh Cooley, Produzenten Sam Raimi und Rob Tapert, die Entwickler als Executive Producer). 🟡 ([Hollywood Reporter](https://www.hollywoodreporter.com/movies/movie-news/99-nights-in-the-forest-josh-cooley-20th-century-studios-film-1236704624/); [Variety](https://variety.com/2026/film/news/99-nights-in-the-forest-movie-20th-century-studios-1236720515/))

**Lehren (🧠)**
1. Eine klare Prämisse mit eingebautem Ziel („99 Nächte“) ist Onboarding und Langzeitziel zugleich.
2. Koop-Survival nutzt den sozialen Kern von Roblox und passt zum RFY-Signal „intentional co-play“. ✅ ([Discovery](https://create.roblox.com/docs/discovery))
3. Neue Systeme (Klassen, Angeln, wöchentliche Quests) statt nur neuer Items halten das Spiel frisch. Das entspricht dem offiziellen „Major Update“-Typ. ✅ ([LiveOps essentials](https://create.roblox.com/docs/production/game-design/liveops-essentials))
4. Horror/Survival wächst 2026 (Statroblox: Survival +13 % in 7 Tagen). 🟠 ([Statroblox](https://statroblox.com/guides/most-popular-roblox-genres))

---

## 4. Plants vs Brainrots (Yo Gurt Studio)
- Tower-/Zombie-Defense mit Brainrot-Ästhetik, Start ca. August 2025. Rekord **3,2 Mio. CCU** etwa einen Monat nach Start (Rolimons), im Januar 2026 wieder bei rund 1 Mio. 🟠 ([ts2.tech](https://ts2.tech/en/robloxs-newest-phenomenon-plants-vs-brainrots-breaks-records-heres-why-everyones-obsessed/); [Bitrue](https://www.bitrue.com/blog/plants-vs-brainrots-roblox-guide-2026))
- **Lehren (🧠):** Ein bekanntes Genre (Tower Defense) in einer gerade populären Ästhetik senkt die Lernkosten. Die Doku sagt: Je näher an Genre-Normen, desto weniger muss erklärt werden. ✅ ([Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox)) Aber Ästhetik-Trends sättigen schnell: Brainrot gilt 2026 als „cooling but not dead“. 🟠 ([RoWatcher](https://rowatcher.com/news/is-the-brainrot-trend-dying-what-ccu-data-from-three-top-games-reveals))

---

## 5. Steal An Egg (2026)
- Start **25.07.2026**. Misfits Gaming nennt es „#1 game on Roblox overnight“ mit 371 K CCU und „another breakout success across the Misfits games portfolio“. Der eigentliche Entwickler ist nicht eindeutig belegt. 🟡/🟠 ([Misfits auf X](https://x.com/MisfitsGG/status/2090785862632038706))
- Rekord **14.272.591** am 19.09.2026 (RoVitals) bzw. 14,3 Mio. (RoWatcher). Monatsdurchschnitt August ca. 542.564, September ca. 1,4 Mio. Snapshots im Oktober 782 K bis 1,5 Mio. (#1 am 24.10.2026). Eine Guide-Seite nennt „around 3 million“, widersprüchlich. 🟠 ([RoVitals](https://rovitals.com/game/107778070777162); [RoWatcher](https://rowatcher.com/games/10563114921/steal-an-egg); [MaxPowerGaming Sept.](https://www.maxpowergaming.co/post/roblox-s-top-games-in-september-2026-steal-an-egg-pulls-away-as-ride-a-pet-arrives))
- Format: „Steal a ___“-Nachfolger mit Eier-/Pet-Diebstahl und Sammeln. Gilt als Test, ob der nächste Viral-Hit die Q3-Bookings von Roblox stützt. 🟡 ([Yahoo Finance/TIKR](https://finance.yahoo.com/markets/stocks/articles/roblox-stock-down-37-2026-041623422.html))
- Nachahmer folgen schnell: *Ride a Pet* (Sept. 2026, ca. 208 K). 🟠 ([StudioKrew](https://studiokrew.com/blog/top-roblox-games-september-2026/))
- **Lehren (🧠):** Das Steal-Muster funktioniert auch 2026 noch als Beschleuniger. Ob es unter der 28-Tage-RFY-Logik länger hält als 2025, ist offen. Hier lohnt es, die Monatsdurchschnitte zu beobachten statt die Spitzen.

---

## 6. Pet Simulator 99 (BIG Games): Kadenzwechsel

**Fakten** 🟡 (Studio-Posts)
- Anfang 2024 (älter, ca. 1.000 Tage) gab BIG Games bekannt, die **wöchentlichen Updates einzustellen** und zu veröffentlichen, wenn Inhalte fertig sind: Ziel ein Samstags-Release nach substanzieller Arbeit, Wochen zwischen den Updates. Ziel pro großem Update: **25+ Gebiete, ein neuer Rebirth, Dutzende Pets, mehrere neue Mechaniken**. ([BIG Games Update 4](https://www.biggames.io/post/pet-simulator-99-update-4))
- 2026 folgen Updates dem Muster **event-gebundener limitierter Huge-Pets**: World-Cup-Update mit Fußball-Minispielen und Ranglisten, Coin-Arcade-Update mit Huges aus Arcade-Zonen und Boss-Truhen. Update-Nummer ~92 um September 2026. ([Update 82](https://www.biggames.io/post/pet-simulator-99-update-82); [Update 92](https://www.biggames.io/post/pet-simulator-99-update-92))
- Handels-Infrastruktur: **Trading Terminal** (gesuchte Items suchen, Teleport zum Angebot auf der Plaza); ein Update entfernte Rangbeschränkungen beim Handel. ([Update 48](https://www.biggames.io/post/pet-simulator-99-update-48))

**Lehren (🧠)**
1. Selbst eines der erfahrensten Roblox-Studios hält wöchentliche Updates nicht dauerhaft durch. Das stützt die offizielle Warnung vor Burnout. ✅ ([LiveOps essentials](https://create.roblox.com/docs/production/game-design/liveops-essentials))
2. Weniger, aber größere Updates mit festem Paket (Gebiete + Rebirth + Pets + Mechanik) geben Spielern ein klares Erwartungsmuster.
3. Limitierte Event-Pets sind der Monetarisierungs- und Retention-Anker, brauchen aber ein Wirtschaftsmodell (siehe `live-ops-events.md`, Event-Ökonomie).
4. Handel braucht Werkzeuge (Suche, Plaza), nicht nur ein Handelsfenster.

---

## 7. Murder Mystery 2: das Evergreen-Modell

**Fakten** 🟠 (Tracker, Blogs)
- Täglicher Durchschnitt ca. 252–301 K Anfang Juli 2026. Das **Sommer-Event am 23.07.2026** (Lobby, Map, Mystery Box, Godly-Packs) hob den 7-Tage-Schnitt auf **596.960** (24.–30.07.). Spitze 1,1 Mio., dann **1.349.555** im August 2026, beschrieben als ältestes Roblox-Spiel über 1 Mio. ([Bloxodes](https://bloxodes.com/stats/reports/roblox-july-2026); [StudioKrew Aug.](https://studiokrew.com/blog/top-roblox-games-august-2026/))
- August-2026-Durchschnitt ca. 633 K (#1). Der September-Durchschnitt wird mit 249 K angegeben, ein Snapshot vom 24.10.2026 zeigt 1,3 Mio. (#2). Die Werte passen nicht zusammen, vermutlich unterschiedliche Methoden. ([MaxPowerGaming Aug.](https://www.maxpowergaming.co/post/roblox-s-top-games-in-august-2026-murder-mystery-2-and-steal-an-egg-take-over); [MaxPowerGaming Sept.](https://www.maxpowergaming.co/post/roblox-s-top-games-in-september-2026-steal-an-egg-pulls-away-as-ride-a-pet-arrives); [RoWatcher](https://rowatcher.com/roblox-player-count))
- Treiber laut Blog: Handelsökonomie mit Hunderten handelbarer Godlies; saisonale Boxen werten alte Inventare um. ([Earnaldo](https://earnaldo.com/blog/best-roblox-games-2026.html))

**Lehren (🧠)**
1. Eine Handelsökonomie mit langer Item-Historie ist ein Langzeit-Asset: Jedes Event macht alte Sammlungen wieder interessant.
2. Ein Runden-Loop plus Sammel-/Handelsschicht ist evergreen-fähig.
3. Ein gutes saisonales Event kann ein sehr altes Spiel auf neue Rekorde heben. Reaktivierung ist möglich. Die Doku nennt Live-Events ausdrücklich als Weg, „lapsed players“ zurückzuholen. ✅ ([LiveOps essentials](https://create.roblox.com/docs/production/game-design/liveops-essentials))

---

## 8. Adopt Me! (Uplift Games)

**Fakten**
- Die offizielle Doku nennt **Pet-Varianten** (gefleckt, farbig) und **thematische Updates** von *Adopt Me!* als Vorbild für nachhaltige Content-Kadenz. ✅ ([Content updates](https://create.roblox.com/docs/production/game-design/content-updates))
- Uplift nutzt Roblox Analytics und Experiments. Bei einem Sommer-Event-Feature „the crash rate and frame rate clued us in that something was going wrong“ (UpliftBradB). ✅ Newsroom, nur Ausschnitt geprüft ([Roblox Newsroom, Aug. 2026](https://about.roblox.com/newsroom/2026/08/optimize-testing-live-updates-roblox-analytics-experimentation-platform))
- 43,2 Mrd. Besuche (2026), am 24.10.2026 Platz 7 mit ca. 209 K CCU. 🟠 ([Cubix](https://www.cubix.co/blog/top-10-most-popular-roblox-games/); [RoWatcher](https://rowatcher.com/roblox-player-count))

**Lehren (🧠)**
1. Varianten bestehender Inhalte (Recolors) sind die günstigste nachhaltige Kadenz, wenn das System sie trägt.
2. Technische Metriken (Crash-Rate, FPS) sind Live-Event-Frühwarnsysteme. Nach jedem Release prüfen. ✅ ([Retention](https://create.roblox.com/docs/production/analytics/retention))
3. Große Studios testen mit Experiments. Ab 1.000 DAU sollten auch kleinere das tun (siehe `analytics-und-experimente.md`).

---

## 9. Offizielle Doku-Beispiele: Jailbreak und Doors ✅
- **Jailbreak:** Kadenz plus große Updates, Season Pass mit Free- und Premium-Track und gezeigter Finalbelohnung. ([LiveOps essentials](https://create.roblox.com/docs/production/game-design/liveops-essentials); [Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design))
- **Doors:** QoL-Updates, Bug-Triage, klare Item-Erklärungen (Revives). ([LiveOps essentials](https://create.roblox.com/docs/production/game-design/liveops-essentials); [Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations))

---

## 10. Studio-Aussagen zum Prozess

**Gamefam (Joe Ferencz)** 🟡
- Eine Finanzierungsrunde über 25 Mio. $ floss in Creator-Partnerschaften, **Analytics, LiveOps-Tools** und Ad-Tech. Ferencz nennt „our live ops practices“ als Grund, warum Top-Entwickler kommen. ([GamesBeat](https://gamesbeat.com/gamefam-sees-rapid-growth-in-making-games-for-roblox/))
- Grundlagen seien Akquise, Retention und Monetarisierung; Akquise sei „essentially fully dependent on the algorithm“. ([GamesBeat](https://gamesbeat.com/gamefam-sees-rapid-growth-in-making-games-for-roblox/); [Player Driven](https://playerdriven.io/desk/gamefam-s-joe-ferencz-on-roblox-s-metaverse-potential))
- Gamefam hatte nach eigener Aussage 5 der Top-15-Markenspiele auf Roblox. 🟡 ([GamesBeat](https://gamesbeat.com/gamefam-closes-year-of-growth-with-5-of-top-15-branded-games-on-roblox/))

**Dubit** 🟡 (Studio-Marketing)
- Beschreibt eine „Retention-Schicht“ (Progression, Freischaltungen, Ziele), misst D1, D7 und **die Form der Retention-Kurve** gegen interne Daten und empfiehlt ein **monatlich rollierendes LiveOps-Budget** mit eigenem Team. ([Dubit Services](https://dubit.io/services/roblox-game-development); [Dubit Blog](https://dubit.io/blog/how-we-build-hit-roblox-games); [Dubit Library](https://dubit.io/library/what-makes-a-new-roblox-game-take-off))

**Portfolio-Studios** 🟡/🟠
- DoBig Studios kauft systematisch Anteile an Roblox-Spielen (u. a. Minderheit an Grow a Garden, Produzent von Steal a Brainrot). Splitting Point, Misfits und andere arbeiten ähnlich. Hits entstehen zunehmend in Studios mit LiveOps-Kapazität, auch wenn die Originale klein starteten. ([Roblox Fandom: DoBig](https://roblox.fandom.com/wiki/Do_Big_Studios%E2%84%A2); [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden))

---

## Querschnitt: wiederkehrende Muster
| Muster | Wo beobachtet | Vertrauen | Offizielle Entsprechung |
|---|---|---|---|
| Timer und Offline-Wachstum | GAG | 🟡 | Rückkehrfrequenz als Wachstumstreiber (GameAnalytics 2025 🟡) |
| Restocks und live gesteuerte Shops | GAG Admin Abuse | 🟠 | – |
| Wetter/Mutationen als Live-Multiplikator | GAG, SaB | 🟠 | – |
| Limitierte, später unerhältliche Items | GAG2, PS99, MM2 | 🟠/🟡 | Golden-Salmon-Beispiel, Event-Ökonomie ✅ |
| Rebirth als Reset | PS99, SaB | 🟡 | – |
| Ranglisten-Events | PS99 | 🟡 | Competitive Major Update ✅ |
| Handelsplaza/-terminal | PS99, SaB, MM2 | 🟡/🟠 | Social Major Update ✅ |
| Samstags-Updates | GAG, SaB, PS99 | 🟠/🟡 | Home-Traffic-Spitze samstags ✅ |
| Crossovers zwischen Hits | GAG × SaB, 99 Nights × Fortnite | 🟡 | – |

## Was du daraus lernen kannst (🧠)
1. **Einfacher Loop, tiefe Schichten.** Alle Hits starten simpel. Die Evergreens haben darunter Handel, Sammlung, Rebirth oder Saisons.
2. **Termine statt Zufall.** Feste Update-Tage, am besten vor dem Wochenende.
3. **Kadenz nach Kapazität.** PS99 und GAG2 zeigen: Wöchentlich ist auch für Top-Teams kaum durchzuhalten. Die offizielle Basis (Drops alle 2–4 Wochen, große Updates alle 2–3 Monate) ist realistischer.
4. **Wirtschaft vor Hype.** Jedes limitierte Item und jedes Admin-Event muss im EV-Modell stehen.
5. **Spitzen sind keine Retention.** Monatsdurchschnitte und D7/D30 beobachten, nicht Rekord-CCU.
6. **Social ohne Chat.** Live-Events auf öffentlichen Servern, Handelsterminals und Koop funktionieren auch mit Altersprüfung.
7. **Nicht kopieren.** Roblox begrenzt die Reichweite für „Non-unique games“ und Standout Games lehnt Kopien oder Reskins ab. ✅ ([Discovery](https://create.roblox.com/docs/discovery); [Standout Games](https://create.roblox.com/docs/creator-programs/standout-games)) Siehe `02-spielkonzepte/spiele-abaendern.md`.

## Do / Don't
| Do | Don't |
|---|---|
| Muster verstehen und auf eigene Idee übertragen | Hit eins zu eins nachbauen |
| Monatsdurchschnitte und Kohorten vergleichen | Tracker-Snapshots als Fakt nehmen |
| Kadenz an Teamgröße anpassen | Wöchentlichen Rhythmus der Hits ohne Team übernehmen |
| Limitierte Items mit Wirtschaftsmodell und fairen Wegen | FOMO als einziger Rückkehrgrund |

## Checkliste
- [ ] Für das eigene Konzept: Welches Muster aus der Tabelle oben passt?
- [ ] Welche Tiefenschicht (Handel, Sammlung, Rebirth, Saison) trägt nach dem Hype?
- [ ] Realistische Kadenz für das eigene Team festgelegt?
- [ ] Event-Ökonomie für limitierte Items modelliert?
- [ ] Unterscheidet sich das Spiel klar von Vorbildern (Originalität für Discovery)?

## Offene Fragen / Recherche-Bedarf
- Keine verifizierten Retention- oder Umsatzzahlen der Studios.
- Nicht recherchiert: Dress to Impress, Fisch, Dead Rails, Doors (Kadenz), Blox Fruits, Rivals im Detail.
- Volltext des GamesBeat-Interviews mit Janzen Madsen und des Uplift-Newsroom-Artikels nicht geprüft.
- Entwickler von Steal An Egg unklar.

## Quellen
- [Roblox Q2-2026-Shareholder-Letter](https://s27.q4cdn.com/984876518/files/doc_financials/2026/q2/Roblox-Q2-2026-Earnings-Shareholder-Letter.pdf) – Juli 2026, ✅
- [Roblox Newsroom: Optimizing Discovery](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox) – Juni 2026, ✅
- [Roblox Newsroom: Analytics & Experimentation (Uplift)](https://about.roblox.com/newsroom/2026/08/optimize-testing-live-updates-roblox-analytics-experimentation-platform) – Aug. 2026, ✅ (Ausschnitt)
- [Creator Docs: Content updates](https://create.roblox.com/docs/production/game-design/content-updates), [LiveOps essentials](https://create.roblox.com/docs/production/game-design/liveops-essentials), [Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design), [Discovery](https://create.roblox.com/docs/discovery) – ✅
- [Wikipedia: Grow a Garden](https://en.wikipedia.org/wiki/Grow_a_Garden), [Steal a Brainrot](https://en.wikipedia.org/wiki/Steal_a_Brainrot), [List of Roblox games](https://en.wikipedia.org/wiki/List_of_Roblox_games) – 🟡
- [GamesBeat: Janzen Madsen](https://gamesbeat.com/janzen-madsen-interview/), [GamesBeat: Gamefam](https://gamesbeat.com/gamefam-sees-rapid-growth-in-making-games-for-roblox/) – 🟡
- [Naavik: Predicting the next big hits](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/) – 2025, 🟡
- [Calcalist](https://www.calcalistech.com/ctechnews/article/dj4lxef8r), [Insider Gaming](https://insider-gaming.com/roblox-grow-a-garden-shatters-all-time-player-record-for-second-week-in-a-row/), [PocketGamer.biz](https://www.pocketgamer.biz/robloxs-steal-a-brainrot-becomes-first-game-to-surpass-25m-concurrent-players), [PCGamesN](https://www.pcgamesn.com/roblox/99-nights-in-the-forest-interview), [Hollywood Reporter](https://www.hollywoodreporter.com/movies/movie-news/99-nights-in-the-forest-josh-cooley-20th-century-studios-film-1236704624/), [Variety RIA 2025](https://variety.com/2025/digital/news/grow-a-garden-roblox-innovation-awards-2025-winners-1236510387) – 🟡
- [BIG Games: Update 4](https://www.biggames.io/post/pet-simulator-99-update-4), [Update 48](https://www.biggames.io/post/pet-simulator-99-update-48), [Update 82](https://www.biggames.io/post/pet-simulator-99-update-82), [Update 92](https://www.biggames.io/post/pet-simulator-99-update-92) – 🟡
- [Dubit](https://dubit.io/blog/how-we-build-hit-roblox-games) – 🟡 (Studio-Marketing)
- [RoWatcher](https://rowatcher.com/news/is-the-brainrot-trend-dying-what-ccu-data-from-three-top-games-reveals), [RoVitals](https://rovitals.com/game/107778070777162), [Rolimons](https://www.rolimons.com/game/97598239454123), [Bloxodes](https://bloxodes.com/stats/reports/roblox-july-2026), [MaxPowerGaming](https://www.maxpowergaming.co/post/roblox-s-top-games-in-august-2026-murder-mystery-2-and-steal-an-egg-take-over), [StudioKrew](https://studiokrew.com/blog/top-roblox-games-september-2026/), [GAG Wiki](https://growagarden.fandom.com/wiki/Admin_Abuse), [roonby](https://roonby.com/2026/07/03/does-grow-a-garden-2-have-admin-abuse-everything-we-know-so-far/), [Eldorado](https://www.eldorado.gg/blog/steal-a-brainrot-update-log/), [Earnaldo](https://earnaldo.com/blog/best-roblox-games-2026.html), [ts2.tech](https://ts2.tech/en/robloxs-newest-phenomenon-plants-vs-brainrots-breaks-records-heres-why-everyones-obsessed/) – 🟠

## Verknüpfungen
`core-loops.md`, `live-ops-events.md`, `social-loops.md`, `analytics-und-experimente.md`, `01-markt-trends/viral-hits-analyse.md`, `02-spielkonzepte/spiele-abaendern.md`
