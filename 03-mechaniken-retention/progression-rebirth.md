# Progression, Rebirth und Prestige

> Stand: 2026-10-24 · Nächste Prüfung: 2026-11-21 · Gesamt-Vertrauen: ✅ für offizielle Progressions-, Quest- und Wirtschaftsregeln (Creator Docs), 🟡/🟠 für Beispiele, 🧠 für Kurven, Zeitwerte und Rebirth-Gestaltung

## Kurzfassung
Progression ist das Gefühl, ständig besser, stärker oder reicher zu werden. Roblox nennt das Progressionssystem den wichtigsten Hebel für **D7-Retention**: klare kurz- und langfristige Ziele, Abwechslung, ausbalancierte Schwierigkeit. ✅ Im Onboarding sollen die ersten Level schnell erreichbar sein (niedrige XP-Schwellen, live per Configs justierbar). ✅ Jede Währung braucht geplante **Quellen und Senken**. Das Economy-Dashboard soll Netto ≈ 0 zeigen, ein wachsendes Wallet bedeutet zu wenige Senken. ✅ Rebirth/Prestige ist ein bewährtes Langzeit-System (Pet Simulator 99 liefert pro großem Update „a new rebirth“), muss aber Neues freischalten und darf nicht bestrafen. 🟡/🧠

## Referenzbilder
Selbst erstellte, beschriftete Referenzbilder (frei nutzbar, Übersicht: `assets/bilder/README.md`).

![Progression: Wand und Rebirth](../assets/bilder/progression-kurve-rebirth.png)
![Sammelbuch mit Meilensteinen](../assets/bilder/ui-sammelbuch.png)

Offizielle Bilder aus der Roblox Creator Documentation (CC BY 4.0, Übersicht und Lizenz: `assets/bilder/offiziell/README.md`).

![XP-Kurve](../assets/bilder/offiziell/game-design/onboarding-progressionskurve.png)
*„XP Required to Level Up“: exponentiell steigende Kurve über Level 1–10. Frühe Level schnell erreichbar. Quelle: Roblox Creator Docs, CC BY 4.0 ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding))*

