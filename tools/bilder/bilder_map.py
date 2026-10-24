"""Map-/Leveldesign-Referenzbilder und Live-Ops-Kalender."""
import math

from svglib import *  # noqa: F401,F403


def blob(s, cx, cy, w, h, fill, stroke=INK, sw=4, wob=0.08, seed=0, op=None):
    """Weiche, unregelmaessige Zonenflaeche."""
    pts = []
    n = 14
    for k in range(n):
        a = 2 * math.pi * k / n
        f = 1 + wob * math.sin(3 * a + seed) + wob * 0.6 * math.cos(5 * a + seed * 1.7)
        pts.append((cx + w / 2 * f * math.cos(a), cy + h / 2 * f * math.sin(a)))
    d = "M%.1f,%.1f " % ((pts[0][0] + pts[-1][0]) / 2, (pts[0][1] + pts[-1][1]) / 2)
    for k in range(n):
        p, q = pts[k], pts[(k + 1) % n]
        d += "Q%.1f,%.1f %.1f,%.1f " % (p[0], p[1], (p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    s.path(d + "Z", fill=fill, stroke=stroke, sw=sw, op=op)


def gate(s, x, y, label, locked=True, color=GOLD):
    s.rect(x - 30, y - 24, 60, 48, 10, fill="#6b4a2b", stroke=INK, sw=3)
    s.rect(x - 18, y - 12, 36, 36, 8, fill=color if locked else GREEN, stroke=INK, sw=2.5)
    s.emoji(x, y + 5, "🔒" if locked else "✅", 22)
    w = tw(label, 15) + 22
    s.rect(x - w / 2, y + 30, w, 28, 14, fill=INK if locked else GREEN_D, stroke=WHITE, sw=2)
    s.text(x, y + 49, label, 15, GOLD if locked else WHITE, anchor="middle")


def teleporter(s, x, y, r=20):
    s.circle(x, y, r + 6, fill=BLUE, op=0.3, extra='filter="url(#glow)"')
    s.circle(x, y, r, fill="#bfe3ff", stroke=BLUE_D, sw=3)
    s.circle(x, y, r * 0.55, fill="none", stroke=BLUE_D, sw=2.5, extra='stroke-dasharray="5 4"')


def plot(s, x, y, sz, owner=True):
    s.rect(x, y, sz, sz, 6, fill="#c9a26b" if owner else "#d9c7a5", stroke=INK, sw=2.5)
    for k in range(3):
        s.line(x + 6, y + 10 + k * (sz - 16) / 2, x + sz - 6, y + 10 + k * (sz - 16) / 2, stroke="#8a6a3e", sw=2)


def zonen_layout(out):
    s = Svg()
    sheet(s, "Map-Zonen-Layout (Draufsicht)",
          "Hub mit Landmarke, fünf Zonen mit eigener Farbwelt, Tore mit Preisen, Wege, Sichtlinien, Teleporter und Spieler-Plots",
          "map-zonen-layout.png", "Nächste Zone sichtbar, Preis am Tor, jede Zone eigenes Merkmal")
    X, Y, W, H = 40, 122, 1130, 712
    s.defs_add('<clipPath id="karte"><rect x="%d" y="%d" width="%d" height="%d" rx="26"/></clipPath>' % (X, Y, W, H))
    s.rect(X - 5, Y - 5, W + 10, H + 10, 30, fill=INK, extra='filter="url(#schatten)"')
    s.g('clip-path="url(#karte)"')
    s.rect(X, Y, W, H, 0, fill=s.gradient([(0, "#5cc3ee"), (1, "#3aa6dc")]))
    for k in range(18):
        s.path("M%d,%d q12,-8 24,0 q12,8 24,0" % (X + 40 + (k * 137) % 1050, Y + 30 + (k * 211) % 660), stroke=WHITE, sw=2, op=0.4)
    blob(s, X + W / 2, Y + H / 2 + 10, W - 70, H - 50, "#a8d98f", sw=4, wob=0.04, seed=1)
    zonen = [  # (cx, cy, w, h, fill, name, res, deko)
        (250, 655, 300, 220, "#7fd36b", "Zone 1 · Wiese", "Äpfel", ["🌳", "🌳", "🍎", "🌳"]),
        (225, 330, 300, 250, "#f3d58a", "Zone 2 · Wüste", "Kaktusfrüchte", ["🌵", "🌵", "🏜️", "🌵"]),
        (590, 255, 320, 210, "#d8f1ff", "Zone 3 · Eis", "Eiskristalle", ["🏔️", "❄️", "⛄", "❄️"]),
        (955, 300, 300, 250, "#a8473a", "Zone 4 · Vulkan", "Lavasteine", ["🌋", "🔥", "🪨", "🔥"]),
        (1000, 628, 260, 200, "#c9a8ff", "Zone 5 · Kristall", "Sternkristalle", ["💎", "✨", "🔮", "💎"]),
    ]
    for i, (cx, cy, w, h, f, name, res, deko) in enumerate(zonen):
        blob(s, cx, cy, w, h, f, sw=4, seed=i * 1.3)
    # Wege
    weg = "M600,640 Q500,660 420,650 Q320,640 250,640 Q235,560 240,495 Q235,400 225,330 Q320,300 405,290 " \
          "Q500,260 590,255 Q690,265 775,280 Q860,290 955,300 Q975,370 980,440 Q990,540 1000,628"
    s.path(weg, stroke="#8a6a3e", sw=26, op=0.9)
    s.path(weg, stroke="#e9d29a", sw=18)
    s.path(weg, stroke="#cdb57a", sw=2, dash="10 12")
    # Deko + Beschriftung
    for i, (cx, cy, w, h, f, name, res, deko) in enumerate(zonen):
        for k, e in enumerate(deko):
            a = math.radians(30 + k * 90)
            s.emoji(cx + w * 0.3 * math.cos(a), cy + h * 0.28 * math.sin(a), e, 40 if k == 0 else 30)
        tw_ = tw(name, 17) + 24
        lx_ = cx
        s.rect(lx_ - tw_ / 2, cy - h / 2 - 2, tw_, 30, 15, fill=WHITE, stroke=INK, sw=2.5)
        s.text(lx_, cy - h / 2 + 19, name, 17, INK, anchor="middle")
        s.text(lx_, cy - h / 2 + 46, "Ressource: " + res, 13, INK if i != 3 else WHITE, anchor="middle")
    # Sichtlinien
    s.path("M600,600 L590,300", stroke=GOLD, sw=4, dash="4 10", op=0.95)
    s.path("M660,620 L950,630", stroke=GOLD, sw=4, dash="4 10", op=0.95)
    s.emoji(600, 470, "👁️", 26)
    tag(s, 612, 430, "Sichtlinie", GOLD_D, 13)
    # Tore
    gate(s, 420, 650, "Frei", locked=False)
    gate(s, 238, 476, "1K")
    gate(s, 405, 290, "10K")
    gate(s, 775, 280, "100K")
    gate(s, 980, 440, "1M")
    # Hub
    s.circle(600, 640, 112, fill="#e6e9f2", stroke=INK, sw=4)
    s.circle(600, 640, 88, fill="none", stroke="#c3c9d8", sw=3, extra='stroke-dasharray="8 6"')
    s.emoji(600, 618, "🗼", 70)
    tag(s, 600, 668, "HUB · Spawn", INK, 14, anchor="middle")
    teleporter(s, 668, 590)
    teleporter(s, 532, 590)
    for (zx, zy) in [(305, 690), (175, 380), (650, 215), (900, 350), (1065, 665)]:
        teleporter(s, zx, zy, 16)
    # Plots
    for k in range(6):
        plot(s, 440 + k * 56, 768, 46, owner=(k == 2))
    tag(s, 600, 740, "Spieler-Plots", "#8a6a3e", 13, anchor="middle")
    s.g_end()
    # Legende
    lx, ly, lw = 1196, 122, 374
    panel(s, lx, ly, lw, 712, fill=WHITE)
    s.text(lx + 22, ly + 40, "Legende", 22, INK)
    items = [("hub", "Hub/Spawn mit Landmarke"), ("zone", "Zone mit eigener Farbwelt"), ("tor", "Tor mit Preis (Ziel!)"),
             ("weg", "Weg / Pfad"), ("sicht", "Sichtlinie zur nächsten Zone"), ("tp", "Teleporter (ab Mittelspiel)"),
             ("plot", "Spieler-Plot (Besitzgefühl)")]
    for k, (ic, t) in enumerate(items):
        yy = ly + 64 + k * 44
        ix = lx + 44
        if ic == "hub":
            s.circle(ix, yy + 14, 16, fill="#e6e9f2", stroke=INK, sw=2.5)
            s.emoji(ix, yy + 12, "🗼", 20)
        elif ic == "zone":
            blob(s, ix, yy + 14, 40, 28, "#c9a8ff", sw=2.5)
        elif ic == "tor":
            s.rect(ix - 16, yy + 2, 32, 26, 6, fill=GOLD, stroke=INK, sw=2.5)
            s.emoji(ix, yy + 15, "🔒", 16)
        elif ic == "weg":
            s.line(ix - 20, yy + 15, ix + 20, yy + 15, stroke="#8a6a3e", sw=14)
            s.line(ix - 20, yy + 15, ix + 20, yy + 15, stroke="#e9d29a", sw=9)
        elif ic == "sicht":
            s.line(ix - 20, yy + 15, ix + 20, yy + 15, stroke=GOLD, sw=4, dash="4 8")
        elif ic == "tp":
            teleporter(s, ix, yy + 15, 13)
        else:
            plot(s, ix - 15, yy, 30)
        s.text(lx + 80, yy + 21, t, 16, INK, bold=False)
    ry = ly + 384
    s.rect(lx + 18, ry, lw - 36, 310, 16, fill=NOTE, stroke=GOLD_D, sw=2.5)
    s.text(lx + 36, ry + 32, "Regeln", 19, INK)
    yy = ry + 44
    for t in ["Nächste Zone vom Hub aus sichtbar (Tor, Leuchten, Berg).",
              "Preis/Level steht direkt am Tor.",
              "Jede Zone: eigene Farbe, Ressource, Merkmal – nicht nur umgefärbt.",
              "Schwierigkeit sanft, Belohnung sichtbar steigend.",
              "Lange Wege ohne Inhalt vermeiden."]:
        yy += s.textbox(lx + 36, yy, "• " + t, lw - 72, 15, INK2) + 7
    s.save(out)


# ---------------------------------------------------------------------------
def wegfuehrung(out):
    s = Svg()
    sheet(s, "Wegführung ohne Text",
          "Sechs Werkzeuge, mit denen eine Map den Spieler lenkt: Licht, Farbe, Linien, Höhe, Engpass/Weite, Spuren",
          "map-wegfuehrung.png", "Licht, Farbe, Linien und Höhe lenken Blick und Schritte")
    tiles = [("Licht", "Helle Bereiche ziehen den Blick."), ("Farbe", "Warm (Gold/Orange) = Ziel, kalt = Hintergrund."),
             ("Linien", "Wege, Zäune, Flüsse zeigen die Richtung."), ("Höhe / Landmarke", "Hohe Objekte = Orientierung von überall."),
             ("Engpass ↔ Weite", "Eng = Spannung, weit = Erholung (Rhythmus)."),
             ("Spuren", "Münz-Spur/Pfeile im Tutorial, später abbauen.")]
    tw_, th = (1520 - 2 * 20) / 3, 346
    for i, (t, cap) in enumerate(tiles):
        x = 40 + (i % 3) * (tw_ + 20)
        y = 122 + (i // 3) * (th + 18)
        panel(s, x, y, tw_, th, fill=WHITE)
        badge(s, x + 30, y + 30, i + 1, BLUE, r=16)
        s.text(x + 56, y + 38, t, 22, INK)
        ix, iy, iw, ih = x + 18, y + 60, tw_ - 36, 220
        cid = s.uid("kachel")
        s.defs_add('<clipPath id="%s"><rect x="%s" y="%s" width="%s" height="%s" rx="16"/></clipPath>' % (cid, ix, iy, iw, ih))
        s.g('clip-path="url(#%s)"' % cid)
        if i == 0:  # Licht
            s.rect(ix, iy, iw, ih, 0, fill="#1a2238")
            s.rect(ix, iy + ih * 0.6, iw, ih * 0.4, 0, fill="#253150")
            s.circle(ix + iw * 0.72, iy + ih * 0.5, 120, fill=s.radial([(0, "#fff3b0", 0.95), (0.5, "#ffd23c", 0.4), (1, "#ffd23c", 0)]))
            s.rect(ix + iw * 0.72 - 30, iy + ih * 0.42, 60, 70, 10, fill="#8a5a2b", stroke=INK, sw=3)
            s.emoji(ix + iw * 0.72, iy + ih * 0.42 + 30, "🎁", 40)
            for k in range(4):
                s.rect(ix + 30 + k * 60, iy + 60 + (k % 2) * 30, 40, 90, 6, fill="#2e3a5c")
            avatar(s, ix + 90, iy + ih - 18, 0.7)
            arrow(s, ix + 130, iy + ih - 60, ix + iw * 0.72 - 50, iy + ih * 0.55, color="#ffd23c", bend=-0.2, dash="8 6")
        elif i == 1:  # Farbe
            s.rect(ix, iy, iw, ih, 0, fill="#b9c7dd")
            gb = iy + ih * 0.72
            s.rect(ix, gb, iw, ih * 0.28, 0, fill="#93a6c4")
            for k, (bx, bh) in enumerate([(20, 90), (90, 120), (300, 110), (370, 80)]):
                s.rect(ix + bx, gb - bh, 60, bh, 6, fill="#7d93b8", stroke="#5d7298", sw=2)
            s.circle(ix + iw / 2, gb - 60, 95, fill=s.radial([(0, ORANGE, 0.6), (1, ORANGE, 0)]))
            s.rect(ix + iw / 2 - 50, gb - 92, 100, 92, 10, fill=GOLD, stroke=INK, sw=3)
            s.poly([(ix + iw / 2 - 62, gb - 88), (ix + iw / 2, gb - 136), (ix + iw / 2 + 62, gb - 88)],
                   fill=ORANGE, stroke=INK, sw=3)
            s.rect(ix + iw / 2 - 16, gb - 46, 32, 46, 6, fill="#8a5a2b", stroke=INK, sw=2)
            tag(s, ix + iw / 2, iy + ih - 40, "Ziel = warm", ORANGE_D, 14, anchor="middle")
        elif i == 2:  # Linien
            s.rect(ix, iy, iw, ih, 0, fill=s.gradient([(0, "#8fd6ff"), (0.4, "#d6f2ff"), (0.41, "#7fd36b"), (1, "#4fae47")]))
            vx, vy = ix + iw * 0.62, iy + ih * 0.4
            s.poly([(ix + iw * 0.25, iy + ih), (vx - 6, vy), (vx + 6, vy), (ix + iw * 0.75, iy + ih)], fill="#e9d29a")
            for k in range(7):
                f = k / 7
                for side in (-1, 1):
                    bx = vx + side * 8 + (ix + iw * (0.5 + side * 0.32) - vx) * (1 - f) ** 1.6
                    by = vy + (iy + ih - vy) * (1 - f) ** 1.6
                    hh = 34 * (1 - f) ** 1.6 + 4
                    s.rect(bx - hh * 0.12, by - hh, hh * 0.24, hh, 2, fill="#8a5a2b")
                s.line(vx + (ix + iw * 0.18 - vx) * (1 - f) ** 1.6, vy + (iy + ih - vy) * (1 - f) ** 1.6 - 10, vx,
                       vy, stroke="#8a5a2b", sw=0)
            s.line(ix + iw * 0.18, iy + ih - 24, vx - 8, vy + 4, stroke="#8a5a2b", sw=3)
            s.line(ix + iw * 0.82, iy + ih - 24, vx + 8, vy + 4, stroke="#8a5a2b", sw=3)
            s.emoji(vx, vy - 16, "🏰", 34)
        elif i == 3:  # Hoehe
            s.rect(ix, iy, iw, ih, 0, fill=s.gradient([(0, "#ffb37a"), (1, "#ffe1b8")]))
            s.rect(ix, iy + ih * 0.78, iw, ih * 0.22, 0, fill="#6a8f5a")
            for k in range(9):
                bh = 30 + (k * 37) % 40
                s.rect(ix + 10 + k * 48, iy + ih * 0.78 - bh, 40, bh, 4, fill="#5a6d8a", stroke="#3d4d68", sw=2)
            tx_ = ix + iw * 0.68
            s.poly([(tx_ - 26, iy + ih * 0.78), (tx_ - 14, iy + 40), (tx_ + 14, iy + 40), (tx_ + 26, iy + ih * 0.78)], fill=WHITE,
                   stroke=INK, sw=3)
            for k in range(3):
                s.rect(tx_ - 20 + k * 2, iy + 70 + k * 40, 40 - k * 4, 12, 2, fill=RED)
            s.rect(tx_ - 20, iy + 22, 40, 22, 6, fill=GOLD, stroke=INK, sw=3)
            s.poly([(tx_, iy + 32), (tx_ - 160, iy + 0), (tx_ - 160, iy + 64)], fill="#fff3b0", op=0.55)
            s.poly([(tx_, iy + 32), (tx_ + 160, iy + 0), (tx_ + 160, iy + 64)], fill="#fff3b0", op=0.55)
            tag(s, tx_ - 34, iy + ih * 0.5, "Landmarke", INK, 14, anchor="end")
        elif i == 4:  # Engpass / Weite
            s.rect(ix, iy, iw, ih, 0, fill="#c9a26b")
            s.rect(ix, iy + ih / 2 - 22, iw * 0.42, 44, 0, fill="#e9d29a")
            s.rect(ix, iy, iw * 0.42, ih / 2 - 22, 0, fill="#8a6a3e")
            s.rect(ix, iy + ih / 2 + 22, iw * 0.42, ih / 2 - 22, 0, fill="#8a6a3e")
            s.ellipse(ix + iw * 0.72, iy + ih / 2, iw * 0.3, ih * 0.44, fill="#9be08a", stroke="#5aa64b", sw=3)
            s.emoji(ix + iw * 0.7, iy + ih / 2 - 30, "🌳", 30)
            s.emoji(ix + iw * 0.8, iy + ih / 2 + 30, "⛲", 30)
            avatar(s, ix + 60, iy + ih / 2 + 14, 0.5)
            arrow(s, ix + 100, iy + ih / 2, ix + iw * 0.5, iy + ih / 2, color=INK, bend=0)
            tag(s, ix + iw * 0.21, iy + 20, "eng → Spannung", RED_D, 14, anchor="middle")
            tag(s, ix + iw * 0.72, iy + ih - 40, "weit → Erholung", GREEN_D, 14, anchor="middle")
        else:  # Spuren
            s.rect(ix, iy, iw, ih, 0, fill="#7fd36b")
            s.path("M%d,%d Q%d,%d %d,%d Q%d,%d %d,%d" % (ix + 40, iy + ih - 20, ix + 80, iy + 80, ix + iw * 0.45, iy + 90,
                                                      ix + iw * 0.75, iy + 100, ix + iw - 60, iy + 40),
                   stroke="#e9d29a", sw=40)
            pts = [(ix + 70, iy + ih - 50), (ix + 80, iy + ih - 95), (ix + 98, iy + 138), (ix + 130, iy + 112),
                   (ix + 172, iy + 97), (ix + 215, iy + 92), (ix + 258, iy + 94), (ix + 300, iy + 92), (ix + 340, iy + 80)]
            for k, (px_, py_) in enumerate(pts):
                coin(s, px_, py_, 10)
            s.emoji(ix + iw - 56, iy + 40, "🏁", 40)
            avatar(s, ix + 40, iy + ih - 6, 0.5)
            tag(s, ix + iw - 20, iy + ih - 40, "später weniger Spuren", INK, 13, anchor="end")
        s.g_end()
        s.rect(ix, iy, iw, ih, 16, fill="none", stroke=INK, sw=3)
        s.text(x + 22, y + th - 26, cap, 16.5, INK)
    s.save(out)


# ---------------------------------------------------------------------------
def spawn_hub(out):
    s = Svg()
    sheet(s, "Spawn und Hub im Detail",
          "Erste Interaktion direkt am Spawn, Shop, Rangliste, Teleporter, Schutzzone und klarer Weg zur ersten Zone",
          "map-spawn-hub.png", "Spawn nahe der ersten Aktion, keine Gefahr am Spawn")
    X, Y, W, H = 40, 122, 1110, 712
    s.defs_add('<clipPath id="hub"><rect x="%d" y="%d" width="%d" height="%d" rx="26"/></clipPath>' % (X, Y, W, H))
    s.rect(X - 5, Y - 5, W + 10, H + 10, 30, fill=INK, extra='filter="url(#schatten)"')
    s.g('clip-path="url(#hub)"')
    s.rect(X, Y, W, H, 0, fill="#8fd47c")
    for k in range(40):
        s.circle(X + (k * 173) % W, Y + (k * 97) % H, 3, fill="#6fbf5c")
    cx, cy = X + 520, Y + 380
    # Weg zur Zone 1
    s.path("M%d,%d Q%d,%d %d,%d" % (cx, cy, cx + 300, cy + 120, X + W + 20, Y + H - 80), stroke="#8a6a3e", sw=56)
    s.path("M%d,%d Q%d,%d %d,%d" % (cx, cy, cx + 300, cy + 120, X + W + 20, Y + H - 80), stroke="#e9d29a", sw=46)
    # Schutzzone
    s.circle(cx, cy, 300, fill=GREEN, op=0.12)
    s.circle(cx, cy, 300, fill="none", stroke=GREEN_D, sw=4, extra='stroke-dasharray="14 10"')
    tag(s, cx, cy + 300 - 14, "Schutzzone: keine Gegner/PvP", GREEN_D, 14, anchor="middle")
    # Platz
    s.circle(cx, cy, 200, fill="#e6e9f2", stroke=INK, sw=4)
    for k in range(12):
        a = math.radians(k * 30)
        s.line(cx + 120 * math.cos(a), cy + 120 * math.sin(a), cx + 200 * math.cos(a), cy + 200 * math.sin(a), stroke="#cfd5e3", sw=3)
    s.circle(cx, cy, 120, fill="#f3f5fa", stroke="#cfd5e3", sw=3)
    # Landmarke Brunnen/Turm
    s.circle(cx, cy - 10, 56, fill="#7fd0ff", stroke=INK, sw=4)
    s.emoji(cx, cy - 18, "⛲", 64)
    # Spawn
    sx, sy = cx - 70, cy + 120
    s.ellipse(sx, sy, 62, 26, fill="#c9d3ee", stroke=INK, sw=3)
    s.ellipse(sx, sy - 6, 62, 26, fill=WHITE, stroke=INK, sw=3)
    avatar(s, sx, sy - 6, 0.85)
    # erste Interaktion (Busch)
    bx, by = cx + 80, cy + 140
    for (dx, dy, r) in [(-24, 6, 28), (22, 0, 30), (0, -20, 30)]:
        s.circle(bx + dx, by + dy, r, fill="#3fae47", stroke=INK, sw=2.5)
    for (dx, dy) in [(-26, -4), (-4, -30), (18, -12), (28, 10), (-10, 12)]:
        s.circle(bx + dx, by + dy, 7, fill="#e8334a", stroke=INK, sw=1.5)
    s.circle(bx, by, 60, fill="none", stroke=GOLD, sw=4, extra='stroke-dasharray="6 6"')
    arrow(s, sx + 40, sy - 20, bx - 50, by - 4, color=GOLD_D, bend=-0.3)
    # Shop
    shx, shy = cx - 360, cy - 80
    s.rect(shx - 70, shy - 50, 140, 110, 12, fill="#ffd9a0", stroke=INK, sw=3)
    s.rect(shx - 80, shy - 70, 160, 30, 8, fill=RED, stroke=INK, sw=3)
    for k in range(5):
        s.rect(shx - 80 + k * 32, shy - 70, 16, 30, 0, fill=WHITE, op=0.7)
    s.emoji(shx, shy + 6, "🛒", 46)
    tag(s, shx, shy + 70, "Shop", INK, 14, anchor="middle")
    # Verkaufen
    vx, vy = cx - 260, cy + 170
    s.rect(vx - 50, vy - 40, 100, 80, 14, fill=GOLD, stroke=INK, sw=3)
    s.emoji(vx, vy - 4, "💰", 40)
    tag(s, vx, vy + 48, "Verkaufen", INK, 14, anchor="middle")
    # Rangliste
    rx, ry = cx + 40, cy - 290
    s.rect(rx - 110, ry - 40, 220, 120, 10, fill="#3d4d68", stroke=INK, sw=3)
    s.text(rx, ry - 12, "🏆 RANGLISTE", 16, GOLD, anchor="middle")
    for k, t in enumerate(["1. Nova  12,4M", "2. Kiko   9,8M", "3. Pixl   7,1M"]):
        s.text(rx - 94, ry + 14 + k * 22, t, 14, WHITE, family="'DejaVu Sans Mono', monospace")
    s.rect(rx - 6, ry + 80, 12, 30, 2, fill="#6b4a2b")
    # Teleporter
    tps = [("Zone 2", cx + 270, cy - 160), ("Zone 3", cx + 330, cy - 60), ("Zone 4", cx + 350, cy + 50)]
    for name, tx, ty in tps:
        s.circle(tx, ty, 34, fill=BLUE, op=0.3, extra='filter="url(#glow)"')
        s.circle(tx, ty, 28, fill="#bfe3ff", stroke=BLUE_D, sw=3)
        s.circle(tx, ty, 15, fill="none", stroke=BLUE_D, sw=2.5, extra='stroke-dasharray="5 4"')
        tag(s, tx + 40, ty - 12, name + " 🔒", BLUE_D, 13)
    # Tagesbelohnung
    s.emoji(cx - 170, cy - 200, "🎁", 46)
    tag(s, cx - 170, cy - 168, "Tagesbelohnung", PURPLE_D, 13, anchor="middle")
    # Tor Zone 1
    gx, gy = X + W - 110, Y + H - 120
    s.rect(gx - 40, gy - 34, 80, 68, 10, fill="#6b4a2b", stroke=INK, sw=3)
    s.rect(gx - 24, gy - 18, 48, 48, 8, fill=GREEN, stroke=INK, sw=3)
    s.emoji(gx, gy + 6, "🌳", 30)
    tag(s, gx, gy + 42, "Zone 1 (frei)", GREEN_D, 14, anchor="middle")
    s.g_end()
    # Nummern + Legende
    marks = [(sx - 74, sy - 60), (bx + 56, by - 44), (cx + 50, cy - 70), (rx + 118, ry - 30), (800, cy - 205),
             (X + W - 170, Y + H - 160), (shx + 76, shy - 64), (cx + 150, cy + 300 - 2)]
    for k, (mx, my) in enumerate(marks):
        badge(s, mx, my, k + 1, BLUE, r=16)
    yy = 122
    for k, (t_, b_) in enumerate([
            ("Spawn", "Sicher landen, erste Aufgabe sofort sichtbar."),
            ("Erste Interaktion", "Wenige Schritte entfernt: Aktion in < 10 s."),
            ("Landmarke in der Mitte", "Brunnen/Turm = Orientierung."),
            ("Rangliste", "Social Proof: zeigt, was möglich ist."),
            ("Teleporter", "Gesperrte Ziele sichtbar = Neugier."),
            ("Weg zur Zone 1", "Breit, hell, führt aus dem Hub heraus."),
            ("Shop + Verkaufen", "Am Hub-Rand, nicht im Weg."),
            ("Schutzzone", "Keine Gefahr für Neulinge am Spawn.")]):
        h = callout(s, 1176, yy, 394, t_, b_, color=BLUE, num=k + 1, tsize=18, size=15)
        yy += h + 9
    s.save(out)


# ---------------------------------------------------------------------------
def liveops_kalender(out):
    s = Svg()
    sheet(s, "Live-Ops: 8-Wochen-Rhythmus",
          "Vorlage aus live-ops-events.md – Updates, Events, Saison und Pflege im Wechsel, darunter die Wirkung auf Spielerzahlen",
          "live-ops-kalender-8-wochen.png", "Rhythmus festlegen, Systemtiefe statt nur Events")
    X, Y = 40, 122
    lanes = [("Großes Update", PURPLE), ("Content-Update", BLUE), ("Event", ORANGE), ("Mini-Events", GOLD_D),
             ("Saison", PINK), ("Pflege", GREY_D)]
    lw, cw = 210, (1520 - 210) / 8
    lh = 62
    panel(s, X, Y, 1520, 64 + lh * len(lanes) + 10, fill=WHITE)
    for w in range(8):
        x = X + lw + w * cw
        s.rect(x + 4, Y + 10, cw - 8, 44, 12, fill="#eef2fa")
        s.text(x + cw / 2, Y + 40, "Woche %d" % (w + 1), 18, INK, anchor="middle")
        if w:
            s.line(x, Y + 60, x, Y + 64 + lh * len(lanes), stroke="#e3e8f3", sw=2)
    for k, (name, c) in enumerate(lanes):
        y = Y + 64 + k * lh
        s.rect(X + 14, y + 12, 12, lh - 24, 6, fill=c)
        s.text(X + 36, y + lh / 2 + 7, name, 18, INK)
        if k:
            s.line(X + 10, y, X + 1510, y, stroke="#eef1f7", sw=2)
    blocks = [  # (lane, start_woche, laenge, text, icon)
        (2, 1, 1, "Launch-Event", "🚀"), (3, 2, 1, "Mini-Events", "⚡"), (5, 2, 1, "Balancing", "⚖️"),
        (1, 3, 1, "Item-Set", "🎒"), (0, 4, 1, "Neue Zone", "🗺️"), (2, 4, 1, "Event-Woche", "🎉"),
        (2, 5, 1, "Community-Ziel", "🤝"), (4, 6, 3, "Saison 1 · Pass, Rangliste", "🏅"), (3, 7, 1, "Mini-Events", "⚡"),
        (5, 7, 1, "Bugfix-Welle", "🛠️"), (0, 8, 1, "Großes Update", "🆕"), (4, 8, 0, "", "")]
    for lane, wk, ln, txt, ic in blocks:
        if not ln:
            continue
        c = lanes[lane][1]
        x = X + lw + (wk - 1) * cw + 6
        y = Y + 64 + lane * lh + 10
        w = cw * ln - 12
        s.rect(x, y + 4, w, lh - 20, 14, fill=INK, op=0.25)
        s.rect(x, y, w, lh - 20, 14, fill=c, stroke=INK, sw=2.5)
        s.emoji(x + 22, y + (lh - 20) / 2, ic, 22)
        sz = 14 if tw(txt, 14) < w - 50 else 12
        s.text(x + 40, y + (lh - 20) / 2 + 5, txt, sz, WHITE, outline=INK, ow=3)
    tag(s, X + lw + 7.6 * cw, Y + 64 + 4 * lh + 46, "Zwischenbilanz", PINK_D, 12, anchor="middle")
    # Spielerkurve
    gy = Y + 64 + lh * len(lanes) + 26
    gh = 178
    panel(s, X, gy, 1000, gh + 50, fill=WHITE)
    s.text(X + 24, gy + 32, "Spieler (illustrativ): Spitzen bei Updates, Basis durch Systemtiefe", 17, INK)
    px0, px1, base_y = X + lw, X + 980, gy + gh + 20
    pts = []
    import math as _m
    for i in range(0, 161):
        t = i / 20.0  # Wochen 0..8
        v = 0.35 + 0.02 * t
        for (pk, amp) in [(0.3, 0.45), (3.3, 0.38), (5.2, 0.15), (5.6, 0.22), (7.3, 0.42)]:
            v += amp * _m.exp(-((t - pk) / 0.35) ** 2) if t >= pk - 0.2 else 0
        pts.append((px0 - 160 + (px1 - px0 + 160) * t / 8.0, base_y - v * (gh - 60)))
    d = "M" + " L".join("%.1f,%.1f" % p for p in pts)
    s.path(d + " L%.1f,%.1f L%.1f,%.1f Z" % (pts[-1][0], base_y, pts[0][0], base_y), fill=BLUE, op=0.15)
    s.path(d, stroke=BLUE_D, sw=4)
    s.path("M%.1f,%.1f L%.1f,%.1f" % (pts[0][0], base_y - 0.35 * (gh - 60), pts[-1][0], base_y - 0.51 * (gh - 60)),
           stroke=GREEN_D, sw=3, dash="8 6")
    tag(s, pts[-1][0] - 4, base_y - 0.51 * (gh - 60) + 10, "Basis (Meta-Systeme)", GREEN_D, 12, anchor="end")
    s.line(pts[0][0], base_y, pts[-1][0], base_y, stroke=INK, sw=2)
    for k in range(8):
        wx = pts[0][0] + (pts[-1][0] - pts[0][0]) * (k + 0.5) / 8
        s.text(wx, base_y + 18, "W%d" % (k + 1), 12, MUTED, anchor="middle")
    # Regeln
    rx = X + 1020
    s.rect(rx, gy, 500, gh + 50, 22, fill=NOTE, stroke=GOLD_D, sw=3)
    s.text(rx + 22, gy + 34, "Gute Events", 19, INK)
    yy = gy + 44
    for t in ["Ein Thema, ein klares Ziel", "Ehrliche Dauer, kein Fake-Druck", "Für alle erreichbar, nicht nur Käufer",
              "Nachlauf: Titel/Item bleibt", "Pipeline 2–3 Updates voraus, Rollback-Plan",
              "Kennzahlen vorher/nachher: CCU, D1/D7, Spielzeit"]:
        s.text(rx + 26, yy + 18, "•", 16, GOLD_D)
        s.text(rx + 42, yy + 18, t, 15, INK, bold=False)
        yy += 30
    s.save(out)


ALLE = {
    "map-zonen-layout": zonen_layout,
    "map-wegfuehrung": wegfuehrung,
    "map-spawn-hub": spawn_hub,
    "live-ops-kalender-8-wochen": liveops_kalender,
}
