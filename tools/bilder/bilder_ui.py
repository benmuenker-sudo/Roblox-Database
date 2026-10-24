"""UI-/UX-Referenzbilder (HUD, Shop, Inventar, Farben, Touch, Tutorial, Popups)."""
from svglib import *  # noqa: F401,F403


def legende(s, x, y, w, items, color=BLUE, tsize=18, size=15, gap=10, start=1):
    """Nummerierte Liste rechts neben einem Mockup. items = [(titel, text), ...]"""
    yy = y
    for i, (t, b) in enumerate(items):
        h = callout(s, x, yy, w, t, b, color=color, num=start + i, tsize=tsize, size=size)
        yy += h + gap
    return yy


# ---------------------------------------------------------------------------
def hud_layout_mobile(out):
    s = Svg()
    sheet(s, "HUD-Layout auf dem Handy (Querformat)",
          "Safe Area, Roblox-Top-Bar, Daumen-Zonen und wo welche HUD-Elemente hingehören",
          "ui-hud-layout-mobile.png", "Wichtiges in grüne Zonen, nichts unter Notch/Top-Bar")
    # Telefon
    px, py, pw, ph = 60, 128, 1080, 560
    sx, sy, sw_, sh = px + 24, py + 24, pw - 48, ph - 48
    s.rect(px, py, pw, ph, 64, fill="#121a30", stroke="#060a16", sw=4, extra='filter="url(#schatten)"')
    s.defs_add('<clipPath id="bildschirm"><rect x="%d" y="%d" width="%d" height="%d" rx="40"/></clipPath>' % (sx, sy, sw_, sh))
    s.g('clip-path="url(#bildschirm)"')
    game_world(s, sx, sy, sw_, sh)
    tree(s, sx + 760, sy + 300, 1.3)
    tree(s, sx + 300, sy + 290, 1.0)
    avatar(s, sx + 516, sy + 400, 1.5)
    # Heatmap Daumen-Zonen
    s.rect(sx, sy, sw_, sh, 0, fill=RED, op=0.26)
    for cxp in (sx, sx + sw_):
        g = s.radial([(0, GREEN, 0.85), (0.5, GREEN, 0.75), (0.6, "#ffd23c", 0.7), (0.85, "#ffd23c", 0.4), (1, "#ffd23c", 0)])
        s.ellipse(cxp, sy + sh, 540, 470, fill=g)
    # Safe Area (Notch links, Rand rechts, Home-Indikator unten)
    ins = 56
    s.rect(sx, sy, ins, sh, 0, fill="url(#schraffur)")
    s.rect(sx + sw_ - ins, sy, ins, sh, 0, fill="url(#schraffur)")
    s.rect(sx, sy + sh - 22, sw_, 22, 0, fill="url(#schraffur)")
    # Roblox Top-Bar
    s.rect(sx + ins, sy, sw_ - 2 * ins, 64, 0, fill="url(#schraffurGrau)")
    for i, ic in enumerate(["☰", "💬"]):
        bx = sx + ins + 14 + i * 56
        s.rect(bx, sy + 10, 44, 44, 12, fill="#1b2440", op=0.75)
        if ic == "☰":
            for k in range(3):
                s.rect(bx + 12, sy + 21 + k * 9, 20, 4, 2, fill=WHITE)
        else:
            s.emoji(bx + 22, sy + 32, ic, 24)
    s.rect(sx + sw_ - ins - 58, sy + 10, 44, 44, 12, fill="#1b2440", op=0.75)
    s.text(sx + sw_ - ins - 36, sy + 39, "⋯", 26, WHITE, anchor="middle")
    lbl = "Roblox-Top-Bar (Core-UI): hier keine eigenen Buttons"
    pill(s, sx + sw_ / 2 - tw(lbl, 17) / 2 - 16, sy + 16, tw(lbl, 17) + 32, 34, fill=INK, stroke=WHITE, sw=2, op=0.85)
    s.text(sx + sw_ / 2, sy + 39, lbl, 17, WHITE, anchor="middle")
    # Waehrung oben links
    for i, (ico, val) in enumerate([("coin", "1,2K"), ("gem", "35")]):
        yy = sy + 82 + i * 54
        pill(s, sx + 70, yy, 160, 44, fill="#1b2440", stroke=WHITE, sw=3, op=0.85)
        (coin if ico == "coin" else gem)(s, sx + 94, yy + 22, 16)
        s.text(sx + 122, yy + 31, val, 24, WHITE)
    # Level oben rechts
    pill(s, sx + sw_ - 270, sy + 82, 200, 44, fill="#1b2440", stroke=WHITE, sw=3, op=0.85)
    s.text(sx + sw_ - 252, sy + 112, "Lv 12", 20, GOLD)
    bar(s, sx + sw_ - 180, sy + 95, 98, 18, 0.65, color=BLUE)
    # Ziel oben Mitte
    pill(s, sx + sw_ / 2 - 170, sy + 82, 340, 50, fill=WHITE, stroke=INK, sw=3)
    s.emoji(sx + sw_ / 2 - 140, sy + 107, "🎯", 26)
    s.text(sx + sw_ / 2 - 118, sy + 114, "Ziel: 50 Äpfel", 20, INK)
    bar(s, sx + sw_ / 2 + 50, sy + 97, 100, 20, 0.64, color=GREEN, label="32/50", size=13)
    # Seitenmenue
    for i, ic in enumerate(["🛒", "🎒", "📜"]):
        by = sy + 200 + i * 74
        gbutton(s, sx + 72, by, 60, 60, icon=ic, color="#ffffff", dark="#b8c3da", r=16)
        if i == 0:
            notif_dot(s, sx + 128, by + 4, "!", 12)
        if i == 1:
            notif_dot(s, sx + 128, by + 4, 3, 12)
    # Joystick
    s.circle(sx + 250, sy + 392, 74, fill=WHITE, stroke=WHITE, sw=4, op=0.35)
    s.circle(sx + 262, sy + 382, 32, fill=WHITE, stroke=INK, sw=3, op=0.85)
    # Aktionen unten rechts
    round_button(s, sx + sw_ - 140, sy + 390, 54, color="#ffffff", dark="#b8c3da", icon="⬆️")
    round_button(s, sx + sw_ - 262, sy + 414, 42, color=GREEN, dark=GREEN_D, icon="✋")
    round_button(s, sx + sw_ - 160, sy + 268, 36, color=GOLD, dark=GOLD_D, icon="💰")
    # Mitte frei
    s.rect(sx + 330, sy + 175, 380, 120, 20, fill="none", stroke=WHITE, sw=3, op=0.9, extra='stroke-dasharray="10 8"')
    s.text(sx + 520, sy + 230, "Mitte frei lassen", 22, WHITE, anchor="middle", outline=INK, ow=5)
    s.text(sx + 520, sy + 260, "(nur kurz Popups)", 17, WHITE, anchor="middle", outline=INK, ow=4)
    s.g_end()
    # Notch + Home-Indikator
    s.rect(sx - 2, sy + sh / 2 - 78, 32, 156, 16, fill="#121a30")
    s.circle(sx + 14, sy + sh / 2, 6, fill="#2a3557")
    s.rect(sx + sw_ / 2 - 80, sy + sh - 14, 160, 6, 3, fill=WHITE, op=0.75)
    # Nummern im Telefon
    for n, (bx, by) in enumerate([(sx + 28, sy + 140), (sx + sw_ / 2 - 330, sy + 32), (sx + 250, sy + 104),
                                  (sx + sw_ / 2 + 180, sy + 107), (sx + 160, sy + 230), (sx + 345, sy + 320),
                                  (sx + sw_ - 70, sy + 330), (sx + 520, sy + 155)], start=1):
        badge(s, bx, by, n, BLUE, r=17)
    # Legende Daumenzonen unter dem Telefon
    ly = 712
    s.text(60, ly + 22, "Daumen-Zonen (Querformat, beide Hände):", 19, INK)
    items = [(GREEN, "leicht erreichbar → Aktionen"), ("#ffd23c", "erreichbar → Menüs"),
             (RED, "schwer erreichbar → nur Anzeigen")]
    xx = 60
    for col, t in items:
        s.rect(xx, ly + 40, 34, 26, 7, fill=col, stroke=INK, sw=2, op=0.85)
        s.text(xx + 44, ly + 60, t, 17, INK2, bold=False)
        xx += 54 + tw(t, 17, False) + 26
    s.rect(60, ly + 82, 34, 26, 7, fill="url(#schraffur)", stroke=INK, sw=2)
    s.text(104, ly + 102, "Safe Area: Notch, Rundungen, Home-Indikator (ScreenInsets)", 17, INK2, bold=False)
    s.rect(640, ly + 82, 34, 26, 7, fill="url(#schraffurGrau)", stroke=INK, sw=2)
    s.text(684, ly + 102, "Roblox-Top-Bar / Core-UI", 17, INK2, bold=False)
    # Legende rechts
    legende(s, 1172, 128, 392, [
        ("Safe Area", "Notch und Ränder: nichts Wichtiges hier."),
        ("Roblox-Top-Bar", "Frei lassen (Standard: CoreUISafeInsets)."),
        ("Währung oben links", "Icon + kurze Zahl (1,2K). Max. 1–2 Werte."),
        ("Ziel oben Mitte", "Nur Anzeige, nichts zum Antippen."),
        ("Seitenmenü am Rand", "Icon-Spalte, roter Punkt bei Neuem."),
        ("Joystick unten links", "Roblox-Steuerung nie überdecken."),
        ("Aktionen unten rechts", "Groß, im grünen Daumenbereich."),
        ("Mitte frei", "Sicht aufs Spiel; Popups nur kurz."),
    ], tsize=18, size=15, gap=9)
    s.save(out)


