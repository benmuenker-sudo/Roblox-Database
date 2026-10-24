# Checking the Roblox research notes against the official Creator Documentation (as of 2026-10-24)

**Source and method.** These notes check claims against a local clone of the official `Roblox/creator-docs` repo. That repo is the Markdown/YAML source of create.roblox.com/docs. The text is licensed CC BY 4.0, and code samples are MIT under LICENSE-CODE ("Copyright (c) 2023 Roblox Corporation").
- **Snapshot:** a shallow clone with a single commit, `4e795e6`, dated **Sat Oct 24 10:11:10 2026 +0000** ("update Open Source Docs from Roblox internal teams"). Because it is shallow, there is no file history and no per-page last-modified date.
- **Search method:** only Grep, Glob and Read on the clone. There was no web access.
- **Citation format:** each source is given as the public URL (`https://create.roblox.com/docs/<path-without-.md>`).
- **Verdict labels:**
  - **CONFIRMED:** the docs say the same thing.
  - **CORRECTED:** the docs say something different. The docs' value is given.
  - **NOT IN DOCS:** the local docs say nothing about it. That does not make the claim false.
  - **NEW:** official detail that the earlier notes did not have.
- **Earlier note files checked:** plattform_discovery_regeln.md, monetarisierung.md, retention_liveops_design.md, ui_map_sound.md, technik_luau.md, markt_trends.md.

---

## 1. Discovery: Recommended For You (RFY) signals, PTR/bounce, 28-day windows, thumbnails, icons, Today's Picks, charts, events, notifications

### Takeaway
The official Discovery page and FAQ confirm the signal tiers.
- **Most important:** PTR, first play bounce rate, play days per user and playtime per user.
- **Important:** intentional co-play days, qualified play sessions, spend days and Robux spent.

All signals are per-user averages over users who arrived organically through RFY. They are measured in Day 1, Day 2–7 and Day 8–28 segments. Bounce is measured in <60 s and 61–180 s buckets, and playtime is capped at 60 min per user per game per day. Neither page uses the phrase "28-day window" or gives any numeric weights.

The thumbnail page describes the personalization algorithm in words but never uses the term "multi-armed bandit". It still optimizes for *qualified* play-through rate (qPTR). Today's Picks is an editorial, nomination-based sort, not an algorithmic one. A custom thumbnail is now **required** for Home recommendation impressions.

