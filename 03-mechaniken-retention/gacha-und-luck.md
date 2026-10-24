# Gacha, Luck und Seltenheit

> Stand: 2026-10-24 · Gesamt-Vertrauen: 🟠 für Beispiele (Spiele-Guides), 🧠 für Designprinzipien. **Plattform-Richtlinien zu Zufallsbelohnungen vor Release offiziell prüfen.**

## Kurzfassung
Zufallsbelohnungen (Eier, Kisten, Mutationen, Drops) erzeugen Spannung und Geschichten. Sie sind auf Roblox weit verbreitet, aber sensibel: Das Publikum ist jung. Baue Zufall **transparent, fair und nie als Zwang**, und prüfe die aktuellen Roblox-Regeln (insbesondere zur Offenlegung von Wahrscheinlichkeiten bei bezahltem Zufall).

## Referenzbilder
Selbst erstellte, beschriftete Referenzbilder (frei nutzbar, Übersicht: `assets/bilder/README.md`).

![Gacha: Wahrscheinlichkeiten und Pity](../assets/bilder/gacha-wahrscheinlichkeiten-pity.png)
![Seltenheitsrahmen](../assets/bilder/ui-inventar-seltenheit.png)

## Wie Roblox-Spiele Zufall aufbauen
Beispiel *Ride a Pet* (Guide, 🟠): 22 Eier in 7 Seltenheitsstufen; vom einfachen Ei mit 1× Luck bis zu extremen Stufen (Billionen-Luck im Guide); Luck wird durch Pets, Mutationen und Rebirths gestapelt; Mutations-Multiplikatoren von 2× bis 100×.
Beispiel *Adopt Me* (Guide, 🟠): Seltenheit wird beim Schlüpfen zufällig bestimmt; Gamepasses können die Chancen erhöhen.

**Muster:**
1. **Eier/Kisten nach Stufen:** Höhere Stufe = teurer, größerer Pool.
2. **Luck-Stat:** Verschiebt Wahrscheinlichkeiten nach oben.
3. **Mutationen:** Zweite Zufallsschicht mit Multiplikatoren.
4. **Seltenheitsstufen:** Common, Uncommon, Rare, Epic, Legendary, Mythic, Secret etc.
5. **Sichtbarkeit:** Server-weite Meldungen bei seltenen Funden (Social Proof).

## Warum Zufall wirkt (🧠 Psychologie, allgemein)
- **Variable Belohnung:** Unvorhersehbare Belohnungen erzeugen mehr Anreiz als feste.
- **Geschichten:** „Ich hab ein Mythic gezogen!" ist erzählbar und teilbar.
- **Sammeldrang:** Fehlende Items in Büchern treiben Wiederkehr.
- **Beinahe-Gewinn:** Seltene Funde „fast" zu haben erhöht die Lust auf Wiederholung.
Diese Mechanismen sind stark. **Verantwortung:** Nutze sie für Spaß, nicht für Druck bei Kindern.

## Verantwortungsvolles Design
| Prinzip | Umsetzung |
|---|---|
| **Transparenz** | Wahrscheinlichkeiten anzeigen (bei bezahltem Zufall Pflicht nach Roblox-Regeln prüfen) |
| **Spielbar ohne Geld** | Seltene Items auch durch Spielen erreichbar |
| **Kein Zwang** | Kein Fortschritts-Block ohne Zufalls-Treffer |
| **Pity-System** | Garantierter Treffer nach X Versuchen (Frust-Schutz) |
| **Kein Druck** | Keine Fake-Countdowns, keine Schuld-Texte |
| **Handel erlaubt?** | Wirtschaft bedenken (Betrug, Scams) |
| **Kind-gerechte Texte** | Nicht „verpasse jetzt!", sondern ehrlich informieren |

## Design-Details

### Wahrscheinlichkeits-Tabelle (Beispiel, 🧠 Startpunkt)
| Stufe | Chance | Gefühl |
|---|---|---|
| Common | 60 % | Alltag |
| Uncommon | 25 % | Freude |
| Rare | 10 % | Highlight |
| Epic | 4 % | Aufregung |
| Legendary | 0,9 % | Geschichte |
| Mythic | 0,1 % | Server-Meldung |

### Pity-System (Beispiel)
- Nach 30 Würfen ohne Epic+ → garantiertes Epic.
- Nach 100 Würfen ohne Legendary → garantiertes Legendary.
- Zähler sichtbar machen.

### Luck-Stacking
- Begrenze Luck-Multiplikatoren (Obergrenze), sonst zerbrechen Seltenheiten.
- Luck-Boosts zeitlich begrenzt oder verdienbar, nicht nur kaufbar.

### Handel und Wert
- Seltene Items brauchen **Wertstabilität**, sonst sind Besitzer frustriert.
- Verhindere Duplikat-Bugs (Server-seitige Validierung, siehe `08-technik-luau/`).

## Alternativen zu reinem Zufall
- **Crafting:** Zutaten sammeln → Item herstellen (planbar).
- **Gezielte Kreuzung:** Regeln, die Spieler lernen können.
- **Erkunden:** Seltene Items an bestimmten Orten/Zeiten.
- **Aufträge:** Belohnung bei Aufgabe.
Ein Mix aus Zufall und Planbarkeit ist langfristig gesünder.

## Checkliste
- [ ] Wahrscheinlichkeiten angezeigt und korrekt implementiert
- [ ] Offizielle Roblox-Richtlinie zu Zufallsbelohnungen geprüft
- [ ] Pity-System vorhanden
- [ ] Spiel ohne Käufe durchspielbar
- [ ] Luck-Obergrenze gesetzt
- [ ] Keine Dark Patterns (Fake-Knappheit, Druck-Texte)
- [ ] Server-seitige Auslosung (Client darf nicht entscheiden)

## Quellen
- [Ride a Pet Eggs – games.gg](https://games.gg/roblox/guides/ride-a-pet-all-eggs-and-how-to-get-them/) 🟠
- Offizielle Roblox-Richtlinien (Creator Hub: Policies) ✅ → bei Update verlinken, hier nicht bestätigt
- Suchlücke: Psychologie-/Industriequellen zu Loot-Mechaniken noch nachrecherchieren
