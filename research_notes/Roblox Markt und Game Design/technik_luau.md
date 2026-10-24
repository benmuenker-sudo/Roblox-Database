# Roblox Engine and Luau: Technical Best Practices and New Features 2025–2026 (as of 2026-10-24)

Method note: these notes come only from WebSearch result snippets. WebFetch failed with a DNS error (getaddrinfo ENOTFOUND devforum.roblox.com) and was not retried. The shared web-search budget (200 per turn) ran out after about 35 queries. The planned checks on versioning/metadata, the official ProcessReceipt sample, Animation Graphs, TextGenerator limits and Experience Events could not be run, so they are listed as gaps. A date tag in [brackets] gives when each fact was valid.

## 1. Data persistence: DataStoreService, MemoryStoreService, session locking, ProfileStore, GDPR

### Takeaway
DataStores now use one request budget per experience, shared by game servers and Open Cloud. It has a base of 300 per minute plus a per-CCU amount for each request type, and storage is 500 MB + 1 MB per lifetime user. Both came from the July 2026 "Unifying Data Stores" change. Per-key throughput is still 4 MB/min for writes and 25 MB/min for reads. The recommended pattern for player data is still one table per player, saved with UpdateAsync under a session lock. ProfileStore (loleris/MadStudio) replaces ProfileService, which is no longer supported. Right-to-erasure requests can be handled by automatic deletion templates or by webhooks.

