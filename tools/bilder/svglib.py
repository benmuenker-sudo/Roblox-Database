"""Kleine SVG-Bibliothek fuer die Referenzbilder der Roblox-Datenbank.

Alle Bilder werden als reines SVG (1600x900) erzeugt und danach mit
`render.js` (Playwright/Chromium) in PNG umgewandelt.
Textbreiten werden mit der DejaVu-Schrift gemessen (Pillow), damit
Beschriftungen nicht ueberlaufen.
"""
import math
import os
from xml.sax.saxutils import escape

try:
    from PIL import ImageFont
except ImportError:  # pragma: no cover
    ImageFont = None

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
FAMILY = "'DejaVu Sans', Verdana, Geneva, sans-serif"
EMOJI = "'Noto Color Emoji', 'Apple Color Emoji', 'Segoe UI Emoji', sans-serif"

# Grundfarben
INK = "#1b2440"
INK2 = "#4a5578"
MUTED = "#6b7694"
WHITE = "#ffffff"
GREEN, GREEN_D = "#2ecc71", "#1e9e55"
RED, RED_D = "#ff4d5e", "#c9303f"
GOLD, GOLD_D = "#ffc93c", "#d99a0b"
BLUE, BLUE_D = "#3d9bff", "#1f6fd1"
PURPLE, PURPLE_D = "#a24dff", "#7428d1"
ORANGE, ORANGE_D = "#ff9a1f", "#d4730a"
PINK, PINK_D = "#ff3d7f", "#c81e5a"
GREY, GREY_D = "#9aa5b8", "#6f7a90"
TEAL, TEAL_D = "#22c7c7", "#139595"
NOTE = "#fff8dc"

RARITY = [
    # (Name, deutsch, Farbe, dunkel, Hex-Text, Symbol)
    ("Common", "Gewöhnlich", "#9aa5b8", "#6f7a90", "#9AA5B8", "●"),
    ("Uncommon", "Ungewöhnlich", "#3ccf5a", "#239a3c", "#3CCF5A", "▲"),
    ("Rare", "Selten", "#3d8bff", "#1f5fd1", "#3D8BFF", "◆"),
    ("Epic", "Episch", "#a24dff", "#7428d1", "#A24DFF", "★"),
    ("Legendary", "Legendär", "#ffa21f", "#d4730a", "#FFA21F", "♛"),
    ("Mythic", "Mythisch", "#ff3d7f", "#c81e5a", "#FF3D7F", "✦"),
]

_fonts = {}


def tw(s, size, bold=True):
    """Textbreite in px fuer DejaVu Sans (Bold/Regular)."""
    key = (bold, int(round(size)))
    if key not in _fonts:
        f = None
        if ImageFont is not None:
            path = FONT_DIR + ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf")
            if os.path.exists(path):
                f = ImageFont.truetype(path, key[1])
        _fonts[key] = f
    f = _fonts[key]
    if f is None:
        return len(s) * size * (0.66 if bold else 0.6)
    return f.getlength(s)


def wrap(s, maxw, size, bold=False):
    lines = []
    for para in s.split("\n"):
        words = para.split(" ")
        cur = ""
        for w in words:
            t = (cur + " " + w).strip()
            if tw(t, size, bold) <= maxw or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def fmt(v):
    if isinstance(v, float):
        return ("%.2f" % v).rstrip("0").rstrip(".")
    return str(v)


