"""Zeichnet eine Uebersicht aller Sounds (Wellenform + Mini-Spektrogramm) als PNG.

Damit kann z. B. Claude Projects (liest Bilder, aber kein Audio) die Klaenge "sehen":
Lautstaerkeverlauf (oben) und Tonhoehe/Frequenzen ueber die Zeit (unten, tief = unten).

Aufruf:  python3 tools/audio/wellenformen_bild.py
Ergebnis: assets/audio/audio-wellenformen.png
"""
import glob
import os
import wave

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HIER = os.path.dirname(os.path.abspath(__file__))
AUDIO = os.path.join(HIER, "..", "..", "assets", "audio")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

KAT = {  # Kategorie, Kurzbeschreibung
    "muenze-pling": ("Belohnung", "hell, 2 Töne aufwärts"),
    "muenze-pling-variante-1": ("Belohnung", "Variante −2 Halbtöne"),
    "muenze-pling-variante-2": ("Belohnung", "Variante +2 Halbtöne"),
    "muenze-pling-variante-3": ("Belohnung", "Variante +4 Halbtöne"),
    "pling-leiter": ("Belohnung", "5 Glocken steigend (Kombo)"),
    "kauf-erfolg": ("Belohnung", "Münze + Dur-Arpeggio"),
    "level-up-fanfare": ("Belohnung", "Bläser-Fanfare + Akkord"),
    "seltener-drop-mythic": ("Belohnung", "Riser · Stille · Impact · Akkord"),
    "checkpoint": ("Belohnung", "2 helle Glocken + Funkeln"),
    "pop-klein": ("UI", "kurz, rund, fallend"),
    "ui-klick": ("UI", "sehr kurz, trocken"),
    "ui-oeffnen": ("UI", "Gleiten aufwärts"),
    "ui-schliessen": ("UI", "Gleiten abwärts"),
    "ui-fehler": ("UI", "2 tiefe Summ-Töne fallend"),
    "countdown-tick": ("UI", "Holzblock-Tick"),
    "whoosh-impact": ("Kampf", "Schwung + Schlag"),
    "treffer-schwer": ("Kampf", "tiefer Wumms + Knacken"),
    "sprung": ("Kampf", "kurzes Gleiten aufwärts"),
    "ernte-weich": ("Natur", "Plopp + Rascheln + Marimba"),
    "wachstum-sparkle": ("Natur", "Funkeln wird dichter"),
    "nacht-beginnt-warnung": ("Warnung", "Gong + fallende Bläser + Drone"),
    "alarm-diebstahl": ("Warnung", "Zwei-Ton-Sirene"),
    "horror-drone-loop": ("Loop", "tiefe Schwebung, Wind"),
    "lofi-loop-menue": ("Loop", "Fmaj7–Em7–Dm7–Cmaj7, 80 BPM"),
    "ambiente-wind-loop": ("Loop", "Rauschen mit Böen"),
    "ambiente-wasser-loop": ("Loop", "Bach-Rauschen + Blubbern"),
}
FARBE = {"Belohnung": (255, 170, 30), "UI": (61, 155, 255), "Kampf": (255, 77, 94), "Natur": (46, 204, 113),
         "Warnung": (162, 77, 255), "Loop": (34, 199, 199)}
REIHENFOLGE = list(KAT.keys())
GAP = (1600 - 80 - 4 * 382) / 3


def lade(path):
    with wave.open(path) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), dtype="<i2").astype(float) / 32768
        return x, w.getframerate()


def farbskala(v):
    """0..1 -> dunkelblau -> lila -> orange -> gelb"""
    stops = [(0, (20, 26, 52)), (0.35, (98, 40, 160)), (0.65, (240, 90, 60)), (0.85, (255, 175, 40)), (1, (255, 245, 170))]
    for (a, ca), (b, cb) in zip(stops, stops[1:]):
        if v <= b:
            f = (v - a) / (b - a)
            return tuple(int(ca[i] + (cb[i] - ca[i]) * f) for i in range(3))
    return stops[-1][1]


