# Roblox Game Design for Retention: Onboarding, Core Loops, Progression, LiveOps, Social Systems, Benchmarks (2024–2026)

Research date: 2026-10-24. Source labels used below: **[OFFICIAL]** = Roblox docs/newsroom/IR/DevForum staff posts; **[STUDIO]** = claims by developers/studios; **[3P-DATA]** = third-party analytics (GameAnalytics etc.); **[PRESS]** = journalism; **[COMMUNITY]** = fan wikis, guide/trading sites, opinion blogs (low reliability).

Method note: The environment's web search budget ran out partway through (shared 200-search cap), and WebFetch only resolved raw.githubusercontent.com/github.com (DNS failed for about.roblox.com, dubit.io, naavik.co). Official Roblox design docs were therefore read in full via the public `Roblox/creator-docs` GitHub repo (the source of create.roblox.com/docs); most other material comes from search-result snippets and should be spot-checked. Several planned case-study searches (Dress to Impress, Fisch, Dead Rails, Doors, Blox Fruits, Adopt Me in depth; SocialService/friend-invite APIs; Gamer Robot, Simple Games) could not be run — see Gaps.

---

## 1. Retention benchmarks (D1/D7/D30, session length, playtime)

### Takeaway
On Roblox, retention is far lower than mobile-game folklore suggests: GameAnalytics' 2026 report (500+ games with ≥1M MAU, Aug 2025–Jul 2026) puts median D1/D7/D30 at about 10.3% / 1.6% / 0.5%, and even top-1% games reach only about 22% / 9% / 4.7%. Roblox's own dashboard benchmarks against similar experiences, and its example shows a 50th–90th percentile D1 band of 12.4%–24.1%. Since June 15, 2026 the discovery algorithm explicitly rewards 28-day retention, which makes D7/D30 commercially decisive rather than vanity metrics.

### Cited Findings

