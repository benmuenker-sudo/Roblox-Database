# Monetarisierung

> Stand: 2026-10-24 · Gesamt-Vertrauen: 🟠 für Zahlen (viele widersprüchliche SEO-Seiten, offizielle Werte vor Entscheidungen im Creator Hub prüfen), ✅ für Struktur der Roblox-Produkte, 🧠 für Designprinzipien

## Kurzfassung
Roblox-Spiele verdienen über **Gamepasses**, **Developer Products**, **Abos**, **Premium-Engagement** und **Werbung/Creator Rewards**. Discovery misst seit 2026 auch Ausgaben als positives Signal ✅, aber aggressive Monetarisierung senkt Retention. Ziel: **fairer Mehrwert, der den Loop beschleunigt oder verschönert, ohne ihn zu brechen**.

## Referenzbilder
Selbst erstellte, beschriftete Referenzbilder (frei nutzbar, Übersicht: `assets/bilder/README.md`).

![Monetarisierung: Produkte und Fairness](../assets/bilder/monetarisierung-produkte.png)
![Shop-Layout](../assets/bilder/ui-shop-layout.png)

## Produkttypen (Roblox) ✅/🟡
| Typ | Was | Typische Nutzung |
|---|---|---|
| **Gamepass** | Einmalkauf, dauerhaft | 2× Geld, VIP, Extra-Slot, Werkzeug |
| **Developer Product** | Mehrfach kaufbar | Währungspakete, Boosts, Wiederbeleben |
| **Abonnement (Subscriptions)** | Wiederkehrend | Monatliche Vorteile (prüfen, ob im Creator Hub verfügbar/Regeln) |
| **Premium-Engagement** | Verdienst durch Zeit, die Premium-Mitglieder im Spiel verbringen | Lange Sitzungen lohnen sich 🟠 (Details nicht bestätigt) |
| **Werbung / Creator Rewards** | Plattform-Programme | Regeln und Teilnahmebedingungen im Creator Hub prüfen |
| **Kosmetik/UGC-Items** | Aussehen | Skins, Emotes, Effekte |

## Zahlen (🟠, vor Nutzung prüfen)
- **Marketplace-Gebühr:** Roblox behält bei Verkäufen von Gamepasses/Items einen Anteil. Mehrere Quellen nennen **30 %** (Entwickler erhält ca. 70 %, Beispiel: 280 von 400 Robux). 🟠 → im Creator Hub bestätigen.
- **DevEx-Kurs:** Mehrere Seiten nennen **0,0035 US-$ pro Robux** (100.000 Robux ≈ 350 US-$). 🟠
- **Mindestbetrag für Auszahlung:** Quellen widersprechen sich (z. B. 30.000 Robux genannt). 🟠 → offizielle DevEx-Seite prüfen.
- **Auszahlungserhöhung:** Presse berichtet von einer Erhöhung der Auszahlungsraten um **8,5 %** im September 2025. 🟡 (Nasdaq/Benzinga). Zukünftiger DevEx-Auszahlungsanteil laut einer Bank grob 23,4 %. 🟡
- **Gesamtauszahlungen 2025:** Quellen zwischen ca. 1,1 und 1,5 Mrd. US-$. 🟠

**Regel für diese Datenbank:** Keine Zahl als Fakt in Projekt-Rechnungen verwenden, ohne sie im Creator Hub bestätigt zu haben.

## Designprinzipien (🧠)

### 1) Monetarisiere Zeit, Komfort und Aussehen
- **Komfort:** Mehr Inventar-Slots, Auto-Sammeln, Schnellreise.
- **Beschleunigung:** 2× Geld/XP (nicht Fortschritt blockieren, nur beschleunigen).
- **Kosmetik:** Skins, Effekte, Haustier-Aussehen, Basis-Deko.
- **Status:** Titel, Rahmen, VIP-Bereich (ohne Spielvorteil).

### 2) Spiel muss ohne Kauf fair sein
Nicht-Zahler müssen jedes Ziel erreichen können, nur langsamer. Sonst entsteht „Pay-to-win"-Ruf, Spieler brechen ab und Retention (Discovery-Signal) sinkt.