def spektro(x, sr, cols, rows=28, fmin=80, fmax=12000):
    n = 2048
    hop = max(1, (len(x) - n) // cols) if len(x) > n else 1
    xp = np.concatenate([x, np.zeros(n + hop * cols)])
    win = np.hanning(n)
    freqs = np.fft.rfftfreq(n, 1 / sr)
    edges = np.geomspace(fmin, fmax, rows + 1)
    M = np.zeros((rows, cols))
    for c in range(cols):
        seg = xp[c * hop: c * hop + n] * win
        P = np.abs(np.fft.rfft(seg)) ** 2
        for r in range(rows):
            m = (freqs >= edges[r]) & (freqs < edges[r + 1])
            M[r, c] = P[m].mean() if m.any() else 0
    D = 10 * np.log10(M + 1e-12)
    D -= D.max()
    return np.clip((D + 60) / 60, 0, 1)


def main():
    files = {os.path.basename(p)[:-4]: p for p in glob.glob(os.path.join(AUDIO, "*.wav"))}
    names = [n for n in REIHENFOLGE if n in files] + sorted(n for n in files if n not in KAT)
    cols, pw, ph = 4, 382, 168
    W = 1600
    H = 130 + ((len(names) + 1) // cols + 1) * (ph + 12) + 40
    img = Image.new("RGB", (W, H), (240, 244, 252))
    d = ImageDraw.Draw(img)
    fb = lambda s: ImageFont.truetype(FONTB, s)
    fr = lambda s: ImageFont.truetype(FONT, s)
    d.rectangle([40, 34, 52, 96], fill=(61, 155, 255))
    d.text((68, 34), "Referenz-Sounds: Wellenform und Spektrogramm", font=fb(38), fill=(27, 36, 64))
    d.text((70, 82), "Oben: Lautstärke über die Zeit · Unten: Frequenzen (tief unten, hoch oben, hell = laut) · alle Sounds selbst synthetisiert",
           font=fr(18), fill=(107, 118, 148))
    for i, n in enumerate(names):
        x0 = 40 + (i % cols) * (pw + GAP)
        y0 = 130 + (i // cols) * (ph + 12)
        kat, kurz = KAT.get(n, ("Sonstiges", ""))
        col = FARBE.get(kat, (150, 150, 150))
        d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], 16, fill=(255, 255, 255), outline=col, width=3)
        d.rounded_rectangle([x0, y0, x0 + 8, y0 + ph], 4, fill=col)
        x, sr = lade(files[n])
        dur = len(x) / sr
        d.text((x0 + 18, y0 + 10), n, font=fb(16), fill=(27, 36, 64))
        meta = "%s · %.2f s · %s" % (kat, dur, kurz)
        d.text((x0 + 18, y0 + 32), meta, font=fr(12.5), fill=(74, 85, 120))
        # Wellenform
        wx, wy, ww, wh = x0 + 18, y0 + 54, pw - 34, 56
        d.rectangle([wx, wy, wx + ww, wy + wh], fill=(246, 248, 253))
        mid = wy + wh / 2
        seg = np.array_split(x, ww)
        for k, s_ in enumerate(seg):
            if len(s_) == 0:
                continue
            lo, hi = s_.min(), s_.max()
            d.line([(wx + k, mid - hi * wh / 2), (wx + k, mid - lo * wh / 2)], fill=col)
        d.line([(wx, mid), (wx + ww, mid)], fill=(200, 208, 225))
        # Spektrogramm
        sx, sy, sh = wx, wy + wh + 4, 42
        S = spektro(x, sr, ww)
        rows = S.shape[0]
        for r in range(rows):
            for c in range(ww):
                y_ = sy + sh - (r + 1) * sh / rows
                d.rectangle([sx + c, y_, sx + c, y_ + sh / rows], fill=farbskala(S[r, c]))
        if kat == "Loop":
            d.rounded_rectangle([x0 + pw - 74, y0 + 10, x0 + pw - 14, y0 + 30], 10, fill=col)
            d.text((x0 + pw - 66, y0 + 12), "LOOP", font=fb(13), fill=(255, 255, 255))
    # Legende
    i = len(names)
    x0 = 40 + (i % cols) * (pw + GAP)
    y0 = 130 + (i // cols) * (ph + 12)
    d.rounded_rectangle([x0, y0, x0 + pw * 2 + GAP if i % cols < 3 else x0 + pw, y0 + ph], 16,
                        fill=(255, 248, 220), outline=(217, 154, 11), width=3)
    d.text((x0 + 18, y0 + 12), "Kategorien", font=fb(17), fill=(27, 36, 64))
    for k, (kat, col) in enumerate(FARBE.items()):
        xx = x0 + 18 + (k % 3) * 120
        yy = y0 + 44 + (k // 3) * 30
        d.rounded_rectangle([xx, yy, xx + 22, yy + 18], 5, fill=col)
        d.text((xx + 30, yy), kat, font=fr(15), fill=(27, 36, 64))
    d.text((x0 + 18, y0 + 112), "Frei verwendbar in eigenen Spielen (eigene Synthese).", font=fr(14), fill=(74, 85, 120))
    d.text((x0 + 18, y0 + 134), "Details: assets/audio/README.md", font=fr(14), fill=(74, 85, 120))
    d.rectangle([0, H - 34, W, H], fill=(27, 36, 64))
    d.text((24, H - 26), "Eigenes Referenzbild (selbst erstellt, frei nutzbar) · Roblox-Datenbank · audio-wellenformen.png",
           font=fr(15), fill=(201, 211, 238))
    out = os.path.join(AUDIO, "audio-wellenformen.png")
    img.save(out, optimize=True)
    print("PNG:", out, img.size)


if __name__ == "__main__":
    main()
