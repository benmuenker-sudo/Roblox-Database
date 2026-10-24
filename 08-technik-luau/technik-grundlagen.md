# Technik-Grundlagen (Luau)

> Stand: 2026-10-24 · Gesamt-Vertrauen: 🟡/🧠 (etablierte Roblox-Praxis aus Entwickler-Erfahrung; **API-Namen und Limits vor Nutzung in der offiziellen Doku bestätigen**, hier wurde nicht live gegen die Doku geprüft, da der Doku-Zugriff in der Sandbox blockiert war)

## Kurzfassung
Roblox-Spiele sind **Client-Server**: Der Server ist die Wahrheit, der Client ist nicht vertrauenswürdig. Alles, was Wert hat (Währung, Items, Käufe, Fortschritt), wird **serverseitig** berechnet und gespeichert. Der Client zeigt nur an und sendet Wünsche.

## Architektur
- **Server (Script in ServerScriptService):** Spiellogik, Ökonomie, Speichern, Validierung.
- **Client (LocalScript):** UI, Eingabe, visuelle Effekte.
- **Gemeinsam (ModuleScript in ReplicatedStorage):** Konfiguration, Hilfsfunktionen.
- **Kommunikation:** `RemoteEvent` / `RemoteFunction`.
- **Organisation:** Module pro System (Inventar, Wirtschaft, Pets), klare Schnittstellen, Konfigurationsdateien für Zahlen (Preise, Chancen), damit Balancing ohne Code-Umbau möglich ist.