class Svg:
    def __init__(self, w=1600, h=900):
        self.w, self.h = w, h
        self.defs = []
        self.body = []
        self._ids = 0
        self._markers = set()
        self.defs.append(
            '<filter id="schatten" x="-20%" y="-20%" width="140%" height="150%">'
            '<feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#0b1330" flood-opacity="0.22"/></filter>'
            '<filter id="schattenK" x="-20%" y="-20%" width="140%" height="150%">'
            '<feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#0b1330" flood-opacity="0.25"/></filter>'
            '<filter id="glow" x="-50%" y="-50%" width="200%" height="200%">'
            '<feGaussianBlur stdDeviation="8" result="b"/><feMerge><feMergeNode in="b"/>'
            '<feMergeNode in="SourceGraphic"/></feMerge></filter>'
            '<filter id="silhouette"><feColorMatrix type="matrix" values="0 0 0 0 0.16  0 0 0 0 0.19  0 0 0 0 0.3  0 0 0 1 0"/></filter>'
            '<filter id="grau"><feColorMatrix type="saturate" values="0"/></filter>'
            '<pattern id="schraffur" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            '<rect width="12" height="12" fill="#ff4d5e" fill-opacity="0.10"/>'
            '<line x1="0" y1="0" x2="0" y2="12" stroke="#ff4d5e" stroke-width="4" stroke-opacity="0.45"/></pattern>'
            '<pattern id="schraffurGrau" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
            '<rect width="12" height="12" fill="#1b2440" fill-opacity="0.18"/>'
            '<line x1="0" y1="0" x2="0" y2="12" stroke="#1b2440" stroke-width="4" stroke-opacity="0.35"/></pattern>'
            '<pattern id="punkte" width="28" height="28" patternUnits="userSpaceOnUse">'
            '<circle cx="2" cy="2" r="1.6" fill="#1b2440" fill-opacity="0.07"/></pattern>'
        )

    # ---------- Grundformen ----------
    def uid(self, p="id"):
        self._ids += 1
        return "%s%d" % (p, self._ids)

    def raw(self, s):
        self.body.append(s)

    def defs_add(self, s):
        self.defs.append(s)

    def _attrs(self, fill=None, stroke=None, sw=None, op=None, extra=""):
        a = ""
        if fill is not None:
            a += ' fill="%s"' % fill
        if stroke is not None:
            a += ' stroke="%s"' % stroke
        if sw is not None:
            a += ' stroke-width="%s"' % fmt(sw)
        if op is not None:
            a += ' opacity="%s"' % fmt(op)
        if extra:
            a += " " + extra
        return a

    def rect(self, x, y, w, h, r=0, fill="none", stroke=None, sw=None, op=None, extra=""):
        self.body.append(
            '<rect x="%s" y="%s" width="%s" height="%s" rx="%s"%s/>'
            % (fmt(x), fmt(y), fmt(w), fmt(h), fmt(r), self._attrs(fill, stroke, sw, op, extra))
        )

    def circle(self, cx, cy, r, fill="none", stroke=None, sw=None, op=None, extra=""):
        self.body.append(
            '<circle cx="%s" cy="%s" r="%s"%s/>' % (fmt(cx), fmt(cy), fmt(r), self._attrs(fill, stroke, sw, op, extra))
        )

    def ellipse(self, cx, cy, rx, ry, fill="none", stroke=None, sw=None, op=None, extra=""):
        self.body.append(
            '<ellipse cx="%s" cy="%s" rx="%s" ry="%s"%s/>'
            % (fmt(cx), fmt(cy), fmt(rx), fmt(ry), self._attrs(fill, stroke, sw, op, extra))
        )

    def line(self, x1, y1, x2, y2, stroke=INK, sw=3, dash=None, arrow=None, op=None, cap="round", extra=""):
        e = 'stroke-linecap="%s"' % cap
        if dash:
            e += ' stroke-dasharray="%s"' % dash
        if arrow:
            e += ' marker-end="url(#%s)"' % self.marker(arrow)
        if extra:
            e += " " + extra
        self.body.append(
            '<line x1="%s" y1="%s" x2="%s" y2="%s"%s/>'
            % (fmt(x1), fmt(y1), fmt(x2), fmt(y2), self._attrs(None, stroke, sw, op, e))
        )

    def path(self, d, fill="none", stroke=None, sw=None, op=None, arrow=None, dash=None, extra=""):
        e = 'stroke-linecap="round" stroke-linejoin="round"'
        if arrow:
            e += ' marker-end="url(#%s)"' % self.marker(arrow)
        if dash:
            e += ' stroke-dasharray="%s"' % dash
        if extra:
            e += " " + extra
        self.body.append('<path d="%s"%s/>' % (d, self._attrs(fill, stroke, sw, op, e)))

    def poly(self, pts, fill="none", stroke=None, sw=None, op=None, extra=""):
        p = " ".join("%s,%s" % (fmt(x), fmt(y)) for x, y in pts)
        self.body.append(
            '<polygon points="%s"%s/>' % (p, self._attrs(fill, stroke, sw, op, 'stroke-linejoin="round" ' + extra))
        )

    def marker(self, color):
        mid = "pfeil" + color.replace("#", "")
        if mid not in self._markers:
            self._markers.add(mid)
            self.defs.append(
                '<marker id="%s" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" '
                'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 L2.5,5 z" fill="%s"/></marker>' % (mid, color)
            )
        return mid

    def text(self, x, y, s, size=22, fill=INK, bold=True, anchor="start", op=None, family=FAMILY,
             outline=None, ow=None, extra="", italic=False):
        e = 'font-family="%s" font-size="%s" font-weight="%s" text-anchor="%s"' % (
            family, fmt(size), "700" if bold else "400", anchor)
        if italic:
            e += ' font-style="italic"'
        if outline:
            e += ' stroke="%s" stroke-width="%s" paint-order="stroke" stroke-linejoin="round"' % (
                outline, fmt(ow if ow else max(2, size / 7)))
        if extra:
            e += " " + extra
        self.body.append(
            '<text x="%s" y="%s"%s>%s</text>' % (fmt(x), fmt(y), self._attrs(fill, None, None, op, e), escape(s))
        )

    def emoji(self, cx, cy, ch, size=40, op=None, extra=""):
        # y-Versatz, damit das Emoji optisch zentriert ist
        self.body.append(
            '<text x="%s" y="%s" font-family="%s" font-size="%s" text-anchor="middle"%s%s>%s</text>'
            % (fmt(cx), fmt(cy + size * 0.36), EMOJI, fmt(size),
               (' opacity="%s"' % fmt(op)) if op is not None else "", (" " + extra) if extra else "", escape(ch))
        )

    def textbox(self, x, y, s, maxw, size=18, fill=INK, bold=False, lh=1.32, anchor="start"):
        """Mehrzeiliger Text, y = Oberkante. Gibt Hoehe zurueck."""
        lines = wrap(s, maxw, size, bold)
        for i, ln in enumerate(lines):
            self.text(x, y + size + i * size * lh, ln, size, fill, bold, anchor)
        return len(lines) * size * lh

    def g(self, extra):
        self.body.append("<g %s>" % extra)

    def g_end(self):
        self.body.append("</g>")

    def gradient(self, stops, x2=0, y2=1, gid=None):
        gid = gid or self.uid("verlauf")
        st = "".join('<stop offset="%s" stop-color="%s"%s/>' % (
            fmt(o), c, (' stop-opacity="%s"' % fmt(a)) if a is not None else "")
            for o, c, a in [(t + (None,))[:3] for t in stops])
        self.defs.append('<linearGradient id="%s" x1="0" y1="0" x2="%s" y2="%s">%s</linearGradient>' % (gid, fmt(x2), fmt(y2), st))
        return "url(#%s)" % gid

    def radial(self, stops, gid=None, cx=0.5, cy=0.5, r=0.5):
        gid = gid or self.uid("radial")
        st = "".join('<stop offset="%s" stop-color="%s"%s/>' % (
            fmt(o), c, (' stop-opacity="%s"' % fmt(a)) if a is not None else "")
            for o, c, a in [(t + (None,))[:3] for t in stops])
        self.defs.append('<radialGradient id="%s" cx="%s" cy="%s" r="%s">%s</radialGradient>' % (gid, fmt(cx), fmt(cy), fmt(r), st))
        return "url(#%s)" % gid

    def save(self, path):
        out = [
            '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">' % (self.w, self.h, self.w, self.h),
            "<defs>" + "".join(self.defs) + "</defs>",
        ]
        out += self.body
        out.append("</svg>")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(out))


