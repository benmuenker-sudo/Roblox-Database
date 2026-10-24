"""Diagramme zu Core Loops, Retention, Progression und Gacha."""
import math
import random

from svglib import *  # noqa: F401,F403


def arc_arrow(s, cx, cy, r, a1, a2, color=INK, sw=4, ry=None):
    """Kreis-/Ellipsenbogen-Pfeil von Winkel a1 nach a2 (Grad, im Uhrzeigersinn)."""
    ry = ry or r
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + ry * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy + ry * math.sin(math.radians(a2))
    large = 1 if (a2 - a1) % 360 > 180 else 0
    s.path("M%.1f,%.1f A%.1f,%.1f 0 %d 1 %.1f,%.1f" % (x1, y1, r, ry, large, x2, y2), stroke=color, sw=sw, arrow=color)


def node(s, cx, cy, w, h, label, color, dark, icon=None, sub=None, size=20, subsize=14):
    s.rect(cx - w / 2, cy - h / 2 + 5, w, h, h / 2.6, fill=dark, stroke=INK, sw=3)
    s.rect(cx - w / 2, cy - h / 2, w, h, h / 2.6, fill=color, stroke=INK, sw=3)
    s.rect(cx - w / 2 + 8, cy - h / 2 + 4, w - 16, h * 0.3, 8, fill=WHITE, op=0.25)
    ty = cy + (size * 0.36 if not sub else -2)
    if icon:
        tx = cx - w / 2 + 34
        s.emoji(tx, cy, icon, h * 0.5 if h < 70 else 34)
        s.text(tx + 26, ty, label, size, WHITE, outline=INK, ow=size / 5)
        if sub:
            s.text(tx + 26, cy + subsize + 6, sub, subsize, WHITE, bold=False, outline=dark, ow=3)
    else:
        s.text(cx, ty, label, size, WHITE, anchor="middle", outline=INK, ow=size / 5)
        if sub:
            s.text(cx, cy + subsize + 6, sub, subsize, WHITE, anchor="middle", bold=False, outline=dark, ow=3)


