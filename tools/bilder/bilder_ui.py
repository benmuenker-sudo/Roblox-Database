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


# ---------------------------------------------------------------------------
def fenster_kopf(s, x, y, w, titel, icon, farbe1=BLUE, farbe2=PURPLE, close=True, h=78):
    """Fenster-Kopfzeile im Roblox-Stil mit grossem X."""
    s.rect(x, y, w, h, 22, fill=s.gradient([(0, farbe1), (1, farbe2)], x2=1, y2=0), stroke=INK, sw=4)
    s.rect(x + 4, y + h - 22, w - 8, 18, 0, fill=farbe2, op=0.0)
    s.emoji(x + 44, y + h / 2, icon, 38)
    s.text(x + 76, y + h / 2 + 13, titel, 36, WHITE, outline=INK, ow=6)
    if close:
        gbutton(s, x + w - 84, y + 8, 64, 60, "✕", color=RED, dark=RED_D, size=34, r=16)


def shop_layout(out):
    s = Svg()
    sheet(s, "Shop-Layout: Aufbau und Kauf-Bestätigung",
          "Tabs, „Beliebt“-Bereich, Produktkarten mit Nutzen und Preis, großes X und Bestätigungsdialog",
          "ui-shop-layout.png", "Preis und Nutzen immer sichtbar, Bestätigung vor Kauf")
    X, Y, W, H = 40, 122, 960, 712
    panel(s, X, Y, W, H, fill="#eef3ff")
    fenster_kopf(s, X, Y, W, "SHOP", "🛒")
    w, h = tag(s, X + W - 104, Y + 26, "Großer Schließen-Button", INK, 15, anchor="end")
    arrow(s, X + W - 100, Y + 40, X + W - 88, Y + 40, color=INK, bend=0, shorten=0)
    # Tabs
    tx = X + 22
    for i, t in enumerate(["⭐ Beliebt", "Boosts", "Komfort", "Kosmetik", "Pakete"]):
        tw_ = tw(t, 17) + 30
        if i == 0:
            gbutton(s, tx, Y + 96, tw_, 46, t, color=GOLD, dark=GOLD_D, size=17, r=14)
        else:
            gbutton(s, tx, Y + 96, tw_, 46, t, color=WHITE, dark="#b8c3da", size=17, r=14, text_color=INK2, outline=False)
        tx += tw_ + 10
    tag(s, X + W - 22, Y + 106, "Aktiver Tab markiert, max. 5–7", INK2, 14, anchor="end")
    # Beliebt-Banner
    by = Y + 166
    s.rect(X + 22, by, W - 44, 140, 20, fill=s.gradient([(0, "#8d4dff"), (1, "#ff3d9a")], x2=1, y2=0), stroke=INK, sw=4)
    s.rect(X + 30, by + 8, W - 60, 40, 14, fill=WHITE, op=0.15)
    s.emoji(X + 100, by + 70, "🎁", 80)
    tag(s, X + 168, by + 14, "BELIEBT", GOLD_D, 14)
    s.text(X + 170, by + 76, "Starter-Paket", 30, WHITE, outline=INK, ow=5)
    s.text(X + 170, by + 106, "5.000 Münzen + 2× Geld (30 Min) + Haustier", 17, WHITE, outline=INK, ow=3.5)
    s.text(X + 170, by + 128, "Einmalig, ehrlicher Wert, kein Fake-Timer", 14, "#ffe9a8")
    pill(s, X + W - 250, by + 26, 120, 44, fill=WHITE, stroke=INK, sw=3)
    robux(s, X + W - 222, by + 48, 13)
    s.text(X + W - 202, by + 57, "99", 24, INK)
    gbutton(s, X + W - 250, by + 80, 200, 46, "Kaufen", color=GREEN, dark=GREEN_D, size=21)
    # Produktkarten
    cards = [("💰", "2× Geld", "Doppeltes Geld für 15 Minuten.", "49", "Boost", GOLD),
             ("🍀", "Glücks-Trank", "+50 % Glück für 10 Minuten.", "35", "Boost", GREEN),
             ("🎒", "Großer Rucksack", "+50 Plätze, dauerhaft.", "149", "Komfort", BLUE),
             ("✨", "Glitzer-Spur", "Funkelnde Spur hinter dir.", "75", "Kosmetik", PURPLE)]
    cw, ch, cy = (W - 44 - 3 * 18) / 4, 338, Y + 326
    for i, (ic, name, nutzen, preis, kat, col) in enumerate(cards):
        cx = X + 22 + i * (cw + 18)
        s.rect(cx, cy, cw, ch, 20, fill=WHITE, stroke=INK, sw=3.5, extra='filter="url(#schattenK)"')
        s.rect(cx + 10, cy + 10, cw - 20, 120, 14, fill=col, op=0.22)
        s.emoji(cx + cw / 2, cy + 70, ic, 70)
        tag(s, cx + 16, cy + 18, kat, col if col != GOLD else GOLD_D, 12)
        s.text(cx + cw / 2, cy + 164, name, 20, INK, anchor="middle")
        s.textbox(cx + cw / 2, cy + 176, nutzen, cw - 60, 15, INK2, anchor="middle")
        pill(s, cx + cw / 2 - 55, cy + 226, 110, 40, fill="#f3f6ff", stroke=INK, sw=2.5)
        robux(s, cx + cw / 2 - 28, cy + 246, 12)
        s.text(cx + cw / 2 - 8, cy + 254, preis, 21, INK)
        gbutton(s, cx + 14, cy + 276, cw - 28, 46, "Kaufen", color=GREEN, dark=GREEN_D, size=20)
    # Nummern auf erster Karte
    cx0 = X + 22
    for n, (bx, by_) in enumerate([(cx0 + cw - 22, cy + 30), (cx0 + 22, cy + 158), (cx0 + 15, cy + 200),
                                   (cx0 + cw / 2 + 70, cy + 246), (cx0 + cw - 16, cy + 299)], start=1):
        badge(s, bx, by_, n, ORANGE, r=14)
    s.text(X + 24, Y + H - 16, "Karte:  ① Icon   ② Name   ③ Nutzen in einem Satz   ④ Preis mit Robux-Symbol   ⑤ Kaufbutton", 16, INK2)
    # Bestaetigungsdialog
    dx, dy, dw, dh = 1030, 122, 540, 360
    s.rect(dx - 10, dy - 6, dw + 20, dh + 16, 30, fill=INK, op=0.08)
    panel(s, dx, dy, dw, dh, fill=WHITE)
    s.rect(dx, dy, dw, 62, 22, fill=GREEN, stroke=INK, sw=4)
    s.text(dx + dw / 2, dy + 41, "Kauf bestätigen?", 26, WHITE, anchor="middle", outline=INK, ow=5)
    s.rect(dx + 26, dy + 84, 120, 120, 20, fill=GOLD, op=0.25)
    s.emoji(dx + 86, dy + 144, "💰", 74)
    s.text(dx + 168, dy + 112, "2× Geld (15 Min)", 24, INK)
    s.textbox(dx + 168, dy + 122, "Wirkung: Doppeltes Geld für 15 Minuten. Startet sofort.", dw - 196, 16, INK2)
    s.text(dx + 168, dy + 196, "Preis:", 20, INK2, bold=False)
    robux(s, dx + 254, dy + 189, 14)
    s.text(dx + 276, dy + 198, "49", 28, INK)
    gbutton(s, dx + 26, dy + 230, 230, 60, "Abbrechen", color="#dfe5f2", dark="#a8b3cc", size=22, text_color=INK2, outline=False)
    gbutton(s, dx + dw - 256, dy + 230, 230, 60, "Kaufen", color=GREEN, dark=GREEN_D, size=24)
    s.text(dx + dw / 2, dy + 330, "Danach folgt der offizielle Roblox-Kaufdialog.", 15, MUTED, anchor="middle", bold=False)
    # Do / Don't
    def liste(x, y, w, titel, farbe, zeichen, items):
        h = 330
        panel(s, x, y, w, h, fill=WHITE, stroke=farbe)
        s.rect(x, y, w, 48, 22, fill=farbe, stroke=farbe, sw=4)
        s.text(x + w / 2, y + 33, titel, 22, WHITE, anchor="middle", outline=INK, ow=4)
        yy = y + 64
        for it in items:
            s.circle(x + 28, yy + 13, 13, fill=farbe)
            s.text(x + 28, yy + 19, zeichen, 16, WHITE, anchor="middle")
            hh = s.textbox(x + 50, yy - 2, it, w - 64, 16, INK)
            yy += max(30, hh) + 10
    liste(1030, 508, 262, "Do", GREEN, "✔", ["Preis immer sichtbar", "Nutzen in einem Satz", "Großes X, Tippen außerhalb schließt",
                                          "Bestätigung vor jedem Kauf", "Erfolg sofort sichtbar"])
    liste(1308, 508, 262, "Don't", RED, "✘", ["Fake-Timer („Nur noch 2 Min!“)", "Schuld-Texte („Du verpasst…“)",
                                           "Versteckte Preise", "Winziges X", "Fortschritt nur gegen Robux"])
    s.save(out)


