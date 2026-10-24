# Einnahmequellen und Auszahlungen

> Stand: 2026-10-24 · Nächste Prüfung: 2026-11-24 · Gesamt-Vertrauen: ✅ für Sätze, Formeln und Regeln (gegen den Quelltext der Creator Docs vom 24.10.2026 geprüft), 🟡 für Plattform-Summen aus Presse und Finanzberichten, 🧠 für Rechenbeispiele und Folgerungen

Übersicht und Einstieg: `monetarisierung.md`. Preise und Shop: `preisgestaltung-und-shop-design.md`. Lootbox-Regeln und Recht: `ethik-und-recht.md`.

## Kurzfassung
- Passes und Developer Products bringen dem Creator **70 %** des Robux-Preises ✅ ([Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus)). Avatar-Items bringen dem Creator nur **30 %**, im Spiel verkauft bekommt der Spielbesitzer zusätzlich **40 %** ✅ ([Marketplace fees](https://create.roblox.com/docs/marketplace/marketplace-fees-and-commissions)).
- Der DevEx-Kurs liegt seit dem 5. September 2025 bei **0,0038 US-$ pro Earned Robux**, also 114 $ für 30.000 Robux. Ältere Guthaben werden zu **0,0035 $** und **zuerst** ausgezahlt ✅ ([Developer Exchange](https://create.roblox.com/docs/production/monetization/developer-exchange)).
- Seit dem 8. Juni 2026 gilt für Käufe verifizierter US-Erwachsener ein Kurs von **0,0054 $**. Voraussetzung ist, dass Spielerfiguren zu **100 % der aktiven Spielzeit R15** oder eigene Figuren sind ✅ ([U.S. 18+ exchange rate](https://create.roblox.com/docs/production/monetization/18-plus-devex-rate)).
- **Creator Rewards** hat am 24. Juli 2025 die Premium-Engagement-Auszahlungen ersetzt. Es zahlt 5 Robux pro Active Spender und Tag sowie 35 % der ersten 100 $ Käufe geworbener Neu- oder Rückkehrer ✅ ([Creator Rewards](https://create.roblox.com/docs/creator-rewards)).
- 2025 zahlte Roblox **1,503 Mrd. $** über DevEx aus (2024: 922,8 Mio. $), an mehr als 23.500 Creator ✅ ([10-K FY2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm)).

## Warum das wichtig ist
Wer die Auszahlungslogik kennt, baut andere Spiele. Drei Beispiele 🧠:
- Der 18+-Kurs zahlt 42 % mehr, aber nur in reinen R15-Spielen. Diese Entscheidung fällt beim Figuren-Design, nicht erst beim Shop.
- Creator Rewards zahlt für Spiele, die zahlende Stammspieler **früh am Tag** und **mindestens 10 Minuten** spielen. Tägliche Gewohnheit lohnt sich also direkt.
- Avatar-Items im eigenen Spiel bringen dem Spielbesitzer 40 %, selbst wenn er das Item nicht gemacht hat. Ein Kleiderladen im Spiel ist damit eine echte Einnahmequelle.

## Referenzbilder
Selbst erstellte und offizielle Referenzbilder (Übersicht: `assets/bilder/README.md` und `assets/bilder/offiziell/README.md`).

![Monetarisierung: Produkte und Fairness](../assets/bilder/monetarisierung-produkte.png)
*Selbst erstellt: Produkttypen und Fairness-Regeln im Überblick.*

![Neue-Nutzer-Funnel nach Akquisequelle](../assets/bilder/offiziell/analytics/akquise-neue-nutzer-funnel.png)
*„New users funnel“ nach Quelle (Home, Suche, Freunde, Sponsored Ads …) mit Conversion, D7, Spielzeit und Umsatz. Für Audience-Expansion-Rewards zählen nur Share Link, Direktlink und Suche nach dem Spielnamen. Quelle: Roblox Creator Docs, CC BY 4.0 ([Acquisition](https://create.roblox.com/docs/production/analytics/acquisition))*

![Benchmark-Scorecard](../assets/bilder/offiziell/analytics/benchmark-scorecard-uebersicht.png)
*Scorecard mit Payer Conversion und ARPPU gegen ähnliche Spiele. Quelle: Roblox Creator Docs, CC BY 4.0 ([Analytics](https://create.roblox.com/docs/production/analytics))*

---

## 1. Alle Einnahmequellen auf einen Blick

| Quelle | Wer zahlt | Anteil für dich | Haltefrist | Quelle |
|---|---|---|---|---|
| **Pass** (Einmalkauf) | Spieler, Robux | 70 % ✅ | ca. 5 Tage ✅ | [Plus](https://create.roblox.com/docs/production/monetization/roblox-plus), [Subscriptions](https://create.roblox.com/docs/production/monetization/subscriptions) |
| **Developer Product** (mehrfach) | Spieler, Robux | 70 % ✅ | ca. 5 Tage ✅ | wie oben |
| **Subscription in Robux** | Spieler, monatlich | 70 % jeden Monat ✅ | ca. 5 Tage ✅ | [Subscriptions](https://create.roblox.com/docs/production/monetization/subscriptions) |
| **Subscription in Landeswährung** | Spieler, monatlich | 70 % im 1. Monat, danach 100 % ✅ | 30 Tage ✅ | [Subscriptions](https://create.roblox.com/docs/production/monetization/subscriptions) |
| **Private Server** | Spieler, monatlich Robux | eigener Preis; Plus-Ersatz bis 100 Robux ✅ | – | [Private servers](https://create.roblox.com/docs/production/monetization/private-servers) |
| **Paid Access in Robux** | Spieler, einmalig | Anteil nicht dokumentiert | bis 7 Tage ✅ | [Paid access (Robux)](https://create.roblox.com/docs/production/monetization/paid-access-robux) |
| **Paid Access in Landeswährung** | Spieler, einmalig | 50 / 60 / 70 % je Preisstufe ✅ | mind. 60 Tage, monatliche Auszahlung ✅ | [Paid access (lokal)](https://create.roblox.com/docs/production/monetization/paid-access-local-currency) |
| **Avatar-Item, Marketplace** | Spieler | 30 % (progressiv bis 70 %) ✅ | 30 Tage ✅ | [Marketplace fees](https://create.roblox.com/docs/marketplace/marketplace-fees-and-commissions) |
| **Avatar-Item, im Spiel verkauft** | Spieler | Creator 30 % + Spielbesitzer 40 % ✅ | 30 Tage ✅ | wie oben |
| **Creator Rewards** | Roblox | 5 Robux/Tag/Active Spender; 35 % auf max. 100 $ ✅ | 60 Tage ✅ | [Creator Rewards](https://create.roblox.com/docs/creator-rewards) |
| **Roblox Plus: Abo-Werbung** | Roblox | 250 Robux/Monat × 3 = bis 750 ✅ | 60 Tage ✅ | [Plus](https://create.roblox.com/docs/production/monetization/roblox-plus) |
| **Roblox Plus: private Server** | Roblox | 70 % des Serverpreises, max. 100 Robux ✅ | – | [Plus](https://create.roblox.com/docs/production/monetization/roblox-plus) |
| **Robux-Transfers** | Plus-Abonnent | 10 % jedes Transfers ✅ | – | [Robux transfers](https://create.roblox.com/docs/production/monetization/robux-transfers) |
| **Rewarded Video Ads** | Werbekunden | EPM × Impressionen / 1000 ✅ (Satz nicht veröffentlicht) | – | [Rewarded video ads](https://create.roblox.com/docs/production/promotion/rewarded-video-ads) |
| **Immersive Ads** | Werbekunden | je Ansicht/Impression/Teleport ✅ | Auszahlung am 25. des Folgemonats ✅ | [Immersive ads](https://create.roblox.com/docs/production/monetization/immersive-ads) |
| **Commerce (Shopify)** | Spieler, echtes Geld | Split nicht dokumentiert | – | [Commerce products](https://create.roblox.com/docs/production/monetization/commerce-products) |
| **Creator Store** (Modelle, Plugins) | andere Creator, US-$ | 100 % abzüglich Steuern und Zahlungsgebühren ✅ | 30 Tage ✅ | [Monetization](https://create.roblox.com/docs/production/monetization) |

**Hinweis zur 70-%-Regel ✅:** Weder die Pass- noch die Developer-Product-Seite nennt die Gebühr direkt. Die 70 % stehen in der Plus-Tabelle: „Non-subscriber … 100 … 70 … 70%“ ([Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus)). Ältere Fassungen dieser Datenbank führten die 30-%-Gebühr deshalb als 🟠. Sie ist jetzt indirekt offiziell belegt.

---

## 2. Developer Exchange (DevEx)

### 2.1 Kurse

| Kurs | Wert pro Earned Robux | 30.000 Robux | 100.000 Robux | 1.000.000 Robux | Gilt für |
|---|---|---|---|---|---|
| Alt (bis 5.9.2025, 10 Uhr PT) | 0,0035 $ ✅ | 105 $ ✅ | 350 $ 🧠 | 3.500 $ 🧠 | Robux, die vor dem Stichtag verdient wurden |
| Standard (seit 5.9.2025) | 0,0038 $ ✅ | 114 $ ✅ | 380 $ 🧠 | 3.800 $ 🧠 | alle anderen Earned Robux |
| US 18+ (seit 8.6.2026) | 0,0054 $ ✅ | 162 $ 🧠 | 540 $ 🧠 | 5.400 $ 🧠 | Passes, Developer Products, Subscriptions, private Server von altersverifizierten US-Erwachsenen in berechtigten Spielen |

Quellen: [Developer Exchange](https://create.roblox.com/docs/production/monetization/developer-exchange), [U.S. 18+ exchange rate](https://create.roblox.com/docs/production/monetization/18-plus-devex-rate). Roblox nennt die Erhöhung „8.5% more“ ✅ ([Roblox Newsroom RDC 2025](https://about.roblox.com/newsroom/2025/09/roblox-rdc-2025)). Der 18+-Kurs liegt 42 % über dem Standardkurs ✅ ([Roblox Newsroom April 2026](https://about.roblox.com/newsroom/2026/04/roblox-fuels-high-fidelity-games-over-18-players-increases-qualifying-devex-rate-42)).

### 2.2 Rechenbeispiel: 100.000 Robux vor und nach September 2025 🧠

| Szenario | Rechnung | Auszahlung |
|---|---|---|
| A: alles vor dem 5.9.2025 verdient | 100.000 × 0,0035 | **350,00 $** |
| B: alles danach verdient | 100.000 × 0,0038 | **380,00 $** (+30 $, +8,6 %) |
| C: alles aus 18+-berechtigten US-Käufen | 100.000 × 0,0054 | **540,00 $** (+42 % ggü. B) |
| D: gemischt, 60.000 alt + 40.000 neu | 60.000 × 0,0035 + 40.000 × 0,0038 = 210 + 152 | **362,00 $** |
| E: wie D, aber nur 50.000 auszahlen | Altguthaben zuerst: 50.000 × 0,0035 | **175,00 $** (Rest: 10.000 alt + 40.000 neu) |

Regel hinter Zeile E ✅: „You can only cash out your Earned Robux at the old exchange rate before you can cash out any Earned Robux at the current exchange rate.“ Wer Robux ausgibt, baut das Altguthaben **nicht** zuerst ab ([Developer Exchange](https://create.roblox.com/docs/production/monetization/developer-exchange)). Das erklärt DevForum-Berichte, nach denen Auszahlungen im November 2025 noch zum alten Kurs liefen 🟠 ([DevForum „DevEx rate Confusion“](https://devforum.roblox.com/t/devex-rate-confusion/4717348)).

**Widerspruch in der Doku ✅:** Die DevEx-Seite sagt „altes Guthaben zuerst“. Die 18+-Seite sagt, DevEx-Anfragen und Gruppen-Auszahlungen „prioritize the U.S. 18+ DevEx rate“ ([U.S. 18+ exchange rate](https://create.roblox.com/docs/production/monetization/18-plus-devex-rate)). Welche der beiden Regeln gewinnt, wenn jemand sowohl Altguthaben als auch 18+-Robux hat, steht nirgends. Eine Help-Center-Zusammenfassung nennt die Reihenfolge 18+ → Altguthaben → Rest 🟡 ([Roblox Help: DevEx](https://en.help.roblox.com/hc/en-us/articles/13061189551124-Developer-Exchange-Help-and-Information-Page), nur als Suchauszug gesehen).

### 2.3 Rechenbeispiel: vom Pass-Kauf zum Dollar 🧠
Ein Spieler kauft einen Pass für 400 Robux.

| Schritt | Standard | US 18+ |
|---|---|---|
| Robux-Preis | 400 | 400 |
| Dein Anteil (70 %) | 280 Earned Robux | 280 Earned Robux |
| × DevEx-Kurs | × 0,0038 | × 0,0054 |
| **Auszahlung** | **1,06 $** | **1,51 $** |
| Mit Plus-Rabatt 20 % (Spieler zahlt 320) | weiterhin 280 Robux → 1,06 $ | 1,51 $ |

Plattformweit kamen 2025 rund **22 %** der Bookings als DevEx-Geld bei Creators an: 1,503 Mrd. $ DevEx ✅ ([10-K](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm)) geteilt durch 6,8 Mrd. $ Bookings 🟡 ([Naavik](https://naavik.co/deep-dives/the-state-of-ugc-games-2026/)). Eine Bank schätzte den künftigen DevEx-Anteil auf grob 23,4 % 🟡 ([Benzinga](https://www.benzinga.com/analyst-stock-ratings/reiteration/25/09/47551437/roblox-analysts-cheer-developer-payout-hike-see-path-to-stronger-growth)). Faustregel 🧠: Von einem Dollar, den ein Spieler in Robux umtauscht und in deinem Spiel ausgibt, landet grob ein Fünftel als Bargeld bei dir.

### 2.4 Was als Earned Robux zählt ✅

| Zählt | Zählt nicht |
|---|---|
| Verkäufe von Developer Products, Passes, Subscriptions | direkt gekaufte Robux |
| Gebühren aus In-Game-Käufen von Marketplace-Items | monatliche Robux aus einem Roblox-Abo |
| Gebühren aus Robux-Transfers (Transfers API) | Handel oder Weiterverkauf von Items |
| bezahlte private Server, Paid Access in Robux | Robux, die man per Transfer **empfangen** hat |
| Roblox-Plus-Anreize, Werbeeinnahmen im Spiel | eingelöste Geschenkkarten |
| Modelle und Plugins im Creator Store | Passes in Template-Spielen ohne echte Besucher |
| Avatar-Items im Marketplace, Creator Rewards | Einnahmen aus moderierten, regelwidrigen Inhalten |

Quelle: [Developer Exchange](https://create.roblox.com/docs/production/monetization/developer-exchange). Roblox entscheidet im Zweifel allein, was zählt.

### 2.5 Voraussetzungen und Ablauf ✅
- Mindestens **13 Jahre** alt.
- Mindestens **30.000 Earned Robux** auf dem Konto.
- **Verifizierte E-Mail-Adresse**.
- Gültiges Konto im **DevEx-Portal** (Tipalti).
- Steuerformular **W-9** (US) oder **W-8** (alle anderen) hinterlegt.
- Einhaltung von Nutzungsbedingungen und Community Standards.
- **Premium ist nicht nötig.** Die Pflicht entfiel Anfang 2022 ✅ ([DevForum](https://devforum.roblox.com/t/developer-exchange-program-requirements-changes/1651282)). SEO-Seiten, die 2026 noch 100.000 Robux Minimum und Premium verlangen, sind veraltet 🟠 ([rolearn.dev](https://rolearn.dev/guidance/roblox-devex-requirements-2026/)).

Quelle für die Liste: [Developer Exchange](https://create.roblox.com/docs/production/monetization/developer-exchange).

**Ablauf ✅:** Creator Hub → Finances → Cash Out. Nur den echten Namen verwenden. Nach der ersten Genehmigung kommt eine Einladung ins Tipalti-Portal. Wer sich dort **nicht innerhalb einer Woche** registriert, bekommt die Anfrage abgelehnt und die Robux zurück. Bearbeitung: erstmalig etwa **10 Werktage**, danach etwa **5 Werktage**, ohne Wochenenden. Eine abgeschickte Anfrage lässt sich nicht stornieren. Das DevEx-Dashboard zeigt den Stand mit bis zu 24 Stunden Verzögerung ([Developer Exchange](https://create.roblox.com/docs/production/monetization/developer-exchange)).

### 2.6 Steuern: Frist 31. Oktober 2026 ✅
Ab dem **1. November 2026** gelten DevEx-Zahlungen als **Lizenzgebühren (royalties)** ([Tax information](https://create.roblox.com/docs/production/monetization/tax-information)).

| Fall | Einbehalt |
|---|---|
| US-Creator mit gültigem W-9 | kein Einbehalt ✅ |
| US-Creator ohne gültige Steuernummer (TIN) | 24 % Backup Withholding ✅ |
| Nicht-US-Creator mit gültigen Angaben bis 31.10.2026 | **0–30 %** nur auf den Anteil aus Verkäufen an US-Spieler, je nach Land und Abkommen ✅ |
| Nicht-US-Creator ohne gültige Angaben | **24 %** auf die **gesamte** Auszahlung möglich ✅ |

Quelle: [Tax information](https://create.roblox.com/docs/production/monetization/tax-information). Maßgeblich ist das Auszahlungsdatum, nicht das Antragsdatum. Einbehaltene Steuern sind laut Doku keine Gebühr, sondern vorausgezahlte Einkommensteuer.
🧠 Für Creator in Deutschland: Ein reduzierter Satz setzt ein gültiges W-8 mit Steuer-ID und ausdrücklichem Abkommens-Antrag voraus. Welcher Satz konkret gilt, mit einer Steuerberatung klären. Die Datenbank gibt keine Steuerberatung.

---

## 3. US-18+-DevEx-Kurs im Detail ✅

| Bedingung | Offizielle Regel |
|---|---|
| Käufer | US-Spieler, per Gesichts-Altersschätzung oder Ausweis als 18+ verifiziert |
| Produkte | Developer Products, Passes, Subscriptions, private Server |
| Nicht genannt | Avatar-Items, Paid Access, Creator Rewards |
| Spielerfiguren | 100 % der aktiven Spielzeit als R15 (Standard oder Advanced), eigene Menschenform oder eigene Nicht-Menschenform |
| R6 | „If a player can spawn into or swap to a R6 avatar at any point during active playtime, your game is **not eligible**“ |
| Animationspakete | müssen R15 sein |
| Eigene Menschenform | etwa 1 Kopf, 2 Arme, 2 Beine; 12 Gliedmaßenteile oder -gelenke gleichmäßig verteilt; Torso mit mind. 2 Teilen/Gelenken; FAQ: 15+ Teile **oder** 15+ Gelenke reichen |
| Ohne Spielfigur | Top-down-Strategie usw. gilt als Nicht-Menschenform und qualifiziert |
| NPCs | werden nicht geprüft |
| Einstellung in Studio | Avatar → Settings → „R15 Only“ |
| Kontrolle | laufende Hintergrundprüfung; bei Verstoß bis zur Behebung nicht berechtigt |

Quelle: [U.S. 18+ exchange rate](https://create.roblox.com/docs/production/monetization/18-plus-devex-rate).

**Korrektur gegenüber der Presse ✅:** Der Newsroom sprach von „select in-game items“, das DevForum schloss Avatar-Items aus ([DevForum](https://devforum.roblox.com/t/introducing-the-us-18-devex-rate-earn-42-more-on-spend-from-18-us-players/4607091)). Die Doku nennt ausdrücklich Developer Products und keine Avatar-Items. Die Community-Behauptung zur R15-Pflicht ([devex.gg](https://devex.gg/18-plus-devex-rate)) ist bestätigt.

**Rechenbeispiel 🧠:** Ein Spiel verdient im Monat 500.000 Robux aus Passes und Developer Products, davon 20 % (100.000) von verifizierten US-Erwachsenen.
- Reines R15-Spiel: 100.000 × 0,0054 + 400.000 × 0,0038 = 540 + 1.520 = **2.060 $**.
- Spiel mit R6-Option: 500.000 × 0,0038 = **1.900 $**.
- Unterschied: 160 $ pro Monat oder **+8,4 %**. Der Hebel wächst mit dem Anteil erwachsener US-Käufer.

---

## 4. Creator Rewards (seit 24. Juli 2025) ✅
Ersetzt **Engagement-Based Payouts** (Premium-Spielzeit) und das **Creator-Affiliate-Programm**. Keine Anmeldung nötig, keine Obergrenze ([Creator Rewards](https://create.roblox.com/docs/creator-rewards); [Engagement-based payouts](https://create.roblox.com/docs/production/monetization/engagement-based-payouts); [DevForum](https://devforum.roblox.com/t/introducing-creator-rewards-earn-more-by-growing-the-community/3777628)).

### 4.1 Begriffe ✅

| Begriff | Offizielle Definition (übersetzt) |
|---|---|
| Active Spender | Nutzer, der in den letzten 60 Tagen Qualifying Purchases von **mind. 9,99 $** gemacht hat und in diesen 60 Tagen kein New oder Reactivated User war |
| Qualifying Purchases | Kauf von Robux, Roblox Premium oder UGC-Abos |
| New User | ganz neu auf Roblox, kein Zweitkonto, nicht über eine Roblox-Werbekampagne gekommen |
| Lapsed User | 60 aufeinanderfolgende Tage nicht eingeloggt |
| Reactivated User | Lapsed User, der wieder spielt, nicht über eine Roblox-Kampagne |

Quelle: [Creator Rewards](https://create.roblox.com/docs/creator-rewards). Kleiner Widerspruch: Die FAQ derselben Seite beschreibt Active Spender als Nutzer, die „seit mindestens 60 Tagen aktiv“ sind. Das ist nicht ganz dasselbe wie „in den letzten 60 Tagen kein Neu- oder Rückkehrer“.

### 4.2 Daily Engagement: 5 Robux pro Spieler und Tag ✅
Formel: **5 Robux**, wenn ein Active Spender das Spiel an einem Tag **mindestens 10 Minuten** spielt **und** es zu den **ersten drei** Spielen gehört, die er an diesem Tag startet. Minuten innerhalb eines Tages werden addiert.

Offizielles Beispiel 2: Reihenfolge A (2 min), B (10), C (15), D (5), E (15), A (15). A (17 min), B und C bekommen je 5 Robux. D hat zu wenig Minuten. E war das vierte Spiel und bekommt trotz 15 Minuten nichts ([Creator Rewards](https://create.roblox.com/docs/creator-rewards)).

**Rechenbeispiel 🧠** für ein Spiel mit 20.000 DAU:

| Annahme | Wert |
|---|---|
| Anteil Active Spender unter den DAU | 10 % → 2.000 |
| davon „unter den ersten drei“ und 10+ min | 60 % → 1.200 |
| Robux pro Tag | 1.200 × 5 = 6.000 |
| Robux pro 30 Tage | 180.000 |
| in US-$ (0,0038) | **684 $ pro Monat** |

Die beiden Prozentwerte sind Annahmen. Den echten Wert zeigt das Dashboard unter Monetization → Creator Rewards als „Daily rewarded active spenders“ mit Benchmark (50.–90. Perzentil) ✅ ([Creator Rewards](https://create.roblox.com/docs/creator-rewards)).

### 4.3 Audience Expansion: 35 % der ersten 100 $ ✅
Formel: **35 % Umsatzbeteiligung** auf die ersten **100 $** Qualifying Purchases eines geworbenen New oder Reactivated Users, **überall auf Roblox**, in seinen ersten **60 Tagen**. Maximal also **35 $ Gegenwert pro geworbenem Nutzer** 🧠.

Drei Wege der Zuordnung, jeweils mit **10+ Minuten am selben Tag** und Ø **100+ DAU** des Spiels in den 60 Tagen nach dem Beitritt:
1. Klick auf den **Share Link** des Spiels, der zum Beitritt oder zur Rückkehr führt.
2. Klick auf den **Direktlink**, der zur ersten Sitzung des Tages führt (ohne Share-Link-Nutzer).
3. **Suche nach dem genauen Spielnamen**, die zur ersten Sitzung des Tages führt (ohne Share-Link-Nutzer).

Weitere Regeln: Bei Nutzern, die schon einmal reaktiviert wurden, werden frühere Käufe abgezogen. Pro Nutzer gibt es nur eine Belohnung. Zweitkonten werden über Geräte-ID, IP und Zahlungsdaten erkannt. Audience Expansion setzt ein **ID-verifiziertes Konto** voraus. Paid-Access-Spiele sind berechtigt. Alle Creator Awards kommen als Earned Robux mit **60 Tagen Haltefrist** ([Creator Rewards](https://create.roblox.com/docs/creator-rewards)).

**Korrektur ✅:** Das Fenster beträgt **60 Tage**. Frühe Ankündigungen nannten „zwei Monate“ ([DevForum](https://devforum.roblox.com/t/introducing-creator-rewards-earn-more-by-growing-the-community/3777628)). **Widerspruch in der Doku:** Die Share-Link-Kennzahlen derselben Seite sprechen weiter von „first two months“.
**Offene Lücke:** Wie die 35 % in Robux umgerechnet werden, steht nicht in der Doku.

**Rechenbeispiel 🧠** (Gegenwert in US-$, Umrechnung in Robux unbekannt):

| Annahme | Wert |
|---|---|
| Neue Nutzer über TikTok-Share-Link, die 10+ min spielen | 1.000 |
| davon kaufen in 60 Tagen | 5 % → 50 |
| Ø Qualifying Purchases je Käufer | 20 $ |
| Belohnung | 50 × 20 $ × 35 % = **350 $ Gegenwert** |
| Obergrenze bei 50 Käufern | 50 × 35 $ = 1.750 $ |

Folgerung 🧠: Audience Expansion belohnt eigenes Marketing außerhalb von Roblox (Videos, Discord, Creator). Ein Share Link pro Kanal macht die Quellen messbar.

### 4.4 Verboten ✅
Bots und automatisierte Besuche, manipulierte Teleports, Aufforderungen zu Zweitkonten, Vortäuschen einer Roblox-Zugehörigkeit, Konten mit sehr hoher Rückbuchungsquote. Folgen: verfallene Belohnungen, Ausschluss, Kontosperre ([Creator Rewards](https://create.roblox.com/docs/creator-rewards)).

---

## 5. Roblox Plus (seit 30. April 2026)
Plus kostet **4,99 $ pro Monat** und ersetzt Premium für Neuabschlüsse ✅ ([Roblox Newsroom](https://about.roblox.com/newsroom/2026/04/introducing-roblox-plus-subscription)). Der Preis steht nicht in der Creator-Doku.

### 5.1 Rabatte, die Roblox bezahlt ✅

| Nutzer | Itempreis | Spieler zahlt | Roblox legt drauf | Du bekommst | Effektiver Anteil |
|---|---|---|---|---|---|
| ohne Plus | 100 | 100 | – | 70 | 70 % |
| Plus, Monat 1–2 (10 %) | 100 | 90 | 10 | 70 | 78 % |
| Plus, ab Monat 3 (20 %) | 100 | 80 | 20 | 70 | 88 % |

Quelle: [Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus). Rabattiert werden Developer Products, Passes, Subscriptions im Spiel, Paid-Access-Spiele und Avatar-Items. Nicht rabattiert: Items über 1.000.000 Robux, Marketplace-Gebühren, Werbeguthaben, Gruppengebühren. Wer kündigt und neu abschließt, startet wieder bei 10 %.
**Technikfolge ✅:** Fest im UI eingetragene Preise zeigen Plus-Nutzern den falschen Betrag. Preise mit `GetProductInfoAsync` lesen, Rabatte stehen in `PriceDiscountDetails`.

### 5.2 Plus-Abschlüsse aus dem Spiel ✅
**250 Robux pro Monat** für die ersten drei aufeinanderfolgenden Monate, also **bis 750 Robux** pro neuem Abonnent. Bezahlt wird nur, wenn der Abschluss über `PromptRobloxSubscriptionPurchase` in deinem Spiel kam und das Abo bezahlt ist; Gratis-Testphasen zählen nicht. 60 Tage Haltefrist ([Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus)).
Rechnung 🧠: 750 Robux × 0,0038 = **2,85 $** pro gewonnenem Abonnent über drei Monate. 100 Abschlüsse ergeben 285 $.

### 5.3 Plus-Ersatz für bezahlte private Server ✅
Plus-Abonnenten bekommen bezahlte private Server gratis. Dafür zahlt Roblox: Hat der Abonnent **mindestens 60 Minuten in 30 Tagen** in dem privaten Server verbracht, den er **selbst** in deinem Spiel erstellt hat, bekommst du **70 % des Serverpreises, höchstens 100 Robux**. Geprüft wird am Verlängerungstag über die **fünf** meistgenutzten privaten Server des Abonnenten, auch wenn er kündigt. Die Zeit eingeladener Freunde zählt nicht. Testphasen-Abonnenten zählen hier mit ([Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus)).

Offizielles Beispiel:

| Server | Preis | Zeit (30 Tage) | Dein Ertrag |
|---|---|---|---|
| A | 100 Robux | 120 min | 70 Robux |
| B | 200 Robux | 80 min | 100 Robux (gedeckelt) |
| C | 50 Robux | 70 min | 35 Robux |
| D | 60 Robux | 15 min | 0 (unter 60 min) |
| E | 70 Robux | 10 min | 0 |
| **Summe** | | | **205 Robux** |

Folgerung 🧠: Ein Preis über **143 Robux** bringt bei Plus-Nutzern nichts mehr, weil 70 % davon schon 100 Robux sind. Bei normalen Käufern zählt der volle Preis. Spiele mit Gruppen-Spiel sollten private Server anbieten, sonst entgeht ihnen diese Zahlung.

---

## 6. Subscriptions im Spiel ✅

| Merkmal | In Robux | In Landeswährung |
|---|---|---|
| Wer darf | alle Creator | Konto per Ausweis oder Telefon verifiziert |
| Plattformen | alle | Web, App Store, Google Play |
| Länder | alle | nicht in Argentinien, China, Kolumbien, Indien, Indonesien, Japan, Russland, Taiwan, Türkei, VAE, Ukraine, Vietnam |
| Preis | beliebig ab **49 Robux** | **2,99 / 4,99 / 7,99 / 9,99 / 14,99 $** |
| Regionale Preise | immer an, nicht abschaltbar | nicht verfügbar |
| Auszahlung | **70 %** jeden Monat | **70 %** im 1. Monat, danach **100 %** |
| Umrechnung | – | 0,01 $ = 1 Robux (nach Plattformgebühren) |
| Haltefrist | ca. 5 Tage | 30 Tage |
| Preisänderung | alle **60 Tage**; Erhöhung erst nach 30 Tagen Vorwarnung | **nicht möglich**, nur löschen und neu anlegen |
| Rückerstattung | keine | über Bank/App-Store; innerhalb der Haltefrist entfällt deine Zahlung, danach wird sie abgezogen |

Quelle: [Subscriptions](https://create.roblox.com/docs/production/monetization/subscriptions). Weitere Regeln: mehrere Abos pro Spiel können gleichzeitig laufen, sich gegenseitig ausschließende Abos gibt es nicht. Abos können nicht spielübergreifend verkauft werden. Bezahlte Vorteile dürfen nicht an Zusatzaufgaben wie Social-Media-Posts geknüpft werden; Battle Passes als Abo sind erlaubt. Wer ein Landeswährungs-Abo löscht, muss allen aktiven Abonnenten erstatten.

**Widerspruch in der Doku ✅:** Die Design-Seite rechnet nur mit vier Preisstufen (2,99 / 4,99 / 7,99 / 14,99 $) und lässt 9,99 $ weg ([Subscription design](https://create.roblox.com/docs/production/game-design/subscription-design)). Die technische Seite nennt fünf. Gültig ist die technische Seite.

**Rechenbeispiel: 12 Monate Abo 🧠** (nach dem offiziellen 5-$-Beispiel: 350 Robux, dann 500)

| Modell | Monat 1 | Monat 2–12 | Summe 12 Monate | in $ (0,0038) |
|---|---|---|---|---|
| Landeswährung 5 $ | 350 | 11 × 500 | **5.850 Robux** | 22,23 $ |
| Robux-Abo 500 Robux | 350 | 11 × 350 | **4.200 Robux** | 15,96 $ |

Bei langen Laufzeiten zahlt das Landeswährungs-Abo deutlich mehr. Dafür ist es in zwölf Ländern nicht verfügbar, nicht regional bepreist und im Preis nicht änderbar. Ein Robux-Abo erreicht dagegen alle Länder.

---

## 7. Private Server, Paid Access, Transfers

### 7.1 Private Server ✅
- Monatliche Robux-Gebühr oder kostenlos. Das Spiel muss öffentlich sein.
- **Eine Preisänderung kündigt alle aktiven Abos.** Spieler bekommen eine Nachricht.
- Private Server und Paid Access schließen sich gegenseitig aus.
- Kinder unter 13 können je nach Elterneinstellungen eventuell nicht beitreten.
- Regionale Preise gelten automatisch ([Managed pricing](https://create.roblox.com/docs/production/monetization/managed-pricing)).

Quelle: [Private servers](https://create.roblox.com/docs/production/monetization/private-servers). Die Doku nennt keinen eigenen Prozentsatz für private Server. Aus dem Plus-Beispiel („70% revenue share on a 100 Robux server price“) lässt sich 70 % ableiten 🟡.
Designhinweis ✅: Private Server nicht so teuer machen, dass Freundesgruppen abgeschreckt werden ([Design for Roblox](https://create.roblox.com/docs/production/game-design/design-for-roblox)).

### 7.2 Paid Access ✅

| | In Robux | In Landeswährung |
|---|---|---|
| Voraussetzung | verifizierte E-Mail, Konto mind. 30 Tage alt | verifizierte E-Mail, 13+ mit Ausweis-Verifikation, Wohnsitz in einem Tipalti-Land |
| Preis | **25–1.000 Robux** | **9,99 $ → 50 %**, **29,99 $ → 60 %**, **49,99 $ → 70 %** Anteil |
| Kauf möglich | Desktop, Mobil, VR, die meisten Konsolen | nur Desktop und Web (spielen auf allen freigegebenen Geräten) |
| Auszahlung | Escrow bis 7 Tage | Escrow mind. 60 Tage, einmal monatlich über Tipalti, nur an den Gruppenbesitzer |
| Rückerstattung | keine | – |
| Demo-Modus | – | ja, Besitz prüfen mit `PlayerOwnsAssetAsync` |

Quellen: [Paid access (Robux)](https://create.roblox.com/docs/production/monetization/paid-access-robux), [Paid access (lokal)](https://create.roblox.com/docs/production/monetization/paid-access-local-currency).
Rechnung 🧠, vor Steuern und Mehrwertsteuer: 9,99 $ → ca. 5,00 $; 29,99 $ → ca. 17,99 $; 49,99 $ → ca. 34,99 $ pro Verkauf.
Regel ✅: Bei Paid Access in Landeswährung darf kein weiterer Robux-Eintritt für Spielteile verlangt werden. Passes und Developer Products sind erlaubt.

### 7.3 Robux-Transfers (Transfers API) ✅
- **Nur Plus-Abonnenten** dürfen senden, **10–500 Robux** pro Transfer.
- Das Spiel erhält **10 %**, der Empfänger **90 %**. Roblox nimmt keine Gebühr.
- Deine 10 % sind DevEx-berechtigt. Was der Empfänger bekommt, ist **nicht** DevEx-berechtigt.
- API: `PromptRobuxTransferAsync` (Server) und `BindReceiptHandler` mit `RobuxTransferSender` und `RobuxTransferReceiver`. Belohnungen erst nach verarbeitetem Beleg vergeben.
- Hintergrund: **spielübergreifende Verkäufe** von Passes und Developer Products wurden zum **30. Mai 2026** abgeschaltet. Transfers ersetzen das alte „Spenden über fremde Passes“.

Quellen: [Robux transfers](https://create.roblox.com/docs/production/monetization/robux-transfers), [Passes](https://create.roblox.com/docs/production/monetization/passes). **Korrektur:** Frühere Notizen nannten den 29. Mai und „alle Spieler dürfen senden“.
Kleiner Doku-Widerspruch: Die Plus-Seite bewirbt Transfers „at no cost to sender or recipient“, zugleich erhält der Empfänger nur 90 %.
Rechnung 🧠: 500 Robux Transfer → 50 Robux für das Spiel → 0,19 $.

---

## 8. Werbung

### 8.1 Rewarded Video Ads ✅

| Punkt | Offizielle Regel |
|---|---|
| Spiel | öffentlich und uneingeschränkt, keine freie Nutzererstellung, geprüfter Maturity-Fragebogen, Ø **2.000 einzigartige Besucher pro Monat** |
| Publisher | 13+, guter Stand, **2FA** und **Ausweis-Verifikation** |
| Länge | 6–30 Sekunden, Vollbild, nur nach Klick |
| Belohnung | muss ein **Developer Product** sein, keine Robux, **keine Zufallsitems**, empfohlen im Wert von **3–10 Robux** |
| Verboten | Werbung als Fortschrittssperre, Bildschirm übernehmen, falsche Belohnungsversprechen („free Robux“) |
| Verdienst | **EPM × Impressionen / 1000**; der erste Frame zählt als Impression |
| Prognose | werbeberechtigte Nutzer der letzten 7 Tage × Anzeigen pro Nutzer × erwarteter EPM |
| Option | „Exclude your most likely purchasers“, nur sinnvoll, wenn die Belohnung auch kaufbar ist |

Quelle: [Rewarded video ads](https://create.roblox.com/docs/production/promotion/rewarded-video-ads). **Korrektur:** Die alte Schwelle von 100.000 DAU und die Begrenzung auf „Minimal/Mild“ stehen nicht mehr in der Doku. EPM- oder CPM-Sätze veröffentlicht Roblox nicht. Roblox meldete Abschlussraten über 80 % ✅ ([Roblox Newsroom April 2025](https://about.roblox.com/newsroom/2025/04/roblox-scales-video-ads-partners-with-google)).

### 8.2 Immersive Ads ✅
- Abrechnung: Click-to-Play-Video ab **15 Sekunden** Ansicht; Autoplay-Video ab 0,5 s Blick, 1,5 % des Sichtfelds, Winkel bis 55°, 50 % sichtbar; Bild ab 1 s mit denselben Bedingungen; Portal pro erfolgreichem Teleport.
- Voraussetzungen wie bei Rewarded Video: öffentlich, 13+, ID + 2FA, Fragebogen, **2.000 Besucher pro Monat**.
- Videotafel: mindestens 8 × 4,5 Studs, höchstens 32 × 18 Studs.
- Auszahlung am **25. des Folgemonats**.

Quelle: [Immersive ads](https://create.roblox.com/docs/production/monetization/immersive-ads).

---

## 9. Avatar-Items, Creator Store, Commerce

### 9.1 Avatar-Items und Marketplace ✅

| Verkauf | Creator | Spielbesitzer | Roblox |
|---|---|---|---|
| im Marketplace | 30 % (progressiv mehr, s. u.) | – | Rest |
| im Spiel (Avatar Inspect Menu, Avatar Editor Service, MarketplaceService) | 30 % | **40 %** | 30 % |

Progressiver Anteil nur bei Marketplace-Käufen, abhängig vom Preis im Verhältnis zur Preisuntergrenze:

| Vielfaches der Untergrenze | 1 | 1,3 | 1,5 | 2 | 2,5 | 3 | 4 | 5 | ab 6 |
|---|---|---|---|---|---|---|---|---|---|
| Creator-Anteil | 30 % | 37 % | 41 % | 50 % | 57 % | 62 % | 67 % | 69 % | 70 % |

Kosten: Upload **80 Robux** (mit Emissive Mask **500**). Rückzahlbarer Veröffentlichungsvorschuss: klassisches T-Shirt/Shirt/Hose **10 Robux**, 3D-Kleidung 600, Haare 1.000, Hut 1.500, Körper 2.500; bei bezahlten Limiteds 5.000–20.000. Emissive Items: fünffacher Vorschuss. Escrow 30 Tage. Hochladen nur mit eigener Ausweis-Verifikation oder verknüpftem verifiziertem Elternkonto.
Quellen: [Marketplace fees](https://create.roblox.com/docs/marketplace/marketplace-fees-and-commissions), [Marketplace FAQ](https://create.roblox.com/docs/marketplace/frequently-asked-questions). Zum Veröffentlichen und Verkaufen braucht der Creator (bzw. Gruppenbesitzer) **Roblox Plus oder Premium 1000/2200** ✅ ([Marketplace policy](https://create.roblox.com/docs/marketplace/marketplace-policy)). Weiterverkauf von Community-Limiteds: 50 % Weiterverkäufer, 10 % Original-Creator, 10 % Verkäufer/Affiliate, 30 % Roblox ✅ ([Marketplace fees](https://create.roblox.com/docs/marketplace/marketplace-fees-and-commissions)).

Offizielles Vorschuss-Beispiel ✅: Vorschuss 1.000 Robux, Item im Spiel für 400 Robux. Pro Verkauf: Creator 120, Spielbesitzer 160, Roblox 120. Die 120 von Roblox gehen als Rückzahlung an den Creator, bis die 1.000 erreicht sind. Ab Verkauf 10 behält Roblox seinen Anteil.

**Korrektur zum Juli-2026-Umbau:** Die Presse berichtete, der 2D-Kleidungsanteil sei von 70 % auf 30 % gesenkt worden 🟠 ([tech-insider.org](https://tech-insider.org/roblox-2d-creator-revenue-share-cut-2026/)). Die Doku nennt heute einheitlich 30 % und keinen eigenen 2D-Satz. Die alten 70 % sind nicht mehr dokumentiert.
Folgerung 🧠: Für Spielbesitzer ist ein Kleiderladen im Spiel attraktiv, weil 40 % ohne eigene Item-Produktion fließen.

### 9.2 Creator Store ✅
Modelle und Plugins werden in **US-$** verkauft. Mindestpreis **4,99 $ für Plugins**, **2,99 $ für Modelle**. Abgezogen werden nur Steuern und Zahlungsgebühren, Escrow 30 Tage ([Monetization](https://create.roblox.com/docs/production/monetization)). Onboarding über Stripe 🟡 ([Tubefilter](https://tubefilter.com/2024/01/29/roblox-creator-store-fees/)).

### 9.3 Commerce mit Shopify ✅

| Ebene | Voraussetzung |
|---|---|
| Creator | 18+, ID und E-Mail verifiziert, 2FA, Inhaber des Shopify-Shops oder schriftliche Erlaubnis, Business-Angaben eingereicht |
| Spiel | öffentlich, Maturity-Labels vorhanden, Community-, Werbe- und Commerce-Standards |
| Käufer | nur **USA**, ab **13**, in **Texas ab 18** |
| Digitale Zugabe | Spiel mit Ø **>100.000 DAU** (90 Tage) **und** Ø **>1.000.000 Robux** Monatsumsatz **und** ein Bundle-Verkauf in 3 Monaten, **oder** Werbevertrag ab **50.000 $** pro Jahr |
| Zugabe-Regeln | kein vorher kaufbares Item, keine Robux oder Spielwährung, **kein Zufallsitem**, keine Zusatzschritte nach dem Kauf |

Quelle: [Commerce products](https://create.roblox.com/docs/production/monetization/commerce-products). Den Umsatzanteil nennt die Doku nicht. Fallstudie: Twin Atlas machte in den ersten Wochen sechsstelligen Commerce-Umsatz, rund 90 % der Bestellungen im Spiel 🟡 ([Roblox Newsroom Mai 2025](https://about.roblox.com/newsroom/2025/05/roblox-launches-shopify-integration-amp-licensing-program)).

---

## 10. Kosten auf Creator-Seite ✅

| Posten | Betrag | Rückzahlbar? | Quelle |
|---|---|---|---|
| Veröffentlichung für alle Altersgruppen | 1.000 Robux pro Spiel | ja, wenn das Spiel 60 Tage lang 25 hoch engagierte Spieler hält | [Publish](https://create.roblox.com/docs/production/publishing/publish-games-and-places) |
| Expedited Review | 50.000 Robux | nach 90 Tagen auf Antrag | [Publish](https://create.roblox.com/docs/production/publishing/publish-games-and-places) |
| Avatar-Item-Upload | 80 bzw. 500 Robux | nein, auch bei Ablehnung nicht | [Marketplace fees](https://create.roblox.com/docs/marketplace/marketplace-fees-and-commissions) |
| Veröffentlichungsvorschuss Avatar-Item | 10–20.000 Robux | ja, aus Verkäufen | wie oben |
| US-Quellensteuer (Nicht-US) | 0–30 % bzw. 24 % | Anrechnung je nach Land | [Tax information](https://create.roblox.com/docs/production/monetization/tax-information) |

---

## 11. Auszahlungen der Plattform (Kontext)

| Kennzahl | Wert | Vertrauen | Quelle |
|---|---|---|---|
| DevEx-Gebühren 2024 | 922,8 Mio. $ | ✅ | [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm) |
| DevEx-Gebühren 2025 | **1.503,1 Mio. $** (+63 %) | ✅ | wie oben |
| Treiber laut Roblox | Bookings-Wachstum, Creator Rewards, Kurserhöhung um 8,5 % | ✅ | wie oben |
| Creator mit DevEx-Auszahlung 2025 | mehr als 23.500 | ✅ | wie oben |
| Ø Top-1.000-Creator 2025 | 1,3 Mio. $ (+50 % ggü. Vorjahr) | ✅ | [Q4-2025-Brief](https://s27.q4cdn.com/984876518/files/doc_financials/2025/q4/Q4-2025-Shareholder-Letter.pdf) |
| DevEx Q4 2025 | 477 Mio. $ (+70 %) | 🟡 | [Lindsey Gamble](https://www.threads.com/@lindseygamble_/post/DUf3DVrkwJ5/in-creators-have-earned-over-billion-through-robloxs-developer-exchange-dev-ex) |
| DevEx 12 Monate bis 30.6.2025 | über 1 Mrd. $ | ✅ | [Newsroom RDC 2025](https://about.roblox.com/newsroom/2025/09/roblox-rdc-2025) |
| Ø Top 10 / Top 100 (12 Monate bis Mitte 2025) | 33,9 Mio. $ / 6 Mio. $ | 🟡 | [Notebookcheck](https://www.notebookcheck.net/Roblox-continues-to-reward-game-content-creators-as-payouts-cross-1-billion.1157555.0.html) |
| Entwickler mit über 1 Mio. $ (12 Monate, Q1 2025) | über 100 | ✅ | [Q1-2025-8-K](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000117/rblx-20250331xexhibit991.htm) |
| Median-Creator-Einkommen | ca. 1.500 $ | 🟠 | [endsights](https://endsights.com/roblox-creator-economy) |
| DevEx-Summen 2026 (Q1–Q3) | nicht gefunden | – | – |

Folgerung 🧠: Die Verteilung ist extrem ungleich. 23.500 Creator teilen sich 1,5 Mrd. $, davon gehen allein an die Top 1.000 rund 1,3 Mrd. $ (1.000 × 1,3 Mio. $). Für die übrigen rund 22.500 bleibt im Schnitt weniger als 10.000 $ pro Jahr. Ein erstes Spiel sollte man nicht als Einkommensquelle einplanen.

---

## Beispiele aus echten Spielen
- *Doors*: Taschenlampe und Revives als Kauf mit klarem Zweck ✅ ([Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations)).
- *Jailbreak*: Season Pass mit Gratis- und Premium-Spur ✅ ([Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design)).
- *Grow a Garden*: rund 12 Mio. $ im Mai 2025, mit Robux-Restocks und zufälligen Samen 🟠 ([Calcalist](https://www.calcalistech.com/ctechnews/article/dj4lxef8r)). Mehr Umsatzschätzungen in `preisgestaltung-und-shop-design.md`.

## Do / Don't
| Do | Don't |
|---|---|
| Preise live über `GetProductInfoAsync` anzeigen (Plus-Rabatt, Regionalpreis) | Preise fest ins UI schreiben |
| Bei neuen Spielen früh entscheiden: R15-only für den 18+-Kurs? | R6-Umschalter einbauen und später den 18+-Kurs erwarten |
| Share Links pro Marketingkanal anlegen | Spieler zu Zweitkonten für Rewards auffordern |
| Private Server anbieten, Preis bewusst wählen (Plus-Deckel 100 Robux) | Preis privater Server oft ändern (kündigt alle Abos) |
| Steuerformular vor dem 31.10.2026 prüfen | Einbehalt von 24 % auf die ganze Auszahlung riskieren |
| Altguthaben-Regel bei der Finanzplanung einrechnen | DevEx-Beträge mit dem neuen Kurs hochrechnen, obwohl altes Guthaben zuerst kommt |
| Rewarded Video freiwillig und mit kleiner Belohnung (3–10 Robux) | Werbung als Pflicht vor dem Weiterspielen |

## Checkliste
- [ ] Passes und Developer Products serverseitig verarbeitet, `ProcessReceipt` korrekt (sonst keine Verkäufe außerhalb des Spiels)
- [ ] Preise dynamisch angezeigt (Dynamic Price Check bestanden)
- [ ] Entscheidung zum 18+-Kurs getroffen (R15-only ja/nein) und Avatar-Einstellung gesetzt
- [ ] Subscription-Modell gewählt: Robux (alle Länder, 70 %) oder Landeswährung (100 % ab Monat 2)
- [ ] Private Server aktiviert und Preis festgelegt, bevor Spieler abonnieren
- [ ] Plus-Abo-Prompt an einem sinnvollen Punkt (`PromptRobloxSubscriptionPurchase`)
- [ ] Share Links für jeden externen Kanal angelegt, ID-Verifikation für Audience Expansion erledigt
- [ ] Rewarded Video: Eignung (2.000 Besucher/Monat, ID, 2FA) geprüft, Belohnung als Developer Product
- [ ] DevEx: 13+, 30.000 Earned Robux, verifizierte E-Mail, W-8/W-9, Tipalti-Registrierung binnen einer Woche
- [ ] Haltefristen (5/7/30/60 Tage) in der Cashflow-Planung berücksichtigt

## Offene Fragen / Recherche-Bedarf
- Umrechnung der Audience-Expansion-Prämie (35 % von US-$) in Robux.
- Prozentsatz für Paid Access in Robux und für private Server (nur indirekt 70 %).
- Umsatzanteil bei Commerce/Shopify.
- EPM-Spannen für Rewarded Video und Immersive Ads (nicht veröffentlicht).
- DevEx-Summen für Q1–Q3 2026 (Q3-Zahlen erwartet um den 29.10.2026).
- Reihenfolge der Auszahlung bei gleichzeitigem Altguthaben und 18+-Guthaben.

## Quellen
- [Developer Exchange](https://create.roblox.com/docs/production/monetization/developer-exchange) – Doku-Stand 2026-10-24, ✅
- [U.S. 18+ exchange rate](https://create.roblox.com/docs/production/monetization/18-plus-devex-rate) – 2026-10-24, ✅
- [Tax information](https://create.roblox.com/docs/production/monetization/tax-information) – 2026-10-24, ✅
- [Creator Rewards](https://create.roblox.com/docs/creator-rewards) – 2026-10-24, ✅
- [Engagement-based payouts (eingestellt)](https://create.roblox.com/docs/production/monetization/engagement-based-payouts) – ✅
- [Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus) – 2026-10-24, ✅
- [Subscriptions](https://create.roblox.com/docs/production/monetization/subscriptions) – ✅; [Subscription design](https://create.roblox.com/docs/production/game-design/subscription-design) – ✅
- [Private servers](https://create.roblox.com/docs/production/monetization/private-servers) – ✅
- [Paid access (Robux)](https://create.roblox.com/docs/production/monetization/paid-access-robux), [Paid access (Landeswährung)](https://create.roblox.com/docs/production/monetization/paid-access-local-currency) – ✅
- [Robux transfers](https://create.roblox.com/docs/production/monetization/robux-transfers) – ✅
- [Passes](https://create.roblox.com/docs/production/monetization/passes), [Developer products](https://create.roblox.com/docs/production/monetization/developer-products) – ✅
- [Rewarded video ads](https://create.roblox.com/docs/production/promotion/rewarded-video-ads), [Immersive ads](https://create.roblox.com/docs/production/monetization/immersive-ads) – ✅
- [Marketplace fees and commissions](https://create.roblox.com/docs/marketplace/marketplace-fees-and-commissions) – ✅
- [Commerce products](https://create.roblox.com/docs/production/monetization/commerce-products) – ✅
- [Monetization (Übersicht)](https://create.roblox.com/docs/production/monetization) – ✅
- [Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places) – ✅
- [Roblox 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000024/rblx-20251231.htm) – Feb. 2026, ✅
- [Q4-2025 Shareholder Letter](https://s27.q4cdn.com/984876518/files/doc_financials/2025/q4/Q4-2025-Shareholder-Letter.pdf) – ✅
- [Roblox Newsroom: RDC 2025](https://about.roblox.com/newsroom/2025/09/roblox-rdc-2025) – Sep. 2025, ✅
- [Roblox Newsroom: 18+-Kurs](https://about.roblox.com/newsroom/2026/04/roblox-fuels-high-fidelity-games-over-18-players-increases-qualifying-devex-rate-42) – Apr. 2026, ✅
- [Roblox Newsroom: Roblox Plus](https://about.roblox.com/newsroom/2026/04/introducing-roblox-plus-subscription) – Apr. 2026, ✅
- [Naavik: State of UGC Games 2026](https://naavik.co/deep-dives/the-state-of-ugc-games-2026/) – 2026, 🟡
- [Benzinga: Analysten zur Auszahlungserhöhung](https://www.benzinga.com/analyst-stock-ratings/reiteration/25/09/47551437/roblox-analysts-cheer-developer-payout-hike-see-path-to-stronger-growth) – Sep. 2025, 🟡
- [Nasdaq: Roblox raises creator payouts](https://www.nasdaq.com/articles/roblox-raises-creator-payouts-will-margins-face-pressure-2026) – 🟡
- [DevForum: DevEx rate Confusion](https://devforum.roblox.com/t/devex-rate-confusion/4717348) – Nov. 2025, 🟠
- [rolearn.dev: DevEx Requirements 2026](https://rolearn.dev/guidance/roblox-devex-requirements-2026/) – veraltet, 🟠