# ---------------------------------------------------------------------------
def core_loop(out):
    s = Svg()
    sheet(s, "Der Core Loop und seine drei Zeitebenen",
          "Aktion → Feedback → Belohnung → Verbesserung → neue Möglichkeit · dazu Mikro-, Meso- und Makro-Loop",
          "core-loop-diagramm.png", "Jede Runde fühlt sich anders an; alle drei Ebenen nötig")
    cx, cy, r = 440, 488, 270
    s.circle(cx, cy, r, fill="none", stroke="#c9d3ee", sw=26)
    nodes = [("Aktion", "klicken, pflanzen, kämpfen", "👆", BLUE, BLUE_D),
             ("Feedback", "Ton, Partikel, Zahl", "✨", TEAL, TEAL_D),
             ("Belohnung", "Währung, Item, Fund", "💰", GOLD, GOLD_D),
             ("Verbesserung", "Upgrade, Kauf", "⬆️", PURPLE, PURPLE_D),
             ("Neue Möglichkeit", "schneller, größer, neu", "🔓", GREEN, GREEN_D)]
    angs = [-90 + i * 72 for i in range(5)]
    for i in range(5):
        arc_arrow(s, cx, cy, r, angs[i] + 25, angs[(i + 1) % 5] - 25 + (360 if i == 4 else 0), INK, 5)
    for i, (t, sub, ic, c, d) in enumerate(nodes):
        a = math.radians(angs[i])
        nx, ny = cx + r * math.cos(a), cy + r * math.sin(a)
        w = max(tw(t, 21), tw(sub, 14, False)) + 90
        node(s, nx, ny, w, 76, t, c, d, icon=ic, sub=sub, size=21)
    s.text(cx, cy - 18, "CORE", 46, INK, anchor="middle")
    s.text(cx, cy + 30, "LOOP", 46, INK, anchor="middle")
    s.text(cx, cy + 66, "Erste Aktion < 10 s", 16, MUTED, anchor="middle")
    s.text(cx, cy + 88, "Erste Belohnung < 30 s", 16, MUTED, anchor="middle")
    # Ringe
    rx, ry = 1196, 462
    rings = [(300, PURPLE, "MAKRO", "Tage – Wochen", "Rebirth, Saison, Sammelbuch → Rückkehr-Gründe"),
             (200, BLUE, "MESO", "3 – 15 Minuten", "Welle, Auftrag → Sitzungsziele"),
             (102, GREEN, "MIKRO", "2 – 30 Sekunden", "Ernten, Schlagen")]
    for rad, c, name, zeit, bsp in rings:
        s.circle(rx, ry, rad, fill=c, stroke=INK, sw=3, op=None, extra='fill-opacity="0.22"')
        s.circle(rx, ry, rad, fill="none", stroke=c, sw=5)
    # Pfeile auf den Ringen
    for rad, c in [(300, PURPLE_D), (200, BLUE_D), (102, GREEN_D)]:
        arc_arrow(s, rx, ry, rad, 300, 345, c, 6)
        arc_arrow(s, rx, ry, rad, 120, 165, c, 6)
    s.text(rx, ry - 252, "MAKRO · Tage – Wochen", 22, PURPLE_D, anchor="middle")
    s.text(rx, ry - 228, "Rebirth, Saison, Sammelbuch", 16, INK2, anchor="middle", bold=False)
    s.text(rx, ry - 156, "MESO · 3 – 15 min", 21, BLUE_D, anchor="middle")
    s.text(rx, ry - 133, "Welle, Auftrag", 16, INK2, anchor="middle", bold=False)
    s.text(rx, ry - 14, "MIKRO", 24, GREEN_D, anchor="middle")
    s.text(rx, ry + 14, "2 – 30 s", 19, GREEN_D, anchor="middle")
    s.text(rx, ry + 40, "Ernten, Schlagen", 15, INK2, anchor="middle", bold=False)
    s.text(rx, ry + 168, "Zweck: Sitzungsziele", 15, BLUE_D, anchor="middle")
    s.text(rx, ry + 262, "Zweck: Rückkehr-Gründe", 15, PURPLE_D, anchor="middle")
    s.text(rx, ry + 64, "sofortige Befriedigung", 12.5, GREEN_D, anchor="middle", bold=False)
    s.rect(866, 790, 694, 50, 14, fill=NOTE, stroke=GOLD_D, sw=2.5)
    s.text(884, 821, "Nur Mikro → nach 10 Min leer. Nur Makro → anfangs zäh. Alle drei bauen!", 15, INK)
    s.save(out)


# ---------------------------------------------------------------------------
LOOPS = [
    ("Simulator", "🧺", BLUE, BLUE_D, ["Sammeln", "Verkaufen", "Upgraden", "mehr sammeln"],
     "Sehr leicht verständlich", "Monoton → Zonen, Funde, Rebirth"),
    ("Warten-Ernten", "🌱", GREEN, GREEN_D, ["Setzen", "Warten", "Rückkehr", "Ernte"],
     "Rückkehr-Anker, passt zu Mobile", "Nur warten → aktive Boni"),
    ("Tag / Nacht", "🌙", PURPLE, PURPLE_D, ["Tag: sammeln", "Nacht: überleben", "Belohnung", "stärker"],
     "Natürlicher Rhythmus, Spannung", "Nacht zu hart/leicht → skalieren"),
    ("Tower Defense", "🏰", ORANGE, ORANGE_D, ["Aufbauen", "Welle", "Belohnung", "Verbessern"],
     "Strategische Tiefe", "Hoher Balancing-Aufwand"),
    ("Besitz mit Risiko", "🛡️", RED, RED_D, ["Sammeln", "Verteidigen", "Bestehlen"],
     "Emotionale Einsätze, Clips", "Frust → Schutzzeiten, Matchmaking"),
    ("Runden", "🔁", TEAL, TEAL_D, ["Lobby", "Runde", "Ergebnis", "Belohnung"],
     "Natürliche Wiederholung", "Leere Server → Mindestspieler"),
    ("Kampf-Progress", "⚔️", PINK, PINK_D, ["Trainieren", "Boss", "Fähigkeit", "stärkerer Boss"],
     "Starke Identität, Sammelreiz", "Balancing, Pay-to-win-Vorwurf"),
]