# ---------- Bausteine ----------

def sheet(s, title, subtitle, datei, regel=None):
    """Hintergrund, Titel und Fusszeile fuer alle Referenzbilder."""
    s.rect(0, 0, s.w, s.h, fill=s.gradient([(0, "#f7f9fe"), (1, "#e4ecf9")]))
    s.rect(0, 0, s.w, s.h, fill="url(#punkte)")
    s.rect(40, 34, 12, 62, r=6, fill=s.gradient([(0, BLUE), (1, PURPLE)]))
    s.text(68, 72, title, 40, INK)
    s.text(70, 100, subtitle, 19, MUTED, bold=False)
    s.rect(0, s.h - 34, s.w, 34, fill=INK)
    s.text(24, s.h - 11, "Eigenes Referenzbild (selbst erstellt, frei nutzbar) · Roblox-Datenbank", 15, "#c9d3ee", bold=False)
    s.text(s.w - 24, s.h - 11, ("Regel: " + regel + "  ·  " if regel else "") + datei, 15, "#c9d3ee", bold=False, anchor="end")


def panel(s, x, y, w, h, fill=WHITE, stroke=INK, r=22, sw=4, shadow=True, op=None):
    s.rect(x, y, w, h, r, fill=fill, stroke=stroke, sw=sw, op=op, extra='filter="url(#schatten)"' if shadow else "")