### Cited Findings
**Request budgets (DataStoreService)**
- [Current docs, after July 2026] Limits are per experience and scale with concurrent users (CCU). Reads (GetAsync etc.) get 300 + 40×CCU per minute. Writes (SetAsync etc.) get 300 + 20×CCU. Lists (ListKeysAsync etc.) get 300 + 2×CCU. Removes get 300 + 40×CCU. Game servers and Open Cloud share these limits — [Data store error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits); [creator-docs GitHub](https://github.com/Roblox/creator-docs/blob/main/content/en-us/cloud-services/data-stores/error-codes-and-limits.md)
- [Announced Apr 2025, updated Dec 4 2025] The "DataStores Access and Storage Updates" post moved access limits from per server to per experience, effective early 2026. Its interim numbers were Get 250+CCU×40, Set 250+CCU×20, List 10+CCU×2 and Remove 100+CCU×40 per universe per minute — [DevForum announcement](https://devforum.roblox.com/t/datastores-access-and-storage-updates/3597255)
- [July 2026] "Unifying Data Stores Open Cloud and Game APIs, and Increasing Storage Limits" puts in-game and Open Cloud requests on the same counters for each request type and says "baseline limits will be increased to 300 across functions". The target date was July 29, 2026 — [DevForum announcement](https://devforum.roblox.com/t/unifying-data-stores-open-cloud-and-game-apis-and-increasing-storage-limits/4739240); [BloxBot secondary summary](https://bloxbot.ai/guide/roblox-datastore-limits-july-2026)
- The old per-server formula (60 + numPlayers × 10 per minute for Get/Set) appears in many forum and tutorial posts but is out of date. A DevForum documentation issue reports the server limits as outdated — [DevForum: Data store server limits outdated/incorrect](https://devforum.roblox.com/t/data-store-server-limits-outdatedincorrect/4050757); [jkit calculator (third-party)](https://jkit.tools/en/tools/roblox-datastore-limits-calculator)
- UpdateAsync uses both the read budget and the write budget — [Roblox throttling docs, via search summary](https://create.roblox.com/docs/cloud/guides/data-stores/throttling)
- Each request queue holds 30 requests. Once it is full, further requests are dropped with errors 301–306 (e.g. SetAsyncThrottle). Throttling shows up as DatastoreThrottled (whole store) or KeyThrottled (single key) — [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)
- Open Cloud callers should bring their own rate limiting because they now draw on the live-game budget. BloxBot warns that a bulk backfill can starve live servers — [BloxBot](https://bloxbot.ai/guide/roblox-datastore-limits-july-2026); [Throttling docs](https://create.roblox.com/docs/cloud/guides/data-stores/throttling)

**Size and throughput per key**
- Per-key throughput is 4 MB per minute for writes (SetAsync, IncrementAsync, UpdateAsync, RemoveAsync) and 25 MB per minute for reads (GetAsync, GetVersionAsync, UpdateAsync…). Each request is rounded up to the next KB, so writing 800 B and then 1.2 KB counts as 3 KB — [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)
- A value can be up to 4 MB per key (4,194,304), and store, key and scope names are capped at 50 characters. This comes from a DevForum post quoting the docs; the live docs page did not show these numbers in the snippet I saw — [DevForum thread](https://devforum.roblox.com/t/is-there-a-limit-to-how-many-items-can-be-in-a-table-datastore/2951520). Unconfirmed: the metadata size limit. I could not verify the commonly quoted 300 B for user metadata.

**Storage quota**
- [2025] Storage was set at 100 MB + 1 MB × lifetime players, with data compressed. Roblox said "99.99%+ of experiences won't hit this limit". Commenters pointed out that this works out to about 1 MB per player on average, even though a single key can hold 4 MB — [DevForum #76 by Roblox](https://devforum.roblox.com/t/datastores-access-and-storage-updates/3597255/76)
- [July 2026 onward] The base rose to 500 MB, so the quota is now 500 MB + 1 MB × lifetime users, measured on the compressed size of the latest version of each key. The weekly recap headline reads "5× more data store storage" — [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits); [Weekly Recap July 13–17 2026](https://devforum.roblox.com/t/weekly-recap-july-13-%E2%80%93-17-animation-graphs-go-live-5%C3%97-more-data-store-storage/4743286)
- Usage can be tracked with email alerts, dashboard insights, error logs, Data Stores Observability and the Data Stores Manager — [DevForum announcement](https://devforum.roblox.com/t/datastores-access-and-storage-updates/3597255); [Unifying announcement](https://devforum.roblox.com/t/unifying-data-stores-open-cloud-and-game-apis-and-increasing-storage-limits/4739240)

**UpdateAsync, session data and session locking**
- Roblox's official guide says to keep all of a player's session data in one table. That lets you update multiple values atomically, use fewer requests, avoid values drifting out of sync, and reason about rollbacks more easily — [Implement player data and purchasing systems](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing)
- The same guide warns that if one player's data is loaded on several servers, a server can save stale data. That causes data loss and item-duplication exploits, which is what session locking prevents — [Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing)
- Community consensus is to prefer UpdateAsync over SetAsync for player data because it reads the previous value. Use SetAsync only to force a value. UpdateAsync also handles new players: the callback receives nil and you supply defaults — [DevForum](https://devforum.roblox.com/t/2309525)
- Roblox has official pages on "Best practices" and "Versioning, listing and caching". I could not retrieve their contents — [Best practices](https://create.roblox.com/docs/cloud-services/data-stores/best-practices); [Versioning, listing, caching](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching)

**ProfileStore and ProfileService**
- ProfileService is marked "no longer supported", and most projects can migrate to ProfileStore — [ProfileService GitHub](https://github.com/MadStudioRoblox/ProfileService)
- ProfileStore is a DataStore wrapper in a single ModuleScript that handles auto-saving and session locking. Its default auto-save interval went up from 30 s to 300 s. Methods ending in Async yield (e.g. `:StartSessionAsync()`) and the rest do not — [ProfileStore docs](https://madstudioroblox.github.io/ProfileStore/); [DevForum ProfileStore thread](https://devforum.roblox.com/t/profilestore/3190543)
- Session conflicts are resolved through MessagingService. While a conflict is unresolved, ProfileStore repeats 1 UpdateAsync and 1 PublishAsync every 10 s (LOAD_REPEAT_PERIOD) for 40 s and then steals the session (SESSION_STEAL). The docs say it "should outperform ProfileService in session conflict resolution time" — [ProfileStore DataStore Use](https://madstudioroblox.github.io/ProfileStore/datause/)
- A later update wraps every MessagingService call so it cannot block, because those calls can sometimes yield indefinitely — [DevForum #246 by loleris](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543/246)
- `Profile:EndSession()` should be called when a player leaves (community example) — [DevForum ProfileStore thread](https://devforum.roblox.com/t/profilestore-save-your-player-data-easy-datastore-module/3190543/)

**MemoryStoreService**
- Each sorted map and each queue is capped at 1,000,000 items and 100 MB, and keys count toward the size of sorted maps. Hash maps have no stated item cap. Instead they have per-key request limits of about 5,000 write units and 15,000 read units per minute — [Memory stores docs](https://create.roblox.com/docs/cloud-services/memory-stores)
- Throttling starts at about 30,000 request units per minute per partition. Roblox calls this an estimate set on the backend that can change. A sorted map or queue sits on a single partition — [Memory stores docs](https://create.roblox.com/docs/cloud-services/memory-stores)
- The memory quota covers the whole experience. Items expire after 45 days by default (AddAsync / SetAsync), so set the shortest practical expiration. Extended Services can raise the limits — [Memory stores best practices](https://create.roblox.com/docs/cloud-services/memory-stores/best-practices)

**GDPR / right to erasure (RTBF)**
- Automatic RTBF deletion templates: you configure key patterns in advance, and Roblox deletes the matching standard or ordered data store entries when it processes an erasure request, with no code to host. Roblox recommends using this first — [RTBF and creators](https://create.roblox.com/docs/production/publishing/RTBF-and-creators.md)
- Webhooks: the "Right to Erasure Request" trigger sends a payload with the User ID and the Start Place IDs. Roblox's sample bot calls DELETE on the Open Cloud standard data store entries endpoint. Use this route for data outside data stores, schemas the templates do not support, or custom logic — [Automate right to erasure](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure)
- One developer using ProfileService reported deletions failing through the webhook bot. The suspected cause was API key permissions or the scope/key format, and the thread had no resolution — [DevForum](https://devforum.roblox.com/t/gdpr-discord-bot-failing-to-remove-the-player-data/2844520)

### Inferences
- From late July 2026, scripts that bulk-read or migrate data through Open Cloud compete directly with live servers for the same budget, so run backfills at low CCU and rate-limit them yourself.
- Most "60 + 10 × players" advice online is out of date. Plan budgets per experience and per request type.
- If RTBF deletion templates are used, key names should contain the UserId (e.g. `Player_<UserId>`) so the patterns can match. This is my inference from how the templates work and is not confirmed.
- Wrappers such as ProfileStore use about 1 UpdateAsync per auto-save interval (300 s) per player. Under the new budgets that is far inside the limits, so the binding constraint is the per-key 4 MB/min write throughput and the 4 MB value size.

### Gaps
- I could not open the versioning page, so these are unverified: version retention (commonly quoted as 30 days), the ListVersionsAsync/GetVersionAsync signatures, DataStoreSetOptions:SetMetadata, and attaching UserIds for GDPR. The metadata size limit is also unconfirmed.
- I did not confirm whether server-level DataStore limits still apply in addition to the per-experience budget.
- I did not check whether ProfileStore has tagged releases or new API since 2025, and `MessageAsync` is unverified.
- MemoryStore quota formula: the familiar 64 KB + 1 KB × users did not appear in the snippets and is unconfirmed.

## 2. Purchases: ProcessReceipt and MarketplaceService 2025–2026

### Takeaway
ProcessReceipt has to be idempotent on `PurchaseId`. Grant the item and record the PurchaseId in the same session-locked save. Return `PurchaseGranted` only after that save succeeds, and return `NotProcessedYet` otherwise. Recent API changes: GetProductInfo is deprecated in favour of `GetProductInfoAsync`, `PromptBulkPurchase` and subscription-info APIs exist, and the creator ID for group creators now returns 0.

### Cited Findings
- Roblox's "Implement player data and purchasing systems" guide pairs the purchase flow with session-locked player data — [Player data and purchasing](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing)
- Community best practice: store fulfilled PurchaseIds together with the player data in the same save, so the grant and the record succeed or fail together. Never return PurchaseGranted at the end of the function by default. Return NotProcessedYet on any failure so Roblox calls the callback again — [DevForum: returning PurchaseGranted at the end](https://devforum.roblox.com/t/is-returning-purchasegranted-at-the-end-bad-practice/279109); [DevForum: purpose of recording ProcessReceipt](https://devforum.roblox.com/t/whats-the-purpose-of-recording-a-successful-processreceipt/149411)
- Receipts can arrive again after network errors or server restarts, or on another server after a teleport, so the duplicate check has to work across servers. Keeping an in-memory set of PurchaseIds being processed and returning NotProcessedYet guards against parallel duplicates — [DevForum: ProcessReceipt called increasing amounts](https://devforum.roblox.com/t/processreceipt-is-called-at-increasing-amounts-per-purchase/2128255); [third-party guide](https://gamertagmythras.com/blog/roblox/roblox-game-passes-developer-products-guide)
- `GetProductInfo` is deprecated and `GetProductInfoAsync` is the preferred descriptor — [MarketplaceService reference](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService); [robloxapi](https://robloxapi.github.io/ref/class/MarketplaceService.html)
- `PromptBulkPurchase(player, lineItems, options)` exists. I found no usage details — [MarketplaceService reference](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService)
- Subscription APIs include `GetSubscriptionProductInfoAsync(subscriptionId)`, `GetUserSubscriptionDetailsAsync`, `GetUserSubscriptionPaymentHistoryAsync` and `GetRobloxSubscriptionDetailsAsync(user)` — [MarketplaceService reference](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService)
- [2026] Breaking change: for group-created products, the ID field returned by GetProductInfo/GetProductInfoAsync is now 0. Use `CreatorType` and `CreatorTargetID` instead — [DevForum: Updates to GetProductInfo return values](https://devforum.roblox.com/t/updates-to-marketplaceservice-getproductinfo-return-values/4666671)
- Prices are set by the backend and can change, so read them through GetProductInfoAsync and do not hardcode them — [robloxapi](https://robloxapi.github.io/ref/class/MarketplaceService.html)

### Inferences
- Under ProfileStore, the usual pattern is: wait for the session-locked profile, check whether `Data.PurchaseIds` already contains the ID, grant if not, append the ID while capping the list length, then save, and return PurchaseGranted only after the save succeeds. This is the community pattern, not an official Roblox sample.

### Gaps
- I could not retrieve the official ProcessReceipt reference text, i.e. the current sample, the retry cadence, and whether the callback fires again on rejoin.
- I could not confirm any 2025–2026 purchase APIs beyond those listed above (e.g. price-optimization APIs, regional pricing).

## 3. Security: remote validation, server authority, anti-exploit, Hyperion

### Takeaway
The client is untrusted. Every remote, Touched event, ProximityPrompt and ClickDetector handler has to validate input and rate-limit on the server. The biggest change in 2025–2026 is Roblox's built-in **Server Authority**, which went from Early Access (2025) through a Studio Beta (late 2025) and a Client Beta (Apr 2026) to **Full Release (July 2026)**. You enable it with `Workspace.AuthorityMode = Server`. It blocks physics exploits such as speed hacks without custom anti-cheat code, uses prediction and rollback to stay responsive, and depends on the Input Action System for client input.

### Cited Findings
- The official guide says any server logic a client can trigger can be spammed. Client-side rate limits must never be the only defense. Use a token bucket, which allows bursts but enforces an average rate. Validate fire rate, ammo, whether the target is a valid enemy, and whether it is alive — [Securing the client-server boundary](https://create.roblox.com/docs/scripting/security/client-server-boundary)
- RemoteEvents and UnreliableRemoteEvents are each limited to about 500 requests per second per client. UnreliableRemoteEvent payloads above 1000 bytes are dropped (current docs); older docs said 900 bytes. Buffers are compressed, which makes it hard to check the size before firing — [UnreliableRemoteEvent reference](https://create.roblox.com/docs/reference/engine/classes/UnreliableRemoteEvent); [older developer.roblox.com reference](https://developer.roblox.com/api-reference/class/UnreliableRemoteEvent)
- [Sept 2025, RDC25] Server authority was in closed beta. It was described as moving the source of truth for critical gameplay to the server, on by default with the default character controllers and physics objects — [Roblox Newsroom RDC 2025](https://about.roblox.com/newsroom/2025/09/roblox-rdc-2025); [Creator Roadmap RDC update](https://devforum.roblox.com/t/creator-roadmap-2025-rdc-update/3961527)
- [2025] Early Access warned: "If you publish games using this API your players will NOT be able to play" — [DevForum Early Access](https://devforum.roblox.com/t/early-access-server-authority/3983188)
- [Late 2025] Studio Beta: "you can feel confident that the structure of Server Authority is ready for you to build upon" — [DevForum Studio Beta](https://devforum.roblox.com/t/studio-beta-build-fair-responsive-games-with-server-authority/4139157)
- [Late Apr 2026] The Client Beta allowed publishing and testing at scale — [Weekly Recap Apr 26–30 2026](https://devforum.roblox.com/t/weekly-recap-april-26-30-2026/4613373); [Client Beta post](https://devforum.roblox.com/t/client-beta-publish-test-your-server-authoritative-experiences/4606949)
- [May 2026] Engineering deep dive: Input Actions are "the only way to send data from Client → Server that the server accepts for inputs" — [Server Authority Tech Deep Dive](https://devforum.roblox.com/t/server-authority-tech-deep-dive-engineering-insights/4624565)
- [July 2026] Full release: "Server Authority is now available for all creators. Block physics-based exploits like speed hacks without custom anti-cheat code, while prediction and rollback help preserve a responsive player experience". Setup includes setting `AuthorityMode` to `Server` in Workspace — [Roblox on X](https://x.com/Roblox/status/2075267517111582783); [DevForum Full Release](https://devforum.roblox.com/t/full-release-ship-fair-and-competitive-games-with-server-authority/4727993)
- How it works: the core simulation runs on the server, clients send inputs, and the server sends state back and overwrites the client when they differ. Caveat: AnimationTrack references cannot be relied on beyond one frame because server authority can override animations that play locally — [Server Authority Studio Beta Updates](https://devforum.roblox.com/t/server-authority-studio-beta-updates/4503827)
- Teleport security: new server-side teleport control. `TeleportService.AllowClientTeleports` defaults to "Fully Open", so existing games are unchanged — [DevForum: Revamped Teleport controls](https://devforum.roblox.com/t/revamped-teleport-controls-and-introducing-server-side-teleport-control/4349211)
- Hyperion is anti-tamper software in the Roblox client, made by Byfron (acquired Oct 2022). It detects software interacting with the client and crashes the client. The 64-bit rollout began May 2023, and the rollout blocked Wine/Linux in 2024 — [Roblox wiki (BreezeWiki mirror)](https://breezewiki.discard.no/roblox/wiki/Hyperion); [It's FOSS](https://itsfoss.com/news/roblox-linux-end/)
- Anecdotally, macOS executors (e.g. "Macsploit") and some Android executors kept working in 2024. These are community reports, not verified — [same wiki/forum summary](https://breezewiki.discard.no/roblox/wiki/Hyperion)

### Inferences
- From July 2026, new competitive or physics-heavy games should use Server Authority together with the Input Action System rather than writing their own movement anti-cheat. Server-side validation of remotes is still needed for gameplay logic such as economy, damage and inventory.
- Hyperion only raises the cost of running exploits on the client. It does not replace server validation.

### Gaps
- I found no reliable 2025–2026 Roblox announcement about Hyperion updates. Searches returned mostly 2022–2024 or low-quality sources.
- Server Authority performance cost, player-count limits and compatibility with custom character controllers were not confirmed.

## 4. Performance: profiling, memory, mobile budgets, Parallel Luau, native codegen, streaming

### Takeaway
Use the MicroProfiler for frame timing, the Developer Console for memory categories, and Luau heap snapshots to find memory leaks. Official baseline-device budgets are roughly 600–1,000 draw calls and 650K–1M triangles; doc versions differ. Native codegen (`--!native`) has been production-ready since 2024 and gained Android support in 2025. Parallel Luau requires multiple Actors, and `require()` is not allowed in the parallel phase. For streaming, keep Persistent models to a minimum and use SLIM LOD for static models.

### Cited Findings
- Performance problems fall into three groups: frame rate, memory and load time. The Developer Console shows memory, server health and script stats, and opens the client or server MicroProfiler — [Identify performance issues](https://create.roblox.com/docs/performance-optimization/identify)
- The MicroProfiler gives visual timing for engine tasks per frame. Find the spike in the frame-time graph, then find the cause in the timeline. 16.67 ms per frame equals 60 FPS — [MicroProfiler docs](https://create.roblox.com/docs/performance-optimization/microprofiler)
- Memory categories include UntrackedMemory, PlaceScriptMemory (which includes custom memory tags) and CoreScriptMemory. PlaceMemory and PlaceScriptMemory matter most. Use the Luau heap tool for snapshots — [Memory usage docs](https://create.roblox.com/docs/studio/optimization/memory-usage.md)
- Budgets: one version of the official page gives 1,000 draw calls and 1,000,000 triangles on the baseline device, another gives 600 draw calls and 650,000 triangles. The Studio emulator is inaccurate for memory, so test on real devices. Enable streaming if memory is high — [Design for performance](https://create.roblox.com/docs/performance-optimization/design)
- Community figures (DevForum, mid-2024): 500K triangles and 500 draw calls keep 60 FPS on 90%+ of phones and tablets. Keep client memory under about 1.3 GB to support 2 GB phones. These are not official — [DevForum optimization article](https://devforum.roblox.com/t/3127146)
- [July 2024] Native code generation left Preview and is fully supported on x64 and ARM64 — [Luau Recap July 2024](https://luau.org/news/2024-07-23-luau-recap-july-2024/)
- [Dec 19 2025] Native codegen gained Android support and has been tested in production. `vector.dot` lowers to a CPU dot-product instruction, and `vector.lerp`/`math.lerp` use a new MULADD_NUM instruction that becomes FMA where the CPU supports it. Load-store propagation can remove temporary userdata allocations — [Luau Recap for 2025: Runtime](https://luau.org/news/2025-12-19-luau-recap-runtime-2025/)
- Typical native-code speedups are 1.5×–2.5× on compute-heavy code (secondary source). One community benchmark found Luau with partial native compilation about 1.6× slower than LuaJIT 2.1 in JIT mode — [Wikipedia: Luau](https://en.wikipedia.org/wiki/Luau_(programming_language)); [Hacker News](https://news.ycombinator.com/item?id=45682560)
- Parallel Luau: `task.desynchronize()` and `task.synchronize()` switch phases, and `ConnectParallel` runs a callback in parallel. Scripts in the same Actor run sequentially, so you need multiple Actors. `require()` cannot be used in the desynchronized phase. SharedTable is shared across Actors without copying and updates atomically — [Parallel Luau docs](https://create.roblox.com/docs/scripting/multithreading)
- Community advice: write to a SharedTable only in the serial phase and buffer changes locally. One measurement put a write at about 0.003–0.01 ms — [DevForum SharedTable Best Practices](https://devforum.roblox.com/t/sharedtable-best-practices/2574316)
- Streaming: Persistent models load after join, never stream out, and stay in memory on every client, so use them sparingly. A static Persistent model costs little; frequent changes cost a lot. Atomic mode only guarantees that the model arrives together during initial replication. Set `LevelOfDetail = SLIM` on static models; animated or runtime-changing models are not supported — [Streaming techniques docs](https://create.roblox.com/docs/workspace/streaming/techniques); [creator-docs GitHub](https://github.com/Roblox/creator-docs/blob/main/content/en-us/workspace/streaming/techniques.md); [DevForum staff clarification](https://devforum.roblox.com/t/clarification-on-streaming-enabled-persistent-mode-sentence/2668431)
- Client scripts should wait for `PersistentLoaded`. `DataModel.Loaded` does not guarantee that persistent content has arrived (third-party guide) — [GamerTag Mythras](https://gamertagmythras.com/blog/roblox/roblox-instance-streaming-guide)
- [RDC25] SLIM (Scalable Lightweight Interactive Models) automatically merges and optimizes distant assets to cut vertex counts and draw calls, with launch targeted by the end of 2025. The terrain limit goes from 16K×16K to 64K×64K studs by mid-2026. RDC25 also announced 4K textures, emissive maps, and acoustic simulation in Studio beta — [GamesBeat](https://gamesbeat.com/roblox-dives-into-the-details-on-its-rdc-engine-updates-roblox-wallet-and-offline-play-press-briefing/); [Roblox Newsroom](https://about.roblox.com/newsroom/2025/09/roblox-rdc-2025)

### Inferences
- `--!native` belongs at the top of hot, number-heavy modules (math, vectors, buffers). Annotated types help the compiler (luau.org recap: it uses type annotations for specializations).
- For mobile, aim at the community budgets (≤500 draw calls, ≤500K triangles, under 1.3 GB client memory) and use the higher official numbers only as an upper limit.

### Gaps
- I found no Script Profiler documentation in the results (features, sampling rate).
- I did not confirm whether SLIM shipped as a full release (the docs describe it as a setting) or whether the 64K terrain change shipped.
- I found no official mobile memory ceiling.
- I did not find official SharedTable size limits.

## 5. Tooling: Rojo, Wally, Selene, StyLua, luau-lsp, Script Sync, AI/MCP, Open Cloud, testing

### Takeaway
There are now two workflows. Roblox's built-in **Studio Script Sync** (full release around June 2026) is easy to set up but limited for luau-lsp because it produces no sourcemap. The **Rojo** toolchain (Rojo 7.7.x, Wally 0.3.2, Selene 0.32, StyLua 2.5.x, luau-lsp 1.70.x, versions pinned with Rokit) is still the standard for Git-based professional workflows. Studio has a **built-in MCP server**, and its Assistant became agentic in April 2026 with Planning Mode and playtesting, plus external models such as Anthropic, OpenAI and Gemini via API key. Headless tests in CI run through the **Open Cloud Luau Execution API**: up to 5 minutes per task and 10 concurrent tasks per place.

### Cited Findings
- [About June 2026] Studio Script Sync full release: it syncs scripts and folders in the data model with Luau files on disk, so you can edit in VS Code, Cursor and similar. The full release adds conflict resolution, safer file deletion, a simpler workflow and Team Create sync indicators. It works "whatever your project setup" — [DevForum Full Release Script Sync](https://devforum.roblox.com/t/full-release-studio-script-sync/4688454); [RoUtility on X](https://x.com/RoUtilityNews/status/2067322619272343974)
- Limitation reported by the community: no sourcemap, so it does not combine well with Rojo and luau-lsp needs extra steps — [DevForum thread](https://devforum.roblox.com/t/best-way-to-port-an-existing-large-game-to-rojovs-code-script-dumping/4194522)
- Community alternatives: Azul (Studio-first two-way sync, generates a Rojo-compatible sourcemap, has a Rojo compatibility mode) and RbxSync (two-way sync for all instance types, MCP/AI integration, E2E tests) — [Azul DevForum](https://devforum.roblox.com/t/azul-%E2%80%94-easy-powerful-studio-first-two-way-sync/4159808); [RbxSync DevForum](https://devforum.roblox.com/t/rbxsync-%E2%80%93-two-way-sync-for-all-instance-types-native-ai-e2e-testing-zero-setup/4238545)
- Toolchain versions [as of 2026-10-04, from a GitHub PR bumping pins]: rojo 7.7.1, selene 0.32.0, luau-lsp 1.70.1, StyLua 2.5.2, wally 0.3.2. An older pin set had Rojo 7.5.1 / Wally 0.3.2 / Selene 0.28.0 / StyLua 2.1.0 / luau-lsp 1.48.0. Rokit manages them in `rokit.toml` — [KeepBlox PR #22](https://github.com/XopoIII/KeepBlox/pull/22); [rbx-wallstick rokit.toml](https://github.com/EgoMoose/rbx-wallstick/blob/main/rokit.toml); [Rojo docs](https://rojo.space/docs/v7/)
- Studio MCP server: open Assistant, go to … → Manage MCP Servers, and turn on "Enable Studio as MCP server". Tools include `execute_luau` (takes datamodel_type Edit, Client or Server), reading Studio state and play state, reading the output log, and capturing the viewport — [Connect to the Roblox Studio MCP server](https://create.roblox.com/docs/studio/mcp)
- [RDC25, Sept 2025] Assistant was upgraded to take multi-step actions, with MCP integration planned — [RDC25: What we announced](https://devforum.roblox.com/t/rdc25-what-we-announced/3920245)
- [Early 2026] Studio MCP updates and external LLM support for Assistant: Anthropic, OpenAI and Google Gemini models, or your own LLM via API key — [DevForum](https://devforum.roblox.com/t/studio-mcp-server-updates-and-external-llm-support-for-assistant/4415631)
- [Apr 16 2026] "Roblox Studio is Going Agentic": Planning Mode reads code and the data model, asks clarifying questions, and drafts an editable plan. It can playtest, find bugs and propose fixes. New Mesh Generation and Procedural Model Generation tools were added. Parallel multi-agent cloud workflows are not yet available. Integration with Claude, Cursor and Codex is in progress — [Roblox Newsroom](https://about.roblox.com/newsroom/2026/04/roblox-studio-going-agentic); [TechCrunch](https://techcrunch.com/2026/04/16/robloxs-ai-assistant-gets-new-agentic-tools-to-plan-build-and-test-games/)
- Open Cloud Luau Execution runs Luau headlessly in a place, for automated tests: up to 5 minutes per task and 10 concurrent tasks per place. The reference implementation is `place-ci-cd-demo`. It was announced as a beta in 2024 — [Luau Execution docs](https://create.roblox.com/docs/cloud/reference/features/luau-execution.md); [DevForum Beta announcement](https://devforum.roblox.com/t/beta-open-cloud-engine-api-for-executing-luau/3172185)
- The Open Cloud DataStore API supports DELETE on standard data store entries (used in the RTBF example) — [Automate right to erasure](https://create.roblox.com/docs/cloud/webhooks/automate-right-to-erasure)
- Testing: the Roblox/TestEZ repo is archived, though Roblox's own code has used it. Jest-Lua (jsdotlua) is a file-by-file port of Jest and a fork of Roblox's source-available jest-roblox, and it only runs inside Roblox — [Roblox GitHub](https://github.com/roblox); [jest-environment-roblox](https://classic.yarnpkg.com/en/package/@jsdotlua/jest-environment-roblox)
- [RDC26, Sept 2026] Studio Debugger Luau API (beta), expanded network simulation in Studio, multiple client views for multiplayer debugging, client sessions and logs (late 2026), and Compute Functions (serverless Luau, event-driven or scheduled, without hosting a game server; target early 2027) — [Creator Roadmap 2026 Fall Update](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208); [Roblox Creator Updates](https://create.roblox.com/updates)

### Inferences
- Recommended stack for late 2026 Git workflows: Rokit, then Rojo 7.7, Wally, Selene, StyLua and luau-lsp, with Jest-Lua tests run in CI through Open Cloud Luau Execution. Script Sync suits teams that work Studio-first.
- AI agents can drive Studio through the official MCP server (`execute_luau`). The same execution rights mean they can run arbitrary code, so review what they do.

### Gaps
- I did not confirm whether Open Cloud Luau Execution is out of beta by Oct 2026.
- I did not confirm whether Rojo 7.7 is still maintained (no official release-notes snippet found).
- I did not check Wally registry status or alternatives such as pesde.

## 6. New engine, Studio and Luau features 2025–2026 (RDC25, RDC26, DevForum)

### Takeaway
2025–2026 releases: Input Action System (full release, mid-2026), Server Authority (full release, July 2026), Luau's new type solver (general release; the beta toggle was removed January 7, 2026), the Luau `const` keyword, require-by-string with aliases and relative paths (implemented), Studio Script Sync, custom matchmaking for all experiences, server-side teleport control, 4D generation / GenerateModelAsync (beta Feb 2026, Mesh Generation API retired March 18, 2026), TextGenerator with structured JSON output, Animation Graphs (live July 2026), and RDC26 items (Compute Functions, State Machines for Animation Graphs, 2D/orthographic camera, browser play).

### Cited Findings
**Luau language and type system**
- [Late 2025] Luau's new type solver reached general release. The Studio beta toggle is removed in the first release of the new year (January 7, 2026), and users are migrated automatically. Beta users running strict mode have to set a workspace property. Features: read-only table properties, better refinements, type functions, singleton improvements. Known issue: error messages are more verbose. Shared self-types for `:` methods were planned for early 2026 — [DevForum General Release](https://devforum.roblox.com/t/general-release-luau%E2%80%99s-new-type-solver/4084991)
- The new solver beta started September 2024 with typestate tracking and read-only properties — [DevForum New Type Solver Beta](https://devforum.roblox.com/t/new-type-solver-beta/3155804)
- The user-defined type functions RFC lets you write functions that compute types — [RFC: User-Defined Type Functions](https://rfcs.luau.org/user-defined-type-functions.html); [DevForum tutorial](https://devforum.roblox.com/t/luaus-new-type-solver-how-to-utilize-type-functions/3637378)
- The `const` keyword for local constant bindings, which cannot be reassigned and are checked statically, was added (RFC #166, contextual keyword). I did not find an exact release date — [RFC PR #166](https://github.com/luau-lang/rfcs/pull/166); [RFC index](https://rfcs.luau.org/)
- Require-by-string: the aliases and relative-paths RFCs are implemented. In 2025 a standalone Luau.Require library was built for embedders — [RFC Aliases](https://rfcs.luau.org/require-by-string-aliases.html); [RFC Relative Paths](https://rfcs.luau.org/new-require-by-string-semantics.html); [Luau Recap 2025 Runtime](https://luau.org/news/2025-12-19-luau-recap-runtime-2025/)
- A 64-bit integer type RFC exists. Integers never convert implicitly to number or string. Implementation status is unconfirmed — [RFC 64-bit Integer Type](https://rfcs.luau.org/type-long-integer.html)

**Input**
- Input Action System: Studio Beta in 2025 added the instances InputContext, InputAction and InputBinding and the enum InputActionType. The Client Beta (publishable) had updates on 2025-11-21, 2026-02-11 and 2026-06-11. Full release came around mid-2026, and the default player scripts are being migrated to IAS in three phases. The Input Action Manager Studio beta followed — [Studio Beta](https://devforum.roblox.com/t/studio-beta-new-input-action-system/3656214); [Client Beta](https://devforum.roblox.com/t/client-beta-input-action-system-is-now-available-to-publish-in-experiences/3890979); [Full Release](https://devforum.roblox.com/t/full-release-input-action-system-ias-newly-converted-player-scripts/4678416); [Input Action Manager](https://devforum.roblox.com/t/studio-beta-input-action-manager/4737890)

**Audio**
- New audio API: AudioPlayer connects to AudioEmitter through Wire instances, and AudioListener produces 3D spatialization. `AcousticSimulationEnabled` (occlusion, diffraction, reverb) has to be on for both the emitter and the listener. One AudioPlayer can feed several emitters through wires. `SimulationFidelity` is deprecated — [AudioEmitter reference](https://create.roblox.com/docs/reference/engine/classes/AudioEmitter)

**Matchmaking and teleport**
- Custom Matchmaking with custom signals (e.g. skill rating): beta in 2025, then available to all experiences through the dashboard. It only applies to teleports into public servers, not reserved servers. Spring 2026 added a TextChat signal — [DevForum Beta](https://devforum.roblox.com/t/beta-introducing-custom-matchmaking-with-custom-signals/3598471); [DevForum all experiences](https://devforum.roblox.com/t/custom-matchmaking-is-now-available-to-all-experiences-on-roblox/4051419); [Creator Roadmap Spring 2026](https://devforum.roblox.com/t/creator-roadmap-2026-spring-update/4625473)
- [Feb 13 2026] `TextChatService:GetChatGroupsAsync` groups players who can chat together so they can be teleported together — [DevForum New Chat APIs](https://devforum.roblox.com/t/new-chat-apis-teleport-users-who-can-chat-together/4337233)
- API changes: `TeleportService.TeleportSwitchServer` was added (with a `gameIdsToExclude` parameter), and `TeleportPartyAsync` and `TeleportToPlaceInstance` are marked deprecated. Dates in the changelog are inconsistent — [robloxapi updates](https://robloxapi.github.io/ref/updates/index.html)

**Generative AI APIs**
- [Jan 2026] Early Access for in-experience 4D functional objects. [Feb 2026] 4D generation is in beta for all experiences. `GenerateModelAsync` replaces the Mesh Generation API, which was retired on March 18, 2026. TextGenerator gained structured JSON output — [Early Access 4D](https://devforum.roblox.com/t/early-access-introducing-in-experience-4d-functional-objects-and-enhanced-3d-generation/4050893); [Beta 4D Generation](https://devforum.roblox.com/t/beta-4d-generation-unlock-new-types-of-gameplay/4331818)
- The Text Generation API (TextGenerator, beta 2025) is used for dynamic NPC dialogue — [DevForum Beta Text Generation API](https://devforum.roblox.com/t/beta-introducing-text-generation-api/3556520)
- Cube 3D is Roblox's 3D generation foundation model — [Wikipedia: Cube 3D](https://en.wikipedia.org/wiki/Cube_3D)

**Animation and avatar**
- [July 2026] Animation Graphs went live — [Weekly Recap July 13–17 2026](https://devforum.roblox.com/t/weekly-recap-july-13-%E2%80%93-17-animation-graphs-go-live-5%C3%97-more-data-store-storage/4743286). [Oct 2026] Studio Beta "State Machines and Luau Expressions for Animation Graphs" — [DevForum](https://devforum.roblox.com/t/studio-beta-introducing-state-machines-and-luau-expressions-for-animation-graphs/4921939)
- [RDC25] The global avatar system gets more lifelike running, climbing, swimming and vaulting — [GamesBeat](https://gamesbeat.com/roblox-dives-into-the-details-on-its-rdc-engine-updates-roblox-wallet-and-offline-play-press-briefing/)

**RDC25 (Sept 2025) other items**
- glTF export, SLIM, Assistant multi-step actions with MCP, 4K textures, emissive maps, acoustic simulation (Studio beta), and terrain up to 64K studs — [RDC25: What we announced](https://devforum.roblox.com/t/rdc25-what-we-announced/3920245); [GamesBeat](https://gamesbeat.com/roblox-dives-into-the-details-on-its-rdc-engine-updates-roblox-wallet-and-offline-play-press-briefing/)

**RDC26 (Sept 10–12 2026, San Jose)**
- 72 new roadmap items were added. Since RDC25, 130 roadmap features shipped, 79% of them on time. Planned: Compute Functions (serverless Luau, early 2027), client sessions and logs, direct sprite-sheet import, multiple client views (late 2026), a Studio Debugger Luau API (beta), and Extended Services for Compute — [Creator Roadmap 2026 Fall Update](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208); [Roblox Creator Updates](https://create.roblox.com/updates); [RDC26: What We Announced](https://devforum.roblox.com/t/rdc26-what-we-announced/4865880)
- 2D game support (orthographic camera, animated image containers, sprite-sheet import), UI blur, text shadows and better gradients, turn-based notifications (Studio Beta Oct 2026), browser play in Chrome by end of 2026, and offline solo play in 2027 (press coverage) — [Roblox IR press release 09/11/2026](https://ir.roblox.com/news/news-details/2026/Roblox-Unveils-New-Ways-to-Play-Build-and-Grow-at-the-Roblox-Developers-Conference-RDC/default.aspx); [allthings.how](https://allthings.how/roblox-rdc-every-major-announcement-for-players-and-creators/)

### Inferences
- In late 2026 the default stack for new projects is: new type solver in `--!strict`, IAS for input, Server Authority for physics and movement, the new audio API, and Animation Graphs.
- Code that uses the old Mesh Generation API stopped working after March 18, 2026, and teleport code should move off the deprecated TeleportPartyAsync and TeleportToPlaceInstance.

### Gaps
- Experience Events: not researched because the search budget ran out.
- TextGenerator rate limits and pricing, and GenerateModelAsync limits: not found.
- Exact release dates for Luau `const` and the IAS full release were not found.
- The RDC26 Luau language announcements (new syntax beyond `const`) are not known in detail.
