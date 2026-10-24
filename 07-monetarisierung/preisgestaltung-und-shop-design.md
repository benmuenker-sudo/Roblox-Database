# Preisgestaltung und Shop-Design

> Stand: 2026-10-24 · Nächste Prüfung: 2026-11-24 · Gesamt-Vertrauen: ✅ für Preisgrenzen, Pricing-Systeme und Shop-Funktionen (Creator Docs vom 24.10.2026), 🟠 für Preisstufen-Empfehlungen, Conversion-Werte und Umsätze von Top-Spielen, 🧠 für Rechenbeispiele

Einstieg: `monetarisierung.md`. Auszahlungssätze: `einnahmequellen-und-auszahlungen.md`. Shop-UI im Detail: `04-ui-ux/hud-shop-menues.md`. Fairness-Regeln: `ethik-und-recht.md`.

## Kurzfassung
- Seit Mitte 2026 legt Roblox Preise teilweise selbst fest. **Managed Pricing** vereint regionale Preise (30–100 % des Standardpreises) und automatische Preistests. Neue Spiele und neue Items sind standardmäßig dabei ✅ ([Managed pricing](https://create.roblox.com/docs/production/monetization/managed-pricing)).
- Daraus folgt eine harte Technikregel: **Preise nie fest ins UI schreiben**, sondern live über `MarketplaceService` lesen ✅ ([Price optimization](https://create.roblox.com/docs/production/monetization/price-optimization)).
- Gelistete Passes und Developer Products verkauft Roblox auch **außerhalb des Spiels**, etwa auf der Startseite, in der Suche und nach dem Robux-Kauf ✅ ([Passes](https://create.roblox.com/docs/production/monetization/passes)).
- Roblox veröffentlicht **keine** Zahlen für gute Conversion oder ARPPU. Das Dashboard vergleicht mit ähnlichen Spielen ✅ ([Monetization analytics](https://create.roblox.com/docs/production/analytics/monetization)). In der Praxis gelten 1–5 % zahlende Spieler pro Tag als üblich 🟠.
- Ein guter Shop ist laut Roblox **integriert, kontextbezogen und einladend** ✅ ([Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations)).

## Warum das wichtig ist
Der Preis ist die einzige Stellschraube, die sofort wirkt und nichts kostet. Ein falsch angezeigter Preis bricht Vertrauen. Ein Shop, den niemand findet, verkauft nichts. Und weil Discovery auch „Spend days per user“ und „Robux spent per user“ misst ✅ ([Discovery](https://create.roblox.com/docs/discovery)), hilft gute Monetarisierung auch der Reichweite, solange sie die Retention nicht beschädigt.

## Referenzbilder
Selbst erstellte und offizielle Referenzbilder (Übersicht: `assets/bilder/README.md` und `assets/bilder/offiziell/README.md`).

![Shop-Layout](../assets/bilder/ui-shop-layout.png)
*Selbst erstellt: Shop mit Tabs, „Beliebt“-Bereich, Produktkarten, Bestätigungsdialog.*

![Shop mit Top-Picks-Tab](../assets/bilder/offiziell/monetarisierung-liveops/shop-top-picks-tab.png)
*Mobiler Shop mit „Top Picks“ als erstem Tab vor Passes und Coins (`RecommendTopProductsAsync`). Quelle: Roblox Creator Docs, CC BY 4.0 ([Developer products](https://create.roblox.com/docs/production/monetization/developer-products))*

![Shop-Items nach Spieler gerankt](../assets/bilder/offiziell/monetarisierung-liveops/shop-items-nach-spieler-gerankt.png)
*Drei Power-Items, für den jeweiligen Spieler gerankt („Ranked #1“, `RankProductsAsync`). Quelle: Roblox Creator Docs, CC BY 4.0 ([Developer products](https://create.roblox.com/docs/production/monetization/developer-products))*

![Roblox-Shop im Systemmenü](../assets/bilder/offiziell/monetarisierung-liveops/shop-ingame-menue.png)
*Der eingebaute Roblox-Shop im In-Game-Menü. Quelle: Roblox Creator Docs, CC BY 4.0 ([Shop](https://create.roblox.com/docs/production/monetization/shop))*

![Kontextkauf vor dem Spiel](../assets/bilder/offiziell/monetarisierung-liveops/kontextkauf-vor-dem-spiel.jpg)
*Doors: Pre-Run-Shop mit Verbrauchsgütern direkt vor der Runde. Quelle: Roblox Creator Docs, CC BY 4.0 ([Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases))*

![Kontextkauf in der Lobby](../assets/bilder/offiziell/monetarisierung-liveops/kontextkauf-lobby.png)
*Super Striker League: 3D-Shop-Automat in der Lobby. Quelle: Roblox Creator Docs, CC BY 4.0 ([Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases))*

![Taschenlampe mit klarem Zweck](../assets/bilder/offiziell/monetarisierung-liveops/monetarisierung-item-zweck-taschenlampe.png)
*Doors: Die Taschenlampe hat einen sofort verständlichen Nutzen. Quelle: Roblox Creator Docs, CC BY 4.0 ([Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations))*

![Season Pass mit Store-Tab](../assets/bilder/offiziell/monetarisierung-liveops/season-pass-integriert-store-tab.png)
*Bot Clash Simulator: Season Pass mit eigenem, klar unterscheidbarem Store-Tab. Quelle: Roblox Creator Docs, CC BY 4.0 ([Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations))*

![Season Pass Jailbreak](../assets/bilder/offiziell/monetarisierung-liveops/season-pass-uebersicht-jailbreak.png)
*Jailbreak: zehn Stufen, Gratis- und Premium-Belohnungen nebeneinander. Quelle: Roblox Creator Docs, CC BY 4.0 ([Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design))*

![Benchmark-Scorecard](../assets/bilder/offiziell/analytics/benchmark-scorecard-uebersicht.png)
*Scorecard mit Payer Conversion und ARPPU gegen ähnliche Spiele (Perzentile). Quelle: Roblox Creator Docs, CC BY 4.0 ([Analytics](https://create.roblox.com/docs/production/analytics))*

![Experiment-Ergebnisse](../assets/bilder/offiziell/analytics/experiment-ergebnisse.png)
*Ergebnisseite eines A/B-Experiments mit signifikanten Ziel- und Lernmetriken. Quelle: Roblox Creator Docs, CC BY 4.0 ([Experiments](https://create.roblox.com/docs/production/experiments))*

---

## 1. Offizielle Preisgrenzen ✅

| Produkt | Untergrenze | Obergrenze / Stufen | Quelle |
|---|---|---|---|
| Developer Product | 1 Robux | 1.000.000.000 Robux | [Developer products](https://create.roblox.com/docs/production/monetization/developer-products) |
| Pass | nicht genannt | nicht genannt | [Passes](https://create.roblox.com/docs/production/monetization/passes) |
| Pass auf der „Buy Robux“-Seite (Promotion) | mehr als 49 Robux | weniger als 801 Robux | [Passes](https://create.roblox.com/docs/production/monetization/passes) |
| Subscription in Robux | 49 Robux | frei; Änderung alle 60 Tage | [Subscriptions](https://create.roblox.com/docs/production/monetization/subscriptions) |
| Subscription in Landeswährung | – | 2,99 / 4,99 / 7,99 / 9,99 / 14,99 $ | [Subscriptions](https://create.roblox.com/docs/production/monetization/subscriptions) |
| Paid Access in Robux | 25 Robux | 1.000 Robux | [Paid access (Robux)](https://create.roblox.com/docs/production/monetization/paid-access-robux) |
| Paid Access in Landeswährung | – | 9,99 / 29,99 / 49,99 $ (50 / 60 / 70 % Anteil) | [Paid access (lokal)](https://create.roblox.com/docs/production/monetization/paid-access-local-currency) |
| Plugin / Modell im Creator Store | 4,99 $ / 2,99 $ | – | [Monetization](https://create.roblox.com/docs/production/monetization) |
| Regionaler Preis | 30 % des Standardpreises | 100 % des Standardpreises | [Regional pricing](https://create.roblox.com/docs/production/monetization/regional-pricing) |
| Plus-Rabatt | – | 10 % (Monat 1–2), 20 % (ab Monat 3), nicht über 1.000.000 Robux | [Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus) |

---

## 2. Managed Pricing, regionale Preise, Preistests

### 2.1 Managed Pricing ✅
- Vereint **Price Optimization** und **Regional Pricing** unter einem einzigen Opt-in. Ein Tab im Creator Hub zeigt vergangene und geplante Tests und den Umsatzeffekt.
- **Neue Spiele und neu angelegte Items sind automatisch dabei.** Abmelden geht pro Item jederzeit.
- Bestehende Items mit regionalen Preisen wechseln automatisch.
- **Subscriptions, private Server und Developer Server** werden automatisch regional bepreist, ohne Opt-in. Subscriptions sind von Preistests ausgenommen.
- Wer fest eingetragene Preise hat, muss sie vor dem Opt-in reparieren.

Quelle: [Managed pricing](https://create.roblox.com/docs/production/monetization/managed-pricing). Einführung um den 15. Juni 2026 🟡 ([Bloxy News](https://www.threads.com/@bloxy.news/post/DZn3MbEgRAy/introducing-managed-pricing-a-new-system-for-roblox-creators-that-unifies/)).

**Widerspruch in der Doku ✅:** Die Managed-Pricing-Seite sagt, neue Items seien standardmäßig eingeschrieben. Die Regional-Pricing-Seite beschreibt für Developer Products dagegen einen manuellen Weg („Click **Enable Managed Pricing**“) und für Passes „enabled by default“. Sicher ist: Für jedes Item im Creator Hub nachsehen, ob Managed Pricing aktiv ist.

### 2.2 Regionale Preise ✅
- Roblox setzt pro Region einen Preis anhand von Kaufkraft, Wechselkursen und lokalem Ausgabeverhalten.
- Grenzen: nie mehr als **70 % Rabatt**, nie über dem Standardpreis. Bei 100 Robux Standardpreis liegt der Regionalpreis zwischen **30 und 100 Robux**.
- Der **wirtschaftliche Standort** ist nicht immer der Kontostandort. Roblox wertet VPN-Nutzung, Zahlungs- und Kontoverlauf aus. Ist er unklar, gilt der globale Standardpreis.
- Regionale Preise werden regelmäßig angepasst.
- Regionale Preise ändern den Creator-Anteil bei Avatar-Items nicht.

Quelle: [Regional pricing](https://create.roblox.com/docs/production/monetization/regional-pricing). Zeitachse: Opt-in für Passes ab April 2025 ✅ ([DevForum](https://devforum.roblox.com/t/introducing-regional-pricing-for-passes/3621382)), Standard für alle Passes ab 30. März 2026 ✅ ([DevForum](https://devforum.roblox.com/t/enabling-regional-prices-for-all-passes-to-grow-your-global-audience/4471199)). DevForum-Nutzer berichteten Rabatte um 60 %, das liegt im erlaubten Rahmen 🟠.

**Arbitrage verhindern ✅:** `MarketplaceService:GetUsersPriceLevelsAsync` liefert pro Nutzer einen Wert von **1 bis 1000**. 1000 bedeutet voller globaler Preis, 500 bedeutet etwa halber Preis. Damit lassen sich Handel und Geschenke zwischen Spielern mit stark unterschiedlichen Preisniveaus begrenzen. Abfrage bei jedem Spielbeitritt, nicht über Sitzungen hinweg zwischenspeichern ([Regional pricing](https://create.roblox.com/docs/production/monetization/regional-pricing)).

**Rechenbeispiel 🧠:** Ein Pass kostet 400 Robux. Ein Spieler mit Preisniveau 400 zahlt etwa 160 Robux, du bekommst 70 % = 112 Robux. Ohne regionale Preise hätte er vielleicht gar nicht gekauft. Verschenkt er den Pass an einen Spieler mit Niveau 1000, entgehen dir 168 Robux (280 − 112). Regel 🧠: Geschenke nur von höherem zu niedrigerem oder gleichem Preisniveau zulassen, wie es die Doku als Beispiel vorschlägt.

### 2.3 Price Optimization (Preistests durch Roblox) ✅

| Punkt | Offizieller Wert |
|---|---|
| Mindestumsatz | „at least **60,000 transactions** over the previous 30 days“ (im Schnitt 2.000 pro Tag 🧠) |
| Testdauer | „After approximately **3 weeks**“ kommt die Ergebnis-Mail |
| Wiederholung | „Tests run automatically at least every **90 days**“ |
| Übernahme | nur bei „positive incremental total revenue“ |
| Kontrollgruppe | Review-Zeitraum: **2 %** sehen weiter die Originalpreise, 98 % die neuen |
| Review-Zeitraum | vier Wochen (Glossar) |
| Gilt für | nur Passes und Developer Products |
| Während des Tests | Preise der Testprodukte nicht änderbar |
| Gruppen | Roblox wählt die kleinste mögliche Kohorte |

Quelle: [Price optimization](https://create.roblox.com/docs/production/monetization/price-optimization). Die oft zitierten „+4 % mehr Einnahmen“ stammen aus einer DevForum-Ankündigung 🟡 ([DevForum](https://devforum.roblox.com/t/introducing-regional-pricing-for-passes/3621382)) und stehen nicht in der Doku.
Folgerung 🧠: Kleine Spiele erreichen die 60.000 Transaktionen nicht. Für sie bleiben regionale Preise automatisch, Preistests aber nicht.

### 2.4 Dynamic Price Check ✅
Das Werkzeug setzt für bis zu **fünf Testkonten** einen falschen Preis („Price pinned“) oder einen falschen Standort („Location pinned“). Ändert sich der angezeigte Preis im Spiel, ist er dynamisch. Bleibt er gleich, ist er fest eingetragen. Pfad: Monetization → Managed Pricing → Dynamic Price Check ([Price optimization](https://create.roblox.com/docs/production/monetization/price-optimization)).
Technik ✅: `GetProductInfoAsync` (einzelnes Produkt), `GetDeveloperProductsAsync` (alle), im Client ausführen, damit personalisierte Preise erscheinen. `receiptInfo` in `ProcessReceipt` enthält den tatsächlich gezahlten Betrag, auch während Preistests ([Developer products](https://create.roblox.com/docs/production/monetization/developer-products)).
Kleiner Doku-Fehler: Die Price-Optimization-Seite schreibt `Enum.InfoType.GamePasses`, die Pass-Seite `Enum.InfoType.GamePass`. Im Zweifel die Engine-Referenz prüfen.

---

## 3. Verkauf außerhalb des Spiels ✅
- **Gelistete** Passes und Developer Products erscheinen auf der Roblox-Startseite, in Suchergebnissen und auf der Seite nach einem Robux-Kauf. Der Spieler kann kaufen und das Spiel dann mit dem Item betreten.
- Developer Products brauchen dafür ein korrektes `ProcessReceipt`. Roblox prüft das laufend. Bei Fehlern verschwindet das Produkt von externen Flächen, ein Banner unter Monetization → Shop verlinkt den Bericht. Im Spiel bleibt es kaufbar.
- Die Einnahmen ändern sich durch externe Verkäufe nicht.
- Eigenes Icon pro Item anlegen, sonst zeigt Roblox ein Standard-Icon.

Quellen: [Passes](https://create.roblox.com/docs/production/monetization/passes), [Developer products](https://create.roblox.com/docs/production/monetization/developer-products). **Korrektur:** Eine Notiz führte den „Pre-Entry-Storefront“ noch als Roadmap-Punkt für Ende 2026 ([Creator Roadmap](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208)). Laut Doku ist die Funktion bereits umgesetzt. Ob auch die dort angekündigten Gratis-Testphasen für Passes schon laufen, steht nicht in der Doku.

**Widerspruch in der Doku ✅:** Die Shop-Seite sagt „Passes are always listed and can't be unlisted“. Die Pass-Seite verlangt, Passes unter Monetization → Shop als **Listed** zu markieren, damit sie extern erscheinen. Praktisch: Status im Creator Hub kontrollieren.

**Promotion auf der „Buy Robux“-Seite ✅:** Passes zwischen 50 und 800 Robux (oder off-sale) mit Thumbnail können in den „Bonus-Pool“. Spieler bekommen sie beim Kauf eines Robux-Pakets **gratis** und werden ins Spiel eingeladen. Keine Zufallsitems. Roblox empfiehlt einen eigenen Pass nur für diese Fläche. Ob der Creator für gratis verteilte Bonus-Passes bezahlt wird, sagt die Doku nicht ([Passes](https://create.roblox.com/docs/production/monetization/passes)).

---

## 4. Shop-Design

### 4.1 Die drei Eigenschaften eines guten Shops ✅

| Eigenschaft | Bedeutung | Offizielles Beispiel |
|---|---|---|
| **Integriert** | Shop-Icon passt zum UI, schnell rein und raus | *Doors* |
| **Kontextbezogen** | Spieler versteht Nutzen und Wert im Vergleich zu anderen Items | *Doors* erklärt Revives |
| **Einladend** | Ort zum Stöbern, neue und rotierende Ware | *Dragon Adventures* |

Quelle: [Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations). Dazu: jedes Item braucht einen klaren Zweck, Beschreibungen müssen wahr sein, Mischung aus **langlebigen** (Skins) und **verbrauchbaren** (Boosts) Items, Mischung aus **Enhancement** (Leistung) und **Expression** (Aussehen).

### 4.2 Der eingebaute Roblox-Shop ✅
- Zeigt alle Passes und gelisteten Developer Products mit **Top Picks**, personalisierten Kategorien und Suche. Roblox übernimmt Ranking und Optimierung.
- Kann Robux-Pakete anzeigen, die deine Items enthalten.
- Im In-Game-Menü standardmäßig sichtbar; ausblenden mit `StarterGui:SetCoreGuiEnabled(Enum.CoreGuiType.ExperienceShop, false)`.
- Der **globale Shop-Button** oben links ist standardmäßig **aus**. Roblox empfiehlt, ihn einzuschalten.
- Kategorien schlägt Roblox vor, du kannst sie umbenennen und Items verschieben. Änderungen erst nach „Save“ sichtbar.
- Ökonomie unverändert: „Shop is a discovery surface“.

Quelle: [Shop](https://create.roblox.com/docs/production/monetization/shop).

### 4.3 Personalisierung per API ✅

| API | Was sie tut | Regeln |
|---|---|---|
| `RankProductsAsync` | sortiert eine Liste von Produkt-IDs für den Spieler | strenges Rate-Limit, einmal beim Beitritt laden |
| `RecommendTopProductsAsync` | liefert bis zu **50** Items, die der Spieler am ehesten kauft | braucht mind. **1 Kauf in den letzten 28 Tagen**; bereits besessene Passes fehlen; mit `task.spawn` nicht-blockierend aufrufen |
| `AnalyticsService:GetPlayerSegmentsAsync` | grobe Segmente: Zahlerstatus, neu/zurückkehrend, Engagement der letzten 7 Tage, Akquisequelle | serverseitig; ausdrücklich „to personalize content or gate features“ |

Quellen: [Passes](https://create.roblox.com/docs/production/monetization/passes), [Developer products](https://create.roblox.com/docs/production/monetization/developer-products), [AnalyticsService](https://create.roblox.com/docs/reference/engine/classes/AnalyticsService).
Beispiel 🧠: Neuen Nichtzahlern zeigt der Shop zuerst das Starter-Paket, abgewanderten Zahlern ein Rückkehr-Angebot, Stammzahlern neue Kosmetik. Fairness-Grenze: gleiche Preise für alle, nur andere Reihenfolge.

### 4.4 Kontextkäufe: die fünf offiziellen Muster ✅

| Muster | Wann | Beispiel | Achtung |
|---|---|---|---|
| **In-Play** | während der Aktivität, z. B. Pause zwischen Runden | *Dress to Impress*: Theme Props | Der Robux-Kaufablauf dauert **mehrere Sekunden**. Ohne Spielpause ungeeignet |
| **Pre-Play** | beim Warten auf die nächste Runde | *Doors*: Pre-Run-Shop im Aufzug | Nutzen jedes Items klar nennen |
| **Lobby** | 3D-Objekte in der Lobby werben | *Super Striker League* | Klarstellen, ob das das ganze Sortiment ist; sonst Hauptshop öffnen |
| **Komplementär** | passende Zweitkäufe | *Bee Swarm Simulator*: Pollen-Pass + Honey-Speed-Pass | nicht bei jedem Item; lieber als Bundle |
| **UI** | Badges, Event-Fenster, Ladebildschirm, Modal | *Adopt Me*: Villa-Angebot im eigenen Haus | **kein Starter-Paket im allerersten Ladebildschirm**; Modals nie übereinander stapeln |

Quelle: [Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases).

### 4.5 Starter-Paket ✅/🧠
- Offizielle Definition: ein Erstangebot, das ein neuer Spieler **in den ersten Minuten** nach dem Beitritt sieht ✅ ([Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations)).
- Roblox empfiehlt Willkommensangebote und Rabatte für Erstkäufer, um die Hürde zu senken ✅ ([Monetization analytics](https://create.roblox.com/docs/production/analytics/monetization)).
- Nicht im allerersten Ladebildschirm, erst in späteren Sitzungen ✅ ([Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases)).
- Drittquellen empfehlen einen Preis um **49 Robux** 🟠 ([creation.dev](https://www.creation.dev/learn/how-to-price-game-passes-roblox)).
- Faustregel 🧠: Starter-Paket nach dem ersten Erfolgserlebnis anbieten, sichtbar günstiger als die Einzelteile, einmalig pro Konto, mit echtem Zeitfenster (oder ohne Timer). Ein „Rabatt“, der immer gilt, ist laut Doku kein echter Rabatt ✅ ([Monetization](https://create.roblox.com/docs/production/monetization)).

### 4.6 Season Pass ✅
- Laufzeit etwa **ein Monat**, danach **mindestens eine Woche Pause**; etwa **zehn Stufen** als Start.
- Gratis- und Premium-Spur. Premium ist eine Obermenge der Gratis-Belohnungen.
- Doppelte XP in der letzten Woche, wöchentliche Missionen mit hoher Belohnung.
- Wer mitten in der Saison upgradet, bekommt die Premium-Belohnungen bereits erreichter Stufen.
- Restzeit und XP pro Stufe klar anzeigen. Abstand zwischen Belohnungen an der durchschnittlichen Sitzungslänge ausrichten.

Quellen: [Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design), [Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations).

### 4.7 Subscriptions gestalten ✅
Zwei Grundsätze: **Wert** (klar und sofort spürbar) und **Vertrauen** (Inhalte pünktlich liefern). Anwendungsfälle: Währungspakete, Item-Pakete, Mitgliedschaft/VIP, Season Pass. Bei Währungspaketen den Wert gegen bestehende Einmalpakete vergleichen (z. B. gegen ein 100-Robux-Paket). Nicht zu viele langlebige Items in Monatspakete packen, sonst entsteht ein Zwang, ständig neue zu designen ([Subscription design](https://create.roblox.com/docs/production/game-design/subscription-design)).

---

## 5. Preispunkte und Preisleiter

### 5.1 Empfehlungen aus Drittquellen 🟠
Diese Stufen sind **nicht offiziell** und stammen aus Ratgeber-Seiten ([creation.dev](https://www.creation.dev/learn/how-to-price-game-passes-roblox); [ugccraft](https://ugccraft.com/blog/roblox-game-passes-pricing-guide/); [obby.fun](https://www.obby.fun/blog/roblox-monetization-guide)):

| Kategorie | Preisbereich (Robux) | Rolle |
|---|---|---|
| Starter-Paket | um 49 | erster Kauf |
| Kosmetik-Pass | 25–99 | Impulskauf |
| Komfort-Pass (QoL) | 100–300 | angeblich höchste Conversion |
| Multiplikator (2× Geld usw.) | 200–500 | Kernkauf |
| Premium-Inhalt | 500–2.000 | Anker, Wale |
| Anker-Preis | 500–1.000 | macht mittlere Stufen attraktiv |

Mindestens drei Preispunkte anbieten. Mit einem Startpreis starten, einige Wochen beobachten, dann anpassen 🟠.

### 5.2 Offizielle Hinweise zu Preisvielfalt ✅
- „Provide items at a variety of price points“, weil manche Spieler nur kleine Beträge ausgeben.
- Für ARPPU: Einmalkäufe **und** wiederholbare Käufe (Verbrauchsgüter, Nachfüllungen, Währung) anbieten; Bestseller ausbauen; saisonale Items.
- Hohe ARPPU bei niedriger ARPDAU heißt: Umsatz kommt von wenigen. Breiter aufstellen.

Quelle: [Monetization analytics](https://create.roblox.com/docs/production/analytics/monetization).

### 5.3 Beispiel-Preisleiter für einen Simulator 🧠

| Produkt | Typ | Preis | Begründung |
|---|---|---|---|
| Starter-Paket (Pet + 2.000 Coins + 15 min 2× Luck) | Developer Product, einmal pro Konto | 49 | Hürde senken |
| Rückkehr-Paket | Developer Product | 79 | für Spieler, die 7+ Tage weg waren |
| Extra-Pet-Slot | Pass | 149 | Komfort |
| Auto-Sammeln | Pass | 249 | Komfort, spart Zeit |
| 2× Coins | Pass | 399 | Beschleunigung, keine neue Obergrenze |
| VIP (Chat-Tag, Lounge, +10 % Coins) | Pass | 699 | Status + leichter Vorteil |
| Coin-Pakete | Developer Product | 25 / 99 / 249 / 599 / 1.299 | Mengenrabatt sichtbar, 10–30 % Bonus |
| Monats-Abo „Gärtner-Club“ | Subscription | 4,99 $ oder 449 Robux | tägliche Belohnung, exklusiver Skin pro Monat |
| Promo-Pass für „Buy Robux“-Seite | Pass | 50–800 | eigener Pass, keine Zufallsitems |

Hinweis: Alle Preise sind Standardpreise. Regionale Preise und Plus-Rabatte ändern die Anzeige, deshalb dynamisch lesen.

---

## 6. Kennzahlen und Benchmarks

### 6.1 Definitionen im Dashboard ✅

| Kennzahl | Offizielle Definition |
|---|---|
| Conversion Rate | Anteil der DAU, die zahlen |
| Paying Users | DAU, die ein spielbezogenes Item gekauft haben |
| ARPPU | Umsatz pro zahlendem Nutzer |
| ARPDAU | Umsatz pro täglich aktivem Nutzer = Conversion × ARPPU |
| Revenue | stündlich/täglich nach Developer Products, Passes, Kommissionen |

Quelle: [Monetization analytics](https://create.roblox.com/docs/production/analytics/monetization). Benchmarks kommen aus Spielen mit ähnlichen Spielern (mind. 100 DAU), als Perzentilband 50.–90. Fallback: Genre, dann alle Spiele ✅ ([Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard)).

### 6.2 Plattform-Kontext

| Kennzahl | Wert | Vertrauen | Quelle |
|---|---|---|---|
| DAU Q2 2026 | 123 Mio. (+10 %) | ✅ | [Q2-2026-8-K](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm) |
| Ø monatlich zahlende Nutzer Q2 2026 | 27 Mio. (+15 %) | ✅ | wie oben |
| Monatlich zahlende Nutzer Q4 2025 / Q1 2026 | 36,7 Mio. / 31 Mio. | 🟡 | [GamesBeat](https://gamesbeat.com/?p=316195), [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/04/30/roblox-rblx-q1-2026-earnings-call-transcript/) |
| Bookings pro DAU Q2 2026 (Quartal) | 12,66 $ (−2 %) | 🟡 | [Aardvark Labs](https://research.aardvarklabs.co/research/rblx/earnings/2026-q2/rblx-2026-q2-recap) |
| Tägliche Zahler laut Roblox Q1 2026 | 1,4 % von 132 Mio. DAU | 🟡 | [Roblox 10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051082/rblx-20260630.htm) (über Notiz) |
| Bookings FY2025 | 6,8 Mrd. $ (+55 %) | 🟡 | [Naavik](https://naavik.co/deep-dives/the-state-of-ugc-games-2026/) |
| Ausgaben außerhalb der Top 10, Q3 2025 | +40 % ggü. Vorjahr | ✅ | [Q3-2025-Brief](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000326/ex991-q32025shareholderl.htm) |
| Prognose Bookings Q3 2026 | −14 % bis −18 % ggü. Vorjahr | ✅ | [Q2-2026-8-K](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm) |

### 6.3 Conversion und ARPPU aus der Praxis 🟠

| Wert | Kontext | Quelle |
|---|---|---|
| 1–5 % Payer Conversion pro Tag | verbreitete Faustregel | [Medium](https://medium.com/@andy.a.g/the-complete-guide-to-monetizing-a-roblox-game-in-2026-c5e915a7c778) |
| 2–5 % Conversion, 100–300 Robux ARPPU | Tycoons, ohne Beleg | wie oben |
| 1,2 % Conversion = „fairly good“; 40–60 Robux ARPPU = „awful“ | echter Entwickler, *Floor Race* | [DevForum](https://devforum.roblox.com/t/very-low-arppu-in-floor-race/3566999) |
| Conversion und ARPDAU **sinken**, wenn das Spiel wächst | Discovery bringt weniger kaufbereite Spieler | [DevForum](https://devforum.roblox.com/t/payer-conversion-rate-and-arpdau-decreasing-as-game-gains-more-popularity/3898921) |
| 3–5 % Pass-Käufer „durchschnittlich“, 8–12 % „gut“ | Quelle unklar, Bezugszeitraum unklar | [creation.dev](https://www.creation.dev/learn/how-to-price-game-passes-roblox) |

Einordnung 🧠: 27 Mio. monatliche Zahler bei 123 Mio. DAU heißt, eine Minderheit zahlt überhaupt. Tägliche Spiel-Conversion von 1–5 % ist damit plausibel. Monatliche Zahler und tägliche Conversion nie direkt vergleichen.

### 6.4 Rechenbeispiel: Tagesumsatz schätzen 🧠

| Größe | Kleines Spiel | Mittleres Spiel |
|---|---|---|
| DAU | 2.000 | 50.000 |
| Conversion | 2 % → 40 Zahler | 1,5 % → 750 Zahler |
| ARPPU (Robux pro Zahler und Tag) | 120 | 150 |
| Robux-Ausgaben pro Tag | 4.800 | 112.500 |
| Dein Anteil 70 % | 3.360 | 78.750 |
| pro 30 Tage | 100.800 | 2.362.500 |
| in US-$ (0,0038) | **ca. 383 $** | **ca. 8.978 $** |
| ARPDAU (Robux) | 2,4 | 2,25 |

Annahmen sind Beispiele. Nimm deine Werte aus dem Dashboard. Creator Rewards, Werbung und Abos kommen oben drauf (siehe `einnahmequellen-und-auszahlungen.md`).

### 6.5 Umsätze bekannter Spiele (alles Schätzungen) 🟠
Tracker wie RoWatcher und profitable.app modellieren aus Besuchen und CCU. Ihre Werte weichen um das Dreifache und mehr voneinander ab. Nur als Größenordnung nutzen.

| Spiel | Schätzung | Quelle |
|---|---|---|
| *Grow a Garden* | ca. 12 Mio. $ im Mai 2025 | [Calcalist](https://www.calcalistech.com/ctechnews/article/dj4lxef8r), [GameDaily](https://gamedaily.com/games/everything-about-grow-a-garden-the-cozy-idle-sim-revolutionizing-roblox-revenue) |
| *Grow a Garden* heute | ca. 1,75 Mio. $/Monat; Lebenszeit-Modell 286,8 Mio. $ | [RoWatcher](https://rowatcher.com/games/7436755782/grow-a-garden), [profitable.app](https://profitable.app/roblox/games/grow-a-garden) |
| *Steal a Brainrot* | ca. 11 Mio. $/Monat am Höhepunkt (Aug. 2025) | [Greyjournal](https://greyjournal.net/?p=109733) |
| *Steal a Brainrot* Okt. 2026 | 1,4–4,4 Mio. $/Monat; Ausreißer 6,9 Mio. $ in 30 Tagen | [Greyjournal](https://greyjournal.net/?p=109733), [RoWatcher](https://rowatcher.com/games/7709344486/steal-a-brainrot), [profitable.app](https://profitable.app/roblox/games/steal-a-brainrot) |
| *Steal a Brainrot* seit Launch | über 64 Mio. $ (Bloomberg, zitiert) | [RoWatcher](https://rowatcher.com/news/is-the-brainrot-trend-dying-what-ccu-data-from-three-top-games-reveals) |
| *Pet Simulator 99* | ca. 534.000 $/Monat | [RoWatcher](https://rowatcher.com/games/3317771874) |
| *Adopt Me!* | „über 16 Mio. $“ kumuliert, undatiert, vermutlich veraltet | [Wikipedia-Liste](https://wikipedia.com/wiki/Tower_of_Hell) |

Offiziell belegt ist nur: Drei der Top 10 nach Robux-Ausgaben im Juni 2025 waren jünger als zwölf Monate (*Grow a Garden*, *Steal a Brainrot*, *Dead Rails*) ✅ ([Q2-2025-Brief](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000261/q225shletterex992.htm)). Roblox erklärte die schwachen Bookings 2026 mit der Abwanderung aus diesen stark monetarisierenden Hits ✅ ([Q2-2026-8-K](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm)).
Folgerung 🧠: Virale Umsätze fallen innerhalb eines Jahres um 60–90 %. Plane mit Live-Ops und Bindung, nicht mit dem Launch-Spike.

---

## 7. A/B-Tests mit Experiments

### 7.1 Offizielle Regeln ✅

| Punkt | Wert |
|---|---|
| Laufzeit | 14–60 Tage |
| Varianten im Spiel | bis zu **2 Varianten + Kontrolle** |
| Matchmaking-Experimente | bis zu 3 Varianten, nur eins gleichzeitig |
| Mindestgröße | unter **1.000 DAU** kaum brauchbare Daten; MDE prüfen |
| Frühe Schadensschwellen | Spielzeit −10 %, **ARPU −20 %**, **Payer Conversion −20 %** |
| Schadensurteil | erst ab **10.000** eingeschriebenen Spielern (Variante + Kontrolle) |
| Targeting | nach Land, Spielzeit-Dauer, **Active-Spender-Stufe** (erhöht die MDE) |
| Sperre | ein aktives Experiment pro Config-Key; Key ist während des Tests gesperrt |

Quelle: [Experiments](https://create.roblox.com/docs/production/experiments). Roblox empfiehlt ausdrücklich, Preispunkte und Rabatte mit Experiments zu testen und Flash-Sales über **Configs** ohne Server-Neustart zu steuern ✅ ([Balance virtual economies](https://create.roblox.com/docs/production/game-design/balance-virtual-economies)).

### 7.2 So testest du einen Preis praktisch 🧠
Robux-Preise stehen im Creator Hub, nicht im Code. Ein Experiment kann aber steuern, **welches** Produkt angezeigt wird:
1. Zwei Developer Products mit gleichem Inhalt anlegen, z. B. Starter-Paket A (49 Robux) und B (79 Robux).
2. Config-Key `starterPackProductId` mit A als Kontrolle, B als Variante.
3. Zielmetrik: ARPU oder Payer Conversion; Leitplanke: D7-Retention und Spielzeit.
4. Laufzeit mindestens 14 Tage, damit Wochentage ausgeglichen sind.
5. Diese Produkte vom Managed-Pricing-Test ausnehmen, damit sich zwei Tests nicht überlagern.

Was sich testen lässt, ohne Preise anzufassen: Position im Shop, Text auf dem Button („Shop öffnen“ statt „JETZT KAUFEN“), Zeitpunkt des Starter-Angebots, Paketinhalt, Bonus-Prozent bei Währungspaketen.
Bei kleinen Spielen (unter 1.000 DAU): stattdessen Shop-Funnel messen (Shop geöffnet → Item angesehen → Kauf-Prompt → gekauft) und qualitative Playtests ✅ ([Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events)).

---

## Beispiele aus echten Spielen
- *Doors*: Lobby-Shop verkauft nur die Währung „Knobs“, der Pre-Run-Shop im Aufzug die Verbrauchsgüter ✅ ([Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases)).
- *Bee Swarm Simulator*: zwei sich ergänzende Passes direkt untereinander ✅ (ebd.).
- *Adopt Me*: Villa-Angebot, während der Spieler sein einfaches Haus ansieht ✅ (ebd.).
- *Jailbreak*: Season Pass mit zehn Stufen und Gratis-/Premium-Spur ✅ ([Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design)).
- *Pet Simulator 99*: Passes plus rotierende, zeitlich begrenzte Pakete zu saisonalen Events 🟠 ([RoWatcher](https://rowatcher.com/games/3317771874)).
- *Grow a Garden*: Robux-Restocks, Pets, die Läden auffüllen, Handels-Token für Robux 🟠 ([Naavik](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/)). Die zufälligen Samen-Drops wurden als lootbox-artig kritisiert, siehe `ethik-und-recht.md`.

## Do / Don't
| Do | Don't |
|---|---|
| Preise mit `GetProductInfoAsync` / `GetDeveloperProductsAsync` anzeigen | feste Zahlen im TextLabel |
| Dynamic Price Check vor jedem Release | darauf hoffen, dass Regionalpreise schon passen |
| Globalen Shop-Button einschalten, Shop leicht auffindbar | Shop drei Menüs tief verstecken |
| Kontextkäufe in Pausen (Pre-Play, Lobby, Rundenende) | Kauf-Prompts mitten im Kampf; der Kaufablauf dauert Sekunden |
| Mindestens drei Preispunkte mit sichtbarem Mengenbonus | nur ein teures Paket |
| Starter-Paket nach dem ersten Erfolg, in späteren Sitzungen auch im Ladebildschirm | Starter-Paket im allerersten Ladebildschirm |
| Echte, seltene Rabatte mit echtem Ende | Dauer-„Sale“ oder neu startende Countdowns |
| Handel zwischen Preisniveaus mit `GetUsersPriceLevelsAsync` begrenzen | Regionalpreis-Arbitrage ignorieren |
| Eigenen Promo-Pass für die „Buy Robux“-Seite | Zufallsitems in Promo-Passes |
| Preise mit Experiments testen, Retention als Leitplanke | Preise nach Bauchgefühl täglich ändern |

## Checkliste
- [ ] Alle Preise im UI dynamisch (Dynamic Price Check mit Testkonto bestanden)
- [ ] Managed-Pricing-Status jedes Items im Creator Hub geprüft
- [ ] Developer Products mit korrektem `ProcessReceipt` und auf **Listed**, eigene Icons hochgeladen
- [ ] Shop: integriert, kontextbezogen, einladend; globaler Shop-Button an
- [ ] Top Picks bzw. `RecommendTopProductsAsync` eingebaut (braucht 1 Kauf in 28 Tagen)
- [ ] Mindestens drei Preispunkte; Starter-Paket einmal pro Konto
- [ ] Kein Modal über einem anderen Modal; kein Kauf-Prompt im Kampf
- [ ] Shop-Funnel als Funnel-Event angelegt
- [ ] Payer Conversion und ARPPU gegen das Benchmark-Band „ähnliche Spiele“ gelesen
- [ ] Preisexperiment nur mit ausreichend DAU (≥ 1.000) und Retention als Leitplanke
- [ ] Rabatte ehrlich (echtes Ende, kein Dauer-Sale), Texte kindgerecht

## Offene Fragen / Recherche-Bedarf
- Offizielle Spannen für Pass-Preise (Unter-/Obergrenze) stehen nicht in der Doku.
- Effekt von Managed Pricing in Prozent (nur DevForum-Zahl +4 %).
- Ob Creator für gratis verteilte Promo-Passes auf der „Buy Robux“-Seite vergütet werden.
- Belastbare ARPDAU-Benchmarks pro Genre fehlen; nur im eigenen Dashboard sichtbar.
- Status der angekündigten Gratis-Testphasen für Passes.

## Quellen
- [Managed pricing](https://create.roblox.com/docs/production/monetization/managed-pricing) – Doku-Stand 2026-10-24, ✅
- [Regional pricing](https://create.roblox.com/docs/production/monetization/regional-pricing) – ✅
- [Price optimization](https://create.roblox.com/docs/production/monetization/price-optimization) – ✅
- [Passes](https://create.roblox.com/docs/production/monetization/passes), [Developer products](https://create.roblox.com/docs/production/monetization/developer-products) – ✅
- [Shop](https://create.roblox.com/docs/production/monetization/shop) – ✅
- [Monetization (Übersicht und Richtlinien)](https://create.roblox.com/docs/production/monetization) – ✅
- [Monetization foundations](https://create.roblox.com/docs/production/game-design/monetization-foundations) – ✅
- [Contextual purchases](https://create.roblox.com/docs/production/game-design/contextual-purchases) – ✅
- [Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design), [Subscription design](https://create.roblox.com/docs/production/game-design/subscription-design) – ✅
- [Balance virtual economies](https://create.roblox.com/docs/production/game-design/balance-virtual-economies) – ✅
- [Monetization analytics](https://create.roblox.com/docs/production/analytics/monetization), [Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard), [Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events) – ✅
- [Experiments](https://create.roblox.com/docs/production/experiments) – ✅
- [AnalyticsService](https://create.roblox.com/docs/reference/engine/classes/AnalyticsService) – ✅
- [Discovery](https://create.roblox.com/docs/discovery) – ✅
- [Roblox Q2-2026-8-K](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm) – 30.07.2026, ✅
- [Q2-2025-Brief](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000261/q225shletterex992.htm), [Q3-2025-Brief](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000326/ex991-q32025shareholderl.htm) – ✅
- [DevForum: Regional Pricing for Passes](https://devforum.roblox.com/t/introducing-regional-pricing-for-passes/3621382) – Apr. 2025, ✅ (Ankündigung) / 🟠 (Nutzerberichte)
- [DevForum: Regional prices for all passes](https://devforum.roblox.com/t/enabling-regional-prices-for-all-passes-to-grow-your-global-audience/4471199) – März 2026, ✅
- [Aardvark Labs Q2 2026](https://research.aardvarklabs.co/research/rblx/earnings/2026-q2/rblx-2026-q2-recap) – 🟡
- [creation.dev Pricing Guide](https://www.creation.dev/learn/how-to-price-game-passes-roblox), [ugccraft](https://ugccraft.com/blog/roblox-game-passes-pricing-guide/), [obby.fun](https://www.obby.fun/blog/roblox-monetization-guide), [Medium-Guide 2026](https://medium.com/@andy.a.g/the-complete-guide-to-monetizing-a-roblox-game-in-2026-c5e915a7c778) – 🟠
- [DevForum: Floor Race ARPPU](https://devforum.roblox.com/t/very-low-arppu-in-floor-race/3566999), [DevForum: sinkende Conversion](https://devforum.roblox.com/t/payer-conversion-rate-and-arpdau-decreasing-as-game-gains-more-popularity/3898921) – 🟠
- [RoWatcher](https://rowatcher.com/games/7436755782/grow-a-garden), [profitable.app](https://profitable.app/roblox/games/grow-a-garden), [Greyjournal](https://greyjournal.net/?p=109733), [Calcalist](https://www.calcalistech.com/ctechnews/article/dj4lxef8r) – 🟠