def gbutton(s, x, y, w, h, label="", color=GREEN, dark=GREEN_D, size=None, r=None, icon=None, icon_size=None,
            text_color=WHITE, outline=True, sw=3):
    """Roblox-typischer 3D-Button: dunkle Unterkante, helle Glanzflaeche, Text mit Kontur."""
    r = r if r is not None else min(16, h / 3)
    s.rect(x, y + 5, w, h, r, fill=dark, stroke=INK, sw=sw)
    s.rect(x, y, w, h, r, fill=color, stroke=INK, sw=sw)
    s.rect(x + 6, y + 4, w - 12, h * 0.38, max(2, r - 4), fill=WHITE, op=0.28)
    size = size or h * 0.42
    cx = x + w / 2
    if icon and label:
        isz = icon_size or h * 0.55
        total = isz + 8 + tw(label, size)
        sx = cx - total / 2
        s.emoji(sx + isz / 2, y + h / 2, icon, isz)
        s.text(sx + isz + 8, y + h / 2 + size * 0.36, label, size, text_color, anchor="start",
               outline=INK if outline else None, ow=size / 5)
    elif icon:
        s.emoji(cx, y + h / 2, icon, icon_size or h * 0.58)
    elif label:
        s.text(cx, y + h / 2 + size * 0.36, label, size, text_color, anchor="middle",
               outline=INK if outline else None, ow=size / 5)


def round_button(s, cx, cy, r, color=BLUE, dark=BLUE_D, icon=None, label=None, size=None, sw=3):
    s.circle(cx, cy + 5, r, fill=dark, stroke=INK, sw=sw)
    s.circle(cx, cy, r, fill=color, stroke=INK, sw=sw)
    s.ellipse(cx, cy - r * 0.45, r * 0.62, r * 0.3, fill=WHITE, op=0.3)
    if icon:
        s.emoji(cx, cy - (r * 0.12 if label else 0), icon, r * (0.85 if label else 1.05))
    if label:
        sz = size or r * 0.34
        s.text(cx, cy + (r * 0.62 if icon else sz * 0.36), label, sz, WHITE, anchor="middle", outline=INK, ow=sz / 4)


def notif_dot(s, cx, cy, n=None, r=13):
    s.circle(cx, cy, r, fill=RED, stroke=WHITE, sw=3)
    if n is not None:
        s.text(cx, cy + r * 0.42, str(n), r * 1.15, WHITE, anchor="middle")


def coin(s, cx, cy, r=18):
    s.circle(cx, cy + 2, r, fill=GOLD_D, stroke=INK, sw=2.5)
    s.circle(cx, cy, r, fill=GOLD, stroke=INK, sw=2.5)
    s.circle(cx, cy, r * 0.68, fill="none", stroke="#e8a817", sw=max(1.5, r * 0.12))
    star(s, cx, cy, r * 0.42, "#e8a817")


def gem(s, cx, cy, r=18, color="#5fd3ff", dark="#1f8fc7"):
    pts = [(cx - r, cy - r * 0.3), (cx - r * 0.5, cy - r * 0.85), (cx + r * 0.5, cy - r * 0.85),
           (cx + r, cy - r * 0.3), (cx, cy + r)]
    s.poly(pts, fill=color, stroke=INK, sw=2.5)
    s.poly([(cx - r, cy - r * 0.3), (cx + r, cy - r * 0.3), (cx, cy + r)], fill=dark, op=0.45)
    s.poly([(cx - r * 0.5, cy - r * 0.85), (cx - r * 0.1, cy - r * 0.3), (cx - r * 0.75, cy - r * 0.3)], fill=WHITE, op=0.5)


def robux(s, cx, cy, r=14, color=INK):
    """Neutrales Platzhalter-Symbol fuer Robux-Preise (Sechseck + R$)."""
    pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in range(30, 390, 60)]
    s.poly(pts, fill="none", stroke=color, sw=max(2, r * 0.22))
    s.text(cx, cy + r * 0.32, "R$", r * 0.82, color, anchor="middle")


def star(s, cx, cy, r, fill=GOLD, stroke=None, sw=None, points=5, inner=0.45):
    pts = []
    for i in range(points * 2):
        a = math.radians(-90 + i * 180 / points)
        rr = r if i % 2 == 0 else r * inner
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    s.poly(pts, fill=fill, stroke=stroke, sw=sw)