![Missionen als Progressionsmotor](../assets/bilder/offiziell/game-design/quests-missionen-progression.png)
*Dragon Adventures: Saison-Level, Fortschrittsbalken und gestaffelte Belohnungen. Quelle: Roblox Creator Docs, CC BY 4.0 ([Quest design](https://create.roblox.com/docs/production/game-design/introduction-to-quest-design))*

![Quests, Achievements, Dailies](../assets/bilder/offiziell/game-design/quests-achievements-dailies-matrix.png)
*Welche Ziele Quests, Achievements und Dailies jeweils abdecken. Quelle: Roblox Creator Docs, CC BY 4.0 ([Quest design](https://create.roblox.com/docs/production/game-design/introduction-to-quest-design))*

![Quellen und Senken](../assets/bilder/offiziell/analytics/economy-quellen-senken-gesamt.png)
*Gesamt-Quellen und -Senken nach Kategorie mit Netto-Linie. Quelle: Roblox Creator Docs, CC BY 4.0 ([Economy events](https://create.roblox.com/docs/production/analytics/economy-events))*

![Durchschnittliches Wallet](../assets/bilder/offiziell/analytics/economy-durchschnittliches-wallet.png)
*Wallet nach Zahlern/Nichtzahlern: Steigende Guthaben heißen zu wenige Senken. Quelle: Roblox Creator Docs, CC BY 4.0 ([Economy events](https://create.roblox.com/docs/production/analytics/economy-events))*

## Warum das wichtig ist
- „Without a progression system, a game becomes repetitive, boring, and shallow.“ ✅ ([Core loops](https://create.roblox.com/docs/production/game-design/core-loops))
- Progression lässt Inhalte länger halten, „so you have time to make more content before users unlock them“. ✅ ([Engagement](https://create.roblox.com/docs/production/analytics/engagement))
- Die Home-Empfehlung bewertet Spieltage in den Fenstern Tag 2–7 und Tag 8–28. Mittel- und Langzeitziele sind damit direkt reichweitenrelevant. ✅ ([Discovery](https://create.roblox.com/docs/discovery))

## Details

### 1. Offizielle Regeln für Progression ✅
Quelle: [Retention](https://create.roblox.com/docs/production/analytics/retention)
1. **Klare Ziele:** Kurzfristige Ziele geben sofortige Befriedigung, langfristige eine Richtung.
2. **Abwechslung:** neue Modi, Items, Social-Features.
3. **Schwierigkeit balancieren:** Zu schnell = Inhalt leer, zu langsam = Frust und Motivationsverlust.

Messung laut Doku:
- Progressionssystem benennen (Währung im Tycoon, Items im Sammelspiel, Skills im Magiespiel).
- **Spielerverteilung pro Level** messen. Die Doku schlägt vor, bei jedem Level-Up ein spezielles Item zu vergeben und so die Zeit pro Level zu messen.
- Aufgaben anpassen, wenn Spieler zu schnell oder zu langsam leveln.
- Praktischer: `LogProgressionEvent` / Progression-Funnel oder Custom Event mit Level als Custom Field. ✅ ([AnalyticsService](https://create.roblox.com/docs/reference/engine/classes/AnalyticsService)) Siehe `analytics-und-experimente.md`.

Onboarding-Progression ✅ ([Onboarding](https://create.roblox.com/docs/production/game-design/onboarding)):
- Progression „is felt when a player gets better, gains access to new systems, and achieves goals“.
- **XP-basiertes Leveln** mit **niedrigen Schwellen in den ersten Leveln**; mit **Configs** in Echtzeit glätten, ohne Server-Neustart.

Engagement-Doku ✅ ([Engagement](https://create.roblox.com/docs/production/analytics/engagement)):
- Aspirative Ziele: Pet-Sammlung vervollständigen, höchster Rang, seltenes Item.
- Progression nicht so bauen, dass sie den Spaß wegsperrt: genug Inhalt in der ersten Sitzung.

Monetarisierungs-Doku ✅ ([Monetization](https://create.roblox.com/docs/production/monetization)): Spieler sollen sich neue Inhalte **verdienen**. Wer ein Update nur betritt, ohne etwas erreicht zu haben, „may check out soon after“.

### 2. Progression-Typen
| Typ | Beispiel | Wirkung | Beleg |
|---|---|---|---|
| **Stat** | mehr Schaden, mehr Geld pro Klick | einfach, sofort spürbar | 🧠 |
| **Freischaltung** | neue Zone, neues Werkzeug, neues System | Neugier, Ziele | ✅ („gains access to new systems“) |
| **Sammlung** | Sets, Bücher, Katalog, Pet-Sammlung | Vollständigkeitsdrang | ✅ ([Engagement](https://create.roblox.com/docs/production/analytics/engagement)) |
| **Fertigkeit** | Spieler wird besser | Meisterschaft | ✅ („gets better“) |
| **Status** | Titel, Rang, Showcase | soziale Bedeutung | 🧠 |
| **Saison** | Season-Pass-Stufen | zeitlich begrenzte Ziele | ✅ (siehe `live-ops-events.md`) |
| **Narrativ** | Welt öffnet sich | emotionale Bindung | 🧠 |

### 3. Quests, Achievements und Dailies ✅
Quelle: [Quest design](https://create.roblox.com/docs/production/game-design/introduction-to-quest-design)
- **Dailies:** kurze Aufgaben mit bescheidenen Belohnungen, innerhalb von **24 Stunden** zu erledigen; gleiche oder rotierende Aufgaben; „exclusively short-term goals“.
- Dailies sind „an excellent delivery mechanism for currencies“: verlässlich, klein, wertvoll genug für tägliche Rückkehr (Resource Drip).
- Quests, Achievements und Dailies decken unterschiedliche Ziele ab (kurz-/mittel-/langfristig, Tutorial, Resource Drip, Narrativ). Bewusst kombinieren.

### 4. Die Kurve (🧠, mit offiziellem Anker)
- **Anfang:** schnell. Alle 30–60 Sekunden ein spürbarer Fortschritt. Offiziell: niedrige frühe XP-Schwellen. ✅
- **Mitte:** langsamer, aber mit Meilensteinen (neue Zone nach X Minuten).
- **Spät:** sehr langsam, dafür Rebirth/Prestige/Saison.
- Die offizielle Beispielkurve „XP Required to Level Up“ steigt **exponentiell** über Level 1–10. ✅ (Bild oben)

**Faustregel:** Kosten steigen exponentiell, Einkommen linear → Wand. Gegenmittel: Multiplikatoren, neue Einkommensquellen, Rebirth. 🧠

**Beispielrechnung (🧠, eigene Zahlen):**
| Level | XP-Bedarf (×1,5 pro Level) | XP kumuliert | Zeit kumuliert bei 60 XP/min |
|---|---|---|---|
| 1→2 | 20 | 20 | 20 s |
| 2→3 | 30 | 50 | 50 s |
| 3→4 | 45 | 95 | ~1,6 min |
| 4→5 | 68 | 163 | ~2,7 min |
| 5→6 | 101 | 264 | ~4,4 min |
| 9→10 | 513 | ~1.500 | ~25 min |
Lesart: Vier Level-Ups in den ersten ~3 Minuten decken das 61–180-s-Bounce-Fenster ab. ✅ ([Discovery](https://create.roblox.com/docs/discovery)) Ab Level 8–10 braucht es zusätzliche Einkommensquellen oder Multiplikatoren.

### 5. Wirtschafts-Gleichgewicht: Quellen und Senken
**Offizielle Regeln** ✅
- Jede Ressource braucht **Quellen** (verdienen) und **Senken** (ausgeben). Neue Quellen nur mit Plan, wie überschüssige Mengen wieder „versinken“. ([Balance virtual economies](https://create.roblox.com/docs/production/game-design/balance-virtual-economies))
- **Daten tracken:** wer was kauft, welche Aktionen Währung bringen, verdient vs. gekauft, ob verdiente oder gekaufte Währung für Käufe genutzt wird, wann welche Items genutzt werden. ([Balance virtual economies](https://create.roblox.com/docs/production/game-design/balance-virtual-economies))
- **Economy-Dashboard:** Gesamt-Quellen minus Senken „should be close to zero“. Wächst das Netto: mehr Senken. Wächst das Durchschnitts-Wallet, besonders bei Zahlern: neue Senken. Kaufen Spieler keine Währung per IAP: Preise senken oder neue Angebote. ([Economy events](https://create.roblox.com/docs/production/analytics/economy-events))
- Max. **5 Währungen** im Tracking einplanen (Doku widerspricht sich: 5 vs. 10). Varianten wie `WarriorXP`/`MageXP` als eine Währung plus Custom Field. ✅ ([Event types](https://create.roblox.com/docs/production/analytics/event-types); [AnalyticsService](https://create.roblox.com/docs/reference/engine/classes/AnalyticsService))

**Ökonomie-Tabelle (🧠 Vorlage)**
| Währung | Quellen (Rate/min) | Senken | Zielzeit für Ziel X | transactionType |
|---|---|---|---|---|
| Coins | Ernte 60/min, Daily 500 | Upgrades, Saatgut | 1. Upgrade in 1 min | Gameplay, TimedReward, Shop |
| Gems (Premium) | IAP, Achievements | Boosts, Kosmetik | – | IAP, Gameplay |
| Event-Token | Event-Aktionen | Event-Shop | Event-Item in 3–5 Tagen | Gameplay, Shop |

Typische Senken (🧠, teils ✅): Upgrades mit steigenden Kosten, Verbrauchsgüter, Kosmetik, Rebirth-Kosten, Gebühren beim Handel, Event-Shops (✅ [Balance virtual economies](https://create.roblox.com/docs/production/game-design/balance-virtual-economies)), sequenzielle Events, die Währung des vorigen Events verbrauchen (✅ ebd.).

### 6. Rebirth / Prestige
**Idee:** Spieler setzt Fortschritt zurück und erhält einen dauerhaften Bonus (Multiplikator, Zugang zu neuem Content). 🧠
**Warum es wirkt:** Der Neustart fühlt sich dank Bonus schneller an, es gibt ein Langzeitziel und einen Rückkehranker. 🧠
**Belege aus Spielen:**
- **Pet Simulator 99:** Ziel pro großem Update laut BIG Games: 25+ Gebiete, **ein neuer Rebirth**, Dutzende Pets, mehrere neue Mechaniken. 🟡 Studio-Post, Anfang 2024 ([BIG Games](https://www.biggames.io/post/pet-simulator-99-update-4))
- **Steal a Brainrot:** Rebirth verlangt Geld **plus einen bestimmten Brainrot**, verknüpft Rebirth also mit Sammeln und Stehlen. 🟡 ([Wikipedia](https://en.wikipedia.org/wiki/Steal_a_Brainrot); [BloxInformer](https://bloxinformer.com/wikis/steal-a-brainrot/))

**Gestaltung (🧠):**
- Erster Rebirth früh genug (z. B. nach 20–40 Minuten), damit das System verstanden wird. Zum Testen.
- Bonus **sichtbar und spürbar** (nicht +1 %).
- Rebirth schaltet **etwas Neues** frei (Zone, Pet-Slot, Fähigkeit), nicht nur Zahlen.
- Rückschritt nur kurz: Nach dem Rebirth sollte der vorherige Stand in einem Bruchteil der Zeit wieder erreicht sein.
- Stufen 1, 2, 3 … mit Meilensteinen und Titeln (Status-Progression).
- Neue Rebirth-Stufen als **Endgame-Content** in Updates nachliefern (siehe PS99). Das passt zur Doku-Empfehlung, Kadenz-Inhalte ans Ende der Progression zu setzen. ✅ ([Content updates](https://create.roblox.com/docs/production/game-design/content-updates))
- Rebirth mit Analytics messen: Anteil der Spieler mit Rebirth 1 nach 1/7/30 Tagen, Zeit bis Rebirth (Progression-Funnel).

### 7. Meilenstein-Planung (🧠 Beispiel)
| Zeit | Ziel | Belohnung | Bezug |
|---|---|---|---|
| < 1 min | erstes Upgrade | sofort spürbar | Bounce-Fenster ✅ |
| ≤ 5 min | Zone 2 / Spaß-Moment | neue Optik, neue Ressource | 5-Minuten-Regel ✅ |
| 15 min | erste Sammlung 3/10 | Sammelbuch sichtbar | – |
| 20–40 min | erster Rebirth | Multiplikator, neues Feature | – |
| Tag 2 | Dailies | Kosmetik/Booster | Spieltage Tag 2–7 ✅ |
| Woche 1 | neue Zone/Mechanik | Frische | D7 ✅ |
| Woche 2–4 | Saison-Rang, Endgame-Stufe | Titel, Skin | Tag 8–28 ✅ |

### 8. Fairness und Tempo
- **Nichtzahler müssen Ziele erreichen können.** Die Doku verlangt Wege zu Belohnungen für Nichtzahler (z. B. Free-Track im Season Pass). ✅ ([Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations))
- **Bezahl-Boosts beschleunigen, ersetzen aber nicht.** 🧠
- **Zeitlinien offenlegen:** Season-Pass-XP pro Level und Restzeit klar anzeigen. ✅ ([Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations))
- **Keine Wand ohne Hinweis:** Wenn etwas 20 Stunden dauert, braucht es Zwischenbelohnungen. 🧠
- Monetarisierung, die Spieler ablehnen, führt zu **Downvotes**. ✅ ([Monetization](https://create.roblox.com/docs/production/monetization))

## Beispiele aus echten Spielen
- **Pet Simulator 99:** Rebirths, Gebiete und limitierte Huge-Pets als wiederkehrendes Update-Paket. 🟡 ([BIG Games](https://www.biggames.io/post/pet-simulator-99-update-4))
- **Grow a Garden:** größere Beete und seltenere Pflanzen als Freischaltungs-Progression, Wetter-Mutationen als Wertmultiplikator. 🟡/🟠 ([Naavik](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/); [GAG Wiki](https://growagarden.fandom.com/wiki/Admin_Abuse))
- **Dragon Adventures, Jailbreak:** Missionen und Season-Stufen als sichtbarer Fortschritt. ✅ (Doku-Bilder)
- Mehr: `fallstudien.md`.

## Do / Don't
| Do | Don't |
|---|---|
| Frühe Level billig, live per Configs justieren | Erste Belohnung nach Minuten |
| Spürbare Sprünge (2×, neue Fähigkeit) | +1-%-Upgrades |
| Rebirth schaltet Neues frei | Rebirth = nur Zahlen |
| Quellen und Senken dokumentieren und tracken | Währungen ohne Senken |
| Spielerverteilung pro Level messen | Balancing nach Gefühl |
| Dailies als kleiner, verlässlicher Resource Drip | Dailies, die die ganze Spielzeit fressen |

## Checkliste
- [ ] Kurz-, mittel- und langfristige Ziele sichtbar
- [ ] Erste 5 Level in ≤ 3 Minuten erreichbar
- [ ] XP-Schwellen als Config (live änderbar)
- [ ] Ökonomie-Tabelle mit Quellen, Senken, Raten, Zielzeiten
- [ ] Economy-Events für alle Quellen/Senken, max. 5 Währungen
- [ ] Netto-Fluss ≈ 0, Wallet der Zahler beobachtet
- [ ] Rebirth: früh verständlich, spürbarer Bonus, schaltet Neues frei
- [ ] Nichtzahler erreichen jedes Kernziel

## Offene Fragen / Recherche-Bedarf
- Keine offiziellen Zahlen, wann der erste Rebirth idealerweise kommt. Wert (20–40 min) ist eine Testhypothese. 🧠
- Interne Rebirth-Daten von PS99 oder Steal a Brainrot sind nicht öffentlich.

## Quellen
- [Creator Docs: Retention](https://create.roblox.com/docs/production/analytics/retention) – Stand 2026-10-24, ✅
- [Creator Docs: Onboarding](https://create.roblox.com/docs/production/game-design/onboarding) – ✅
- [Creator Docs: Engagement](https://create.roblox.com/docs/production/analytics/engagement) – ✅
- [Creator Docs: Core loops](https://create.roblox.com/docs/production/game-design/core-loops) – ✅
- [Creator Docs: Quest design](https://create.roblox.com/docs/production/game-design/introduction-to-quest-design) – ✅
- [Creator Docs: Balance virtual economies](https://create.roblox.com/docs/production/game-design/balance-virtual-economies) – ✅
- [Creator Docs: Economy events](https://create.roblox.com/docs/production/analytics/economy-events) und [Event types](https://create.roblox.com/docs/production/analytics/event-types) – ✅
- [Creator Docs: Monetization](https://create.roblox.com/docs/production/monetization) und [Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations) – ✅
- [Creator Docs: Content updates](https://create.roblox.com/docs/production/game-design/content-updates) – ✅
- [BIG Games: Pet Simulator 99 Update 4](https://www.biggames.io/post/pet-simulator-99-update-4) – Anfang 2024, 🟡
- [Wikipedia: Steal a Brainrot](https://en.wikipedia.org/wiki/Steal_a_Brainrot) – 🟡
- [Naavik: Predicting the next big hits on Roblox](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/) – 2025, 🟡

## Verknüpfungen
`core-loops.md`, `gacha-und-luck.md`, `live-ops-events.md`, `analytics-und-experimente.md`, `07-monetarisierung/monetarisierung.md`
