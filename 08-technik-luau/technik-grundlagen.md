# Technik-Grundlagen (Luau)

> Stand: 2026-10-24 · Nächste Prüfung: 2027-01-24 · Gesamt-Vertrauen: ✅ für API-Namen, Limits und Sicherheitsregeln (gegen den lokal geklonten Quelltext der offiziellen Creator Docs geprüft, Snapshot `4e795e6` vom 24.10.2026; Links zeigen auf create.roblox.com/docs), 🟡 für Release-Termine aus DevForum/Presse, 🧠 für Architektur- und Designempfehlungen. Die Code-Beispiele dieser Datei wurden gegen die API-Referenz geprüft.

## Kurzfassung
Roblox-Spiele sind **Client-Server**: Der Server ist die Wahrheit, der Client ist nicht vertrauenswürdig ✅ ([Security tactics](https://create.roblox.com/docs/scripting/security/security-tactics)). Alles, was Wert hat (Währung, Items, Käufe, Fortschritt), wird **serverseitig** berechnet und gespeichert. Der Client zeigt nur an und sendet Wünsche. Diese Datei ist die **Übersicht**; die Details stehen in drei Vertiefungen:

| Thema | Datei | Inhalt |
|---|---|---|
| Daten speichern | [`datenspeicherung.md`](./datenspeicherung.md) | DataStore-Limits (Spiel- und Server-Budget), UpdateAsync, Session-Locking, Versionen, RTBF, MemoryStore, MessagingService, robustes Lade-/Speicher-Modul |
| Käufe und Sicherheit | [`kaeufe-und-sicherheit.md`](./kaeufe-und-sicherheit.md) | ProcessReceipt-Garantien, sicheres PurchaseId-Muster, BindReceiptHandler, Gamepasses, Remote-Limits, Validierung, Token Bucket, Server Authority, Anti-Exploit |
| Performance und Tooling | [`performance-und-tooling.md`](./performance-und-tooling.md) | Budgets, MicroProfiler, Script Profiler, Speicher, Parallel Luau, `--!native`, `const`, Require-by-String, Script Sync, Rojo, Studio MCP, Assistant, Luau Execution, IAS, Matchmaking, TextGenerator, 4D-Generierung |

## Referenzbilder
Selbst erstellte, beschriftete Referenzbilder (frei nutzbar, Übersicht: `assets/bilder/README.md`).

![Client-Server-Architektur](../assets/bilder/client-server-architektur.png)

Offizielle Abbildung aus den Roblox Creator Docs (Index: `assets/bilder/offiziell/README.md`):

![Performance-Kreislauf Design, Identify, Improve, Monitor](../assets/bilder/offiziell/performance/performance-workflow.png)
*Performance ist ein Kreislauf: mitdesignen, Probleme finden, verbessern, überwachen. Quelle: Roblox Creator Docs, CC BY 4.0*

## Architektur ✅/🧠
- **Server (`Script` in `ServerScriptService`):** Spiellogik, Ökonomie, Speichern, Validierung. Logik und Daten von Anfang an hier bzw. in `ServerStorage`, nie in replizierten Containern ✅ ([Security tactics](https://create.roblox.com/docs/scripting/security/security-tactics)).
- **Client (`LocalScript`):** UI, Eingabe, visuelle Effekte. Jedes replizierte LocalScript und ModuleScript kann dekompiliert werden ✅.
- **Gemeinsam (`ModuleScript` in `ReplicatedStorage`):** Konfiguration, Hilfsfunktionen. Achtung: Der Client lädt **alles** in `ReplicatedStorage` → Server-only-Inhalte nach `ServerStorage` ✅ ([Design for performance](https://create.roblox.com/docs/performance-optimization/design)).
- **Kommunikation:** `RemoteEvent` (zuverlässig, geordnet), `UnreliableRemoteEvent` (für häufige, unkritische Daten ≤ 1.000 Bytes), `RemoteFunction` (Anfrage/Antwort; `InvokeClient` meiden) ✅ ([Remote events and callbacks](https://create.roblox.com/docs/scripting/events/remote)).
- **Module laden:** klassisch `require(instanz)` oder **Require-by-String** (`./`, `../`, `@self/`, `@game/`); nicht blockierend ✅ ([LuaGlobals](https://create.roblox.com/docs/reference/engine/globals/LuaGlobals)).
- **Organisation:** Module pro System (Inventar, Wirtschaft, Pets), klare Schnittstellen, Zahlen (Preise, Chancen) in Konfigurationsmodulen, damit Balancing ohne Code-Umbau geht 🧠. Für unveränderliche Konfiguration `const` + `table.freeze()` ✅ ([Variables](https://create.roblox.com/docs/luau/variables)).
- **Kompetitive Spiele:** Server Authority (`Workspace.AuthorityMode = Server`, im Studio-Properties-Fenster gesetzt) macht den Server zur Wahrheit für Bewegung und Physik; Eingaben dann über das Input Action System ✅ ([Server authority model](https://create.roblox.com/docs/projects/server-authority)).

## Sicherheit (wichtigste Regeln) ✅
Details und Code: [`kaeufe-und-sicherheit.md`](./kaeufe-und-sicherheit.md).
1. **Nie dem Client vertrauen.** Exploiter feuern Remotes mit beliebigen Argumenten und Frequenzen; nur das erste Argument (`player`) ist echt ✅.
2. **Drei Validierungsebenen** für jeden Remote: Kontext/Berechtigung (Distanz, lebt, besitzt Schlüssel), Typ/Struktur (`typeof`, Länge, **Tabelle statt Instance**), Wert (Bereich, Ganzzahl, **NaN und ±inf per `math.isfinite` abweisen**) ✅ ([Client-server boundary](https://create.roblox.com/docs/scripting/security/client-server-boundary)).
3. **Berechnungen am Server:** Belohnungen, Zufalls-Drops, Preise, Schaden (Treffer per Server-Raycast prüfen) ✅.
4. **Rate-Limits am Server** (Token Bucket); client-seitige Cooldowns nie als einzige Verteidigung ✅. RemoteEvents: ca. **500 Anfragen/s pro Client**, geteilt über alle Events desselben Typs ✅ ([RemoteEvent](https://create.roblox.com/docs/reference/engine/classes/RemoteEvent)).
5. **ProximityPrompts, ClickDetectors, DragDetectors** wie Remotes behandeln: Exploiter lösen sie aus jeder Entfernung aus; nur `ProximityPrompt.Triggered` hat eine Server-Distanzprüfung ✅.
6. **Server als Türsteher**, nicht als Relais, bevor etwas per `FireAllClients` an alle geht ✅.
7. **Duplikat-Schutz:** Itemvergabe atomar (erst prüfen, dann ändern), Handel transaktional, Session-Locking für Spielerdaten ✅.
8. **Erkennen ohne Fehlurteile:** Heuristiken als Signale, Verdachts-Score, Konsequenz-Leiter, `Players:BanAsync` für Wiederholungstäter ✅ ([Server-side detection](https://create.roblox.com/docs/scripting/security/server-side-detection)).

## Daten speichern (Kurzfassung) ✅
Details, Limit-Tabellen und vollständiges Modul: [`datenspeicherung.md`](./datenspeicherung.md).
- **Ein Schlüssel pro Spieler** (`User_<UserId>`), eine Tabelle, im Server-Speicher bearbeitet; DataStore nur beim Laden, periodisch (Doku-Beispiel: **180 s**, mit zufälligem Versatz), beim Verlassen, in `BindToClose` (max. **30 s**, parallel speichern) und bei Käufen ✅ ([Best practices](https://create.roblox.com/docs/cloud-services/data-stores/best-practices)).
- **Limits auf zwei Ebenen:** Spiel-Budget pro Minute Read **300 + 40 × CCU**, Write **300 + 20 × CCU**, List 300 + 2 × CCU, Remove 300 + 40 × CCU, **geteilt mit Open Cloud**; dazu Server-Limits **60 + 40 × Spieler** (Standard-Read/Write/Remove) ✅ ([Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)). Die verbreitete Formel „60 + 10 × Spieler" ist überholt.
- Weitere Grenzen: **4 MB** pro Schlüssel, Durchsatz **25 MB/min lesen** und **4 MB/min schreiben** pro Schlüssel, Metadaten **≤ 300 Zeichen**, Speicher **500 MB + 1 MB × Lifetime-Nutzer** ✅.
- **`UpdateAsync` statt `SetAsync`** für alles, was vom alten Wert abhängt; Callback yieldet nicht und gibt UserIds und Metadaten mit zurück, sonst gehen sie verloren ✅.
- **Session-Locking** über eine GUID in den Metadaten (im selben `UpdateAsync`) ✅ ([Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing)). Community-Standard dafür: **ProfileStore**; ProfileService wird nicht mehr gepflegt 🟡.
- **Retries** mit exponentiellem Backoff und Jitter, **geordnet pro Schlüssel** ✅.
- **Fallback:** Wenn Laden fehlschlägt, mit Standarddaten spielen lassen, aber **Speichern und Käufe sperren** und den Spieler informieren ✅.
- Ein fehlgeschlagener Schreibaufruf garantiert nicht, dass nichts geschrieben wurde; zur Klärung mit `DataStoreGetOptions.UseCache = false` nachlesen ✅.
- **Versionen:** erste Schreiboperation pro Schlüssel und UTC-Stunde wird als Backup behalten, ältere Versionen verfallen **30 Tage** nach dem Überschreiben; vor Updates der Speicherlogik einen **Snapshot** (einmal täglich möglich) machen ✅ ([Versioning, listing, and caching](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching)).
- **Schema versionieren** (Feld `version` + Migration) 🧠.
- **RTBF/DSGVO:** automatische Lösch-Templates mit `{UserId}` (bis 100) einrichten ✅ ([Data store RTBF](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten)).
- **MemoryStore** für Flüchtiges: **64 KB + 1,2 KB × Nutzer** Speicher, **1.000 + 120 × CCU** Request Units/min, max. 45 Tage ✅ ([Memory stores](https://create.roblox.com/docs/cloud-services/memory-stores)).

## Käufe (Kurzfassung) ✅
Details und Code: [`kaeufe-und-sicherheit.md`](./kaeufe-und-sicherheit.md).
- **Gamepass:** Besitz am Server mit `UserOwnsGamePassAsync` prüfen (Ergebnis wird von Roblox gecacht), `PromptGamePassPurchaseFinished` **nur am Server** auswerten ✅ ([MarketplaceService](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService)).
- **Developer Product:** Gutschrift **nur** über `ProcessReceipt` (einmal, in einem Server-Script) oder das neuere `BindReceiptHandler` ✅. Vier Schritte: PurchaseId noch nicht verarbeitet? → im Speicher gutschreiben → PurchaseId vermerken → speichern; **erst dann** `PurchaseGranted`, sonst `NotProcessedYet` ✅ ([Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing)).
- `ProcessReceipt` hat **keinen zeitbasierten Retry** (erst beim nächsten Kauf oder Rejoin), **kein Timeout**, kann **parallel auf zwei Servern** laufen; ohne Callback werden Belege automatisch bestätigt ✅.
- Das Kurzbeispiel auf der Developer-Products-Seite speichert nichts und prüft nur den `pcall`-Erfolg → nicht produktiv nutzen 🧠.
- Preise dynamisch mit **`GetProductInfoAsync`** lesen (`GetProductInfo` ist veraltet) ✅. Spielübergreifende Verkäufe sind seit **30.05.2026** deaktiviert ✅ ([Developer products](https://create.roblox.com/docs/production/monetization/developer-products)).

## Performance (Kurzfassung) ✅
Details: [`performance-und-tooling.md`](./performance-und-tooling.md).
- **Budget:** 60 FPS = **16,67 ms** pro Frame; Server-Heartbeat max. 60/s; Server-Speicher **6,25 GiB + 100 MiB × Spitzen-Spielerzahl**, unter 50 % bleiben ✅ ([Identify](https://create.roblox.com/docs/performance-optimization/identify)).
- **Ereignisbasiert arbeiten** statt Dauerabfrage; `RunService`-Events (`Heartbeat`, `PreRender` …) nur für wirklich nötige Updates; lange Arbeit in Zeitscheiben mit `task.wait()` teilen ✅ ([Design for performance](https://create.roblox.com/docs/performance-optimization/design)).
- **Instanzen wiederverwenden** (Pooling, z. B. NPCs mit häufigem Respawn) statt ständig `Instance.new`/`Destroy` ✅ ([Improve performance](https://create.roblox.com/docs/performance-optimization/improve)).
- **Remotes bündeln und drosseln**, Effekte nur auf dem Client, Tweens auf dem Client ✅.
- **Instance Streaming** für große Welten (bei neuen Places Standard), statische Modelle auf `LevelOfDetail = SLIM`; Skripte müssen mit nachgeladenen Teilen umgehen ✅.
- **Memory-Leaks:** Verbindungen trennen; `Player`-Objekte und Charaktere werden beim Verlassen **nicht** automatisch zerstört → `Workspace.PlayerCharacterDestroyBehavior` aktivieren oder selbst aufräumen ✅.
- **Messen:** Developer Console (F9), MicroProfiler, Script Profiler, Luau Heap, Performance Dashboard; auf einem **günstigen Android-Gerät** testen (Android ≈ 65 % der Spieler, ~60 % davon mit 2–4 GB RAM) ✅ ([Test on hardware](https://create.roblox.com/docs/performance-optimization/test-on-hardware)).
- **Beschleuniger:** Parallel Luau (mehrere Actors, kein `require` in der parallelen Phase), `@native`/`--!native` für heiße, getypte Rechenfunktionen ✅.

## Code-Qualität und Werkzeuge ✅/🟡
- **Typprüfung:** `--!strict` für neue Module (Modi: `--!nocheck`, `--!nonstrict`, `--!strict`) ✅ ([Type checking](https://create.roblox.com/docs/luau/type-checking)). Der neue Type Solver ist seit Anfang 2026 Standard 🟡.
- **Benennung** konsistent, kleine Funktionen, Kommentare nur für das „Warum"; Konstanten in `LOUD_SNAKE_CASE` ✅ ([Variables](https://create.roblox.com/docs/luau/variables)).
- **Fehler loggen** (mit Kontext), aber keine sensiblen Daten 🧠.
- **Externer Editor / Versionskontrolle:** **Script Sync** (bis 10.000 Skripte pro synchronisierter Wurzel, nur Skripte und Ordner, ignoriert Attribute/Tags) oder **Rojo** für das ganze Projekt im Dateisystem, Versionen mit **Rokit** pinnen; dazu luau-lsp + Studio-Plugin „Luau Language Server Companion", Selene, StyLua ✅ ([Script Sync](https://create.roblox.com/docs/scripting/sync), [Third-party tools](https://create.roblox.com/docs/projects/external-tools)).
- **KI-Werkzeuge:** Studio hat einen eingebauten **MCP-Server** (u. a. `execute_luau`, Playtest-Steuerung) und Assistant mit **Planning Mode** ✅ ([Studio MCP](https://create.roblox.com/docs/studio/mcp)). Nur vertrauenswürdige Clients verbinden.
- **Tests:** Kritische Logik (Ökonomie, Zufall) als engine-unabhängige Module; automatisiert per **Open Cloud Luau Execution** (Skript ≤ 4 MB, ≤ 5 min, ohne Physik, aber mit echten DataStores → Test-Place) ✅ ([Luau Execution](https://create.roblox.com/docs/cloud/reference/features/luau-execution)). TestEZ ist archiviert, Jest-Lua ist die Community-Alternative 🟡.

## Zufall serverseitig 🧠/✅
- Zufall (Drops, Mutationen) **nur am Server**, mit einem `Random`-Objekt ✅ ([Random](https://create.roblox.com/docs/reference/engine/datatypes/Random)).
- Gewichtete Auswahl über kumulierte Gewichte 🧠.
- Pity-Zähler im Spielerprofil speichern (wird mit den Spielerdaten gesichert) 🧠.
- Wahrscheinlichkeiten **konfigurierbar** und für die Anzeige im UI nutzbar (Anzeige = Realität). Paid Random Items unterliegen eigenen Regeln (Odds-Anzeige), siehe `07-monetarisierung/monetarisierung.md` und die offizielle [Paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items)-Seite ✅.

## Beispiel: Gewichtete Auswahl (Luau)
Geprüft: alle verwendeten APIs (`Random.new`, `Random:NextNumber`, `math.isfinite`) stehen in der API-Referenz ✅. Gegenüber der früheren Fassung ergänzt: Gewichte werden validiert, und eine Liste statt eines Dictionarys sorgt für eine feste Reihenfolge (Dictionary-Iteration hat keine garantierte Reihenfolge; für die Wahrscheinlichkeit egal, für Tests und UI-Anzeige aber unpraktisch).
```lua
--!strict
local rng = Random.new()

export type WeightedEntry = { name: string, weight: number }

local function rollWeighted(entries: { WeightedEntry }): string
	local total = 0
	for _, entry in entries do
		assert(math.isfinite(entry.weight) and entry.weight >= 0, "ungültiges Gewicht: " .. entry.name)
		total += entry.weight
	end
	assert(total > 0, "Summe der Gewichte muss > 0 sein")

	local roll = rng:NextNumber() * total -- NextNumber() liefert [0, 1)
	local acc = 0
	for _, entry in entries do
		acc += entry.weight
		if roll < acc then
			return entry.name
		end
	end
	return entries[#entries].name -- Absicherung gegen Rundungsfehler
end

-- Beispiel
local EGG_ODDS: { WeightedEntry } = {
	{ name = "Common", weight = 60 },
	{ name = "Rare", weight = 30 },
	{ name = "Epic", weight = 9 },
	{ name = "Legendary", weight = 1 },
}
print(rollWeighted(EGG_ODDS))
```

## Beispiel: Sicherer Remote-Handler (Muster)
Geprüft: Das frühere Beispiel war korrekt; ergänzt um das offizielle Token-Bucket-Prinzip (Bursts erlaubt, Dauerrate begrenzt) statt eines starren Cooldowns, `time()` wie im Doku-Beispiel und Aufräumen beim Verlassen ✅ ([Client-server boundary](https://create.roblox.com/docs/scripting/security/client-server-boundary)). Vollständiges `TokenBucket`-Modul und weitere Validierung: [`kaeufe-und-sicherheit.md`](./kaeufe-und-sicherheit.md).
```lua
--!strict
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local sellRemote = ReplicatedStorage:WaitForChild("SellAll") :: RemoteEvent

-- Minimaler Token Bucket: max. 3 Aufrufe am Stück, danach 1 pro Sekunde
local CAPACITY = 3
local REFILL_PER_SECOND = 1
local buckets: { [Player]: { tokens: number, last: number } } = {}

local function allow(player: Player): boolean
	local now = time()
	local bucket = buckets[player]
	if bucket == nil then
		bucket = { tokens = CAPACITY, last = now }
		buckets[player] = bucket
	end
	bucket.tokens = math.min(CAPACITY, bucket.tokens + (now - bucket.last) * REFILL_PER_SECOND)
	bucket.last = now
	if bucket.tokens < 1 then
		return false
	end
	bucket.tokens -= 1
	return true
end

sellRemote.OnServerEvent:Connect(function(player: Player)
	if not allow(player) then
		return -- Spam verwerfen
	end
	-- Menge und Preis am Server aus dem Spielerprofil lesen, nie vom Client nehmen
end)

Players.PlayerRemoving:Connect(function(player: Player)
	buckets[player] = nil -- sonst wächst die Tabelle mit jedem Spieler (Speicherleck)
end)
```
(Muster zur Illustration; an die eigene Architektur anpassen und testen.)

## Do / Don't
| Do | Don't |
|---|---|
| Alles mit Wert am Server berechnen und speichern | Dem Client Preise, Mengen oder Belohnungen glauben |
| Remotes: Rate-Limit + Typ-, Wert-, Kontextprüfung | Zahlen ungeprüft verrechnen (NaN, inf) |
| `UpdateAsync` + Session-Lock + geordnete Retries | `SetAsync` für Spielerdaten aus mehreren Servern |
| Käufe idempotent über `PurchaseId`, erst speichern, dann bestätigen | `PurchaseGranted` ohne Speichern zurückgeben |
| Auf einem günstigen Android-Gerät messen | Nur auf dem Entwickler-PC testen |
| Verbindungen trennen, Spieler-Tabellen aufräumen | Pro-Spieler-Daten ewig im Speicher lassen |
| Konfiguration in Modulen, `const` + `table.freeze` | Magische Zahlen quer durch den Code |
| Script Sync oder Rojo + Git, Toolchain mit Rokit pinnen | Code nur in einer einzigen Place-Datei ohne Versionen |

## Checkliste
- [ ] Alle Wert-Logik am Server, Server-only-Inhalte in `ServerScriptService`/`ServerStorage`
- [ ] Remotes validiert (Kontext, Typ, Wert, `math.isfinite`) und am Server rate-limitiert
- [ ] ProximityPrompts/ClickDetectors am Server nachgeprüft
- [ ] DataStore: ein Schlüssel pro Spieler, `UpdateAsync`, Session-Lock, Retries mit Backoff
- [ ] Laden-Fehlschlag sperrt Speichern und Käufe
- [ ] Auto-Save mit Versatz, `PlayerRemoving` speichert, `BindToClose` speichert parallel (< 30 s)
- [ ] DataStore-Budget gerechnet (Spiel- **und** Server-Ebene)
- [ ] `ProcessReceipt`/`BindReceiptHandler` idempotent (PurchaseId), erst nach Speichern bestätigt
- [ ] Verbindungen werden getrennt, Player/Charaktere aufgeräumt
- [ ] Mobile-Performance auf echtem Gerät gemessen (Frame-Zeit, Speicher)
- [ ] Konfiguration ausgelagert, `--!strict` in neuen Modulen
- [ ] RTBF-Lösch-Templates eingerichtet
- [ ] Server Authority für kompetitive/physiklastige Spiele geprüft

## Quellen
- [Security and cheat mitigation tactics](https://create.roblox.com/docs/scripting/security/security-tactics), [Securing the client-server boundary](https://create.roblox.com/docs/scripting/security/client-server-boundary), [Server-side detection](https://create.roblox.com/docs/scripting/security/server-side-detection) – Creator Docs, Stand 24.10.2026, ✅
- [Remote events and callbacks](https://create.roblox.com/docs/scripting/events/remote), [RemoteEvent](https://create.roblox.com/docs/reference/engine/classes/RemoteEvent) – ✅
- [Data stores](https://create.roblox.com/docs/cloud-services/data-stores), [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits), [Best practices](https://create.roblox.com/docs/cloud-services/data-stores/best-practices), [Versioning, listing, and caching](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching), [Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing), [Data store RTBF](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten), [Memory stores](https://create.roblox.com/docs/cloud-services/memory-stores) – ✅
- [MarketplaceService](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService), [Developer products](https://create.roblox.com/docs/production/monetization/developer-products), [Paid random items](https://create.roblox.com/docs/production/monetization/paid-random-items) – ✅
- [Performance optimization](https://create.roblox.com/docs/performance-optimization), [Design for performance](https://create.roblox.com/docs/performance-optimization/design), [Identify](https://create.roblox.com/docs/performance-optimization/identify), [Improve](https://create.roblox.com/docs/performance-optimization/improve), [Test on hardware](https://create.roblox.com/docs/performance-optimization/test-on-hardware) – ✅
- [Server authority model](https://create.roblox.com/docs/projects/server-authority), [Type checking](https://create.roblox.com/docs/luau/type-checking), [Variables](https://create.roblox.com/docs/luau/variables), [LuaGlobals](https://create.roblox.com/docs/reference/engine/globals/LuaGlobals), [Random](https://create.roblox.com/docs/reference/engine/datatypes/Random) – ✅
- [Script Sync](https://create.roblox.com/docs/scripting/sync), [Third-party tools](https://create.roblox.com/docs/projects/external-tools), [Studio MCP](https://create.roblox.com/docs/studio/mcp), [Luau Execution](https://create.roblox.com/docs/cloud/reference/features/luau-execution) – ✅
- [DevForum: General Release Luau's New Type Solver](https://devforum.roblox.com/t/general-release-luau%E2%80%99s-new-type-solver/4084991) – 🟡
- [ProfileStore-Doku](https://madstudioroblox.github.io/ProfileStore/) – Community, 🟡
- Vertiefungen und Prüfprotokoll: `reports/Roblox Markt und Game Design.md`, `research_notes/Roblox Markt und Game Design/technik_luau.md`, `research_notes/Roblox Markt und Game Design/offizielle_doku_verifikation.md`