def badge(s, cx, cy, n, color=BLUE, r=17, text_color=WHITE):
    s.circle(cx, cy, r, fill=color, stroke=WHITE, sw=3, extra='filter="url(#schattenK)"')
    s.text(cx, cy + r * 0.38, str(n), r * 1.05, text_color, anchor="middle")


def pill(s, x, y, w, h, fill=WHITE, stroke=INK, sw=3, op=None):
    s.rect(x, y, w, h, h / 2, fill=fill, stroke=stroke, sw=sw, op=op)


def bar(s, x, y, w, h, frac, color=GREEN, back="#24304f", stroke=INK, sw=2.5, label=None, size=None):
    s.rect(x, y, w, h, h / 2, fill=back, stroke=stroke, sw=sw)
    if frac > 0:
        s.rect(x + 2, y + 2, max(h - 4, (w - 4) * frac), h - 4, (h - 4) / 2, fill=color)
        s.rect(x + 6, y + 4, max(0, (w - 12) * frac), (h - 4) * 0.3, (h - 4) * 0.15, fill=WHITE, op=0.35)
    if label:
        sz = size or h * 0.62
        s.text(x + w / 2, y + h / 2 + sz * 0.36, label, sz, WHITE, anchor="middle", outline=INK, ow=sz / 4.5)


def box_anchor(bx, by, bw, bh, tx, ty):
    """Punkt auf dem Rand eines Rechtecks Richtung Ziel."""
    cx, cy = bx + bw / 2, by + bh / 2
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    sx = (bw / 2) / abs(dx) if dx else 1e9
    sy = (bh / 2) / abs(dy) if dy else 1e9
    k = min(sx, sy)
    return cx + dx * k, cy + dy * k


def arrow(s, x1, y1, x2, y2, color=INK, sw=3, bend=0.18, dash=None, shorten=6):
    """Gebogener Pfeil von (x1,y1) nach (x2,y2)."""
    dx, dy = x2 - x1, y2 - y1
    d = math.hypot(dx, dy) or 1
    x2s, y2s = x2 - dx / d * shorten, y2 - dy / d * shorten
    mx, my = (x1 + x2s) / 2, (y1 + y2s) / 2
    nx, ny = -dy / d, dx / d
    cx, cy = mx + nx * d * bend, my + ny * d * bend
    s.path("M%s,%s Q%s,%s %s,%s" % (fmt(x1), fmt(y1), fmt(cx), fmt(cy), fmt(x2s), fmt(y2s)),
           stroke=color, sw=sw, arrow=color, dash=dash)


def callout(s, x, y, w, title, body=None, target=None, color=BLUE, num=None, size=17, tsize=19,
            bend=0.15, fill=WHITE, dot=True, targets=None):
    """Erklaer-Kaestchen mit Nummer und optionalem Pfeil zum Ziel."""
    pad = 14
    inner = w - 2 * pad - (30 if num is not None else 0)
    tl = wrap(title, inner, tsize, True)
    bl = wrap(body, w - 2 * pad, size, False) if body else []
    h = pad + len(tl) * tsize * 1.25 + (6 + len(bl) * size * 1.32 if bl else 0) + pad - 2
    tgts = targets or ([target] if target else [])
    for t in tgts:
        ax, ay = box_anchor(x, y, w, h, t[0], t[1])
        arrow(s, ax, ay, t[0], t[1], color=color, sw=3, bend=bend)
        if dot:
            s.circle(t[0], t[1], 5, fill=color, stroke=WHITE, sw=2)
    s.rect(x, y, w, h, 14, fill=fill, stroke=color, sw=3, extra='filter="url(#schattenK)"')
    s.rect(x, y, 8, h, 4, fill=color)
    tx = x + pad + (30 if num is not None else 0)
    if num is not None:
        badge(s, x + pad + 12, y + pad + tsize * 0.5, num, color, r=14)
    for i, ln in enumerate(tl):
        s.text(tx, y + pad + tsize * 0.95 + i * tsize * 1.25, ln, tsize, INK)
    yy = y + pad + len(tl) * tsize * 1.25 + 6
    for i, ln in enumerate(bl):
        s.text(x + pad, yy + size * 0.95 + i * size * 1.32, ln, size, INK2, bold=False)
    return h


