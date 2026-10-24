# Craft-Level Design for Roblox Games: UI/UX, Level/Map Design, Art Direction, Thumbnails/Icons, Sound (2024–2026)

Research method note: WebFetch failed (DNS error on devforum.roblox.com), so every finding comes from WebSearch result snippets of the cited pages, not from reading full pages. The shared web-search budget ran out after about 33 queries. Topics that never got a search are listed under Gaps. Labels: **[Official]** means Roblox docs, a Roblox staff DevForum post or the Roblox newsroom. **[Community]** means DevForum community posts. **[3rd-party]** means blogs or vendors.

## UI/UX: official building blocks, cross-platform input, touch targets, mobile share, styles, animation, mistakes, accessibility

### Takeaway
Roblox's official guidance is: design mobile-first, size with Scale rather than Offset, keep interactive UI inside `ScreenInsets = CoreUISafeInsets`, build layouts with UIListLayout flex and UIFlexItem, and centralize looks with the StyleSheet/token system. Input should go through the Input Action System so one action can bind to keyboard, gamepad and touch. In 2024 about 80% of DAU played on mobile (official annual report). Players can now set a preferred text size and reduced motion, and UI has to respect both.

### Cited Findings
**Safe areas / ScreenGui (Official)**
- `ScreenGui.ScreenInsets` options: **CoreUISafeInsets** (default) keeps UI clear of device cutouts such as the notch and of Roblox core UI such as the top-bar buttons. Docs recommend it for interactive or important UI. **DeviceSafeInsets** avoids cutouts only. **TopbarSafeInsets** is a dynamic area inside the top bar whose size comes from `GuiService.TopbarInset`. **None** is for non-interactive content like background images only — [ScreenInsets enum](https://create.roblox.com/docs/reference/engine/enums/ScreenInsets.md); [ScreenGui](https://create.roblox.com/docs/reference/engine/classes/ScreenGui.md)
- Legacy `IgnoreGuiInset` defaults to false (which means CoreUISafeInsets). Setting it to true while ScreenInsets is CoreUISafeInsets switches ScreenInsets to DeviceSafeInsets. `ClipToDeviceSafeArea` is ignored when ScreenInsets = None — [ScreenGui docs](https://create.roblox.com/docs/reference/engine/classes/ScreenGui#ClipToDeviceSafeArea)
- Minor doc inconsistency: the ScreenGui reference says TopbarSafeInsets runs between the left-most Roblox controls and the safe-area edge, while the on-screen containers guide words it differently — [On-screen containers](https://create.roblox.com/docs/en-us/ui/on-screen-containers.md)

**Roblox Engine UI team guide, "Designing UI – Tips and Best Practices" (Official, Roblox Staff, DevForum, ~mid-2024)**
- Preview on preset phones, tablets, consoles and HD monitors with the Device Emulator.
- Design **mobile first**, because phones have the least screen space.
- Prefer **Scale over Offset** (Offset is pixels; Scale is a percentage of the parent).
- Understand AnchorPoint and Position, and use Offset sparingly.
- Plan placement around platform UI: the top bar, chat, leaderboard and mobile controls — [DevForum staff post](https://devforum.roblox.com/t/designing-ui-tips-and-best-practices/3074034)
- A companion staff post recommends a reusable component library (buttons, scrolling frames, text) for team consistency, plus integration with external design tools — [Integrating External Applications into your UI Design](https://devforum.roblox.com/t/integrating-external-applications-into-your-ui-design/3266163)
- Community: use AnchorPoint 0.5, 0.5 so positions scale across aspect ratios. TextScaled is not always best; Offset sizing plus TextSize is an alternative — [The Ultimate UI Design Guide (community)](https://devforum.roblox.com/t/the-ultimate-ui-design-guide/1236916); [Guide to UI Designing (community)](https://devforum.roblox.com/t/the-guide-to-ui-designing/606984)

**Layouts: flex (Official)**
- `UIListLayout.HorizontalFlex` and `VerticalFlex` distribute leftover space along the fill direction. Example: a tab bar that fills evenly regardless of tab count. `Wraps` lets children wrap to a new row or column. `SortOrder` uses LayoutOrder or Name — [List and flex layouts](https://create.roblox.com/docs/de-de/ui/list-flex-layouts)
- `UIFlexItem` (a child of a single element) sets per-item `FlexMode`: Fill, Grow, Shrink or Custom. Example: a slider with fixed end labels and a bar that flexes between them — [List and flex layouts](https://create.roblox.com/docs/vi-vn/ui/list-flex-layouts)

**Styling system (Official)**
- `StyleSheet` holds `StyleRule`s, which apply to every instance matching a Selector (class, name or hierarchy). Tokens are attributes on a token StyleSheet, comparable to CSS variables. Themes are swappable token sets (for example light and dark) and must share the same token set. `StyleDerive` inherits tokens or themes, and `StyleLink` attaches a sheet to a UI tree, with only one StyleSheet per tree. Style queries apply styles conditionally on context. There is a visual **Style Editor** — [UI styling](https://create.roblox.com/docs/en-us/ui/styling); [Style Editor](https://create.roblox.com/docs/ui/styling/editor)

**UIDragDetector (Official)**
- Adding `UIDragDetector` as a direct child makes any GuiObject draggable. `DragStyle` options include TranslatePlane and Rotate. Movement is bounded by `MinDragTranslation`/`MaxDragTranslation`, plus `BoundingUI`/`BoundingBehavior` to keep the object inside a UI region — [UI drag detectors](https://create.roblox.com/docs/de-de/ui/ui-drag-detectors); [API dump (robloxapi)](https://robloxapi.github.io/ref-temp/class/UIDragDetector.html)

**Text and rich text (Official)**
- Rich text works on TextLabel, TextButton and TextBox when the `RichText` property is enabled. It uses HTML-style nested tags that must close in reverse order: bold, italic, underline, strikethrough, `<font color/size/face/family/weight>` and `<stroke>`. Unrecognized tags are silently ignored (per the older beta post) — [Rich text markup](https://create.roblox.com/docs/en-us/ui/rich-text); [RichText DevForum](https://devforum.roblox.com/t/richtext-textscaled-support-added/634167)

**Localization (Official)**
- `LocalizationService:GetTranslatorForPlayerAsync` yields until the cloud localization table loads and should be wrapped in pcall. The reference page now marks it deprecated. The non-yielding alternative is `GetTranslatorForPlayer`. `Translator:Translate(context, text)` and `Translator:FormatByKey(key, args)` exist, and `LocaleId` defaults to "en-us" — [GetTranslatorForPlayerAsync](https://create.roblox.com/docs/reference/engine/classes/LocalizationService/GetTranslatorForPlayerAsync.html); [Translator](https://create.roblox.com/docs/en-us/reference/engine/classes/Translator); [Localize with scripting](https://create.roblox.com/docs/en-us/production/localization/localize-with-scripting.md)
- RDC 2025 announced new language tools, including **real-time translation** — [RDC25 What we announced](https://devforum.roblox.com/t/rdc25-what-we-announced/3920245); [Roblox newsroom RDC 2025](https://about.roblox.com/newsroom/2025/09/roblox-rdc-2025)

**Cross-platform input (Official)**
- **Input Action System**: `InputContext` groups actions (for example a PlayContext for character controls and a NavContext for menus) and has an `Enabled` toggle. Priority plus `Sink` decides which context consumes input. `InputAction` has a Type (Bool by default, also Direction1D/Direction2D). `InputBinding` maps an action to hardware. The documented sprint example binds LeftShift for keyboard, ButtonY for gamepad and an on-screen SprintButton for touch. Test with Studio's Controller Emulator — [Input Action System](https://create.roblox.com/docs/en-us/input/input-action-system)
- **Gamepad UI navigation** via GuiService: `SelectedObject` is the GuiObject the gamepad navigator focuses on and may reset to nil if off-screen. `AutoSelectGuiEnabled` controls whether the Select button picks a GUI automatically; if it is off, set SelectedObject manually. There are also `GuiNavigationEnabled` and `CoreGuiNavigationEnabled` — [GuiService](https://create.roblox.com/docs/en-us/reference/engine/classes/GuiService)
- **Console guidelines**: assume players sit **8–10 ft** from the TV. Use relative sizes, develop for lower resolutions first, use `UISizeConstraint`, and check `GuiService.ViewportDisplaySize` (TVs fall in the "Large" category). Keep key UI in TV-safe areas because some TVs overscan. Navigation is sequential, so key actions should be only a few moves away. Disable the chat window on console. Use ScrollingFrame to reduce clutter. Button icons must match the player's device. Content maturity info is required for console release — [Console guidelines](https://create.roblox.com/docs/production/publishing/console-guidelines)
- **VR guidelines**: Quest has an Auto Quality Mode that targets a minimum of **72 FPS**. Players choose comfort presets (Comfort, Default, Expert, Custom), with options such as vignette, stepped rotation and a fixed 3rd-person camera. `VRService:GetUserCFrame(Enum.UserCFrame.LeftHand)` and the `UserCFrameChanged` event are available — [VR guidelines](https://create.roblox.com/docs/production/publishing/vr-guidelines); [VRService](https://create.roblox.com/docs/reference/engine/classes/VRService). Alpha-era advice (old, possibly outdated): minimize 2D ScreenGui in VR and prefer SurfaceGui and BillboardGui — [VR developer alpha](https://devforum.roblox.com/t/vr-developer-alpha/22144)

**Touch target sizes (no official Roblox number found)**
- Community and 3rd-party guidance: at least **44×44 px** for tappable elements (Apple HIG), described as roughly 0.06 scale on a 1080p screen. Enforce it with a UISizeConstraint min of 44 px, or give small icons an invisible larger hit area — [creation.dev](https://www.creation.dev/blog/roblox-ui-design-best-practices); [game-dev-skills ui-ux](https://skills.sh/taozhuo/game-dev-skills/ui-ux)
- Platform standards: Apple 44 pt, Android **48 dp** — [W3C mobile a11y wiki](https://www.w3.org/WAI/GL/mobile-a11y-tf/wiki/M2); [Deque touch target](https://docs.deque.com/devtools-mobile/2025.7.2/en/android-touch-target-size)

**Mobile share of players**
- 2024 (Roblox annual report, via PocketGamer.biz): average DAU of 82.9M, of which **80% were on mobile, 17% on PC and 3% on console**. Mobile still produced only **46% of Robux revenue** through the App Store and Google Play — [PocketGamer.biz](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue)
- A 3rd-party Feb 2026 post claims ">60% of 144M DAU" are on mobile. This conflicts with the official 80% figure and should be treated cautiously — [RoLearn](https://rolearn.dev/insights/mobile-first-design-roblox-engagement)

**Popular UI styles 2025–2026 (community/3rd-party only)**
- The breakout 2025 hits Grow a Garden (released 26 Mar 2025) and Steal a Brainrot are idle-style games driven by "admin abuse" events — [Wikipedia Grow a Garden](https://en.wikipedia.org/wiki/Grow_a_Garden); [Wikipedia Steal a Brainrot](https://en.wikipedia.org/wiki/Steal_a_Brainrot)
- Developers ask how to build the "studded UI" of Grow a Garden and Plants vs Brainrots. The Grow a Garden dialog uses a drop shadow behind text — [DevForum: stud UI](https://devforum.roblox.com/t/how-do-you-make-stud-ui/4020877); [DevForum: GaG dialog UI](https://devforum.roblox.com/t/grow-a-garden-dialog-ui/3736124)
- A commercial "Grow a UI Pack" lists the standard frame set: Seed Shop, Confirmation, Codes, Limited Shop, Pet/Cosmetic Shop, HUD, Inventory, Hotbar, Notification, Quests, Settings — [BuiltByBit](https://builtbybit.com/resources/grow-a-ui-pack.79298/). A "Cartoony UI Pack" markets clean, colorful simulator and tycoon styling with tween and hover/click effects — [BuiltByBit](https://builtbybit.com/resources/cartoony-ui-pack-pro-ui-system.107727/)

**UI animation / juice (Official technique)**
- `TweenService:Create(obj, TweenInfo, goals):Play()`. Chain tweens with `.Completed`. Example uses are enlarging a button on selection and sliding menus in from screen edges. Style transitions work similarly to CSS transitions — [UI animation/tweens](https://create.roblox.com/docs/en-us/ui/animation)

**Common UI mistakes (3rd-party)**
- Desktop-style HUDs (health, mana, minimap, inventory, chat, quest tracker) cover half of a phone screen. Keep the 2–3 essential elements visible and put the rest behind expandable menus. Top mobile games use **1–3 action buttons plus a virtual joystick**. Keep the screen center free of persistent elements. Hover-only tooltips fail on touch, so provide tap, long-press or info-button alternatives — [creation.dev](https://www.creation.dev/blog/roblox-ui-design-best-practices); [RoLearn](https://rolearn.dev/insights/mobile-first-design-roblox-engagement)

**Accessibility (Official)**
- **Preferred Text Size** maps to `GuiService.PreferredTextSize` (default Medium, then Large, Larger, Largest). TextScaled labels ignore it. AutomaticSize elements grow with it, TextWrapped text adds lines, and it can be clamped with `UITextSizeConstraint`. It was announced as a Studio Beta on 25 Aug 2025 — [Accessibility guidelines](https://create.roblox.com/docs/production/publishing/accessibility); [Text Scaling Studio Beta](https://devforum.roblox.com/t/introducing-text-scaling-setting-studio-beta/3136967); [Can I Play That](https://caniplaythat.com/2025/08/27/roblox-introduces-global-text-size-accessibility-setting/)
- Developer pushback: a 31 Aug 2025 thread argued for reverting the feature because custom UIs break above Medium — [DevForum thread](https://devforum.roblox.com/t/preferred-text-scaling-needs-to-be-reverted-abrupt-release-with-no-concerns-addressed-are-disruptive/3911199)
- **Reduced Motion** maps to `GuiService.ReducedMotionEnabled`. Official pattern: set tween Time to 0, fade instead of fly-in, and stop or replace looping motion — [GuiService.ReducedMotionEnabled](https://create.roblox.com/docs/reference/engine/classes/GuiService#ReducedMotionEnabled); [Introducing Accessibility Settings](https://devforum.roblox.com/t/introducing-accessibility-settings/2723187)
- The UI Navigation toggle uses the backslash key to enter and exit UI navigation — [Roblox Help](https://en.help.roblox.com/hc/en-us/articles/203314230-In-experience-Settings-and-Help)

### Inferences
- With about 80% of DAU on mobile, phones (small screens, notch, touch thumbstick) are the main design target. Desktop and console are adaptations of the phone layout.
- To support Preferred Text Size, prefer AutomaticSize containers and TextWrapped over TextScaled, and clamp with UITextSizeConstraint. Otherwise text either ignores the setting (TextScaled) or breaks the layout.
- The StyleSheet/token system lets one theme drive the "chunky cartoony" look across all panels, which suits the studded/outlined style common in 2025 hits.

### Gaps
- No official Roblox touch-target minimum was found. 44 px and 48 dp are platform or community standards.
- No official 2025/2026 device split was found. The latest official number is the 2024 figure of 80% mobile.
- Not verified because the search budget ran out: the date of the Roblox top-bar redesign (TopbarInset), and Builder Sans as a font name.
- The full text of the Engine UI staff post could not be fetched, so any pixel numbers in it are unknown.
- No rigorous, screenshot-based teardown of top-game HUDs was found.

## Thumbnails & icons: official guidance, personalization/testing, top-game traits, CTR

### Takeaway
Official specs: icons are square, at least 512×512, and shown at about 150×150. Thumbnails are 16:9, ideally 1920×1080. Thumbnail Personalization uses a multi-armed bandit across up to 5 active thumbnails and reported an average +8.5% qualified play-through rate (some games +50%). A 2026 Open Cloud API lets you drive it programmatically.

### Cited Findings
- **Icon (Official):** square, at least **512×512**, previewed at small sizes such as **150×150**. Use unique, relevant imagery, with color and contrast expressing the theme — [Experience icons](https://create.roblox.com/docs/production/publishing/experience-icons.md); [Game icons](https://create.roblox.com/docs/production/promotion/game-icons)
- **Thumbnail (Official):** 16:9, ideally **1920×1080**. Formats: .jpg, .gif, .png, .tga, .bmp. Displayed thumbnails are stretched to 16:9 whatever the upload ratio. Show what players will actually find; ambiguous imagery confuses. Video thumbnails must be authentic in-game footage with no real-life footage of people or places. Video thumbnails are not supported on Xbox, PlayStation or VR — [Thumbnails](https://create.roblox.com/docs/production/publishing/thumbnails); [Promotional thumbnails](https://create.roblox.com/docs/production/promotion/promotional-thumbnails)
- Thumbnails are managed under the "Home Page" and "Experience Detail Page" tabs of Creator Dashboard > Thumbnails — [Thumbnails docs](https://create.roblox.com/docs/en-us/production/publishing/thumbnails)
- **Thumbnail Personalization (Official):** set up to **5** thumbnails active, and personalization starts at **2 or more** (with 1, everyone sees it). It uses a multi-armed bandit rather than an A/B test. During testing, games averaged **+8.5% qualified play-through rate**, some **+50%** — [Thumbnails docs (GitHub)](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/publishing/thumbnails.md); [Live now announcement](https://devforum.roblox.com/t/live-now-personalize-your-thumbnails-to-attract-more-users/3257233); [Get your thumbnails ready](https://devforum.roblox.com/t/get-your-thumbnails-ready-for-thumbnail-personalization/3226599); [GamesBeat](https://gamesbeat.com/roblox-will-let-game-devs-personalize-thumbnails-to-attract-more-players/)
- Launch timing: Roblox tweeted about it on ~13 Nov 2024 — [Roblox on X](https://x.com/Roblox/status/1856760513038110792). One snippet suggested a Feb 2025 date, so the sources conflict.
- **July 2025 update (Official):** new test thumbnails no longer reset traffic to an even split. Most traffic stays on the existing winner while new thumbnails are tested — [Thumbnail personalization now remembers winning thumbnails](https://devforum.roblox.com/t/thumbnail-personalization-now-remembers-your-existing-winning-thumbnails/3793665)
- **Aug 2026 (Official):** new Open Cloud APIs for analytics, events, experiments and **thumbnail personalization** — [DevForum announcement](https://devforum.roblox.com/t/new-opencloud-apis-for-analytics-events-experiments-and-thumbnail-personalization/4828676). A 3rd-party write-up names the scope `universe.thumbnail:write` and warns that a write without the right scope can return success without applying, so read back to verify — [ZehnStudio99](https://zehn-studio26.com/news/experiment-targeting-and-analytics-apis/)
- A DevForum announcement titled "**Homepage Recommendation Eligibility Now Requires a Custom Thumbnail**" exists in search results ([link](https://devforum.roblox.com/t/homepage-recommendation-eligibility-now-requires-a-custom-thumbnail/4945086)), but its content could not be retrieved or confirmed.
- **3rd-party specs and tips:** up to 10 thumbnails per experience. Minimum thumbnail 768×432. Design the icon at 1024×1024 and export at 512. Keep text and faces off the bottom edge where metadata overlays. Game-pass, badge and dev-product icons are also 512×512 (badges display as circles). File-size limits conflict (3 MB vs 8 MB) — [vizzbees](https://vizzbees.com/blog/roblox-thumbnail-size-guide); [DEV Community cheat sheet](https://dev.to/heivps_38dd9f177fe982fa93/roblox-image-sizes-in-2026-thumbnails-icons-badges-and-game-passes-cheat-sheet-4fal); [generalistprogrammer](https://generalistprogrammer.com/tutorials/how-to-make-a-roblox-game-icon)
- **What top icons share (3rd-party generalizations):** a single high-quality render of a character or recognizable item as the focal point. Bright, high-contrast colors that stand out on Roblox's dark theme. Minimal or no text, at most a few large words legible at 150×150. Pass a "squint/postage-stamp" test — [generalistprogrammer](https://generalistprogrammer.com/tutorials/how-to-make-a-roblox-game-icon); [axefm](https://axefm.co.uk/reads/2026/03/30/how-to-create-roblox-game-icons-that-attract-players.html); [obby.fun](https://www.obby.fun/blog/roblox-game-icon-thumbnail-maker)
- The widely repeated claim that "good thumbnails raise CTR by up to 40%" is attributed to Roblox internal data, but appears only on low-quality mirror sites. It is **unverified**.

### Inferences
- Treat the icon as a 150 px asset: one focal subject, a face or emotion, saturated contrast against dark UI, and no small text. Use thumbnails to carry the gameplay context.
- Keep 3–5 active thumbnails at all times and rotate seasonal or update variants in. Since July 2025, adding a test no longer costs the winner's traffic.

### Gaps
- No official Roblox CTR benchmarks were found. Roblox reports "qualified play-through rate", not CTR.
- The official icon page's full best-practice text and the custom-thumbnail eligibility rule were not retrieved.
- No measured study of top-100 icon traits was found.

## Level/map design & art direction: environment, lighting, streaming, LOD, performance budgets, greyboxing, onboarding, AI tools, materials

### Takeaway
Official building blocks: greybox first, with lanes and doorways at least 10 studs wide and walls at least 10 studs tall for the default character. Use instance streaming with the defaults (MinRadius 64, TargetRadius 1024, `ModelStreamingBehavior.Improved`). Use SLIM or StreamingMesh model LOD and RenderFidelity Automatic. Keep textures ≤1024² and scaled to object size. Budget draw calls and triangles against a baseline mobile device. Cube 3D (Mar 2025) and Assistant with MCP (RDC 2025) are the official AI building tools.

### Cited Findings
**Greyboxing / spawn / lanes (Official tutorials)**
- Greyboxing means building the level with simple shapes before scripting or final art, so gameplay and layout can be tested cheaply — [Greybox a playable area](https://create.roblox.com/docs/tutorials/curriculums/core/building/greybox-a-playable-area); [Greybox your environment](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment)
- Laser-tag sample layout: **2 spawn zones, 3 primary lanes and 5 cross lanes**, mirrored across the midline. "Combat pockets" segment the distance from spawns. Cross lanes help players learn the map quickly. Doorways and hallways are **at least 10 studs wide** and walls **at least 10 studs tall**, so two players can pass, the default **5-stud jump** cannot clear walls, and the camera stays clear — [Greybox a playable area](https://create.roblox.com/docs/en-us/tutorials/curriculums/core/building/greybox-a-playable-area)
- Platforming sample (Island Jump): use flat cylinder landing surfaces, and increase the height difference between platforms gradually to drive progression — [Greybox a playable area](https://create.roblox.com/docs/tutorials/core/building/greybox-a-playable-area)

**Onboarding (Official)**
- The FTUE is the first few minutes of play and introduces the game, interface and mechanics. It is measured with D1 retention and a step-by-step player funnel, and drop-off steps are A/B tested with Experiments (for example a shorter dialogue vs a guided arrow). Three practices: **teach the essentials, get to the fun quickly, leave players wanting more** — [Onboarding](https://create.roblox.com/docs/en-us/production/game-design/onboarding)

**Lighting (Official and community)**
- `Lighting.Technology`: **Voxel** (4×4×4 voxel light grid), **ShadowMap** (sun or directional shadows), **Future** (highest fidelity). **Compatibility** is deprecated; use Voxel plus ColorGrading to approximate it — [Technology enum](https://create.roblox.com/docs/reference/engine/enums/Technology.md)
- Devices without Future support fall back to ShadowMap, then Voxel. Future's per-pixel light distance depends on the quality level (2020 staff post) — [Future is Bright Phase 3](https://devforum.roblox.com/t/future-is-bright-phase-3-released/878634)
- Shadow cost: spot shadows are cheapest, then surface lights, with point lights the most expensive. Wide spot angles approach point cost — [Future vs ShadowMap thread](https://devforum.roblox.com/t/future-vs-shadowmap/658587) (community)

**Atmosphere (Official)**
- `Atmosphere.Density` is the particle amount and obscures distant objects and terrain, but not the skybox. `Haze` gives a visible haze toward the horizon. `Glare` gives a sun glow and needs Haze > 0. `Decay` is the hue away from the sun and needs Haze and Glare > 0 — [Atmospheric effects](https://create.roblox.com/docs/en-us/environment/atmosphere); [Atmosphere class](https://create.roblox.com/docs/en-us/reference/engine/classes/Atmosphere)

**Streaming (Official)**
- `StreamingMinRadius` defaults to **64** (highest-priority radius; the default maximizes scale-down on low-end devices). `StreamingTargetRadius` defaults to **1024** (max stream-in distance; smaller values reduce server load but shorten full-detail view). `Workspace.ModelStreamingBehavior` is recommended at **Improved**, under which Nonatomic models are excluded from initial replication — [Instance streaming](https://create.roblox.com/docs/en-us/workspace/streaming); [Streaming techniques](https://create.roblox.com/docs/en-us/workspace/streaming/techniques.md)

**LOD (Official and community)**
- `Model.LevelOfDetail` (`ModelLevelOfDetail` enum): **StreamingMesh** renders a coarse, untextured "imposter" mesh outside the streaming radius. **SLIM** renders a composite of child parts at progressively lower resolution and gives much better visual quality than StreamingMesh. **Disabled** shows no LOD mesh — [ModelLevelOfDetail enum](https://create.roblox.com/docs/en-us/reference/engine/enums/ModelLevelOfDetail.md)
- Meshes need `MeshPart.RenderFidelity = Automatic` for distance LOD (community) — [DevForum RenderFidelity](https://devforum.roblox.com/t/more-renderfidelity-options/460741). The 3rd-party claim that Automatic switches at <250, 250–500 and >500 studs is not officially confirmed — [nilo.io](https://nilo.io/articles/advanced-roblox-custom-meshes)

**Performance budgets (Official, with conflicting revisions)**
- "Design for performance": mobile devices have tight memory limits and can crash with out-of-memory errors, and Roblox cannot use all of a device's memory. Pick a **baseline device** and test on it throughout development. The Studio emulator is **not accurate for memory** because it runs server and client together. Enable streaming to control memory — [Design for performance](https://create.roblox.com/docs/en-us/performance-optimization/design)
- Draw-call and triangle budgets on the baseline device: an older revision says **< 1,000 draw calls and < 1,000,000 triangles**. A newer revision (search snippet, reportedly updated Oct 2026) lists **600 draw calls and 650,000 triangles**. Verify on the live page — [Design for performance](https://create.roblox.com/docs/performance-optimization/design.md)
- Per-mesh triangle cap: 3rd-party sources say **~20,000–21,000 triangles per MeshPart** and lower for UGC accessories (4k vs 10k, conflicting). No official doc was confirmed — [nilo.io](https://nilo.io/articles/advanced-roblox-custom-meshes); [vasundhara](https://www.vasundhara.io/blogs/how-to-optimize-roblox-art-for-better-performance-low-poly-tips)
- Tools (3rd-party summary): Shift+F3 stats (texture memory, GPU memory), MicroProfiler and Rendering Stats (triangles, draw calls). A wide Render bar means you are GPU-bound — [santozstudios](https://santozstudios.com/blog/roblox-performance-optimisation-guide/)
- Community physics tips: avoid `CollisionFidelity.Default` (use Hull or Box), set `CanCollide` false where possible, reduce part and weld counts. Disabling shadows on small props is commonly advised — [HackMD community notes](https://hackmd.io/@Mullets/HJb5iUYfO); [DevForum part count and lag](https://devforum.roblox.com/t/part-count-and-lag/145280); [Optimization for Roblox Environments (community)](https://devforum.roblox.com/t/optimization-for-roblox-environments/3844846)

**Materials / PBR (Official)**
- Textures are supported up to **1024×1024**. Guidance by object size: **256² for 5×5 studs, 512² for 10×10 studs, 1024² for 20×20 studs**. Default materials map about 1024² across an 8×8-stud face — [Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications)
- `SurfaceAppearance` supports **5 PBR maps** (color, normal, roughness, metalness, emissive). One material per mesh. Tinting via `SurfaceAppearance.Color` is free for performance and saves memory by reusing one ColorMap. Alpha blending needs `MeshPart.Transparency` ≥ **0.02** — [PBR textures](https://create.roblox.com/docs/en-us/art/modeling/surface-appearance)
- 3rd-party: use 256–512 for most props and save 1024 for hero assets. One shared 1024 atlas can beat several 512s by cutting draw calls. Reuse identical MeshParts and materials for batching. Decals on meshes can duplicate geometry — [alivegames](https://www.alivegames.io/posts/roblox-texture-optimization-best-practices); [nilo.io](https://nilo.io/articles/roblox-asset-optimization-tutorial)

**AI tools for building (Official)**
- **Cube 3D** (GDC, Mar 2025): a 1.8B-parameter 3D foundation model trained on 1.5M assets. It shipped with a beta Mesh Generation API and an open-source release — [Beta Cube 3D tools](https://devforum.roblox.com/t/beta-cube-3d-generation-tools-and-apis-for-creators/3558947); [Roblox newsroom Mar 2025](https://about.roblox.com/newsroom/2025/03/unveiling-future-creation-native-3d-generation-collaborative-studio-tools-economy-expansion)
- **RDC 2025** (Sep 2025): generation of functional **4D objects** (scripted vehicles and weapons first), **MCP in Studio Assistant** (Assistant as an MCP client, for example laying out UI in Figma), and real-time translation — [RDC25 What we announced](https://devforum.roblox.com/t/rdc25-what-we-announced/3920245)
- Jan 2026: early access to in-experience 4D functional objects. Wikipedia says 4D creation went to public beta in Feb 2026 — [DevForum early access](https://devforum.roblox.com/t/early-access-introducing-in-experience-4d-functional-objects-and-enhanced-3d-generation/4050893); [Wikipedia Cube 3D](https://en.wikipedia.org/wiki/Cube_3D)

### Inferences
- A practical mobile-first map recipe: ShadowMap or Future with few shadow-casting point lights, Atmosphere for depth and to hide streaming pop-in, StreamingEnabled with defaults plus SLIM LOD on large models, size-appropriate textures with tinted shared maps, and Box or Hull collision on decoration.
- Hub and spawn design can follow the official greybox metrics (≥10-stud corridors, walls ≥10 studs) and the onboarding principle "get to the fun quickly". Keep the path from spawn to the first core-loop action short and visible.

### Gaps
- No official wayfinding guidance (signage, sightlines, landmarks) was found.
- Not searched because the budget ran out: Terrain tools specifics, MaterialVariant docs, CastShadow guidance, an official per-mesh triangle limit, and Assistant's 2026 building capabilities.
- The two conflicting draw-call/triangle budgets need verification on the live page.

## Sound/audio: Sound vs new Audio API, privacy and upload limits, licensed music, spatial audio, mixing and game feel

### Takeaway
Roblox now officially steers creators from `Sound`/`SoundGroup`/`SoundEffect` to the wire-based Audio API (AudioPlayer → effects → AudioEmitter/AudioListener → AudioDeviceOutput, connected by Wire). Since 22 Mar 2022, uploaded audio is private by default. Current docs allow free uploads of 2,000 per 30 days for ID-verified accounts and 100 for unverified accounts, with each file ≤7 min and ≤20 MB. Licensed music comes from APM, Monstercat, DistroKid and others.

### Cited Findings
**Audio API (Official)**
- `AudioPlayer` loads and plays an asset. `AudioEmitter` is a virtual speaker located at its parent. `AudioListener` is a virtual microphone at the camera or character. `AudioDeviceOutput` sends to the player's speakers and is auto-created under SoundService when ListenerLocation is Character or Camera. `Wire` connects streams through `SourceInstance` and `TargetInstance`. The docs say `Sound`, `SoundGroup` and `SoundEffect` are now **discouraged** in favor of audio objects — [Audio objects](https://create.roblox.com/docs/en-us/audio/objects); [Audio overview](https://create.roblox.com/docs/en-us/audio.md)
- Effects: `AudioFader` (volume), `AudioEqualizer` (frequency, for example muffled rain), `AudioCompressor` (dynamic range, usable for ducking), `AudioReverb` (indoor reflections), `AudioAnalyzer` (reads volume and spectrum) — [Audio effects](https://create.roblox.com/docs/en-us/audio/effects); [Engine reference llms.txt](https://create.roblox.com/docs/reference/engine/llms.txt)
- Community guide: audio must reach an AudioDeviceOutput to be heard. 3D audio goes emitter → listener, while global or 2D audio can skip that step — [A simple guide to the Audio API](https://devforum.roblox.com/t/a-simple-guide-to-the-audio-api/3132049)

**Legacy SoundGroup mixing (Official)**
- A SoundGroup acts as a mixer bus. Common setup is "SoundEffects" and "BackgroundMusic" groups with their own master volumes, all kept in one place. `CompressorSoundEffect` ducks background audio under priority audio (for example music under a GUI notification), with Threshold from −80 to 0. Weigh importance: player ability sounds matter more than ambience — [Sound groups](https://create.roblox.com/docs/en-us/sound/groups)
- Community: nested SoundGroups let one parent carry a shared effect (for example reverb for all weapons) instead of an effect on every sound. This saves CPU and makes per-category volume sliders easy — [Support for nested SoundGroups](https://devforum.roblox.com/t/support-for-nested-soundgroups/1669856)

**Privacy and upload limits (Official)**
- From **22 Mar 2022**, all new audio is Private and existing audio longer than **6 s** was set to Private. Roblox added free uploads with monthly limits, an Audio Discovery plugin and a licensed catalog — [Action Needed: Asset Privacy for Audio](https://devforum.roblox.com/t/1701697). Whether short clips (<6 s) can still be public is disputed in community threads — [DevForum](https://devforum.roblox.com/t/1-second-long-sfx-cant-be-made-public/1991394)
- Current docs: **ID-verified accounts get 2,000 free audio imports per 30 days, unverified get 100**. Each file must be a single track in .mp3/.ogg/.wav/.flac, **< 20 MB and < 7 min**. The uploader must be ID-verified for songs to appear on game detail pages — [Audio assets](https://create.roblox.com/docs/en-us/audio/assets). The 2022 announcement had said 100 per month for verified accounts, so the limit appears to have risen. A 3rd-party "7 MB" claim conflicts with the official 20 MB.

**Licensed music (Official and secondary)**
- **APM Music** (license since May 2018, a large commercial library). **Monstercat** (since July 2020). **DistroKid** (Sep 2024: artists who own their rights can distribute to Roblox, with a "DistroKid Hits" section in Creator Store > Audio; you must acquire the asset into your inventory first). Other sources include Pro Sound Effects, Nettwerk and Position Music — [Amplify Your Experiences with New Music](https://devforum.roblox.com/t/amplify-your-experiences-with-new-music/3164792); [Music Ally](https://musically.com/2024/09/09/roblox-moves-into-music-discovery-with-charts-and-distrokid/); [Creator Store Audio](https://create.roblox.com/store/audio); [Roblox wiki (secondary)](https://roblox.fandom.com/wiki/Audio)
- DistroKid artist terms reported: no royalties during beta. Artists need 100% publishing ownership and no PRO registration — [Music Ally](https://musically.com/2024/09/09/roblox-moves-into-music-discovery-with-charts-and-distrokid/)
- Caution (community): licensed APM tracks can still trigger automated copyright claims on creators' YouTube videos. See Roblox Help on licensed music in videos — [Roblox Help](https://en.help.roblox.com/hc/en-us/articles/360038525351-Using-Licensed-Music-in-Videos)

### Inferences
- For new projects, build the mix on the Audio API: AudioPlayer → AudioFader per category bus → AudioCompressor for ducking → AudioDeviceOutput, with AudioEmitter and AudioListener for 3D SFX. Expose Music, SFX and UI volume sliders through the per-category faders.
- For game feel, prioritize player-action and UI feedback sounds over ambience, and duck music under rewards and notifications (the official ducking example).

### Gaps
- Not searched because the budget ran out: AudioEmitter distance attenuation curves (e.g. a `SetDistanceAttenuation` API is unconfirmed), AudioInteractionGroup, RDC 2025 audio announcements, and music charts.
- No sourced guidance was found on loop points, crossfades, LUFS loudness targets or SFX timing.