**Third-party platform benchmarks (GameAnalytics 2026 Roblox Benchmark Report) [3P-DATA]**
- Sample: 500+ titles with ≥1M MAU, Aug 2025–Jul 2026. 67 titles exceeded 10M monthly sessions and 253 exceeded 1M, for 4.76B sessions total — [GameAnalytics 2026](https://www.gameanalytics.com/reports/2026-roblox-report); [Mellow/GameDevReports summary](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox-game-metrics-in-2026). Note: the URL in search results was gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox.
- Median game retention is **D1 10.3%, D7 1.6%, D30 0.5%**. The report calls this "normal for the platform, not a sign of a failing game" — [GameAnalytics 2026](https://www.gameanalytics.com/reports/2026-roblox-report); [RRQ World](https://blog.rrqworld.com/roblox-game-retention/)
- Percentile spread: D1 runs from **8.4% (25th percentile) to 22.2% (99th)**, and D30 from **0.3% to 4.7%**. **Top-1% games: D1 22.2%, D7 9.1%, D30 4.7%** — [GameAnalytics 2026](https://www.gameanalytics.com/reports/2026-roblox-report)
- The report says the widely quoted "20% D1 = good / 40% D1 = excellent" thresholds usually come from small samples of already-promoted games — [GameAnalytics 2026](https://www.gameanalytics.com/reports/2026-roblox-report)
- Session length per game: **median 9.8 min**, top 5% 16.6 min, top 1% 21.1 min — [Mellow summary](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox)
- Sessions per player per day, per game: **median 1.56**, top 10% 3.22, top 1% 8.3 — same source
- Player level (all Roblox games): the median player opens games **3×/day**; the top 10% open 11, the top 1% open 42. Median player session is **7.28 min** (top 1%: 74.82 min). Median daily in-game time is **22.4 min**; the top 10% spend 123.85 min, the top 1% spend 404.98 min — same source
- Caveat: Roblox's own figure of about 2.7 h/day per user includes non-game activity (chat, avatar editing). GameAnalytics counts only in-game time — [Mellow summary](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-roblox)
- The 2025 GameAnalytics report used a different sample and breaks retention down by session-length band. In the 0–3 min band, the 75th percentile is about **D1 7.4%, D7 1.0%, D30 0.3%**. It identified **return frequency (more sessions), not longer sessions**, as the biggest 2025 shift. The 2025 and 2026 numbers are not directly comparable — [GameAnalytics 2025](https://www.gameanalytics.com/reports/2025-roblox-report); [InvestGame PDF](https://investgame.net/wp-content/uploads/2025/09/2025-Roblox-Benchmark-Report.pdf)
- An older GameAnalytics summary (2023, **label: older**) said only 12–15% of users return after day 1 — [GameDevReports 2023](https://gamedevreports.substack.com/p/gameanalytics-key-roblox-and-games)
- Genre tables: BLOXG claims D1/D7/D30 by genre (Simulator, Horror, Tycoon, Obby, RPG, FPS, Social, Adventure) across 850+ promoted games. The values could not be retrieved. Its qualitative claim is that simulators and tycoons retain better than obbies and single-session games **[COMMUNITY, unverified methodology]** — [BLOXG benchmarks](https://bloxg.com/statistics/roblox-retention-benchmarks); [BLOXG guide](https://bloxg.com/guides/roblox-player-retention)
- Mobile "top quartile" figures (e.g., 40/20/10) are **mobile, not Roblox**, and should not be applied to Roblox — [Playio](https://blog.playio.co/d1-d7-d30-retention-benchmarks-2026); [GameGrowthAdvisor](https://gamegrowthadvisor.com/blog/2026-03-17-mobile-game-retention-strategies-2026/)

**Official Roblox analytics benchmarks [OFFICIAL]**
- Each KPI shows a similar-experience benchmark as a **50th–90th percentile range**. Roblox's example: a D1 benchmark of 12.4%–24.1% means 50% of similar experiences are at or below 12.4% and 10% are at or above 24.1% — [Roblox Analytics Dashboard docs](https://create.roblox.com/docs/production/analytics/sales-data)
- Benchmark pool for overall-success KPIs: the top 1,000 experiences by total playtime over a rolling 30 days, excluding experiences under 30 days old. Top 200, Top 500, and Top 1000 are available as tiers. Benchmark comparison requires **100+ DAU** — same source
- Roblox recommends focusing first on **D1 retention and average session time**, then D7 and D30, against similar-experience benchmarks — [Roblox Analytics docs](https://create.roblox.com/docs/production/analytics)
- Since about late 2025, D1/D7/D30 can be viewed **by acquisition source** on the Overview and Retention pages, with a choice between similar-experience and genre benchmarks — [DevForum announcement](https://devforum.roblox.com/t/analytics-view-retention-by-acquisition-source-and-select-your-benchmark-set/4010157)
- The Retention page shows daily cohorts over 10 days, weekly cohorts over 10 weeks, and per-cohort 7D playtime/user, 7D payer conversion, and 7D/30D revenue per user. It notes that a large influx of new users can temporarily dip retention — [creator-docs retention.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/analytics/retention.md)
- Earlier "Similar Experience Benchmarks" launch (**2023, older**) — [DevForum](https://devforum.roblox.com/t/analytics-similar-experience-benchmarks-broader-access/2210285)

**Discovery algorithm ties benchmarks to traffic [OFFICIAL + PRESS]**
- On **June 15, 2026**, Roblox expanded "Recommended For You" from a 7-day to a **28-day** evaluation window, with separate signals for day 1, days 2–7, and days 8–28. Qualified play-through rate was replaced with play-through rate (PTR) and first-play bounce rate (a negative signal) — [Roblox newsroom "Optimizing Discovery"](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox); [PCGamesN](https://www.pcgamesn.com/roblox/adult-games-long-term-retention); [allthings.how](https://allthings.how/robloxs-new-recommended-for-you-algorithm-rewards-games-that-keep-you-hooked/)
- Vlad Loktev (Chief Creator Ecosystem Officer) said the goal is to "level the playing field for ambitious, high-quality games that keep players coming back for years." Roblox said it would publish the ranking signals and their relative weights — [PCGamesN](https://www.pcgamesn.com/roblox/adult-games-long-term-retention); [games.gg](https://games.gg/news/roblox-algorithm-adult-games-retention/)
- Earlier signals: the Q4 2024 shareholder letter says Roblox tunes its objective function "towards long-term retention." The Q2 2025 letter cites multi-task learning on "high value actions… that lead to retention, engagement, and monetization" — [Q4 2024 letter (SEC)](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000021/ex992-q42024shareholderl.htm); [Q2 2025 letter (SEC)](https://www.sec.gov/Archives/edgar/data/1315098/000131509825000261/q225shletterex992.htm)
- The impact is contested. Roblox claimed a platform DAU/engagement increase. Naavik reported developer confusion over impression swings, and a blog claims Roblox attributed a financial shortfall to the change **[COMMUNITY claim, unverified]** — [Naavik](https://naavik.co/digest/robloxs-expensive-year-of-good-intentions/); [lensblox](https://lensblox.com/blog/roblox-algorithm-change-2026-explained/)

**Acquisition/ads context [OFFICIAL]**
- RDC 2025 ads recap: in conversion-lift studies, the typical experience running ads saw **+150% impressions, +24% plays, +16% playtime** (varies with spend) — [DevForum Ads RDC recap](https://devforum.roblox.com/t/ads-for-creators-rdc-recap-and-what%E2%80%99s-next/3929106)
- More than 45,000 experiences used Ads Manager in 2025, up 70% YoY — [Roblox RDC 2025 newsroom](https://about.roblox.com/newsroom/2025/09/roblox-rdc-2025)

### Inferences
- A practical Roblox scorecard (2025–26, large games): D1 about 10% is median, about 15% is solidly above median, and 20%+ is roughly top 1–10% depending on the sample. D7 of 5%+ and D30 of 2%+ are elite. Small or unpromoted games should expect lower values, because the GameAnalytics sample excludes games under 1M MAU.
- Because discovery now weights days 8–28, the "D7→D30 shelf" (endgame, social hooks, update cadence) matters as much as FTUE. The Roblox docs map D1 to FTUE/core loop, D7 to progression, and D30 to endgame/social/updates (see section 2).
- Engagement growth on Roblox comes mainly from session frequency (multiple short returns per day) rather than long sessions. This favors timers, restocks, offline/idle growth, and scheduled events (consistent with Grow a Garden's design).

### Gaps
- No official Roblox genre-level D1/D7/D30 numbers were found. The in-dashboard genre benchmarks are visible only to developers.
- BLOXG genre values could not be retrieved, and its methodology is unverified.
- No headline retention statistic from RDC 2025 or RDC 2026 was found.
- No verified retention numbers for specific hit games (Grow a Garden, Steal a Brainrot, etc.) — studios don't publish them.

---

## 2. Official Roblox game-design guidance (onboarding, core loops, monetization, LiveOps, funnels, Experiments, analytics events)

### Takeaway
Roblox's official docs set out a coherent retention playbook. FTUE is measured by D1, and players should reach the fun in 5 minutes or less. The core loop has three layers and must feed a progression engine. LiveOps combines a cadence of small content drops (2–4 weeks per the analytics docs; weekly is ideal and monthly is the minimum per the monetization docs) with major updates every 2–3 months. The toolchain for measuring and tuning all of this is server-side funnel/economy/custom events, Experiments (A/B, 14–60 days), and Configs (live tuning).

### Cited Findings

**Onboarding / FTUE [OFFICIAL]** — [onboarding.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/onboarding.md); [create.roblox.com/docs/production/game-design/onboarding](https://create.roblox.com/docs/production/game-design/onboarding)
- FTUE = the first few minutes. Success is measured by **Day 1 retention** and completion of onboarding goals. The "Player Funnel" narrows at each step, and the goal is to minimize drop-off between steps.
- Goal 1, teach the essentials: controls (on-screen prompts, e.g., *Super Striker League*) and the **core loop** — players must understand "what they are expected to do and why."
- Goal 2, get to the fun fast: use low early XP thresholds so players level up quickly (tune them live with Configs), social motivators (test matchmaking in FTUE with Experiments), and starter items/currency (A/B test starting amounts, then roll out the winner with Configs).
- Goal 3, leave players wanting more: make short-, mid-, and long-term goals visible (skill trees, season passes, quests, collections; *Jailbreak*'s season pass is the example). Design "moments of joy" and a deliberate celebration at the end of onboarding.
- The analytics docs add: get users "to the fun in **5 minutes or less**," deliver a joyful moment after the first loop completion, preview future progress, and track completion of each FTUE step — [retention.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/analytics/retention.md)

**Onboarding techniques [OFFICIAL]** — [onboarding-techniques.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/onboarding-techniques.md)
- **Visual elements:** in-world signs in the line of sight (*Color or Die*), spotlight/dim highlights (*Hello Kitty Cafe*), persistent hints (*Jailbreak* footprints), directional arrows and trails (*Winds of Fortune*, *Hello Kitty Cafe*), and strong action feedback (damage numbers, screen pulse, coin rewards). Visuals are recommended because they need less translation and work for pre-readers and small mobile screens.
- **Contextual tutorials:** trigger them at the moment of need. *Squishmallows* shows the combine tutorial when a player holds two identical items, and reveals its marketplace only when players discover it, since it serves mid/late game.
- **Timed hints:** set the delay just past the time most players take (for example, if most players press "PLANT CABBAGE SEED" within 10 s, highlight it at 11 s). Show each hint once and only to struggling players. Use hints to surface overlooked features (e.g., highlight the trade button for players who haven't traded in their first two sessions). A/B test hint timing (5 vs. 10 s) with Experiments.

**Platform-specific design principles [OFFICIAL]** — [design-for-roblox.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/design-for-roblox.md)
- Most users are on mobile and sensitive to friction and load times: design mobile-first and avoid long tutorials (users leave for something more immediate).
- Users hop between games, often with friends. **"Tourists"** favor variety; **"locals"** make up almost the entire engaged base, and many locals start as tourists.
- The audience is aging. Older users invest more in engagement and monetization and anchor communities.
- Social play drives growth (friend invites) and retention (user-generated interaction as content). Single-player games are harder to retain. Don't price private servers so high that friend groups are discouraged. Support streamers (UI hiding, easy friend inclusion).

**Core loops [OFFICIAL]** — [core-loops.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/core-loops.md)
- Three parts: (1) minute-to-minute interaction, (2) the most repeated set of actions, and (3) a **progression engine** that feeds back into (1) and (2). "Without a progression system, a game becomes repetitive, boring, and shallow."

**Retention by horizon [OFFICIAL]** — [retention.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/analytics/retention.md)
- **D1:** core loop clarity, balanced challenge, FTUE, and performance (crash rate, FPS across devices).
- **D7:** progression with short- and long-term goals, content variety (modes, items, social features), and difficulty balance. Measure progression by granting an item per level and tracking time-to-level.
- **D30:** the "ending system" (what to do after main objectives) and regular updates: **smaller updates to existing mechanics every 2–4 weeks, larger feature updates every 2–3 months**. Add social mechanics (trading, parties, guilds, PvP, tournaments, leaderboards).

**LiveOps [OFFICIAL]**
- LiveOps has four parts: content cadence, major updates, QoL, and bug fixes. Cadence ranges from **weekly to monthly** depending on the team. Cadence content should reuse existing systems (pets, vehicles, weapons, maps, quests). Major update types: social (guilds, trading, parties), competitive (PvP, leaderboards, tournaments), collections/achievements (pets, season pass), and live events (map overhauls, new roles to re-engage lapsed players). Examples: *Jailbreak* (cadence plus majors) and *Doors* (QoL, bug triage). The docs explicitly recommend prioritizing team mental health and realistic schedules — [liveops-essentials.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/liveops-essentials.md)
- Content cadence: favor cheap, art-based variants (recolors, pets, furniture), and keep each cadence update **under three weeks of effort**. "Many games release every two weeks to one month." Use a consistent schedule so players anticipate releases. Content shouldn't be consumed instantly: add it at the end of progression, as limited-time content that takes "weeks" to finish, or through season passes. Examples: *Adopt Me!* pet variants and themed updates, *Robloxian High School* seasonal content, *Jailbreak* season pass — [content-updates.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/content-updates.md)
- The German Monetization/LiveOps section states players expect regular updates, that a **weekly rhythm is ideal, and monthly is the minimum** — [Roblox monetization docs (de)](https://create.roblox.com/docs/de-de/production/monetization)
- Event planning: pick target KPIs and model the impact on currency earning and spending (the *Overlook Bay 2* fishing tournament example). Monitor hourly or same-day data. Compare event vs. non-event periods, including the week before vs. the week after, to judge whether the effect lasted. Key indicators are short- and long-term retention and item/currency sales during and after the event. Announcing in advance lets players schedule their return, while a surprise announcement risks players missing it. Communicate externally (socials, Discord) and internally (login pop-ups, UI alerts, lobby displays; *World//Zero* example) — [liveops-planning.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/liveops-planning.md)

**Economy design for events [OFFICIAL]** — [balance-virtual-economies.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/balance-virtual-economies.md)
- Plan sinks before sources. The safest option is a separate **event currency** spent in an event shop. Use Expected Value (EV) modeling: in the *Feline Fishing Fun* example, a normal day yields 14G EV per attempt, or 14,000G per day at 1,000 attempts. An unmodeled event created a Gold surplus that **reduced revenue after the event**.
- Limited items: the example is a *Golden Salmon* available for 24 h with a 0.1% catch chance. Limited items must be included in EV models. A/B test prices with Experiments and run flash sales with Configs.

**Monetization and season passes [OFFICIAL]**
- Monetization foundations: give each item a clear purpose, mix durable and consumable items, balance enhancement and expression items, and use a contextual, rotating shop. Describe items accurately. Non-payers must still be able to earn rewards (free pass tracks). Season passes support daily engagement and long-term retention. Space rewards relative to average session length, and show time remaining and XP per level. Examples: *Doors* (Revives), *Tower Defense Simulator*, *Evade*, *Bot Clash Simulator*, *Jailbreak*, *Dragon Adventures* — [monetization-foundations.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/monetization-foundations.md)
- Users may downvote a game whose monetization they dislike — [Roblox monetization docs](https://create.roblox.com/docs/production/monetization.md)
- Season pass design:
  - Start with a **1-month season** and **at least 1 week of rest** between seasons to avoid team burnout.
  - Use about 10 tiers, with a brand-new final reward that is retired afterwards.
  - Require claim buttons with a notification badge, and auto-award unclaimed rewards at season end.
  - Use daily missions across at least 3 categories and 3 difficulty levels. Never require hard currency for missions.
  - Add **double XP in the final week** as catch-up, plus a weekly high-reward mission and co-op missions.
  - Players who upgrade mid-season receive premium rewards for tiers already completed.
  - [season-pass-design.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/season-pass-design.md)

**Funnels and analytics events [OFFICIAL]**
- Funnel types: **onboarding** (one-time), **progression**, and **shop** (recurring). The dashboard supports up to 10 funnels.
  - APIs: `LogOnboardingFunnelStepEvent(player, step, stepName)` and `LogFunnelStepEvent(player, funnelName, funnelSessionId, step, stepName)`.
  - Events are server-only and only work in published games. A funnel step expires after 180 days. Only the 10 most recent funnelSessionIds per user per funnel are tracked. Skipped steps count earlier steps as complete.
  - Recommendations: log step 1 in `PlayerAdded`, use a GUID for store sessions, and validate client-sent step numbers against exploits.
  - Docs example ("Plant" game): about **70% drop-off between "In Farm" and "Plant Seed"**, fixed with contextual indicators and a forced plant-and-grow tutorial.
  - [funnel-events.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/analytics/funnel-events.md)
- Staff DevForum guide on finding onboarding drop-offs ("larger than expected drops… worth investigating") — [DevForum: Improving Onboarding through Funnel Events](https://devforum.roblox.com/t/improving-onboarding-through-funnel-events/3064458)
- AnalyticsService also covers:
  - `LogEconomyEvent(player, flowType, currencyType, amount, endingBalance, transactionType, itemSku, customFields)`, limited to **5 currency types per experience**.
  - `LogCustomEvent(player, eventName, value, customFields)`, limited to **8,000 unique custom-field combinations**.
  - `LogProgressionEvent`, `LogProgressionCompleteEvent`, and `LogProgressionFailEvent`.
  - [AnalyticsService reference](https://create.roblox.com/docs/reference/engine/classes/AnalyticsService)

**Experiments (A/B) and Configs [OFFICIAL]** — [experiments.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/experiments.md); [create.roblox.com/docs/production/experiments](https://create.roblox.com/docs/production/experiments.md)
- Two types: **in-game** experiments test Config values, with up to 2 variants plus a control and a configurable rollout %. **Matchmaking** experiments allow up to 3 variants, need no code, and only one can run at a time (100% rollout recommended). **Duration is 14–60 days.**
- Every experiment tracks D1 retention, D7 retention, playtime, ARPU, ARPPU, payer conversion, and session time.
- Games under **1,000 DAU** may struggle to get useful data. Harm decisions need 10,000+ players across variant and control. Early-harm thresholds: playtime −10%, ARPU −20%, payer conversion −20%. The docs warn about novelty effects (run the full duration).
- A Roblox newsroom feature (Aug 2026) shows **Uplift Games (Adopt Me!)** using Analytics and Experiments. UpliftBradB said that during a summer event feature "the crash rate and frame rate clued us in that something was going wrong" **[STUDIO via OFFICIAL]** — [Roblox newsroom, Aug 2026](https://about.roblox.com/newsroom/2026/08/optimize-testing-live-updates-roblox-analytics-experimentation-platform) (snippet only; page fetch failed)

### Inferences
- Roblox's official cadence guidance is internally inconsistent: weekly ideal and monthly minimum (monetization docs), every 2–4 weeks for small updates (analytics docs), every 2 weeks to 1 month typical (content-updates docs). Top 2025 hits ran weekly (Grow a Garden, Steal a Brainrot), above the docs' sustainable baseline.
- The official toolkit (onboarding funnel → Experiments → Configs) makes "ship, measure, roll out the winner" possible without server restarts. The 1,000 DAU and 14-day minimums mean small games must rely on funnels and qualitative playtests instead of A/B tests.
- A Roblox-native onboarding blueprint: first core action within seconds (for example, plant a seed), first reward and celebration within about 1–3 minutes, visible next goal, then a timer that brings the player back later.

### Gaps
- The "Sketch Series: Onboarding Techniques" content and the full "Quest design" and "UI/UX" pages were not reviewed.
- The full Aug 2026 Roblox newsroom article on the Analytics and Experimentation platform could not be fetched (DNS failure). Only the Uplift snippet is available.

---

## 3. Case studies: what hit games and studios do

### Takeaway
The 2025–26 mega-hits (Grow a Garden, Steal a Brainrot, 99 Nights in the Forest) combine a dead-simple core loop with timers and offline growth or steal/defend tension, weekly Saturday updates paired with live **"Admin Abuse"** events (devs manipulate weather, mutations, and shop stock live in public servers), limited and unobtainable items, and trading economies. Older evergreen titles (Pet Simulator 99, Adopt Me) show the alternative: content-driven cadence, huge or limited pets, and trading infrastructure. Most evidence about mechanics comes from fan wikis and trackers; studios rarely publish metrics.

### Cited Findings

**Grow a Garden (BMWLux + Splitting Point Studios / Jandel)**
- Ownership: co-owned by original developer BMWLux and Splitting Point Studios, led by Janzen "Jandel" Madsen, with DoBig Studios as a minority holder. Jandel says the original version was built in **three days** **[PRESS/STUDIO]** — [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden); [LegalClarity](https://legalclarity.org/who-owns-grow-a-garden-roblox-studios-explained/)
- Splitting Point bought in around April 2025 at about **1,000 CCU**, put "almost all" its dev staff (**about 12 people**) on the game, and "started weekly updates" **[STUDIO, 2025]** — [GamesBeat interview with Janzen Madsen](https://gamesbeat.com/janzen-madsen-interview/); [Calcalist](https://www.calcalistech.com/ctechnews/article/dj4lxef8r)
- Scale: **21.3M CCU in June 2025** (Naavik) and a peak of **22.3M CCU on Aug 23, 2025** (Wikipedia). It lost the CCU record to Steal a Brainrot in Sept 2025 — [Naavik](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/); [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden). An earlier milestone was 8.9M CCU — [GameDiscoverCo](https://newsletter.gamediscover.co/p/what-grow-a-gardens-89-million-ccu)
- Revenue: Jandel declined to share figures. A **third-party** report cited about $12M in May 2025 item sales, unconfirmed by the studio — [Calcalist](https://www.calcalistech.com/ctechnews/article/dj4lxef8r)
- Design analysis **[3P analyst, Naavik]**:
  - Core loop: plant, wait, harvest, then unlock bigger plots and rarer plants.
  - Robux speeds up progress and enables stealing from neighbors.
  - Its gentle onboarding and idle timers recall FarmVille, Hay Day, and Idle Farming Empire, "entirely fresh" for much of the Roblox audience.
  - [Naavik](https://naavik.co/digest/predicting-the-next-big-hits-on-roblox/)
- Bot controversy: TD Cowen alleged bots inflated recommendation visibility. Roblox said its analysis showed genuine popularity — [Wikipedia](https://en.wikipedia.org/wiki/Grow_a_Garden)
- Admin Abuse **[COMMUNITY]**:
  - A weekly event, typically on **Saturdays alongside major updates**. Jandel or team members use admin powers to trigger **weather events** and manipulate **shop stock**.
  - A secondary weekly slot, "Watering Wednesday," was hosted by Jhailatte.
  - Admin events run only in **public servers**, not private ones.
  - Reported start times conflict (about 1 h before a 2 pm UTC update vs. about 8:30 pm UTC).
  - [GAG Fandom wiki](https://growagarden.fandom.com/wiki/Admin_Abuse); [Sportskeeda](https://www.sportskeeda.com/roblox-news/when-admin-abuse-start-grow-garden); [mygagcalculator](https://mygagcalculator.com/grow-a-garden-admin-events-schedule/)
- Grow a Garden 2 (2026) **[COMMUNITY]**:
  - Weekly Admin Abuse was reportedly dropped in favor of smaller content drops spread through the week, plus occasional **"Admin Party"** events.
  - The first Admin Party ran around Aug 1–2, 2026 (Jandel and DJ Jhai) and introduced a Jandel Monkey pet that became unobtainable after the 30-minute window.
  - A "Fall World" migration mechanic reportedly gave players 60 days to "Magic Mail" items to their main garden before losing them.
  - [gameboost](https://gameboost.com/blog/grow-a-garden-2-admin-abuse); [roonby](https://roonby.com/2026/07/03/does-grow-a-garden-2-have-admin-abuse-everything-we-know-so-far/); [mygagcalculator GAG2 tracker](https://mygagcalculator.com/grow-a-garden-2-event-tracker/)
- Splitting Point's earlier game *Field Trip Z* reached 45M players in a year, per a GameAnalytics blog **[STUDIO/3P, older]** — [GameAnalytics blog](https://www.gameanalytics.com/blog/splitting-point-how-field-trip-z-got-45m-players)

**Steal a Brainrot**
- It took the all-time Roblox CCU record from Grow a Garden in **Sept 2025** — [Wikipedia (Grow a Garden)](https://en.wikipedia.org/wiki/Grow_a_Garden); [Wikipedia (Steal a Brainrot)](https://en.wikipedia.org/wiki/Steal_a_Brainrot)
- Cadence **[COMMUNITY, conflicting]**:
  - Trackers describe an update "almost every **Saturday**" adding brainrots, events, **mutations**, and traits, with numbered updates up to Update 62 (2026-08-15).
  - Another tracker estimates new brainrot waves about every 2 weeks.
  - A weekly dev-hosted **Admin Abuse** event exists, and missing a Saturday event means waiting a week (FOMO).
  - [playbrainrot update log](https://www.playbrainrot.org/en/updates/); [allthings.how schedule](https://allthings.how/steal-a-brainrot-new-brainrots-schedule/); [Eldorado admin abuse](https://www.eldorado.gg/blog/steal-a-brainrot-en/steal-a-brainrot-admin-abuse-schedule-explained/)
- One guide site argues its retention comes from the **steal-and-defend tension** of the core loop and the trading market for rare brainrots, rather than codes, which are sparse **[COMMUNITY opinion]**. The 2026 update logs list permanent trading and Trade Plaza improvements — [timesaver.gg](https://timesaver.gg/blog/steal-a-brainrot-codes-october-2026); [Eldorado update log](https://www.eldorado.gg/blog/steal-a-brainrot-update-log/)

**99 Nights in the Forest (Grandma's Favourite Games)**
- Developers: Alec Kieft, Matt Hufton, and Cameron Angland. They told PCGamesN in Sept 2026 that "the numbers don't feel real," prefer to stay anonymous, and are "not keen" on using AI in their games **[STUDIO via PRESS]** — [PCGamesN interview](https://www.pcgamesn.com/roblox/99-nights-in-the-forest-interview)
- Scale: about 29–30B visits, and a group (founded 2020) with 10M+ members **[COMMUNITY trackers]** — [Roblox Fandom](https://roblox.fandom.com/wiki/Grandma's_Favourite_Games); [Rolimons](https://www.rolimons.com/game/79546208627805)
- IP extension: a 20th Century Studios live-action film (writer Josh Cooley; producers Sam Raimi and Rob Tapert; the devs as EPs), announced in 2026 — [Hollywood Reporter](https://www.hollywoodreporter.com/movies/movie-news/99-nights-in-the-forest-josh-cooley-20th-century-studios-film-1236704624/); [Variety](https://variety.com/2026/film/news/99-nights-in-the-forest-movie-20th-century-studios-1236720515/); [Deadline](https://deadline.com/2026/04/99-nights-in-the-forest-movie-1236859433/)

**Pet Simulator 99 (BIG Games)** **[STUDIO, official update posts]**
- An early-2024 post (**about 1,000 days old, older**) says BIG Games **stopped weekly updates** and moved to releasing when content is ready, targeting a Saturday release after significant work, with gaps of weeks between updates. Its target per major release: 25+ areas, a new rebirth, dozens of pets, and several new mechanics — [BIG Games: New Year's Event (Update 4)](https://www.biggames.io/post/pet-simulator-99-update-4)
- 2026 updates follow a pattern of **event-tied limited Huge pets**. The World Cup update had soccer minigames and **leaderboards**. The Coin Arcade update gave Huges from arcade zones and boss chests — [World Cup (Update 82)](https://www.biggames.io/post/pet-simulator-99-update-82); [Coin Arcade (Update 92)](https://www.biggames.io/post/pet-simulator-99-update-92)
- Trading infrastructure: a **Trading Terminal** lets players search for wanted items and teleports them to the trading plaza listing. An earlier update removed rank restrictions from trading — [Trading Cards (Update 48)](https://www.biggames.io/post/pet-simulator-99-update-48); also [RNG Event (Update 24)](https://www.biggames.io/post/pet-simulator-99-update-24), [Plant & Combine (Update 87)](https://www.biggames.io/post/pet-simulator-99-update-87)
- The update number reached about 92 by around Sept 2026 — [Coin Arcade](https://www.biggames.io/post/pet-simulator-99-update-92)

**Adopt Me! (Uplift Games)**
- Official docs cite Adopt Me!'s **pet variants** (spotted/colored recolors) and themed updates as the model for sustainable content cadence **[OFFICIAL]** — [content-updates.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/content-updates.md)
- Uplift uses Roblox Analytics and Experiments, and crash-rate and FPS monitoring caught a broken summer-event feature **[STUDIO via OFFICIAL]** — [Roblox newsroom Aug 2026](https://about.roblox.com/newsroom/2026/08/optimize-testing-live-updates-roblox-analytics-experimentation-platform)

**Jailbreak / Doors (cited in official docs)**
- *Jailbreak*: cadence releases plus major updates, and a season pass with free and premium tracks and a previewed final reward. *Doors*: examples of QoL updates, bug triage, and clear item explanations (Revives) **[OFFICIAL]** — [liveops-essentials.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/liveops-essentials.md); [monetization-foundations.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/monetization-foundations.md)

**Studios on process**
- **Gamefam (Joe Ferencz)** **[STUDIO]**:
  - Its $25M round went into creator partnerships, **analytics, live ops tools**, and ad tech. Ferencz credits "our live ops practices" with attracting top developers.
  - He names acquisition, retention, and monetization as the fundamentals, with acquisition "essentially fully dependent on the algorithm."
  - [GamesBeat](https://gamesbeat.com/gamefam-sees-rapid-growth-in-making-games-for-roblox/); [GamesBeat (5 of top 15 branded)](https://gamesbeat.com/gamefam-closes-year-of-growth-with-5-of-top-15-branded-games-on-roblox/); [Player Driven](https://playerdriven.io/desk/gamefam-s-joe-ferencz-on-roblox-s-metaverse-potential)
- **Dubit** **[STUDIO marketing]**: describes a "retention layer" (progression, unlocks, goals) and measures D1, D7, and **the shape of the retention curve** against internal data. Recommends a **monthly rolling live-ops budget** with a dedicated team — [Dubit services](https://dubit.io/services/roblox-game-development); [Dubit: How We Build Hit Roblox Games](https://dubit.io/blog/how-we-build-hit-roblox-games); [Dubit: What makes a new Roblox game take off?](https://dubit.io/library/what-makes-a-new-roblox-game-take-off)

**Recurring mechanic patterns across hits (synthesized from the above)**
- Timers and offline growth (GAG plants grow while offline, per Naavik's idle comparison). Restocking shops that the devs manipulate during Admin Abuse.
- **Weather events and mutations** as live multipliers (GAG weather via Admin Abuse; SaB weekly mutations and traits).
- **Limited and unobtainable items** (GAG2 Jandel Monkey, PS99 event Huges, Golden Salmon pattern in official docs).
- **Rebirths** as a progression reset (PS99 "a new rebirth" per major update).
- **Leaderboards** (PS99 World Cup).
- **Trading plazas and terminals** (PS99, SaB Trade Plaza).

### Inferences
- The weekly "Saturday update + live admin event" is the defining 2025 Roblox LiveOps pattern. It turns updates into appointments (CCU spikes), creates scarcity, and keeps public servers attractive, since admin events skip private servers and that drives social density. It is expensive: GAG used about 12 devs on one game, and BIG Games (PS99) moved away from weekly updates as early as 2024, and GAG2 reportedly shifted to smaller distributed drops plus irregular "parties." This points to the weekly-update treadmill being unsustainable even for top teams.
- For a new game, the official docs' sustainable baseline (biweekly to monthly cadence, under 3 weeks of effort per drop, majors every 2–3 months) plus one recurring scheduled live event is a more realistic target. Escalate to weekly only once DAU justifies a dedicated team.
- Limited items and admin events must be modeled economically (EV, event currencies) to avoid post-event revenue dips, as the official Feline Fishing example shows.

### Gaps
- Could not research (search budget exhausted): Dress to Impress (Gigi/Tiffany), Fisch, Dead Rails, Doors (LSPLASH) cadence and postmortems, Blox Fruits (Gamer Robot) update cadence, Simple Games, and Big Games interviews (only official patch posts found).
- No verified studio-published retention or revenue metrics for any of these games.
- Grow a Garden "offline progress" specifics and exact luck formulas were not verified from primary sources.
- The GamesBeat Madsen interview's full contents were not retrieved; only the snippet facts are listed.

---

## 4. Social mechanics (friend invites, parties, trading, guilds, server events, social proof) and the age-check/chat impact

### Takeaway
Roblox officially frames social play as both the main growth driver (friend invites) and retention driver (players as content). It recommends parties, trading, invites, guilds, PvP, and leaderboards, especially for D30. Since January 2026, chat requires a facial-age check and is restricted to similar age bands. This structurally weakens chat-dependent social loops (trading negotiation, cross-age friend groups), but no published data quantifies the effect on game retention.

### Cited Findings
- Social design drives growth (friend invitations) and retention (user-generated interaction as ongoing content). Single-player games are harder to retain. Build parties, trading, and invitations. Price private servers so friend groups aren't discouraged. Make it easy for streamers to bring in friends **[OFFICIAL]** — [design-for-roblox.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/design-for-roblox.md)
- D30 retention tactics include trading, parties, guilds, PvP, tournaments, and leaderboards **[OFFICIAL]** — [retention.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/analytics/retention.md). Major-update categories include social systems (guilds, groups, trading, parties) and competitive systems (PvP, leaderboards, tournaments) — [liveops-essentials.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/liveops-essentials.md)
- Use Experiments to test **matchmaking parameters during FTUE** for social games and measure long-term engagement. Timed hints can surface the **trade button** for players who haven't traded in 2 sessions **[OFFICIAL]** — [onboarding.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/onboarding.md); [onboarding-techniques.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/onboarding-techniques.md)
- Season pass: social mission categories (throw or attend parties, compete in races) and **cooperative missions** with shared progress **[OFFICIAL]** — [season-pass-design.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/season-pass-design.md)
- Server-wide events in practice: GAG and SaB admin events happen live in public servers (not private), creating shared moments and server-hopping **[COMMUNITY]** — [GAG wiki](https://growagarden.fandom.com/wiki/Admin_Abuse); [Eldorado](https://www.eldorado.gg/blog/steal-a-brainrot-en/steal-a-brainrot-admin-abuse-schedule-explained/)
- Trading as a retention engine: PS99 Trading Terminal and plaza, SaB Trade Plaza, and an active third-party trading and value-site ecosystem (e.g., growagardengame.com) **[STUDIO/COMMUNITY]** — [BIG Games Update 48](https://www.biggames.io/post/pet-simulator-99-update-48); [Eldorado SaB update log](https://www.eldorado.gg/blog/steal-a-brainrot-update-log/); [growagardengame.com](https://growagardengame.com/)
- Social proof and creator-led discovery: users follow YouTubers and streamers into new games, so support UI hiding for recording **[OFFICIAL]** — [design-for-roblox.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/design-for-roblox.md)
- **Age checks** **[OFFICIAL]**:
  - Announced Nov 2025 and live globally in early January 2026. Chat requires facial age estimation (vendor Persona) or ID (13+).
  - Users are grouped as under 9, 9–12, 13–15, 16–17, 18–20, and 21+, and chat is limited to similar age bands.
  - Roblox claims a mean absolute error of 1.4 years for under-18s.
  - Age checks also gate Studio Team Create and links.
  - [Roblox newsroom Nov 2025](https://about.roblox.com/newsroom/2025/11/roblox-requires-age-checks-limits-minor-and-adult-chat); [Roblox IR 2026](https://ir.roblox.com/news/news-details/2026/Roblox-Requires-Users-Worldwide-to-Age-Check-to-Access-Chat/default.aspx); [DevForum: now live globally](https://devforum.roblox.com/t/age-check-requirement-to-chat-now-live-globally/4226101/print); [DevForum: Age checks for chat, Team Create, links](https://devforum.roblox.com/t/age-checks-to-access-chat-studio-team-create-and-links-on-roblox/4079702); [Biometric Update](https://www.biometricupdate.com/202601/roblox-rolls-out-facial-age-estimation-for-chat-access-globally)
- Developer reaction is anecdotal. One DevForum creator said misclassification is common and claimed it "put a massive dent in the traffic." This is opinion, not data **[COMMUNITY]** — [DevForum thread](https://devforum.roblox.com/t/age-check-requirement-to-chat-now-live-globally/4226101/print)
- Platform context: Roblox's 2026 algorithm shift is framed as courting older ("adult") players and long-term retention **[PRESS]** — [PCGamesN](https://www.pcgamesn.com/roblox/adult-games-long-term-retention)

### Inferences
- With chat gated and age-banded, social systems that work **without free text** gain importance: structured trade UIs (offer/accept windows, trading terminals), emotes and gestures, party invites via platform friends, co-op missions, shared server events, and leaderboards. A trading design that depends on chat haggling is now riskier.
- Admin-style live events and server-wide weather work as "chat-less social proof." Everyone sees the same event at once.
- Monetization and social interact: private-server pricing and "public-server-only" events pull in opposite directions. Hits chose to keep events public to concentrate players.

### Gaps
- No search could be run on Roblox's friend-invite and referral APIs (SocialService:PromptGameInvite, invite rewards), the Parties feature, or the Experience Invites API changes in 2025–26.
- No quantitative data on how age checks affected engagement in social or trading games.
- No guild-system case studies were found.

---

## 5. Anti-patterns: churn causes, dark-pattern criticism, update burnout

### Takeaway
Official guidance points to the main churn causes: slow or long tutorials, unclear core loops, missing progression or endgame, performance problems on mobile and low-end devices, unbalanced event economies, and monetization players dislike (which they punish with downvotes). Externally, Roblox's FOMO and scarcity mechanics (limited items, gacha, chance wheels, opaque Robux pricing) face growing 2025–26 regulatory, legal, and academic pressure. Weekly-update cadences are widely criticized as a burnout and shallow-content treadmill, and even Roblox's docs warn about team mental health.

### Cited Findings
**Churn drivers per official docs [OFFICIAL]**
- Lengthy tutorials make users leave for something more immediately engaging, and the audience is friction- and load-time-sensitive on mobile — [design-for-roblox.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/design-for-roblox.md)
- Without progression a game becomes "repetitive, boring, and shallow" — [core-loops.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/core-loops.md)
- Performance (crash rate, FPS) affects D1. Unbalanced difficulty causes frustration or content exhaustion (D7). Lacking an endgame hurts D30 — [retention.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/analytics/retention.md)
- Cadence content that is consumed instantly forces an ever-faster treadmill — [content-updates.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/content-updates.md)
- Event currency surpluses reduce later purchases and revenue — [balance-virtual-economies.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/balance-virtual-economies.md)
- Disliked monetization leads to downvotes — [monetization docs](https://create.roblox.com/docs/production/monetization.md)
- Inaccurate item descriptions are discouraged, and non-payers must be able to progress — [monetization-foundations.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/monetization-foundations.md)
- Since June 2026, **first-play bounce rate** is an explicit negative discovery signal, so a weak FTUE now directly cuts traffic — [Roblox newsroom (Optimizing Discovery)](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox); [allthings.how](https://allthings.how/robloxs-new-recommended-for-you-algorithm-rewards-games-that-keep-you-hooked/)

**Dark patterns and regulatory pressure [PRESS/ACADEMIC/ADVOCACY]**
- May 2026 complaint by advocacy groups (Anxious Generation Movement, ParentsSOS, Consumer Federation of America, EPIC). It targets **limited-quantity items that "manufacture urgency,"** loot boxes and chance wheels, and Robux layering that hides real prices from children. The allegations are not adjudicated, and sources differ on whether it went to the FTC — [Fortune](https://fortune.com/2026/05/20/exclusive-advocacy-groups-file-complaint-roblox-manipulative-design/)
- A University of Sydney study found **14 of 15** Roblox games tested used manipulative tricks to extract money. A Monash study found **58%** of participants reported seeing 10+ dark patterns in 12 months — [ACS Information Age](https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html)
- A CHI 2025 paper ("The System is Made to Inherently Push Child Gambling…") covers child safety, monetization, and moderation on Roblox — [ACM DL](https://dl.acm.org/doi/10.1145/3706598.3713170)
- Roblox's response: only **1.4% of 132M DAU were payers in Q1 2026**, and it has policies against real and simulated gambling **[OFFICIAL via PRESS]** — [ACS Information Age](https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html)
- Roblox made **paid random items unavailable to under-18s in the UK and to all players in Australia**. Reportedly 100+ lawsuits alleged addictive design as of early 2026 **[PRESS/advocacy aggregate; treat counts cautiously]** — [ACS Information Age](https://ia.acs.org.au/article/2026/roblox-sucking-up-money-from-young-players--study.html); [TechCrunch 2023 class action (older)](https://techcrunch.com/2023/08/18/roblox-children-gambling-class-action-lawsuit-robux/amp)
- Industry audit framing of "loot boxes, FOMO, fake scarcity" as dark patterns brands must audit **[COMMUNITY/consultancy]** — [NewGamePlus](https://newgameplus.group/en/article/loot-boxes-fomo-and-fake-scarcity-8-dark-patterns-brands-must-audit)

**Update-cadence burnout [OFFICIAL + COMMUNITY]**
- Official docs: "Prioritize mental health." Be realistic about how often updates can ship while maintaining work-life balance. Leave at least 1 week of rest between season-pass seasons. Keep cadence work under 3 weeks of effort — [liveops-essentials.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/liveops-essentials.md); [season-pass-design.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/season-pass-design.md); [content-updates.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/game-design/content-updates.md)
- An opinion piece (Jan 2026) argues Roblox developers "burn themselves out crunching to add new updates weekly." It says the author has seen many developer apology posts about burnout, and criticizes one- to two-week gacha-reward windows as favoring breadth over depth **[COMMUNITY opinion]** — [Slyther Games](https://www.slythergames.com/2026/01/09/i-wish-roblox-developers-focused-on-depth-over-constant-updates/)
- BIG Games abandoned weekly PS99 updates in early 2024 in favor of content-ready releases **[STUDIO, older]** — [BIG Games Update 4](https://www.biggames.io/post/pet-simulator-99-update-4)
- GAG2 reportedly replaced the weekly Admin Abuse cadence with smaller distributed drops and irregular Admin Parties **[COMMUNITY]** — [roonby](https://roonby.com/2026/07/03/does-grow-a-garden-2-have-admin-abuse-everything-we-know-so-far/)
- Speculative YouTube reports of a Grow a Garden developer leaving the dev list. No evidence it relates to burnout **[COMMUNITY, speculative]** — [YouTube](https://www.youtube.com/watch?v=TCiUc5vJAIs)

### Inferences
- Retention design on Roblox now carries regulatory risk. FOMO levers (countdown-limited items, chance-based paid items, opaque currency) still work, but are under scrutiny from advocates, academics, regulators (UK/AU paid-random-item restrictions), and plaintiffs. Safer substitutes include earnable event items with transparent odds, free-track season rewards, time-limited cosmetic-only exclusives, and catch-up mechanics (double-XP final week).
- The weekly-update treadmill trades team health and content depth for short-term CCU spikes. The 28-day retention algorithm may reward deeper progression and endgame systems more than constant novelty, but that is unproven.

### Gaps
- No quantitative churn-cause data (e.g., top uninstall/leave reasons) from Roblox or third parties was found.
- No primary interviews with Grow a Garden or Steal a Brainrot staff on workload or burnout were found.
- No Roblox policy text on time-limited items or FOMO beyond the paid-random-item restrictions was found.