def tag(s, x, y, text, color=INK, size=16, anchor="start", text_color=WHITE):
    """Kleines dunkles Etikett direkt im Bild."""
    w = tw(text, size) + 18
    h = size + 12
    if anchor == "middle":
        x -= w / 2
    elif anchor == "end":
        x -= w
    s.rect(x, y, w, h, h / 2, fill=color, op=0.92)
    s.text(x + w / 2, y + h / 2 + size * 0.36, text, size, text_color, anchor="middle")
    return w, h


def avatar(s, cx, base, sc=1.0, shirt="#2f7fd6", pants="#3ea84a", skin="#f5cd30"):
    """Einfache Block-Spielfigur (generisch)."""
    u = 10 * sc
    s.ellipse(cx, base, 3.2 * u, 0.9 * u, fill="#000", op=0.18)
    s.rect(cx - 2 * u, base - 4 * u, 1.9 * u, 4 * u, 0.4 * u, fill=pants, stroke=INK, sw=2)
    s.rect(cx + 0.1 * u, base - 4 * u, 1.9 * u, 4 * u, 0.4 * u, fill=pants, stroke=INK, sw=2)
    s.rect(cx - 3.9 * u, base - 8 * u, 1.8 * u, 4 * u, 0.4 * u, fill=skin, stroke=INK, sw=2)
    s.rect(cx + 2.1 * u, base - 8 * u, 1.8 * u, 4 * u, 0.4 * u, fill=skin, stroke=INK, sw=2)
    s.rect(cx - 2 * u, base - 8 * u, 4 * u, 4.1 * u, 0.4 * u, fill=shirt, stroke=INK, sw=2)
    s.rect(cx - 1.4 * u, base - 10.9 * u, 2.8 * u, 2.8 * u, 0.7 * u, fill=skin, stroke=INK, sw=2)
    s.circle(cx - 0.55 * u, base - 9.7 * u, 0.22 * u, fill=INK)
    s.circle(cx + 0.55 * u, base - 9.7 * u, 0.22 * u, fill=INK)
    s.path("M%s,%s Q%s,%s %s,%s" % (fmt(cx - 0.6 * u), fmt(base - 9.0 * u), fmt(cx), fmt(base - 8.6 * u),
                                     fmt(cx + 0.6 * u), fmt(base - 9.0 * u)), stroke=INK, sw=1.6)


def tree(s, cx, base, sc=1.0, color="#3fae47", dark="#2b8a36"):
    u = 10 * sc
    s.rect(cx - 0.8 * u, base - 4 * u, 1.6 * u, 4 * u, 0.4 * u, fill="#8a5a2b", stroke=INK, sw=2)
    s.circle(cx, base - 6.5 * u, 3.6 * u, fill=dark, stroke=INK, sw=2)
    s.circle(cx - 0.8 * u, base - 7.2 * u, 2.6 * u, fill=color)
    s.circle(cx - 1.5 * u, base - 8 * u, 0.9 * u, fill=WHITE, op=0.25)


def game_world(s, x, y, w, h, sky=("#6fc8ff", "#cdefff"), ground=("#6ad35f", "#43ad45"), horizon=0.42):
    """Einfache Spielwelt als Hintergrund fuer HUD-Mockups."""
    hy = y + h * horizon
    s.rect(x, y, w, h, 0, fill=s.gradient([(0, sky[0]), (1, sky[1])]))
    # Wolken
    for (fx, fy, sc) in [(0.15, 0.12, 1), (0.55, 0.08, 1.3), (0.82, 0.18, 0.9)]:
        cx, cy = x + w * fx, y + h * fy
        for dx, dy, r in [(-30, 6, 22), (0, 0, 30), (32, 8, 20)]:
            s.circle(cx + dx * sc, cy + dy * sc, r * sc, fill=WHITE, op=0.85)
    # Huegel
    s.path("M%s,%s Q%s,%s %s,%s T%s,%s L%s,%s L%s,%s Z" % (
        fmt(x), fmt(hy + 10), fmt(x + w * 0.2), fmt(hy - h * 0.12), fmt(x + w * 0.45), fmt(hy),
        fmt(x + w), fmt(hy - h * 0.05), fmt(x + w), fmt(hy + 20), fmt(x), fmt(hy + 20)), fill="#58b860", op=0.8)
    s.rect(x, hy, w, y + h - hy, 0, fill=s.gradient([(0, ground[0]), (1, ground[1])]))
    return hy
