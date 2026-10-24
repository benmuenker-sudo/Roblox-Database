# Datenspeicherung (DataStores, MemoryStores, Session-Locking)

> Stand: 2026-10-24 · Nächste Prüfung: 2027-01-24 · Gesamt-Vertrauen: ✅ für Limits und API-Verhalten (gegen den Quelltext der offiziellen Creator Docs, Snapshot `4e795e6` vom 24.10.2026, geprüft), 🟡 für Community-Bibliotheken (ProfileStore), 🧠 für Architektur-Empfehlungen und Rechenbeispiele

## Kurzfassung
- Spielerdaten liegen **in einer Tabelle unter einem Schlüssel pro Spieler** (`User_<UserId>`), werden beim Join einmal geladen, im Server-Speicher bearbeitet und nur periodisch, beim Verlassen, beim Shutdown und bei Käufen geschrieben ✅ ([Best practices](https://create.roblox.com/docs/cloud-services/data-stores/best-practices)).
- Es gibt **zwei Limit-Ebenen**: ein **Spiel-Budget** (300 + 40/20/2/40 × CCU pro Minute), das sich Spielserver und Open Cloud teilen, **und** konfigurierbare **Server-Limits** (Standard: 60 + 40 × Spieler) ✅ ([Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)). Die alte Formel „60 + 10 × Spieler" ist überholt.
- **`UpdateAsync` statt `SetAsync`**, **Session-Locking** über eine GUID in den Metadaten und **geordnete Retries pro Schlüssel** verhindern Datenverlust und Item-Duplikation ✅ ([Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing)).
- Ein fehlgeschlagener Schreibaufruf heißt **nicht**, dass nichts geschrieben wurde. Wer Gewissheit braucht, liest mit `UseCache = false` nach ✅.
- **MemoryStores** sind für flüchtige, schnelle Daten (Matchmaking, Live-Ranglisten, Auktionen): 64 KB + 1,2 KB × Nutzer Speicher, 1.000 + 120 × CCU Request Units pro Minute, maximal 45 Tage Lebensdauer ✅ ([Memory stores](https://create.roblox.com/docs/cloud-services/memory-stores)).

## Referenzbilder
Selbst erstelltes, beschriftetes Referenzbild (frei nutzbar, Übersicht: `assets/bilder/README.md`). DataStore-Zugriffe gehören ausschließlich auf die Server-Seite.

![Client-Server-Architektur mit DataStore auf der Server-Seite](../assets/bilder/client-server-architektur.png)

## Warum das wichtig ist
Datenverlust ist der schnellste Weg, Vertrauen und Bewertungen zu verlieren. Duplikations-Exploits zerstören jede Ökonomie (Handel, Pets, Seltenheit). Die meisten dieser Fehler entstehen nicht durch Roblox-Ausfälle, sondern durch typische Muster: Speichern mit `SetAsync`, ungeordnete Retries, kein Session-Lock, leere Fallback-Daten, die echte Daten überschreiben ✅ ([Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing)). Seit 2026 kommt dazu: Open-Cloud-Skripte (Backfills, Admin-Tools) zehren am selben Budget wie die Live-Server ✅.

---

## Details

### 1. Welcher Speicher wofür? ✅
Quelle: [Data stores vs. memory stores](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores)

| Dienst | Lebensdauer | Reichweite | Im Spiel | Typische Nutzung |
|---|---|---|---|---|
| **Standard DataStore** | dauerhaft (ältere Versionen 30 Tage) | serverübergreifend | lesen/schreiben | Spielerprofil, Inventar, Einstellungen |
| **Ordered DataStore** | dauerhaft, **keine Versionen, keine Metadaten** | serverübergreifend | lesen/schreiben | dauerhafte Ranglisten (nur Zahlen) |
| **MemoryStore** (Sorted Map, Queue, Hash Map) | max. 45 Tage | serverübergreifend | lesen/schreiben | Matchmaking-Queues, Tages-/Wochenranglisten, Auktionen, Cache |
| **Configs** | dauerhaft | serverübergreifend | nur lesen | Feature-Flags, Balancing-Werte |
| **Secrets Store** | dauerhaft | serverübergreifend | nur lesen | API-Schlüssel |
| **Luau im Speicher** | Sitzung | ein Server | lesen/schreiben | Laufende Spielerdaten-Kopie |

Alle Cloud-Dienste sind im Spiel **nur aus Server-Skripten** erreichbar ✅. Ein `LocalScript`, das `DataStoreService` nutzt, wirft einen Fehler ✅ ([Data stores](https://create.roblox.com/docs/cloud-services/data-stores)).

### 2. DataStore-Limits im Überblick

#### 2.1 Spiel-Budget (geteilt mit Open Cloud) ✅
„Game server and Open Cloud **share** a budget; Open Cloud traffic can be throttled by in-experience usage (and vice versa)." ([Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits))

| Anfrage-Typ | Spiel-API (Beispiele) | Open-Cloud-Gegenstück | Limit pro Minute |
|---|---|---|---|
| Read | `GetAsync`, `GetVersionAsync`, `GetVersionAtTimeAsync`, `UpdateAsync` | Get Data Store Entry | **300 + 40 × CCU** ✅ |
| Write | `SetAsync`, `IncrementAsync`, `UpdateAsync` | Create/Update/Increment Entry | **300 + 20 × CCU** ✅ |
| List | `ListDataStoresAsync`, `ListKeysAsync`, `ListVersionsAsync` | List Data Stores/Entries/Revisions | **300 + 2 × CCU** ✅ |
| Remove | `RemoveAsync` | Delete Entry/Data Store, Undelete | **300 + 40 × CCU** ✅ |

Ordered DataStores haben dieselben Werte (Read umfasst dort auch `BatchGetAsync`, List entspricht `GetSortedAsync`) ✅. **`UpdateAsync` zählt gegen Read *und* Write** ✅.

Rechenbeispiel (🧠, aus der ✅-Formel): Bei 1.000 CCU stehen dem ganzen Spiel 40.300 Reads, 20.300 Writes, 2.300 Lists und 40.300 Removes pro Minute zur Verfügung. Ein Open-Cloud-Backfill mit 10.000 Writes pro Minute würde also rund die Hälfte des Schreib-Budgets der Live-Server verbrauchen.

#### 2.2 Server-Limits (Standardwerte, konfigurierbar) ✅
„Data stores are subject to both experience and server-level limits." Server erhalten beim Start einen einmaligen Zusatz-Burst ✅. Quelle: [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)

| Typ | `Enum.DataStoreRequestType` | Standard pro Minute |
|---|---|---|
| Standard Read | `StandardRead` | **60 + Spieler × 40** ✅ |
| Standard Write | `StandardWrite` | **60 + Spieler × 40** ✅ |
| Standard List | `StandardList` | **5 + Spieler × 2** ✅ |
| Standard Remove | `StandardRemove` | **60 + Spieler × 40** ✅ |
| RemoveVersion (veraltet) | `RemoveVersionAsync` | 5 + Spieler × 2 ✅ |
| Ordered Read | `OrderedRead` | 60 + Spieler × 40 ✅ |
| Ordered Write | `OrderedWrite` | **30 + Spieler × 5** ✅ |
| Ordered List | `OrderedList` | 5 + Spieler × 2 ✅ |
| Ordered Remove | `OrderedRemove` | 30 + Spieler × 5 ✅ |

- Steuerung: `DataStoreService:SetRateLimitForRequestType(requestType, baseLimit, perPlayerLimit)` und `DataStoreService:GetRequestBudgetForRequestType(requestType)` ✅ ([DataStoreService](https://create.roblox.com/docs/reference/engine/classes/DataStoreService)).
- Erlaubte Spannen für die neuen Typen (`StandardRead` usw.): `baseLimit` 0–10.000, `perPlayerLimit` 0–200. `UpdateAsync` und `OnUpdate` lassen sich **nicht** konfigurieren (Fehler) ✅. Aufruf **einmal pro Typ beim Serverstart**, nicht während des Spiels ✅.
- In **Studio Run** gelten eigene, statische und eventuell niedrigere Limits. Für Limit-Tests empfiehlt die Doku Team Create ✅.
- Rechenbeispiel (🧠): Ein Server mit 20 Spielern darf standardmäßig 860 Standard-Reads und 860 Writes pro Minute senden, also 43 pro Spieler und Minute. Ein Auto-Save alle 180 s braucht davon 0,33.

#### 2.3 Daten-, Metadaten- und Warteschlangen-Limits ✅
Quelle: [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)

| Komponente | Maximum |
|---|---|
| Name des DataStores | 50 Zeichen ✅ |
| Schlüsselname | 50 Zeichen ✅ |
| Scope | 50 Zeichen ✅ |
| Wert pro Schlüssel | **4.194.304 Zeichen** (4 MB, als JSON-String gemessen) ✅ |
| Metadaten: Schlüssel / Wert | 50 / 250 Zeichen ✅ |
| Metadaten gesamt | **300 Zeichen** (beliebig viele Paare, aber zusammen ≤ 300) ✅ |
| Warteschlange pro Typ (Set, Ordered Set, Get, Ordered Get) | **30 Anfragen**, danach Fehler 301–306 ✅ |
| Seitengröße `GetSortedAsync` | 1–100 ✅ |

Größe prüfen: `#HttpService:JSONEncode(data)` liefert ungefähr die gespeicherte Länge ✅. Strings müssen gültiges UTF-8 sein, sonst scheitert der Schreibvorgang ✅ ([GlobalDataStore](https://create.roblox.com/docs/reference/engine/classes/GlobalDataStore)).

#### 2.4 Durchsatz pro Schlüssel ✅
| Richtung | Methoden | Limit |
|---|---|---|
| Lesen | `GetAsync`, `GetVersionAsync`, `GetVersionAtTimeAsync`, `ListVersionsAsync`, `UpdateAsync` | **25 MB pro Minute** ✅ |
| Schreiben | `SetAsync`, `IncrementAsync`, `UpdateAsync`, `RemoveAsync` | **4 MB pro Minute** ✅ |

- Gemessen über die letzten 60 Sekunden, über **alle Server** hinweg ✅.
- Jede Anfrage wird **auf das nächste KB aufgerundet** (800 B + 1,2 KB = 3 KB) ✅.
- Fehlerbild: `KeyThrottled` (ein Schlüssel) oder `DatastoreThrottled` (ganzer Store) ✅.
- Rechenbeispiel (🧠): Ein 100-KB-Profil, alle 180 s gespeichert, belegt ca. 33 KB/min, also unter 1 % des Schreib-Limits. Ein 1-MB-Profil, das fünfmal pro Minute gespeichert wird, überschreitet das Limit.

#### 2.5 Speicherplatz ✅
- **Formel: 500 MB + 1 MB × Lifetime-Nutzer** (jeder, der das Spiel mindestens einmal betreten hat) ✅ ([Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)).
- Gezählt wird die **komprimierte Größe der jeweils neuesten Version** jedes Schlüssels. Gelöschte Schlüssel und ältere Versionen zählen nicht ✅.
- **Nicht selbst vorkomprimieren**: Roblox komprimiert automatisch, eigene Kompression kostet CPU und verschlechtert die eingebaute Kompression ✅.
- Über Open Cloud (`DeleteDataStore`) gelöschte Stores zählen während der **30-tägigen Löschphase** weiter ✅.
- Wird das Limit überschritten, zeigt der Data Stores Manager „Est. Monthly Costs" an; mehr Kapazität gibt es über Extended Services ✅ ([Data Stores Manager](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager)).
- Rechenbeispiel (🧠): 100.000 Lifetime-Nutzer → 500 MB + 100.000 MB ≈ 100,5 GB, im Schnitt also etwa 1 MB pro Spieler. Ein einzelner Schlüssel darf 4 MB groß sein, im Durchschnitt aller Spieler ist aber nur ca. 1 MB eingeplant.
- Historie 🟡: Die Ankündigung von 2025 nannte 100 MB + 1 MB × Lifetime-Nutzer; im Juli 2026 stieg die Basis auf 500 MB („5× more data store storage") ([DevForum Weekly Recap](https://devforum.roblox.com/t/weekly-recap-july-13-%E2%80%93-17-animation-graphs-go-live-5%C3%97-more-data-store-storage/4743286)).

### 3. Fehlercodes, die man kennen muss ✅
Quelle: [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)

| Code | Name | Bedeutung | Reaktion |
|---|---|---|---|
| 101 / 102 | `KeyNameEmpty` / `KeyNameLimit` | Schlüssel leer bzw. > 50 Zeichen | Bug, nicht wiederholen |
| 103 / 104 | `ValueNotAllowed` / `CantStoreValue` | Callback lieferte nicht speicherbaren Typ (z. B. Instance) | Bug, Daten bereinigen |
| 105 | `ValueTooLarge` | Wert > 4 MB | Daten aufteilen/verkleinern |
| 301–306 | `…Throttle` | Warteschlange (30) voll, Anfrage verworfen | Last senken, später wiederholen |
| 401 / 402 | `DataModelNoAccess` / `LuaWebSrvsNoAccess` | Server fährt herunter | in `BindToClose` früher speichern |
| 403 | `StudioAccessToApisNotAllowed` | Studio-Zugriff nicht aktiviert | Experience Settings ⟩ Security |
| 501–505 | `InternalError` / `RequestRejected` | Backend-Fehler, evtl. Datenkorruption | mit Backoff wiederholen |
| 509 | `OperationNotAllowed` | Schreiben auf Personal RCC blockiert | – |
| 511 | `AttributeSizeTooLarge` | Metadaten zu groß | Metadaten kürzen (≤ 300 Zeichen) |
| 512 / 513 | `UserIdLimitExceeded` / `AttributeFormatError` | UserId-Liste zu lang bzw. Format falsch | Eingaben prüfen |
| – | `Standard…ExperienceThrottled` / `…GameServerThrottled` | Spiel- bzw. Server-Budget erschöpft | Anfragen strecken, Budget prüfen |

**Wichtig:** „A failed write call, such as `UpdateAsync()`, means the game server did not receive a successful response. It does not always guarantee that the backend write did not occur." ✅

### 4. API-Grundlagen und Verhalten ✅

#### 4.1 `SetAsync` vs. `UpdateAsync`
Quelle: [Data stores](https://create.roblox.com/docs/cloud-services/data-stores), [GlobalDataStore](https://create.roblox.com/docs/reference/engine/classes/GlobalDataStore)

| | `SetAsync` | `UpdateAsync` |
|---|---|---|
| Liest vorher | nein | ja, den neuesten Wert vom Backend |
| Budget | nur Write | Read **und** Write |
| Mehrere Server | kann Daten inkonsistent machen | wiederholt den Callback bei Konflikt, bis gespeichert oder `nil` |
| Abbrechen | – | Callback gibt `nil` zurück → kein Schreiben |
| Wann | neuer Schlüssel, Wert hängt nicht vom alten ab | alles, was vom alten Wert abhängt (Spielerdaten) |

Regeln für den `UpdateAsync`-Callback ✅:
- Er darf **nicht yielden** (kein `task.wait`, keine anderen Async-Aufrufe).
- Er bekommt `(aktuellerWert, keyInfo)`; `keyInfo` ist ein `DataStoreKeyInfo`.
- Er gibt bis zu drei Werte zurück: neuen Wert, UserId-Liste, Metadaten. **Wer UserIds oder Metadaten nicht mit zurückgibt, löscht sie** ✅. Darum immer `keyInfo:GetUserIds()` und `keyInfo:GetMetadata()` weiterreichen, wenn man nichts ändern will.
- Er kann mehrfach aufgerufen werden. Nebenwirkungen (Zähler, Signale) gehören nicht hinein 🧠.

#### 4.2 Metadaten und UserIds ✅
- **Service-Metadaten** (nur lesen): `keyInfo.Version`, `keyInfo.CreatedTime`, `keyInfo.UpdatedTime` (Millisekunden seit Epoch).
- **Eigene Metadaten**: `DataStoreSetOptions:SetMetadata({...})` bei `SetAsync`, oder dritter Rückgabewert von `UpdateAsync`. Limit 300 Zeichen gesamt.
- **UserIds**: dritter Parameter von `SetAsync` bzw. zweiter Rückgabewert von `UpdateAsync`. Die Doku nennt sie hilfreich für das Nachverfolgen und Entfernen von Inhalten ✅.
- Ordered DataStores: `DataStoreKeyInfo` ist immer `nil` ✅.

#### 4.3 Caching ✅
Quelle: [Versioning, listing, and caching](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching)
- `GetAsync` cacht Werte **4 Sekunden** lokal pro DataStore-Instanz. Gecachte Antworten zählen **nicht** gegen Server- und Durchsatz-Limits ✅.
- `GetVersionAsync`, `ListVersionsAsync`, `ListKeysAsync`, `ListDataStoresAsync` cachen nie ✅.
- Frische Werte: `DataStoreGetOptions` mit `UseCache = false` (kostet Budget) ✅.
- Zwei DataStore-Instanzen auf denselben Schlüssel (z. B. mit und ohne `AllScopes`) haben getrennte Caches → Inkonsistenzgefahr ✅.

Offizielles Prüfmuster nach einem fehlgeschlagenen Schreiben (MIT-Code aus den Creator Docs, gekürzt):
```lua
local ok = pcall(function()
	store:UpdateAsync(key, transform)
end)
if not ok then
	local options = Instance.new("DataStoreGetOptions")
	options.UseCache = false
	local success, value = pcall(function()
		return store:GetAsync(key, options)
	end)
	if success then
		-- Entscheidung anhand des Backend-Zustands treffen, nicht anhand des Caches
	end
end
```

#### 4.4 Versionen, Snapshots, Listing ✅
- Versionen entstehen durch `SetAsync`, `UpdateAsync`, `IncrementAsync`: **die erste Schreiboperation pro Schlüssel und UTC-Stunde** wird als Backup behalten; weitere Writes derselben Stunde überschreiben ✅.
- Alte Versionen verfallen **30 Tage**, nachdem sie überschrieben wurden; die neueste Version verfällt nie ✅.
- `RemoveAsync` erzeugt einen „Tombstone"; ältere Versionen bleiben über `ListVersionsAsync`/`GetVersionAsync` abrufbar ✅.
- **Snapshots**: Über die Open-Cloud-API „Snapshot Data Stores" kann man **einmal pro Tag** alle DataStores eines Spiels sichern. Vor jedem Update, das die Speicherlogik ändert, einen Snapshot machen ✅.
- **Prefix-Listing** statt Scopes für neue Spiele: `ListKeysAsync("User_123456/Profile")` listet z. B. alle Charakterprofile eines Spielers ✅. Scopes sind Legacy, bestehende Spiele dürfen sie weiter nutzen ✅.

Wiederherstellung einer Version (verkürzt nach dem offiziellen Beispiel, MIT):
```lua
--!strict
local DataStoreService = game:GetService("DataStoreService")
local store = DataStoreService:GetDataStore("PlayerData")

local function restoreBefore(key: string, year: number, month: number, day: number, hour: number, minute: number)
	local maxDate = DateTime.fromUniversalTime(year, month, day, hour, minute)
	local listOk, pages = pcall(function()
		return store:ListVersionsAsync(key, Enum.SortDirection.Descending, nil, maxDate.UnixTimestampMillis)
	end)
	if not listOk then
		warn("ListVersionsAsync fehlgeschlagen:", pages)
		return
	end
	local items = pages:GetCurrentPage()
	if #items == 0 then
		warn("Keine Version vor diesem Zeitpunkt")
		return
	end
	local getOk, value, info = pcall(function()
		return store:GetVersionAsync(key, items[1].Version)
	end)
	if getOk and info then
		local setOptions = Instance.new("DataStoreSetOptions")
		setOptions:SetMetadata(info:GetMetadata())
		store:SetAsync(key, value, info:GetUserIds(), setOptions)
	end
end
```
Achtung 🧠: Bei aktivem Session-Lock nur wiederherstellen, wenn der Spieler offline ist, sonst überschreibt dessen Server den wiederhergestellten Stand beim nächsten Auto-Save.

#### 4.5 Serialisierung ✅
Speicherbar: `nil`, Booleans, Zahlen, Strings, Tabellen (nur aus diesen Typen), **Buffers** ✅. Nicht speicherbar: Instances, Vector3, CFrame, Color3 usw. → selbst in Tabellen/Zahlen umwandeln. `inf`, `-inf` und `nan` nicht speichern (kein gültiges JSON) ✅. Tabellen mit Länge 0 und Zahlen-Schlüsseln werden zu String-Schlüsseln ✅. Unbekannte Typen führen zu Fehler **oder werden still als `nil` gespeichert** → mit `HttpService:JSONEncode()` vorab prüfen ✅ ([Versioning, listing, and caching](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching)).

### 5. Architektur für Spielerdaten ✅/🧠

#### 5.1 Die offiziellen Grundregeln ✅
Quellen: [Best practices](https://create.roblox.com/docs/cloud-services/data-stores/best-practices), [Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing)
1. **Wenige DataStores**, Datensätze per Schlüssel organisieren (ein `PlayerData`-Store für alle, nicht einer pro Spieler).
2. **Ein Schlüssel pro Spieler**, solange er unter 4 MB bleibt. Nur aufteilen, wenn Teile unterschiedliche Zugriffsmuster haben oder an Limits stoßen; was atomar zusammen geändert werden muss, bleibt in einem Schlüssel.
3. **Statische Schlüsselmuster** wie `User_{UserId}`, nie Anzeigenamen. Das macht Schlüssel vorhersagbar und erlaubt automatisierte RTBF-Löschung.
4. **Im Speicher puffern**: DataStore-Anfragen nur für (a) Laden zu Sitzungsbeginn, (b) finales Speichern, (c) periodisches Speichern, (d) Speichern bei Kaufabwicklung.
5. **Auto-Save-Intervall** innerhalb der Limits und **kürzer als der Lock-Ablauf**; das offizielle Beispiel nutzt **180 Sekunden** und versetzt den ersten Save jedes Spielers zufällig.
6. **Retries mit exponentiellem Backoff und Jitter**, gedeckelt in Dauer und Anzahl, **geordnet pro Schlüssel**. Ungültige Anfragen nicht wiederholen.
7. **Fallback-Daten dürfen echte Daten nie überschreiben**: Bei Ladefehler mit Standarddaten spielen lassen, Profil als „errored" markieren, Speichern und Käufe sperren, Spieler informieren. Die Doku empfiehlt das ausdrücklich gegenüber einem Kick.
8. **`BindToClose`**: alle Spieler **parallel** speichern; der Server wartet maximal **30 Sekunden** auf gebundene Funktionen ✅ ([DataModel](https://create.roblox.com/docs/reference/engine/classes/DataModel)).
9. **Hot Keys sharden** (nur gegen Read-Throttling): z. B. `Weather_1`…`Weather_3`, Server wählt per Hash der `JobId` eine Kopie ✅.
10. **DataStore2 nicht mehr für neue Spiele** verwenden; Roblox bietet ein Beta-Migrationstool ✅.

#### 5.2 Warum Retries geordnet sein müssen ✅
Die Doku zeigt das klassische Problem: Request A (Wert 1) scheitert und wird verzögert wiederholt, Request B (Wert 2) gelingt in der Zwischenzeit, dann überschreibt die Wiederholung von A den neueren Wert. Auch bei `UpdateAsync` können ungeordnete Requests ungültige Zwischenzustände erzeugen (z. B. Kauf zieht Münzen ab, bevor eine Gutschrift verarbeitet ist → negativer Kontostand). Das offizielle Beispiel nutzt deshalb eine Warteschlange pro Schlüssel (`DataStoreWrapper`/`ThreadQueue`), in der jede Anfrage inklusive Retries abgeschlossen sein muss, bevor die nächste startet ✅.

#### 5.3 Session-Locking: so funktioniert es ✅
Ohne Lock kann Server B die Daten laden, bevor Server A die neuere Version gespeichert hat; danach überschreibt B die neuen Daten. Die Doku nennt vier reale Ursachen: fehlgeschlagene Saves mit langen Retries, gedrosselte Saves in der Queue, yieldender Code in `PlayerRemoving` vor dem Save und überlastete Server. Besonders häufig beim schnellen Serverwechsel (Teleport) und gezielt ausgenutzt bei Handelsspielen ✅.

Ablauf im offiziellen Beispiel (`SessionLockedDataStoreWrapper`):
1. **Jede** Anfrage (auch Lesen) läuft über `UpdateAsync`, weil nur dort Lesen und Schreiben atomar sind.
2. Im Callback prüfen: Gibt es eine fremde `LockId` in den Metadaten, die jünger als der Lock-Ablauf ist → abbrechen (`nil`). Hat dieser Server früher selbst gelockt, muss seine `LockId` noch vorhanden sein (sonst hat ein anderer Server übernommen).
3. Beim Laden `LockId` = neue GUID setzen und im Server merken; beim finalen Speichern `LockId` entfernen.
4. Den Lock durch regelmäßige Zugriffe (Auto-Save) frisch halten; ein abgelaufener Lock darf von jedem Server übernommen werden.
5. Bei Abbruch wegen fremdem Lock wiederholen und dem Client einen eigenen Fehler `SessionLocked` melden ✅.

#### 5.4 Bibliothek oder selbst bauen? 🟡
- **ProfileStore** (MadStudio/loleris) ist der verbreitete Community-Standard mit Auto-Save und Session-Locking in einem ModuleScript; **ProfileService ist „no longer supported"** 🟡 ([ProfileStore-Doku](https://madstudioroblox.github.io/ProfileStore/), [ProfileService GitHub](https://github.com/MadStudioRoblox/ProfileService)).
- Bekannte Eckdaten 🟡: Auto-Save-Standard 300 s (früher 30 s); Konfliktlösung über MessagingService; bei bestehendem Lock wird 40 s lang alle 10 s (`LOAD_REPEAT_PERIOD`) nachgefragt, danach „gestohlen" ([ProfileStore DataStore Use](https://madstudioroblox.github.io/ProfileStore/datause/)).
- Die offizielle Doku sagt neutral: Drittanbieter-Module sind „in many cases preferred", vorher Eigentümer, Wartungsstand und Funktionsumfang prüfen und **wissen, wie man ohne das Modul an die Daten kommt und migriert** ✅ ([Best practices](https://create.roblox.com/docs/cloud-services/data-stores/best-practices)).
- Typische ProfileStore-Nutzung (🟡, Community-API, vor Einsatz mit der aktuellen ProfileStore-Doku abgleichen):
```lua
-- Community-API (ProfileStore), nicht Teil der Roblox-Engine
local ProfileStore = require(game:GetService("ServerScriptService").ProfileStore)
local PlayerStore = ProfileStore.New("PlayerData", { coins = 0, purchaseIds = {} })

local function onPlayerAdded(player: Player)
	local profile = PlayerStore:StartSessionAsync("User_" .. player.UserId, {
		Cancel = function()
			return player.Parent ~= game:GetService("Players")
		end,
	})
	if profile == nil then
		player:Kick("Profil konnte nicht geladen werden, bitte erneut beitreten.")
		return
	end
	profile:AddUserId(player.UserId)
	profile:Reconcile()
	profile.OnSessionEnd:Connect(function()
		player:Kick("Profil-Sitzung beendet, bitte erneut beitreten.")
	end)
	-- profile.Data im Speicher bearbeiten; profile:EndSession() bei PlayerRemoving
end
```

### 6. Beispiel: robustes Laden und Speichern mit Session-Lock (Luau) 🧠/✅
Eigenes Lernbeispiel nach dem Muster der offiziellen Doku (Lock-GUID in Metadaten, nur `UpdateAsync`, Retries mit Backoff und Jitter, ein Save pro Spieler gleichzeitig, Fallback ohne Speichern, versetzter Auto-Save, paralleles Speichern in `BindToClose`). Nur APIs aus der Creator Docs. Vor Produktivnutzung ausgiebig testen (Teleports, Serverabsturz, Throttling).

```lua
--!strict
-- ModuleScript "PlayerData" in ServerScriptService
local DataStoreService = game:GetService("DataStoreService")
local HttpService = game:GetService("HttpService")
local Players = game:GetService("Players")

local STORE = DataStoreService:GetDataStore("PlayerData")
local SCHEMA_VERSION = 2
local AUTO_SAVE_INTERVAL = 180 -- Sekunden, wie im offiziellen Beispiel
local LOCK_EXPIRY = 30 * 60 -- muss deutlich länger sein als AUTO_SAVE_INTERVAL
local MAX_ATTEMPTS = 5
local LOCK_WAIT_ATTEMPTS = 6 -- 6 × 5 s auf einen fremden Lock warten
local LOCK_WAIT_SECONDS = 5

export type Data = {
	version: number,
	coins: number,
	inventory: { [string]: number },
	purchaseIds: { string },
}

type Session = {
	data: Data,
	lockId: string,
	loadFailed: boolean, -- true = Standarddaten, NIE speichern
	saving: boolean,
}

local PlayerData = {}
local sessions: { [Player]: Session } = {}

local function keyFor(userId: number): string
	return "User_" .. tostring(userId)
end

local function defaultData(): Data
	return { version = SCHEMA_VERSION, coins = 0, inventory = {}, purchaseIds = {} }
end

-- Schema-Migration: alte Stände schrittweise anheben
local function migrate(raw: any): Data
	if type(raw) ~= "table" then
		return defaultData()
	end
	local version = if type(raw.version) == "number" then raw.version else 1
	if version < 2 then
		raw.purchaseIds = raw.purchaseIds or {}
		version = 2
	end
	raw.version = version
	raw.coins = if type(raw.coins) == "number" then raw.coins else 0
	raw.inventory = if type(raw.inventory) == "table" then raw.inventory else {}
	return raw :: Data
end

-- Wiederholt fn mit exponentiellem Backoff und Jitter (gedeckelt)
local function withRetries(fn: () -> any): (boolean, any)
	local lastError: any = nil
	for attempt = 1, MAX_ATTEMPTS do
		local ok, result = pcall(fn)
		if ok then
			return true, result
		end
		lastError = result
		if attempt < MAX_ATTEMPTS then
			local backoff = math.min(32, 2 * 2 ^ (attempt - 1))
			task.wait(backoff * (0.5 + math.random() * 0.5))
		end
	end
	return false, lastError
end

local function loadAsync(player: Player): Session
	local lockId = HttpService:GenerateGUID(false)
	for _ = 1, LOCK_WAIT_ATTEMPTS do
		local lockedByOther = false
		local ok, value = withRetries(function()
			return STORE:UpdateAsync(keyFor(player.UserId), function(current: any, keyInfo: DataStoreKeyInfo?)
				lockedByOther = false -- Callback kann mehrfach laufen
				local meta: { [string]: any } = if keyInfo then keyInfo:GetMetadata() else {}
				local userIds: { number } = if keyInfo then keyInfo:GetUserIds() else {}
				local otherLock = meta.LockId
				local lockAge = os.time() - (tonumber(meta.LockTime) or 0)
				if otherLock ~= nil and otherLock ~= lockId and lockAge < LOCK_EXPIRY then
					lockedByOther = true
					return nil -- abbrechen, nichts schreiben
				end
				meta.LockId = lockId
				meta.LockTime = os.time()
				if not table.find(userIds, player.UserId) then
					table.insert(userIds, player.UserId)
				end
				return current or defaultData(), userIds, meta
			end)
		end)
		if not ok then
			warn("Laden fehlgeschlagen für", player.UserId, value)
			break
		end
		if not lockedByOther then
			return { data = migrate(value), lockId = lockId, loadFailed = false, saving = false }
		end
		task.wait(LOCK_WAIT_SECONDS) -- anderer Server speichert vermutlich gerade
	end
	-- Fallback: spielen lassen, aber nie speichern und keine Käufe zulassen
	return { data = defaultData(), lockId = lockId, loadFailed = true, saving = false }
end

local function saveAsync(player: Player, releaseLock: boolean): boolean
	local session = sessions[player]
	if session == nil or session.loadFailed then
		return false
	end
	while session.saving do -- nur ein Save pro Schlüssel gleichzeitig (Reihenfolge!)
		task.wait()
	end
	session.saving = true
	local lostLock = false
	local ok, err = withRetries(function()
		return STORE:UpdateAsync(keyFor(player.UserId), function(_current: any, keyInfo: DataStoreKeyInfo?)
			lostLock = false
			local meta: { [string]: any } = if keyInfo then keyInfo:GetMetadata() else {}
			if meta.LockId ~= session.lockId then
				lostLock = true -- ein anderer Server hat übernommen
				return nil
			end
			if releaseLock then
				meta.LockId = nil
				meta.LockTime = nil
			else
				meta.LockTime = os.time() -- Lock auffrischen
			end
			local userIds: { number } = if keyInfo then keyInfo:GetUserIds() else { player.UserId }
			return session.data, userIds, meta
		end)
	end)
	session.saving = false
	if not ok then
		warn("Speichern fehlgeschlagen für", player.UserId, err)
	elseif lostLock then
		warn("Session-Lock verloren für", player.UserId)
		session.loadFailed = true -- ab jetzt nichts mehr schreiben
	end
	return ok and not lostLock
end

local function startAutoSave(player: Player)
	task.spawn(function()
		task.wait(math.random() * AUTO_SAVE_INTERVAL) -- Server und Spieler entzerren
		while player.Parent == Players and sessions[player] do
			saveAsync(player, false)
			task.wait(AUTO_SAVE_INTERVAL)
		end
	end)
end

Players.PlayerAdded:Connect(function(player: Player)
	local session = loadAsync(player)
	if player.Parent ~= Players then
		-- Spieler ist während des Ladens gegangen: Lock sofort wieder freigeben
		sessions[player] = session
		saveAsync(player, true)
		sessions[player] = nil
		return
	end
	sessions[player] = session
	startAutoSave(player)
end)

Players.PlayerRemoving:Connect(function(player: Player)
	saveAsync(player, true)
	sessions[player] = nil
end)

game:BindToClose(function()
	local pending = 0
	for player in sessions do
		pending += 1
		task.spawn(function()
			saveAsync(player, true)
			pending -= 1
		end)
	end
	local deadline = os.clock() + 25 -- Puffer zu den 30 s von BindToClose
	while pending > 0 and os.clock() < deadline do
		task.wait(0.1)
	end
end)

-- Öffentliche Schnittstelle
function PlayerData.get(player: Player): Data?
	local session = sessions[player]
	return if session then session.data else nil
end

function PlayerData.canTransact(player: Player): boolean
	local session = sessions[player]
	return session ~= nil and not session.loadFailed
end

function PlayerData.waitForSessionAsync(player: Player, timeoutSeconds: number): boolean
	local deadline = os.clock() + timeoutSeconds
	while sessions[player] == nil and player.Parent == Players and os.clock() < deadline do
		task.wait(0.1)
	end
	return sessions[player] ~= nil
end

function PlayerData.saveNowAsync(player: Player): boolean
	return saveAsync(player, false)
end

return PlayerData
```

Bewusste Vereinfachungen (🧠): Die Retries laufen innerhalb eines Saves geordnet, weil pro Spieler nur ein Save gleichzeitig läuft; ein vollständiger `ThreadQueue` wie im offiziellen Beispiel würde zusätzlich Lese-/Schreibreihenfolgen anderer Systeme absichern. Bei `loadFailed` dürfen weder Saves noch Käufe stattfinden (siehe `kaeufe-und-sicherheit.md`). Wer Spieler in Studio ohne API-Zugriff testet, bekommt Fehler 403; das Skript fällt dann sauber auf Standarddaten zurück.

### 7. Budget gezielt steuern ✅
```lua
--!strict
-- Einmal beim Serverstart (Script in ServerScriptService)
local DataStoreService = game:GetService("DataStoreService")

-- Eigenes, engeres Leselimit für diesen Server: 100 + 30 × Spieler pro Minute
DataStoreService:SetRateLimitForRequestType(Enum.DataStoreRequestType.StandardRead, 100, 30)

-- Vor einer Massenoperation prüfen, wie viel Budget gerade frei ist
local budget = DataStoreService:GetRequestBudgetForRequestType(Enum.DataStoreRequestType.StandardWrite)
if budget < 10 then
	warn("Wenig DataStore-Schreibbudget frei:", budget)
end
```
Für Open-Cloud-Skripte empfiehlt die Doku eine **eigene Drosselung**: einfach eine Pause von `60 / gewünschte Anfragen pro Minute` Sekunden nach jeder Anfrage, robust ein **Leaky-Bucket**-Limiter (Node.js-Referenz in der Doku) ✅ ([Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)). Für große Batch-Jobs nennt die Doku den „Data Stores Batch Processor" (CLI) ✅ ([Best practices](https://create.roblox.com/docs/cloud-services/data-stores/best-practices)).

### 8. Beobachten und eingreifen ✅
- **Data Stores Observability Dashboard** (Creator Hub ⟩ Spiel ⟩ Monitoring ⟩ Data Stores): Storage Usage Bytes, Request Count by API, by Status, API × Status, Quota Usage für Read/Write/List/Remove; Daten der letzten **30 Tage**, die letzten **3 Minuten** können unvollständig sein; 1 KB = 1024 Bytes ✅ ([Observability](https://create.roblox.com/docs/cloud-services/data-stores/observability)).
- **Data Stores Manager**: Stores, Schlüssel, Größe, Storage-Limit, geschätzte Kosten; ab **mehr als 100 DataStores** werden Größe und Schlüsselanzahl in der Liste nicht mehr angezeigt ✅ ([Data Stores Manager](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager)).
- Gelöschte DataStores lassen sich **30 Tage** lang wiederherstellen, danach endgültig weg ✅ ([Best practices](https://create.roblox.com/docs/cloud-services/data-stores/best-practices)).
- **Custom Alerts** für wichtige DataStore-Metriken einrichten; Creator-Hub-Benachrichtigungen warnen, wenn der Speicher sich dem Limit nähert ✅.
- **Studio-Zugriff** (Experience Settings ⟩ Security ⟩ „Enable Studio Access to API Services") nur in einer **separaten Test-Experience** aktivieren, nie im Live-Spiel: Studio greift auf dieselben DataStores zu ✅ ([Data stores](https://create.roblox.com/docs/cloud-services/data-stores)).

### 9. Recht auf Löschung (RTBF / DSGVO) ✅
Quellen: [Data store RTBF](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten), [Automate right to erasure](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure)
- **Bevorzugt: automatische Lösch-Templates.** Roblox löscht bei einer bearbeiteten RTBF-Anfrage passende Einträge selbst, ohne eigenen Server ✅.
- Bis zu **100 Templates** pro Spiel ✅. Token `{UserId}` (Groß-/Kleinschreibung beachten) ✅.
- Voraussetzungen: Daten in Standard- oder Ordered-DataStore; UserId steht im **Namen oder Scope** des Stores bzw. Schlüssels; statisches Muster wie `User_{UserId}`. Ganze Stores löschen nur bei Standard-DataStores ✅.
- Einrichtung: Creator Dashboard ⟩ Configurations ⟩ Data stores manager ⟩ **RTBF Deletion** ⟩ Create Template (Typ: Standard Data Store, Standard Key oder Ordered Key) oder per Open-Cloud-**Configs-API** (Konfiguration `user_data_templates` im Repository `DataStoresConfig`, API-Key mit `universe:read` und `universe:write`) ✅.
- Fehlt `scope_pattern`, gilt `global` ✅.
- **Alternative: Webhook „Right to Erasure Request"** (Payload mit UserId und Start-Place-IDs) plus eigener Bot, der über die Open-Cloud-DataStore-API löscht. Nötig für Daten außerhalb von DataStores, nicht unterstützte Schemata oder eigene Logik ✅.
- Praxisfolge 🧠: Schlüsselnamen von Anfang an als `User_<UserId>` anlegen. Wer Spielerdaten unter Anzeigenamen oder zufälligen IDs speichert, kann RTBF nicht automatisieren.

### 10. MemoryStoreService ✅
Quelle: [Memory stores](https://create.roblox.com/docs/cloud-services/memory-stores)

#### 10.1 Limits
| Limit | Wert |
|---|---|
| Speicher-Kontingent (pro Spiel) | **64 KB + 1,2 KB × Nutzer** ✅ (wächst sofort, sinkt erst nach **8 Tagen** wieder) |
| Request Units (pro Spiel) | **1.000 + 120 × CCU pro Minute** ✅ |
| Pro Sorted Map oder Queue | max. **1.000.000 Einträge** und **100 MB** (bei Sorted Maps inkl. Schlüssel) ✅ |
| Pro Datenstruktur | 100.000 Request Units pro Minute (`DataStructureRequestsOverLimit`) ✅ |
| Pro Partition (Schätzwert) | ca. **30.000 Request Units pro Minute** ✅ |
| Hash Map pro Schlüssel | ca. **5.000 Write-** und **15.000 Read-Units pro Minute** ✅ |
| Wertgröße pro Eintrag | **32 KB** (`ItemValueSizeTooLarge`) ✅ |
| Ablaufzeit | 0–**3.888.000 s** (45 Tage), Standard **45 Tage** ✅ |

Kosten in Request Units ✅: meist 1 pro Aufruf; `MemoryStoreSortedMap:GetRangeAsync()` = Anzahl zurückgegebener Einträge (mind. 1); `MemoryStoreQueue:ReadAsync()` = Einträge + 1 Unit je 2 Sekunden Wartezeit; `MemoryStoreHashMap:UpdateAsync()` mindestens 2; `MemoryStoreHashMap:ListItemsAsync()` = gescannte Partitionen + Einträge.

Rechenbeispiel (🧠, aus ✅-Formel): Bei 1.000 Nutzern sind es nur ca. 1,23 MB Speicher, aber 121.000 Request Units pro Minute. MemoryStores sind also **für viele kleine Zugriffe gebaut, nicht für große Datenmengen**.

#### 10.2 Welche Struktur?
- **Hash Map**: Zugriff per Schlüssel, verteilt sich über viele Partitionen → erste Wahl, wenn weder Sortierung noch FIFO nötig ist ✅.
- **Sorted Map**: sortierte Daten (Ranglisten, Auktionen); liegt auf **einer** Partition ✅.
- **Queue**: Verarbeitung in Reihenfolge (Matchmaking); liegt auf **einer** Partition ✅.

#### 10.3 Best Practices ✅
- Verarbeitete Einträge **explizit löschen**; Ablaufzeit so kurz wie möglich, als Sicherheitsnetz.
- Nur Nötiges speichern (Auktion: nur Höchstgebot per `MemoryStoreSortedMap:UpdateAsync`).
- Bei `DataUpdateConflict` exponentiell zurückweichen (2 s, 4 s, 8 s …).
- Große Strukturen und heiße Hash-Map-Schlüssel **sharden**.
- Bei `TotalMemoryOverLimit`: Einträge löschen, ablaufen lassen, per Open Cloud **flushen** (löscht **alle** Strukturen im Scope `LIVE` oder `TEST`) oder Extended Services buchen.
- Studio- und Live-MemoryStores sind getrennt.

Beispiel: Tages-Rangliste mit kurzer Ablaufzeit (nur dokumentierte Methoden):
```lua
--!strict
local MemoryStoreService = game:GetService("MemoryStoreService")
-- DateTime statt os.date (os.date gilt laut Doku als "should be avoided")
local today = DateTime.now():FormatUniversalTime("YYYYMMDD", "en-us")
local dailyBoard = MemoryStoreService:GetSortedMap("DailyCoins_" .. today)
local ONE_DAY = 24 * 60 * 60

local function submitScore(userId: number, score: number)
	local ok, err = pcall(function()
		dailyBoard:UpdateAsync(tostring(userId), function(old: any)
			if type(old) == "number" and old >= score then
				return nil -- kein Schreiben, alter Wert ist besser
			end
			return score
		end, ONE_DAY)
	end)
	if not ok then
		warn("Rangliste konnte nicht aktualisiert werden:", err)
	end
end

local function top10(): { any }
	local ok, entries = pcall(function()
		-- kostet so viele Request Units wie Einträge zurückkommen
		return dailyBoard:GetRangeAsync(Enum.SortDirection.Descending, 10)
	end)
	return if ok then entries else {}
end
```
Hinweis 🧠: Für eine echte Punkte-Sortierung den Score zusätzlich als `sortKey` setzen (vierter Parameter von `MemoryStoreSortedMap:SetAsync`); ohne `sortKey` sortiert die Sorted Map nach Schlüssel ✅ ([MemoryStoreSortedMap](https://create.roblox.com/docs/reference/engine/classes/MemoryStoreSortedMap)).

### 11. MessagingService (serverübergreifende Nachrichten) ✅
Quelle: [MessagingService](https://create.roblox.com/docs/reference/engine/classes/MessagingService) („limits are subject to change")

| Limit | Maximum |
|---|---|
| Nachrichtengröße | 1 kB ✅ |
| Gesendete Nachrichten pro Server | 600 + 240 × Spieler im Server pro Minute ✅ |
| Empfangen pro Topic | 40 + 80 × Anzahl Server pro Minute ✅ |
| Empfangen fürs ganze Spiel | 400 + 200 × Anzahl Server pro Minute ✅ |
| Abonnements pro Server | 20 + 8 × Spieler ✅ |
| Subscribe-Anfragen pro Server | 240 pro Minute ✅ |

Nutzung 🧠: Signale wie „globales Event startet" oder „Lock freigegeben", nie als Datenspeicher (keine Zustellgarantie).

---

## Do / Don't
| Do | Don't |
|---|---|
| Ein Schlüssel pro Spieler (`User_<UserId>`), eine Tabelle | Für jeden Wert einen eigenen Schlüssel oder DataStore |
| `UpdateAsync` mit Session-Lock in den Metadaten | `SetAsync` für Spielerdaten aus mehreren Servern |
| Retries mit Backoff + Jitter, geordnet pro Schlüssel | Sofortige Endlos-Retries in einer Schleife |
| Bei Ladefehler: Standarddaten, Speichern und Käufe sperren, Hinweis zeigen | Leere Fallback-Daten später über echte Daten schreiben |
| Auto-Save (z. B. 180 s) mit zufälligem Startversatz | Alle Server zur selben Sekunde speichern lassen |
| In `BindToClose` alle Spieler parallel speichern | Spieler in `BindToClose` nacheinander speichern (30-s-Grenze) |
| UserIds und Metadaten im `UpdateAsync`-Callback weiterreichen | Metadaten vergessen und damit den Lock löschen |
| Schema-Feld `version` + Migrationsfunktion | Struktur ändern, ohne alte Stände zu migrieren |
| Vor Updates an der Speicherlogik einen Snapshot machen | Ungetestete Speicheränderungen live schalten |
| Open-Cloud-Skripte selbst drosseln (Leaky Bucket) | Backfills zur Hauptspielzeit ungebremst starten |
| MemoryStore für Flüchtiges, kurze TTL, explizit löschen | MemoryStore als dauerhaften Speicher missbrauchen |
| RTBF-Templates mit `{UserId}` einrichten | Spielerdaten unter Anzeigenamen speichern |
| Größe mit `JSONEncode` prüfen, Strings auf UTF-8 prüfen | Instances, Vector3, NaN/inf direkt speichern |
| Studio-API-Zugriff nur in einer Test-Experience | Studio-Tests gegen Live-Daten fahren |

## Checkliste
- [ ] Nur ein `PlayerData`-Store, Schlüssel `User_<UserId>`
- [ ] Alle Zugriffe über `UpdateAsync`, Callback yieldet nicht und reicht UserIds/Metadaten weiter
- [ ] Session-Lock (GUID + Zeitstempel in Metadaten, Ablauf > Auto-Save-Intervall)
- [ ] Retries: Backoff + Jitter, max. Versuche, geordnet pro Schlüssel
- [ ] Ladefehler setzt `loadFailed`: kein Speichern, keine Käufe, sichtbarer Hinweis
- [ ] Auto-Save mit zufälligem Startversatz, Speichern bei `PlayerRemoving`, paralleles `BindToClose` (< 30 s)
- [ ] Spieler verlässt das Spiel während des Ladens → Lock wird freigegeben
- [ ] Schema-Version und Migration vorhanden, Datengröße (`JSONEncode`) unter Kontrolle
- [ ] Budget gerechnet: Spiel (300 + x × CCU) **und** Server (60 + 40 × Spieler)
- [ ] Open-Cloud-Skripte gedrosselt, Batch-Jobs außerhalb der Spitzenzeit
- [ ] Snapshot vor jedem Update der Speicherlogik
- [ ] Observability-Dashboard und Alerts eingerichtet
- [ ] RTBF-Templates angelegt und getestet
- [ ] MemoryStore-Daten mit kurzer TTL und expliziter Löschung
- [ ] Studio-API-Zugriff nur in Test-Experience aktiv

## Offene Fragen / Recherche-Bedarf
- Exakter Wert für den Lock-Ablauf im offiziellen Beispiel (`Purchase-Handling`, Creator-Store-Asset 14376223840) nicht aus dem Doku-Text ablesbar 🟠.
- Grenze der UserId-Liste pro Schlüssel (Fehler 512 nennt einen dynamischen Wert X) 🟠.
- Ob die MemoryStore-Formel „Nutzer" als CCU oder als Nutzer der letzten 8 Tage zählt, ist im Doku-Text nicht eindeutig 🟠.
- Aktueller Release-Stand von ProfileStore (Version, API-Änderungen seit 2025) 🟠.

## Quellen
- [Data stores](https://create.roblox.com/docs/cloud-services/data-stores) – Creator Docs, Stand 24.10.2026, ✅
- [Data store error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits) – ✅
- [Best practices for data stores](https://create.roblox.com/docs/cloud-services/data-stores/best-practices) – ✅
- [Versioning, listing, and caching](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching) – ✅
- [Implement player data and purchasing systems](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing) – ✅
- [Data store observability](https://create.roblox.com/docs/cloud-services/data-stores/observability), [Data Stores Manager](https://create.roblox.com/docs/cloud-services/data-stores/data-stores-manager) – ✅
- [Data store RTBF](https://create.roblox.com/docs/cloud-services/data-stores/right-to-be-forgotten), [Automate right to erasure](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure) – ✅
- [Memory stores](https://create.roblox.com/docs/cloud-services/memory-stores), [Data stores vs. memory stores](https://create.roblox.com/docs/cloud-services/data-stores-vs-memory-stores) – ✅
- API-Referenz: [DataStoreService](https://create.roblox.com/docs/reference/engine/classes/DataStoreService), [GlobalDataStore](https://create.roblox.com/docs/reference/engine/classes/GlobalDataStore), [DataModel](https://create.roblox.com/docs/reference/engine/classes/DataModel), [MessagingService](https://create.roblox.com/docs/reference/engine/classes/MessagingService), [MemoryStoreSortedMap](https://create.roblox.com/docs/reference/engine/classes/MemoryStoreSortedMap) – ✅
- [DevForum: Weekly Recap Juli 2026 (5× Storage)](https://devforum.roblox.com/t/weekly-recap-july-13-%E2%80%93-17-animation-graphs-go-live-5%C3%97-more-data-store-storage/4743286) – 🟡
- [ProfileStore-Doku](https://madstudioroblox.github.io/ProfileStore/), [ProfileService GitHub](https://github.com/MadStudioRoblox/ProfileService) – Community, 🟡
- Code-Beispiele der Creator Docs: MIT-Lizenz (LICENSE-CODE, © 2023 Roblox Corporation); Doku-Texte CC BY 4.0