## Sicherheit (wichtigste Regeln)
1. **Nie dem Client vertrauen.** Jeder Remote-Aufruf wird serverseitig geprüft: Typ, Wertebereich, Berechtigung, Cooldown.
2. **Berechnungen am Server:** Belohnungen, Zufalls-Drops, Preise, Schaden.
3. **Rate-Limits/Cooldowns** pro Spieler gegen Spam.
4. **Keine sensiblen Entscheidungen im Client** (z. B. „gib mir 1000 Münzen").
5. **Handel/Käufe** mit Bestätigung und Log.
6. **Exploit-Annahme:** Nimm an, dass Spieler Remotes beliebig aufrufen können.
7. **Duplikat-Schutz:** Itemvergabe atomar, Doppelaufrufe abfangen.

## Daten speichern
- **DataStoreService:** Spielerdaten speichern. Typische Praxis:
  - **Laden** beim Beitritt, **Speichern** beim Verlassen, bei Meilensteinen und in Intervallen, sowie bei `BindToClose` (Serverabschaltung).
  - **`UpdateAsync`** statt `SetAsync` für konsistentes Lesen-Ändern-Schreiben.
  - **Fehlerbehandlung:** `pcall` + Wiederholungen mit Wartezeit; Request-Limits beachten.
  - **Daten-Schema versionieren** (Feld `version`), um später Migrationen zu ermöglichen.
  - **Session-Locking** (verhindert, dass zwei Server dieselben Daten überschreiben), oft über bewährte Bibliotheken (z. B. ProfileService/ProfileStore) gelöst. 🟡 Community-Standard, Auswahl prüfen.
  - **Fallback:** Wenn Laden fehlschlägt, Spieler nicht mit leeren Daten überschreiben lassen (Speichern sperren, Meldung/Retry).
- **Backup-Strategie:** Wichtige Daten gelegentlich in zweiten Schlüssel/Version sichern.

## Käufe (MarketplaceService)
- **Gamepass:** Besitz prüfen (`UserOwnsGamePassAsync`), Ergebnis zwischenspeichern, Kauf-Ereignis behandeln.
- **Developer Product:** `ProcessReceipt`-Callback **muss** `Enum.ProductPurchaseDecision.PurchaseGranted` zurückgeben, erst nachdem die Belohnung sicher gespeichert ist; bei Fehler `NotProcessedYet`. Kauf-IDs (`PurchaseId`) speichern, damit Belohnungen nicht doppelt vergeben werden.
- Alles am Server.

## Performance
- **Schleifen** (`while true do`) sparsam; ereignisbasiert arbeiten (Signale statt Dauerabfrage).
- **`RunService`-Events** (`Heartbeat`) nur für wirklich nötige Updates.
- **Instanzen:** Wiederverwenden/Pooling statt ständig `Instance.new`/`Destroy` (z. B. Münzen-Effekte).
- **Remotes bündeln:** Nicht jedes Frame senden.
- **StreamingEnabled** für große Welten (bewusst konfigurieren, Skripte müssen mit nachgeladenen Teilen umgehen).
- **Memory-Leaks:** Verbindungen (`Connect`) trennen, wenn Objekte verschwinden (`Disconnect`, Maid/Janitor-Muster).
- **Messen:** MicroProfiler, Entwickler-Konsole, `Stats`.

## Code-Qualität
- **Strikter Modus:** `--!strict` für Typprüfung wo sinnvoll.
- **Benennung** konsistent, kleine Funktionen, Kommentare nur für „Warum".
- **Konfiguration auslagern** (Zahlen in Modulen).
- **Fehler loggen** (mit Kontext), aber keine sensiblen Daten.
- **Versionskontrolle:** Rojo + Git ermöglicht Arbeit außerhalb des Studios (🟡 verbreitete Praxis, Setup prüfen). Dieses Repo ist ein guter Ort für Skripte.
- **Tests:** Kritische Logik (Ökonomie, Zufall) mit Unit-Tests (z. B. TestEZ/Jest-Lua), falls das Team es braucht.

## Zufall serverseitig
- Zufall (Drops, Mutationen) **nur am Server**, mit `Random`-Objekt.
- Gewichtete Auswahl über kumulierte Gewichte.
- Pity-Zähler im Spielerprofil speichern.
- Wahrscheinlichkeiten **konfigurierbar** und für die Anzeige im UI nutzbar (damit Anzeige = Realität).

## Beispiel: Gewichtete Auswahl (Luau)
```lua
--!strict
local rng = Random.new()

local function rollWeighted(weights: { [string]: number }): string
	local total = 0
	for _, w in weights do
		total += w
	end
	local roll = rng:NextNumber() * total
	local acc = 0
	for name, w in weights do
		acc += w
		if roll <= acc then
			return name
		end
	end
	error("empty weights")
end
```

## Beispiel: Sicherer Remote-Handler (Muster)
```lua
--!strict
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local sellRemote = ReplicatedStorage:WaitForChild("SellAll") :: RemoteEvent
local lastCall: { [Player]: number } = {}

sellRemote.OnServerEvent:Connect(function(player: Player)
	local now = os.clock()
	if now - (lastCall[player] or 0) < 0.5 then
		return -- Cooldown gegen Spam
	end
	lastCall[player] = now
	-- Menge und Preis am Server aus dem Spielerprofil lesen, nie vom Client nehmen
end)

Players.PlayerRemoving:Connect(function(player: Player)
	lastCall[player] = nil
end)
```
(Muster zur Illustration; an die eigene Architektur anpassen und testen.)

## Checkliste
- [ ] Alle Wert-Logik am Server
- [ ] Remotes validiert (Typ, Bereich, Cooldown)
- [ ] DataStore: Fehler behandelt, Laden-Fehlschlag sperrt Speichern
- [ ] `BindToClose` speichert
- [ ] `ProcessReceipt` idempotent
- [ ] Verbindungen werden getrennt
- [ ] Mobile-Performance gemessen
- [ ] Konfiguration ausgelagert

## Quellen
- Offizielle Doku (Creator Hub: Scripting, DataStores, MarketplaceService, Memory Stores, Security Tactics) ✅ → bei nächstem Update mit Direktlinks und Prüfdatum ergänzen
- Bekannte Community-Bibliotheken: ProfileService/ProfileStore, Rojo (🟡, Aktualität prüfen)
