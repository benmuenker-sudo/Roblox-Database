# Beleuchtung, Atmosphäre und Performance der Map

> Stand: 2026-10-24 · Nächste Prüfung: 2027-01-24 · Gesamt-Vertrauen: ✅ für Lighting-, Streaming-, LOD-, Textur- und Budget-Angaben (Creator Docs, lokal am Quelltext geprüft, Commit `4e795e6`), 🟡 für Ankündigungen (Cube 3D, 4D) und Community-Budgets, 🟠 für Drittquellen, 🧠 für eigene Rezepte

## Kurzfassung
**Licht:** `Lighting.Technology` (Voxel/ShadowMap/Future) ist **veraltet** und durch `Lighting.LightingStyle` (`Realistic` oder `Soft`) plus `Lighting.PrioritizeLightingQuality` ersetzt; neue Spiele starten mit `Soft` ✅ ([Technology](https://create.roblox.com/docs/reference/engine/enums/Technology), [Global lighting](https://create.roblox.com/docs/environment/lighting)). **Atmosphäre** schafft Tiefe und kaschiert Streaming-Lücken. **Streaming** ist bei neuen Places an; empfohlen: `StreamingMinRadius` 64, `StreamingTargetRadius` 1024, `ModelStreamingBehavior.Improved`, `StreamOutBehavior.Opportunistic` ✅ ([Instance streaming](https://create.roblox.com/docs/workspace/streaming)). **LOD:** `Model.LevelOfDetail = SLIM` explizit setzen, denn `Automatic` entspricht derzeit `Disabled` ✅ ([ModelLevelOfDetail](https://create.roblox.com/docs/reference/engine/enums/ModelLevelOfDetail)). **Budget:** Die Doku nennt „unter 1.000 Draw Calls und 1.000.000 Dreiecken“ nur als **Beispiel** für ein selbst gewähltes Basisgerät ✅ ([Design for performance](https://create.roblox.com/docs/performance-optimization/design)). **Texturen:** bis 4096×4096 unterstützt, die gleiche Seite nennt im UV-Abschnitt aber noch 1024×1024 – Widerspruch in der Doku ✅ ([Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications)).

## Warum das wichtig ist
- Mobilgeräte (2024: 80 % der DAU 🟡, [PocketGamer.biz](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue)) haben starke Speichergrenzen und stürzen bei Out-of-Memory ab ✅ ([Design for performance](https://create.roblox.com/docs/performance-optimization/design)).
- Licht ist der billigste Stimmungshebel: Das offizielle Außen-Tutorial verwandelt eine flache Mittagsszene allein durch Tageszeit, Ambient-Farbe, Atmosphäre und ein Lagerfeuerlicht ✅ ([Enhance outdoor environments](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments)).
- Lange Ladezeiten und Ruckler erhöhen die frühe Absprungrate 🧠; Streaming verbessert laut Doku Join-Zeit, Speicher und Frame-Rate ✅.

## Referenzbilder
Offizielle Bilder aus der Roblox Creator Documentation (Übersicht: `assets/bilder/offiziell/README.md`):

![Außenszene vorher](../assets/bilder/offiziell/level-design-umgebung/aussen-beleuchtung-vorher.jpg)
![Außenszene nachher](../assets/bilder/offiziell/level-design-umgebung/aussen-beleuchtung-nachher.jpg)
*Vorher: neutrales Mittagslicht. Nachher: tiefe Sonne, warmes Ambient, Dunst, leuchtendes Feuer. Quelle: Roblox Creator Docs, CC BY 4.0*

![LightingStyle Realistic](../assets/bilder/offiziell/level-design-umgebung/lichtstil-realistic.jpg)
![LightingStyle Soft](../assets/bilder/offiziell/level-design-umgebung/lichtstil-soft.jpg)
*Gleiche Bibliothek mit `Realistic` (harte Schatten, Tiefe) und `Soft` (flacher Retro-Look). Quelle: Roblox Creator Docs, CC BY 4.0*

![Innenraum mit Lichtleck](../assets/bilder/offiziell/level-design-umgebung/innen-lichtleck-ohne-huelle.jpg)
![Innenraum abgedichtet](../assets/bilder/offiziell/level-design-umgebung/innen-lichtleck-mit-huelle.jpg)
*Ohne umschließende Parts dringt Außenlicht ein; mit Hülle wirken nur Innenlichter. Quelle: Roblox Creator Docs, CC BY 4.0*

![Atmosphere Density 0](../assets/bilder/offiziell/level-design-umgebung/atmosphaere-dichte-0.jpg)
![Atmosphere Density 0,35](../assets/bilder/offiziell/level-design-umgebung/atmosphaere-dichte-035.jpg)
*Ohne Dichte harte Fernsicht; mit Dichte verblassen ferne Felsen. Quelle: Roblox Creator Docs, CC BY 4.0*

![Lokale Lichter bei Nacht](../assets/bilder/offiziell/effekte/lichtquellen-diner-nacht.jpg)
*Lokale Lichtquellen als Blickfang. Quelle: Roblox Creator Docs, CC BY 4.0*

![Schatten an](../assets/bilder/offiziell/effekte/lichtquelle-schatten-an.jpg)
![Schatten aus](../assets/bilder/offiziell/effekte/lichtquelle-schatten-aus.jpg)
*Schatten geben Tiefe, kosten aber Leistung – nur wo sie wirken. Quelle: Roblox Creator Docs, CC BY 4.0*

![Streaming-Radius 64](../assets/bilder/offiziell/performance/duvall-streaming-radius-64.jpg)
![Streaming-Radius 1024](../assets/bilder/offiziell/performance/duvall-streaming-radius-1024.jpg)
*Radius 64: Haus im Hintergrund fehlt; Radius 1024: sichtbar. Quelle: Roblox Creator Docs, CC BY 4.0*

![SLIM aus](../assets/bilder/offiziell/performance/slim-deaktiviert.jpg)
![SLIM an](../assets/bilder/offiziell/performance/slim-aktiviert.jpg)
*Ohne SLIM verschwinden ferne Gebäude, mit SLIM bleiben vereinfachte Modelle sichtbar. Quelle: Roblox Creator Docs, CC BY 4.0*

![SLIM-Zonen](../assets/bilder/offiziell/performance/slim-zonen-diagramm.jpg)
*Vier SLIM-Render-Zonen um den Spieler. Quelle: Roblox Creator Docs, CC BY 4.0*

![LOD Original](../assets/bilder/offiziell/performance/lod-original.jpg)
![LOD SLIM](../assets/bilder/offiziell/performance/lod-slim.jpg)
![LOD Imposter](../assets/bilder/offiziell/performance/lod-imposter.jpg)
*Original → SLIM → grober Imposter (StreamingMesh). Quelle: Roblox Creator Docs, CC BY 4.0*

![Atomic Streaming](../assets/bilder/offiziell/performance/streaming-modell-atomic.png)
*Atomic-Modell streamt mit allen Kindern zusammen. Quelle: Roblox Creator Docs, CC BY 4.0*

![Geometrie zusammenfassen](../assets/bilder/offiziell/performance/geometrie-optimierung-tuerme.jpg)
*Links viele Einzel-Assets, rechts zu einem Mesh zusammengefasst = weniger Draw Calls. Quelle: Roblox Creator Docs, CC BY 4.0*

![Performance-Workflow](../assets/bilder/offiziell/performance/performance-workflow.png)
*Design → Identify → Improve → Monitor. Quelle: Roblox Creator Docs, CC BY 4.0*

![Laser-Tag-Layout drei Wege](../assets/bilder/offiziell/level-design-umgebung/lasertag-layout-drei-hauptwege.jpg)
*Greybox-Basis des Laser-Tag-Beispiels (Maße in Abschnitt 9). Quelle: Roblox Creator Docs, CC BY 4.0*

## Details

### 1. Lighting-Technik: alt vs. neu ✅
Quelle: [Technology](https://create.roblox.com/docs/reference/engine/enums/Technology), [Lighting](https://create.roblox.com/docs/reference/engine/classes/Lighting), [Global lighting](https://create.roblox.com/docs/environment/lighting).

| Alt (`Lighting.Technology`, veraltet) | Status laut Referenz |
|---|---|
| `Voxel` | 4×4×4-Voxel-Lichtraster |
| `ShadowMap` | schärfere Schatten von Sonne/gerichteten Lichtern |
| `Future` | höchste Licht- und Schattenqualität |
| `Compatibility`, `Legacy`, `Unified` | veraltet, in Studio nicht mehr wählbar; Compatibility-Look ≈ `Voxel` + `ColorGradingEffect` mit `TonemapperPreset.Retro` |

**Neu:** Die Property `Lighting.Technology` ist selbst als veraltet markiert und ersetzt durch:
- `Lighting.LightingStyle`: `Realistic` = „das fortschrittlichste und realistischste Licht und die Schatten, die Roblox liefern kann“; `Soft` = flacher Retro-Roblox-Look mit weicheren Lichtern und Schatten. **Studio startet jedes Spiel mit `Soft`** ✅ ([Enhance outdoor environments](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments)). Nur im Properties-Fenster änderbar ✅ ([Light sources](https://create.roblox.com/docs/effects/light-sources)).
- `Lighting.PrioritizeLightingQuality`: `true` = bei sinkender Qualitätsstufe zuerst Sichtweite opfern, Schatten/Shader in der Nähe behalten; `false` = Sichtweite priorisieren.
- Korrektur gegenüber älteren Notizen: Die Aussage „Technology = Voxel/ShadowMap/Future wählen“ ist überholt; Geräte ohne Future fielen früher auf ShadowMap/Voxel zurück (Staff-Post 2020) 🟡 ([DevForum](https://devforum.roblox.com/t/future-is-bright-phase-3-released/878634)) – für neue Arbeit `LightingStyle` verwenden.

### 2. Die Lighting-Eigenschaften ✅
Quelle: [Global lighting](https://create.roblox.com/docs/environment/lighting).
| Gruppe | Eigenschaften | Wirkung |
|---|---|---|
| Farbe | `Ambient` (ganzes Spiel, innen und außen), `OutdoorAmbient` (nur wo der Himmel sichtbar ist), `ColorShift_Top` (sonnenzugewandte Flächen), `ColorShift_Bottom` (abgewandte Flächen) | Grundstimmung, Tageszeit-Färbung |
| Intensität | `Brightness`, `ExposureCompensation` | Kontrast Licht/Schatten, Belichtung |
| Schatten | `GlobalShadows`, `ShadowSoftness` (0 hart – 1 weich, nur bei `Realistic`) | Schattenwurf |
| Darstellung | `LightingStyle`, `PrioritizeLightingQuality` | Stil, Skalierung |
| Umgebung | `ClockTime` (0–24) / `TimeOfDay` (String), `GeographicLatitude`, `EnvironmentDiffuseScale`, `EnvironmentSpecularScale` | Sonnenstand, Umgebungslicht, Reflexionen |

- `ClockTime`/`TimeOfDay` laufen **nicht** von allein; nur per Skript ✅.
- **Offizielles Außen-Rezept** ✅ ([Enhance outdoor environments](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments)): `LightingStyle = Realistic`; `EnvironmentDiffuseScale` und `EnvironmentSpecularScale` = **1** (Metall reflektiert); `ClockTime = 17`; `Ambient` und `OutdoorAmbient` von Standard **70, 70, 70** auf **156, 136, 176** (lila Abendton); Skybox; `Atmosphere.Density = 0.272`, `Haze = 1`; `PointLight` am Lagerfeuer mit Schatten und `Brightness = 2`.
- **Offizielles Innen-Rezept** ✅ ([Enhance indoor environments](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments)): Innenräume mit `Part`s von **mindestens 1 Stud Dicke** umschließen (Beispiel nutzt 2,5 Studs um Mesh-Wände und Decke), sonst leckt Außenlicht; `Ambient` warm (Orange) passend zu Feuer und Kerzen; `SunRaysEffect` betont Licht durchs Fenster.

### 3. Lokale Lichter ✅
Quelle: [Light sources](https://create.roblox.com/docs/effects/light-sources), [Improve performance](https://create.roblox.com/docs/performance-optimization/improve).
| Typ | Form | Typischer Einsatz | Wichtige Properties |
|---|---|---|---|
| `PointLight` | Kugel | Glühbirne, Fackel, Feuerball | `Range` (Studs); am besten in einem `Attachment` |
| `SpotLight` | Kegel | Straßenlaterne, Taschenlampe, Scheinwerfer | `Face`, `Angle` (max. 180 = Halbkugel), `Range` |
| `SurfaceLight` | ganze Fläche | Bildschirme, Schilder, Leuchtröhren | `Face`, `Angle` (0 = gerade raus, 180 = parallel zur Fläche), `Range` |

- Gemeinsam (`Light`): `Color`, `Brightness` (höher ≠ größerer Radius), `Shadows`.
- In Studio „Show Light Guides“ einschalten, um Kegel/Reichweite zu sehen.
- **Kosten senken** ✅: Engine verschlechtert Schatten mit sinkender Grafikstufe und schaltet sie **unter Stufe 4** ganz ab. Zusätzlich: `BasePart.CastShadow` an kleinen/fernen Teilen aus, Schatten an bewegten Objekten aus, `Light.Shadows` aus, wo unnötig, Reichweite und Winkel begrenzen, weniger Lichter, Lichter raumweise oder außerhalb einer Distanz abschalten.
- Community-Erfahrung: Spot-Schatten am günstigsten, dann Surface, Point am teuersten; breite Spot-Winkel nähern sich Point-Kosten 🟠 ([DevForum](https://devforum.roblox.com/t/future-vs-shadowmap/658587)).

### 4. Atmosphäre, Himmel, Post-Processing ✅
Quelle: [Atmospheric effects](https://create.roblox.com/docs/environment/atmosphere), [Post-processing effects](https://create.roblox.com/docs/environment/post-processing-effects).

| `Atmosphere`-Property | Wirkung | Abhängigkeit |
|---|---|---|
| `Density` | Menge der Luftpartikel; verdeckt ferne Objekte und Terrain (Skybox nur indirekt) | – |
| `Offset` | Hoch = Horizont-Silhouette; niedrig = Ferne verschmilzt mit dem Himmel | Mit `Density` abstimmen; zu niedrig → Skybox scheint durch |
| `Haze` | Dunst über dem Horizont und in die Ferne | – |
| `Color` | Farbton der Atmosphäre | Wirkt stärker mit hohem `Haze` |
| `Glare` | Glühen um die Sonne | braucht `Haze` > 0 |
| `Decay` | Farbton abseits der Sonne | braucht `Haze` und `Glare` > 0 |

| Post-Effekt | Einsatz laut Doku |
|---|---|
| `BloomEffect` | Helle Teile glühen |
| `BlurEffect` | Hintergrund unscharf, wenn ein Menü offen ist |
| `ColorCorrectionEffect` | `Brightness`, `Contrast`, `Saturation`, `TintColor`; z. B. rot tönen bei wenig Gesundheit |
| `DepthOfFieldEffect` | Fokus auf ein Item im Shop, Ferne unscharf |
| `SunRaysEffect` | Sonnenstrahlen, abhängig von `ClockTime` |
| `ColorGradingEffect` | `TonemapperPreset` `Default` (seit 2019, kräftig) oder `Retro` (vor 2019, blasser; für vollen Retro-Look Lichter auf max. 1,0) |

🧠 Mobile-Rezept: `Atmosphere` mit mäßiger `Density` (0,2–0,35) kaschiert Streaming-Ränder billiger als riesige Sichtweiten; nur 1–2 Post-Effekte dauerhaft.

### 5. Instance Streaming ✅
Quelle: [Instance streaming](https://create.roblox.com/docs/workspace/streaming), [Streaming techniques](https://create.roblox.com/docs/workspace/streaming/techniques).
- `Workspace.StreamingEnabled` ist bei **neuen Places standardmäßig an** und nicht per Skript setzbar. Gilt nur für Nachkommen von `Workspace` (nicht `ReplicatedStorage`).
- **Empfohlene Werte:**

| Property | Standard | Empfehlung | Hinweis |
|---|---|---|---|
| `StreamingMinRadius` | 64 | 64 | Höchste Priorität; Erhöhen kostet Speicher und Bandbreite. Regionen darin streamen nie aus. |
| `StreamingTargetRadius` | 1024 | 1024 | Maximale Distanz mit voller Detailtiefe; kleiner = weniger Serverlast. Muss größer als MinRadius sein (Puffer). |
| `ModelStreamingBehavior` | `Legacy` | `Improved` | Modelle mit BaseParts streamen erst, wenn ein Teil berechtigt ist |
| `StreamOutBehavior` | `LowMemory` | `Opportunistic` | Client räumt außerhalb des Target-Radius auch ohne Speicherdruck auf → weniger OOM-Abstürze |
| `StreamingIntegrityMode` | – | `PauseOutsideLoadedArea` | Pausiert nur, wenn der Spieler in ungeladenes Gebiet läuft |
| `EnableSLIMAvatars` | – | `Enabled` | R15-Avatare als animierte SLIM-Platzhalter |
| `PredictiveStreamingMode` | aus | `Enabled` erwägen | Lädt Respawn-Orte vor, hält verlassene Orte nach Teleport kurz |

- **Model-Modi:** `Nonatomic` (Standard), `Atomic` (alle Kinder zusammen), `Persistent` (nie ausgestreamt, nach Join gesendet, vor `Workspace.PersistentLoaded`), `PersistentPerPlayer` (über `Model:AddPersistentPlayer()`). Persistent nur in seltenen Fällen; Überbenutzung schadet.
- **Verhalten:** Ausgestreamte Instanzen werden auf `nil` geparentet (nicht zerstört); lokale Property-Änderungen können verloren gehen. Vom Client erzeugte Instanzen streamen nicht aus. Physik-Assemblies streamen als Ganzes ein; riesige bewegte Assemblies verursachen Spitzen.
- **Replication Foci:** Standard ist die `PrimaryPart` des Charakters; `Player.ReplicationFocus`, `Player:AddReplicationFocus()`. 9 bewegte Foci erzeugen ähnliche Last wie 10 Spieler.
- **Debug:** Shift+F3 (Studio: Shift+Ctrl+F3) → Shift+1 bis zum 4. Panel „Streaming“; farbige Regionen zeigen Radien; zum Überblicken `CameraMaxZoomDistance` z. B. auf 1000.
- **Eigene Pause-Anzeige:** `GuiService:SetGameplayPausedNotificationEnabled(false)` und `Player.GameplayPaused` beobachten.
- Streaming-Regeln fürs Leveldesign (gewundene Wege, Sichtblocker, Modelle < ~64 Kubik-Studs): `map-grundlagen.md`.

### 6. LOD: SLIM, StreamingMesh, RenderFidelity ✅
Quelle: [SLIM](https://create.roblox.com/docs/workspace/streaming/slim), [ModelLevelOfDetail](https://create.roblox.com/docs/reference/engine/enums/ModelLevelOfDetail), [Improve performance](https://create.roblox.com/docs/performance-optimization/improve).

| `Model.LevelOfDetail` | Verhalten |
|---|---|
| `SLIM` („Scalable Lightweight Interactive Models“) | Cloud-generierte Verbundmeshes mit mehreren Detailstufen; weniger Draw Calls, Dreiecke, Speicher; alle Teile wechseln gleichzeitig; ferne Modelle sehen detaillierter aus als mit dem alten System |
| `StreamingMesh` | Alter grober, untexturierter „Imposter“ außerhalb des Streaming-Radius |
| `Disabled` | Kein LOD-Mesh |
| `Automatic` | Standard, **derzeit gleichbedeutend mit `Disabled`** |

**SLIM-Voraussetzungen:** Streaming an; Place **bei Roblox gespeichert** (nicht lokale `.rbxl`); **Team Create** aktiv. Erstgenerierung kann dauern – **1–2 Minuten** warten und neu beitreten.
**SLIM-Grenzen:** nur **statische** Modelle (keine Teile hinzufügen/entfernen, keine Animation); Modelle mit `Humanoid` ausgeschlossen; SLIM-Avatare nur R15 (kein R6, keine NPCs, keine Sonderproportionen); `Scale = 0` ausgeschlossen; auf nicht unterstützten Plattformen Rückfall auf `Disabled`. Unterstützte Instanztypen im Modell: `Part`, `MeshPart`, `Decal`, `Texture`, `SurfaceAppearance`, `PartOperation`, `NegateOperation`, `SpecialMesh`. Demo: 200 animierte SLIM-Avatare.

```lua
-- Command Bar: alte StreamingMesh-Modelle auf SLIM umstellen (aus der Creator Docs)
for _, descendant in workspace:GetDescendants() do
	if descendant:IsA("Model") and descendant.LevelOfDetail == Enum.ModelLevelOfDetail.StreamingMesh then
		descendant.LevelOfDetail = Enum.ModelLevelOfDetail.SLIM
	end
end
```
- **Meshes:** `MeshPart.RenderFidelity = Automatic` oder `Performance`, damit weniger komplexe Varianten genutzt werden; zu viele `Precise`-Meshes sind ein typisches Problem ✅. Die oft genannten Umschaltdistanzen (< 250, 250–500, > 500 Studs) sind nicht offiziell bestätigt 🟠 ([nilo.io](https://nilo.io/articles/advanced-roblox-custom-meshes)).

### 7. Draw Calls, Dreiecke, Budgets ✅
Quelle: [Design for performance](https://create.roblox.com/docs/performance-optimization/design), [Improve performance](https://create.roblox.com/docs/performance-optimization/improve).
- **Basisgerät wählen** und die ganze Entwicklung darauf testen. Offizielles **Beispiel**: Mit Render- und Summary-Stats sieht man, dass die Frame-Rate in vollen Bereichen fällt, und legt fest, **unter 1.000 Draw Calls und 1.000.000 Dreiecken** zu bleiben. Das ist ausdrücklich ein hypothetisches Beispiel, kein Plattformlimit.
- **Korrektur:** Die in Notizen kursierenden Werte **600 Draw Calls / 650.000 Dreiecke** stehen **nirgends** in der aktuellen Doku ✅ (Volltextsuche im Doku-Quelltext).
- Community-Ziel für Mobile: **500 Draw Calls, 500.000 Dreiecke, unter 1,3 GB Client-Speicher** 🟡 ([DevForum, von der Doku verlinkt](https://devforum.roblox.com/t/real-world-building-and-scripting-optimization-for-roblox/3127146)). Pro-Mesh-Obergrenzen (~20.000–21.000 Dreiecke) nennen nur Drittquellen 🟠 ([nilo.io](https://nilo.io/articles/advanced-roblox-custom-meshes)).
- **Instancing:** Identische Meshes (gleiches `MeshContent`) mit identischer `SurfaceAppearance` bzw. identischem `TextureContent`/Material werden in **einem** Draw Call gezeichnet. Darum jedes Mesh **einmal hochladen** und in Studio duplizieren; ganze Szenen auf einmal zu importieren erzeugt Duplikate mit eigenen IDs (der Importer dedupliziert nicht).
- **Teuer:** hohe Objektdichte; Decals, Texturen, Partikel (batchen schlecht); Property-Änderungen an `ParticleEmitter`; viele schattenwerfende Lichter; teiltransparente Überlagerungen (Overdraw); bewegte Skinned-MeshParts ohne Humanoid; zu viele Teile in einem Modell (FastCluster-Rebuilds).
- **Culling:** Frustum- und Occlusion-Culling laufen automatisch; in Innenräumen kann ein eigenes Raum-/Portalsystem mehr sparen.
- **Transparenz:** nur 0 oder 1 verwenden, wo möglich.
- **Built-in Materials** sparen viel Speicher gegenüber eigenen Texturen; **Packages** gegen doppelte Assets.

```lua
-- Command Bar: doppelte Mesh-IDs aufspüren (aus der Creator Docs)
for _, descendant in workspace:GetDescendants() do
	if descendant:IsA("MeshPart") then
		print(descendant.Name .. ", " .. descendant.MeshId)
	end
end
```

### 8. Texturen und der 4096/1024-Widerspruch ✅
Quelle: [Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications), [PBR textures](https://create.roblox.com/docs/art/modeling/surface-appearance), [Improve performance](https://create.roblox.com/docs/performance-optimization/improve).
- **Abschnitt „Resolution“:** „Roblox supports up to 4096×4096 pixel texture resolutions (4K).“ Beim Laden startet die Engine mit niedriger Qualität und steigert je nach Gerät.
- **Abschnitt „UV mapping“ derselben Seite:** „Roblox supports up to 1024×1024 pixel spaces for texture maps.“ → **Widerspruch innerhalb der Doku.** Avatar-/Accessory-Budgets bleiben bei max. 1024, Nicht-Albedo-Maps rigider Accessories max. 256×256.
- 🧠 Praxis: Für Welt-Assets 4K nur in Ausnahmefällen; die Größenregel unten ist für Speicher entscheidend.

| Objektgröße | Textur laut Doku |
|---|---|
| ca. 5×5 Studs | 256×256 |
| ca. 10×10 Studs | 512×512 |
| ca. 20×20 Studs | 1024×1024 |
| Part-Material | zeigt 1024×1024 auf einer 8×8-Stud-Fläche |
| Terrain | 512×512 auf 8×8 Studs |

- **Speicher:** hängt von der **Pixelzahl** ab, nicht von der Dateigröße; 1024² braucht **4×** so viel Grafikspeicher wie 512². Vorab komprimieren oder Alpha entfernen spart keinen Grafikspeicher (Roblox transkodiert in ein festes Format).
- **UI-/Nebenbilder:** meist ≤ 512², kleine < 256²; Sprite Sheets für UI.
- **Wiederverwenden:** eine Textur hochladen und per `SurfaceAppearance.Color` einfärben statt mehrere Farbvarianten; **Trim Sheets** für maximale Wiederverwendung.
- `SurfaceAppearance`: 5 PBR-Map-Typen (Color/Albedo, Normal, Roughness, Metalness, Emissive); Transparenz über `SurfaceAppearance.AlphaMode` = `Overlay` (Standard, zeigt darunter `MeshPart.Color`) oder `Transparency` (Mesh wird durchsichtig) ✅ ([PBR textures](https://create.roblox.com/docs/art/modeling/surface-appearance)). Die in einer Notiz genannte Schwelle „`MeshPart.Transparency` ≥ 0,02 für Alpha-Blending“ steht nicht in der aktuellen Seite 🟠.

### 9. Greybox-Metriken und Laser-Tag-Beispiel (Kurzform) ✅
Quelle: [Greybox your environment](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment).
- Gänge/Türen **≥ 10 Studs** breit, Wände **≥ 10 Studs** hoch (Sprung 5 Studs, Kamera frei), Raster 5 Studs/90°.
- Layout: **2 Spawnzonen** (je 2 Ausgänge), **3 Hauptwege** (Interior/Middle/Exterior), **5 Querwege**, gespiegelt; Combat Pockets mit max. 3 Ein-/Ausgängen.
- Ausführlich: `map-grundlagen.md`.
- Performance-Schritt der Lernreihe: Türme aus vielen Einzel-Assets zu einem Mesh zusammenfassen, doppelte Texturen entfernen, geschichtete Transparenzen löschen ✅ ([Optimize your experience](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience)).

### 10. Speicher und Ladezeit ✅
Quelle: [Improve performance](https://create.roblox.com/docs/performance-optimization/improve).
- Wirksamster Hebel für Client-Speicher: **Instance Streaming**; bei Speicherproblemen aggressiver einstellen (weniger `Persistent`, kleinere Radien).
- **Audio** kann überraschend viel Speicher kosten – nicht alles auf einmal laden.
- Vor dem Spielstart lädt der Client `ReplicatedFirst`, `ReplicatedStorage`, den initialen Workspace und vorgeladene Assets → beides schlank halten; große Assets in `ServerStorage`.
- `PreloadAsync` nur für Ladebildschirm, wichtige Menü-Bilder, Spawn-Assets; bei viel Vorladen einen Skip-Button anbieten.
- Große Places in mehrere Places teilen + Teleport: kürzere Erst-Ladezeit, aber Wartezeit beim Wechsel ✅ ([Design for performance](https://create.roblox.com/docs/performance-optimization/design)).

### 11. Messen und Werkzeuge ✅
| Werkzeug | Taste | Zweck |
|---|---|---|
| Developer Console | F9 | Speicher, Netzwerk, Skript-Stats, MicroProfiler starten |
| Render-/Summary-Stats | Shift+F2 | Draw Calls, Dreiecke (`Draw (scene)`) |
| Network Stats / Streaming | Shift+F3 (Studio Shift+Ctrl+F3), dann Shift+1 | Streaming-Zustand |
| MicroProfiler | Ctrl+Alt+F6 (Mac ⌘⌥F6) | Frames > 16,67 ms und Spitzen finden |

Quellen: [Identify performance issues](https://create.roblox.com/docs/performance-optimization/identify), [Design for performance](https://create.roblox.com/docs/performance-optimization/design), [Instance streaming](https://create.roblox.com/docs/workspace/streaming). Der Studio-Emulator ist **für Speicher ungenau** (Server + Client in einem Prozess) ✅. Ein breiter Render-Balken im MicroProfiler bedeutet GPU-Limit 🟠 ([santozstudios](https://santozstudios.com/blog/roblox-performance-optimisation-guide/)).

### 12. VR-Besonderheiten ✅
Quest-Auto-Quality zielt auf **≥ 72 FPS**, skaliert Sichtweite und kann Lichtberechnung abschalten; Mobile-VR reagiert empfindlich auf Draw Calls, teiltransparente Objekte (Decals, `Glass`) und komplexe `SurfaceGui`s ✅ ([VR guidelines](https://create.roblox.com/docs/production/publishing/vr-guidelines)).

### 13. KI-Werkzeuge für Bau und Blockout
| Werkzeug | Stand | Beleg |
|---|---|---|
| `GenerationService:GenerateModelAsync()` | Text-Prompt → Modell; Schemas `Car5` und `Body1`; optional Bounding Box und max. Dreieckszahl; Ergebnisse werden moderiert; auch für Spieler im Spiel nutzbar | ✅ [Model generation](https://create.roblox.com/docs/parts/model-generation), [Generative AI](https://create.roblox.com/docs/generative-AI) |
| Assistant in Studio | Schreibt Skripte, fügt Objekte ein, ändert sie, automatisiert Wiederholungen; offener Studio-MCP-Server für externe KI-Werkzeuge (u. a. Anthropic, OpenAI, Google Gemini) | ✅ [Assistant](https://create.roblox.com/docs/assistant/overview), [MCP servers](https://create.roblox.com/docs/assistant/mcp) |
| **Cube 3D** | GDC März 2025: 3D-Foundation-Model mit 1,8 Mrd. Parametern, trainiert auf 1,5 Mio. Assets, Beta-Mesh-Generation-API, Open Source | 🟡 [DevForum](https://devforum.roblox.com/t/beta-cube-3d-generation-tools-and-apis-for-creators/3558947), [Newsroom](https://about.roblox.com/newsroom/2025/03/unveiling-future-creation-native-3d-generation-collaborative-studio-tools-economy-expansion) (Name „Cube“ nicht in der lokalen Doku) |
| **4D-Objekte** | RDC Sep. 2025: funktionale Objekte (zuerst Fahrzeuge und Waffen); Jan. 2026 Early Access im Spiel; laut Wikipedia Public Beta Feb. 2026 | 🟡 [RDC25](https://devforum.roblox.com/t/rdc25-what-we-announced/3920245), [DevForum](https://devforum.roblox.com/t/early-access-introducing-in-experience-4d-functional-objects-and-enhanced-3d-generation/4050893), [Wikipedia](https://en.wikipedia.org/wiki/Cube_3D) |

- Pflichten bei generativer KI im Spiel: Moderation durch Roblox bei Roblox-APIs; bei Drittanbietern ist der Entwickler verantwortlich; Content-Maturity-Fragebogen angeben; längere KI-Gespräche brauchen das Label „Restricted“ (18+) ✅ ([Generative AI](https://create.roblox.com/docs/generative-AI)).
- 🧠 Einsatz im Leveldesign: Props und Varianten für Greybox/Deko schnell erzeugen, dann manuell auf Stil, Dreieckszahl und Wiederverwendung (Instancing) prüfen.

### 14. Rezept: mobilfreundliche Welt 🧠 (aus den offiziellen Bausteinen)
1. `LightingStyle` bewusst wählen: `Soft` für stilisierte/kindliche Spiele und Lesbarkeit, `Realistic` für Stimmung; `PrioritizeLightingQuality` nur `true`, wenn Licht zentral ist.
2. Wenige schattenwerfende Lichter, `CastShadow` an Kleinteilen aus.
3. `Atmosphere` (Density 0,2–0,35) für Tiefe und gegen Streaming-Kanten.
4. Streaming mit Doku-Empfehlungen, `Opportunistic`, SLIM an statischen Gebäuden, SLIM-Avatare an.
5. Texturen nach Stud-Größe, Farbvarianten per `SurfaceAppearance.Color`, Trim Sheets.
6. Meshes einmal hochladen, duplizieren; Packages nutzen.
7. Kollision der Deko vereinfachen (`CanCollide = false`, Box/Hull) 🟠 ([Community-Notizen](https://hackmd.io/@Mullets/HJb5iUYfO)).
8. Auf Basisgerät messen, eigenes Budget festhalten, nach jedem Update erneut messen (Kreislauf Design → Identify → Improve → Monitor ✅).

## Beispiele aus echten Spielen
- *The Mystery of Duvall Drive* (Roblox-Showcase): Streaming-Radius 64 vs. 1024 und gewundene Auffahrt mit Sichtblockern ✅ ([Stream in immersion](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion)).
- *City People Cars SLIM Template* und *SLIM Platform Avatars* (200 animierte Avatare) als offizielle Demos ✅ ([SLIM](https://create.roblox.com/docs/workspace/streaming/slim)).

## Do / Don't
| Do | Don't |
|---|---|
| `LightingStyle` + `PrioritizeLightingQuality` | `Technology` als Hauptschalter behandeln |
| Innenräume mit ≥ 1 Stud dicken Parts abdichten | Mesh-Wände ohne Hülle (Lichtlecks) |
| Wenige Schattenlichter, `CastShadow` an Kleinteilen aus | Dutzende Point-Lights mit Schatten |
| Streaming an, Doku-Empfehlungen, `Opportunistic` | Streaming aus bei großer Map |
| SLIM explizit setzen | Auf `Automatic` vertrauen (= Disabled) |
| Eigenes Budget auf Basisgerät messen | 1.000/1 Mio. als festes Limit zitieren |
| Meshes einmal hochladen, duplizieren | Ganze Map auf einmal importieren |
| Texturgröße nach Stud-Fläche | Überall 4K |
| Nur Transparenz 0/1 | Viele halbtransparente Schichten |
| Speicher auf echtem Gerät messen | Speicherwerte aus Studio glauben |

## Checkliste
- [ ] `LightingStyle` gewählt, `PrioritizeLightingQuality` bewusst gesetzt
- [ ] Innenräume abgedichtet, Ambient je Zone abgestimmt
- [ ] Schattenwerfende Lichter gezählt und begrenzt
- [ ] Atmosphere eingestellt (Density/Offset/Haze), Skybox passt
- [ ] Streaming an: Min 64, Target 1024, `Improved`, `Opportunistic`, `PauseOutsideLoadedArea`
- [ ] SLIM für statische Gebäude/Props, Place gespeichert, Team Create an
- [ ] `RenderFidelity` nicht überall `Precise`
- [ ] Doppelte Mesh-/Textur-IDs entfernt, Packages genutzt
- [ ] Texturen nach Stud-Größe, UI-Bilder ≤ 512
- [ ] Draw Calls/Dreiecke/Speicher auf Basisgerät gemessen und als Budget notiert
- [ ] `ReplicatedStorage`/`ReplicatedFirst` schlank, `PreloadAsync` sparsam

## Offene Fragen / Recherche-Bedarf
- Welche Texturgrenze (4096 oder 1024) für Welt-Assets tatsächlich gilt: Doku widerspricht sich; bei nächstem Update prüfen.
- Offizielle Pro-Mesh-Dreiecksgrenze und offizielle Mobile-Speichergrenze: nicht in der Doku.
- Terrain-Werkzeuge, `MaterialVariant` und Wolken/Wind (`Clouds`, `GlobalWind`) noch nicht ausgewertet.
- Stand von Cube 3D/4D-Generierung 2026 in der Doku nicht unter diesem Namen auffindbar.

## Verknüpfungen
`map-grundlagen.md`, `04-ui-ux/mobile-first.md`, `08-technik-luau/technik-grundlagen.md`, `06-sound-audio/audio-api-und-upload.md`

## Quellen
- [Creator Docs: Global lighting](https://create.roblox.com/docs/environment/lighting), [Lighting](https://create.roblox.com/docs/reference/engine/classes/Lighting), [Technology](https://create.roblox.com/docs/reference/engine/enums/Technology) – Stand 2026-10-24, ✅
- [Creator Docs: Light sources](https://create.roblox.com/docs/effects/light-sources), [Atmospheric effects](https://create.roblox.com/docs/environment/atmosphere), [Post-processing effects](https://create.roblox.com/docs/environment/post-processing-effects) – ✅
- [Creator Docs: Enhance outdoor environments](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-outdoor-environments), [Enhance indoor environments](https://create.roblox.com/docs/tutorials/use-case-tutorials/lighting/enhance-indoor-environments) – ✅
- [Creator Docs: Instance streaming](https://create.roblox.com/docs/workspace/streaming), [Streaming techniques](https://create.roblox.com/docs/workspace/streaming/techniques), [SLIM](https://create.roblox.com/docs/workspace/streaming/slim), [ModelLevelOfDetail](https://create.roblox.com/docs/reference/engine/enums/ModelLevelOfDetail) – ✅
- [Creator Docs: Design for performance](https://create.roblox.com/docs/performance-optimization/design), [Improve performance](https://create.roblox.com/docs/performance-optimization/improve), [Identify performance issues](https://create.roblox.com/docs/performance-optimization/identify) – ✅
- [Creator Docs: Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications), [PBR textures](https://create.roblox.com/docs/art/modeling/surface-appearance) – ✅
- [Creator Docs: Greybox your environment](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/greybox-your-environment), [Optimize your experience](https://create.roblox.com/docs/tutorials/curriculums/environmental-art/optimize-your-experience) – ✅
- [Creator Docs: The Mystery of Duvall Drive – Stream in immersion](https://create.roblox.com/docs/resources/the-mystery-of-duvall-drive/stream-in-immersion) – ✅
- [Creator Docs: VR guidelines](https://create.roblox.com/docs/production/publishing/vr-guidelines) – ✅
- [Creator Docs: Model generation](https://create.roblox.com/docs/parts/model-generation), [Generative AI](https://create.roblox.com/docs/generative-AI), [Assistant](https://create.roblox.com/docs/assistant/overview), [MCP servers](https://create.roblox.com/docs/assistant/mcp) – ✅
- [DevForum: Real World Building and Scripting Optimization](https://devforum.roblox.com/t/real-world-building-and-scripting-optimization-for-roblox/3127146) – 🟡
- [DevForum: Beta Cube 3D generation tools](https://devforum.roblox.com/t/beta-cube-3d-generation-tools-and-apis-for-creators/3558947), [Roblox Newsroom März 2025](https://about.roblox.com/newsroom/2025/03/unveiling-future-creation-native-3d-generation-collaborative-studio-tools-economy-expansion), [RDC25](https://devforum.roblox.com/t/rdc25-what-we-announced/3920245), [4D Early Access](https://devforum.roblox.com/t/early-access-introducing-in-experience-4d-functional-objects-and-enhanced-3d-generation/4050893) – 🟡
- [DevForum: Future is Bright Phase 3](https://devforum.roblox.com/t/future-is-bright-phase-3-released/878634) – 2020, 🟡
- [Wikipedia: Cube 3D](https://en.wikipedia.org/wiki/Cube_3D) – 🟡
- [DevForum: Future vs ShadowMap](https://devforum.roblox.com/t/future-vs-shadowmap/658587), [nilo.io](https://nilo.io/articles/advanced-roblox-custom-meshes), [santozstudios](https://santozstudios.com/blog/roblox-performance-optimisation-guide/), [HackMD-Notizen](https://hackmd.io/@Mullets/HJb5iUYfO) – 🟠
- [PocketGamer.biz](https://www.pocketgamer.biz/80-of-roblox-users-are-on-mobile-contributing-46-of-robux-revenue) – 🟡