# ---------------------------------------------------------------------------
def slot(s, x, y, size, emoji_, r_idx, label=True, extra=None):
    name, de, col, dark, hx, sym = RARITY[r_idx]
    if r_idx == 5:
        s.rect(x - 6, y - 6, size + 12, size + 12, 20, fill=col, op=0.35, extra='filter="url(#glow)"')
    s.rect(x, y, size, size, 16, fill=s.gradient([(0, WHITE), (1, col, 0.45)]), stroke=col, sw=6)
    s.rect(x, y, size, size, 16, fill="none", stroke=INK, sw=2)
    s.emoji(x + size / 2, y + size * 0.42, emoji_, size * 0.5)
    if label:
        s.rect(x + 3, y + size - 28, size - 6, 25, 10, fill=col)
        s.text(x + size / 2, y + size - 10, sym + " " + de, 13 if len(de) < 11 else 11.5, WHITE, anchor="middle",
               outline=dark, ow=3)


def inventar(out):
    s = Svg()
    sheet(s, "Inventar mit Seltenheitsrahmen",
          "Raster, Sortieren/Filtern, Platz-Anzeige, Mehrfachauswahl mit Sicherheitsabfrage – und die Farb-Konvention",
          "ui-inventar-seltenheit.png", "Seltenheit = Farbe + Symbol, Platz-Anzeige X/Y")
    X, Y, W, H = 40, 122, 1010, 712
    panel(s, X, Y, W, H, fill="#eef3ff")
    fenster_kopf(s, X, Y, W, "Inventar", "🎒", farbe1="#ff9a1f", farbe2="#ff5d3d")
    pill(s, X + W - 300, Y + 18, 190, 42, fill=INK, stroke=WHITE, sw=3)
    s.text(X + W - 205, Y + 46, "47/60 Plätze", 19, WHITE, anchor="middle")
    # Filterleiste
    fy = Y + 96
    pill(s, X + 22, fy, 270, 44, fill=WHITE, stroke=INK, sw=3)
    s.text(X + 40, fy + 29, "Sortieren: Seltenheit ▾", 17, INK)
    xx = X + 308
    for i, c in enumerate(["Alle", "Neu", "Haustiere", "Werkzeuge"]):
        cw = tw(c, 16) + 30
        pill(s, xx, fy + 2, cw, 40, fill=BLUE if i == 0 else WHITE, stroke=INK, sw=2.5)
        s.text(xx + cw / 2, fy + 28, c, 16, WHITE if i == 0 else INK2, anchor="middle")
        xx += cw + 8
    pill(s, xx + 6, fy, X + W - 22 - xx - 6, 44, fill=WHITE, stroke=INK, sw=3)
    s.text(xx + 22, fy + 29, "🔍 Suchen …", 16, MUTED, bold=False)
    # Raster
    items = [("🐉", 5), ("🦄", 4), ("🔥", 4), ("🦊", 3), ("🐙", 3), ("💎", 3), ("🐢", 2),
             ("🐸", 2), ("🍄", 2), ("🐝", 1), ("🌵", 1), ("🐰", 1), ("🐟", 0), ("🐌", 0),
             ("🥕", 0), ("🪨", 0), ("🐭", 0), (None, 0), (None, 0), (None, 0), (None, 0)]
    sz, gap = 118, 16
    gx0, gy0 = X + (W - (7 * sz + 6 * gap)) / 2, Y + 166
    for i, (e, r) in enumerate(items):
        gx, gy = gx0 + (i % 7) * (sz + gap), gy0 + (i // 7) * (sz + gap)
        if e is None:
            s.rect(gx, gy, sz, sz, 16, fill="#dfe6f5", stroke="#aab5cc", sw=3, extra='stroke-dasharray="8 6"')
            continue
        slot(s, gx, gy, sz, e, r)
        if i == 2:
            tag(s, gx + sz - 8, gy - 8, "NEU", RED, 12, anchor="end")
        if i == 3:
            s.circle(gx + sz - 14, gy + 14, 14, fill=GREEN, stroke=WHITE, sw=2.5)
            s.text(gx + sz - 14, gy + 20, "✔", 15, WHITE, anchor="middle")
        if i == 1:
            s.emoji(gx + 20, gy + 20, "🔒", 20)
        if i in (12, 13, 14):
            s.rect(gx - 4, gy - 4, sz + 8, sz + 8, 18, fill="none", stroke=BLUE, sw=5)
            s.rect(gx + 8, gy + 8, 26, 26, 7, fill=BLUE, stroke=WHITE, sw=2)
            s.text(gx + 21, gy + 28, "✔", 17, WHITE, anchor="middle")
    # Aktionsleiste
    ay = Y + H - 118
    s.rect(X + 22, ay, W - 44, 96, 18, fill=WHITE, stroke=INK, sw=3)
    s.text(X + 44, ay + 38, "Mehrfachauswahl: 3 gewählt", 20, INK)
    s.text(X + 44, ay + 70, "⚠ Ab Episch: Sicherheitsabfrage vor Verkauf", 16, RED_D)
    gbutton(s, X + W - 470, ay + 22, 190, 54, "Ausrüsten", color=BLUE, dark=BLUE_D, size=20)
    gbutton(s, X + W - 262, ay + 22, 218, 54, "Verkaufen (3)", color=RED, dark=RED_D, size=20)
    # Hinweise
    for n, (bx, by) in enumerate([(X + W - 300, Y + 22), (X + 30, fy + 4), (gx0 + 3 * (sz + gap) + sz - 2, gy0 + 34),
                                  (gx0 + 2 * (sz + gap) + sz - 4, gy0 + 30), (gx0 - 6, gy0 + 2 * (sz + gap) + 4)], start=1):
        badge(s, bx, by, n, BLUE, r=14)
    # Legende
    lx, ly, lw = 1076, 122, 494
    panel(s, lx, ly, lw, 712, fill=WHITE)
    s.text(lx + 24, ly + 42, "Seltenheits-Konvention", 24, INK)
    s.text(lx + 24, ly + 68, "Spieler kennen diese Reihenfolge aus vielen Spielen.", 15, MUTED, bold=False)
    for i, (en, de, col, dark, hx, sym) in enumerate(RARITY):
        yy = ly + 88 + i * 74
        slot(s, lx + 24, yy, 62, ["🐟", "🐝", "🦊", "🦄", "🔥", "🐉"][i], i, label=False)
        s.text(lx + 104, yy + 26, "%s %s" % (sym, de), 21, dark)
        s.text(lx + 104, yy + 50, "%s · %s" % (en, hx), 16, INK2, bold=False)
        s.text(lx + lw - 24, yy + 38, ["60 %", "25 %", "10 %", "4 %", "0,9 %", "0,1 %"][i], 17, MUTED, anchor="end")
    yy = ly + 88 + 6 * 74 + 4
    s.rect(lx + 20, yy, lw - 40, 170, 16, fill=NOTE, stroke=GOLD_D, sw=2.5)
    s.text(lx + 36, yy + 30, "Legende der Nummern", 17, INK)
    for k, t in enumerate(["① Platz-Anzeige 47/60  ② Sortieren + Filter-Chips",
                           "③ Ausgerüstet-Haken  ④ NEU-Markierung",
                           "⑤ Mehrfachauswahl (blau)  🔒 = gesperrt/Favorit",
                           "Symbol + Farbe: auch farbenblind lesbar.",
                           "Chancen rechts = Beispielwerte (siehe Gacha)."]):
        s.text(lx + 36, yy + 58 + k * 24, t, 14.5, INK2, bold=(k == 3))
    s.save(out)


# ---------------------------------------------------------------------------
def sammelbuch(out):
    s = Svg()
    sheet(s, "Sammelbuch / Katalog",
          "Gesammelt hell, fehlend als Silhouette, Fortschritt 34/120 und Belohnungen an Meilensteinen",
          "ui-sammelbuch.png", "Fehlendes sichtbar machen, Teilziele belohnen")
    X, Y, W, H = 40, 122, 1110, 712
    s.rect(X, Y, W, H, 30, fill="#8a4b22", stroke=INK, sw=4, extra='filter="url(#schatten)"')
    # Reiter
    for i, (t, c) in enumerate([("🌲", GREEN), ("🏜️", GOLD), ("❄️", BLUE), ("🌋", RED), ("❓", PURPLE)]):
        ty_ = Y + 120 + i * 92
        s.rect(X + W - 14, ty_, 64 if i == 0 else 52, 78, 12, fill=c, stroke=INK, sw=3)
        s.emoji(X + W + (22 if i == 0 else 16), ty_ + 39, t, 28)
    s.rect(X + 18, Y + 18, W - 36, H - 36, 20, fill="#fff6e3", stroke=INK, sw=3)
    s.line(X + W / 2, Y + 100, X + W / 2, Y + H - 140, stroke="#d9c49a", sw=4)
    s.text(X + 44, Y + 66, "📖 Sammelbuch · Wald", 28, "#6b3a16")
    bar(s, X + 470, Y + 42, 420, 34, 34 / 120, color=GREEN, label="34 / 120 gesammelt (28 %)", size=16)
    # Seiten
    beispiele = [("🦊", 3, True), ("🐿️", 1, True), ("🦉", 2, True), ("🐞", 0, True), ("🍄", 0, True), ("🦔", 1, True),
                 ("🐺", 3, False), ("🦌", 2, True), ("🐗", 1, False), ("🌲", 0, True), ("🦋", 2, True), ("🐉", 5, False),
                 ("🐸", 1, True), ("🐌", 0, True), ("🦡", 2, False), ("🐻", 0, False), ("🐝", 1, True), ("🌼", 0, True),
                 ("🐍", 2, False), ("🦄", 4, False), ("🐛", 0, True), ("🕷️", 1, False), ("🦜", 3, True), ("🦚", 4, False)]
    sz, gap = 104, 18
    for page in range(2):
        px0 = X + 50 + page * (W / 2 - 18)
        for k in range(12):
            e, r, have = beispiele[page * 12 + k]
            gx, gy = px0 + (k % 4) * (sz + gap), Y + 104 + (k // 4) * (sz + 40)
            if have:
                slot(s, gx, gy, sz, e, r, label=False)
                s.text(gx + sz / 2, gy + sz + 22, RARITY[r][1], 14, RARITY[r][3], anchor="middle")
            else:
                s.rect(gx, gy, sz, sz, 16, fill="#e8dcc2", stroke="#b8a37a", sw=4, extra='stroke-dasharray="9 6"')
                s.emoji(gx + sz / 2, gy + sz * 0.45, e, sz * 0.52, op=0.85, extra='filter="url(#silhouette)"')
                s.text(gx + sz / 2, gy + sz - 12, "?", 22, "#8a7a5a", anchor="middle")
                if page == 1 and k == 7:
                    s.text(gx + sz / 2, gy + sz + 22, "💡 Tipp", 14, BLUE_D, anchor="middle")
                else:
                    s.text(gx + sz / 2, gy + sz + 22, "???", 14, "#a08d66", anchor="middle")
        if page == 0:
            tag(s, px0 + sz - 6, Y + 96, "NEU", RED, 12, anchor="end")
    # Meilensteine
    my = Y + H - 178
    s.rect(X + 18, my - 4, W - 36, Y + H - 18 - my + 4, 0, fill="#f3e3c0")
    s.text(X + 44, my + 62, "Meilen-", 19, "#6b3a16")
    s.text(X + 44, my + 86, "steine", 19, "#6b3a16")
    x0, x1 = X + 230, X + W - 80
    s.line(x0, my + 62, x1, my + 62, stroke="#c9b48a", sw=12)
    s.line(x0, my + 62, x0 + (x1 - x0) * 34 / 120, my + 62, stroke=GREEN, sw=12)
    for val, ic, lbl in [(10, "🪙", "Münzen"), (25, "🐾", "Tier-Slot"), (50, "🏷️", "Titel"),
                         (75, "✨", "Aura"), (100, "👑", "Krone"), (120, "🏆", "Goldrahmen")]:
        mx = x0 + (x1 - x0) * val / 120
        done = val <= 34
        s.circle(mx, my + 62, 28, fill=GREEN if done else (GOLD if val == 50 else "#e8dcc2"), stroke=INK, sw=3)
        s.emoji(mx, my + 61, ic, 28)
        s.text(mx, my + 118, str(val), 17, INK, anchor="middle")
        s.text(mx, my + 140, lbl, 14, INK2 if not done else GREEN_D, anchor="middle")
        if done:
            s.circle(mx + 20, my + 40, 11, fill=GREEN_D, stroke=WHITE, sw=2)
            s.text(mx + 20, my + 45, "✔", 12, WHITE, anchor="middle")
    tag(s, x0 + (x1 - x0) * 50 / 120 + 36, my + 20, "nächstes Ziel: 34/50", GOLD_D, 13)
    # Erklaerungen
    cx = 1218
    callout(s, cx, 122, 350, "Fortschritt X/Y", "Zahl + Balken oben. Prozent hilft bei großen Büchern.", target=(X + 900, Y + 59),
            color=GREEN, num=1)
    callout(s, cx, 262, 350, "Silhouetten statt Leere", "Fehlende Items als Umriss mit „?“ wecken Neugier.",
            target=(1097, Y + 156), color=PURPLE, num=2)
    callout(s, cx, 402, 350, "Hinweis zum Fundort", "Antippen zeigt z. B. „Eis-Zone, nachts“: ein konkretes Ziel.",
            target=(1097, Y + 300), color=BLUE, num=3)
    callout(s, cx, 542, 350, "Kategorien als Reiter", "Zonen/Sets getrennt, jedes mit eigenem Fortschritt.",
            target=(X + W + 36, Y + 120 + 3 * 92 + 39), color=ORANGE, num=4)
    callout(s, cx, 682, 350, "Belohnung an Meilensteinen", "Teilziele (10/25/50 …) belohnen schon früh.",
            target=(x1 + 30, my + 62), color=GOLD_D, num=5)
    s.save(out)


# ---------------------------------------------------------------------------
def farbpalette(out):
    s = Svg()
    sheet(s, "Farben und ihre Bedeutung",
          "Konsistente Signalfarben, Seltenheitsfarben mit Hex-Codes und der Farbenblind-Tipp „Icon + Farbe“",
          "ui-farbpalette-bedeutung.png", "Gleiche Bedeutung = gleiche Farbe, nie nur Farbe")
    karten = [(GREEN, GREEN_D, "#2ECC71", "Grün", "Bestätigen, positiv", "✔ Kaufen", "Ja, Fertig, +Belohnung, Erfolg"),
              (RED, RED_D, "#FF4D5E", "Rot", "Gefahr, Abbrechen, Fehler", "✘ Löschen", "Schaden, Warnung, Neu-Punkt"),
              (GOLD, GOLD_D, "#FFC93C", "Gold / Gelb", "Währung, Premium", "💰 1,2K", "Münzen, Robux-Angebote, VIP"),
              (BLUE, BLUE_D, "#3D9BFF", "Blau", "Info, Navigation", "ℹ Details", "Hinweise, Tabs, Links, Hilfe")]
    cw = (1520 - 3 * 24) / 4
    for i, (c, d, hx, name, bed, btn, bsp) in enumerate(karten):
        x = 40 + i * (cw + 24)
        y = 124
        panel(s, x, y, cw, 290, fill=WHITE)
        s.rect(x, y, cw, 96, 22, fill=c, stroke=INK, sw=4)
        s.text(x + 22, y + 46, name, 28, WHITE, outline=INK, ow=5)
        s.text(x + 22, y + 78, hx, 20, WHITE, outline=d, ow=4)
        s.text(x + 22, y + 132, bed, 20, INK)
        s.textbox(x + 22, y + 142, "z. B. " + bsp, cw - 44, 16, INK2)
        lbl = btn
        if btn.startswith("💰"):
            gbutton(s, x + 22, y + 210, cw - 44, 56, btn[2:], color=c, dark=d, size=24, icon="💰", icon_size=30)
        else:
            gbutton(s, x + 22, y + 210, cw - 44, 56, lbl, color=c, dark=d, size=24)
    # Seltenheit
    y = 442
    panel(s, 40, y, 1520, 176, fill=WHITE)
    s.text(64, y + 38, "Seltenheitsfarben (Konvention bei Sammelspielen)", 22, INK)
    rw = (1520 - 48 - 5 * 16) / 6
    for i, (en, de, c, d, hx, sym) in enumerate(RARITY):
        x = 64 + i * (rw + 16)
        s.rect(x, y + 56, rw, 100, 16, fill=s.gradient([(0, c), (1, d)]), stroke=INK, sw=3)
        s.text(x + 16, y + 92, sym + " " + de, 20, WHITE, outline=d, ow=4)
        s.text(x + 16, y + 118, en, 15, WHITE, outline=d, ow=3)
        s.text(x + 16, y + 142, hx, 16, WHITE, outline=d, ow=3)
    # Farbenblind
    y = 646
    panel(s, 40, y, 980, 196, fill=WHITE)
    s.text(64, y + 36, "Farbenblind-sicher: nie nur Farbe als Information", 22, INK)
    s.text(64, y + 64, "Oben: so sieht es normal aus · Unten: Simulation ohne Farbe (Graustufen)", 15, MUTED, bold=False)

    def paar(x, mit_icon):
        for row, filt in enumerate([None, "grau"]):
            yy = y + 80 + row * 56
            if filt:
                s.g('filter="url(#grau)"')
            gbutton(s, x, yy, 150, 44, "✔ Ja" if mit_icon else "Ja", color=GREEN, dark=GREEN_D, size=20)
            gbutton(s, x + 166, yy, 150, 44, "✘ Nein" if mit_icon else "Nein", color=RED, dark=RED_D, size=20)
            if filt:
                s.g_end()
    paar(64, False)
    paar(540, True)
    s.text(440, y + 122, "✘", 40, RED, anchor="middle")
    s.text(440, y + 160, "nur Farbe", 15, RED_D, anchor="middle")
    s.text(935, y + 122, "✔", 40, GREEN, anchor="middle")
    s.text(935, y + 160, "+ Icon/Form", 15, GREEN_D, anchor="middle")
    # Palette-Regel
    x = 1044
    panel(s, x, y, 516, 196, fill=WHITE)
    s.text(x + 24, y + 36, "Palette begrenzen", 22, INK)
    for i, (c, t) in enumerate([("#3d9bff", "1 Hauptfarbe"), ("#ff9a1f", "1–2 Akzente"), ("#1b2440", "Neutral dunkel"),
                                ("#eef3ff", "Neutral hell")]):
        xx = x + 24 + i * 120
        s.rect(xx, y + 56, 100, 60, 12, fill=c, stroke=INK, sw=2.5)
        s.text(xx + 50, y + 138, t, 13, INK2, anchor="middle")
    s.text(x + 24, y + 176, "Kontrast: hell auf dunkel – nie Grau auf Grau.", 15, INK)
    s.save(out)


# ---------------------------------------------------------------------------
def touch_groessen(out):
    s = Svg()
    sheet(s, "Touch-Größen, Abstände und Schriftgrößen",
          "Maßstab 1:1 in Pixeln bei 1× Skalierung – Richtwerte zum Testen, nicht als feste Regel",
          "ui-touch-groessen.png", "Buttons ≥ 44–48 px, Abstand, Text ≥ 14–16 px")

    def finger(cx, cy):
        s.ellipse(cx, cy, 27, 33, fill="#f2b38a", stroke=INK, sw=2.5, op=0.75)
        s.ellipse(cx, cy - 10, 14, 12, fill=WHITE, op=0.35)

    def mass(x1, y1, x2, y2, label, col=INK, below=True):
        s.line(x1, y1, x2, y2, stroke=col, sw=2)
        s.line(x1, y1 - 7, x1, y1 + 7, stroke=col, sw=2)
        s.line(x2, y2 - 7, x2, y2 + 7, stroke=col, sw=2)
        s.text((x1 + x2) / 2, y1 + (24 if below else -12), label, 15, col, anchor="middle")

    cols = [(40, "Zu klein", RED, "✘"), (560, "Gut", GREEN, "✔"), (1080, "Hauptaktion", BLUE, "✔✔")]
    for x, t, c, z in cols:
        panel(s, x, 124, 480, 400, fill=WHITE, stroke=c)
        s.rect(x, 124, 480, 56, 22, fill=c, stroke=INK, sw=4)
        s.text(x + 24, 162, z + "  " + t, 26, WHITE, outline=INK, ow=5)
    # zu klein: 28 px Buttons, 4 px Abstand
    x0, y0 = 40 + 90, 262
    for i in range(5):
        gbutton(s, x0 + i * 32, y0, 28, 28, icon=["🛒", "🎒", "📜", "⚙️", "📖"][i], color=WHITE, dark="#b8c3da", r=7, sw=2,
                icon_size=17)
    finger(x0 + 76, y0 + 16)
    mass(x0, y0 + 50, x0 + 28, y0 + 50, "28 px")
    s.text(x0 + 172, y0 + 20, "← 4 px Abstand", 15, RED_D)
    s.textbox(40 + 24, 392, "Fingerkuppe (≈ 45–57 px) trifft 2–3 Buttons gleichzeitig. Fehl-Tipps, Frust, versehentliche Käufe.",
              432, 17, INK)
    # gut: 48 px, 16 px Abstand
    x0, y0 = 560 + 70, 246
    for i in range(4):
        gbutton(s, x0 + i * 64, y0, 48, 48, icon=["🛒", "🎒", "📜", "⚙️"][i], color=WHITE, dark="#b8c3da", r=12, icon_size=28)
    finger(x0 + 24, y0 + 26)
    mass(x0 + 64, y0 + 70, x0 + 112, y0 + 70, "48 px")
    mass(x0 + 112, y0 - 20, x0 + 128, y0 - 20, "16 px", GREEN_D, below=False)
    s.textbox(560 + 24, 392, "Mind. ca. 44–48 px pro Trefferfläche, 12–16 px Luft dazwischen. Finger trifft genau einen Button.",
              432, 17, INK)
    # Hauptaktion 88 px
    cx, cy = 1080 + 170, 262
    round_button(s, cx, cy, 44, color=GREEN, dark=GREEN_D, icon="✋")
    round_button(s, cx + 130, cy - 10, 54, color=WHITE, dark="#b8c3da", icon="⬆️")
    finger(cx + 6, cy + 8)
    mass(cx - 44, cy + 70, cx + 44, cy + 70, "88 px")
    mass(cx + 76, cy + 70, cx + 184, cy + 70, "108 px")
    s.textbox(1080 + 24, 392, "Häufige Aktionen (Springen, Angriff, Sammeln) groß: 72–110 px, unten rechts in der Daumen-Zone.",
              432, 17, INK)
    # Schriftgroessen
    y = 552
    panel(s, 40, y, 1000, 290, fill=WHITE)
    s.text(64, y + 38, "Schriftgrößen auf dem Handy (1× Skalierung)", 22, INK)
    rows = [(10, "Münzen: 1.234", "zu klein", RED), (14, "Münzen: 1.234", "Minimum für kurze Labels", ORANGE_D),
            (18, "Münzen: 1.234", "gut für Text und Beschreibungen", GREEN_D),
            (28, "1,2K Münzen", "fett: Zahlen, Überschriften", BLUE_D)]
    yy = y + 70
    for sz, sample, verdict, c in rows:
        s.text(64, yy + sz * 0.85, "%d px" % sz, 16, MUTED)
        s.text(140, yy + sz * 0.85, sample, sz, INK, bold=(sz >= 18))
        s.text(560, yy + sz * 0.85, verdict, 17, c)
        yy += max(44, sz + 26)
    # Umsetzung
    x = 1064
    panel(s, x, y, 496, 290, fill=NOTE, stroke=GOLD_D)
    s.text(x + 24, y + 38, "So setzt du es in Roblox um", 21, INK)
    for i, t in enumerate(["Größen in Scale + UISizeConstraint (Min.)", "TextScaled + UITextSizeConstraint",
                           "UIPadding / UIListLayout für Abstände", "UIScale für Tablets", "Im Studio-Emulator UND auf echtem Handy testen"]):
        s.text(x + 30, y + 84 + i * 42, "•", 20, GOLD_D)
        s.text(x + 50, y + 84 + i * 42, t, 16.5, INK, bold=False)
    s.save(out)


# ---------------------------------------------------------------------------
def tutorial_pfeil(out):
    s = Svg()
    sheet(s, "Tutorial: Pfeil und Pfad statt Textmauer",
          "Onboarding-Mockup: leuchtender Pfad zum ersten Ziel, ein Satz Hinweis, Schritt-Anzeige und Überspringen",
          "ui-tutorial-pfeil.png", "Zeigen statt erklären, eine Anweisung zur Zeit")
    ox, oy, W, H = 40, 122, 1180, 664
    s.defs_add('<clipPath id="mock2"><rect x="%d" y="%d" width="%d" height="%d" rx="26"/></clipPath>' % (ox, oy, W, H))
    s.rect(ox - 6, oy - 6, W + 12, H + 12, 30, fill=INK, extra='filter="url(#schatten)"')
    s.g('clip-path="url(#mock2)"')
    game_world(s, ox, oy, W, H, horizon=0.36)
    tree(s, ox + 120, oy + 300, 1.6)
    tree(s, ox + 1080, oy + 290, 1.4)
    tree(s, ox + 520, oy + 260, 1.0)
    # Spawn
    s.ellipse(ox + 230, oy + 560, 110, 34, fill="#cfd8ea", stroke=INK, sw=3)
    s.ellipse(ox + 230, oy + 552, 110, 34, fill="#eef3ff", stroke=INK, sw=3)
    tag(s, ox + 230, oy + 596, "SPAWN", MUTED, 14, anchor="middle")
    avatar(s, ox + 230, oy + 556, 1.3)
    # Ziel: Busch mit Gluehen
    tx, ty = ox + 860, oy + 420
    s.circle(tx, ty, 120, fill=s.radial([(0, "#fff38a", 0.9), (0.6, "#ffd23c", 0.45), (1, "#ffd23c", 0)]))
    for (dx, dy, r) in [(-36, 6, 42), (34, 0, 46), (0, -30, 46)]:
        s.circle(tx + dx, ty + dy, r, fill="#3fae47", stroke=INK, sw=2.5)
    for (dx, dy) in [(-40, -6), (-8, -44), (26, -18), (44, 14), (-18, 16)]:
        s.circle(tx + dx, ty + dy, 10, fill="#e8334a", stroke=INK, sw=1.5)
    # Pfad aus leuchtenden Punkten
    import math as _m
    p0, p1, p2, p3 = (ox + 300, oy + 560), (ox + 450, oy + 640), (ox + 680, oy + 600), (tx - 70, ty + 50)
    for k in range(1, 15):
        t = k / 15
        bx = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t * t * p2[0] + t ** 3 * p3[0]
        by = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t * t * p2[1] + t ** 3 * p3[1]
        s.ellipse(bx, by, 16, 9, fill="#fff38a", op=0.55, extra='filter="url(#glow)"')
        s.ellipse(bx, by, 9, 5, fill=WHITE, stroke="#ffb800", sw=2)
    # Huepfender Pfeil
    ax, ay = tx, ty - 120
    s.path("M%d,%d l-34,-46 h20 v-50 h28 v50 h20 z" % (ax, ay), fill=GOLD, stroke=INK, sw=4, extra='filter="url(#schattenK)"')
    for k in range(3):
        s.path("M%d,%d h%d" % (ax - 70 - k * 4, ay - 70 + k * 18, 22), stroke=INK, sw=3, op=0.5)
        s.path("M%d,%d h%d" % (ax + 48 + k * 4, ay - 70 + k * 18, 22), stroke=INK, sw=3, op=0.5)
    s.emoji(tx + 70, ty + 50, "👆", 46)
    # Abdunkeln der Raender (Vignette)
    s.rect(ox, oy, W, H, 0, fill=s.radial([(0, "#000", 0), (0.65, "#000", 0), (1, "#000", 0.38)], cx=0.62, cy=0.62, r=0.75))
    # Hinweis oben
    hw = 640
    s.rect(ox + W / 2 - hw / 2, oy + 30, hw, 76, 22, fill=WHITE, stroke=INK, sw=4, extra='filter="url(#schatten)"')
    s.emoji(ox + W / 2 - hw / 2 + 40, oy + 68, "💡", 36)
    s.text(ox + W / 2 + 22, oy + 66, "Tippe auf den Beerenbusch, um zu sammeln!", 22, INK, anchor="middle")
    s.text(ox + W / 2 + 22, oy + 92, "Schritt 1 von 3", 15, MUTED, anchor="middle")
    for k in range(3):
        s.circle(ox + W / 2 + 118 + k * 18, oy + 87, 6, fill=BLUE if k == 0 else "#c9d3ee")
    # Ueberspringen
    gbutton(s, ox + W - 220, oy + 36, 190, 50, "Überspringen ⏭", color="#eef1f7", dark="#a8b3cc", size=17,
            text_color=INK2, outline=False)
    # Distanz
    tag(s, ox + 520, oy + 640, "nur ~5 s Laufweg vom Spawn", INK, 15, anchor="middle")
    s.g_end()
    for n, (bx, by) in enumerate([(ox + W / 2 - hw / 2 - 2, oy + 32), (ox + 560, oy + 590), (tx + 46, ty - 200),
                                  (ox + W / 2 + 180, oy + 108), (ox + W - 226, oy + 40), (ox + 340, oy + 520)], start=1):
        badge(s, bx, by, n, BLUE, r=16)
    legende(s, 1248, 122, 320, [
        ("Ein Satz pro Schritt", "Kurz, aktiv: Was tun? Kein Textblock."),
        ("Leuchtender Pfad", "Führt den Blick vom Spieler zum Ziel."),
        ("Pfeil + Glühen am Ziel", "Hüpfender Pfeil, Hand-Symbol, Licht."),
        ("Schritt-Anzeige", "Zeigt: Es ist kurz (1 von 3)."),
        ("Überspringen", "Für Wiederkehrer, klar sichtbar."),
        ("Ziel nah am Spawn", "Erste Aktion in < 10 Sekunden."),
    ], tsize=18, size=15, gap=10)
    callout(s, 1248, 700, 320, "Danach: Pfeile abbauen", "Später nur noch dezente Hinweise.", color=GREEN, tsize=17, size=14)
    s.save(out)


# ---------------------------------------------------------------------------
def popup_hierarchie(out):
    s = Svg()
    sheet(s, "Toast, Banner, Modal: Popup-Hierarchie",
          "Welche Meldung wofür, wo sie erscheint, wie lange sie bleibt – und warum Meldungen in eine Warteschlange gehören",
          "ui-popup-toast-hierarchie.png", "Modal nur für Wichtiges, Toasts 2–4 s, nacheinander")
    cols = [("Toast", GREEN, "Kurze Info", ["Wo: Rand/oben rechts, klein", "Dauer: 2–4 s, dann weg", "Interaktion: keine nötig",
                                             "Für: Belohnung, Fortschritt"]),
            ("Banner", ORANGE, "Hinweis mit Zeitbezug", ["Wo: breites Band oben", "Dauer: 5–8 s, dann einklappen",
                                                         "Interaktion: antippbar → Details", "Für: Event, Server-Meldung"]),
            ("Modal", RED, "Entscheidung nötig", ["Wo: Mitte, Hintergrund abgedunkelt", "Dauer: bis Entscheidung",
                                                  "Interaktion: blockiert das Spiel", "Für: Kauf, Löschen, Fehler"])]
    cw = (1520 - 2 * 24) / 3
    for i, (name, c, sub, specs) in enumerate(cols):
        x, y = 40 + i * (cw + 24), 122
        panel(s, x, y, cw, 466, fill=WHITE, stroke=c)
        s.rect(x, y, cw, 60, 22, fill=c, stroke=INK, sw=4)
        s.text(x + 22, y + 41, name, 28, WHITE, outline=INK, ow=5)
        s.text(x + cw - 22, y + 39, sub, 17, WHITE, anchor="end", outline=INK, ow=3.5)
        # Mini-Bildschirm
        mx, my, mw, mh = x + 22, y + 80, cw - 44, 240
        cid = s.uid("mini")
        s.defs_add('<clipPath id="%s"><rect x="%s" y="%s" width="%s" height="%s" rx="18"/></clipPath>' % (cid, mx, my, mw, mh))
        s.g('clip-path="url(#%s)"' % cid)
        game_world(s, mx, my, mw, mh, horizon=0.45)
        avatar(s, mx + mw / 2, my + mh - 40, 0.9)
        if name == "Toast":
            s.rect(mx + mw - 220, my + 16, 204, 50, 14, fill=WHITE, stroke=GREEN, sw=3, extra='filter="url(#schattenK)"')
            coin(s, mx + mw - 194, my + 41, 13)
            s.text(mx + mw - 172, my + 48, "+50 Münzen", 18, INK)
            s.rect(mx + mw - 220, my + 74, 204, 40, 14, fill=WHITE, stroke=GREEN, sw=2, op=0.45)
            s.text(mx + mw - 118, my + 100, "wartet …", 14, MUTED, anchor="middle")
        elif name == "Banner":
            s.rect(mx, my + 14, mw, 58, 0, fill=s.gradient([(0, ORANGE), (1, PINK)], x2=1, y2=0), stroke=INK, sw=3)
            s.emoji(mx + 34, my + 43, "🎉", 28)
            s.text(mx + 62, my + 41, "Event: Doppelte Drops", 18, WHITE, outline=INK, ow=4)
            s.text(mx + 62, my + 62, "noch 2 Std · Tippen für Details", 13, WHITE, outline=INK, ow=3)
        else:
            s.rect(mx, my, mw, mh, 0, fill="#0b1330", op=0.55)
            s.rect(mx + 50, my + 34, mw - 100, mh - 68, 16, fill=WHITE, stroke=INK, sw=3)
            s.text(mx + mw / 2, my + 70, "Haustier löschen?", 19, INK, anchor="middle")
            s.text(mx + mw / 2, my + 96, "Legendär – geht für immer verloren.", 13, RED_D, anchor="middle")
            gbutton(s, mx + 70, my + 120, (mw - 160) / 2, 40, "Abbrechen", color="#dfe5f2", dark="#a8b3cc", size=15,
                    text_color=INK2, outline=False)
            gbutton(s, mx + mw / 2 + 10, my + 120, (mw - 160) / 2, 40, "Löschen", color=RED, dark=RED_D, size=16)
        s.g_end()
        s.rect(mx, my, mw, mh, 18, fill="none", stroke=INK, sw=3)
        for k, sp in enumerate(specs):
            s.text(x + 26, y + 352 + k * 28, "•", 18, c)
            s.text(x + 44, y + 352 + k * 28, sp, 16, INK, bold=False)
    # Warteschlange
    y = 610
    panel(s, 40, y, 1000, 232, fill=WHITE)
    s.text(64, y + 36, "Warteschlange statt Stapel", 22, INK)
    x0, x1 = 210, 1000
    sec = (x1 - x0) / 12
    for k in range(0, 13, 2):
        s.line(x0 + k * sec, y + 196, x0 + k * sec, y + 204, stroke=MUTED, sw=2)
        s.text(x0 + k * sec, y + 224, "%d s" % k, 13, MUTED, anchor="middle", bold=False)
    s.line(x0, y + 196, x1, y + 196, stroke=MUTED, sw=2)
    s.text(64, y + 92, "✔ richtig:", 17, GREEN_D)
    s.text(64, y + 112, "nacheinander", 14, INK2, bold=False)
    for k, t in enumerate(["+50 Münzen", "Quest fertig!", "Neues Ei"]):
        bx = x0 + (k * 3.4) * sec
        s.rect(bx, y + 74, 3 * sec, 40, 12, fill=GREEN, stroke=INK, sw=2.5)
        s.text(bx + 1.5 * sec, y + 100, t, 15, WHITE, anchor="middle", outline=INK, ow=3)
    s.text(64, y + 158, "✘ falsch:", 17, RED_D)
    s.text(64, y + 178, "übereinander", 14, INK2, bold=False)
    for k, t in enumerate(["+50 Münzen", "Quest fertig!", "Neues Ei"]):
        bx = x0 + k * 14
        s.rect(bx, y + 136 + k * 8, 3 * sec, 40, 12, fill=RED, stroke=INK, sw=2.5, op=0.9)
        s.text(bx + 1.5 * sec, y + 162 + k * 8, t, 15, WHITE, anchor="middle", outline=INK, ow=3)
    s.text(x0 + 3.6 * sec, y + 166, "→ unlesbar, verdeckt Spiel", 15, RED_D)
    # Prioritaet
    x = 1064
    panel(s, x, y, 496, 232, fill=NOTE, stroke=GOLD_D)
    s.text(x + 24, y + 36, "Priorität und Regeln", 21, INK)
    stufen = [("Modal (blockiert)", RED), ("Warnung / Gefahr", ORANGE), ("Banner", GOLD_D), ("Toast", GREEN)]
    for k, (t, c) in enumerate(stufen):
        w = 300 - k * 40
        s.rect(x + 24, y + 54 + k * 34, w, 28, 10, fill=c, stroke=INK, sw=2)
        s.text(x + 36, y + 74 + k * 34, t, 15, WHITE, outline=INK, ow=3)
    s.textbox(x + 340, y + 52, "Nie mitten im Kampf mit Kauf-Werbung unterbrechen.", 140, 15, INK)
    s.text(x + 24, y + 210, "Ein Fenster zur Zeit, große Schließen-Fläche.", 15, INK2)
    s.save(out)


ALLE = {
    "ui-hud-layout-mobile": hud_layout_mobile,
    "ui-hud-beispiel-simulator": hud_simulator,
    "ui-shop-layout": shop_layout,
    "ui-inventar-seltenheit": inventar,
    "ui-sammelbuch": sammelbuch,
    "ui-farbpalette-bedeutung": farbpalette,
    "ui-touch-groessen": touch_groessen,
    "ui-tutorial-pfeil": tutorial_pfeil,
    "ui-popup-toast-hierarchie": popup_hierarchie,
}
