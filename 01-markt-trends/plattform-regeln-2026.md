# Plattform-Regeln 2026 (Veröffentlichung, Alter, Chat, Zufallsitems, Links, Moderation)

> Stand: 2026-10-24 · Nächste Prüfung: monatlich (Regeln änderten sich 2026 mehrfach) · Gesamt-Vertrauen: ✅ für Werte aus der offiziellen Creator-Doku (verifiziert am Quelltext, Stand 24.10.2026), 🟡 für Newsroom/DevForum/Presse, 🟠 wo Quellen widersprechen

## Kurzfassung
Seit dem **19. Mai 2026** startet **jedes neue Spiel als 16+-Titel**. Für die 16+-Veröffentlichung reichen ein gutes, mind. 2 Tage altes Konto und ein Alterscheck. Für **alle Altersgruppen** braucht der Creator zusätzlich Verifikation (unter 18: Gesichtsschätzung, ab 18: Ausweis), 2FA, 2 Monate Roblox Plus/Premium **oder** eine rückzahlbare Gebühr von **1.000 Robux**, den vollständigen Fragebogen (Minimal/Mild/Moderate) und eine Evaluationsphase, die nach **250 Plays hoch engagierter, altersgeprüfter 16+-Nutzer in 60 Tagen** endet (nicht mehr 500/30). Die Abkürzung **Expedited Review** kostet **50.000 Robux** (nicht 100.000) ✅. Seit Januar 2026 ist **Chat weltweit an einen Alterscheck** gebunden; gechattet wird nur in ähnlichen Altersbändern. Bezahlte Zufallsitems brauchen **numerische Quoten vor dem Kauf** und ein PolicyService-Gate. **Social-Media-Links sind im Spiel verboten**, nur auf der Detailseite erlaubt (sichtbar für verifizierte 16+) ✅.

