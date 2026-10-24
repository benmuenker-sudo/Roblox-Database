# Ethik und Recht der Monetarisierung

> Stand: 2026-10-24 · Nächste Prüfung: 2026-11-24 · Gesamt-Vertrauen: ✅ für die Roblox-Regeln zu bezahlten Zufallsitems und zur Produktdarstellung (Creator Docs vom 24.10.2026), 🟡 für Klagen und Studien aus Presse und Finanzberichten, 🟠 für Länderlisten aus Sekundärquellen, 🧠 für Designregeln. **Keine Rechtsberatung.**

Einstieg: `monetarisierung.md`. Mechanik, Quoten und Pity im Detail: `03-mechaniken-retention/gacha-und-luck.md`. Plattformregeln allgemein: `01-markt-trends/plattform-regeln-2026.md`.

## Kurzfassung
- **Bezahlte Zufallsitems** (direkt mit Robux oder über mit Robux gekaufte Spielwährung) brauchen **alle möglichen Ergebnisse mit echten Prozentwerten, die genau 100 % ergeben**, sichtbar **vor dem Kauf** ✅ ([Paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items)).
- Für Spieler mit `ArePaidRandomItemsRestricted = true` muss das Spiel eine von **sechs** Alternativen bieten, etwa einen Direktkauf zum Erwartungswert ✅ (ebd.).
- Roblox verbietet in Produkttexten falsche Knappheit, falsche oder neu startende Countdowns und Dauer-„Sales“, und empfiehlt ruhige Texte gegenüber Kindern ✅ ([Monetization](https://create.roblox.com/docs/production/monetization)).
- Der rechtliche Druck wächst. Mehrere US-Bundesstaaten klagen, vor allem wegen Kinderschutz 🟡. Eine Studie der University of Sydney fand irreführende Kaufgestaltung in **14 von 15** untersuchten Spielen 🟡 ([ACS Information Age](https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html)).
- Fair zu monetarisieren schützt nicht nur Kinder, sondern auch das Spiel: Nutzer **downvoten** Spiele mit Monetarisierung, die sie ablehnen ✅ ([Monetization](https://create.roblox.com/docs/production/monetization)).

## Warum das wichtig ist
Ein großer Teil der Roblox-Spieler ist minderjährig. Regelverstöße bei Zufallsitems können zu Moderation führen, unfaire Muster zu Downvotes und schlechter Retention. Länder wie Großbritannien, Australien und Brasilien schränken bezahlte Zufallsitems bereits ein. Wer Zufall und Kaufdruck von Anfang an sauber baut, muss später nichts zurückbauen 🧠.

## Referenzbilder
Selbst erstellte und offizielle Referenzbilder (Übersicht: `assets/bilder/README.md` und `assets/bilder/offiziell/README.md`).

![Gacha: Wahrscheinlichkeiten und Pity](../assets/bilder/gacha-wahrscheinlichkeiten-pity.png)
*Selbst erstellt: Quoten-Anzeige, „1 von X“, sichtbarer Pity-Zähler.*

![Season Pass mit Gratis- und Premium-Spur](../assets/bilder/offiziell/monetarisierung-liveops/season-pass-uebersicht-jailbreak.png)
*Jailbreak: Gratis-Spur neben der Premium-Spur. Roblox verlangt, dass Nichtzahler weiter Belohnungen verdienen können. Quelle: Roblox Creator Docs, CC BY 4.0 ([Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design))*

![Kontextkauf vor dem Spiel](../assets/bilder/offiziell/monetarisierung-liveops/kontextkauf-vor-dem-spiel.jpg)
*Doors: Angebot in einer ruhigen Wartephase mit klar beschriebenem Nutzen statt Druck im Kampf. Quelle: Roblox Creator Docs, CC BY 4.0 ([Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases))*

---

## 1. Roblox-Regeln für bezahlte Zufallsitems ✅

### 1.1 Was als bezahltes Zufallsitem gilt
Alles mit zufälligem Ergebnis, das **direkt oder indirekt mit Robux** bezahlt wird, auch über **bezahlte Spielwährung**. Offizielle Beispiele: Robux für ein Glücksrad; Robux für Edelsteine oder Spin-Tickets, die man dann am Rad ausgibt ([Paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items)).

| Typ | Beispiele aus der Doku |
|---|---|
| Kapsel-Items | Rad drehen, Ei ausbrüten, Truhe öffnen |
| Verstärkungs-Items | Trank mit zufälliger Dauer, Zauber-Upgrade mit Erfolgschance |
| Kombinations-Items | zwei seltene Eier verschmelzen für bessere Chance |
| **Wahrscheinlichkeits-Modifikatoren** | **Luck-Boosts, Pity-Systeme**, erhöhte Ressourcen-Drops, Rate-up-Scrolls |

Wichtig 🧠: Auch ein bezahlter Luck-Trank oder ein Pity-System ist selbst ein bezahltes Zufallsitem im Sinne der Regel.

### 1.2 Offenlegungspflichten

| Regel | Wortlaut / Inhalt |
|---|---|
| Alle Ergebnisse und echte Quoten | „you must indicate all possible outcomes and the actual numerical odds“ |
| Format | Prozentwerte; alle Endergebnisse ergeben **genau 100 %** |
| Zeitpunkt | **vor dem Kauf**; bei indirekten Käufen (Schlüssel, Re-Roll-Token, Spin-Tickets) **bevor** die Spielwährung für den Zufall ausgegeben wird |
| Lange Listen | Pop-up erlaubt, wenn der Auslöser ein beschriftetes **„Info“- oder „Details“-Symbol** hat. Ein **(i) allein reicht nicht** |
| Rundung | auf **vier oder mehr Stellen** hinter der ersten Nicht-Null-Stelle runden, mit Hinweis wie „Probabilities are rounded; total of displayed individual probabilities may not equal 100%.“ |
| Gleiche Quoten | „Odds for each item listed below: X%“ am Listenanfang ist erlaubt |
| Nur einmal erhältlich | bekommt ein Spieler ein Ergebnis nur einmal, müssen die Quoten der übrigen Ergebnisse **für diesen Spieler** aktualisiert werden |
| Luck-Items | Wirkung **numerisch** erklären; die neuen Quoten bei aktivem Item **dynamisch** anzeigen |
| Ausnahme | Zufall ohne Robux und ohne Spielwährung (z. B. gefundener Schlüssel öffnet Truhe) braucht keine Offenlegung |

Quelle: [Paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items). Die Seite verweist auf Nutzungsbedingungen und Community Standards ([Community Standards](https://about.roblox.com/community-standards)).

**Rundungsbeispiel 🧠** (eigene Auslegung der Regel): 0,1739130…% hat die erste Nicht-Null-Stelle an der ersten Nachkommastelle, also mindestens bis zur fünften runden: **0,17391 %**. 52,173913…% beginnt bei den Zehnern, vier Stellen tiefer ist die dritte Nachkommastelle: **52,174 %**. Rechenbeispiele für Luck und Pity in `03-mechaniken-retention/gacha-und-luck.md`.

### 1.3 Per-Spieler-Regeln über PolicyService ✅
`PolicyService:GetPolicyInfoForPlayerAsync()` liefert unter anderem `ArePaidRandomItemsRestricted` und `IsPaidItemTradingAllowed`. Ist `ArePaidRandomItemsRestricted` **true**, darf der Spieler bezahlte Zufallsgeneratoren nicht nutzen, weder mit Robux noch mit Robux-Währung ([PolicyService](https://create.roblox.com/docs/reference/engine/classes/PolicyService)).

Pflicht: eine dieser sechs Behandlungen ([Paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items)):

| # | Behandlung | Offizielles Beispiel |
|---|---|---|
| 1 | unbezahlter, erspielbarer Weg | Mystery-Eier gratis an Meilensteinen |
| 2 | feste, vorher offengelegte Reihenfolge | 1. Dreh immer 5 Edelsteine, 2. immer 10, 3. immer 20 |
| 3 | Direktkauf zum **Erwartungswert** | Lootbox 10 Robux mit 5 % auf ein seltenes Schwert → Schwert direkt für **200 Robux** |
| 4 | Item entfernen oder verstecken | Glücksrad durch Direktkauf-Shop ersetzen |
| 5 | Kauf mit Fehlermeldung blockieren | „Sorry, this item is unavailable for users in your region“ |
| 6 | Spieler aus dem Bereich entfernen | wegteleportieren |

Ist `IsPaidItemTradingAllowed` **false**, darf der Spieler Ergebnisse bezahlter Zufallsitems **und andere bezahlte Items** nicht handeln.

Die Monetarisierungs-Übersicht sagt es noch deutlicher: „If a user can use Robux or something else that was acquired with Robux to get a random reward, you are **required** to use PolicyService to block this feature for users who are not permitted“ ✅ ([Monetization](https://create.roblox.com/docs/production/monetization)).

**Widerspruch in der Doku ✅:** Die Seite zum Maturity-Fragebogen formuliert weicher: „it's **recommended** to take the mandatory precautions“ ([Content maturity](https://create.roblox.com/docs/production/promotion/content-maturity)). Policy-Seite und Monetarisierungs-Übersicht sagen „must“ bzw. „required“. Behandle es als Pflicht.

**Erwartungswert-Formel 🧠:** Direktpreis = Boxpreis ÷ Chance auf das Item. 10 ÷ 0,05 = 200. Bei 25 Robux und 0,5 % wären es 5.000 Robux. Das zeigt dem Designer auch, wie teuer ein seltenes Item im Schnitt wirklich ist.

### 1.4 Weitere Stellen, an denen Zufall verboten ist ✅
- **Rewarded Video:** Belohnungen „cannot be randomized items“ ([Rewarded video ads](https://create.roblox.com/docs/production/promotion/rewarded-video-ads)).
- **Promo-Passes auf der „Buy Robux“-Seite:** dürfen keine bezahlten Zufallsitems gewähren ([Passes](https://create.roblox.com/docs/production/monetization/passes)).
- **Commerce-Zugaben:** dürfen kein Zufallsitem sein und keinen Zufallsmechanismus brauchen ([Commerce products](https://create.roblox.com/docs/production/monetization/commerce-products)).
- **Glücksspiel:** Spielbares Glücksspiel, auch simuliert, ist verboten. Nur nicht spielbare Darstellung (z. B. ein Casino als Kulisse) ist mit Label erlaubt ([Content maturity](https://create.roblox.com/docs/production/promotion/content-maturity)).
- **Fragebogen:** Bezahlte Zufallsitems und Handel mit bezahlten Items müssen im Maturity-&-Compliance-Fragebogen angegeben werden ([Content maturity](https://create.roblox.com/docs/production/promotion/content-maturity)).

### 1.5 Zeitachse und Länder

| Datum | Ereignis | Vertrauen | Quelle |
|---|---|---|---|
| 2019 | erste Richtlinien zu bezahlten Zufallsitems | ✅ | [DevForum](https://devforum.roblox.com/t/guidelines-around-users-paying-for-random-virtual-items/307189) |
| ca. 2024 (🧠 aus der Thread-Nummer geschätzt) | Einschränkung für **UK-Nutzer unter 18** | ✅ (Ankündigung) | [DevForum UK](https://devforum.roblox.com/t/update-on-paid-random-items-restriction-for-uk-users-under-18/3072183) |
| ca. 2024 (🧠 geschätzt) | Einschränkung für **australische Nutzer**; laut Presse für **alle** Spieler in Australien | ✅ / 🟡 | [DevForum AU](https://devforum.roblox.com/t/update-on-paid-random-items-restriction-for-australian-users/3153602), [ACS Information Age](https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html) |
| 31. März (Jahr nicht gesichert, vermutlich 2026) | **Brasilien**: unter 18 gesperrt, zusätzlich Erwachsene ohne Altersprüfung | 🟠 | Suchauszug, siehe [DevForum 4654622](https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622) |
| 26. Mai 2026 | „Clarifying Requirements for Paid Random Items“: Quoten vor dem Kauf, auch bei Robux-Währung; (i)-Symbol reicht nicht | 🟡 (Datum aus Sekundärquelle) | [DevForum 4654622](https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622), [ZehnStudio26](https://zehn-studio26.com/news/paid-random-items-odds-disclosure/) |
| Juni 2026 | Presse: Südkoreas Lootbox-Gesetz als Auslöser der weltweiten Quotenpflicht | 🟠 | [TechTimes](https://www.techtimes.com/articles/319148/20260626/koreas-loot-box-rules-push-roblox-disclose-item-odds-worldwide.htm) |

**Regulierte Märkte:** Eine Notiz nennt **Australien, Belgien, Niederlande, Großbritannien, Brasilien** und empfiehlt, sie im Player Emulator von Studio zu testen 🟠. Diese Länderliste steht **nicht** in der Doku; die Policy-Seite nennt keine Länder. Deshalb nie eine eigene Länderliste hart codieren, sondern immer `ArePaidRandomItemsRestricted` pro Spieler abfragen 🧠.
Laut derselben Sekundärquelle verlangt die Klarstellung vom Mai 2026 auch, dass **jedes Ergebnis einen Nutzen** hat 🟠. In der Doku steht das nicht.

---

## 2. Regeln für die Darstellung von Angeboten ✅

### 2.1 Ehrliche Rabatte und Timer
Aus der Monetarisierungs-Übersicht ([Monetization](https://create.roblox.com/docs/production/monetization)):
- Rabatte müssen **echt** und **fair** sein. Nicht echt: ein Item ist „immer im Angebot“ zum gleichen Preis. Nicht fair: ein Rabatt nur für sehr kurze Zeit, um zum schnellen Kauf zu drängen.
- Nutzer dürfen nie irregeführt, verwirrt oder gedrängt werden. Sie sollen immer eine klare, bewusste Wahl treffen.
- Nicht behaupten, etwas sei fast ausverkauft oder nur kurz verfügbar, wenn das nicht stimmt.
- Keine ungenauen oder **neu startenden Countdowns** für dasselbe Item. Beispiel aus der Doku: ein „Deal des Tages“, der bei jedem Login wieder 24 Stunden anzeigt.
- Ein bemerkenswerter Plattformhinweis: Timer und Wartezeiten, die man **wegkaufen oder vorziehen** kann, funktionieren auf anderen Plattformen, sind bei Roblox-Spielern aber **unbeliebt**.

### 2.2 Sprache gegenüber Kindern ✅

| Vermeiden | Stattdessen |
|---|---|
| „GET IT NOW“ | „View Item“ (Item ansehen) |
| „LAST CHANCE, ACT NOW“ | „See Price“ (Preis ansehen) |
| „BUY BEFORE IT'S GONE!“ | „Open Shop“ (Shop öffnen) |

Quelle: [Monetization](https://create.roblox.com/docs/production/monetization). Deutsche Entsprechungen 🧠: nicht „JETZT ZUSCHLAGEN!“, „LETZTE CHANCE!“, „Nur noch heute!“, sondern „Ansehen“, „Preis anzeigen“, „Zum Shop“.

### 2.3 Weitere offizielle Fairness-Regeln ✅
- Item-Beschreibungen müssen wahr und genau sein ([Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations)).
- Nichtzahler müssen weiter Belohnungen verdienen können, z. B. über eine Gratis-Spur im Season Pass (ebd.).
- Abo-Vorteile dürfen nach dem Kauf nicht an Zusatzaufgaben wie Social-Media-Posts geknüpft werden ([Subscriptions](https://create.roblox.com/docs/production/monetization/subscriptions)).
- Spiele, die mit falschen Angeboten täuschen, werden entfernt (ebd.).
- Rewarded Video: klare Offenlegung, sofortige Belohnung, **keine Fortschrittssperre**, keine „free Robux“-Versprechen ([Rewarded video ads](https://create.roblox.com/docs/production/promotion/rewarded-video-ads)).
- Beim Werben um Plus-Abos oder Abo-Käufe muss das Spiel prüfen, ob der Nutzer überhaupt kaufen darf (PolicyService: Subscriptions, Commerce, Immersive Ads) ([Monetization](https://create.roblox.com/docs/production/monetization)).

---

## 3. Klagen, Beschwerden und Behörden

### 3.1 Klagen mit Bezug zu Geld und Käufen 🟡

| Fall | Vorwurf | Stand laut Quellen | Quelle |
|---|---|---|---|
| **Colvin v. Roblox** (Aug. 2023) | Roblox habe Casino-Seiten mit Robux geduldet und über die DevEx-Gebühr profitiert | Ansprüche gegen Roblox abgewiesen; Rest unklar, Überschriften widersprechen sich | [Courthouse News](https://www.courthousenews.com/roblox-dodges-lawsuit-claims-over-in-game-currency-gambling/), [TechCrunch](https://techcrunch.com/2023/08/18/roblox-children-gambling-class-action-lawsuit-robux/amp) |
| **Haugland v. Roblox und Stripe** (Hawaii, Juli, Jahr unklar) | Käufe von Kindern unter 13 ohne Zustimmung der Eltern | geplante Sammelklage | [AboutLawsuits](https://www.aboutlawsuits.com/roblox-class-action-lawsuit-app-charges-children-money-without-parental-consent/) |
| **Noel v. Roblox** (2024) | Ausbeutung junger Creator („Kinderarbeit“) über Robux-Bezahlung | Sammelklage | [ClassAction.org](https://www.classaction.org/news/roblox-lawsuit-alleges-entire-platform-built-around-exploitation-of-child-labor) |
| Vergleich über 10 Mio. $ | kaufbezogene Sammelklage | Details und Datum unklar | 🟠 [TopClassActions](https://topclassactions.com/lawsuit-settlements/consumer-products/video-games/roblox-class-action-alleges-platform-allows-minors-to-gamble/) |
| „Über 100 Klagen“ wegen süchtig machendem Design (Anfang 2026) | Sammelzahl aus Presse und Interessengruppen | Zahl vorsichtig behandeln | 🟠 [ACS Information Age](https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html) |

### 3.2 Klagen von US-Bundesstaaten (vor allem Kinderschutz) 🟡

| Bundesstaat | Zeitpunkt | Kern | Quelle |
|---|---|---|---|
| Louisiana | Aug. 2025 | Kinderschutz, Ausbeutung | [Dakota News Now](https://www.dakotanewsnow.com/2025/08/15/state-attorney-general-sues-roblox-alleging-child-exploitation-safety-failures/) |
| Kentucky | Okt. 2025 | Verbraucherschutzgesetz, bis 2.000 $ pro Verstoß | [WEKU](https://www.weku.org/the-commonwealth/2025-10-09/kentucky-attorney-general-files-suit-against-roblox-alleges-its-unsafe-for-children) |
| Iowa | Dez. 2025 | Gefährdung von Kindern | [Iowa AG](https://www.iowaattorneygeneral.gov/newsroom/attorney-general-brenna-bird-sues-roblox-for-endangering-iowa-children) |
| Florida | 2025/26 | 76-seitige Klage plus **strafrechtliche Vorladungen** | [Fox35](https://www.fox35orlando.com/news/florida-ag-sues-roblox-claiming-misled-parents-exposed-kids-predators) |
| Nebraska | März 2026 | fordert verpflichtende Alters- und Identitätsprüfung | [Nebraska Public Media](https://nebraskapublicmedia.org/en/news/news-articles/attorney-general-sues-gaming-platform-roblox-over-child-safety-issues/) |
| Oklahoma | ca. Mai 2026 | Kinderschutz | [Quartz](https://qz.com/oklahoma-ag-sues-roblox-child-safety-051526) |
| Tennessee | 2025/26 | Kinderschutz, Verbraucherrecht | [Fox Baltimore](https://foxbaltimore.com/news/nation-world/tennessee-ag-sues-roblox-says-platform-endangers-kids-breaches-consumer-laws) |
| Texas | 2025/26 | Anspruch nach dem Texas Deceptive Trade Practices Act läuft weiter | [Roblox 10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051082/rblx-20260630.htm) (über Notiz) |
| Alabama, Nevada, West Virginia | April 2026 | **Vergleiche** laut 10-Q | wie oben |

Bundesweite Kinderschutz-Verfahren sind in einem **MDL** gebündelt ([Harm Report](https://www.harmreport.com/lawsuits/roblox/)). Urteile in den Klagen der Bundesstaaten wurden nicht gefunden. Folgerung 🧠: Die meisten Klagen zielen auf Sicherheit und Chat, nicht direkt auf Monetarisierung. Kaufdruck gegenüber Kindern taucht aber in Verbraucherschutz-Ansprüchen (Kentucky, Texas) auf.

### 3.3 Beschwerde wegen manipulativem Design (Mai 2026) 🟡
Interessengruppen reichten eine Beschwerde ein. Sie kritisiert **limitierte Items, die künstliche Dringlichkeit erzeugen**, Lootboxen und Glücksräder sowie die **Robux-Schicht**, die echte Preise vor Kindern verschleiere ([Fortune](https://fortune.com/2026/05/20/exclusive-advocacy-groups-file-complaint-roblox-manipulative-design/)). Die Vorwürfe sind nicht entschieden.
**Widersprüchliche Angaben:** Eine Notiz nennt Fairplay und NCOSE als Beschwerdeführer bei der FTC. Eine andere nennt Anxious Generation Movement, ParentsSOS, Consumer Federation of America und EPIC und hält offen, ob die Beschwerde bei der FTC einging. Beide berufen sich auf denselben Fortune-Artikel.

### 3.4 Studien 🟡

| Studie | Ergebnis | Quelle |
|---|---|---|
| University of Sydney (2026), „Misleading and Deceptive Monetisation in Roblox“ | manipulative bzw. irreführende Kaufgestaltung in **14 von 15** beliebten Spielen | [Bericht (PDF)](https://ses.library.usyd.edu.au/bitstream/handle/2123/35033/Misleading%20and%20Deceptive%20Monetisation%20in%20Roblox%20-%20Final.pdf?sequence=3&isAllowed=y), [ACS Information Age](https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html) |
| Monash University | **58 %** der Teilnehmer sahen in 12 Monaten 10+ Dark Patterns | [ACS Information Age](https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html) |
| CHI 2025, „The System is Made to Inherently Push Child Gambling…“ | Kinderschutz, Monetarisierung und Moderation auf Roblox | [ACM DL](https://dl.acm.org/doi/10.1145/3706598.3713170) |

Kritik an konkreten Spielen 🟡: Die zufälligen Samen-Drops in *Grow a Garden* wurden mit Lootboxen verglichen, das Studio für „excessive monetization“ kritisiert ([GameDaily](https://gamedaily.com/games/everything-about-grow-a-garden-the-cozy-idle-sim-revolutionizing-roblox-revenue); [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)). Roblox' Antwort laut 10-Q: Nur **1,4 %** von 132 Mio. DAU waren im Q1 2026 Zahler 🟡 ([10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051082/rblx-20260630.htm), über Notiz).

### 3.5 Plattform-Reaktionen (Folgerung) 🧠
Mehrere Schritte passen zu diesem Druck: Altersprüfung als Basis des 18+-DevEx-Kurses, Ende spielübergreifender Pass-Verkäufe (30.5.2026), Robux-Transfers nur für Plus-Abonnenten, Ausweis-Pflicht für Avatar-Item-Uploads, Handelssperren über `IsPaidItemTradingAllowed`. Die Anreize verschieben sich hin zu verifizierten Erwachsenen und transparenten Direktkäufen.

---

## 4. Dark Patterns erkennen

| Muster | Warum problematisch | Status bei Roblox | Faire Alternative 🧠 |
|---|---|---|---|
| Falscher Countdown / neu startender Timer | erzeugt Druck ohne echten Grund | **verboten** ✅ | echtes Enddatum oder kein Timer |
| „Fast ausverkauft“, obwohl nicht wahr | falsche Knappheit | **verboten** ✅ | echte Stückzahl anzeigen oder weglassen |
| Dauer-„Sale“ | falscher Referenzpreis | **kein echter Rabatt** ✅ | seltene, echte Rabatte |
| Rabatt nur für Sekunden/Minuten | drängt zum Sofortkauf | **nicht fair** ✅ | Rabatt über Tage |
| Wartezeit wegkaufen | bei Roblox-Spielern unbeliebt | Plattform rät ab ✅ | Beschleunigung, die den Spaß nicht beendet |
| Lootbox ohne Quoten | Glücksspielnähe | **verboten** bei Robux-Bezug ✅ | Quoten + Pity + Direktkauf |
| Werbung als Fortschrittssperre | Zwang | **verboten** (Rewarded Video) ✅ | freiwillige Werbung, kleine Belohnung |
| Robux-Schicht verschleiert echten Preis | Kinder rechnen nicht um | in Studie und Beschwerde kritisiert 🟡 | Robux-Preis klar zeigen, keine zweite Bezahlwährung mit krummen Kursen |
| Kauf-Prompt direkt nach Niederlage | nutzt Frust aus | nicht ausdrücklich geregelt | Angebot in Pausen oder vor der Runde |
| Limitierte Items mit „Manufactured Urgency“ | FOMO bei Kindern | in Beschwerde kritisiert 🟡 | erspielbare Event-Items, Aufholmechaniken |
| Mehrere Modals übereinander | überfordert | Doku rät ab ✅ ([Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases)) | Warteschlange, ein Angebot zur Zeit |

---

## 5. Designregeln für ein junges Publikum 🧠
1. **Robux-Bezug prüfen:** Kann man mit Robux oder mit gekaufter Währung irgendwo ein zufälliges Ergebnis bekommen? Dann gelten alle Regeln aus Abschnitt 1.
2. **Eine Bezahlwährung, glatte Kurse:** Wenn es eine Premium-Währung gibt, dann mit einfachem Verhältnis (z. B. 1 Robux = 10 Edelsteine) und Robux-Preis daneben.
3. **Zufall immer mit Ausweg:** Pity-Zähler sichtbar, Direktkauf zum Erwartungswert oder erspielbarer Weg. Das erfüllt gleichzeitig Behandlung 1 oder 3 für eingeschränkte Spieler.
4. **Kein Fortschritt hinter Zufall oder Geld:** Nichtzahler erreichen jedes Ziel, nur langsamer.
5. **Kaufmomente in Ruhephasen:** Lobby, vor der Runde, nach einem Erfolg. Nie mitten im Kampf, nie direkt nach einer Niederlage.
6. **Bestätigung und Klarheit:** Preis, Wirkung und Dauer stehen auf der Kaufkarte. Roblox zeigt ohnehin einen Kaufdialog; zusätzliche Fake-Bestätigungen („Bist du sicher, dass du verzichten willst?“) weglassen.
7. **Handel absichern:** `IsPaidItemTradingAllowed` prüfen, Preisniveaus mit `GetUsersPriceLevelsAsync` berücksichtigen, Betrug durch serverseitige Validierung verhindern.
8. **Texte ruhig halten:** keine Großbuchstaben-Rufe, keine Schuld- oder Angst-Formulierungen.
9. **Ausgaben-Spitzen beobachten:** Wenn wenige Spieler einen großen Teil des Umsatzes bringen (hohe ARPPU, niedrige ARPDAU), Angebote breiter aufstellen statt die Spitze weiter zu melken. Das empfiehlt auch Roblox ✅ ([Monetization analytics](https://create.roblox.com/docs/production/analytics/monetization)).
10. **Dokumentieren:** Quoten, Pity-Regeln und PolicyService-Behandlung im Konzept festhalten, damit Updates nichts kaputt machen.

## Beispiele aus echten Spielen
- *Grow a Garden*: Samen mit Robux kaufen und pflanzen ist indirekter bezahlter Zufall. Nach den älteren Richtlinien mussten die Quoten **vor dem Pflanzen** sichtbar sein ✅ ([Developer Hub: Virtual items policy](https://developer.roblox.com/zh-cn/articles/virtual-items-policy)); heute verlangt die Doku die Anzeige, bevor die Währung für den Zufall ausgegeben wird.
- *Adopt Me*: Seltenheit beim Schlüpfen zufällig, Gamepasses können Chancen erhöhen 🟠 (Guide). Solche Chancen-Passes sind Wahrscheinlichkeits-Modifikatoren und brauchen numerische Erklärung ✅.
- *Jailbreak*: Gratis-Spur im Season Pass als offizielles Beispiel für faire Belohnungen ✅ ([Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design)).

## Do / Don't
| Do | Don't |
|---|---|
| Alle Quoten als Prozent, Summe 100 %, vor dem Kauf | Quoten nur als „selten/episch“ |
| „Details“-Button mit Text | nur ein (i)-Symbol |
| Luck-Boost als neue Prozentwerte zeigen | „2× Luck!“ ohne Zahlen |
| `ArePaidRandomItemsRestricted` pro Spieler prüfen | eigene Länderliste hart codieren |
| Direktkauf zum Erwartungswert anbieten | eingeschränkte Spieler einfach ins Leere laufen lassen |
| Echte Rabatte mit echtem Ende | „Deal des Tages“, der nie endet |
| „Shop öffnen“, „Ansehen“ | „LETZTE CHANCE, JETZT KAUFEN!“ |
| Paid-Random-Items im Maturity-Fragebogen angeben | Fragebogen raten oder veralten lassen |
| Handel für `IsPaidItemTradingAllowed = false` sperren | Ergebnisse bezahlter Zufallsitems frei handelbar machen |

## Checkliste
- [ ] Liste aller Stellen, an denen Robux oder gekaufte Währung zu Zufall führt (inkl. Luck-Tränke, Pity, Re-Rolls)
- [ ] Jede Stelle zeigt alle Ergebnisse mit Prozent, Summe 100 %, vor dem Kauf bzw. vor dem Ausgeben der Währung
- [ ] Pop-up-Auslöser mit Wort „Info“ oder „Details“
- [ ] Rundung nach Regel plus Rundungshinweis
- [ ] Quoten bei aktivem Luck-Item dynamisch aktualisiert
- [ ] Einmalige Ergebnisse: Restquoten pro Spieler aktualisiert
- [ ] `ArePaidRandomItemsRestricted` abgefragt, eine der sechs Behandlungen umgesetzt
- [ ] `IsPaidItemTradingAllowed` abgefragt, Handel ggf. gesperrt
- [ ] Im Player Emulator mit eingeschränktem Profil getestet
- [ ] Maturity-&-Compliance-Fragebogen aktuell (Paid Random Items, Paid Item Trading)
- [ ] Keine falschen Countdowns, keine falsche Knappheit, kein Dauer-Sale
- [ ] Texte nach der Doku-Tabelle geprüft
- [ ] Rewarded Video ohne Zufallsbelohnung und ohne Fortschrittssperre

## Offene Fragen / Recherche-Bedarf
- Offizielle Liste der Länder mit Einschränkungen (die Doku nennt keine).
- EU- und deutsches Recht (z. B. Jugendschutz, Lootbox-Debatte in Belgien und den Niederlanden) wurde für diese Datei nicht recherchiert.
- Ausgang der Klagen der Bundesstaaten und Details der Vergleiche mit Alabama, Nevada und West Virginia.
- Wer genau die Beschwerde vom Mai 2026 eingereicht hat und bei welcher Behörde.
- Ob „jedes Ergebnis muss einen Nutzen haben“ eine offizielle Regel ist.

## Quellen
- [Paid random items policy guidelines](https://create.roblox.com/docs/production/monetization/paid-random-items) – Doku-Stand 2026-10-24, ✅
- [Monetization (Richtlinien zur Darstellung)](https://create.roblox.com/docs/production/monetization) – ✅
- [PolicyService](https://create.roblox.com/docs/reference/engine/classes/PolicyService) – ✅
- [Content maturity](https://create.roblox.com/docs/production/promotion/content-maturity) – ✅
- [Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations), [Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases), [Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design) – ✅
- [Subscriptions](https://create.roblox.com/docs/production/monetization/subscriptions), [Rewarded video ads](https://create.roblox.com/docs/production/promotion/rewarded-video-ads), [Passes](https://create.roblox.com/docs/production/monetization/passes), [Commerce products](https://create.roblox.com/docs/production/monetization/commerce-products) – ✅
- [Roblox Community Standards](https://about.roblox.com/community-standards) – ✅
- [DevForum: Clarifying Requirements for Paid Random Items](https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622) – Mai 2026, ✅ (Ankündigung) / 🟡 (Inhalt über Sekundärquelle)
- [DevForum: UK unter 18](https://devforum.roblox.com/t/update-on-paid-random-items-restriction-for-uk-users-under-18/3072183), [DevForum: Australien](https://devforum.roblox.com/t/update-on-paid-random-items-restriction-for-australian-users/3153602), [DevForum: Richtlinien 2019](https://devforum.roblox.com/t/guidelines-around-users-paying-for-random-virtual-items/307189) – ✅
- [Developer Hub: Virtual items policy (alt)](https://developer.roblox.com/zh-cn/articles/virtual-items-policy) – ✅ (veraltet)
- [Roblox 10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051082/rblx-20260630.htm) – ✅ (Inhalte über Notiz 🟡)
- [Fortune: Beschwerde wegen manipulativem Design](https://fortune.com/2026/05/20/exclusive-advocacy-groups-file-complaint-roblox-manipulative-design/) – 20.05.2026, 🟡
- [ACS Information Age: Studien](https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html) – 2026, 🟡
- [University of Sydney: Misleading and Deceptive Monetisation in Roblox (PDF)](https://ses.library.usyd.edu.au/bitstream/handle/2123/35033/Misleading%20and%20Deceptive%20Monetisation%20in%20Roblox%20-%20Final.pdf?sequence=3&isAllowed=y) – 2026, 🟡
- [ACM CHI 2025](https://dl.acm.org/doi/10.1145/3706598.3713170) – 🟡
- [Courthouse News](https://www.courthousenews.com/roblox-dodges-lawsuit-claims-over-in-game-currency-gambling/), [TechCrunch 2023](https://techcrunch.com/2023/08/18/roblox-children-gambling-class-action-lawsuit-robux/amp), [AboutLawsuits](https://www.aboutlawsuits.com/roblox-class-action-lawsuit-app-charges-children-money-without-parental-consent/), [ClassAction.org](https://www.classaction.org/news/roblox-lawsuit-alleges-entire-platform-built-around-exploitation-of-child-labor) – 🟡
- Klagen der Bundesstaaten: [Dakota News Now](https://www.dakotanewsnow.com/2025/08/15/state-attorney-general-sues-roblox-alleging-child-exploitation-safety-failures/), [WEKU](https://www.weku.org/the-commonwealth/2025-10-09/kentucky-attorney-general-files-suit-against-roblox-alleges-its-unsafe-for-children), [Iowa AG](https://www.iowaattorneygeneral.gov/newsroom/attorney-general-brenna-bird-sues-roblox-for-endangering-iowa-children), [Fox35](https://www.fox35orlando.com/news/florida-ag-sues-roblox-claiming-misled-parents-exposed-kids-predators), [Nebraska Public Media](https://nebraskapublicmedia.org/en/news/news-articles/attorney-general-sues-gaming-platform-roblox-over-child-safety-issues/), [Quartz](https://qz.com/oklahoma-ag-sues-roblox-child-safety-051526), [Fox Baltimore](https://foxbaltimore.com/news/nation-world/tennessee-ag-sues-roblox-says-platform-endangers-kids-breaches-consumer-laws), [Harm Report](https://www.harmreport.com/lawsuits/roblox/) – 🟡
- [TechTimes: Korea als Auslöser](https://www.techtimes.com/articles/319148/20260626/koreas-loot-box-rules-push-roblox-disclose-item-odds-worldwide.htm), [ZehnStudio26](https://zehn-studio26.com/news/paid-random-items-odds-disclosure/), [TopClassActions](https://topclassactions.com/lawsuit-settlements/consumer-products/video-games/roblox-class-action-alleges-platform-allows-minors-to-gamble/) – 🟠