### 3) Erster Kauf früh und klein
- Ein günstiges Einstiegsangebot (z. B. Starter-Paket) nach dem ersten Erfolgserlebnis, nicht in den ersten 30 Sekunden.
- Preisstufen: klein, mittel, groß, mit sichtbarem Wertzuwachs.

### 4) Wert klar machen
- Konkrete Wirkung („2× Geld für 30 Minuten").
- Vorschau für Kosmetik.
- Keine versteckten Bedingungen.

### 5) Zeitpunkt
- **Gute Momente:** Nach einem Erfolg, bei einer Wand mit Alternativen, in Menüs.
- **Schlechte Momente:** Mitten im Kampf, direkt nach Niederlage (wirkt wie Ausnutzung), ständig wiederholende Popups.

### 6) Preisgestaltung
- Mehrere Preispunkte (Anker): ein hoher Preis macht den mittleren attraktiv.
- Pakete mit Bonus-Wert.
- Lokale Preise: Robux-Preise werden an Kaufpakete angepasst; krumme Preise testen.
- **A/B-Tests** (Preise, Position, Texte) mit ausreichend Spielern.

### 7) Whales und Kinder-Schutz
- Das Publikum ist jung: Keine Druck-Texte, kein Fake-Timer, keine „Schuld"-Formulierungen.
- Käufe klar bestätigen.
- Transparenz bei Zufallsprodukten (Wahrscheinlichkeiten), siehe `gacha-und-luck.md`.

## Produkt-Ideen nach Genre
| Genre | Gamepasses | Developer Products |
|---|---|---|
| Simulator | 2× Geld, Auto-Collect, Extra-Pets-Slot | Währungspakete, Luck-Boost (zeitlich) |
| Tycoon | Auto-Collect, VIP, 2× | Cash-Pakete |
| Survival/Koop | Extra-Slot, Kosmetik | Wiederbeleben, Start-Pakete |
| Kampf | Kosmetik-Effekte, Slots | Boosts, Reset-Optionen |
| Roleplay | Autos, Häuser-Slots, Kosmetik | Kleingeld-Items |
| Obby | Skip-Stage (vorsichtig), Effekte | Checkpoint/Skip-Pakete |

## Wirtschaft balancieren
- Premium-Boosts erhöhen die **Geschwindigkeit**, nicht die Obergrenze.
- Bedenke Inflation: Boosts + Rebirth multiplizieren sich. Rechne durch (siehe `progression-rebirth.md`).
- Verfolge **ARPDAU** (Umsatz pro täglich aktivem Nutzer), **Conversion** (Anteil Zahler), **ARPPU** (Umsatz pro Zahler), **Retention nach Kauf**.

## Technik-Hinweise
- Käufe nur **serverseitig** verarbeiten (`MarketplaceService`; Developer Products über `ProcessReceipt`, korrekt bestätigen, Idempotenz sichern). Details in `08-technik-luau/technik-grundlagen.md`.
- Gamepass-Besitz serverseitig prüfen und zwischenspeichern.
- Kaufprotokoll führen (Fehlersuche, Support).

## Verknüpfungen
`gacha-und-luck.md`, `progression-rebirth.md`, `01-markt-trends/discovery-algorithmus.md`, `04-ui-ux/hud-shop-menues.md`

## Quellen
- [DevEx Math 2026 – rowatcher](https://rowatcher.com/news/devex-math-in-2026-what-you-actually-take-home-per-1-000-players) 🟠
- [DevEx Requirements 2026 – rolearn](https://rolearn.dev/guidance/roblox-devex-requirements-2026) 🟠
- [Roblox raises creator payouts – Nasdaq](https://www.nasdaq.com/articles/roblox-raises-creator-payouts-will-margins-face-pressure-2026) 🟡
- [Analysts on payout hike – Benzinga](https://www.benzinga.com/analyst-stock-ratings/reiteration/25/09/47551437/roblox-analysts-cheer-developer-payout-hike-see-path-to-stronger-growth) 🟡
- [Creator Hub: Discovery](https://create.roblox.com/docs/discovery.md) ✅