### Cited Findings
**RFY mechanics**
- **NEW: two-stage model.** "Stage 1: Retrieval… selects a subset of games… based on key signals like engagement, retention, and monetization." "Stage 2: Ranking… How far your game goes… depends entirely on the engagement and retention of users who come to your game through Recommended for You. Roblox doesn't count the engagement, monetization, or retention of users first acquired from ads, curation, friends, search, social media, or any other source in the ranking stage." — [Discovery](https://create.roblox.com/docs/discovery)
- **CONFIRMED: signal tiers.**
  - Most important: Play through rate ("The rate at which users play your game after seeing it in the Recommended for You sort"), First play bounce rate ("**This is a negative signal**"), Play days per user, Playtime per user.
  - Important: Intentional co-play days per user ("including co-play days through join, invites, or private servers"), Qualified play sessions per user, Spend days per user, Robux spent per user.
  - "There is no single signal that determines ranking."
  - Sources: [Discovery](https://create.roblox.com/docs/discovery); [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)
- **NEW: exact time segments.**
  - First play bounce rate uses "< 60 seconds average rate" and "61-180 seconds average rate".
  - Play days, playtime and the "Important" signals use "Day 8-28 average", "Day 2-7 average" and "Day 1 average".
  - PTR has "N/A".
  - Playtime: "There is a maximum of 60 minutes per user, per game, per day."
  - Source: [Discovery](https://create.roblox.com/docs/discovery)
- **NOT IN DOCS: the June 15, 2026 date, the "7-day → 28-day" wording and the removal of QPTR.** The docs show only the current state: Day 8–28 segments, with PTR and bounce among the top signals.
- **NOT IN DOCS: numeric weights.** The docs say only "each carrying a different amount of influence".
- **CONFIRMED / NEW: PTR and bounce count only new users from RFY.** "PTR and first play bounce only measure users acquired organically from Home recommendations in their first session… Returning-user traffic comes through other sorts such as Continue." Day 2–7 and Day 8–28 then track those same RFY-acquired users even when they come back through other surfaces. — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)
- **NEW: how Day 2–7 is calculated.** "Play days: Out of the 6 days in the 2–7 window, how many days on average did those users play." — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)
- **NEW / resolves a gap: cold start.** "New games do not have to wait 28 days… Playthrough rate and bounce rate capture the first session; Then Day 1 signals…; Then Day 2–7; Then Day 8–28. Early signals kick in immediately."
  - "The retrieval stage requires only a very low minimum number of plays from any source… The algorithm tests your game daily."
  - "There is no penalty for games that did not perform well at first. The signals use a moving window."
  - Source: [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)
- **NEW / partly resolves the bucket-weighting gap:** the three segments "are considered both separately and combined together to decide impression volume." — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)
- **NEW: Home pre-ranking.** "narrows down to roughly 100 games shown on a user's Home page." — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)
- **NEW: genre is not an explicit ranking factor.** "Genre and gameplay type are not explicit ranking factors… Changing your genre tag does not change the underlying behavioral signals." Story-driven and finite games "are not penalized" for lower Day 8–28 retention. — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)
- **NEW: ads and RFY.**
  - "Engagement, retention, and monetization from users acquired through ads are excluded from RFY ranking signals."
  - "When a user is acquired through an ad, Roblox considers that user already acquired. This means the user acquired through an ad will generally not subsequently see your game in RFY… Ads do not penalize or downrank your game."
  - The **Plays** objective is described as helping a game "get considered for Recommended For You". This matches the retrieval stage.
  - Sources: [Discovery FAQ](https://create.roblox.com/docs/discovery-faq); [Ads Manager](https://create.roblox.com/docs/production/promotion/ads-manager)
- **CONFIRMED: benchmarks do not affect the algorithm.** "Benchmarks and benchmark games do not impact the Recommended for You algorithm in any way." — [Discovery](https://create.roblox.com/docs/discovery)
- **NEW: retention vs. monetization.** "Games that are strong in only one area… will continue to receive Home recommendation impressions. However, games that perform well in both… might receive broader distribution." Also: "If retention is low, focus on core gameplay first. Once retention is strong, improving monetization can help you increase your Home impressions." — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)
- **NEW: four impression factors.**
  1. Your own changes.
  2. Roblox algorithm changes.
  3. Home traffic and seasonality ("Weekly seasonality which usually peaks on a Saturday").
  4. Competitors improving more than you.
  - Source: [Discovery](https://create.roblox.com/docs/discovery)
- **NEW: issues that limit exposure.**
  - "Leading with giveaways", "Mismatched metadata and content" and "Non-unique games".
  - A daily-updated banner on the Creator Dashboard shows the status.
  - Originality is credited to "the game that first added the unique metadata and/or placefile", not to whichever game was created first.
  - Sources: [Discovery](https://create.roblox.com/docs/discovery); [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)
- **CONFIRMED (the DevForum title whose content was unverified): custom thumbnail required.** "A custom thumbnail is required for your game to receive impressions from homepage recommendations. If your game only has a default thumbnail, it is not eligible." — [Discovery](https://create.roblox.com/docs/discovery)
- **NEW: opting out of RFY.** "Exclude from recommendations" toggle under Audience > Advanced Settings. — [Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places)

**Search, charts, Today's Picks and other sorts**
- **CORRECTED: search is officially documented, but only briefly.** The docs say search "historically… focused on relevance based on exact search queries and limited metadata such as titles", and that "you can now use semantic search for all of our officially supported languages… such as 'food games'". No ranking factors are listed. — [Discovery](https://create.roblox.com/docs/discovery)
- **NEW: Search ads.** Advertisers pick "up to 10 keywords within an Ad Set". The ads show "if a user submits a search with an exact keyword match", at the top of results or right after an exact-name match. — [Search ads](https://create.roblox.com/docs/production/promotion/search-ads)
- **CORRECTED: Today's Picks is editorial.** "Today's Picks on Home is a curation of the best games on a daily basis." Creators nominate through a survey, and "Our editorial team reviews nominations on an ongoing basis… only those selected… will be notified." Re-apply "each time your game has a notable update." Status: Open. — [Today's Picks on Home](https://create.roblox.com/docs/creator-programs/todays-picks-home)
- **NEW: Standout Games.**
  - A hand-curated Home sort for "novel games" that takes nominations through a survey.
  - "RPG, strategy, puzzle, and shooter games are heavily underrepresented despite strong demand from older age groups."
  - "Games that seem like a copy or reskin of a popular Roblox game are a hard sell."
  - Sources: [Standout Games](https://create.roblox.com/docs/creator-programs/standout-games); [Discovery](https://create.roblox.com/docs/discovery)
- **NOT IN DOCS: charts with "about 29 sorts".** The docs only say "top and trending sorts have been updated". — [Discovery](https://create.roblox.com/docs/discovery)

**Thumbnails and icons**
- **CONFIRMED: thumbnail specs.**
  - "16:9 aspect ratio and ideally 1920×1080 pixels"; formats `.jpg`, `.gif`, `.png`, `.tga`, `.bmp`.
  - "stretched to 16:9 aspect ratio regardless of the upload's aspect ratio".
  - "avoid placing any essential text or elements at the **bottom**".
  - Source: [Thumbnails](https://create.roblox.com/docs/production/publishing/thumbnails)
- **CONFIRMED (3rd-party "10 thumbnails") / NEW: more limits.**
  - "up to 10 images or videos for each of your games' detail pages".
  - Video thumbnails: "Free, with monthly quota of 3 uploads". Rejected videos "count against the monthly quota".
  - Personalization uploads: "keep these images under 3 MB and 1920×1080 pixels".
  - These settle the 3 MB vs. 8 MB conflict for personalization uploads at **3 MB**.
  - Source: [Thumbnails](https://create.roblox.com/docs/production/publishing/thumbnails)
- **NEW: video rules.**
  - Not allowed: "Spoken Audio — Added voice-overs, narration, voice chat conversations, and music with lyrics", "External Content & Overlays" and claims such as "50% off" / "Free UGC!".
  - Allowed: camera work, minor post-processing, logo overlay and catalog music.
  - "Xbox, PlayStation, and VR headsets do not currently support video thumbnails."
  - Source: [Thumbnails](https://create.roblox.com/docs/production/publishing/thumbnails)
- **CONFIRMED: personalization limits and results.**
  - "Thumbnail personalization only starts when you activate 2 or more thumbnails"; enable "Active" on "2-5 thumbnails".
  - "average increase of +8.5% in their qualified play through rate. Some games had an increase of +50%."
  - Source: [Thumbnails](https://create.roblox.com/docs/production/publishing/thumbnails)
- **CORRECTED / precision: wording and target metric.** The docs do not use the term "multi-armed bandit". They describe the algorithm like this: it "shows each thumbnail to a random set of users to get data on the qualified play through rate for each user group. It then gives more impressions to the winning thumbnail for each group, but still gives the other thumbnails minimal traffic." Its stated goal is still "**qualified** play through rate". This answers the open question: the docs have not switched the thumbnail target to PTR. — [Thumbnails](https://create.roblox.com/docs/production/publishing/thumbnails)
- **NEW: test cadence.** "keep multiple thumbnails active instead of choosing one winner". "test multiple new thumbnails with any major game or content update, and then not make changes to your thumbnails until your game's next update." — [Thumbnails](https://create.roblox.com/docs/production/publishing/thumbnails)
- **NOT IN DOCS:** the July 2025 change ("remembers winning thumbnails") and the Open Cloud thumbnail personalization API.
- **CONFIRMED: icon.**
  - "template of **512×512 pixels**… icons scale down to smaller sizes like 150×150 pixels".
  - "square and at least 512×512".
  - "you can only display one icon per locale". All icons go through moderation.
  - Source: [Icons](https://create.roblox.com/docs/production/publishing/experience-icons)
- **NOT IN DOCS: native icon A/B testing.** No such feature is documented. Reusing thumbnails or icons is allowed: "Reusing an existing thumbnail alone shouldn't negatively affect discoverability." — [Discovery FAQ](https://create.roblox.com/docs/discovery-faq)

**Events and notifications**
- **CONFIRMED: Trending Events.** "An active event that started within the last 7 days. Minimum of 1,000 RSVPs." Ranked by "the experience's daily active users (DAU), filterable by location and platform". — [Experience events](https://create.roblox.com/docs/production/promotion/experience-events)
- **NEW: event limits.**
  - "you can publish a maximum of 10 ongoing or upcoming events".
  - Up to "5 thumbnails" per event plus "a primary event type".
  - "Notify Me" delivers stream notifications, with opt-in push.
  - Sources: [Experience events](https://create.roblox.com/docs/production/promotion/experience-events); [Discovery](https://create.roblox.com/docs/discovery)
- **NEW: Update announcements.** "Updates have a limit of 60 characters and you can only announce an update once every three days." — [Experience events](https://create.roblox.com/docs/production/promotion/experience-events)
- **NEW: "Submit for Featuring" (off-platform featuring).**
  - Requirements: the creator is 13+ with a linked email; the event is "submitted at least 7 days prior to the event start".
  - "The best events run for 7-30 days".
  - Selection uses "performance signals (DAU growth, playtime, retention, monetization)".
  - Featuring is free and comes with a performance report.
  - Source: [Experience events](https://create.roblox.com/docs/production/promotion/experience-events)
- **CONFIRMED: notification eligibility.** "Minimum 100 visits since launch. The game must not be under moderation. You… must have permission to manage the game." Delivery goes to "opted-in users age 13+". — [Experience notifications](https://create.roblox.com/docs/production/promotion/experience-notifications)
- **NEW / resolves the "notification cap" gap:**
  - "Each user can receive **one** notification per day from a given experience." — [User notifications (Open Cloud)](https://create.roblox.com/docs/cloud/guides/experience-notifications)
  - The opt-in prompt is not shown if the user "Has already seen the permission prompt for your experience in the past 30 days". Launch data is capped at "200 bytes". — [Experience notifications](https://create.roblox.com/docs/production/promotion/experience-notifications)

### Inferences
- Ads can only feed the **retrieval** stage. Ranking ignores ad-acquired users completely, and those users are then "already acquired" and are no longer offered to RFY. A large ad burst can therefore lower RFY impressions while total acquisition rises. The docs say this explicitly.
- Bounce is measured in <60 s and 61–180 s buckets, and Day 1 playtime counts. The first 3 minutes of a session therefore carry very high weight for ranking.
- Optimizing playtime beyond 60 min/day brings no extra RFY signal, because of the cap.

### Gaps
- Numeric signal weights and exact bucket weights: NOT IN DOCS.
- Charts ranking and the number of sorts: NOT IN DOCS.
- Whether the thumbnail-personalization metric will move from qPTR to PTR: the docs still say qPTR.

---

## 2. Publishing and age gating: 16+ vs. all ages, unlocking under-16 reach, Expedited Review, maturity labels, unrated games

### Takeaway
The docs confirm the tiered model.
- **16+ release:** an account in good standing and at least 2 days old, plus an age check. Answering "No" to the first questionnaire question gives a "Content May Vary" label and 16+-only release.
- **All-ages release:** additionally ID verification (facial age estimation if under 18, government ID if 18+), 2FA, a 2-month Plus/Premium subscription **or** a refundable 1,000 Robux fee, the full questionnaire with a Minimal/Mild/Moderate rating, and the evaluation process.
- **Evaluation threshold:** "250 unique plays by highly engaged age-checked users within a 60-day window" (CONFIRMED, replacing 500 / 30 days).
- **Expedited Review:** 50,000 Robux, with a 48-hour review (CONFIRMED; the 100k figure is outdated).

There are internal contradictions about when the publishing fee is refunded.

### Cited Findings
- **CONFIRMED: account tiers.**
  - Roblox Kids: "Self-declared age 5-8, or age-checked age 5-8"; ratings Minimal or Mild.
  - Roblox Select: "Self-declared age 9 or older (until age-checked), or age-checked age 9-15"; Minimal, Mild or Moderate (9+).
  - Roblox: "Age-checked age 16 or older"; "All rated content, except Restricted (18+)".
  - Source: [Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)
- **NEW: chat defaults per tier.**
  - Kids: "Off by default. Once age-checked, chat can be enabled through a linked parent account."
  - Select: "Off for self-declared accounts".
  - Roblox: "chat is on by default".
  - Source: [Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)
- **CONFIRMED: requirements for 16+.**
  - "Have an account that is in good standing and at least 2 days old. Complete an age check through facial age estimation or government ID."
  - First questionnaire question: answering **No** gives "a **Content May Vary** label. The game releases only to age-checked Roblox users ages 16+."
  - Requirements "apply to **all** release actions", including updates, "Publish As" and changes to the target audience.
  - Source: [Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places)
- **CONFIRMED with refinement: requirements for all ages.**
  - "Verify your account through facial age estimation if you are under 18 years old, or through government ID if you are 18 years old or older."
  - Enable 2FA.
  - "Maintain an active Roblox Plus or Roblox Premium subscription for 2 consecutive months" **or** "Pay a one-time, refundable fee".
  - Pass the evaluation process.
  - Get a Minimal, Mild or Moderate (9+) rating.
  - This fits the RTC post that under-18 creators do not need an ID check: they verify with facial age estimation instead.
  - Sources: [Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places); [Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)
- **CONFIRMED: publishing fee is 1,000 Robux.** "one-time, refundable fee of 1,000 Robux per game". — [Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places)
  - **CONFLICT INSIDE THE DOCS on refund timing:**
    - The publish page: "If your game maintains 25 highly engaged players for 60 days without moderation, you will receive a refund".
    - The Kids/Select FAQ: "automatically refunded 90 days after your game becomes eligible… If your game never reaches eligibility, it's still refunded 90 days after your initial payment date."
    - The earlier notes said "3 months after eligible". That matches the FAQ.
    - Sources: [Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places) vs. [Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)
- **CONFIRMED: threshold of 250 plays in 60 days.**
  - "Once the game reaches a benchmark of 250 unique plays by highly engaged age-checked users within a 60-day window, it completes evaluation."
  - Progress is tracked in the "Audience Reach" dashboard. "This metric is evaluated hourly."
  - The first step is a "Trial phase — The game is first made available only to age-checked users 16 and older."
  - Source: [Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)
- **NEW: definition of a "highly engaged player."** "must meet requirements on account tenure, playtime in your game, and platform spend… made a minimum purchase anywhere on Roblox in the last 60 days and have spent time in your game within that same window. They don't need to spend anything in your game specifically… your game doesn't need to be monetized." Engagement is checked by the "Realtime Multimodal Moderation system". — [Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)
- **CONFIRMED: Expedited Review is 50,000 Robux (CORRECTS the 100,000 figure).**
  - "one-time, refundable fee of 50,000 Robux per game".
  - "If a minor violation is found during the 48-hour review… The 48-hour clock restarts from the point of resubmission."
  - Refund: "After 90 days, you can request a refund. As long as your game remains in good standing and maintains 25 highly engaged players".
  - No refund after permanent moderation.
  - Sources: [Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places); [Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)
- **CONFIRMED: an expired subscription does not unpublish a game.** "If your subscription later expires, your game stays published for all ages." — [Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)
- **CONFIRMED: free Plus for creators.** The FAQ mentions a free Plus subscription that "rolled out one day later than planned", with automatic refunds of fees paid by mistake. — [Roblox Kids and Select](https://create.roblox.com/docs/production/publishing/kids-and-select)
- **NEW: release limits and early testers.**
  - "You can release up to 5 games per day that have never been released before."
  - Early testers: "up to 10 similar-aged friends". The age matrix allows, for example, 18+ creators to invite 16+ testers and 13–15 creators to invite 9–17 testers.
  - Source: [Publish games and places](https://create.roblox.com/docs/production/publishing/publish-games-and-places)
- **CONFIRMED / precise: maturity labels.**
  - "Minimal or Mild label are eligible for Roblox Kids (ages 5–8) and Roblox Select (ages 9–15)."
  - "Moderate label are eligible for Roblox Select (ages 9–15) and standard Roblox (ages 16+)."
  - "Content May Vary… only accessible to age-checked Roblox users ages 16+."
  - "Restricted label are only accessible to age-verified Roblox users ages 18+."
  - Source: [Content maturity and compliance](https://create.roblox.com/docs/production/promotion/content-maturity)
- **NEW / precise: what triggers 18+ content.**
  - Strong violence, heavy realistic blood, strong language, alcohol, romantic themes and private spaces or adult settings → "only available to age-verified players that are at least 18 years old".
  - "Social hangouts without private spaces are only available to players that are at least 16 years old, and social hangouts with private spaces are only available to age-verified players that are at least 18 years old."
  - This **CORRECTS the old 17+ thresholds** for hangouts. The earlier gap asked whether they had moved to 18+; they have.
  - Source: [Content maturity and compliance](https://create.roblox.com/docs/production/promotion/content-maturity)
- **NEW: Restricted is region-blocked.** "Restricted maturity label are unplayable for players who created their accounts or are located in certain countries or regions, such as Korea, Saudi Arabia, and Türkiye (Turkey)." Assigning Restricted restarts servers and removes all non-18+-verified players. — [Content maturity and compliance](https://create.roblox.com/docs/production/promotion/content-maturity)
- **NEW: questionnaire question 2 is about the paid random items API.** "Does this game respect the ArePaidRandomItemsRestricted policy API?" — [Content maturity and compliance](https://create.roblox.com/docs/production/promotion/content-maturity)
- **NOT IN DOCS (current pages): the September 30, 2025 deadline for unrated games.** The current guide no longer uses "unrated". Instead, a game without the full questionnaire gets "Content May Vary" (16+). A stale page still says "Roblox treats unrated experiences the same as those with an age recommendation of **Ages 13+**". That is a leftover from the older guidelines system and contradicts the current pages. — [Experience guidelines (stale)](https://create.roblox.com/docs/production/promotion/experience-guidelines)

### Inferences
- "Content May Vary" is now the default path. Skipping the full questionnaire costs all under-16 reach and region-specific compliance, but it does not block the game.
- Because the publish page and the Kids/Select FAQ disagree on refund timing, the knowledge base should give both and point to the FAQ as the more recent-sounding wording.

### Gaps
- The exact thresholds for "account tenure" and "playtime in your game" in the highly-engaged definition: NOT IN DOCS.

---

## 3. Monetization: passes, developer products, subscriptions, pricing systems, paid random items, ads, Creator Rewards, DevEx, commerce, paid access, private servers, Plus, transfers, marketplace fees

### Takeaway
Most monetization claims hold up. The official docs add a lot of exact detail and correct several points.
- **Active Spender:** defined as at least **$9.99** of qualifying purchases in 60 days.
- **18+ DevEx rate:** includes **developer products** and requires **R15-only** player characters (the community claim is CONFIRMED).
- **Cross-game sales:** disabled from **May 30, 2026** (not May 29).
- **Transfers:** only **Plus subscribers** can send, 10–500 Robux per transaction.
- **Rewarded Video:** eligibility is now **2,000 unique visitors/month**, ID verification and 2FA (the old 100K DAU rule is outdated).
- **Avatar items:** the docs list a uniform 30% creator commission, 80 Robux upload fee and 10 Robux 2D publishing advance.

### Cited Findings
**Passes and developer products**
- **CONFIRMED (indirectly): 70% creator share for in-game items.** The Plus table shows "Non-subscriber… 100 [price]… 70 [creator earnings]… 70%". Neither the passes page nor the developer products page states the fee directly. — [Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus)
- **CORRECTED date: cross-game sales end May 30, 2026.** "Starting May 30, 2026, cross-game pass sales will be disabled" (passes); the same wording appears for developer products. The earlier notes said May 29. — [Passes](https://create.roblox.com/docs/production/monetization/passes); [Developer products](https://create.roblox.com/docs/production/monetization/developer-products)
- **NEW: sales outside the game (this has shipped).**
  - "Roblox surfaces your **Listed** passes outside your game, including on the Roblox homepage, in search results, and on the post-purchase page after a player buys Robux. A player can buy your pass and then join your game with it already granted."
  - Developer products additionally need a correct `ProcessReceipt`: "Roblox checks your ProcessReceipt implementation on an ongoing basis. If an issue is detected, the developer product stops showing on surfaces outside your game".
  - This updates the roadmap item "late 2026 pre-entry storefront".
  - Sources: [Passes](https://create.roblox.com/docs/production/monetization/passes); [Developer products](https://create.roblox.com/docs/production/monetization/developer-products)
- **NEW: Buy Robux page promotion.** Promoted passes "must be greater than 49 Robux and less than 801 Robux"; there is "no limit to the number of passes you can promote." — [Passes](https://create.roblox.com/docs/production/monetization/passes)

**Subscriptions**
- **CONFIRMED / clarified: subscription payouts.**
  - Robux: "Any amount equal to or greater than 49 Robux", "70% of subscription earnings each month".
  - Local currency: "\$2.99, \$4.99, \$7.99, \$9.99, or \$14.99", "70% in the first month, then 100% in subsequent months", "at a rate of US \$0.01 to 1 Robux". Example: \$5 → 350 Robux in month 1, then 500.
  - Hold periods: local currency "30-day hold"; Robux "approximately 5 days".
  - Robux price changes are allowed "once every 60 days", with 30 days' notice for increases.
  - Regional pricing is on by default for Robux subscriptions "and cannot be turned off".
  - "Mutually exclusive subscriptions are not supported."
  - Source: [Subscriptions](https://create.roblox.com/docs/production/monetization/subscriptions)

**Managed pricing, regional pricing and price optimization**
- **CONFIRMED: Managed pricing.**
  - "a unified system… that combines price optimization and regional pricing under a single opt-in".
  - "New games and newly created items are enrolled in Managed pricing by default. Item-level opt-out is available".
  - Existing regional-pricing items "transition to managed pricing automatically".
  - "Subscriptions, Private Servers, and Developer Servers are regionalized automatically".
  - "Regional prices are bound between 30% and 100% of the default price."
  - Source: [Managed pricing](https://create.roblox.com/docs/production/monetization/managed-pricing)
- **CONFIRMED (the DevForum "never below 30%" quote):** "Regional prices will never be discounted by more than 70% of your default price… if your item has a default price of 100 Robux, the lowest… is 30 Robux." The DevForum report of roughly 60% discounts is therefore within the range. — [Regional pricing](https://create.roblox.com/docs/production/monetization/regional-pricing)
- **CONFIRMED / precise: VPN handling.** "To determine a user's economic location, Roblox looks at signals, including VPN usage, billing history, and account history. If their economic location can't be determined, users see the default global price." — [Regional pricing](https://create.roblox.com/docs/production/monetization/regional-pricing)
- **NEW: anti-arbitrage API.** `GetUsersPriceLevelsAsync` returns "a numerical value between 1 and 1000… The price level 1000 represents the full global price." Results should be fetched at join and not cached across sessions. — [Regional pricing](https://create.roblox.com/docs/production/monetization/regional-pricing)
- **NEW: price optimization requirements and test design.**
  - "at least 60,000 transactions over the previous 30 days".
  - Test duration: "After approximately 3 weeks".
  - "Tests run automatically at least every 90 days".
  - "optimized prices are applied only if it results in positive incremental total revenue".
  - The review period keeps "2% of users shown the original prices".
  - The "+4%" figure: NOT IN DOCS.
  - Source: [Price optimization](https://create.roblox.com/docs/production/monetization/price-optimization)
- **CONFIRMED: hard-coded prices.** Managed pricing prompts you to fix hard-coded prices before opt-in. The Dynamic Price Check accepts "up to five Roblox users" as test accounts. Plus discounts also break hard-coded UI prices. — [Managed pricing](https://create.roblox.com/docs/production/monetization/managed-pricing); [Price optimization](https://create.roblox.com/docs/production/monetization/price-optimization); [Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus)

**Paid random items**
- **CONFIRMED: odds disclosure.**
  - "you must indicate all possible outcomes and the actual numerical odds"; "Odds must be displayed as a probability percentage… sum to exactly 100%".
  - A pop-up needs "an 'Info' or 'Details' icon visible and accessible prior to purchase. Using a standalone symbol like the (i) icon without a descriptive word is **not** sufficient."
  - Rounding rule: "round to four or more decimal places lower than the decimal place with the first non-zero number" plus a disclaimer.
  - Source: [Paid random items policy guidelines](https://create.roblox.com/docs/production/monetization/paid-random-items)
- **NEW: more required rules.**
  - "If users can only obtain one instance of an outcome, the odds for the remaining obtainable outcomes must be updated."
  - Luck items: "impacts must be numerically explained. The new odds… must also be dynamically updated when these items are active".
  - Indirect purchases (keys, re-roll tokens, spin tickets): odds must be shown "before they spend the in-game currency".
  - Free randomized rewards that involve no Robux or currency need no disclosure.
  - Source: [Paid random items policy guidelines](https://create.roblox.com/docs/production/monetization/paid-random-items)
- **CONFIRMED: item types.** Capsule, Enhancement, Combination and "Probability modifier items" ("Luck boosts, Pity systems, Enhanced resource drops, Rate-up scrolls"). — [Paid random items policy guidelines](https://create.roblox.com/docs/production/monetization/paid-random-items)
- **CONFIRMED / NEW: PolicyService fields and required treatments.**
  - `GetPolicyInfoForPlayerAsync()` returns `ArePaidRandomItemsRestricted` and `IsPaidItemTradingAllowed`.
  - If restricted, creators "must apply one of these treatments":
    1. an unpaid earnable path;
    2. a pre-determined non-random order;
    3. a direct purchase "priced based on the expected value" (example: a 10 Robux box at 5% odds → 200 Robux direct);
    4. remove or hide the item;
    5. block it with an error message;
    6. teleport the player away.
  - If `IsPaidItemTradingAllowed` is false: "must not allow them to access the ability to trade the resulting outcome of a paid random item or other paid items."
  - Source: [Paid random items policy guidelines](https://create.roblox.com/docs/production/monetization/paid-random-items)
- **NEW: rule in the monetization overview.** "If a user can use Robux or something else that was acquired with Robux to get a random reward, you are required to use PolicyService to block this feature for users who are not permitted". It also warns: "A discount is not genuine if an item is always 'on sale' for the same amount of Robux." — [Monetization](https://create.roblox.com/docs/production/monetization)
- **NOT IN DOCS: the list of regulated markets** (AU/BE/NL/UK/BR), the Player Emulator test and the May 26, 2026 date. The policy page names no countries.

**Rewarded video and immersive ads**
- **CORRECTED / resolves a gap: Rewarded Video eligibility.**
  - Games must be "public and unrestricted", have "no free-form user creation", a reviewed questionnaire and "an average of at least **2,000 unique visitors per month**".
  - Publishers must be "13+", in good standing, have "two-step verification (2FA) and verified your ID".
  - The old 100K DAU and Minimal/Mild limits are no longer documented.
  - Source: [Rewarded video ads](https://create.roblox.com/docs/production/promotion/rewarded-video-ads)
- **CONFIRMED / NEW: Rewarded Video earnings and rules.**
  - "multiplying EPM (earnings per 1000 impressions) by the total number of impressions".
  - Ad length: "6 to 30 seconds".
  - Recommended reward: "equivalent to 3 to 10 Robux".
  - "Rewards must be **developer products**. You can't reward users with Robux." Rewards "**cannot** be randomized items"; an ad must not be used as a "progress gate".
  - Granting runs through `ProcessReceipt`.
  - The forecaster uses "ads-eligible users… in the last 7 days × ads per user × projected EPM".
  - Source: [Rewarded video ads](https://create.roblox.com/docs/production/promotion/rewarded-video-ads)
- **NEW: immersive ad billing units.**
  - Click-to-play video: a "15 second view".
  - Autoplay video impression: at least 0.5 s, at least 1.5% of the viewport, angle up to 55°, at least 50% of pixels visible. An image impression needs at least 1 s.
  - Portal: a successful teleport.
  - Payout "on the 25th of the following month".
  - Source: [Immersive ads](https://create.roblox.com/docs/production/monetization/immersive-ads)
- **NOT IN DOCS:** CPM/EPM rates and the "Join with Reward" placement.

**Creator Rewards (exact formulas)**
- **CONFIRMED / precise: Daily Engagement.**
  - "Creators earn 5 Robux each day if their experience is one of the first three an Active Spender plays for 10+ minutes."
  - Minutes add up within a day: the docs' example has 2 + 10 min = 12 min in Experience A, which counts.
  - Source: [Creator Rewards](https://create.roblox.com/docs/creator-rewards)
- **NEW: Active Spender definition (this was missing).**
  - "Active Spender means any User who on a particular day: (a) has made Qualifying Purchases totaling at least \$9.99 USD anywhere on Roblox within the past 60 days; and (b) was not a New User or Reactivated User during the past 60 days."
  - "Qualifying Purchases means the purchase of Robux, Roblox Premium, or UGC subscriptions."
  - Source: [Creator Rewards](https://create.roblox.com/docs/creator-rewards)
- **CORRECTED / precise: Audience Expansion.** "35% revenue share on their first \$100 of Qualifying Purchases anywhere on the platform during their first 60 days".
  - The window is **60 days**, not "two months". The dashboard still says "first two months".
  - Lapsed User: "has not logged on to Roblox for 60 consecutive days".
  - Three attribution paths:
    1. a Share Link;
    2. a direct link that leads to the user's first session that day;
    3. a search for "the Creator's specific experience name" leading to the first session that day.
  - Each path also requires "10+ minutes within the same day" **AND** that "the experience maintains an average of 100+ DAU for 60 days after the joining or rejoining date". The "100+ DAU" community claim is CONFIRMED.
  - Source: [Creator Rewards](https://create.roblox.com/docs/creator-rewards)
- **NEW: holding period and eligibility.**
  - "Creator Awards… are made in 'Earned Robux' with a 60-day holding period."
  - Audience Expansion requires "an ID-verified account in good standing".
  - Paid access games are eligible.
  - Alt accounts are detected by "unique device ID, IP, and payment data".
  - Source: [Creator Rewards](https://create.roblox.com/docs/creator-rewards)
- **CONFIRMED: the old program is deprecated.** "Effective July 24, 2025, the Engagement-Based Payouts program is deprecated and has been replaced by the Creator Rewards program." — [Engagement-based payouts](https://create.roblox.com/docs/production/monetization/engagement-based-payouts)

**DevEx**
- **CONFIRMED: rates.**
  - "standard exchange rate… is 0.0038 per 1 Earned Robux, which comes out to \$114 USD for 30,000 Earned Robux".
  - "Before September 5, 2025 at 10am PT, the standard exchange rate was 0.0035."
  - Order: "You can only cash out your Earned Robux at the old exchange rate before you can cash out any Earned Robux at the current exchange rate."
  - Spending Robux does not reduce the legacy balance first.
  - Source: [Developer Exchange](https://create.roblox.com/docs/production/monetization/developer-exchange)
- **CONFIRMED: requirements.** "Be at least 13 years old; Have a minimum of 30,000 Earned Robux; Have a Roblox-verified email address; … W-9… or W-8". The docs list no Premium requirement. After the first approval, the DevEx Portal (Tipalti) must be completed "within one week". — [Developer Exchange](https://create.roblox.com/docs/production/monetization/developer-exchange)
- **CORRECTED / precise: U.S. 18+ rate.**
  - "0.0054" for Earned Robux from "Developer products, Passes, Subscriptions, Private servers" bought by U.S. players age-verified as 18+.
  - The docs list **developer products**. Avatar items are not listed.
  - Effective "June 8, 2026".
  - **CONFIRMED (community R15 claim):** player characters must spend "100% of active playtime" as R15 (standard or advanced), custom human-form or custom non-human-form characters. "If a player can spawn into or swap to a R6 avatar at any point during active playtime, your game is **not eligible**." Animation packs must be R15.
  - Games without a player character qualify as non-human-form. NPCs are not evaluated. A background compliance check runs.
  - Group payouts and DevEx requests "prioritize the U.S. 18+ DevEx rate".
  - Source: [U.S. 18+ exchange rate](https://create.roblox.com/docs/production/monetization/18-plus-devex-rate)
- **NEW: tax withholding.** "If you provide valid tax information by October 31, 2026, **0% to 30% U.S. tax withholding** will apply on your DevEx payments related to sales to U.S. players". — [Tax information](https://create.roblox.com/docs/production/monetization/tax-information)

**Commerce, paid access and private servers**
- **CONFIRMED / precise: commerce (Shopify).**
  - Creators must be 18+ and the Shopify account holder, or have written permission.
  - "only US-based users can purchase commerce products… 13+ years of age, except Texas. Must be 18+ years of age in Texas."
  - The game must be public and have maturity labels.
  - Digital-benefit bundles require "more than 100,000 daily active users on average for the last 90 days" **and** "more than 1,000,000 Robux average monthly earnings", **or** "ad spend amount of at least \$50,000 USD in one year".
  - Commerce revenue split: NOT IN DOCS.
  - Source: [Commerce products](https://create.roblox.com/docs/production/monetization/commerce-products)
- **NEW (filled from docs; previously not researched): paid access.**
  - Robux: "anywhere from 25 to 1000 Robux". Escrow "up to 7 days"; no refunds.
  - Local currency: revenue share tiers "\$9.99 → 50%, \$29.99 → 60%, \$49.99 → 70%". Escrow "minimum of 60 days", monthly payout through Tipalti, and only the group owner receives payouts.
  - Paid access and private servers cannot be enabled at the same time.
  - Sources: [Paid access in Robux](https://create.roblox.com/docs/production/monetization/paid-access-robux); [Paid access in local currency](https://create.roblox.com/docs/production/monetization/paid-access-local-currency); [Private servers](https://create.roblox.com/docs/production/monetization/private-servers)
- **NEW: private servers.** "Changing the price of private servers **cancels all active subscriptions**." — [Private servers](https://create.roblox.com/docs/production/monetization/private-servers)

**Roblox Plus**
- **CONFIRMED: sign-up payout.** "250 Robux per month for their first three consecutive months, with up to 750 Robux for every newly acquired subscriber". This is paid only when the subscription is bought through `PromptRobloxSubscriptionPurchase`, starts only once the subscription is paid (free trials do not count), and has a 60-day hold. — [Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus)
- **CONFIRMED / precise: private-server payout.**
  - "at least 60 cumulative minutes over the last 30 days… you can earn up to 100 Robux for that subscriber based on the server price". This is 70% of the server price, capped at 100.
  - Only the server owner's time counts.
  - It is evaluated on the renewal day across the subscriber's "top five paid private servers across Roblox".
  - Source: [Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus)
- **NEW: Plus discount mechanics.**
  - "10% for their first two months, which increases to 20% starting in the third month". Roblox subsidizes the discount, so the creator still earns 70.
  - The docs show an "effective revenue share" of 78% at a 10% discount and 88% at 20%.
  - The discount does not apply to items above 1,000,000 Robux, Marketplace publishing fees, ad credits or group fees.
  - The \$4.99 price: NOT IN DOCS.
  - Source: [Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus)

**Robux transfers**
- **CONFIRMED + NEW.**
  - "your game earns **10%** of the Robux sent and the recipient receives the remaining **90%**… eligible for the DevEx program. Roblox does not take a fee."
  - **Only "Roblox Plus subscribers" can send.**
  - "the amount must be between 10 and 500 Robux per transaction."
  - API: `PromptRobuxTransferAsync` and `BindReceiptHandler` with `RobuxTransferSender` / `RobuxTransferReceiver`.
  - Robux the recipient gets through a transfer is not DevEx-eligible.
  - Sources: [Robux transfers](https://create.roblox.com/docs/production/monetization/robux-transfers); [Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus)

**Marketplace and avatar items**
- **CONFIRMED / CORRECTED: commissions.**
  - "Marketplace Purchase: Creator receives 30%". "In-game Purchase: Creator receives 30%; Game owner receives 40%".
  - A progressive revenue share applies only to Marketplace sales ("1.15x the price floor will receive ~33%").
  - 30-day escrow.
  - Limited resales: "50% to reseller, 10% to creator, 10% to seller/affiliate, 30% to Roblox".
  - The docs no longer give any separate 2D share. The "70%→30%" change is consistent with this, but the old 70% is not documented.
  - Source: [Marketplace fees and commissions](https://create.roblox.com/docs/marketplace/marketplace-fees-and-commissions)
- **CONFIRMED: upload fees.**
  - "Pay an upload fee of **80 Robux** per submission". Emissive items cost "**500 Robux**".
  - Publishing advance: "Classic t-shirt/shirt/pants: 10". 3D advances range from 600 (clothing) to 2,500 (body), and paid Limited advances from 5,000 to 20,000.
  - Uploading requires your own government ID verification or a linked, ID-verified parent account. Selling also needs Plus or Premium 1000/2200 (the community claim is CONFIRMED).
  - Free Limited per-unit fee: "100 Robux".
  - Sources: [Marketplace fees and commissions](https://create.roblox.com/docs/marketplace/marketplace-fees-and-commissions); [Marketplace FAQ](https://create.roblox.com/docs/marketplace/frequently-asked-questions)
- **CONFIRMED: Creator Store.** Prices in USD, "the minimum price is \$4.99 for plugins and \$2.99 for models", with "only taxes and payment processing fees… deducted". — [Monetization](https://create.roblox.com/docs/production/monetization)

### Inferences
- Daily Engagement rewards only reach payers who spent at least \$9.99 in 60 days. They therefore favor games that sit early in the daily routine of established spenders: "first three experiences of the day".
- The 18+ DevEx bonus forces R15-only. R6 games, or games that let players switch to R6, give it up completely.
- A Robux subscription pays 70% every month. A local-currency subscription pays 100% from month 2, so it pays better for long-running subscriptions, but it cannot be regionally priced and its price cannot be changed.

### Gaps
- An explicit "30% fee on passes and developer products" sentence: NOT IN DOCS. It can only be derived from the Plus table.
- Commerce revenue split, Plus price, regulated loot-box markets, CPM/EPM figures: NOT IN DOCS.

---

## 4. Analytics and game design: retention benchmarks, funnel/economy/custom events, Experiments, onboarding, LiveOps, season pass

### Takeaway
The official limits differ from the earlier notes.
- **Benchmark example:** D1 is now **12.11%–18.73%** (50th–90th percentile), not 12.4%–24.1%.
- **Economy events:** the limits table says **10 resource types**, while the AnalyticsService reference and the Economy dashboard say **5**. This is an internal contradiction.
- **Custom events:** 100 event names, 3 custom fields and 8,000 combinations.
- **Global rate limit:** 120 + 20×CCU per minute.
- **Experiments:** 14–60 days, up to 2 variants (in-game) or 3 (matchmaking), and below 1,000 DAU results are weak.

The design guidance is confirmed: 5 minutes to the fun, updates every 2–4 weeks with larger ones every 2–3 months, weekly cadence ideal and monthly the minimum, season pass of 1 month with 1 week of rest and 10 tiers.

### Cited Findings
- **CORRECTED: benchmark example and URL.** "if you see your Day 1 Retention benchmark's 50th - 90th percentile is 12.11% - 18.73%, it means that: 50% of games with similar players have a Day 1 Retention of 12.11% or lower. 10% … 18.73% or higher." The earlier notes had 12.4/24.1 and the URL `.../sales-data`. — [Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard)
- **CONFIRMED / NEW: benchmark pools.**
  - Overall-success KPIs: "top 1000 games with the highest total playtime over a rolling 30 days… excluding games that are less than 30 days old", with tiers "Top 200, Top 500, and Top 1000".
  - Similar-game benchmarks are drawn from games "with at least 100 daily active users". The fallback order is "Games with similar players" → "Genre" → "All experiences".
  - Benchmarked KPIs include Retention (all), Average Session Time, ARPPU, ARPDAU, CVR and Play Through Rate.
  - Source: [Analytics dashboard](https://create.roblox.com/docs/production/analytics/analytics-dashboard)
- **CONFIRMED: retention guidance.** "get users to the fun as quickly as possible, ideally in 5 minutes or less". "smaller updates on the existing mechanics every 2-4 weeks, and bigger updates of new features every 2-3 months." — [Retention](https://create.roblox.com/docs/production/analytics/retention)
- **CONFIRMED: update cadence.** "A **weekly cadence** for updates is ideal. At the bare minimum, aim for monthly updates." — [Monetization](https://create.roblox.com/docs/production/monetization)
- **CONFIRMED: event tracking limits.**
  - "Global Rate Limit — Total AnalyticsService requests per minute: 120 + (20 * CCU)".
  - Custom fields: 3. "After 8,000 combined values across all custom fields, values will be grouped as 'Other'."
  - Economy: "Resource types 10". transactionTypes after 20 → "Other"; itemSkus after 100 → "Other".
  - Funnels: "Number of funnels 10", "Steps per funnel 100".
  - Custom: "eventNames 100".
  - Events roll off "after 90 days from the last data received".
  - Source: [Event types](https://create.roblox.com/docs/production/analytics/event-types)
  - **CONFLICT INSIDE THE DOCS on currencies:** `LogEconomyEvent` says currencyType is "Limited to 5 unique currency types per experience" ([AnalyticsService](https://create.roblox.com/docs/reference/engine/classes/AnalyticsService)), and the Economy dashboard says "You can add up to five currencies" ([Economy events](https://create.roblox.com/docs/production/analytics/economy-events)). The limits table says 10. The earlier note's 5 is defensible; the conflict should be flagged.
- **CONFIRMED: funnels.**
  - "up to ten funnels".
  - "If a user has no events for a funnel for more than 180 days, their saved step expires".
  - "Analytics only tracks the 10 most recent unique funnelSessionId values per user for each funnel".
  - Events are server-only, published games only.
  - Source: [Funnel events](https://create.roblox.com/docs/production/analytics/funnel-events)
- **CONFIRMED / NEW: custom events.** "You can add up to 100 custom events". Aggregation is daily, "may take up to 24 hours". Use custom fields instead of new event names because of "a much tighter cardinality limit on event names". — [Custom events](https://create.roblox.com/docs/production/analytics/custom-events)
- **NEW: `AnalyticsService:GetPlayerSegmentsAsync` (server-only).** It returns coarse buckets: ActivePayerStatus, WhenUserFirstPlayed, PlatformSpenderStatus, ExperienceActivationStatus (last 30 days), EngagementLevel ("How many days the player played this experience in the last 7 days"), PlatformActivationStatus (last 60 days), UserNewReturningStatus and UserAcquisitionSource. It is meant "to personalize content or gate features". — [AnalyticsService](https://create.roblox.com/docs/reference/engine/classes/AnalyticsService)
- **CONFIRMED: Experiments.**
  - "Experiments run for between 14-60 days."
  - In-game: "up to **two variants** and one control".
  - Matchmaking: "up to three variants"; "you can only run one matchmaking experiment at a time"; 100% rollout is recommended.
  - "Games with fewer than 1,000 daily active users might struggle to get useful data".
  - Early harm thresholds: "Playtime -10%, ARPU -20%, Payer conversion rate -20%", with no harm decisions below "10,000 players enrolled across the variant and the control".
  - Source: [Experiments](https://create.roblox.com/docs/production/experiments)
- **NEW: more Experiments detail.**
  - Early-harm metrics refresh "every 5 minutes" during the first 24 hours.
  - **Targeting** by country, tenure or "active spender tiers", which raises the MDE.
  - "You can't run more than one active experiment on the same config key at a time."
  - "Completed… 14 days after for in-game" after the decision date.
  - Source: [Experiments](https://create.roblox.com/docs/production/experiments)
- **CONFIRMED: season pass.**
  - "one month is considered a good starting point… at least a one-week rest period"; "ten tiers is a good place to start".
  - "Provide double XP in the season's final week"; weekly high-reward missions.
  - Mid-season upgraders get the premium rewards for tiers already completed.
  - Source: [Season pass design](https://create.roblox.com/docs/production/game-design/season-pass-design)

### Inferences
- `GetPlayerSegmentsAsync` gives a first-party way to target segments, for example showing a different shop offer to new non-payers than to lapsed spenders, without your own analytics stack. Watch the paid random items and fairness rules when doing this.
- To stay safe with currency tracking, plan for at most 5 currencies and model the rest through custom fields, as the docs themselves recommend for XP.

### Gaps
- Official genre-level D1/D7/D30 numbers: NOT IN DOCS. They are only visible in the dashboard.

---

## 5. UI: ScreenInsets, flex layouts, StyleSheets, accessibility, Input Action System, console and gamepad

### Takeaway
The UI claims in the earlier notes are almost all confirmed. The docs give no official touch-target size. The Input Action System is documented without a beta label; only InputActionLabel and the Input Action Manager are still marked beta.

### Cited Findings
- **CONFIRMED: ScreenInsets.**
  - CoreUISafeInsets is the default and is "recommended if the ScreenGui contains interactive UI elements".
  - DeviceSafeInsets: no inset for the top bar.
  - TopbarSafeInsets: "between the top bar controls and the right edge of the device safe area… automatically flex in horizontal size".
  - None: only for "non‑interactive content like background images".
  - Source: [On-screen containers](https://create.roblox.com/docs/ui/on-screen-containers)
- **CONFIRMED: flex layouts.** `UIListLayout.HorizontalFlex` / `VerticalFlex` distribute extra space, `Wraps` wraps to new lines, and `UIFlexItem` handles each child. — [List and flex layouts](https://create.roblox.com/docs/ui/list-flex-layouts)
- **CONFIRMED: preferred text size.**
  - `GuiService.PreferredTextSize` defaults to Medium, with Large, Larger and Largest.
  - "When TextScaled is enabled… text will **not** be scaled by the PreferredTextSize value."
  - UITextSizeConstraint min and max are respected.
  - Source: [Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)
- **CONFIRMED: reduced motion.** `GuiService.ReducedMotionEnabled`; "set the Time parameter of a TweenInfo to 0". **NEW:** `GuiService.PreferredTransparency` (1 = default, 0 = fully opaque). "Over 5% of people in the world have some form of color blindness." — [Accessibility](https://create.roblox.com/docs/production/publishing/accessibility)
- **CONFIRMED: Input Action System.**
  - InputContext ("PlayContext"/"NavContext"), Priority plus Sink (example Priority `2000`), and InputAction types Bool, Direction1D and Direction2D.
  - **NEW:** `InputAction.PreferredBinding` returns the binding for the current device.
  - "InputActionLabel" and "Input Action Manager" are marked beta.
  - Source: [Input Action System](https://create.roblox.com/docs/input/input-action-system)
- **CONFIRMED: console guidelines.** "typically sitting 8–10 feet away"; `GuiService.ViewportDisplaySize` (Large = TVs); TV-safe areas; "disable the chat window for console games"; content maturity is required for console release. — [Console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines)
- **NOT IN DOCS: an official touch-target minimum** (44 px / 48 dp). The UI/UX design page has no pixel value. — [UI/UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)

### Inferences
- Default rule: UI from the TV distance (10 ft) down to the phone, with no TextScaled on text that should follow Preferred Text Size.

### Gaps
- Official touch-target value and official mobile share: NOT IN DOCS. The user-base page only says "more users that are at least 13 years old than under the age of 13". — [Roblox user base](https://create.roblox.com/docs/production/roblox-user-base)

---

## 6. Environment and performance: draw-call budget (600 vs. 1,000), textures, streaming, LOD, lighting

### Takeaway
The draw-call conflict resolves in favor of **1,000 draw calls and 1,000,000 triangles**, but the docs present this only as an *example* for one baseline device, not as a fixed budget. The values **600 / 650,000 appear nowhere** in the current docs.

Texture limit is **CORRECTED**: general textures can now be **4096×4096 (4K)**. The UV mapping section still says 1024×1024, which is an internal contradiction.

Streaming defaults are confirmed (64 / 1024, Improved recommended). There is a new recommendation to use `StreamOutBehavior = Opportunistic`. `ModelLevelOfDetail.Automatic` is currently equivalent to Disabled.

### Cited Findings
- **CORRECTED / resolved: draw-call budget.** "you might… examine the **Draw (scene)** numbers and determine that you need to stay below 1,000 draw calls and 1,000,000 triangles for the game to run well on your baseline device." It is worded as a hypothetical example: "For example… you might". A search of all docs found no "650,000" and no "600 draw". — [Design for performance](https://create.roblox.com/docs/performance-optimization/design)
- **CORRECTED: texture resolution.**
  - "Roblox supports up to 4096×4096 pixel texture resolutions (4K). As a game loads, the engine automatically starts with lower quality versions… and ramps up quality."
  - Size guidance is unchanged: 5×5 studs → 256², 10×10 → 512², 20×20 → 1024². Parts show "1024×1024 on an 8×8 stud face", terrain "512×512 across 8×8 studs".
  - **CONFLICT INSIDE THE DOCS:** the UV mapping section of the same page says "Roblox supports up to 1024×1024 pixel spaces for texture maps". Avatar and accessory budgets stay at a 1024 maximum, and "256x256 is the maximum budget for non-albedo maps for rigid accessories".
  - Source: [Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications)
- **CONFIRMED + NEW: streaming.**
  - `StreamingMinRadius` "default of 64"; `StreamingTargetRadius` "default of 1024"; `ModelStreamingBehavior.Improved` recommended. Legacy is still the default.
  - **NEW:** "Use StreamOutBehavior.Opportunistic to allow the client to aggressively garbage collect content… helping prevent out‑of‑memory crashes". LowMemory is the default.
  - Streaming is "enabled by default for new places".
  - Source: [Instance streaming](https://create.roblox.com/docs/workspace/streaming)
- **CONFIRMED / NEW: LOD.** `ModelLevelOfDetail` has SLIM ("Scalable Lightweight Interactive Model"), StreamingMesh, Disabled and **Automatic**, which is the "Default behavior, currently equivalent to Disabled". — [ModelLevelOfDetail](https://create.roblox.com/docs/reference/engine/enums/ModelLevelOfDetail)
- **CONFIRMED: lighting technologies.** Voxel, ShadowMap and Future are selectable. **Compatibility**, **Legacy** and **Unified** are "deprecated and cannot be selected in Studio". — [Technology](https://create.roblox.com/docs/reference/engine/enums/Technology)

### Inferences
- For the knowledge base: "around 1,000 draw calls / 1M triangles as an example ceiling on a chosen baseline device; measure on your own device." Treat the community targets (500/500K) as a conservative mobile goal and the 600/650K figure as unconfirmed.
- 4K textures are allowed, but the engine scales them down by device. Keep the size guidance per stud area for memory budgets.

### Gaps
- An official per-mesh triangle cap and an official mobile memory ceiling: NOT IN DOCS (not found in the files checked).

---

## 7. Audio: Audio API objects, upload limits, length/size, licensed music

### Takeaway
The figures are confirmed: **2,000 uploads per 30 days for ID-verified accounts and 100 for unverified**, each file **under 20 MB and 7 minutes**. The 2022 figure of 100/month for verified accounts is outdated. Sound, SoundGroup and SoundEffect are officially "discouraged". The licensing partners (APM, Monstercat, DistroKid) are **not named** in the docs; only "more than 100,000 professionally-produced sound effects and music tracks from top audio and music partners".

### Cited Findings
- **CONFIRMED: upload limits.**
  - "If you're ID verified, you can import 2,000 free audio assets per 30 days; if you're unverified, you can import 100 free audio assets per 30 days. If a daily import limit exists, it's removed and replaced with a simplified monthly limit."
  - Format: "a single track/stream in either .mp3, .ogg, .wav or .flac". "less than 20 MB in size and 7 minutes in duration."
  - Songs on the game details page need an ID-verified uploader, minimum duration/plays/age requirements and acceptance of the Audio Terms.
  - Source: [Audio assets](https://create.roblox.com/docs/audio/assets)
- **CONFIRMED: Audio API.**
  - "Sound, SoundGroup, and SoundEffect objects are now discouraged in favor of the more robust functionality of audio objects."
  - Objects: AudioPlayer, AudioEmitter, AudioListener, AudioDeviceOutput and Wire.
  - **NEW** in the list: `AudioDeviceInput` (a physical microphone), `AudioTextToSpeech` and `AudioSpeechToText`.
  - Sources: [Audio objects](https://create.roblox.com/docs/audio/objects); [Audio](https://create.roblox.com/docs/audio)
- **CONFIRMED (in part): licensed catalog.** "more than 100,000 professionally-produced sound effects and music tracks from top audio and music partners". The partner names APM, Monstercat and DistroKid are NOT IN DOCS. Catalog music is allowed in video thumbnails. — [Audio](https://create.roblox.com/docs/audio); [Thumbnails](https://create.roblox.com/docs/production/publishing/thumbnails)
- **NOT IN DOCS:** the March 22, 2022 privacy date. The Asset Privacy page says audio has "its own creation defaults" and is not affected by the Asset Privacy setting. — [Asset privacy](https://create.roblox.com/docs/projects/assets/privacy)

### Inferences
- New projects should use the wire-based API. With TextToSpeech and SpeechToText, audio objects now also cover accessibility and voice features.

### Gaps
- Licensing partner names and the details of music charts: NOT IN DOCS.

---

## 8. Technical: DataStore and MemoryStore limits, ProcessReceipt, RemoteEvents, Server Authority, Luau const/require, Script Sync, Luau Execution

### Takeaway
**DataStores have both kinds of limits.** There is an experience-wide budget shared with Open Cloud (300 + 40/20/2/40 × CCU) **and** configurable server limits (Standard Read/Write/Remove **60 + numPlayers × 40**, List 5 + numPlayers × 2; Ordered Write/Remove 30 + numPlayers × 5). The old "60 + 10 × players" figure is outdated, but per-server limits have not gone away. Storage is 500 MB + 1 MB × lifetime users.

**MemoryStore** is **CORRECTED** to 64 KB + **1.2 KB** × users of memory and 1000 + 120 × CCU request units per minute.

**ProcessReceipt:** the official page sample is simple and has no PurchaseId tracking. The robust approach (PurchaseId plus session locking) is documented separately.

Server Authority, `const`, require-by-string and Script Sync are confirmed. Luau Execution: 5 minutes and 4 MB per script are confirmed; "10 concurrent tasks" is NOT IN DOCS.

### Cited Findings
**DataStores**
- **CONFIRMED: experience-wide limits.**
  - Standard data stores, "Shared limits (requests per minute)": Get "300 + concurrentUsers × 40"; Set "300 + concurrentUsers × 20"; List "300 + concurrentUsers × 2"; Remove "300 + concurrentUsers × 40". Ordered data stores use the same values.
  - "Game server and Open Cloud **share** a budget; Open Cloud traffic can be throttled by in-experience usage (and vice versa)."
  - Source: [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)
- **CORRECTED / resolves the conflict: server limits still exist.**
  - "Data stores are subject to both **experience and server-level limits**… server-level limits are configurable and meant to be used as a tool by the creator."
  - Standard: Read/Write/Remove "60 + numPlayers × 40", List "5 + numPlayers × 2". Ordered: Write/Remove "30 + numPlayers × 5".
  - "Servers receive a one-time startup burst". Control them with `SetRateLimitForRequestType()` and `GetRequestBudgetForRequestType()`.
  - Source: [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)
- **CONFIRMED: data and metadata limits.**
  - Names, keys and scopes: 50 characters. Value: "4,194,304 per key".
  - Metadata: key 50, value 250, "Key-value pairs 300", and "the total size can't exceed 300 characters". This confirms the "300" figure that was unverified.
  - Queue: "Each queue has a limit of 30 requests" → errors 301–306.
  - Throughput: "25 MB per minute" read and "4 MB per minute" write per key, "rounds throughput up to the next kilobyte".
  - Source: [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)
- **CONFIRMED: storage.** "Total latest version storage limit = 500 MB + 1 MB × lifetime user count", measured on the "compressed size of the latest version of each key". Advice: "avoid pre-compressing it yourself". Data stores deleted through Open Cloud keep counting during a "30-day deletion processing period". — [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)
- **CONFIRMED (version retention was unverified):** "Versioned backups expire 30 days after a new write overwrites them. The latest version never expires." **NEW:** `GetAsync` caches for "four seconds"; cached reads do not count toward server or throughput limits; `DataStoreGetOptions.UseCache = false` reads fresh. — [Versioning, listing, and caching](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching)
- **NEW: write failure semantics.** "A failed write call, such as UpdateAsync(), means the game server did not receive a successful response. It does not always guarantee that the backend write did not occur." — [Error codes and limits](https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits)
- **Official verification pattern (MIT code, quoted in full):**
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
          -- decide based on backend state, not cached state
      end
  end
  ```
  — [Versioning, listing, and caching](https://create.roblox.com/docs/cloud-services/data-stores/versioning-listing-and-caching)
- **CONFIRMED: session locking.** The lock is written atomically into the key's metadata (`LockId` = GUID) inside `UpdateAsync`. The sample routes "every DataStore request… through UpdateAsync". The reference code is "Purchase-Handling" (Creator Store asset 14376223840), with the warning "Don't use this code in your game as-is without extensive testing." — [Implement player data and purchasing systems](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing)

**MemoryStore**
- **CORRECTED: memory quota.** "64 KB + 1.2 KB * [number of users]", applied per game. An "eight days" traceback period applies before the quota is lowered again. — [Memory stores](https://create.roblox.com/docs/cloud-services/memory-stores)
- **NEW: request units.** "1000 + 120 * [number of concurrent users] request units per minute", per game. — [Memory stores](https://create.roblox.com/docs/cloud-services/memory-stores)
- **CONFIRMED: other memory store limits.**
  - Per sorted map or queue: "1,000,000" items and "100 MB".
  - Per partition: about "30,000 request units per minute".
  - Hash maps: "5,000 write request units per minute and 15,000 read" per key.
  - "the default expiration time is 45 days".
  - Source: [Memory stores](https://create.roblox.com/docs/cloud-services/memory-stores)

**ProcessReceipt and purchases**
- **Official ProcessReceipt sample, core quoted (MIT):**
  ```lua
  local function processReceipt(receiptInfo)
      local userId = receiptInfo.PlayerId
      local productId = receiptInfo.ProductId
      local player = Players:GetPlayerByUserId(userId)
      if player then
          local handler = productFunctions[productId]
          local success, result = pcall(handler, receiptInfo, player)
          if success then
              -- The user has received their items
              return Enum.ProductPurchaseDecision.PurchaseGranted
          else
              warn("Failed to process receipt:", receiptInfo, result)
          end
      end
      -- Returns "NotProcessedYet" and tries again next time the user joins the game
      return Enum.ProductPurchaseDecision.NotProcessedYet
  end
  -- This can only be done once by one server-side script
  MarketplaceService.ProcessReceipt = processReceipt
  ```
  The page also warns: "The functions for handling each product ID must return `true` for the transaction to be successful." It notes that `receiptInfo` contains "the exact Robux amount the user paid… even if you're running a price optimization test". — [Developer products](https://create.roblox.com/docs/production/monetization/developer-products)
- **NEW: official ProcessReceipt guarantees and limits (API reference).**
  - The callback runs for unresolved purchases on purchase completion, when a purchase prompt appears and when a user joins.
  - "ProcessReceipt has no time-based retry mechanism… only called again on the same server if: The user successfully initiates another developer product purchase. The user re-joins any server".
  - "no timeout for yielded callbacks".
  - "If you don't implement a ProcessReceipt callback, your receipts will be auto-acknowledged."
  - "callbacks are called in a non-deterministic order".
  - "might run on two different servers at the same time".
  - "might still fail to be recorded on the backend, even if it returns… PurchaseGranted".
  - "Unresolved developer product purchases are not removed or refunded after the escrow period expires."
  - `receiptInfo` fields: PurchaseId, PlayerId, ProductId, PlaceIdWherePurchased, CurrencySpent, CurrencyType, ProductPurchaseChannel.
  - Source: [MarketplaceService](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService)
- **NEW: `BindReceiptHandler`.** A "newer alternative that processes developer product receipts (and Robux transfer receipts)". It supports filtered (by product IDs) and catch-all handlers, which take precedence over `ProcessReceipt`, so you can migrate incrementally. Handlers return `Enum.ReceiptDecision.Processed` / `NotProcessedYet`. — [MarketplaceService](https://create.roblox.com/docs/reference/engine/classes/MarketplaceService)
- **CONFIRMED (the community pattern is official): idempotent handling.**
  - "1. Verify the PurchaseId has not already been recorded as handled. 2. Award the purchase in the player's in-memory player data. 3. Record the PurchaseId as handled… 4. Write the player's in-memory player data to the DataStore."
  - Return PurchaseGranted only if the save succeeds, otherwise NotProcessedYet.
  - "If it is recorded as processed, but _not_ reflected in the DataStore, return NotProcessedYet."
  - Source: [Implement player data and purchasing systems](https://create.roblox.com/docs/cloud-services/data-stores/player-data-purchasing)
- **CONFIRMED: read prices dynamically.** Use `GetProductInfoAsync` / `GetDeveloperProductsAsync`. Plus discounts are exposed through `PriceDiscountDetails` and `UserBasePriceInRobux`. — [Roblox Plus](https://create.roblox.com/docs/production/monetization/roblox-plus)

**RemoteEvents**
- **CONFIRMED: rate and size limits.**
  - "RemoteEvents and UnreliableRemoteEvents both have a limit of approximately 500 requests per second, per client. This limit is **shared among all remote events of the same type**."
  - "Events with payloads larger than 1000 bytes are dropped" for UnreliableRemoteEvent.
  - **NEW:** excess events "are processed later instead of dropping them, and they keep their order". Messages that arrive with no handler connected are queued, within limits on count and memory.
  - Sources: [UnreliableRemoteEvent](https://create.roblox.com/docs/reference/engine/classes/UnreliableRemoteEvent); [RemoteEvent](https://create.roblox.com/docs/reference/engine/classes/RemoteEvent); [Remote events and callbacks](https://create.roblox.com/docs/scripting/events/remote)

**Server Authority**
- **CONFIRMED + NEW: setup.**
  - "Workspace.AuthorityMode must be Server (setting this automatically sets the following five)": NextGenerationReplication enabled; PlayerScriptsUseInputActionSystem enabled; SignalBehavior Deferred; UseFixedSimulation enabled; StreamingEnabled enabled.
  - Core logic goes in `RunService:BindToSimulation()` inside a ModuleScript loaded on both client and server.
  - Prediction can be controlled with `RunService:SetPredictionMode()`.
  - Inside the simulation `time()` is synchronized; `tick()`, `os.time()` and `os.clock()` are not, and they do not roll back.
  - "Mispredictions are a **normal and expected** part".
  - The docs have no beta label for it.
  - Source: [Server authority model](https://create.roblox.com/docs/projects/server-authority)

**Luau**
- **CONFIRMED: `const` is documented.**
  - "use `const` instead of `local`. Trying to reassign a `const` variable causes an error, including through a compound assignment operator such as `+=`."
  - It works for functions (`const function`). "const makes the variable itself immutable, not the value", so use `table.freeze()` for contents.
  - "`const` is contextual… existing code that uses `const` as a variable name still works."
  - Source: [Variables](https://create.roblox.com/docs/luau/variables)
- **CONFIRMED: require-by-string.** "Paths with the `./` prefix begin resolution at `script.Parent`… `../` … `script.Parent.Parent`… `@self/` … `script`… `@game/` … `game`." It is "non-blocking: it does not implicitly wait for a ModuleScript to be created." The docs also show `require("@rbx/AvatarAbilities")` (Character Controller Library). — [LuaGlobals](https://create.roblox.com/docs/reference/engine/globals/LuaGlobals); [Character controller library](https://create.roblox.com/docs/characters/character-controller-library)

**Script Sync**
- **CONFIRMED + NEW: Script Sync.**
  - Limits: "up to 10,000 scripts per top-level synced instance and up to 128 top-level synced instances".
  - Conflict dialog "Keep Studio vs. Keep Disk"; works with Team Create (icons and automatic suffixes).
  - It syncs only Script, LocalScript, ModuleScript and Folder; attributes and tags are ignored ("can lead to data loss").
  - "It is currently not possible to control Roblox Studio's debugger from an external development environment."
  - For whole-project version control, "third-party tools like Rojo are a better choice".
  - **Precision on the "no sourcemap" community claim:** the docs recommend luau-lsp together with the "Luau Language Server Companion" Studio plugin, which "provides this data" (the data model hierarchy).
  - Source: [Script Sync](https://create.roblox.com/docs/scripting/sync)

**Luau Execution API and Studio MCP**
- **CONFIRMED (in part): Luau Execution API.**
  - "Scripts can be up to 4 MB in size and run for up to 5 minutes"; timeout "Defaults to 5 minutes".
  - Return values must be at most 4 MB.
  - Binary input is at most 100 MiB and valid for 15 minutes. Binary output is at most 256 MiB.
  - "physics simulation does not run. Server and local scripts within the place also do not automatically run"; data model changes are not persisted, but DataStore APIs affect real data.
  - **"10 concurrent tasks per place": NOT IN DOCS** (not found in the local OpenAPI file).
  - Source: [Luau Execution (Open Cloud)](https://create.roblox.com/docs/cloud/features/luau-execution), read from `reference/cloud/cloud.docs.json`
- **CONFIRMED: Studio MCP.** "`execute_luau` — Runs Luau code in Studio… Requires specifying a `datamodel_type` (Edit, Client, or Server)." — [Studio MCP](https://create.roblox.com/docs/studio/mcp)

### Inferences
- Plan DataStore budgets on two levels: the experience-wide pool and the per-server pool. Backfills through Open Cloud should be rate-limited on the client side, as the docs recommend.
- The official ProcessReceipt sample on the developer-products page is a teaching sample. It checks only `success` from `pcall`, not `result == true`, so a handler that returns `nil` would still produce `PurchaseGranted`. It also does not save anything. For production, use the PurchaseId and session-lock pattern from the player-data-purchasing page. This is my own reading of the code, not a statement in the docs.

### Gaps
- Luau Execution concurrency limit and beta status: NOT IN DOCS.
- ProfileStore and community tooling: not covered by the docs (outside scope).

---

## 9. Safety and chat: TextChatService, GetChatGroupsAsync, age groups, PolicyService, links

### Takeaway
`GetChatGroupsAsync` is confirmed. The six age bands (under 9, 9–12, …) are **not in the Creator Docs**; they only link to the Help Center. There are new official rules for preset chat systems and Quick Words, which allow communication across age groups but only for gameplay coordination.

Two corrections:
- `AllowedExternalLinkReferences` is officially legacy and always empty.
- **Social media links may not be shared inside the game** at all, only on the game details page, and only users age-verified 16+ can see them.

### Cited Findings
- **CONFIRMED: `TextChatService:GetChatGroupsAsync`.**
  - "Returns a sorted array of arrays of chat group IDs… If two or more players share the same chat group ID, those players are able to synchronously text chat… based on their age-check status and chat settings."
  - Server-only, for matchmaking and teleports; "more efficient than calling `CanUsersChatAsync()` pairwise… N^2".
  - IDs are unique per universe, change over time and must not be stored after the user leaves.
  - Requires "Chat & Voice Groups APIs" under Experience Settings ⟩ Communication. In Studio it works only in Team Test.
  - Source: [TextChatService](https://create.roblox.com/docs/reference/engine/classes/TextChatService)
- **NOT IN DOCS: the age bands.** The docs refer to "similar age to chat" and link to the Help Center. — [Preset system guidelines](https://create.roblox.com/docs/chat/preset-system-guidelines)
- **NEW: preset systems.**
  - Allowed: "If the system… is purely to help players communicate in-game actions, confirmations, or basic reactions, you can use a preset system that lets users send presets to each other regardless of age or age check status."
  - Not allowed: "Enable back-and-forth dialogue across age groups", "Alphabet wheels or number-based encoding", "'Hi!' 'Hello!' 'How are you?'".
  - Source: [Preset system guidelines](https://create.roblox.com/docs/chat/preset-system-guidelines)
- **NEW: Quick Words.** "Add up to three custom categories, with three to ten Quick Words in each category. Each Quick Word must be fewer than 25 characters", entered in English only and translated automatically, with a review before going live. — [Quick Words](https://create.roblox.com/docs/chat/quick-words)
- **CONFIRMED / CORRECTED: PolicyService fields.**
  - `AreAdsAllowed`, `ArePaidRandomItemsRestricted`, `IsContentSharingAllowed`, `IsEligibleToPurchaseCommerceProduct`, `IsEligibleToPurchaseSubscription`, `IsPaidItemTradingAllowed`, `IsPhotoToAvatarAllowed`, `IsSubjectToChinaPolicies`, `IsEndlessContentLoadAllowed` and `IsEndlessContentAutoplayAllowed`.
  - **`AllowedExternalLinkReferences`: "This is a legacy field. It always returns an empty array."** This confirms the community report.
  - This answers the earlier gap about AreAdsAllowed and IsEligibleToPurchaseSubscription.
  - Source: [PolicyService](https://create.roblox.com/docs/reference/engine/classes/PolicyService)
- **CORRECTED: social and off-platform links.**
  - "Roblox's Community Standards only permit you to share social media links on your game's main details page. You **cannot** share social media links directly within a game." Allowed in-game text is a pointer such as "Check out our social media links on our game's page".
  - "up to three links". Adding them requires age verification as 16+, and "Users who are under 16 years old or who have not verified their age **cannot** view social media links."
  - If every 16+-verified collaborator leaves a group, its links are deleted after 90 days.
  - Source: [Social media links](https://create.roblox.com/docs/production/promotion/social-media-links)

### Inferences
- Social systems without free text (trade UIs, emotes, Quick Words, shared events) are officially the way to support interaction across age groups. Free-form systems must respect age checks and age similarity.
- Off-platform links in the game UI, such as a Discord button, are against the docs even with a PolicyService check. Only an in-game pointer to the details page is allowed.

### Gaps
- Voice chat eligibility details: not checked in voice-chat.md (time constraint). The age bands themselves: NOT IN DOCS.