# ---------------------------------------------------------------------------
def hud_simulator(out):
    s = Svg()
    sheet(s, "HUD-Beispiel: Simulator",
          "Fiktives Beispielspiel „Beeren-Rausch Simulator“ – vollständiges HUD mit allen typischen Elementen",
          "ui-hud-beispiel-simulator.png", "6–8 Dauer-Elemente, Rest ins Menü")
    ox, oy, W, H = 40, 122, 1180, 664
    s.defs_add('<clipPath id="mock"><rect x="%d" y="%d" width="%d" height="%d" rx="26"/></clipPath>' % (ox, oy, W, H))
    s.rect(ox - 6, oy - 6, W + 12, H + 12, 30, fill=INK, extra='filter="url(#schatten)"')
    s.g('clip-path="url(#mock)"')
    hy = game_world(s, ox, oy, W, H, horizon=0.4)
    # Weg
    s.path("M%d,%d Q%d,%d %d,%d L%d,%d Q%d,%d %d,%d Z" % (ox + 520, oy + H, ox + 560, oy + 420, ox + 600, hy,
                                                         ox + 640, hy, ox + 660, oy + 420, ox + 760, oy + H),
           fill="#e9d29a", op=0.9)
    # Beerenbuesche
    for (bx, by, sc) in [(ox + 330, oy + 430, 1.0), (ox + 820, oy + 440, 1.1), (ox + 420, oy + 330, 0.7),
                         (ox + 760, oy + 320, 0.65), (ox + 1000, oy + 520, 1.2)]:
        s.ellipse(bx, by + 30 * sc, 70 * sc, 14 * sc, fill="#000", op=0.15)
        s.circle(bx - 34 * sc, by, 40 * sc, fill="#2b8a36", stroke=INK, sw=2)
        s.circle(bx + 30 * sc, by - 4 * sc, 44 * sc, fill="#2b8a36", stroke=INK, sw=2)
        s.circle(bx, by - 30 * sc, 42 * sc, fill="#3fae47", stroke=INK, sw=2)
        for (dx, dy, c) in [(-40, -10, "#e8334a"), (-10, -45, "#7a3cff"), (25, -20, "#e8334a"), (40, 10, "#ff7ab6"),
                            (-20, 12, "#7a3cff"), (5, -5, "#e8334a")]:
            s.circle(bx + dx * sc, by + dy * sc, 9 * sc, fill=c, stroke=INK, sw=1.5)
    tree(s, ox + 150, hy + 40, 1.4)
    tree(s, ox + 1090, hy + 60, 1.6)
    avatar(s, ox + 600, oy + 560, 1.35, shirt="#e8334a")
    s.emoji(ox + 690, oy + 540, "🐶", 52)
    # schwebende Belohnungen
    for (fx, fy, t, op_) in [(ox + 345, oy + 345, "+25", 1), (ox + 380, oy + 300, "+25", 0.7)]:
        coin(s, fx - 22, fy - 8, 13)
        s.text(fx, fy, t, 26, GOLD, outline=INK, ow=5, op=op_)
    # Top-Bar-Platzhalter
    for i in range(2):
        s.rect(ox + 18 + i * 52, oy + 12, 42, 42, 12, fill="#1b2440", op=0.6)
    # Waehrungen
    vals = [("coin", "1,2K"), ("gem", "348"), ("rb", "Rebirth 3")]
    for i, (ic, v) in enumerate(vals):
        yy = oy + 66 + i * 52
        pill(s, ox + 18, yy, 210, 44, fill="#1b2440", stroke=WHITE, sw=3, op=0.88)
        if ic == "coin":
            coin(s, ox + 42, yy + 22, 15)
        elif ic == "gem":
            gem(s, ox + 42, yy + 22, 15)
        else:
            s.emoji(ox + 42, yy + 22, "🌟", 24)
        s.text(ox + 66, yy + 31, v, 22 if i < 2 else 19, WHITE)
        if i < 2:
            gbutton(s, ox + 190, yy + 7, 30, 30, "+", color=GREEN, dark=GREEN_D, size=22, r=9, sw=2)
    s.text(ox + 236, oy + 84, "+25", 18, GOLD, outline=INK, ow=4)
    # Boosts
    for i, (ic, t, col) in enumerate([("💰", "14:32", WHITE), ("🍀", "04:10", WHITE), ("⚡", "0:45", "#ffb3bb")]):
        bx = ox + 18 + i * 72
        s.rect(bx, oy + 228, 60, 60, 16, fill=WHITE, stroke=INK, sw=3)
        s.emoji(bx + 30, oy + 250, ic, 26)
        s.text(bx + 30, oy + 282, "2×" if i == 0 else ("+50%" if i == 1 else "3×"), 13, INK, anchor="middle")
        pill(s, bx + 2, oy + 294, 56, 24, fill=INK if i < 2 else RED, stroke=WHITE, sw=2)
        s.text(bx + 30, oy + 311, t, 14, col if i < 2 else WHITE, anchor="middle")
    # Seitenmenue
    for i, (ic, lbl) in enumerate([("🛒", "Shop"), ("🐾", "Tiere"), ("📖", "Sammlung")]):
        by = oy + 350 + i * 96
        gbutton(s, ox + 18, by, 58, 58, icon=ic, color=WHITE, dark="#b8c3da", r=16)
        s.text(ox + 47, by + 76, lbl, 13, WHITE, anchor="middle", outline=INK, ow=3.5)
        if i == 0:
            notif_dot(s, ox + 72, by + 4, "!", 12)
        if i == 1:
            notif_dot(s, ox + 72, by + 4, 3, 12)
    # Event-Banner oben Mitte
    bw = 470
    s.rect(ox + W / 2 - bw / 2, oy + 14, bw, 52, 18, fill=s.gradient([(0, "#ff9a1f"), (1, "#ff3d7f")], x2=1, y2=0),
           stroke=INK, sw=3, extra='filter="url(#schattenK)"')
    s.emoji(ox + W / 2 - bw / 2 + 30, oy + 40, "🎉", 28)
    s.text(ox + W / 2 + 14, oy + 38, "Beeren-Fest: 2× Drops", 20, WHITE, anchor="middle", outline=INK, ow=4)
    s.text(ox + W / 2 + 14, oy + 58, "endet in 1 Std 12 Min", 14, WHITE, anchor="middle", outline=INK, ow=3)
    # Aufgaben
    qx, qy, qw = ox + W - 290, oy + 80, 270
    s.rect(qx, qy, qw, 214, 18, fill="#1b2440", stroke=WHITE, sw=3, op=0.9)
    s.emoji(qx + 24, qy + 24, "📜", 22)
    s.text(qx + 42, qy + 32, "Aufgaben", 19, WHITE)
    for i, (t, f, lbl, rw) in enumerate([("Sammle 200 Beeren", 0.7, "140/200", "500"), ("Verkaufe 3×", 0.66, "2/3", "200"),
                                         ("Finde 1 Glitzerbeere", 0.0, "0/1", "1")]):
        yy = qy + 52 + i * 54
        s.text(qx + 14, yy + 16, t, 15, WHITE)
        bar(s, qx + 14, yy + 24, 180, 18, f, color=GREEN, label=lbl, size=12)
        if i < 2:
            coin(s, qx + 216, yy + 28, 10)
        else:
            gem(s, qx + 216, yy + 28, 10)
        s.text(qx + 232, yy + 34, rw, 14, GOLD)
    # Toast
    tx, ty = qx - 10, qy + 236
    s.rect(tx, ty, 290, 60, 16, fill=WHITE, stroke=PURPLE, sw=4, extra='filter="url(#schattenK)"')
    s.emoji(tx + 32, ty + 30, "✨", 30)
    s.text(tx + 58, ty + 26, "Seltene Beere gefunden!", 16, PURPLE)
    s.text(tx + 58, ty + 47, "+1 Glitzerbeere (Episch)", 14, INK2, bold=False)
    # Rucksack
    s.emoji(ox + W / 2 - 230, oy + H - 48, "🎒", 34)
    bar(s, ox + W / 2 - 200, oy + H - 64, 380, 34, 0.87, color=ORANGE, label="Rucksack 87/100", size=17)
    tag(s, ox + W / 2 + 50, oy + H - 104, "Fast voll!", RED, 14)
    # Joystick
    s.circle(ox + 210, oy + H - 100, 62, fill=WHITE, stroke=WHITE, sw=4, op=0.3)
    s.circle(ox + 218, oy + H - 108, 26, fill=WHITE, stroke=INK, sw=3, op=0.8)
    # Verkaufen + Sprung
    gbutton(s, ox + W - 340, oy + H - 112, 210, 70, "VERKAUFEN", color=GREEN, dark=GREEN_D, size=24, icon="💰", icon_size=34)
    round_button(s, ox + W - 70, oy + H - 82, 46, color=WHITE, dark="#b8c3da", icon="⬆️")
    s.g_end()
    # Nummern
    for n, (bx, by) in enumerate([(ox + 300, oy + 88), (ox + 236, oy + 258), (ox + W / 2 + 250, oy + 40),
                                  (qx - 16, qy + 20), (ox + 100, oy + 368), (ox + W / 2 - 262, oy + H - 48),
                                  (ox + W - 350, oy + H - 118), (tx - 14, ty + 30), (ox + 600, oy + 400)], start=1):
        badge(s, bx, by, n, BLUE, r=16)
    legende(s, 1248, 122, 320, [
        ("Währungen", "Icon + Kurzformat (1,2K), Anstieg animiert."),
        ("Boosts mit Timer", "Ablaufende Boosts rot markieren."),
        ("Event-Banner", "Oben Mitte, ehrliche Restzeit."),
        ("Aufgaben-Tracker", "1–3 Ziele, Balken, Belohnung sichtbar."),
        ("Seitenmenü", "Roter Punkt / Zahl bei Neuem."),
        ("Rucksack-Anzeige", "Zeigt, wann Verkaufen nötig ist."),
        ("Verkaufen-Button", "Groß, unten rechts, Daumen-Zone."),
        ("Toast", "Kurze Meldung, 2–4 s, dann weg."),
        ("Spielwelt frei", "Mitte bleibt für die Aktion."),
    ], tsize=17, size=14, gap=7)
    s.save(out)