## Warum das wichtig ist
- Die Regeln entscheiden, **wen dein Spiel überhaupt erreichen darf**. Ein Kinderspiel ohne Freischaltung erreicht 2026 keine Kinder.
- Verstöße kosten Reichweite (Label, Moderation) oder machen ein Spiel unspielbar.
- Roblox nennt Alterschecks selbst als Gegenwind für Neukundengewinnung und Chat-basierte Virality ✅ ([Q1-2026-Brief](https://s27.q4cdn.com/984876518/files/doc_financials/2026/q1/Q1-2026-Earnings-Shareholder-Letter.pdf)). Design muss ohne freien Chat funktionieren.

## Referenzbilder
Offizielle Bilder aus der Roblox Creator Documentation (Übersicht: `assets/bilder/offiziell/README.md`) und selbst erstellte Bilder (`assets/bilder/README.md`).

![Gacha-Wahrscheinlichkeiten und Pity sichtbar](../assets/bilder/gacha-wahrscheinlichkeiten-pity.png)
*Selbst erstellt: Quoten als Prozent, die 100 % ergeben, sichtbar vor dem Kauf; Pity-Zähler. So sieht die Odds-Pflicht in der Praxis aus.*

![Shop mit klar beschriftetem Angebot](../assets/bilder/offiziell/ui-design/uiux-aufmerksamkeit-shop-bundles.png)
*Shop aus Dragon Adventures: Angebote klar beschriftet. Bei Zufallsitems braucht der Info-Auslöser eine Beschriftung wie „Info“ oder „Details“, ein bloßes (i) reicht nicht. Quelle: Roblox Creator Docs, CC BY 4.0.*

## Details

### 1. Chronik der Regeländerungen 2024–2026

| Datum | Änderung | Quelle / Vertrauen |
|---|---|---|
| April 2024 | Rights Manager (IP-Ansprüche) | [DevForum](https://devforum.roblox.com/t/introducing-rights-manager/2880717) ✅ |
| Nov 2024 | Unter 13: kein Zugang zu unbewerteten Spielen, Social Hangouts und freier 2D-Nutzererstellung | [DevForum 3249079](https://devforum.roblox.com/t/updating-experience-guideline-policies-to-keep-our-younger-users-safe/3249079); [TechCrunch](https://techcrunch.com/2024/11/07/roblox-adds-new-safety-measures-to-ban-kids-under-13-from-social-spaces) ✅/🟡 |
| Aug 2025 | Klarstellung romantische/sexuelle Inhalte; Hangouts mit privaten Räumen eingeschränkt (damals 17+) | [Roblox Newsroom](https://about.roblox.com/newsroom/2025/08/extending-roblox-policy-on-romantic-and-sexual-content) ✅ |
| 2025 | „Restricted“ von 17+ (ID) auf 18+ (altersgeprüft); unter 18 ohne Suche/Empfehlung für Restricted | [DevForum 3905863](https://devforum.roblox.com/t/updating-age-requirements-for-experiences-with-%E2%80%98restricted%E2%80%99-content-maturity-label/3905863) ✅ |
| 30.09.2025 | Frist für den Maturity-&-Compliance-Fragebogen; unbewertete Spiele danach unspielbar (historisch, siehe unten) | [DevForum 3899317](https://devforum.roblox.com/t/important-updates-unrated-experiences-and-changes-to-experience-pages/3899317) ✅ |
| Nov 2025 | Alterscheck für Chat angekündigt; ab erster Dezemberwoche in Australien, Neuseeland, Niederlande | [Roblox Newsroom](https://about.roblox.com/newsroom/2025/11/roblox-requires-age-checks-limits-minor-and-adult-chat) ✅ |
| 17.12.2025 | „New Requirements to Publish and Update Public Experiences“ (ID, Kauf, 100+ Spielstunden oder DevEx in 12 Monaten) | [DevForum 4143953](https://devforum.roblox.com/t/new-requirements-to-publish-and-update-public-experiences/4143953) ✅ |
| Anfang Jan 2026 | Alterscheck für Chat weltweit | [Roblox IR](https://ir.roblox.com/news/news-details/2026/Roblox-Requires-Users-Worldwide-to-Age-Check-to-Access-Chat/default.aspx); [DevForum 4226101](https://devforum.roblox.com/t/age-check-requirement-to-chat-now-live-globally/4226101) ✅ |
| 13.02.2026 | `TextChatService:GetChatGroupsAsync` | [DevForum 4337233](https://devforum.roblox.com/t/new-chat-apis-teleport-users-who-can-chat-together/4337233) ✅ |
| März 2026 | Echtzeit-KI-Moderation, Transparenz im Creator Analytics | [DevForum 4538721](https://devforum.roblox.com/t/new-transparency-into-proactive-safety-protections-in-creator-analytics/4538721) ✅ |
| 13.04.2026 | Roblox Kids (5–8) und Roblox Select (9–15) angekündigt | [Roblox IR](https://ir.roblox.com/news/news-details/2026/Roblox-Introduces-New-Age-Based-Accounts-and-Expanded-Parental-Controls-for-Users-Under-16/default.aspx); [TechCrunch](https://techcrunch.com/2026/04/13/roblox-introduces-kids-and-select-accounts-for-age-appropriate-access-to-games-and-chat/) ✅ |
| 17.04. / 11.05. / **19.05.2026** | Neue Veröffentlichungsregeln + Evaluationsprozess (angekündigt, aktualisiert, in Kraft) | [DevForum 4573166](https://devforum.roblox.com/t/new-publishing-requirements-evaluation-process-for-games/4573166) ✅ |
| 30.04.2026 | Neue Nutzungsbedingungen (KI-Werkzeuge, IP, Ableitungen) | [DevForum: Terms April 2026](https://devforum.roblox.com/t/updates-to-the-roblox-terms-of-use-april-2026/4548394) ✅ |
| 26.05.2026 | „Clarifying Requirements for Paid Random Items“ (Odds-Pflicht) | [DevForum 4654622](https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622) ✅ (Datum laut Sekundärquelle 🟡) |
| Juni 2026 | Globaler Start Kids/Select; Engagement-Ziel im Ads Manager; Expedited Review | [DevForum 4685717](https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717) ✅ |
| 19.08.2026 | Schwelle von 500 auf 250 Plays gesenkt (laut GEEIQ, offiziell nicht datiert) | [GEEIQ](https://geeiq.com/resources/blog/roblox-evaluation-changes-brands) 🟠 |
| 11.09.2026 | Creator unter 18 brauchen keinen Ausweis mehr für jüngere Zielgruppen (Alterscheck bleibt) | [RTC auf X](https://x.com/Roblox_RTC/status/2098520734536712672) 🟡 |
| Herbst 2026 | Roadmap: „relaxed Kids & Select requirements“; „deceptive game copy takedown“ | [Creator Roadmap Fall Update](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208) ✅ |
| 01.11.2026 | Weitere Neufassung der Nutzungsbedingungen (User Terms, Creator Terms) | [DevForum: Terms November 2026](https://devforum.roblox.com/t/updates-to-the-roblox-terms-of-use-november-2026/4907620) ✅ |

### 2. Veröffentlichen seit 19.05.2026 ✅
Quelle: [Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places); [Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)

| Anforderung | Veröffentlichung 16+ | Veröffentlichung für alle Altersgruppen |
|---|---|---|
| Konto | gutes Standing, mind. 2 Tage alt | wie 16+ |
| Alterscheck | Gesichtsschätzung oder Ausweis | wie 16+ |
| Verifikation | – | unter 18: Gesichtsschätzung; ab 18: Ausweis |
| 2FA | – | Pflicht |
| Bezahlhürde | – | 2 aufeinanderfolgende Monate Roblox Plus/Premium **oder** 1.000 Robux pro Spiel (rückzahlbar) |
| Fragebogen | Erste Frage „Nein“ → Label **„Content May Vary“**, nur altersgeprüfte 16+ | vollständig, Rating Minimal, Mild oder Moderate (9+) |
| Evaluation | – | Trial-Phase nur für altersgeprüfte 16+, bis **250 einzigartige Plays hoch engagierter, altersgeprüfter Nutzer in 60 Tagen**; Fortschritt stündlich im Dashboard „Audience Reach“ |
| Gilt für | **alle** Release-Aktionen: Updates, „Publish As“, Zielgruppenwechsel | dto. |

- **„Hoch engagiert“** heißt: Anforderungen an Kontoalter, Spielzeit im Spiel und Plattform-Ausgaben; der Nutzer hat „made a minimum purchase anywhere on Roblox in the last 60 days and have spent time in your game within that same window. They don't need to spend anything in your game specifically… your game doesn't need to be monetized.“ Geprüft wird über das „Realtime Multimodal Moderation system“ ✅. Genaue Schwellen für Kontoalter/Spielzeit: nicht dokumentiert.
- **Korrektur:** 500 Spieler in 30 Tagen (Mai-Start, Social Posts) gilt nicht mehr; offiziell 250 / 60 Tage ✅.
- **Expedited Review:** einmalig **50.000 Robux** pro Spiel, rückzahlbar; Prüfung in 48 h (bei kleinem Verstoß startet die Uhr nach erneuter Einreichung neu). Rückerstattung auf Antrag nach 90 Tagen, wenn das Spiel in gutem Standing bleibt und 25 hoch engagierte Spieler hält; keine Rückerstattung bei dauerhafter Moderation ✅. **Korrektur:** 100.000 Robux (Juni-Ankündigung, RTC) ist veraltet.
- **Rückzahlung der 1.000-Robux-Gebühr: Die Doku widerspricht sich** 🟠: Veröffentlichungsseite: „If your game maintains 25 highly engaged players for 60 days without moderation, you will receive a refund“. Kids/Select-FAQ: „automatically refunded 90 days after your game becomes eligible… If your game never reaches eligibility, it's still refunded 90 days after your initial payment date.“
- **Abo abgelaufen:** „your game stays published for all ages“ ✅. Bereits veröffentlichte Spiele müssen Alterscheck/Abo nicht dauerhaft halten 🟡 ([AMA](https://devforum.roblox.com/t/ama-publishing-requirements-roblox-kids-select/4580953?page=16)).
- **Limits:** bis zu **5 noch nie veröffentlichte Spiele pro Tag**; **Early Tester:** bis zu 10 Freunde ähnlichen Alters (z. B. 18+-Creator → 16+-Tester; 13–15-Creator → 9–17-Tester) ✅.
- Einige Konten erhielten ein kostenloses Plus (6 Monate); versehentlich gezahlte Gebühren werden automatisch erstattet ✅/🟡 ([Alternate Publishing Requirements](https://devforum.roblox.com/t/alternate-publishing-requirements-for-roblox-kids-and-select/4630944)).

### 3. Kontotypen und Zielgruppen ✅
Quelle: [Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)

| Kontotyp | Alter | Sichtbare Ratings | Chat-Standard |
|---|---|---|---|
| **Roblox Kids** | selbst angegeben oder geprüft 5–8 | Minimal, Mild | aus; nach Alterscheck über verknüpftes Elternkonto aktivierbar |
| **Roblox Select** | selbst angegeben 9+ (bis geprüft) oder geprüft 9–15 | Minimal, Mild, Moderate (9+) | aus bei selbst angegebenen Konten |
| **Roblox** (Standard) | altersgeprüft 16+ | alle außer Restricted (18+) | an |

- Globaler Start im Juni 2026 nach vier Startregionen; „tens of thousands of games“ in den Kids/Select-Katalogen ✅ ([DevForum 4685717](https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717)).
- Spiele mit sensiblen Themen, Social Hangouts oder freiem Zeichnen sind standardmäßig ausgeschlossen 🟡 ([Bloxy News](https://www.bloxy.news/post/roblox-kids-chat-restrictions-publishing-requirements)).

### 4. Maturity-Labels ✅
Quelle: [Content maturity and compliance](https://create.roblox.com/docs/production/promotion/content-maturity)

| Label | Erreicht | Typische Auslöser |
|---|---|---|
| Minimal / Mild | Roblox Kids (5–8), Roblox Select (9–15), Roblox 16+ | ergibt sich aus den Fragebogen-Antworten (Details im Fragebogen) |
| Moderate (9+) | Roblox Select (9–15) und Roblox 16+ (nicht Kids) | ergibt sich aus den Fragebogen-Antworten |
| Content May Vary | nur altersgeprüfte 16+ | Fragebogen nicht vollständig (erste Frage „Nein“) |
| Restricted | nur **altersverifizierte 18+**; in u. a. **Korea, Saudi-Arabien, Türkei** unspielbar | starke Gewalt, viel realistisches Blut, starke Sprache, Alkohol, romantische Themen, private Räume/Erwachsenen-Orte |

- **Social Hangouts:** ohne private Räume ab 16, **mit privaten Räumen nur altersverifizierte 18+** ✅. **Korrektur:** Die 17+-Schwellen von 2024/2025 sind überholt.
- Restricted zuweisen startet Server neu und entfernt alle nicht 18+-verifizierten Spieler ✅.
- **Frage 2 des Fragebogens:** „Does this game respect the ArePaidRandomItemsRestricted policy API?“ ✅
- **Unbewertete Spiele:** Die Frist 30.09.2025 steht nicht mehr in der aktuellen Doku. Heute erhält ein Spiel ohne vollständigen Fragebogen „Content May Vary“ (16+) statt gesperrt zu werden. Eine veraltete Seite sagt noch, unbewertete Spiele würden wie „Ages 13+“ behandelt; das widerspricht den aktuellen Seiten 🟠 ([Experience guidelines, veraltet](https://create.roblox.com/docs/production/promotion/experience-guidelines)).
- Moderatoren prüfen Antworten; ein abgelehnter Fragebogen entfernt das Label und macht das Spiel unspielbar, bis er neu ausgefüllt ist 🟡 ([DevForum 4815099](https://devforum.roblox.com/t/experience-moderatedinaccessible-for-inaccurate-maturity-rating/4815099)).
- Sexuelle Handlungen und reale Partnersuche sind überall verboten ✅ ([Roblox Newsroom Aug 2025](https://about.roblox.com/newsroom/2025/08/extending-roblox-policy-on-romantic-and-sexual-content)).

### 5. Alterscheck und Chat
- **Pflicht seit Anfang Januar 2026 weltweit** (wo Chat verfügbar ist). Methode: Gesichts-Altersschätzung über den Dienstleister Persona (Bilder/Videos werden direkt nach der Verarbeitung gelöscht), alternativ Ausweis (13+) oder Eltern-Verifikation ✅ ([Roblox Newsroom](https://about.roblox.com/newsroom/2025/11/roblox-requires-age-checks-limits-minor-and-adult-chat); [Safety Snapshot Dez 2025](https://about.roblox.com/newsroom/2025/12/safety-snapshot-age-checks-for-chat)).
- **Altersbänder:** unter 9, 9–12, 13–15, 16–17, 18–20, 21+. Chat innerhalb des eigenen und angrenzender Bänder (Beispiel: 12-Jährige chatten mit bis 15-Jährigen). Erwachsene und jüngere Teens standardmäßig getrennt; Ausnahme **Trusted Connections** 🟡 ([allthings.how](https://allthings.how/robloxs-new-chat-rules-explained-january-2026/)). Die Bänder stehen im Newsroom/Help Center, **nicht** in der Creator-Doku ✅ (verifiziert).
- Roblox nennt einen mittleren absoluten Fehler von **1,4 Jahren** für unter 18-Jährige 🟡 ([Roblox IR](https://ir.roblox.com/news/news-details/2026/Roblox-Requires-Users-Worldwide-to-Age-Check-to-Access-Chat/default.aspx)).
- Alterschecks gelten auch für **Team Create** und Links ✅ ([DevForum 4079702](https://devforum.roblox.com/t/age-checks-to-access-chat-studio-team-create-and-links-on-roblox/4079702); [DevForum 4117693](https://devforum.roblox.com/t/age-check-notifications-in-studio-and-creator-hub/4117693)).
- Ein Entwickler behauptet, Fehleinstufungen hätten „a massive dent in the traffic“ verursacht (Meinung, keine Daten) 🟠 ([DevForum 4226101](https://devforum.roblox.com/t/age-check-requirement-to-chat-now-live-globally/4226101/print)).
- Aus der Vorversion (weiterhin 🟡, Status prüfen): Gruppen können altersgeprüften 18+-Mitgliedern Lesezugriff auf Experience-Chat geben; geplant waren Chat-Zusammenfassungen und Kommunikationsmetriken ([DevForum 6. Feb 2026](https://devforum.roblox.com/t/february-6-2026-an-update-on-our-age-check-to-chat-fast-follow-roadmap/4340230); [DevForum 26. März 2026](https://devforum.roblox.com/t/march-26-2026-an-update-on-our-age-check-to-chat-fast-follow-roadmap/4539685)).

### 6. Chat-APIs und erlaubte Kommunikation über Altersgrenzen ✅
- **`TextChatService:GetChatGroupsAsync`** (serverseitig): liefert sortierte Arrays von Chat-Gruppen-IDs; Spieler mit gleicher ID können synchron chatten. Für Matchmaking/Teleports gedacht, effizienter als paarweises `CanUsersChatAsync()` (N²). IDs sind pro Universe, ändern sich und dürfen nach dem Verlassen nicht gespeichert werden. Aktivieren unter Experience Settings ⟩ Communication („Chat & Voice Groups APIs“); in Studio nur im Team Test. Voice-Gegenstück existiert ([TextChatService](https://create.roblox.com/docs/reference/engine/classes/TextChatService)). Einzelner Bug-Report: leeres Array beim Join 🟠 ([DevForum 4540533](https://devforum.roblox.com/t/textchatservicegetchatgroupsasync-not-reliably-returning-chat-groups-on-join/4540533)).
- **Preset-Systeme** sind erlaubt, wenn sie „purely to help players communicate in-game actions, confirmations, or basic reactions“ dienen, auch über Altersgrenzen. **Verboten:** „back-and-forth dialogue across age groups“, Buchstabenräder/Zahlencodes, Smalltalk wie „Hi!“ „Hello!“ „How are you?“ ([Preset system guidelines](https://create.roblox.com/docs/chat/preset-system-guidelines)).
- **Quick Words:** bis zu 3 eigene Kategorien mit 3–10 Begriffen, je unter 25 Zeichen, nur auf Englisch eingegeben, automatisch übersetzt, vor Livegang geprüft ([Quick Words](https://create.roblox.com/docs/chat/quick-words)).
- **Korrektur zur Vorversion:** Statt „Roblox rät vom eigenen Preset-System ab, Dienst geplant“ gibt es jetzt offizielle Preset-Richtlinien und Quick Words.
- Eigene Chat-UIs müssen Nachrichten weiter über TextChatService schicken (Filter, Altersgating) 🟡 ([DevForum](https://devforum.roblox.com/t/how-to-make-a-custom-chat-system-using-textchatservice/4097288)).

### 7. PolicyService ✅
`GetPolicyInfoForPlayerAsync` liefert u. a.: `AreAdsAllowed`, `ArePaidRandomItemsRestricted`, `IsContentSharingAllowed`, `IsEligibleToPurchaseCommerceProduct`, `IsEligibleToPurchaseSubscription`, `IsPaidItemTradingAllowed`, `IsPhotoToAvatarAllowed`, `IsSubjectToChinaPolicies`, `IsEndlessContentLoadAllowed`, `IsEndlessContentAutoplayAllowed`. **`AllowedExternalLinkReferences`: „This is a legacy field. It always returns an empty array.“** ([PolicyService](https://create.roblox.com/docs/reference/engine/classes/PolicyService))

### 8. Bezahlte Zufallsitems (Lootboxen, Eier, Spins) ✅
Quelle: [Paid random items policy guidelines](https://create.roblox.com/docs/production/monetization/paid-random-items); [Monetization](https://create.roblox.com/docs/production/monetization)

- **Geltungsbereich:** direkte Robux-Käufe **und** indirekte über Spielwährung, die mit Robux gekauft wurde (Schlüssel, Re-Roll-Tokens, Spin-Tickets). Kostenlose Zufallsbelohnungen ohne Robux brauchen keine Offenlegung.
- **Quoten:** alle möglichen Ergebnisse mit echten numerischen Wahrscheinlichkeiten **vor dem Kauf**, als Prozent, die **genau 100 %** ergeben. Lange Listen dürfen hinter einem Pop-up liegen, der Auslöser braucht aber eine Beschriftung wie **„Info“ oder „Details“**; ein bloßes (i) reicht **nicht**.
- **Rundung:** auf vier oder mehr Nachkommastellen unterhalb der ersten Nicht-Null-Stelle, plus Hinweis.
- **Einmalige Ergebnisse:** Wenn ein Ergebnis nur einmal erhältlich ist, müssen die Quoten der übrigen aktualisiert werden.
- **Glücks-Items** (Luck-Boosts, Pity, erhöhte Drops, Rate-up): Wirkung numerisch erklären, Quoten dynamisch aktualisieren, solange aktiv.
- **Item-Typen:** Capsule, Enhancement, Combination, Probability modifier.
- **Wenn `ArePaidRandomItemsRestricted` = true**, eine von sechs Behandlungen: (1) unbezahlter erspielbarer Weg, (2) feste, nicht zufällige Reihenfolge, (3) Direktkauf zum **Erwartungswert** (Beispiel: 10-Robux-Box mit 5 % Chance → 200 Robux direkt), (4) entfernen/verstecken, (5) mit Fehlermeldung blockieren, (6) wegteleportieren.
- **Wenn `IsPaidItemTradingAllowed` = false:** Ergebnisse bezahlter Zufallsitems oder anderer bezahlter Items dürfen nicht gehandelt werden.
- Weitere Regel: „A discount is not genuine if an item is always 'on sale' for the same amount of Robux.“
- **Regulierte Märkte** (Australien, Belgien, Niederlande, UK, Brasilien) nennt eine Sekundärquelle; die Doku nennt keine Länder 🟡. Bekannt: UK unter 18 und Australien eingeschränkt; Brasilien unter 18 gesperrt, ab 31.03. auch nicht altersgeprüfte Erwachsene 🟡 ([DevForum UK](https://devforum.roblox.com/t/update-on-paid-random-items-restriction-for-uk-users-under-18/3072183); [DevForum AU](https://devforum.roblox.com/t/update-on-paid-random-items-restriction-for-australian-users/3153602)). Treiber der globalen Offenlegung soll Koreas Lootbox-Gesetz sein (unbestätigt) 🟠 ([TechTimes](https://www.techtimes.com/articles/319148/20260626/koreas-loot-box-rules-push-roblox-disclose-item-odds-worldwide.htm)).
- Testen im Studio-„Player Emulator“ 🟡 ([ZehnStudio26](https://zehn-studio26.com/news/paid-random-items-odds-disclosure/)).

### 9. Links, Teilen, Social Media ✅
- „Roblox's Community Standards only permit you to share social media links on your game's main details page. You **cannot** share social media links directly within a game.“ Erlaubt im Spiel ist nur ein Hinweis wie „Check out our social media links on our game's page“.
- Bis zu **drei Links**; Hinzufügen erfordert Altersverifikation als 16+; „Users who are under 16 years old or who have not verified their age cannot view social media links.“ Verlassen alle 16+-verifizierten Mitarbeiter eine Gruppe, werden die Links nach 90 Tagen gelöscht.
- Quelle: [Social media links](https://create.roblox.com/docs/production/promotion/social-media-links)
- **Korrektur:** Ein Discord-Button im Spiel ist auch mit PolicyService-Prüfung nicht erlaubt.
- Unter 13-Jährige dürfen grundsätzlich keine Links teilen ✅ ([Privacy Policy](https://en.help.roblox.com/hc/en-us/articles/115004630823-Roblox-Privacy-and-Cookie-Policy)).

### 10. Nutzungsbedingungen, KI-Inhalte, IP
- **30.04.2026:** vereinfachte Bedingungen, Klarstellungen zu KI-Werkzeugen und deren Datennutzung, IP-Werkzeugen und Ableitungen ✅ ([Roblox Help](https://en.help.roblox.com/hc/en-us/articles/14663412502676-Roblox-is-Updating-our-Terms-of-Use)).
- EWR/UK/CH: Roblox beansprucht kein Eigentum an neuem IP in KI-„Outputs“; Prompts und Outputs gelten als UGC, der Creator ist allein verantwortlich ✅ ([Roblox Help EWR](https://en.help.roblox.com/hc/en-us/articles/52986438082068-Roblox-is-Updating-our-Terms-of-Use-for-the-European-Economic-Area-the-United-Kingdom-and-Switzerland)).
- **01.11.2026:** Sprache vereinfacht, Abschnitte neu geordnet (User/Creator Terms) ✅.
- **Echtzeit-KI-Moderation (März 2026):** multimodal; wiederholte Verstöße in einer Server-Instanz schließen nur diesen Server; geplant: „Safety Callback API“ ✅.
- **Rights Manager:** zentrale Entfernungsanträge; ein „Claim“ ist keine DMCA-Mitteilung; unbestrittene Inhalte werden aus Marketplace/Creator Store entfernt ✅ ([IP Platform Terms](https://en.help.roblox.com/hc/en-us/articles/21857240911380-IP-Platform-Terms-of-Use)). Beschwerden 2025 über monatelange Bearbeitung und falsche Takedowns 🟠.

### 11. Monetarisierung gegenüber Minderjährigen (Kontext)
Ausführlich zu fairer Gestaltung und Recht: `07-monetarisierung/ethik-und-recht.md`; Zufallsmechaniken: `03-mechaniken-retention/gacha-und-luck.md`.

- University of Sydney (2026): irreführende Kaufgestaltung in 14 von 15 populären Spielen; Monash: 58 % sahen 10+ Dark Patterns in 12 Monaten 🟡 ([ACS Information Age](https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html); [Sydney-Bericht](https://ses.library.usyd.edu.au/bitstream/handle/2123/35033/Misleading%20and%20Deceptive%20Monetisation%20in%20Roblox%20-%20Final.pdf?sequence=3&isAllowed=y)).
- Mai 2026: Beschwerde von Interessengruppen gegen künstlich verknappte Items, Lootboxen und die Robux-Schicht (ob bei der FTC, ist zwischen Quellen strittig) 🟡 ([Fortune](https://fortune.com/2026/05/20/exclusive-advocacy-groups-file-complaint-roblox-manipulative-design/)).
- Klage nach Texas Deceptive Trade Practices Act läuft; Vergleiche mit Alabama, Nevada, West Virginia im April 2026 ✅ ([10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051082/rblx-20260630.htm)).
- Roblox: nur 1,4 % der 132 Mio. DAU waren in Q1 2026 Zahler 🟡.

## Beispiele aus echten Spielen
- Kein Studio hat öffentlich Zahlen zur Wirkung der 16+-Startphase genannt. 🧠 Erwartbar ist: Kids-Spiele (Obby, Simulator) spüren die Hürde stärker als Shooter/Horror für 16+.
- Grow a Garden wurde für lootbox-ähnliche Samen-Drops kritisiert 🟠 ([GameDaily](https://gamedaily.com/games/everything-about-grow-a-garden-the-cozy-idle-sim-revolutionizing-roblox-revenue)). Mit der Odds-Pflicht müssen solche Systeme heute Quoten zeigen.

## Was heißt das für dich (🧠)
1. **Launch-Plan nach Zielgruppe:**
   - Spiel für 16+: Alterscheck, „Content May Vary“ oder vollständiger Fragebogen, fertig.
   - Spiel für alle: Verifikation + 2FA + Plus/1.000 Robux + Fragebogen + 250 hoch engagierte 16+-Plays in 60 Tagen. Plane eine **16+-Testphase** (Freunde 16+, Discord, ggf. Ads-Ziel „Engagement“) oder budgetiere **50.000 Robux** Expedited Review.
2. **Rating bewusst wählen:** Moderate verliert die 5–8-Jährigen; Restricted verliert alle unter 18 und einige Länder.
3. **Spiel ohne freien Chat voll spielbar machen:** Pings, Emotes, Presets, Quick Words, strukturierte Tausch-UIs.
4. **Zufallsitems von Tag 1 compliant bauen:** Odds-Panel mit „Info“-Label, PolicyService-Gate, Direktkauf-Alternative zum Erwartungswert, Luck-Anzeige dynamisch.
5. **Keine Social-Links im Spiel.** Nur der Hinweis auf die Detailseite.
6. **KI-Assets sind deine Verantwortung** (UGC). Rechte prüfen.

## Do / Don't
| Do | Don't |
|---|---|
| Zielgruppe vor dem Bau festlegen (16+ vs. alle) | Ein Kinderspiel bauen und die Evaluation vergessen |
| Fragebogen ehrlich und vollständig ausfüllen | Rating „optimieren“, um mehr Reichweite zu bekommen |
| Lobbys über `GetChatGroupsAsync` bilden | Gruppen teleportieren, die nicht miteinander reden dürfen |
| Presets/Quick Words für Koordination | Buchstabenräder oder Smalltalk-Presets |
| Quoten mit „Info“-Button vor dem Kauf | Nur ein (i)-Symbol |
| Hinweis „Links auf der Spielseite“ | Discord-Button im Spiel |
| Eigene Preise live lesen (Managed Pricing) | Fake-Countdowns und Dauer-„Rabatte“ |

## Checkliste vor Release
- [ ] Creator-Konto: Alterscheck, gutes Standing, mind. 2 Tage alt
- [ ] Für alle Altersgruppen: Verifikation, 2FA, Plus/Premium (2 Monate) oder 1.000 Robux
- [ ] Maturity-&-Compliance-Fragebogen vollständig, Rating passt zum Inhalt
- [ ] Plan für 250 hoch engagierte 16+-Plays in 60 Tagen (oder Expedited Review 50.000 Robux)
- [ ] Audience-Reach-Dashboard beobachtet
- [ ] Spiel ohne Chat voll spielbar; Presets nur für Spielaktionen
- [ ] Chat-Funktionen über TextChatService; Lobbys über `GetChatGroupsAsync`
- [ ] Zufallsitems: Quoten (100 %), „Info“-Label, PolicyService-Gate, Alternative, Trading-Sperre bei `IsPaidItemTradingAllowed` = false
- [ ] Keine Social-Media-Links im Spiel; max. 3 auf der Detailseite
- [ ] KI-generierte Assets auf Rechte geprüft
- [ ] Reporting-/Moderationswege vorhanden

## Offene Fragen / Recherche-Bedarf
- Genaue Schwellen für „Kontoalter“ und „Spielzeit“ in der Definition „hoch engagiert“.
- Widerspruch bei der Rückzahlung der 1.000-Robux-Gebühr (25 Spieler/60 Tage vs. 90 Tage nach Berechtigung).
- Details der „relaxed Kids & Select requirements“ (Roadmap Herbst 2026).
- Regeln für Voice-Chat-Berechtigung 2025/26 nicht geprüft.
- Liste regulierter Lootbox-Märkte nicht in der Doku.

## Quellen
- [Creator Docs: Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places) – Stand 24.10.2026, ✅
- [Creator Docs: Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select) – ✅
- [Creator Docs: Content maturity and compliance](https://create.roblox.com/docs/production/promotion/content-maturity) – ✅
- [Creator Docs: Paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items) – ✅
- [Creator Docs: PolicyService](https://create.roblox.com/docs/reference/engine/classes/PolicyService) – ✅
- [Creator Docs: TextChatService](https://create.roblox.com/docs/reference/engine/classes/TextChatService) – ✅
- [Creator Docs: Preset system guidelines](https://create.roblox.com/docs/chat/preset-system-guidelines) / [Quick Words](https://create.roblox.com/docs/chat/quick-words) – ✅
- [Creator Docs: Social media links](https://create.roblox.com/docs/production/promotion/social-media-links) – ✅
- [DevForum: New Publishing Requirements & Evaluation Process](https://devforum.roblox.com/t/new-publishing-requirements-evaluation-process-for-games/4573166) – Apr/Mai 2026, ✅
- [DevForum: Kids and Select Global Launch](https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717) – Jun 2026, ✅
- [DevForum: Clarifying Requirements for Paid Random Items](https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622) – Mai 2026, ✅
- [Roblox Newsroom: Age Checks for Communication](https://about.roblox.com/newsroom/2025/11/roblox-requires-age-checks-limits-minor-and-adult-chat) – Nov 2025, ✅
- [Roblox IR: Worldwide Age-Check](https://ir.roblox.com/news/news-details/2026/Roblox-Requires-Users-Worldwide-to-Age-Check-to-Access-Chat/default.aspx) – Jan 2026, ✅
- [DevForum: Age Check Requirement Live Globally](https://devforum.roblox.com/t/age-check-requirement-to-chat-now-live-globally/4226101) – ✅
- [DevForum: New Chat APIs (4337233)](https://devforum.roblox.com/t/new-chat-apis-teleport-users-who-can-chat-together/4337233) – Feb 2026, ✅
- [Roblox IR: Kids and Select](https://ir.roblox.com/news/news-details/2026/Roblox-Introduces-New-Age-Based-Accounts-and-Expanded-Parental-Controls-for-Users-Under-16/default.aspx) – Apr 2026, ✅
- [DevForum: Terms of Use April 2026](https://devforum.roblox.com/t/updates-to-the-roblox-terms-of-use-april-2026/4548394) / [November 2026](https://devforum.roblox.com/t/updates-to-the-roblox-terms-of-use-november-2026/4907620) – ✅
- [DevForum: Creator Roadmap 2026 Fall Update](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208) – ✅
- [allthings.how: Chat-Regeln Januar 2026](https://allthings.how/robloxs-new-chat-rules-explained-january-2026/) – 🟡
- [GEEIQ: Evaluation Changes](https://geeiq.com/resources/blog/roblox-evaluation-changes-brands) – Sep 2026, 🟠
- [Fortune: Advocacy complaint](https://fortune.com/2026/05/20/exclusive-advocacy-groups-file-complaint-roblox-manipulative-design/) – Mai 2026, 🟡
