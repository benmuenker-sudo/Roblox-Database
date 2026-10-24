# Käufe und Sicherheit (ProcessReceipt, Remotes, Server Authority)

> Stand: 2026-10-24 · Nächste Prüfung: 2027-01-24 · Gesamt-Vertrauen: ✅ für API-Garantien, Limits und Sicherheitsregeln (gegen den Quelltext der offiziellen Creator Docs, Snapshot `4e795e6` vom 24.10.2026, geprüft), 🟡 für Release-Zeitpunkte aus DevForum/Presse, 🧠 für eigene Code-Muster und Designempfehlungen

## Kurzfassung
- **Der Client ist nie vertrauenswürdig.** Exploiter können Remotes mit beliebigen Argumenten und in beliebiger Frequenz feuern, LocalScripts dekompilieren, ihre Figur teleportieren und ProximityPrompts aus jeder Entfernung auslösen ✅ ([Security tactics](https://create.roblox.com/docs/scripting/security/security-tactics)).
- **Developer Products** werden ausschließlich über `ProcessReceipt` (oder das neuere `BindReceiptHandler`) gutgeschrieben, **idempotent über die `PurchaseId`** und erst nach erfolgreichem Speichern bestätigt ✅ ([Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing)).
- Das offizielle Kurzbeispiel auf der Developer-Products-Seite ist ein **Lehrbeispiel**: kein Speichern, kein Duplikatschutz, `PurchaseGranted` auch dann, wenn der Handler nichts zurückgibt 🧠.
- **RemoteEvents** und **UnreliableRemoteEvents**: je ca. **500 Anfragen pro Sekunde und Client**, geteilt über alle Events desselben Typs; Unreliable-Payloads über **1.000 Bytes** werden verworfen ✅ ([RemoteEvent](https://create.roblox.com/docs/reference/engine/classes/RemoteEvent), [UnreliableRemoteEvent](https://create.roblox.com/docs/reference/engine/classes/UnreliableRemoteEvent)).
- **Server Authority** (`Workspace.AuthorityMode = Server`) macht den Server zur einzigen Wahrheit für Bewegung und Physik, mit Client-Vorhersage und Rollback ✅ ([Server authority model](https://create.roblox.com/docs/projects/server-authority)). Seit Juli 2026 für alle verfügbar 🟡. Ökonomie, Schaden und Inventar müssen trotzdem serverseitig validiert werden.

## Referenzbilder
Selbst erstelltes, beschriftetes Referenzbild (frei nutzbar, Übersicht: `assets/bilder/README.md`). Validierung, Kaufabwicklung und Speichern liegen ausschließlich rechts, auf dem Server.

![Client-Server-Architektur mit Validierung und MarketplaceService auf dem Server](../assets/bilder/client-server-architektur.png)

## Warum das wichtig ist
Ein einziger ungeprüfter Remote („gib mir Münzen", „kauf Item mit Preis X") reicht, um eine Ökonomie zu zerstören. Duplikations-Exploits über Handel und Serverwechsel sind laut Doku „a common source of item duplication exploits" ✅. Fehlerhafte Kaufabwicklung kostet seit 2026 zusätzlich Reichweite: Roblox prüft `ProcessReceipt` laufend und blendet fehlerhafte Developer Products auf Flächen außerhalb des Spiels aus ✅ ([Developer products](https://create.roblox.com/docs/production/monetization/developer-products)).

---

## Teil A: Käufe

### 1. Developer Products: Eckdaten ✅
Quelle: [Developer products](https://create.roblox.com/docs/production/monetization/developer-products)

| Punkt | Wert / Regel |
|---|---|
| Preis | **1 bis 1.000.000.000 Robux** ✅ |
| Icon | max. **512 × 512 px**, `.jpg`/`.png`/`.bmp`, wichtige Details innerhalb des Kreises ✅ |
| Voraussetzung | Spiel veröffentlicht und erreichbar ✅ |
| Spielübergreifende Verkäufe | **ab 30. Mai 2026 deaktiviert** (gilt auch für Passes); Alternative: Robux-Transfers ✅ |
| Verkauf außerhalb des Spiels | Produkt im Shop als **Listed** markieren **und** `ProcessReceipt` korrekt implementieren ✅ |
| Kontrolle | Roblox prüft die Implementierung laufend; fehlerhafte Produkte erscheinen als Banner/Report in Creator Hub ⟩ Monetization ⟩ Shop und verschwinden von externen Flächen, bis man „Mark as fixed" klickt ✅ |
| Kaufhistorie | Roblox speichert **keine** Developer-Product-Historie pro Nutzer; das ist Aufgabe des Spiels ✅ |
| Price Optimization | Preis-Skripte auf dem **Client** ausführen, damit Nutzer personalisierte Preise sehen; `receiptInfo.CurrencySpent` enthält den tatsächlich gezahlten Betrag ✅ |
| Nicht verwenden | `PromptProductPurchaseFinished` zur Gutschrift; das Event bedeutet keinen erfolgreichen Kauf ✅ |

### 2. Garantien und Grenzen von `ProcessReceipt` ✅
Quelle: [MarketplaceService.ProcessReceipt](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService)

| Thema | Offizielles Verhalten |
|---|---|
| Wann aufgerufen | für alle offenen Käufe: bei Kaufabschluss, wenn ein erfolgreicher Kaufdialog erscheint, wenn der Nutzer einem Server beitritt |
| Erneuter Aufruf | **kein zeitbasierter Retry**; nach `NotProcessedYet` erst wieder beim nächsten Kauf des Nutzers oder beim Rejoin auf irgendeinen Server |
| Timeout | **keiner**; der Callback darf so lange yielden, wie der Server läuft |
| Kein Callback gesetzt | Belege werden **automatisch bestätigt** und sind danach nicht zurückholbar |
| Mehrere offene Käufe | Reihenfolge nicht deterministisch |
| Nutzer muss online sein | ja, für den Aufruf; nein, damit das Ergebnis im Backend landet |
| Parallelität | derselbe Kauf **kann gleichzeitig auf zwei Servern** laufen (Join auf Server B, bevor A fertig ist) |
| Backend-Fehler | auch nach `PurchaseGranted` kann die Bestätigung im Backend scheitern; der Kauf bleibt dann offen |
| Escrow | offene Käufe werden nach Ablauf des Escrows **weder entfernt noch erstattet** |
| Setzen | **nur einmal**, in **einem** Server-Script; muss alle Produkte abdecken |
| `receiptInfo` | `PurchaseId`, `PlayerId`, `ProductId`, `PlaceIdWherePurchased`, `CurrencySpent`, `CurrencyType` (immer Robux), `ProductPurchaseChannel` |

### 3. Das offizielle Kurzbeispiel und seine Schwächen
Kern des Beispiels von der Developer-Products-Seite (MIT-Code der Creator Docs, gekürzt):
```lua
local function processReceipt(receiptInfo)
	local userId = receiptInfo.PlayerId
	local productId = receiptInfo.ProductId
	local player = Players:GetPlayerByUserId(userId)
	if player then
		local handler = productFunctions[productId]
		local success, result = pcall(handler, receiptInfo, player)
		if success then
			return Enum.ProductPurchaseDecision.PurchaseGranted
		else
			warn("Failed to process receipt:", receiptInfo, result)
		end
	end
	return Enum.ProductPurchaseDecision.NotProcessedYet
end
MarketplaceService.ProcessReceipt = processReceipt
```
Die Doku sagt selbst: „The functions for handling each product ID must return `true` for the transaction to be successful" ✅. Der Code prüft aber nur `success` von `pcall`, nicht `result == true` 🧠. Weitere Schwächen (eigene Analyse 🧠, durch die API-Garantien oben begründet ✅):

| Schwäche | Folge |
|---|---|
| Nur `success` geprüft | Handler, die `nil` zurückgeben (z. B. Humanoid fehlt), führen trotzdem zu `PurchaseGranted` → Spieler zahlt, bekommt nichts |
| Gutschrift nur in `leaderstats` | nichts wird gespeichert; nach Rejoin ist der Kauf weg |
| Keine `PurchaseId`-Prüfung | läuft der Callback parallel auf zwei Servern, gibt es die Belohnung doppelt |
| Kein Warten auf geladene Daten | Kauf direkt nach dem Join landet in noch nicht geladenen Daten |
| Andere Beispiele der Seite nutzen `GetProductInfo` | die Methode ist **veraltet**, Nachfolger `GetProductInfoAsync` ✅ |

### 4. Das sichere Muster (offiziell dokumentiert) ✅
Quelle: [Implement player data and purchasing systems](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing)

Vor `PurchaseGranted` müssen vier Schritte erfolgreich sein:
1. Prüfen, dass die `PurchaseId` **noch nicht** als verarbeitet vermerkt ist.
2. Den Kauf in den **Spielerdaten im Speicher** gutschreiben.
3. Die `PurchaseId` in denselben Spielerdaten als verarbeitet vermerken.
4. Die Spielerdaten in den DataStore **schreiben**. Nur bei Erfolg `PurchaseGranted`, sonst `NotProcessedYet`.

Zusatzregeln aus derselben Doku ✅:
- Vorher sicherstellen, dass die Daten **geladen** und **ohne Fehler** geladen sind (mit Session-Lock sind sie dann aktuell). Beim Warten auf das Laden auch das Verlassen des Spielers beachten, damit der Callback nicht ewig blockiert.
- Ist die `PurchaseId` vermerkt **und gespeichert** → `PurchaseGranted`. Ist sie vermerkt, aber **nicht gespeichert** → `NotProcessedYet`.
- Scheitert Schritt 4, behält der Spieler den Kauf für die laufende Sitzung; ein späterer Auto-Save kann ihn noch sichern, beim nächsten Aufruf greift dann Schritt 1.
- Käufe nur zulassen, wenn das Laden geklappt hat (`hasErrored` im offiziellen Beispiel); Kaufdialoge im Client bei Lade-/Speicherfehlern deaktivieren.

### 5. Beispiel: idempotente Kaufabwicklung (Luau) 🧠/✅
Setzt das Modul `PlayerData` aus `datenspeicherung.md` voraus (Session-Lock, `purchaseIds`-Liste, `saveNowAsync`). Ein gemeinsamer Kern wird von `ProcessReceipt` **und** `BindReceiptHandler` genutzt.

```lua
--!strict
-- ModuleScript "ReceiptCore" in ServerScriptService
local Players = game:GetService("Players")
local ServerScriptService = game:GetService("ServerScriptService")

local PlayerData = require(ServerScriptService.PlayerData)
type Data = PlayerData.Data

local MAX_PURCHASE_IDS = 100 -- Liste begrenzen (Annahme: sehr alte Belege kommen nicht wieder)
local LOAD_TIMEOUT = 30

-- Jeder Handler ändert NUR Daten im Speicher und gibt true zurück, wenn alles geklappt hat.
-- Handler müssen "alles oder nichts" sein: erst prüfen, dann ändern.
local productHandlers: { [number]: (data: Data, receiptInfo: { [string]: any }) -> boolean } = {
	[123123] = function(data, _receiptInfo) -- 100 Münzen
		data.coins += 100
		return true
	end,
	[456456] = function(data, _receiptInfo) -- Trank ins Inventar
		data.inventory.Potion = (data.inventory.Potion or 0) + 1
		return true
	end,
}

local inProgress: { [string]: boolean } = {} -- gegen Doppelaufrufe auf diesem Server

local ReceiptCore = {}

-- Gibt true zurück, wenn der Kauf gutgeschrieben UND gespeichert ist.
function ReceiptCore.handle(receiptInfo: { [string]: any }): boolean
	local purchaseId = tostring(receiptInfo.PurchaseId)
	local player = Players:GetPlayerByUserId(receiptInfo.PlayerId)
	if player == nil or inProgress[purchaseId] then
		return false
	end
	inProgress[purchaseId] = true

	local result = false
	-- 0. Daten müssen geladen sein, und zwar ohne Fehler
	if PlayerData.waitForSessionAsync(player, LOAD_TIMEOUT) and PlayerData.canTransact(player) then
		local data = PlayerData.get(player)
		local handler = productHandlers[receiptInfo.ProductId]
		if data ~= nil and handler ~= nil then
			if table.find(data.purchaseIds, purchaseId) then
				-- 1. schon gutgeschrieben: nur sicherstellen, dass es gespeichert ist
				result = PlayerData.saveNowAsync(player)
			else
				local ok, granted = pcall(handler, data, receiptInfo)
				if ok and granted == true then -- 2. gutgeschrieben (im Speicher)
					table.insert(data.purchaseIds, purchaseId) -- 3. vermerken
					if #data.purchaseIds > MAX_PURCHASE_IDS then
						table.remove(data.purchaseIds, 1)
					end
					result = PlayerData.saveNowAsync(player) -- 4. speichern
				else
					warn("Handler fehlgeschlagen:", receiptInfo.ProductId, granted)
				end
			end
		elseif handler == nil then
			warn("Kein Handler für Produkt", receiptInfo.ProductId)
		end
	end

	inProgress[purchaseId] = nil
	return result
end

return ReceiptCore
```

Variante 1, klassisch mit `ProcessReceipt`:
```lua
--!strict
-- Script in ServerScriptService (ProcessReceipt nur EINMAL im ganzen Spiel setzen)
local MarketplaceService = game:GetService("MarketplaceService")
local ServerScriptService = game:GetService("ServerScriptService")
local ReceiptCore = require(ServerScriptService.ReceiptCore)

MarketplaceService.ProcessReceipt = function(receiptInfo: { [string]: any }): Enum.ProductPurchaseDecision
	if ReceiptCore.handle(receiptInfo) then
		return Enum.ProductPurchaseDecision.PurchaseGranted
	end
	return Enum.ProductPurchaseDecision.NotProcessedYet
end
```

Variante 2, neuer mit `BindReceiptHandler` ✅ ([MarketplaceService:BindReceiptHandler](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService)):
```lua
--!strict
local MarketplaceService = game:GetService("MarketplaceService")
local ServerScriptService = game:GetService("ServerScriptService")
local ReceiptCore = require(ServerScriptService.ReceiptCore)

-- Catch-all für alle Developer Products ohne eigenen gefilterten Handler
local connection = MarketplaceService:BindReceiptHandler(
	Enum.ReceiptType.DeveloperProduct,
	function(receiptInfo: { [string]: any }): Enum.ReceiptDecision
		if ReceiptCore.handle(receiptInfo) then
			return Enum.ReceiptDecision.Processed
		end
		return Enum.ReceiptDecision.NotProcessedYet
	end
)
-- connection:Disconnect() würde den Handler wieder abmelden
```
Fakten zu `BindReceiptHandler` ✅:
- Behandelt `Enum.ReceiptType.DeveloperProduct` sowie Robux-Transfers (`RobuxTransferSender`, `RobuxTransferReceiver`).
- **Gefiltert** (dritter Parameter: Liste von Produkt-IDs) oder **Catch-all** (ohne Filter). Filter werden für Transfer-Typen nicht unterstützt.
- Ein gebundener Handler hat **Vorrang** vor `ProcessReceipt`; passt keiner, fällt der Beleg an `ProcessReceipt` durch. So kann man schrittweise migrieren.
- Fehler, wenn für denselben Typ und dieselbe Produkt-ID schon ein Handler existiert oder schon ein Catch-all registriert ist.
- Zusatzfelder im Beleg: `ReceiptType`, bei Transfers `TransferRequestId`. Transfer-Belege landen auf dem Server, auf dem der Nutzer gerade ist (kein Rejoin nötig).
- Rückgabe: `RBXScriptConnection` (zum Abmelden).

### 6. Gamepasses ✅
Quellen: [MarketplaceService](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService), [Passes](https://create.roblox.com/docs/production/monetization/passes)
- `UserOwnsGamePassAsync(userId, gamePassId)` funktioniert auf Client und Server, das Ergebnis wird **gecacht**. Beim ersten Server-Beitritt nach dem Kauf liefert es immer `true`; Käufe außerhalb des Spiels während der Sitzung brauchen „mehrere Minuten" bis zum Cache-Update ✅.
- `PromptGamePassPurchaseFinished` **nur im Server-Script** auswerten; dort spiegelt `wasPurchased` das Endergebnis, im LocalScript darf man sich nicht darauf verlassen ✅. Das Event aktualisiert auch den Ownership-Cache ✅.
- `UserOwnsGamePassAsync` unterstützt **Transparent Batching**: mehrere gleichzeitig per `task.spawn` gestartete Aufrufe werden zu weniger HTTP-Anfragen gebündelt ✅ ([Transparent batching](https://create.roblox.com/docs/scripting/transparent-batching)).
- Gamepasses brauchen keinen `ProcessReceipt`-Fix, müssen für externe Verkäufe aber ebenfalls **Listed** sein ✅.

```lua
--!strict
-- Script in ServerScriptService
local MarketplaceService = game:GetService("MarketplaceService")
local Players = game:GetService("Players")

local VIP_PASS_ID = 0 -- eigene Pass-ID eintragen (nicht die Asset-ID)

local function applyVip(player: Player)
	player:SetAttribute("VIP", true) -- Server setzt, Client liest nur
end

local function checkOwnership(player: Player)
	local ok, owns = pcall(function()
		return MarketplaceService:UserOwnsGamePassAsync(player.UserId, VIP_PASS_ID)
	end)
	if ok and owns then
		applyVip(player)
	elseif not ok then
		warn("Pass-Prüfung fehlgeschlagen, später erneut versuchen:", owns)
	end
end

Players.PlayerAdded:Connect(checkOwnership)
for _, player in Players:GetPlayers() do
	task.spawn(checkOwnership, player)
end

MarketplaceService.PromptGamePassPurchaseFinished:Connect(function(player: Player, gamePassId: number, wasPurchased: boolean)
	if wasPurchased and gamePassId == VIP_PASS_ID then
		applyVip(player)
	end
end)
```

### 7. Preise und Produktinfos dynamisch lesen ✅
Quelle: [MarketplaceService:GetProductInfoAsync](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService)
- `GetProductInfo` ist **veraltet** → `GetProductInfoAsync(assetId, infoType)`. Für Developer Products `Enum.InfoType.Product`, für Passes `Enum.InfoType.GamePass`. Existiert die ID nicht, wirft die Methode einen Fehler → `pcall` ✅.
- Relevante Felder: `Name`, `Description` (kann `nil` sein), `PriceInRobux`, `UserBasePriceInRobux`, `PriceDiscountDetails` (Liste mit `Type`, `AmountInRobux`, `Percent`; Typ `"RobloxPlusSubscription"` für Plus-Rabatt), `ProductId`, `IsForSale`, `Created`/`Updated` (ISO 8601), `Creator` ✅.
- Im `Creator`-Feld ist `Id` überholt: **`CreatorTargetId` verwenden** ✅. Laut DevForum liefert die alte ID bei Gruppen-Produkten seit 2026 `0` 🟡 ([DevForum](https://devforum.roblox.com/t/updates-to-marketplaceservice-getproductinfo-return-values/4666671)).
- `GetDeveloperProductsAsync()` liefert ein `Pages`-Objekt mit allen Developer Products des Spiels ✅.
- `GetProductInfoAsync` (Product, GamePass, Bundle) unterstützt Transparent Batching ✅.
- Personalisierung: `RankProductsAsync` hat ein **striktes Rate-Limit** → einmal beim Join laden; `RecommendTopProductsAsync` liefert bis zu **50** Einträge und braucht mindestens **einen Kauf in den letzten 28 Tagen**, sonst eine leere Liste ✅ ([Developer products](https://create.roblox.com/docs/production/monetization/developer-products)).

```lua
--!strict
-- LocalScript: Preise für den Shop parallel laden (Transparent Batching)
local MarketplaceService = game:GetService("MarketplaceService")

local PRODUCT_IDS = { 123123, 456456, 789789 }
local prices: { [number]: number } = {}
local remaining = #PRODUCT_IDS

for _, productId in PRODUCT_IDS do
	task.spawn(function()
		local ok, info = pcall(function()
			return MarketplaceService:GetProductInfoAsync(productId, Enum.InfoType.Product)
		end)
		if ok and info.IsForSale then
			prices[productId] = info.PriceInRobux
		end
		remaining -= 1
	end)
end
while remaining > 0 do
	task.wait()
end
-- prices für die UI nutzen; Gutschrift passiert trotzdem nur am Server
```

---

## Teil B: Sicherheit

### 8. Exploit-Denken: was ein Angreifer kann ✅
Quelle: [Security and cheat mitigation tactics](https://create.roblox.com/docs/scripting/security/security-tactics)
- Jedes replizierte LocalScript und ModuleScript **dekompilieren**, auch wenn es auf dem Client nie läuft.
- **Network Ownership** der eigenen Figur und unverankerter Teile übernehmen.
- Touched-Events und ProximityPrompts **aus beliebiger Entfernung und Frequenz** auslösen.
- Position, Physik und Interaktionen der eigenen Figur ändern.
- RemoteEvents/RemoteFunctions mit **beliebigen Argumenten** feuern (nur das erste Argument `player` ist echt).
- Alles im lokalen DataModel ändern, ohne dass Events feuern; lokalen Code beliebig manipulieren.

Bedrohungsmodell für jedes neue Feature (Fragen aus der Doku ✅):
- Wie würde ein Angreifer das mit voller Client-Kontrolle ausnutzen?
- Was ist das schlimmste Ergebnis, wenn jeder Parameter jeden Wert haben kann?
- Was passiert bei **1.000+ Aufrufen pro Sekunde**? Was ist die maximal sinnvolle Rate?
- Kann damit jemand anderen Spielern das Spiel ruinieren?
- Wie viele Ressourcen kostet das Feature im schlimmsten Fall?
- Welche minimale Information muss ich dafür überhaupt an den Client geben?
- Logik und Daten von Anfang an in `ServerScriptService`/`ServerStorage`, nie in replizierten Containern ✅.

### 9. Remotes: Limits und Zustellgarantien ✅
Quellen: [Remote events and callbacks](https://create.roblox.com/docs/scripting/events/remote), [RemoteEvent](https://create.roblox.com/docs/reference/engine/classes/RemoteEvent), [UnreliableRemoteEvent](https://create.roblox.com/docs/reference/engine/classes/UnreliableRemoteEvent)

| Eigenschaft | RemoteEvent | UnreliableRemoteEvent | RemoteFunction |
|---|---|---|---|
| Richtung | eine Richtung | eine Richtung | Anfrage + Antwort (yieldet) |
| Rate-Limit Client → Server | ca. **500/s pro Client**, geteilt über alle RemoteEvents ✅ | ca. **500/s pro Client**, geteilt über alle Unreliable ✅ | – |
| Über dem Limit | wird **später verarbeitet**, Reihenfolge bleibt ✅ | wird **verworfen** ✅ | – |
| Payload-Grenze | – | **1.000 Bytes**, darüber verworfen (Studio-Warnung mit Überschuss) ✅ | – |
| Reihenfolge | garantiert, **auch über verschiedene RemoteEvent-Instanzen** ✅ | keine ✅ | keine Ordnung relativ zu RemoteEvents ✅ |
| Kein Handler verbunden | wird gepuffert (begrenzt), danach verworfen mit Fehler „Remote event invocation" ✅ | sofort verworfen ✅ | gepuffert wie RemoteEvent ✅ |

Weitere Regeln ✅:
- Ordnung gilt für den **Start** der Handler; yieldet ein Handler, kann der nächste schon laufen.
- **`InvokeClient` vermeiden**: wirft der Client einen Fehler, wirft auch der Server; trennt sich der Client, Fehler; antwortet der Client nie, **yieldet der Server für immer**.
- Argument-Einschränkungen: Funktionen kommen als `nil` an; nicht-String-Schlüssel werden zu Strings; **keine gemischten Tabellen** (Array + Dictionary); keine `nil`-Lücken; Tabellen werden kopiert (andere Identität).
- Buffers werden komprimiert übertragen und verkleinern Payloads (gut für Unreliable), machen die Größe vorab aber schwer abschätzbar ✅.
- Unter Server Authority: RemoteEvents sind nicht garantiert geordnet relativ zu Property-/Attribut-Updates ✅.

### 10. Validierung: drei Ebenen ✅
Quelle: [Securing the client-server boundary](https://create.roblox.com/docs/scripting/security/client-server-boundary)

| Ebene | Prüft | Beispiele |
|---|---|---|
| **Kontext / Berechtigung** | Darf dieser Spieler das jetzt? | Nah genug am Shop? Schlüssel im Besitz? Figur lebt? Nicht im Cooldown/Reload? |
| **Typ und Struktur** | Ist es der erwartete Typ in sinnvoller Größe? | `typeof`, String-Länge, Tabellen-Tiefe, **Tabelle statt Instance** (Spoofing) |
| **Wert** | Ist der Wert logisch im erlaubten Bereich? | Menge > 0, Ganzzahl, Item-ID existiert, **NaN und ±inf abweisen** |

Besonders gefährlich ✅:
- **NaN** ist vom Typ `number`, besteht aber jede Vergleichsprüfung (`NaN < 0` und `NaN > 1000000` sind beide falsch). Ein NaN-Angebot im Handel umgeht Bereichs- und Kontostandsprüfungen und „vergiftet" alle Systeme, die den Wert weiterverwenden. Abwehr: `math.isfinite(x)`.
- **Gefälschte Instances**: Ein Exploiter schickt eine Tabelle `{ Name = "Ultra Blade", ClassName = "Folder", Price = { Value = 0 } }`. Abwehr: `typeof(item) == "Instance"` **und** `item:IsDescendantOf(erwarteterOrdner)`.
- **DataStore-Manipulation**: Instances sind nicht speicherbar, beliebig lange Strings sprengen Limits, Tabellen-Indizes dürfen nicht NaN/nil sein, Strings müssen gültiges UTF-8 sein (`utf8.len` liefert bei ungültigen Zeichen `nil`) ✅.
- Remotes, die beliebige Pfade/Instances zum Löschen/Ändern annehmen oder anhand von Argumenten Assets laden/`require` ausführen, sind tabu ✅.

Validierungs-Modul (eigenes Muster 🧠, nur dokumentierte Funktionen):
```lua
--!strict
-- ModuleScript "Validate" in ServerScriptService
local Validate = {}

function Validate.number(value: unknown, min: number, max: number): number?
	if typeof(value) ~= "number" then
		return nil
	end
	local n = value :: number
	if not math.isfinite(n) or n < min or n > max then -- isfinite fängt NaN und ±inf
		return nil
	end
	return n
end

function Validate.integer(value: unknown, min: number, max: number): number?
	local n = Validate.number(value, min, max)
	if n == nil or n % 1 ~= 0 then
		return nil
	end
	return n
end

function Validate.text(value: unknown, maxChars: number): string?
	if typeof(value) ~= "string" then
		return nil
	end
	local s = value :: string
	if #s > maxChars * 4 then -- billige Byte-Grenze vor der UTF-8-Prüfung
		return nil
	end
	local length = utf8.len(s) -- nil bei ungültigem UTF-8
	if length == nil or length > maxChars then
		return nil
	end
	return s
end

function Validate.vector3(value: unknown, maxMagnitude: number): Vector3?
	if typeof(value) ~= "Vector3" then
		return nil
	end
	local v = value :: Vector3
	if not (math.isfinite(v.X) and math.isfinite(v.Y) and math.isfinite(v.Z)) then
		return nil
	end
	if v.Magnitude > maxMagnitude then
		return nil
	end
	return v
end

function Validate.descendantOf(value: unknown, container: Instance): Instance?
	if typeof(value) ~= "Instance" then -- Tabellen, die Instances imitieren, fallen hier raus
		return nil
	end
	local instance = value :: Instance
	if not instance:IsDescendantOf(container) then
		return nil
	end
	return instance
end

function Validate.key(value: unknown, allowed: { [string]: any }): string?
	if typeof(value) ~= "string" or allowed[value :: string] == nil then
		return nil
	end
	return value :: string
end

return Validate
```

### 11. Rate-Limiting mit Token Bucket ✅
Die Doku empfiehlt den **Token Bucket**: kurze Bursts erlaubt, dauerhafte Rate begrenzt. Client-seitige Limits sind praktisch, **aber nie die einzige Verteidigung** ✅. Gilt für alles, was der Client auslösen kann: Remotes, Touched, ProximityPrompts, ClickDetectors ✅.

Modul nach dem offiziellen Beispiel (MIT-Code der Creator Docs, leicht gekürzt, Kommentare übersetzt):
```lua
--!strict
-- ModuleScript "TokenBucket" in ServerScriptService
type Bucket = { tokens: number, last: number }
type TokenBucketT = {
	capacity: number,
	refillPerSecond: number,
	buckets: { [number]: Bucket },
	allow: (self: TokenBucketT, userId: number) -> boolean,
}

local TokenBucket = {}
TokenBucket.__index = TokenBucket

-- capacity = maximale Burst-Größe, windowSeconds = Zeit bis zum vollen Nachfüllen
function TokenBucket.new(capacity: number, windowSeconds: number): TokenBucketT
	assert(capacity >= 1, "capacity must be >= 1")
	assert(windowSeconds > 0, "windowSeconds must be > 0")
	local self = {
		capacity = capacity,
		refillPerSecond = capacity / windowSeconds,
		buckets = {},
	}
	return (setmetatable(self, TokenBucket) :: any) :: TokenBucketT
end

function TokenBucket:allow(userId: number): boolean
	local now = time()
	local b = self.buckets[userId]
	if not b then
		b = { tokens = self.capacity, last = now }
		self.buckets[userId] = b
	else
		local elapsed = now - b.last
		if elapsed > 0 then
			b.tokens = math.min(self.capacity, b.tokens + elapsed * self.refillPerSecond)
			b.last = now
		end
	end
	if b.tokens >= 1 then
		b.tokens -= 1
		return true
	end
	return false
end

return TokenBucket
```
`TokenBucket.new(5, 10)` erlaubt Bursts von 5 und füllt alle 2 Sekunden einen Token nach ✅. Beim Verlassen den Eintrag löschen (`limiter.buckets[player.UserId] = nil`), sonst Speicherleck ✅.

### 12. Beispiel: sicherer Shop-Kauf mit Spielwährung 🧠
```lua
--!strict
-- Script in ServerScriptService
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local ServerScriptService = game:GetService("ServerScriptService")

local PlayerData = require(ServerScriptService.PlayerData)
local TokenBucket = require(ServerScriptService.TokenBucket)
local Validate = require(ServerScriptService.Validate)

-- Preise existieren NUR am Server; der Client schickt nur eine ID und eine Menge
local ITEM_PRICES: { [string]: number } = { Sword = 250, Shield = 400 }
local SHOP_POSITION = Vector3.new(0, 5, 0)
local MAX_SHOP_DISTANCE = 20

local buyItem = ReplicatedStorage:WaitForChild("BuyItem") :: RemoteFunction
local limiter = TokenBucket.new(5, 10)

local function isNearShop(player: Player): boolean
	local character = player.Character
	local root = character and character:FindFirstChild("HumanoidRootPart")
	if root == nil or not root:IsA("BasePart") then
		return false
	end
	return (root.Position - SHOP_POSITION).Magnitude <= MAX_SHOP_DISTANCE
end

buyItem.OnServerInvoke = function(player: Player, itemId: unknown, quantity: unknown)
	if not limiter:allow(player.UserId) then
		return false, "Zu viele Anfragen"
	end
	local id = Validate.key(itemId, ITEM_PRICES)
	local amount = Validate.integer(quantity, 1, 10)
	if id == nil or amount == nil then
		return false, "Ungültige Anfrage"
	end
	if not isNearShop(player) then
		return false, "Zu weit vom Shop entfernt"
	end
	if not PlayerData.canTransact(player) then
		return false, "Daten nicht geladen"
	end
	local data = PlayerData.get(player)
	if data == nil then
		return false, "Daten nicht geladen"
	end
	local cost = ITEM_PRICES[id] * amount
	if data.coins < cost then
		return false, "Nicht genug Münzen"
	end
	data.coins -= cost -- erst prüfen, dann atomar ändern
	data.inventory[id] = (data.inventory[id] or 0) + amount
	return true, data.coins
end

Players.PlayerRemoving:Connect(function(player: Player)
	limiter.buckets[player.UserId] = nil
end)
```

### 13. Client-ausgelöste Instanzen absichern ✅
Quelle: [Securing the client-server boundary](https://create.roblox.com/docs/scripting/security/client-server-boundary)

| Objekt | Schwäche laut Doku | Server muss prüfen |
|---|---|---|
| **ProximityPrompt** | Events feuerbar, auch wenn `Enabled = false`; `Enabled`, `MaxActivationDistance`, `RequiresLineOfSight` lokal änderbar; Hold-Events trotz `HoldDuration = 0`; **nur `Triggered` hat eine Server-Distanzprüfung** | Aktiv? Distanz? Spielerzustand? Mindestdauer eingehalten? Rate-Limit |
| **ClickDetector** | **keinerlei** Server-Prüfung; feuerbar aus jeder Distanz, auch deaktiviert, auch ohne klickbares Parent | alles selbst prüfen |
| **DragDetector** | geerbte ClickDetector-Events ungeprüft; bei Drag-Events werden nur `Enabled` und `PermissionPolicy` respektiert | Rest selbst prüfen |

Hängen diese Objekte an **unverankerten** Teilen, kann ein Exploiter deren Network Ownership übernehmen und sie zu sich ziehen, womit Distanzprüfungen ausgehebelt sind. Für kritische Aktionen verankerte Teile oder die Network-Ownership-API nutzen ✅.

### 14. Client-zu-Client-Effekte: der Server ist Türsteher ✅
Ein Server, der `FireServer`-Daten ungeprüft per `FireAllClients` weiterreicht, erlaubt Spam (Effekte hunderte Male pro Sekunde), ungültige Daten (nil, NaN, falscher Typ → Skriptfehler bei allen Clients) und unberechtigte Nutzung (Zauber, die man nicht besitzt). Vor dem Broadcast: Typ, NaN, Rate-Limit, Berechtigung, Reichweite prüfen ✅ ([Client-server boundary](https://create.roblox.com/docs/scripting/security/client-server-boundary)).

### 15. Server Authority ✅/🟡
Quelle: [Server authority model](https://create.roblox.com/docs/projects/server-authority)

#### 15.1 Was es ist
Der Server ist die einzige Wahrheit für den gesamten Spielzustand; Clients melden nur noch **Eingaben**. Das verhindert ganze Cheat-Klassen wie Fly- und Speedhacks ✅. Gegen Eingabelatenz **sagt der Client einige Frames voraus** (Client Prediction); weicht der Server-Zustand ab (Misprediction), **rollt der Client zurück und simuliert neu** (Rollback & Resimulation). Mispredictions sind „a **normal and expected** part" der Architektur ✅.

#### 15.2 Voraussetzungen (Workspace-Eigenschaften) ✅
| # | Eigenschaft | Wert |
|---|---|---|
| 1 | `Workspace.AuthorityMode` | `Enum.AuthorityMode.Server` (setzt die folgenden fünf automatisch) |
| 2 | `Workspace.NextGenerationReplication` | aktiviert |
| 3 | `Workspace.PlayerScriptsUseInputActionSystem` | aktiviert |
| 4 | `Workspace.SignalBehavior` | `Enum.SignalBehavior.Deferred` |
| 5 | `Workspace.UseFixedSimulation` | aktiviert |
| 6 | `Workspace.StreamingEnabled` | aktiviert |

`AuthorityMode` hat Schreib-Sicherheit `RobloxScriptSecurity` ✅ ([Workspace](https://create.roblox.com/docs/reference/engine/classes/Workspace)): Man setzt es im **Properties-Fenster in Studio**, nicht per Skript.

#### 15.3 Regeln für den Code ✅
- Kernlogik in Funktionen, die per `RunService:BindToSimulation()` gebunden sind, in einem **ModuleScript, das auf Client und Server initialisiert** wird. Diese Funktionen laufen bei Resimulation erneut. `BindToSimulation` gibt es nur mit `UseFixedSimulation` ✅ ([RunService](https://create.roblox.com/docs/reference/engine/classes/RunService)).
- In gebundenen Funktionen nur Properties/Methoden mit dem Label **„Simulation Access"** verwenden, sonst Fehler. Beispiele mit Simulation Access: `BasePart.CFrame`, `Instance:GetAttribute`, `Instance:SetAttribute`, `Instance:FindFirstChild`, `InputAction:GetState`; **ohne**: `Player.Character`, `Players:GetPlayers` ✅ (API-Referenz, `simulationAccess`-Feld).
- **Zeit**: nur `time()` ist synchronisiert und läuft bei Resimulation zurück; `tick()`, `os.time()` und `os.clock()` nicht ✅.
- **Eigene Zustände** (Leben, Munition, Inventar) als **Attribute** auf vorhergesagten Instanzen speichern und nur in gebundenen Funktionen schreiben. Replikation nur, wenn das Attribut unter den **ersten 64** einer Instanz ist, der Name **≤ 50 Zeichen** und ein String-Wert **≤ 50 Zeichen** hat ✅.
- `task.spawn` aus der Simulation läuft mit Simulations-Einschränkungen weiter; `task.defer` plant Code außerhalb ✅.
- Eingaben, die die Simulation beeinflussen, **ausschließlich über das Input Action System**; `UserInputService.InputBegan` gehört nicht in die Kernsimulation. `InputContext`s müssen Nachfahren des `Player` sein ✅.
- Effekte, Sounds, Animationen getrennt von der Simulation darstellen; nicht-synchronisierbare Properties in `PostSimulation`/`RenderStepped` aus Attributen ableiten ✅.
- Vorhersage pro Instanz steuern: `RunService:SetPredictionMode(instance, Enum.PredictionMode.On/Off/Automatic)` ✅.
- Vorlagen der Doku: **Racing, Soccer, Laser Tag** ✅.

#### 15.4 Skizze (nach dem Doku-Muster) 🧠
```lua
--!strict
-- ModuleScript "Simulation" in ReplicatedStorage; ein Script und ein LocalScript
-- darunter rufen jeweils Simulation.Initialize() auf (wie in den Creator Docs)
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

type Entry = { sprint: InputAction, character: Model? }
local entries: { [Player]: Entry } = {}

-- Außerhalb der Simulation: Referenzen auflösen (Player.Character hat KEIN Simulation Access)
local function track(player: Player)
	local inputs = player:WaitForChild("Inputs")
	local sprint = inputs:WaitForChild("PlayContext"):WaitForChild("CharacterSprint") :: InputAction
	local entry: Entry = { sprint = sprint, character = player.Character }
	entries[player] = entry
	player.CharacterAdded:Connect(function(character: Model)
		entry.character = character
	end)
end

local Simulation = {}

function Simulation.Initialize()
	for _, player in Players:GetPlayers() do
		task.spawn(track, player)
	end
	Players.PlayerAdded:Connect(function(player: Player)
		task.spawn(track, player)
	end)
	Players.PlayerRemoving:Connect(function(player: Player)
		entries[player] = nil
	end)

	-- Kernsimulation: nur Simulation-Access-APIs (GetState, SetAttribute)
	RunService:BindToSimulation(function(_deltaTime: number)
		for _, entry in entries do
			local character = entry.character
			if character then
				character:SetAttribute("Sprinting", entry.sprint:GetState() == true)
			end
		end
	end)

	-- Darstellung/abgeleitete Properties außerhalb der Simulation
	RunService.PostSimulation:Connect(function()
		for _, entry in entries do
			local character = entry.character
			if character then
				local humanoid = character:FindFirstChildOfClass("Humanoid")
				if humanoid then
					humanoid.WalkSpeed = if character:GetAttribute("Sprinting") then 24 else 16
				end
			end
		end
	end)
end

return Simulation
```
Die `Inputs`-Ordner klont ein Server-Script beim `PlayerAdded` aus `ReplicatedStorage.Inputs` in jeden Spieler (Muster „InputSetup" der Doku) ✅. Diese Skizze vor Nutzung mit den offiziellen Vorlagen abgleichen.

#### 15.5 Status und Zeitachse 🟡
- Early Access 2025 („If you publish games using this API your players will NOT be able to play"), Studio Beta Ende 2025, Client Beta Ende April 2026, **Full Release Juli 2026** („Block physics-based exploits like speed hacks without custom anti-cheat code") 🟡 ([DevForum Full Release](https://devforum.roblox.com/t/full-release-ship-fair-and-competitive-games-with-server-authority/4727993)).
- Die Server-Authority-Seite der Doku trägt **kein Beta-Label** ✅. **Widerspruch in der Doku:** Die Seite „Network ownership, movement validation, and physics" sagt noch „Server authority is currently in beta and will be released soon" ✅ ([Network ownership](https://create.roblox.com/docs/scripting/security/network-ownership)). Maßgeblich ist die Server-Authority-Seite.
- Nicht in der Doku: Performance-Kosten, Spielerzahl-Grenzen, Kompatibilität mit eigenen Character-Controllern 🟠.

### 16. Ohne Server Authority: Network Ownership ✅
Quelle: [Network ownership](https://create.roblox.com/docs/scripting/security/network-ownership)
- Besitzt ein Client eine Assembly (inkl. seiner Figur), kann er teleportieren, fliegen, `WalkSpeed` beliebig setzen (ohne dass der Server das sieht), Kollision umgehen, beliebige Animationen abspielen, `Inf`/`NaN` in CFrames und Velocities replizieren (Fling) und Touched-Events manipulieren oder unterdrücken.
- Gegenmittel: gameplay-kritische unverankerte Teile per Network-Ownership-API manuell zuweisen oder automatische Ownership abschalten; Bewegungsprüfung mit Toleranz für Latenz (z. B. Prüfung in der XZ-Ebene, Ausnahmen für legitime Teleports). Einfache Distanz-über-Zeit-Prüfungen produzieren bei Fahrzeugen, Flug und Physik viele Fehlalarme.

### 17. Erkennen und reagieren ✅
Quelle: [Server-side detection and consequencing](https://create.roblox.com/docs/scripting/security/server-side-detection)

Grundsätze: **Der Server entscheidet** (nie auf Basis von Client-Erkennung bannen), **erst Schaden verhindern** (z. B. Speedhacker zurücksetzen statt sofort kicken), **verhältnismäßig und umkehrbar**, **Design schlägt Erkennung** ✅.

| Heuristik | Idee | Beispiel aus der Doku |
|---|---|---|
| Schnellste Abschlusszeit | theoretisches Minimum berechnen | Obby-Rekord 30 s, Lauf mit 5 s → Teleport-Verdacht |
| Zuwachsrate | maximale legitime Rate je Ressource | 100 Münzen/min möglich, 10.000 in 1 s → Flag |
| Aktions-Takt | menschliche Eingaben schwanken | 100 Würfe mit exakt 2,500 s Abstand → Makro |

- Jede Heuristik ist ein **Signal**, kein Beweis → **Verdachts-Score**, harte Strafen erst nach mehreren, verschiedenen Treffern ✅.
- **Honeypots**: ein RemoteEvent, das kein legitimer Client nutzt; jeder Aufruf ist verdächtig. Variante: Remotes mit fester Richtung, Aufruf in falscher Richtung = Flag ✅.
- **Konsequenz-Leiter**: stilles Loggen → leise Abschwächung (Requests verwerfen, Werte klemmen, Zustand korrigieren) → temporäre Einschränkungen (Handel, Ranglisten, Matchmaking) → sichtbare Strafen (Kick, Sperre, Bann) ✅.
- Sichtbare Strafen **verzögern**, damit Exploiter nicht lernen, was sie verraten hat; Erkennungsregeln versionieren ✅.
- Für Wiederholungstäter `Players:BanAsync()` statt nur Kicks (unterbindet Rejoin, wirkt universumweit, optional gegen Alt-Accounts) ✅ ([Players](https://create.roblox.com/docs/reference/engine/classes/Players)).

### 18. Defensives Design ✅
Quelle: [Defensive design tactics](https://create.roblox.com/docs/scripting/security/defensive-design)

| Szenario | Reaktiv (schwächer) | Defensiv (stärker) |
|---|---|---|
| Bots lassen sich für Kill-Punkte töten | Bots erkennen | **keine Punkte für frisch gespawnte Spieler** (bremst auch Spawn-Camper) |
| Obby: Teleport ans Ziel | nur Endposition und Zeit prüfen | **Pflicht-Checkpoints in Reihenfolge**, Server prüft jeden |
| Kampf: unmöglicher Schaden | absurde Werte filtern | **Schaden am Server aus Waffenwerten**, Treffer per Server-Raycast |
| Ökonomie: Duplikation durch schnelle Requests | Muster erkennen | **Server-Cooldowns**, jede Transaktion gegen aktuellen Inventarstand prüfen |

Waffen-Treffer prüfen ✅: Client schickt Schussursprung und vermuteten Treffer; Server prüft Ursprung nahe der Figur (mit Latenz-Toleranz), Treffer nahe am getroffenen Teil, keine **statische** Geometrie dazwischen, Feuerrate, Munition (am Server gezählt), Gegner statt Teammitglied, Ziel lebt, Spieler nicht im Reload/Sprint.

### 19. Handel und Duplikation ✅/🧠
Beispiel aus der Doku ✅: Spieler startet einen Handel, gibt das Item ab, verlässt sofort das Spiel; der Handel läuft durch, sein Save scheitert an ungültigen Daten → beim Rejoin hat er das Item noch, der Partner auch. Gegenmittel laut Doku: alle Daten **vor** dem Handel validieren, **transaktionsartig** erst nach Prüfung beider Seiten ändern, bei Teilfehlern alles zurückrollen ✅.
Ergänzend 🧠: Handel nur zwischen Spielern mit erfolgreich geladenen, gelockten Profilen; beide Profile direkt nach dem Handel speichern; Handels-Log (wer, was, wann, Server-JobId) in einem eigenen DataStore für Support-Fälle.

### 20. Hyperion (Client-Anti-Tamper) 🟠
Hyperion ist die Anti-Tamper-Software im Roblox-Client (von Byfron, 2022 übernommen); Rollout 64-Bit ab 2023 🟠 (Fan-Wiki/Presse, keine offizielle Doku gefunden). Für die Praxis gilt unabhängig davon: Hyperion erhöht nur die Kosten für Exploits und **ersetzt keine Server-Validierung** 🧠.

---

## Do / Don't
| Do | Don't |
|---|---|
| Developer Products nur über `ProcessReceipt`/`BindReceiptHandler` gutschreiben | Gutschrift über `PromptProductPurchaseFinished` oder Client-Signale |
| `PurchaseId` in den Spielerdaten vermerken und mitspeichern | `PurchaseGranted` am Funktionsende als Standard zurückgeben |
| Erst speichern, dann `PurchaseGranted`/`Processed` | Belohnung nur in `leaderstats` vergeben |
| Handler-Rückgabe auf `== true` prüfen | Nur `pcall`-Erfolg prüfen |
| Käufe sperren, wenn Daten nicht (fehlerfrei) geladen sind | Käufe in Standard-/Fallback-Daten schreiben |
| `GetProductInfoAsync` mit `pcall`, Preise nie hart codieren | Veraltetes `GetProductInfo`, `Creator.Id` statt `CreatorTargetId` |
| Pass-Besitz am Server prüfen, `PromptGamePassPurchaseFinished` nur am Server | `wasPurchased` im LocalScript als Wahrheit nehmen |
| Jeden Remote auf Kontext, Typ, Wert prüfen; `math.isfinite` | Zahlen ungeprüft verrechnen (NaN, inf) |
| Token Bucket am Server, Buckets beim Verlassen löschen | Nur client-seitige Cooldowns |
| `typeof(x) == "Instance"` + `IsDescendantOf` | Vom Client geschickte „Objekte" mit Preis-Feldern vertrauen |
| Server als Türsteher vor `FireAllClients` | Remote-Daten 1:1 an alle Clients weiterreichen |
| Unreliable nur für häufige, unkritische Daten < 1.000 Bytes | Käufe/Inventar über UnreliableRemoteEvent |
| Server Authority für Bewegung/Physik in kompetitiven Spielen | Eigenen Bewegungs-Anti-Cheat mit starren Distanzgrenzen |
| Verdachts-Score, Konsequenz-Leiter, `BanAsync` für Wiederholer | Sofort-Bann bei einem einzigen Heuristik-Treffer |
| ProximityPrompt/ClickDetector-Events am Server nachprüfen | `Enabled`/`MaxActivationDistance` als Schutz ansehen |
| `InvokeClient` meiden | Server-Logik auf eine Client-Antwort warten lassen |

## Checkliste
**Käufe**
- [ ] `ProcessReceipt` genau einmal gesetzt (oder `BindReceiptHandler` mit Catch-all), alle Produkt-IDs abgedeckt
- [ ] Vier Schritte: PurchaseId prüfen → gutschreiben → PurchaseId vermerken → speichern → erst dann bestätigen
- [ ] Warten auf geladene Daten mit Timeout und Abbruch, wenn der Spieler geht
- [ ] Käufe gesperrt bei Lade-/Speicherfehler, Kaufbuttons im Client deaktiviert
- [ ] In-Memory-Sperre gegen parallele Doppelaufrufe derselben PurchaseId
- [ ] Developer Products im Shop „Listed", kein Fix-Banner im Creator Hub
- [ ] Keine spielübergreifenden Verkäufe mehr (seit 30.05.2026)
- [ ] Gamepass-Besitz beim Join am Server geprüft, Kaufereignis am Server behandelt
- [ ] Preise per `GetProductInfoAsync` geladen, parallel (Transparent Batching)

**Sicherheit**
- [ ] Alle Remotes: Rate-Limit, Typ-, Wert- und Kontextprüfung
- [ ] NaN/inf, UTF-8, String-Längen, Tabellen-Struktur geprüft
- [ ] Keine Preise, Drop-Chancen-Entscheidungen oder Belohnungsmengen vom Client übernommen
- [ ] ProximityPrompts/ClickDetectors/DragDetectors am Server nachgeprüft
- [ ] Remote-Payloads klein, Unreliable < 1.000 Bytes, kein Spam über 500/s
- [ ] Server Authority bewertet (Bewegung/Physik), Voraussetzungen im Workspace gesetzt
- [ ] Heuristiken + Verdachts-Score + Logging; Ban-Strategie definiert
- [ ] Handel transaktional, beide Profile danach gespeichert
- [ ] Logik und geheime Daten nur in `ServerScriptService`/`ServerStorage`

## Offene Fragen / Recherche-Bedarf
- Genaue Puffergrenzen (Anzahl/Speicher) für RemoteEvents ohne verbundenen Handler stehen nicht in der Doku 🟠.
- Performance-Kosten und Grenzen von Server Authority bei vielen Spielern 🟠.
- Offizielle Angaben zu Hyperion-Updates 2025/2026 nicht gefunden 🟠.
- `PromptBulkPurchase` und Abo-APIs (`GetUserSubscriptionStatusAsync` u. a.) existieren in der API-Referenz ✅, Praxisempfehlungen fehlen noch 🟠.

## Quellen
- [Developer products](https://create.roblox.com/docs/production/monetization/developer-products) – Creator Docs, Stand 24.10.2026, ✅
- [Passes](https://create.roblox.com/docs/production/monetization/passes) – ✅
- [MarketplaceService (API-Referenz)](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService) – ProcessReceipt, BindReceiptHandler, GetProductInfoAsync, UserOwnsGamePassAsync, ✅
- [Implement player data and purchasing systems](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing) – ✅
- [Transparent batching](https://create.roblox.com/docs/scripting/transparent-batching) – ✅
- [Security and cheat mitigation tactics](https://create.roblox.com/docs/scripting/security/security-tactics) – ✅
- [Securing the client-server boundary](https://create.roblox.com/docs/scripting/security/client-server-boundary) – ✅
- [Network ownership, movement validation, and physics](https://create.roblox.com/docs/scripting/security/network-ownership) – ✅
- [Server-side detection and consequencing](https://create.roblox.com/docs/scripting/security/server-side-detection) – ✅
- [Defensive design tactics](https://create.roblox.com/docs/scripting/security/defensive-design) – ✅
- [Remote events and callbacks](https://create.roblox.com/docs/scripting/events/remote), [RemoteEvent](https://create.roblox.com/docs/reference/engine/classes/RemoteEvent), [UnreliableRemoteEvent](https://create.roblox.com/docs/reference/engine/classes/UnreliableRemoteEvent) – ✅
- [Server authority model](https://create.roblox.com/docs/projects/server-authority), [RunService](https://create.roblox.com/docs/reference/engine/classes/RunService), [Workspace](https://create.roblox.com/docs/reference/engine/classes/Workspace) – ✅
- [Players (BanAsync)](https://create.roblox.com/docs/reference/engine/classes/Players) – ✅
- [DevForum: Full Release Server Authority](https://devforum.roblox.com/t/full-release-ship-fair-and-competitive-games-with-server-authority/4727993) – Juli 2026, 🟡
- [DevForum: Updates to GetProductInfo return values](https://devforum.roblox.com/t/updates-to-marketplaceservice-getproductinfo-return-values/4666671) – 2026, 🟡
- Code-Beispiele der Creator Docs: MIT-Lizenz (LICENSE-CODE, © 2023 Roblox Corporation); Doku-Texte CC BY 4.0
