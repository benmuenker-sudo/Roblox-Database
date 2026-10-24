# Roblox Platform Mechanics for Creators 2025–2026: Discovery, Search, Thumbnails, Ads, Policies, Safety APIs

Research date: 2026-10-24. Method: WebSearch only. WebFetch failed with a DNS error (devforum.roblox.com) and the search budget ran out before every question was covered. All findings come from search-engine summaries of the cited pages, not from reading the full pages. Before relying on exact numbers, check the primary pages (DevForum, Creator Hub). Roblox changed several rules more than once during 2026; the dates below are the best reconstruction from the sources.

---

## 1. Discovery: Home "Recommended For You" (RFY), the June 2026 change, signals and weights

### Takeaway
On June 15, 2026 Roblox widened RFY ranking from a 7-day to a 28-day retention view. Signals are measured separately for Day 1, Days 2–7 and Days 8–28. Roblox removed qualified play-through rate (QPTR) and added play-through rate (PTR) and first-play bounce rate. Roblox published signal tiers ("most important" / "important") but, as far as the sources show, no numeric weights. The change cut short-term monetization enough that Roblox named it as a cause of weak Q2 2026 bookings and a negative Q3 guide.

### Cited Findings
- **Official change (June 15, 2026):** "we're expanding the Recommended For You algorithm from its previous 7-day view to a 28-day view that directly measures long-term retention. We're also sharing the full list of signals and their relative importance with creators." — [Roblox Newsroom: Optimizing Discovery (June 2026)](https://about.roblox.com/newsroom/2026/06/optimizing-discovery-great-games-reach-millions-players-roblox)
- **Signal buckets:** familiar signals extended from 7 to 28 days, measured separately for Day 1, Day 2–7 and Day 8–28. The signals are playtime, play days, qualified play sessions, intentional co-play days, spend days and Robux spent. — [DevForum: Recommended For You Algorithm Improvements That Better Value Long-Term Retention](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575)
- **Removed/added:** "removing QPTR and introducing PTR and first play bounce rates." — [DevForum 4684575](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575); summarized by [ZehnStudio26](https://zehn-studio26.com/news/recommended-for-you-retention-update/)
- **Official signal tiers (Creator Hub Discovery FAQ / Discovery doc):**
  - *Most important:* play-through rate (PTR, the rate at which users play a game after seeing it in the RFY sort), first-play bounce rate, play days per user, playtime per user. "There is no single signal that determines ranking."
  - *Important:* qualified play sessions per user, intentional co-play days, spend days, Robux spent per user.
  - Signals are computed only from users who organically joined from the RFY sort on Home.
  - A "qualified play" filters out accidental clicks and quick bounces.
  — [Creator Hub: Discovery FAQ](https://create.roblox.com/docs/discovery-faq); [Creator Hub: Discovery](https://create.roblox.com/docs/discovery)
- **First-play bounce** counts against a game: the rate at which players leave after a short first session. — [Dubit](https://dubit.io/library/what-makes-a-new-roblox-game-take-off) (secondary)
- **Per-user averages, not totals,** "ensures that smaller experiences with highly engaged users are not disadvantaged." — [DevForum: Boost Your Discovery with the Improved RFY Algorithm and Analytics (2025)](https://devforum.roblox.com/t/boost-your-discovery-with-the-improved-recommended-for-you-algorithm-and-analytics-for-creators/3587441)
- **History:** late 2024 tests of RFY improvements → 2025 version that ranks on engagement plus monetization (QPTR, D1/D7 retention, playtime, payer conversion) and tests return frequency, spend and friend interaction → the **intentional co-play** signal (users who manually join with friends via invites, party/sessions or private servers) → further tests in late 2025 and spring 2026 ("Testing More RFY Algorithm Signals") → June 2026 28-day launch. Public testing reportedly ran from about April 2026. — [DevForum: Testing Improvements to RFY (2024)](https://devforum.roblox.com/t/testing-improvements-to-the-%E2%80%9Crecommended-for-you%E2%80%9D-algorithms/3275201); [DevForum: [Tests] Continuing to improve RFY](https://devforum.roblox.com/t/tests-continuing-to-improve-the-%E2%80%98recommended-for-you%E2%80%99-algorithm/4067565); [DevForum: Testing More RFY Algorithm Signals](https://devforum.roblox.com/t/testing-more-recommended-for-you-algorithm-signals/4568033?page=4); [Lensblox](https://lensblox.com/blog/roblox-algorithm-change-2026-explained/) (secondary, for the April testing date)
- **August 2026 follow-up by Roblox's Chief Growth Officer (the surname "Ciancutti" appears in secondary coverage; full name not verified):** the post "Boost Your Discovery by Building Games People Want to Play" says benchmarks and benchmark games "do not impact the recommendation algorithm"; they are only comparison points in Creator Analytics. It lists the factors that change how many Home impressions a game gets, including the creator's own changes and Roblox's algorithm changes. Roblox is testing further updates that "better recognize long-term player value". Core line: "The most important thing is to build games people want to play, and keep playing." The date is stated as Aug 6 or Aug 20, 2026; the sources conflict. — [DevForum 4779042](https://devforum.roblox.com/t/boost-your-discovery-by-building-games-people-want-to-play/4779042); [ComicBook.com](https://comicbook.com/gaming/news/new-roblox-update-finally-targets-spam-slop-experiences-build-games-people-want/)
- **Business impact (Q2 2026, reported July 30, 2026):** bookings +8% to about $1.6B, at the low end of guidance; DAU 123M (+10%); hours 29B. Management attributed the shortfall partly to the RFY changes, which favor "highly retentive games at the expense of near-term monetization", with a larger-than-expected hit to younger cohorts (under-13 in US/Canada). Q3 bookings guide: $1.576–1.653B, a 14–18% YoY decline and the first guided drop. Stricter age checks and safety measures were also named as headwinds. — [Roblox Q2 2026 shareholder letter (SEC 8-K)](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm); [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-roblox-q2-2026-beats-eps-but-shares-sink-on-bookings-93CH-4826338); [BigGo Finance](https://finance.biggo.com/news/US_RBLX_2026-07-30)
- **Unverified claim:** a secondary blog says the change "cost the company $9B" in market value. Not confirmed elsewhere. — [Lensblox](https://lensblox.com/blog/roblox-algorithm-change-2026-explained/)
- **Developer pushback:** some developers report impressions collapsing (one: from 2–3k/hour to about 200) and call it a "chicken-and-egg" cold-start problem for new games, which cannot yet show 28-day data. — [DevForum 4779042](https://devforum.roblox.com/t/boost-your-discovery-by-building-games-people-want-to-play/4779042); [DevForum 4568033](https://devforum.roblox.com/t/testing-more-recommended-for-you-algorithm-signals/4568033?page=4) (anecdotal)
- **RDC 2026 (third-party):** Roblox reportedly plans to help strong games aimed at 18+ audiences gain visibility through the algorithm and through Roblox's own paid UA campaigns. — [MaxPowerGaming](https://www.maxpowergaming.co/post/rdc-2026-roblox-is-building-for-professionals-now); see also [games.gg](https://games.gg/news/roblox-algorithm-adult-games-retention/)

### Inferences
- The first touch (thumbnail/icon → PTR) and the first session (→ first-play bounce) are now the top-weighted levers. A strong FTUE in the first minutes matters directly for ranking, not only for retention.
- Monetization still counts as an "important" signal (spend days, Robux per user), but it is computed per user and over 28 days. Spend that recurs over many days probably helps more than one-off spikes. This is an inference; Roblox did not publish weights.
- New games face a structural delay: the full signal set needs about 4 weeks of organic RFY traffic. Ads (Plays/Engagement objectives) and friend/referral loops are the main ways to seed that traffic.

### Gaps
- No numeric weights per signal or per bucket (Day 1 / 2–7 / 8–28) were found. Secondary sources say the bucket weighting is "officially unanswered", which conflicts with the newsroom's "relative importance" wording. The official page may only give tiers.
- How cold start works for brand-new games under the 28-day window is unknown.
- The exact name and title of the August 2026 author could not be verified (the search summary gave only "Ciancutti").

---

## 2. Sorts/Charts, "Today's Picks", curated sorts, search ranking

### Takeaway
Home is personalized and dynamically ranked: "Continue", "People You May Know" and "Today's Picks" placement now depend on user engagement. Charts (roblox.com/charts) hold about 29 public sorts, such as Top Trending, Up-and-Coming, Top Playing Now and Top Revisited. Roblox has published no official documentation of search ranking; third-party sources describe keyword relevance plus engagement.

### Cited Findings
- **2025 Discovery Roadmap (March 2025):** Home is being made "more dynamic and personalized". After dynamic ranking for "People You May Know" and "Continue" launched in January 2025, Roblox planned dynamic placement for "Today's Picks" and a new "Recommended Paid Access Experiences" sort. It also promised an improved RFY focused on long-term retention and an upcoming Friend Referral System. — [DevForum: Roblox's 2025 Discovery Roadmap](https://devforum.roblox.com/t/roblox%E2%80%99s-2025-discovery-roadmap-and-ways-to-reach-and-engage-your-audience/3557533); [Tubefilter](https://www.tubefilter.com/2025/03/20/roblox-discovery-roadmap-2025/)
- **Today's Picks** placement "now depends on users' engagement patterns" (personalized Home and Search initiative). — [DevForum: Building the Future of Roblox Home and Search: Introducing Personalized Discovery](https://devforum.roblox.com/t/building-the-future-of-roblox-home-and-search-introducing-personalized-discovery/3432124)
- **Charts:** about 29 sorts, including Top Trending, Up-and-Coming, Top Playing Now and Top Revisited (fan wiki). The official charts page shows Top Trending and Up-and-Coming lists with rating % and player counts but does not explain ranking. — [Roblox Charts](https://www.roblox.com/charts); [Roblox Fandom: Charts](https://roblox.fandom.com/wiki/Charts)
- **Trending Events in Experiences chart:** ranks active events by the experience's DAU. To qualify, an event must have started within the last 7 days and have at least 1,000 RSVPs. — [Creator Hub: Experience events and updates](https://create.roblox.com/docs/production/promotion/experience-events)
- **"Relevant information" tests (2025):** tests showing more relevant information on game tiles/details to improve discovery. Curated editorial lists such as "Best Horror Games" appeared in the thread only as a community suggestion. — [DevForum: [Upcoming Tests] Improving Game Discovery With Relevant Information](https://devforum.roblox.com/t/upcoming-tests-improving-game-discovery-with-relevant-information/3907203)
- **Creator Roadmap 2026 Fall Update (post-RDC 2026):**
  - Shipped: "better discovery recommendations" and an improved "Continue Playing" feed.
  - Planned for late 2026: show passes and developer products on Home and other discovery surfaces before players enter a game; free session-long trials of passes; dynamic filters (moved from "Ongoing" to "Late 2026"); a "deceptive game copy takedown" feature aimed at games that imitate another title or thumbnail.
  — [DevForum: Creator Roadmap 2026: Fall Update](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208); [Creator Roadmap](https://create.roblox.com/roadmap)
- **Search (third-party only):** Lensblox describes search as a system separate from RFY, "driven primarily by keyword relevance". Inputs it lists: keyword match (title, description, genre tags), engagement (CCU, playtime, retention), recency of updates and, increasingly, semantic relevance. — [Lensblox: Roblox SEO guide](https://lensblox.com/blog/roblox-seo-guide/); [rolearn.dev](https://rolearn.dev/insights/roblox-game-discovery-algorithm-2026/) (both unofficial)
- **Restricted content in search:** users under 18 no longer see search results or recommendations for experiences labeled 'Restricted'. — [DevForum: Updating Age Requirements for Experiences with 'Restricted' Content Maturity Label](https://devforum.roblox.com/t/updating-age-requirements-for-experiences-with-%E2%80%98restricted%E2%80%99-content-maturity-label/3905863)
- **Age-gated audience reach (2026)** limits which surfaces a new game appears on for under-16 users (see Section 6). — [Creator Hub: Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)

### Inferences
- Charts (Top Trending, Up-and-Coming) seem to reward short-term growth velocity, while RFY rewards 28-day retention. Third-party sources say a viral spike can still win Charts traffic even when RFY prefers retentive games.
- Search optimization is mostly about metadata hygiene (title, description, genre) and is a minor channel next to Home. This rests on unofficial sources.

### Gaps
- No official Roblox documentation on search ranking was found.
- It is unclear whether a manually curated sort or "Today's Picks" editorial selection still exists. The sources describe Today's Picks as engagement-driven, not as manual curation.
- No 2026 discovery roadmap separate from the Creator Roadmap was found.

---

## 3. Thumbnails, thumbnail personalization/testing, icon testing

### Takeaway
Thumbnail personalization went live in late 2024. Creators set up to 5 active thumbnails; with 2 or more active, a multi-armed bandit shifts impressions hourly per user group, originally toward the highest QPTR. There is no native icon A/B testing as of mid-2026; the workaround is to test the icon's motif as a thumbnail.

### Cited Findings
- **Test phase:** a small-scale experiment starting July 8, 2024 on 5% of traffic. — [DevForum: Testing Personalized Thumbnails in Home this July](https://devforum.roblox.com/t/testing-personalized-thumbnails-in-home-this-july/3039419)
- **Live:** "you can upload new thumbnails and then set up to 5 thumbnails as 'active.' When you set 2 or more thumbnails to active, personalization will turn on." The system uses a multi-armed bandit "instead of A/B testing to help you find multiple winning thumbnails in hours". Traffic starts evenly split; "thumbnails with higher qualified play through rates (qPTR) for specific user groups will automatically receive more traffic from that group." Per-thumbnail stats (impressions, qualified plays, play-through rate) appear in Creator Hub after a few hours. — [DevForum: [Live now] Personalize your thumbnails](https://devforum.roblox.com/t/live-now-personalize-your-thumbnails-to-attract-more-users/3257233); [GamesBeat](https://gamesbeat.com/roblox-will-let-game-devs-personalize-thumbnails-to-attract-more-players/); [Creator Hub: Thumbnails](https://create.roblox.com/docs/production/publishing/thumbnails)
- **Flag:** RFY dropped QPTR for PTR in June 2026. Whether the thumbnail bandit's optimization target also moved to PTR was not confirmed. — inference from [DevForum 4684575](https://devforum.roblox.com/t/recommended-for-you-algorithm-improvements-that-better-value-long-term-retention/4684575)
- **Icon & thumbnail translation experiment (2024):** Roblox ran an experiment on localized (translated) icons and thumbnails. — [DevForum: Upcoming Icon & Thumbnail Translation Experiment](https://devforum.roblox.com/t/upcoming-icon-thumbnail-translation-experiment/3105942)
- **No icon A/B testing:** an older DevForum answer said icon testing was not possible. A third-party guide says that as of May 2026 Creator Hub still has no native icon A/B testing. Feature requests remain open for icon/title testing and for testing titles together with thumbnails. — [DevForum: Are you able to A/B test game icons](https://devforum.roblox.com/t/are-you-able-to-ab-test-game-icons/3339468); [CreatorXP](https://creatorxp.gg/guides/roblox-game-icon-mistakes) (secondary); [DevForum feature request: A/B Testing Titles With Thumbnails](https://devforum.roblox.com/t/ab-testing-experience-titles-together-with-thumbnails/4900092); [DevForum: Add A/B Testing and Stats for Titles & Icons](https://devforum.roblox.com/t/add-ab-testing-and-stats-for-titles-icons/4778726)
- **Copy/clone enforcement:** a "deceptive game copy takedown" for games that imitate another title or thumbnail is on the roadmap for late 2026. — [Creator Roadmap 2026 Fall Update](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208)

### Inferences
- PTR is now the top RFY signal, so the thumbnail and icon are probably the cheapest high-impact levers. The bandit should be used constantly, with 3–5 active variants.
- Misleading thumbnails may raise PTR but also raise first-play bounce, which is now an explicit negative signal. That gives a built-in penalty for clickbait.

### Gaps
- No confirmation of a 2025–2026 change to the 5-thumbnail cap or to the bandit's target metric.
- No official native icon testing was found.

---

## 4. Experience Events, notifications, friend-based discovery

### Takeaway
Roblox offers several first-party re-engagement and social channels:
- Experience Events with RSVP, a "Notify Me" button, SocialService APIs, an Open Cloud API and a Trending Events chart.
- Experience Notifications via Open Cloud, delivered to opted-in users aged 13+.
- Invite prompts.
- A Friend Referral System, launched in 2025.
Intentional co-play is also an explicit RFY signal.

### Cited Findings
- **Experience Events:**
  - Events appear in a dedicated section on the experience details page, with a "Join Event" button (active events) and "Notify Me" (upcoming events).
  - Trending Events chart: the event started within 7 days and has at least 1,000 RSVPs, ranked by DAU.
  — [Creator Hub: Experience events and updates](https://create.roblox.com/docs/production/promotion/experience-events)
- **Event discovery tests:** in 2024–2025 Roblox tested surfacing events more prominently on the Experience Details page, the "first of several improvements" for event discovery. — [DevForum: Upcoming Experience Events Discovery Tests](https://devforum.roblox.com/t/upcoming-experience-events-discovery-tests/3146504)
- **Event APIs (mid-2025 and later):**
  - SocialService methods to read a player's RSVP status and prompt a change (with the option to follow the event).
  - Later additions: `GetUpcomingExperienceEventsAsync()` and `GetExperienceEventAsync()`.
  - An Open Cloud "Game Events" API, marked experimental.
  — [DevForum: Introducing the New Experience Event APIs](https://devforum.roblox.com/t/introducing-the-new-experience-event-apis/3754058); [DevForum: Automate your Event RSVP invites (SocialService)](https://devforum.roblox.com/t/automate-your-event-rsvp-invites-new-ways-to-get-event-information-from-the-socialservice-api/4034921); [Creator Hub: SocialService](https://create.roblox.com/docs/reference/engine/classes/SocialService); [Open Cloud: Game Events](https://create.roblox.com/docs/cloud/reference/features/virtual-events)
- **Experience Notifications:**
  - Sent from server-side scripts or Open Cloud.
  - Delivered to opted-in users aged 13+ through their Roblox notification stream.
  - Eligibility: at least 100 visits since launch, no moderation hold, management permission on the game.
  - Per-recipient text uses parameters in the notification string.
  - Developers complain that notifications are passive and do not push like friend invites (May 2025 thread).
  — [Creator Hub: Experience notifications](https://create.roblox.com/docs/production/promotion/experience-notifications); [Creator Hub: User notifications (Open Cloud)](https://create.roblox.com/docs/cloud/guides/experience-notifications); [DevForum: Introducing Experience Notifications](https://devforum.roblox.com/t/introducing-experience-notifications/2826474?page=7)
- **Invite prompts:** `SocialService:PromptGameInvite` with `ExperienceInviteOptions` (custom prompt message, target user, launch data). Since a redesign, online and closest friends appear at the top instead of alphabetical order. — [Creator Hub: Player invite prompts](https://create.roblox.com/docs/production/promotion/invite-prompts); [DevForum: Updates to Invites](https://devforum.roblox.com/t/updates-to-invites-joining-friends-just-got-easier/2729692)
- **GetFriendsOnline change (2025):** it returns only friends whose online status the experience creator can see. Roblox recommends moving referral systems to `PromptGameInvite`. — [DevForum: Upcoming Changes to the GetFriendsOnline API](https://devforum.roblox.com/t/upcoming-changes-to-the-getfriendsonline-api/3632813)
- **Friend Referral System (launched 2025):** lets developers reward referrers. Designed for public servers; referral tracking is per server. — [DevForum: Announcing the new Friend Referral System](https://devforum.roblox.com/t/announcing-the-new-friend-referral-system-for-your-experiences/3623795?page=2)
- **Intentional co-play** (manually joining friends via invites, sessions or private servers) is an RFY "important" signal. — [Creator Hub: Discovery FAQ](https://create.roblox.com/docs/discovery-faq)
- **Chat-group-aware matchmaking:** `TextChatService:GetChatGroupsAsync` (Feb 2026) groups and teleports players who can chat with each other. See Section 8. — [DevForum: New Chat APIs: Teleport Users Who Can Chat Together](https://devforum.roblox.com/t/new-chat-apis-teleport-users-who-can-chat-together/4337233)

### Inferences
- Since January 2026, age-check-gated chat separates adults from younger teens by default. Friend loops in mixed-age games may weaken for players without an age check. Co-play among friends (Trusted Connections) becomes more valuable.

### Gaps
- No official 2026 changes to notification throttling or the notification cap were found.
- No official "Friends are playing" sort mechanics were found.

---

## 5. Paid acquisition: Ads Manager, Sponsored, CPP/CPM, Rewarded Video

### Takeaway
Ads Manager is the single buying tool. Sponsored Experiences moved into it in 2023. Objectives include Plays, Earnings (ROAS-optimized, available to about 30k games by October 2026) and Engagement (beta, which buys players who count toward the Kids/Select "Highly Engaged Player" threshold). Rewarded Video Ads opened to all ads-eligible creators in February 2026; creators earn EPM × impressions. Roblox claims sharply lower cost per play but publishes no official CPP/CPM rate card.

### Cited Findings
- **Sponsored → Ads Manager:** [DevForum: Sponsored Experiences moving to Ads Manager](https://devforum.roblox.com/t/sponsored-experiences-moving-to-ads-manager/2661756)
- **Play definition:** a user clicks a sponsored experience, lands on the experience details page and enters the experience within 1 hour. — [ppc.land](https://ppc.land/robloxs-ad-platform-hits-90-completion-rates-as-age-checks-unlock-adult-audience-data/) (secondary)
- **CPP reductions:** Roblox says cost per play is "now over 71% cheaper" (RDC 2025 recap context). A later report cites a ">40% reduction in cost-per-play versus Q1 2025". — [DevForum: Ads for Creators: RDC Recap and What's Next (Sept 2025)](https://devforum.roblox.com/t/ads-for-creators-rdc-recap-and-what%E2%80%99s-next/3929106); [ppc.land](https://ppc.land/robloxs-ad-platform-hits-90-completion-rates-as-age-checks-unlock-adult-audience-data/)
- **Creator-reported costs:** one developer paid about $8 per 1,000 plays on "Maximize Plays" and considered it expensive (anecdotal). — [DevForum 3929106 p.2](https://devforum.roblox.com/t/ads-for-creators-rdc-recap-and-what%E2%80%99s-next/3929106?page=2)
- **Ads Manager features (2025):** [DevForum: Leveling Up Ads Manager With New Features](https://devforum.roblox.com/t/leveling-up-ads-manager-with-new-features/3587640)
- **2026 updates:**
  - "Maximize Earnings" objective, attribution updates, new tile format in beta. — [DevForum: Ads Manager Updates – Maximize Earnings, Attribution Updates, New Tile in Beta](https://devforum.roblox.com/t/ads-manager-updates-maximize-earnings-attribution-updates-new-tile-in-beta-other-updates/4623762)
  - New Advertising Policies & Standards. — [DevForum: New Advertising Policies & Standards](https://devforum.roblox.com/t/new-advertising-policies-standards/4527365)
- **RDC 2026 Ads recap (about Oct 2026):**
  - Unified Attribution (launched May 2026). All 21 incrementality-study campaigns produced incremental plays: median +14% incremental play sessions and median +10% D7-retained users for exposed versus unexposed users. Studies are only available for "Plays"-objective campaigns.
  - The Earnings objective is available to nearly 30,000 games, with ROAS as the success metric.
  - Reporting filters for new, returning and lapsed users.
  — [DevForum: Ads Manager RDC Recap: Earnings, ROAS Reporting, & Incrementality](https://devforum.roblox.com/t/ads-manager-rdc-recap-earnings-roas-reporting-incrementality/4909790); [DevForum Weekly Recap Sep 28–Oct 2, 2026](https://devforum.roblox.com/t/weekly-recap-september-28%E2%80%93october-2-2026/4910267)
- **Engagement objective (beta, June 2026):** prioritizes players whose sessions count toward the Highly Engaged Player threshold for Kids/Select eligibility. — [DevForum: Roblox Kids and Select Global Launch: Upcoming Updates to Eligibility, Ads Manager, and Expedited Review](https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717)
- **Rewarded Video for creators (earning side):**
  - 2025: limited to experiences averaging 100K+ DAU over 28 days, with Minimal/Mild maturity and good standing. Roblox then said it would open to all creators meeting Advertising Standards and Community Standards regardless of maturity rating.
  - Feb 18, 2026: "Rewarded Video ads are now available to all ads eligible creators."
  - Earnings = EPM (earnings per 1,000 impressions) × impressions. Higher-completion and Minimal-maturity experiences likely see higher EPM because advertiser demand is higher.
  - Earnings forecaster under Creator Hub > Monetization > Ads; an option to reduce ads for likely payers.
  - May 2026: "Join with Reward" placement added.
  — [DevForum: More Creators Can Now Use Rewarded Video Ads](https://devforum.roblox.com/t/more-creators-can-now-use-rewarded-video-ads/3838678); [DevForum: Rewarded Video ads are now available to all ads eligible creators](https://devforum.roblox.com/t/rewarded-video-ads-are-now-available-to-all-ads-eligible-creators/4063278); [DevForum: Boost your game earnings with Rewarded Video enhancements](https://devforum.roblox.com/t/boost-your-game-earnings-with-rewarded-video-enhancements/4645335)
- **Ad revenue scale:** Roblox's Q4 2025 shareholder letter calls advertising revenue "modest" and says expanding Rewarded Video supply will take time to scale. — [Roblox Q4 2025 shareholder letter (SEC)](https://www.sec.gov/Archives/edgar/data/1315098/000131509826000009/ex991-q42025shareholder.htm)
- **Third-party CPM/eCPM estimates (unverified):** rewarded video CPM "$5–$15" ([rolearn.dev](https://rolearn.dev/insights/rewarded-video-ads-new-revenue-stream/)); creator eCPM "$6–12" (same site). Some guides say advertisers can buy rewarded video via Google Ad Manager ([Gupta Media](https://www.guptamedia.com/insights/roblox-advertising)). Treat all of these with caution.
- **Age checks and adult targeting:** age checks reportedly unlock adult audience data for advertisers; video completion rates are above 90%. — [ppc.land](https://ppc.land/robloxs-ad-platform-hits-90-completion-rates-as-age-checks-unlock-adult-audience-data/) (secondary)

### Inferences
- For new games after May 2026, paid UA has a second job beyond plays: buying "highly engaged" age-checked 16+ sessions to unlock the under-16 audience (Engagement objective). The alternative is the Expedited Review fee.
- Incrementality data (+14% sessions, +10% D7 retained) suggests ads also feed RFY signals. But RFY signals count only organic RFY joins, so ads help indirectly at best.

### Gaps
- No official CPP, CPM or EPM rate card was found. Current cost per play varies by objective, audience and age band and can only be seen in the Ads Manager dashboard.
- The exact 2026 Rewarded Video eligibility criteria (minimum DAU, maturity) after the February expansion were cut off in the search snippets.

---

## 6. Policies: age checks, maturity labels, unrated experiences, publishing requirements, Kids/Select

### Takeaway
2025–2026 brought a cascade of age gating:
1. Labels (Maturity & Compliance Questionnaire) became mandatory. Unrated experiences became unplayable after September 30, 2025.
2. "Restricted" moved from 17+ ID-verified to 18+ age-checked.
3. Age checks for chat went global in January 2026 (six age bands).
4. Publishing eligibility tightened in December 2025, then was replaced in May 2026 by a tiered system: 16+ by default, plus an evaluation period before a game reaches under-16 users.
5. Roblox Kids (5–8) and Roblox Select (9–15) accounts launched globally in June 2026 with separate catalogs.

### Cited Findings
**Maturity labels and questionnaire**
- **Labels:** Minimal, Mild, Moderate, Restricted.
  - Minimal/Mild → eligible for Roblox Kids (5–8) and Roblox Select (9–15).
  - Moderate → Roblox Select (9–15) and standard Roblox (16+). The publishing post calls it "Moderate (9+)".
  - Restricted → "only accessible to age-verified Roblox users 18 and older."
  - Without accurate and complete maturity information, Roblox restricts playability for all players.
  — [Creator Hub: Content maturity and compliance](https://create.roblox.com/docs/production/promotion/content-maturity); [Creator Hub: Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)
- **Restricted moves from 17+ to 18+ (2025):** the older rule was ID-verified 17+. The 2025 announcement says under-18 users lose search results and recommendations for Restricted experiences, access is later fully blocked for under-18 users, and creators of new Restricted experiences must be 18+. — [DevForum: Updating Age Requirements for Experiences with 'Restricted' Content Maturity Label](https://devforum.roblox.com/t/updating-age-requirements-for-experiences-with-%E2%80%98restricted%E2%80%99-content-maturity-label/3905863); older wording in the [ESRB blog](https://www.esrb.org/blog/what-parents-need-to-know-about-roblox-2/)
- **Questionnaire updates (2025):** [DevForum: Updates to Our Maturity & Compliance Questionnaire](https://devforum.roblox.com/t/updates-to-our-maturity-compliance-questionnaire/3860056)
- **Unrated experiences:**
  - Creators had to complete the Maturity & Compliance Questionnaire by **September 30, 2025**. Unrated experiences then became unplayable but stayed editable and testable in Studio. Completing the questionnaire restores access at any time.
  - Moderators check answers. A rejected questionnaire removes the label and makes the experience unplayable until it is retaken.
  — [DevForum: Important Updates: Unrated Experiences and Changes to Experience Pages](https://devforum.roblox.com/t/important-updates-unrated-experiences-and-changes-to-experience-pages/3899317); [GameRant](https://gamerant.com/new-roblox-rating-system-unrated-games-disabled-on-september-30/); [DevForum: Experience moderated/inaccessible for inaccurate maturity rating](https://devforum.roblox.com/t/experience-moderatedinaccessible-for-inaccurate-maturity-rating/4815099)
- **Earlier (Nov 2024):** under-13 users were blocked from unrated experiences, social hangouts and experiences with free-form 2D user creation. — [DevForum: Updating Experience Guideline Policies to Keep Our Younger Users Safe](https://devforum.roblox.com/t/updating-experience-guideline-policies-to-keep-our-younger-users-safe/3249079); [TechCrunch (Nov 2024)](https://techcrunch.com/2024/11/07/roblox-adds-new-safety-measures-to-ban-kids-under-13-from-social-spaces)
- **Social hangouts and adult settings (Aug 2025):**
  - Social Hangouts with private spaces (bedrooms, bathrooms) and experiences set mainly in private spaces or adult venues (bars, clubs) are limited to ID-verified 17+ users. They are not playable, not shown in top charts and not recommended to other users. They are not banned outright.
  - Sexual activity and seeking real-world romance are prohibited everywhere. 17+ experiences may contain non-sexual affection and romantic themes (2024 FAQ).
  - Flag: given the Restricted change to 18+, this 17+ threshold may since have moved to 18+. Not verified.
  — [Roblox Newsroom: Clarifying Our Policy on Romantic and Sexual Content (Aug 2025)](https://about.roblox.com/newsroom/2025/08/extending-roblox-policy-on-romantic-and-sexual-content); [DevForum: Strengthening Our Safety Policies and Tools](https://devforum.roblox.com/t/strengthening-our-safety-policies-and-tools/3882864); [DevForum: Upcoming Changes to Experience Guidelines (2024)](https://devforum.roblox.com/t/upcoming-changes-to-experience-guidelines/3070343)

**Age checks for chat**
- **Rollout:** announced November 2025. Enforced from the first week of December 2025 in Australia, New Zealand and the Netherlands, then globally (wherever chat is available) in early January 2026. Facial Age Estimation runs through the vendor Persona; images and video are deleted right after processing. ID verification (13+) and parental verification are alternatives. — [Roblox Newsroom: Roblox Requires Age Checks for Communication (Nov 2025)](https://about.roblox.com/newsroom/2025/11/roblox-requires-age-checks-limits-minor-and-adult-chat); [Roblox IR: Expands Facial Age Checks](https://ir.roblox.com/news/news-details/2025/Roblox-Expands-Facial-Age-Checks-for-Communication-Setting-New-Safety-Standard/default.aspx); [Roblox Newsroom: Safety Snapshot December 2025](https://about.roblox.com/newsroom/2025/12/safety-snapshot-age-checks-for-chat); [TechCrunch](https://techcrunch.com/2025/11/18/roblox-will-require-all-users-to-perform-age-checks-to-access-chat-from-january); [BiometricUpdate (Jan 2026)](https://www.biometricupdate.com/202601/roblox-rolls-out-facial-age-estimation-for-chat-access-globally)
- **Age bands:** under 9, 9–12, 13–15, 16–17, 18–20, 21+. Users chat within their own band and adjacent bands (example: a 12-year-old in 9–12 can chat with users aged 15 and younger). Adults and younger teens are separated by default; Trusted Connections are the exception. — [allthings.how](https://allthings.how/robloxs-new-chat-rules-explained-january-2026/); [Roblox Newsroom (Nov 2025)](https://about.roblox.com/newsroom/2025/11/roblox-requires-age-checks-limits-minor-and-adult-chat). One source lists the bands slightly differently (18–21); likely an error.
- **Developer follow-ups:**
  - [DevForum: Age Check Requirement to Chat Now Live Globally](https://devforum.roblox.com/t/age-check-requirement-to-chat-now-live-globally/4226101/print)
  - [DevForum: Age Check to Chat Update & Fast Follow Roadmap](https://devforum.roblox.com/t/age-check-to-chat-update-fast-follow-roadmap/4238626)
  - [DevForum: Age Check Notifications in Studio and Creator Hub](https://devforum.roblox.com/t/age-check-notifications-in-studio-and-creator-hub/4117693): age checks will also be required for Team Create.

**Publishing requirements (sequence)**
- **Dec 17, 2025** ("New Requirements to Publish and Update Public Experiences"). To publish or update public experiences, a creator needed one of:
  - completed ID verification;
  - a real-money or gift-card purchase since Jan 1, 2025;
  - edit access to an experience with 100+ playtime hours in a set window;
  - a DevEx request in the prior 12 months.
  A content maturity label was also required.
  — [DevForum 4143953](https://devforum.roblox.com/t/new-requirements-to-publish-and-update-public-experiences/4143953)
- **April 17, 2026, updated May 11, 2026, effective May 19, 2026** ("New Publishing Requirements & Evaluation Process for Games"). Three parts:
  1. **Creator eligibility.** For 16+ and Trusted Friends: an age check, good standing and an account at least 2 days old. For all ages: additionally ID verification, 2-step verification and Roblox Plus or Premium (or a one-time fee). Eligibility is rechecked at every publish.
  2. **Automated safety screening**, including the Maturity & Compliance Questionnaire (Minimal, Mild or Moderate rating).
  3. **Evaluation period.** The game is first shown only to age-checked users 16 and older. Roblox screens engagement for real users using account age, play history and spend.
  — [DevForum: New Publishing Requirements & Evaluation Process for Games](https://devforum.roblox.com/t/new-publishing-requirements-evaluation-process-for-games/4573166); [DevForum: [AMA] Publishing Requirements + Roblox Kids & Select](https://devforum.roblox.com/t/ama-publishing-requirements-roblox-kids-select/4580953); [RTC on X (Apr 2026)](https://x.com/Roblox_RTC/status/2043713212000985149)
- **Alternative to the subscription:** a one-time **1,000 Robux** fee per game, refunded 3 months after the game becomes eligible if it is still in good standing. Alternatively, 2 consecutive months of Roblox Plus or Premium. Some accounts received a free 6-month Plus. — [DevForum: Alternate Publishing Requirements for Roblox Kids and Select](https://devforum.roblox.com/t/alternate-publishing-requirements-for-roblox-kids-and-select/4630944); [Roblox Help: How to Publish Games on Roblox](https://en.help.roblox.com/hc/en-us/articles/203313890-How-to-Publish-Games-on-Roblox)
- **Highly-engaged threshold for under-16 reach (conflicting, changed):**
  - May 2026 launch: 500 unique age-checked 16+ players (social posts say "in the past 30 days"; other sources say 60 days). — [KreekCraft on X](https://x.com/KreekCraft/status/2056775261899649503?lang=en); [AMA](https://devforum.roblox.com/t/ama-publishing-requirements-roblox-kids-select/4580953)
  - Current official wording: "250 unique plays by highly engaged, age-checked users (16+) within a 60-day window." Progress is tracked in the Audience Reach dashboard. GEEIQ says the cut from 500 to 250 happened on Aug 19, 2026 (not verified officially). — [Roblox Help](https://en.help.roblox.com/hc/en-us/articles/203313890-How-to-Publish-Games-on-Roblox); [Creator Hub: Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select); [GEEIQ (Sept 3, 2026)](https://geeiq.com/resources/blog/roblox-evaluation-changes-brands)
- **Expedited Review (to bypass the engagement threshold):** a refundable fee, with review in up to 48 hours. Refundable after 90 days in good standing; no refund if the game is permanently moderated. Fee conflict: 100,000 Robux (June 2026 announcement / RTC) versus **50,000 Robux** (current Creator Hub and Help page). — [DevForum 4685717](https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717); [RTC on X](https://x.com/Roblox_RTC/status/2066971588143259786?lang=en); [Creator Hub: Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)
- **Creator verification on the Kids/Select page:** facial age estimation for creators under 18, government ID for creators 18+, and 2-step verification. A September 11, 2026 RTC post says creators under 18 no longer need an ID check to publish for younger audiences (an age check is still required). — [Creator Hub: Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select); [RTC on X (Sept 2026)](https://x.com/Roblox_RTC/status/2098520734536712672); [Creator Hub: Account verification](https://create.roblox.com/docs/production/publishing/account-verification)
- **Already-published games:** they do not need to keep age-check status or an active Plus subscription to stay available (AMA). — [AMA p.16](https://devforum.roblox.com/t/ama-publishing-requirements-roblox-kids-select/4580953?page=16)
- **Fall 2026 roadmap:** "relaxed Kids & Select requirements", with lower engagement and review requirements. — [Creator Roadmap 2026 Fall Update](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208)

**Roblox Kids / Roblox Select accounts**
- **Announcement (Apr 13, 2026):** Roblox Kids (ages 5–8, "under 9") and Roblox Select (9–15, with regional variation). Users move to a standard account at 16. Only games that passed Roblox's three-step screening appear in these catalogs. Games with sensitive issues, social hangouts or free-form drawing are excluded by default (secondary source). — [Roblox IR: New Age-Based Accounts](https://ir.roblox.com/news/news-details/2026/Roblox-Introduces-New-Age-Based-Accounts-and-Expanded-Parental-Controls-for-Users-Under-16/default.aspx); [TechCrunch (Apr 13, 2026)](https://techcrunch.com/2026/04/13/roblox-introduces-kids-and-select-accounts-for-age-appropriate-access-to-games-and-chat/); [Bloxy News guide](https://www.bloxy.news/post/roblox-kids-chat-restrictions-publishing-requirements)
- **Global launch (June 2026):** started after four initial regions; "tens of thousands of games" are in the Kids/Select catalogs. — [DevForum 4685717](https://devforum.roblox.com/t/roblox-kids-and-select-global-launch-upcoming-updates-to-eligibility-ads-manager-and-expedited-review/4685717)

### Inferences
- Since May 19, 2026, every new game starts as a 16+ game. Reaching the large under-16 audience needs creator verification plus a fee or subscription, plus 250 highly engaged 16+ plays (or Expedited Review). Early tests with friends and ads aimed at age-checked 16+ users are now a launch prerequisite for kid-focused games.
- The rating is a discovery lever: Moderate keeps Select (9–15) but drops Kids (5–8); Restricted drops all under-18 search and recommendations.

### Gaps
- Exact current numbers can change monthly. The engagement threshold (250 vs 500; 30 vs 60 days) and the Expedited Review fee (50k vs 100k Robux) conflict across sources; the official pages say 250 / 60 days / 50k as of the latest snapshots.
- Whether the August 2025 17+ thresholds for social hangouts were raised to 18+ was not verified.

---

## 7. Policies: paid random items (loot boxes), monetization toward minors, off-platform links, AI content, IP/DMCA, Terms changes

### Takeaway
- **Paid random items:** creators must gate them with `PolicyService:GetPolicyInfoForPlayerAsync().ArePaidRandomItemsRestricted` and offer a compliant alternative. Since a May 26, 2026 clarification, numeric odds (percentages summing to 100%) must be shown before purchase, including for items bought with Robux-purchased in-game currency. Regulated markets named: Australia, Belgium, Netherlands, United Kingdom, Brazil.
- **Off-platform links:** must go through PolicyService. Users under 13 cannot see links.
- **AI outputs:** count as UGC under the April 2026 Terms; the creator is responsible.
- **IP:** handled through Rights Manager.
- **Terms:** new Terms of Use took effect April 30, 2026 and November 1, 2026.

### Cited Findings
**Paid random items**
- **Community Standards:** creators offering paid random items must use the `ArePaidRandomItemsRestricted` attribute of PolicyService so only eligible users can access them. Paid random items are Robux purchases (or purchases with Robux-bought in-game currency) with a random outcome at developer-set odds. Real or simulated gambling is prohibited. — [Roblox Community Standards](https://about.roblox.com/community-standards)
- **"Clarifying Requirements for Paid Random Items" (live May 26, 2026 per a secondary source):**
  - The definition covers direct Robux purchases and indirect ones via in-game currencies bought with Robux.
  - Numeric odds for every possible outcome must be shown before purchase, as percentages summing to exactly 100%.
  - A long list may sit behind a clickable pop-up, but a bare (i) icon is not enough; it needs a label such as "Info" or "Details".
  - Odds modifiers (luck boosts) must show their effect numerically.
  - Every outcome must give some benefit.
  - Ineligible users must get a compliant alternative.
  - Test regulated markets (AU, BE, NL, UK, BR) in Studio's Player Emulator.
  — [DevForum 4654622](https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622); [Creator Hub: Paid random items policy guidelines](https://create.roblox.com/docs/production/monetization/paid-random-items); [ZehnStudio26](https://zehn-studio26.com/news/paid-random-items-odds-disclosure/)
- **Korea as driver (unconfirmed officially):** the global odds-disclosure rule was reportedly driven by South Korea's loot-box law. — [TechTimes (June 26, 2026)](https://www.techtimes.com/articles/319148/20260626/koreas-loot-box-rules-push-roblox-disclose-item-odds-worldwide.htm)
- **Regional restrictions history:**
  - UK under-18 restriction. — [DevForum: Update on Paid Random Items Restriction for UK Users Under 18](https://devforum.roblox.com/t/update-on-paid-random-items-restriction-for-uk-users-under-18/3072183)
  - Australia. — [DevForum: Update on Paid Random Items Restriction for Australian Users](https://devforum.roblox.com/t/update-on-paid-random-items-restriction-for-australian-users/3153602)
  - Brazil: under-18 users barred (`ArePaidRandomItemsRestricted` returns True). A further restriction from March 31 applies to Brazilian adults 18+ without an age check. — Roblox DevForum announcement as summarized in search results; see [DevForum 4654622](https://devforum.roblox.com/t/clarifying-requirements-for-paid-random-items/4654622)
  - Original 2019 guidelines: [DevForum: Guidelines around users paying for random virtual items](https://devforum.roblox.com/t/guidelines-around-users-paying-for-random-virtual-items/307189)

**Monetization toward minors (context)**
- **Research:** University of Sydney (2026) found misleading purchase design in 14 of 15 popular experiences.
- **FTC complaint:** filed by Fairplay and NCOSE in May 2026.
- **Litigation:** a Texas Deceptive Trade Practices Act claim is proceeding; settlements with Alabama, Nevada and West Virginia were reached in April 2026 (10-Q).
- **Roblox's response:** only 1.4% of 132M DAU were payers in Q1 2026.
— [University of Sydney report (PDF)](https://ses.library.usyd.edu.au/bitstream/handle/2123/35033/Misleading%20and%20Deceptive%20Monetisation%20in%20Roblox%20-%20Final.pdf?sequence=3&isAllowed=y); [Fortune (May 20, 2026)](https://fortune.com/2026/05/20/exclusive-advocacy-groups-file-complaint-roblox-manipulative-design/); [Roblox 10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051082/rblx-20260630.htm)
- **Pre-entry storefront (roadmap, late 2026):** passes and developer products shown on Home and discovery surfaces before players enter a game, plus free session-long pass trials. — [Creator Roadmap 2026 Fall Update](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208)

**Off-platform links**
- **Under-13 rule:** "For their privacy and safety, we don't permit users under 13 to share links." — [Roblox Privacy and Cookie Policy (Help)](https://en.help.roblox.com/hc/en-us/articles/115004630823-Roblox-Privacy-and-Cookie-Policy)
- **In-experience links:** allowed only when wrapped in a PolicyService check. Links where the check cannot apply, such as text chat, are prohibited (community interpretation of the rules). — [DevForum: Discord (or social) links in game](https://devforum.roblox.com/t/discord-or-social-links-in-game-policyservice/3139899); [DevForum: Using Off-Site links](https://devforum.roblox.com/t/using-off-site-links/1900040)
- **AllowedExternalLinkReferences may be legacy:** it historically returned an array of permitted link types (e.g. Discord, Facebook, Twitch, YouTube). Recent community reports say it now always returns an empty array (the backing endpoint is being sunset). Developers asked whether `IsSubjectToChinaPolicies` alone is a valid gate for Discord invites (2026 thread). — [robloxapi PolicyService mirror](https://robloxapi.github.io/ref/class/PolicyService.html); [DevForum reply in Age Check thread](https://devforum.roblox.com/t/age-check-requirement-to-chat-now-live-globally/4226101/4221); [DevForum: Is showing a Discord invite using only IsSubjectToChinaPolicies…](https://devforum.roblox.com/t/is-showing-a-discord-invite-using-only-issubjecttochinapolicies-as-a-check-within-tos/4578884)

**AI-generated content and Terms**
- **April 30, 2026 Terms of Use:** simplified terms; clarifications on the use of AI tools and their data use; clearer language on IP tools and derivative works. — [Roblox Help: Roblox is Updating our Terms of Use](https://en.help.roblox.com/hc/en-us/articles/14663412502676-Roblox-is-Updating-our-Terms-of-Use); [DevForum: Updates to the Roblox Terms of Use [April 2026]](https://devforum.roblox.com/t/updates-to-the-roblox-terms-of-use-april-2026/4548394)
- **EEA/UK/CH terms:** Roblox "does not assert any ownership rights in any new intellectual property created in your Outputs". Prompts and AI outputs count as UGC, and creators are solely responsible for the UGC they license to Roblox. — [Roblox Help: Terms update for EEA/UK/Switzerland](https://en.help.roblox.com/hc/en-us/articles/52986438082068-Roblox-is-Updating-our-Terms-of-Use-for-the-European-Economic-Area-the-United-Kingdom-and-Switzerland)
- **November 1, 2026 Terms update:** language simplified and sections reorganized, including the User Terms and Creator Terms. Details beyond that were not found. — [DevForum: Updates to the Roblox Terms of Use [November 2026]](https://devforum.roblox.com/t/updates-to-the-roblox-terms-of-use-november-2026/4907620)
- **Real-time AI moderation (March 2026):**
  - Multimodal model family; repeated violations in one server instance shut down that server only.
  - Roadmap: a "Safety Callback API" so scripts can remove violating content before a shutdown.
  - Creator Analytics now shows proactive safety protections.
  — [DevForum: New transparency into proactive safety protections in Creator Analytics](https://devforum.roblox.com/t/new-transparency-into-proactive-safety-protections-in-creator-analytics/4538721); [Creator Roadmap 2026 Fall Update](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208)

**IP / DMCA**
- **Rights Manager (launched April 2024):** a central tool to request removal of infringing content (IP originating on or off Roblox; removes only content hosted on Roblox). — [DevForum: Introducing Rights Manager](https://devforum.roblox.com/t/introducing-rights-manager/2880717)
- **IP Platform Terms:** a "Claims" filing is not a DMCA notice. Undisputed claimed UGC is delisted from the Marketplace or Creator Store. — [Roblox Help: IP Platform Terms of Use](https://en.help.roblox.com/hc/en-us/articles/21857240911380-IP-Platform-Terms-of-Use)
- **2025 creator complaints (anecdotal):** DMCA handling taking months, wrongful takedowns of the filer's own assets, and a first-upload bias. — [DevForum: Rights Manager DMCAs taking longer than 2 weeks](https://devforum.roblox.com/t/right-manager-dmcas-taking-longer-than-2-weeks/3744199); [DevForum: DMCA report wrongly took down my own assets](https://devforum.roblox.com/t/dmca-report-against-other-users-wrongly-took-down-my-own-assets/3839845); [DevForum: DMCA System has a giant flaw](https://devforum.roblox.com/t/dmca-system-has-a-giant-flaw/3933795)
- **Clone/copy takedown feature:** planned for late 2026. — [Creator Roadmap 2026 Fall Update](https://devforum.roblox.com/t/creator-roadmap-2026-fall-update/4880208)

### Inferences
- Any gacha, crate or spin bought with Robux or Robux-derived currency needs: (a) a PolicyService gate, (b) a non-random alternative for restricted users, and (c) visible percentage odds before purchase, applied worldwide. Building this from day one avoids retrofits.
- Because of the uncertainty around `AllowedExternalLinkReferences`, the safest course is to avoid off-platform links in-experience, or to show them only to users who pass a PolicyService check.

### Gaps
- No current Community Standards text was found that specifically governs AI-generated content (for example disclosure duties). Only the Terms provisions above were found.
- Neither the 2026 Advertising Standards content nor the current official Roblox rule on Discord and social links was confirmed.
- No official dedicated "monetization toward minors" creator guideline update for 2026 was found, beyond the paid random items rules and the Advertising Standards.

---

## 8. Safety APIs for developers: TextChatService, GetChatGroupsAsync, PolicyService, voice

### Takeaway
`TextChatService:GetChatGroupsAsync` (Feb 13, 2026) returns chat-group IDs so servers can matchmake and teleport players who can legally chat with each other. A voice counterpart, `VoiceChatService:GetChatGroupsAsync`, followed. PolicyService's `GetPolicyInfoForPlayerAsync` fields confirmed in sources: `ArePaidRandomItemsRestricted`, `IsSubjectToChinaPolicies`, `AllowedExternalLinkReferences` (possibly legacy/empty), `IsContentSharingAllowed` and `IsPaidItemTradingAllowed`.

### Cited Findings
- **`TextChatService:GetChatGroupsAsync`:**
  - Server-side; takes a list of Players and returns chat-group IDs; players sharing an ID can text chat.
  - Intended for real-time matchmaking and teleporting.
  - Requires enabling "Chat & Voice Groups APIs" in Experience Settings and accepting the Terms. Available in Studio only in Team Test.
  - IDs are universe-specific, can change, and must not be stored after the user leaves.
  — [Creator Hub: TextChatService](https://create.roblox.com/docs/reference/engine/classes/TextChatService); [DevForum: New Chat APIs: Teleport Users Who Can Chat Together (Feb 13, 2026)](https://devforum.roblox.com/t/new-chat-apis-teleport-users-who-can-chat-together/4337233)
- **Bug report:** it can return an empty array on join for verified players (single report). — [DevForum: GetChatGroupsAsync not reliably returning chat groups on join](https://devforum.roblox.com/t/textchatservicegetchatgroupsasync-not-reliably-returning-chat-groups-on-join/4540533)
- **TextChatService message filtering:** messages sent through a TextChannel are filtered and age-gated automatically. Custom UIs must still route messages through TextChatService (community explanation). — [DevForum: How to make a custom chat system using TextChatService](https://devforum.roblox.com/t/how-to-make-a-custom-chat-system-using-textchatservice/4097288); [DevForum: How Do I filter custom chat](https://devforum.roblox.com/t/how-do-i-filter-custom-chat/4479906)
- **PolicyService fields:**
  - `IsSubjectToChinaPolicies`: China Program compliance. — [robloxapi PolicyService](https://robloxapi.github.io/ref/class/PolicyService.html)
  - `IsContentSharingAllowed`: true when the player may share off-platform, e.g. via `CaptureService:PromptShareCapture`. — [robloxapi PolicyService](https://robloxapi.github.io/ref/class/PolicyService.html)
  - `IsPaidItemTradingAllowed`: appears in sample responses; no official description found. — [Roblox Fandom: GetPolicyInfoForPlayerAsync](https://roblox.fandom.com/wiki/Class:PolicyService/GetPolicyInfoForPlayerAsync)
  - `ArePaidRandomItemsRestricted`: required for paid random items. — [Community Standards](https://about.roblox.com/community-standards); [DevForum: Wording clarity for ArePaidRandomItemsRestricted](https://devforum.roblox.com/t/wording-clarity-for-arepaidrandomitemsrestricted-policy-description-column/1418339)
  - `AllowedExternalLinkReferences`: see Section 7.
- **Voice:** a voice counterpart to the chat-groups API exists. — [DevForum 4337233](https://devforum.roblox.com/t/new-chat-apis-teleport-users-who-can-chat-together/4337233)

### Inferences
- For social and multiplayer games after January 2026, building lobbies around chat groups, so that teleported groups can actually talk to each other, likely helps co-play, which is an RFY "important" signal.

### Gaps
- Other PolicyService fields such as `AreAdsAllowed` or `IsEligibleToPurchaseSubscription` could not be confirmed this session. Check them against the official PolicyService reference before use.
- No 2025–2026 voice-chat eligibility rules were found (age/ID requirements for voice, spatial voice policy). The search budget ran out before this could be researched.