def loop_muster(out):
    s = Svg()
    sheet(s, "Loop-Muster auf Roblox – Übersicht",
          "Sieben typische Schleifen mit Stärke und Gefahr (aus core-loops.md)",
          "loop-muster-uebersicht.png", "Jeder Loop braucht ein Gegenmittel gegen Monotonie")
    cw, ch = (1520 - 3 * 20) / 4, 346
    for i in range(8):
        x = 40 + (i % 4) * (cw + 20)
        y = 122 + (i // 4) * (ch + 18)
        if i == 7:
            panel(s, x, y, cw, ch, fill=NOTE, stroke=GOLD_D)
            s.text(x + 22, y + 40, "So liest du die Karten", 20, INK)
            yy = y + 60
            for t in ["Pfeile = Reihenfolge der Schleife", "Symbol oben rechts = Genre",
                      "+ Stärke: warum es fesselt", "– Gefahr: was schiefgehen kann, mit Gegenmittel"]:
                yy += s.textbox(x + 22, yy, "• " + t, cw - 40, 16, INK2) + 8
            s.rect(x + 18, y + ch - 112, cw - 36, 92, 14, fill=WHITE, stroke=GOLD_D, sw=2)
            s.textbox(x + 32, y + ch - 104, "Regel: Jede Runde muss sich anders anfühlen als die letzte.", cw - 64, 16, INK, bold=True)
            continue
        name, ic, c, d, steps, plus, minus = LOOPS[i]
        panel(s, x, y, cw, ch, fill=WHITE, stroke=c)
        s.rect(x, y, cw, 48, 20, fill=c, stroke=INK, sw=4)
        s.text(x + 20, y + 33, "%d  %s" % (i + 1, name), 21, WHITE, outline=INK, ow=4)
        s.emoji(x + cw - 32, y + 24, ic, 30)
        lcx, lcy, lr, lry = x + cw / 2, y + 168, 104, 84
        n = len(steps)
        angs = [-90 + k * 360 / n for k in range(n)]
        s.ellipse(lcx, lcy, lr, lry, fill="none", stroke=c, sw=10, op=0.25)
        for k in range(n):
            arc_arrow(s, lcx, lcy, lr, angs[k] + (26 if n == 4 else 30), angs[(k + 1) % n] - (26 if n == 4 else 30) +
                      (360 if k == n - 1 else 0), d, 3.5, ry=lry)
        for k, st in enumerate(steps):
            a = math.radians(angs[k])
            nx, ny = lcx + lr * math.cos(a), lcy + lry * math.sin(a)
            w = tw(st, 14) + 22
            if n == 4 and k in (1, 3):
                nx = min(max(nx, x + 10 + w / 2), x + cw - 10 - w / 2)
            s.rect(nx - w / 2, ny - 15, w, 30, 15, fill=c, stroke=INK, sw=2.5)
            s.text(nx, ny + 5, st, 14, WHITE, anchor="middle", outline=INK, ow=3)
        s.text(x + 20, y + 290, "+", 20, GREEN_D)
        s.text(x + 40, y + 289, plus, 15, INK)
        s.text(x + 20, y + 322, "–", 20, RED_D)
        s.text(x + 40, y + 321, minus, 15, INK2, bold=False)
    s.save(out)


# ---------------------------------------------------------------------------
def retention_funnel(out):
    s = Svg()
    sheet(s, "Onboarding-Trichter: die ersten 30 Minuten",
          "Zeitplan als Startpunkt (zum Testen) mit Ziel und Maßnahme pro Schritt – Abbrüche je Schritt messen",
          "retention-funnel-onboarding.png", "Schnell zum Spaß, ein Konzept zur Zeit, Rückkehr-Grund am Ende")
    steps = [("0–10 s", "Spieler handelt", "Keine lange Cutscene, Spawn nah an erster Interaktion", "erste Aktion"),
             ("10–30 s", "Erste Belohnung", "Sichtbares Feedback: Ton, Zahl, Partikel", "erste Belohnung"),
             ("30–90 s", "Loop verstanden", "Pfeil/Highlight, max. 1 Satz pro Schritt", "Tutorial fertig"),
             ("1–3 min", "Erstes Upgrade", "Spürbare Verbesserung (2×, neuer Effekt)", "erstes Upgrade"),
             ("3–10 min", "Erstes Ziel / Zone", "Nächstes Ziel sichtbar, „Haken“-Gefühl", "Zone 2 erreicht"),
             ("10–30 min", "Meta-Einstieg", "Erste Sammlung, Rebirth oder Social-Hook", "Sammlung gestartet"),
             ("Sitzungsende", "Rückkehr-Grund", "Timer, Belohnung für morgen, unfertiger Fortschritt", "D1-Rückkehr")]
    n = len(steps)
    x0, x1, cyy = 50, 1550, 300
    sw_ = (x1 - x0) / n
    cols = ["#2ecc71", "#22c7a9", "#22b5c7", "#3d9bff", "#5b7bff", "#7d5bff", "#a24dff"]
    hmax, hmin = 290, 120
    for i, (zeit, ziel, mass, mp) in enumerate(steps):
        xa, xb = x0 + i * sw_, x0 + (i + 1) * sw_
        ha = hmax - (hmax - hmin) * i / n
        hb = hmax - (hmax - hmin) * (i + 1) / n
        s.poly([(xa, cyy - ha / 2), (xb, cyy - hb / 2), (xb, cyy + hb / 2), (xa, cyy + ha / 2)], fill=cols[i], stroke=INK, sw=3)
        s.poly([(xa + 4, cyy - ha / 2 + 6), (xb - 4, cyy - hb / 2 + 6), (xb - 4, cyy - hb / 2 + 22), (xa + 4, cyy - ha / 2 + 22)],
               fill=WHITE, op=0.22)
        mx = (xa + xb) / 2
        s.text(mx, cyy - 8, zeit, 23 if len(zeit) < 10 else 19, WHITE, anchor="middle", outline=INK, ow=4.5)
        lines = wrap(ziel, sw_ - 26, 16, True)
        for k, ln in enumerate(lines):
            s.text(mx, cyy + 22 + k * 20, ln, 16, WHITE, anchor="middle", outline=INK, ow=3.5)
        # Abbruch-Pfeil
        if i < n - 1:
            bx = xb
            by = cyy + hb / 2
            s.path("M%.1f,%.1f q10,26 34,40" % (bx - 14, by + 4), stroke=RED, sw=3, arrow=RED, dash="6 5")
        # Karte darunter
        cy2 = 478
        s.rect(xa + 6, cy2, sw_ - 12, 236, 16, fill=WHITE, stroke=cols[i], sw=3, extra='filter="url(#schattenK)"')
        s.rect(xa + 6, cy2, sw_ - 12, 10, 5, fill=cols[i])
        s.text(xa + 20, cy2 + 38, "Maßnahme", 15, cols[i] if i else GREEN_D)
        s.textbox(xa + 20, cy2 + 46, mass, sw_ - 40, 15, INK)
        s.line(xa + 20, cy2 + 168, xb - 20, cy2 + 168, stroke="#dde3f0", sw=2)
        s.text(xa + 20, cy2 + 192, "Messpunkt", 13, MUTED)
        s.text(xa + 20, cy2 + 214, mp, 14.5, INK)
    s.text(1550, 186, "Rote Pfeile = Abbrüche: je Schritt zählen (Funnel-Analytics im Creator Hub)", 15, RED_D, anchor="end")
    s.rect(50, 740, 1500, 90, 16, fill=NOTE, stroke=GOLD_D, sw=2.5)
    s.text(72, 774, "Regeln:", 18, INK)
    s.text(160, 774, "Zeigen statt erklären · ein Konzept zur Zeit · keine Strafen in den ersten Minuten · Überspringen erlauben", 17, INK, bold=False)
    s.text(72, 806, "Hinweis:", 18, INK)
    s.text(160, 806, "Trichterbreite ist illustrativ (keine echten Daten). Zeiten sind ein Startpunkt zum Testen, keine Regel.", 17, INK2, bold=False)
    s.save(out)


# ---------------------------------------------------------------------------
def chart_frame(s, x, y, w, h, title, xl, yl):
    panel(s, x, y, w, h, fill=WHITE)
    s.text(x + 24, y + 40, title, 23, INK)
    px, py, pw, ph = x + 80, y + 70, w - 110, h - 236
    for k in range(5):
        gy = py + ph * k / 4
        s.line(px, gy, px + pw, gy, stroke="#e3e8f3", sw=1.5)
    s.line(px, py - 10, px, py + ph, stroke=INK, sw=3, arrow=INK)
    s.line(px, py + ph, px + pw + 10, py + ph, stroke=INK, sw=3, arrow=INK)
    s.text(px + pw, py + ph + 34, xl, 16, INK2, anchor="end")
    s.text(px - 16, py + ph / 2, yl, 16, INK2, anchor="middle", extra='transform="rotate(-90 %d %d)"' % (px - 22, py + ph / 2))
    return px, py, pw, ph


def polyline(s, pts, color, sw=4, dash=None):
    d = "M" + " L".join("%.1f,%.1f" % p for p in pts)
    s.path(d, stroke=color, sw=sw, dash=dash)


def progression(out):
    s = Svg()
    sheet(s, "Progression: die Wand und der Rebirth",
          "Kosten steigen exponentiell, Einkommen linear → Fortschritt stockt. Rebirth setzt zurück und gibt dauerhaften Bonus.",
          "progression-kurve-rebirth.png", "Gegenmittel: Multiplikatoren, neue Einkommen, Rebirth")
    # links: Wand
    px, py, pw, ph = chart_frame(s, 40, 122, 750, 670, "1  Die Wand", "Spielzeit →", "Münzen")
    T = 10.0
    ymax = 520.0

    def X(t):
        return px + pw * t / T

    def Yv(v):
        return py + ph - ph * min(v, ymax) / ymax

    kosten = [(X(t / 10), Yv(8 * 1.62 ** (t / 10))) for t in range(0, 101) if 8 * 1.62 ** (t / 10) <= ymax * 1.02]
    einkommen = [(X(t / 10), Yv(40 + 32 * t / 10)) for t in range(0, 101)]
    # Schnittpunkt
    ts = next(t / 100 for t in range(0, 1001) if 8 * 1.62 ** (t / 100) > 40 + 32 * t / 100)
    s.rect(X(ts), py, px + pw - X(ts), ph, 0, fill="url(#schraffur)")
    s.text(X(ts) + 16, Yv(150), "WAND", 30, RED_D)
    s.textbox(X(ts) + 16, Yv(150) + 8, "Wartezeit pro Upgrade explodiert, Spieler gibt auf", px + pw - X(ts) - 26, 15, RED_D)
    polyline(s, einkommen, GREEN, 5)
    polyline(s, kosten, RED, 5)
    s.circle(X(ts), Yv(40 + 32 * ts), 9, fill=WHITE, stroke=INK, sw=3)
    tag(s, X(2.2), Yv(40 + 32 * 2.2) + 14, "Einkommen pro Minute (linear)", GREEN_D, 15)
    tag(s, X(0.4), Yv(430), "Kosten nächstes Upgrade (exponentiell)", RED_D, 15)
    arrow(s, X(4.1), Yv(430) + 30, X(6.6), Yv(8 * 1.62 ** 6.6), color=RED_D, bend=-0.2)
    s.rect(60, 690, 710, 82, 14, fill=NOTE, stroke=GOLD_D, sw=2.5)
    s.text(78, 720, "Gegenmittel vor der Wand:", 17, INK)
    s.text(78, 748, "Multiplikatoren · neue Einkommensquelle · neue Zone · Rebirth", 16, INK2, bold=False)
    # rechts: Rebirth
    px, py, pw, ph = chart_frame(s, 810, 122, 750, 670, "2  Rebirth / Prestige", "Spielzeit →", "Fortschritt")
    dur = [3.0, 2.4, 2.1, 1.9]
    bases = [0.0, 0.12, 0.24, 0.36]
    gains = [0.30, 0.42, 0.50, 0.56]
    mults = ["Bonus ×1", "×1,5", "×2,25", "×3,4"]

    def P(tv, v):
        return (px + pw * tv / 10.0, py + ph - ph * v)

    pts, peaks, starts = [], [], []
    tt = 0.0
    for k in range(4):
        starts.append(P(tt, bases[k]))
        for j in range(41):
            u = j / 40
            pts.append(P(tt + dur[k] * u, bases[k] + gains[k] * (1 - (1 - u) ** 2.2)))
        tt += dur[k]
        peaks.append(P(tt, bases[k] + gains[k]))
    polyline(s, starts + [P(tt, 0.48)], GOLD_D, 3, dash="10 8")
    polyline(s, pts, PURPLE, 5)
    tag(s, P(4.4, 0.13)[0], P(4.4, 0.13)[1], "steigende Basis = dauerhafter Bonus", GOLD_D, 14)
    for k in range(3):
        bx, by = peaks[k]
        s.circle(bx, by, 8, fill=WHITE, stroke=INK, sw=3)
        tag(s, bx, by - 44, "Rebirth %d" % (k + 1), PURPLE_D, 14, anchor="middle")
    t_acc = 0.0
    for k in range(4):
        mx = px + pw * (t_acc + dur[k] / 2) / 10.0
        s.text(mx, py + ph - 12, mults[k], 15, PURPLE_D, anchor="middle")
        t_acc += dur[k]
    s.rect(830, 690, 710, 82, 14, fill=NOTE, stroke=GOLD_D, sw=2.5)
    s.text(848, 720, "Erster Rebirth früh (ca. 20–40 Min, zum Testen).", 17, INK)
    s.text(848, 748, "Bonus spürbar (nicht +1 %), jede Runde schneller, schaltet Neues frei.", 16, INK2, bold=False)
    s.text(800, 830, "Kurven sind illustrativ (selbst berechnet), keine Messdaten.", 15, MUTED, anchor="middle", bold=False)
    s.save(out)


# ---------------------------------------------------------------------------
def gacha(out):
    s = Svg()
    sheet(s, "Gacha: Wahrscheinlichkeiten und Pity-System",
          "Beispiel-Chancen aus gacha-und-luck.md (Startpunkt, kein Standard) und ein sichtbarer Pity-Zähler",
          "gacha-wahrscheinlichkeiten-pity.png", "Chancen anzeigen, Pity sichtbar, Server lost aus")
    chancen = [60, 25, 10, 4, 0.9, 0.1]
    gefuehl = ["Alltag", "Freude", "Highlight", "Aufregung", "Geschichte", "Server-Meldung"]
    einvon = ["1 von 1,7", "1 von 4", "1 von 10", "1 von 25", "1 von 111", "1 von 1.000"]
    X, Y, W, H = 40, 122, 860, 712
    panel(s, X, Y, W, H, fill=WHITE)
    s.text(X + 24, Y + 42, "Chance pro Ei (Beispiel)", 23, INK)
    s.text(X + 24, Y + 68, "Balkenlänge linear – darum sind die seltenen Stufen winzig. Genau das macht sie wertvoll.", 15, MUTED, bold=False)
    bx, bw = X + 210, 420
    for i, (en, de, c, d, hx, sym) in enumerate(RARITY):
        y = Y + 96 + i * 72
        s.text(X + 24, y + 30, sym + " " + de, 19, d)
        s.text(X + 24, y + 52, gefuehl[i], 14, MUTED, bold=False)
        s.rect(bx, y + 8, bw, 40, 12, fill="#eef2fa")
        w = max(8, bw * chancen[i] / 60)
        s.rect(bx, y + 8, w, 40, 12, fill=c, stroke=INK, sw=2.5)
        lab = ("%s %%" % ("%g" % chancen[i]).replace(".", ","))
        s.text(bx + w + 12 if w < bw - 90 else bx + w - 12, y + 35, lab, 19, INK if w < bw - 90 else WHITE,
               anchor="start" if w < bw - 90 else "end", outline=None if w < bw - 90 else INK, ow=3)
        s.text(X + W - 24, y + 35, einvon[i], 16, INK2, anchor="end")
    # Zoom
    zy = Y + 540
    s.rect(X + 20, zy, W - 40, 150, 14, fill="#f6f8fd", stroke="#c9d3ee", sw=2)
    s.text(X + 40, zy + 30, "🔍 Lupe: 0–5 % vergrößert", 17, INK)
    for k, i in enumerate([3, 4, 5]):
        c, d = RARITY[i][2], RARITY[i][3]
        yy = zy + 46 + k * 32
        s.text(X + 40, yy + 20, RARITY[i][5] + " " + RARITY[i][1], 15, d)
        w = max(4, (W - 300) * chancen[i] / 5)
        s.rect(X + 200, yy + 4, w, 22, 8, fill=c, stroke=INK, sw=2)
        s.text(X + 210 + w, yy + 21, ("%g %%" % chancen[i]).replace(".", ","), 15, INK)
    # Pity
    px, py, pw = 924, 122, 636
    panel(s, px, py, pw, 712, fill=WHITE)
    s.text(px + 24, py + 42, "Pity: garantierter Treffer", 23, INK)
    s.text(px + 24, py + 68, "Frust-Schutz nach X Versuchen ohne Treffer – Zähler sichtbar.", 15, MUTED, bold=False)
    random.seed(7)
    tiles = []
    for k in range(30):
        if k < 27:
            r = random.random()
            tiles.append(0 if r < 0.68 else (1 if r < 0.93 else 2))
        else:
            tiles.append(None)
    ts, tg = 50, 10
    gx0, gy0 = px + 24 + (pw - 48 - (10 * ts + 9 * tg)) / 2, py + 96
    for k, t in enumerate(tiles):
        tx, ty = gx0 + (k % 10) * (ts + tg), gy0 + (k // 10) * (ts + tg)
        if k == 29:
            s.rect(tx - 4, ty - 4, ts + 8, ts + 8, 14, fill=PURPLE, op=0.45, extra='filter="url(#glow)"')
            s.rect(tx, ty, ts, ts, 12, fill=PURPLE, stroke=INK, sw=3)
            s.text(tx + ts / 2, ty + 34, "★", 26, WHITE, anchor="middle")
        elif t is None:
            s.rect(tx, ty, ts, ts, 12, fill="#eef2fa", stroke="#aab5cc", sw=2.5, extra='stroke-dasharray="6 5"')
            s.emoji(tx + ts / 2, ty + ts / 2, "🥚", 26, op=0.6)
        else:
            c, d = RARITY[t][2], RARITY[t][3]
            s.rect(tx, ty, ts, ts, 12, fill=c, stroke=INK, sw=2)
            s.text(tx + ts / 2, ty + 33, RARITY[t][5], 22, WHITE, anchor="middle", outline=d, ow=3)
    s.text(px + 24, gy0 + 3 * (ts + tg) + 26, "27 Würfe ohne Episch+ … Wurf 30 ist garantiert Episch.", 16, INK)
    # Zaehler-UI
    uy = py + 340
    s.rect(px + 24, uy, pw - 48, 196, 20, fill="#1b2440", stroke=INK, sw=3)
    s.emoji(px + 80, uy + 64, "🥚", 64)
    s.text(px + 130, uy + 50, "Wald-Ei", 22, WHITE)
    s.text(px + 130, uy + 76, "Chancen ansehen ⓘ", 15, "#9fc7ff")
    gbutton(s, px + pw - 230, uy + 28, 180, 56, "Öffnen", color=GREEN, dark=GREEN_D, size=22)
    s.text(px + 48, uy + 126, "Episch-Garantie", 15, WHITE)
    bar(s, px + 226, uy + 108, pw - 276, 24, 27 / 30, color=PURPLE, label="27 / 30", size=14)
    s.text(px + 48, uy + 168, "Legendär-Garantie", 15, WHITE)
    bar(s, px + 226, uy + 150, pw - 276, 24, 64 / 100, color=ORANGE, label="64 / 100", size=14)
    # Regeln
    ry = py + 560
    s.rect(px + 24, ry, pw - 48, 132, 14, fill=NOTE, stroke=GOLD_D, sw=2.5)
    for k, t in enumerate(["Server entscheidet den Zufall, nie der Client.",
                           "Luck-Boosts begrenzen (Obergrenze), auch verdienbar.",
                           "Bezahlter Zufall: Roblox-Regeln zur Offenlegung prüfen.",
                           "Seltenes auch ohne Geld erreichbar."]):
        s.text(px + 42, ry + 30 + k * 28, "•  " + t, 15.5, INK, bold=(k == 2))
    s.save(out)


ALLE = {
    "core-loop-diagramm": core_loop,
    "loop-muster-uebersicht": loop_muster,
    "retention-funnel-onboarding": retention_funnel,
    "progression-kurve-rebirth": progression,
    "gacha-wahrscheinlichkeiten-pity": gacha,
}
