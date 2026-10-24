"""Zusatzbilder: Ideen-Generator und Genre-Uebersicht."""
from svglib import *  # noqa: F401,F403


def ideen_generator(out):
    s = Svg()
    sheet(s, "Ideen-Generator: Fantasie × Loop × Spannung × Meta",
          "Je ein Baustein pro Spalte wählen, Ein-Satz-Test machen, dann die 7 Filterfragen (aus ideen-methodik.md)",
          "ideen-generator-matrix.png", "Hits in Bausteine zerlegen, neu kombinieren, früh testen")
    spalten = [
        ("Fantasie", "🎭", BLUE, BLUE_D, ["Bäcker", "Archäologe", "Fischer", "Hacker", "Hausmeister", "Tierarzt", "Geisterjäger",
                                         "Wetterforscher", "Pirat"], 2),
        ("Loop", "🔁", GREEN, GREEN_D, ["Farmen und Verkaufen", "Erkunden und Sammeln", "Bauen und Verteidigen", "Craften und Liefern",
                                       "Aufziehen und Kämpfen"], 0),
        ("Spannung", "⚡", ORANGE, ORANGE_D, ["Nachtgefahr", "Diebstahl durch andere", "Zeitlimit", "Zufalls-Mutation", "Wetter-Events",
                                            "Konkurrenz-Rangliste"], 4),
        ("Meta", "📖", PURPLE, PURPLE_D, ["Sammelbuch", "Rebirth", "Saisonpass", "Gilden", "Museum", "Handelsmarkt"], 0),
    ]
    cw, gap, X, Y = 248, 18, 40, 122
    sel = []
    for i, (name, ic, c, d, opts, pick) in enumerate(spalten):
        x = X + i * (cw + gap)
        panel(s, x, Y, cw, 590, fill=WHITE, stroke=c)
        s.rect(x, Y, cw, 56, 20, fill=c, stroke=INK, sw=4)
        s.emoji(x + 32, Y + 28, ic, 26)
        s.text(x + 56, Y + 37, name, 22, WHITE, outline=INK, ow=4)
        for k, o in enumerate(opts):
            yy = Y + 74 + k * 56
            if k == pick:
                s.rect(x + 12, yy - 4, cw - 24, 48, 24, fill=GOLD, op=0.5, extra='filter="url(#glow)"')
                gbutton(s, x + 16, yy, cw - 32, 40, o, color=GOLD, dark=GOLD_D, size=15 if len(o) < 20 else 13.5, r=20, sw=2.5)
                sel.append((x + cw / 2, yy + 20))
            else:
                pill(s, x + 16, yy, cw - 32, 40, fill="#f3f6fc", stroke=c, sw=2)
                s.text(x + cw / 2, yy + 26, o, 15 if len(o) < 20 else 13.5, INK, anchor="middle", bold=False)
    # Verbindungslinie durch die Auswahl
    for (x1, y1), (x2, y2) in zip(sel, sel[1:]):
        s.path("M%.0f,%.0f C%.0f,%.0f %.0f,%.0f %.0f,%.0f" % (x1 + 100, y1, x1 + 140, y1, x2 - 140, y2, x2 - 104, y2),
               stroke=GOLD_D, sw=5, dash="2 9", arrow=GOLD_D)
    # Ergebnis
    rx, rw = 1120, 440
    panel(s, rx, Y, rw, 250, fill=NOTE, stroke=GOLD_D)
    s.text(rx + 22, Y + 40, "Rohidee (noch ungeprüft)", 21, INK)
    s.text(rx + 22, Y + 70, "Fischer × Farmen × Wetter × Sammelbuch", 16, GOLD_D)
    s.textbox(rx + 22, Y + 84, "Jeder Teich hat eigenes Wetter; seltene Fische erscheinen nur bei Sturm; ein Fischbuch zeigt die Vollständigkeit.",
              rw - 44, 16, INK)
    s.rect(rx + 18, Y + 176, rw - 36, 56, 14, fill=WHITE, stroke=GOLD_D, sw=2)
    s.text(rx + 32, Y + 199, "Ein-Satz-Test:", 14, MUTED)
    s.text(rx + 32, Y + 221, "„Du fängst Fische, um das Fischbuch zu füllen.“", 13.5, INK)
    # Filterfragen
    fy = Y + 270
    panel(s, rx, fy, rw, 442, fill=WHITE)
    s.text(rx + 22, fy + 38, "Die 7 Filterfragen", 21, INK)
    fragen = [("Ein-Satz", "In einem Satz erklärbar?"), ("10 Sekunden", "Klare erste Aktion?"),
              ("Wiederholung", "Nach 30 Min noch Spaß?"), ("Rückkehr", "Warum morgen wieder?"),
              ("Social", "Warum erzählt man es Freunden?"), ("Content", "8 Wochen Updates ohne Umbau?"),
              ("Monetarisierung", "Fairer Kauf, der beschleunigt?")]
    for k, (t, q) in enumerate(fragen):
        yy = fy + 58 + k * 48
        badge(s, rx + 36, yy + 16, k + 1, BLUE, r=14)
        s.text(rx + 60, yy + 14, t, 16, INK)
        s.text(rx + 60, yy + 34, q, 14.5, INK2, bold=False)
    s.rect(rx + 18, fy + 398, rw - 36, 32, 12, fill="#ffe8ea", stroke=RED, sw=2)
    s.text(rx + 32, fy + 420, "≥ 3 durchgefallen → verwerfen oder umbauen", 14.5, RED_D)
    # Weitere Beispiele
    by = 722
    s.rect(40, by, 1046, 112, 18, fill=WHITE, stroke="#c9d3ee", sw=2.5)
    s.text(60, by + 28, "Weitere Rohideen aus der Datenbank:", 17, INK)
    by -= 8
    ex = ["Archäologe × Erkunden × Mutation × Museum", "Geisterjäger × Verteidigen × Nachtgefahr × Gilden",
          "Bäcker × Craften × Diebstahl × Saisonpass"]
    xx = 60
    for k, e in enumerate(ex):
        w = tw(e, 13.5) + 24
        if xx + w > 1070:
            xx = 60
            by += 38
        pill(s, xx, by + 46, w, 32, fill="#f3f6fc", stroke=INK2, sw=2)
        s.text(xx + w / 2, by + 67, e, 13.5, INK, anchor="middle")
        xx += w + 10
    s.save(out)


GENRES = [
    ("Simulator", "🧺", BLUE, "„Ich werde stärker/reicher“", "Aktion → Währung → Upgrade → Rebirth", "Einfach, Fortschritt, Monetarisierung",
     "Austauschbar, viele Klone"),
    ("Survival", "🔥", ORANGE, "„Ich überlebe gegen Druck“", "Tag sammeln → Nacht verteidigen", "Lange Sessions, Spannung, Koop",
     "Content-Hunger, Balancing"),
    ("Anime-Kampf", "⚔️", PINK, "„Ich werde ein starker Kämpfer“", "Trainieren → Boss → Fähigkeit", "Loyale Community, Sammeln",
     "Komplexes Balancing, Cheater"),
    ("Roleplay / Social", "🏠", TEAL, "„Ich spiele eine Rolle“", "Frei spielen, Häuser, Autos", "Sehr lange Verweildauer",
     "Wenig Umsatz pro Kopf, Moderation"),
    ("Tycoon", "🏭", GOLD_D, "„Ich baue ein Imperium“", "Geld → Maschinen → mehr Geld", "Klarer Fortschritt",
     "Kurze Halbwertszeit ohne Updates"),
    ("Horror", "👻", PURPLE, "„Ich überstehe die Angst“", "Erkunden → Gefahr → Flucht", "Teilbar (Streams), Koop",
     "Hoher Content-Bedarf, Altersfreigabe"),
    ("Obby / Parkour", "🏃", GREEN, "„Ich schaffe die Strecke“", "Strecke → Checkpoint → Belohnung", "Günstig, schneller Einstieg",
     "Kurze Sessions, niedrige Retention"),
    ("Social Deduction", "🕵️", RED, "„Ich durchschaue die anderen“", "Runden mit Rollen", "Natürliche Wiederholung, Streamer",
     "Braucht viele Spieler"),
    ("Tower Defense", "🏰", ORANGE_D, "„Ich plane die Verteidigung“", "Wellen → Upgrades → Boss", "Strategische Tiefe, Sammel-Meta",
     "Balancing, Content"),
    ("Shooter / Waffen", "🎯", GREY_D, "„Ich gewinne den Kampf“", "Runde → Level → Loadout", "Hohes Skill-Ceiling",
     "Hohe Qualitätsanforderung"),
]


def genre_uebersicht(out):
    s = Svg()
    sheet(s, "Genre-Übersicht: Fantasie, Loop, Stärken, Risiken",
          "Zehn Roblox-Genres auf einen Blick (aus genre-analyse.md) – Hits sind oft Mischungen aus zwei Genres plus Meta-Schicht",
          "genre-uebersicht.png", "Genre A (Loop) × Genre B (Spannung) × Meta-Schicht")
    cw, ch = (1520 - 4 * 16) / 5, 300
    for i, (n, ic, c, fant, loop, plus, minus) in enumerate(GENRES):
        x = 40 + (i % 5) * (cw + 16)
        y = 122 + (i // 5) * (ch + 16)
        panel(s, x, y, cw, ch, fill=WHITE, stroke=c)
        s.rect(x, y, cw, 52, 20, fill=c, stroke=INK, sw=3.5)
        s.emoji(x + 28, y + 26, ic, 26)
        s.text(x + 50, y + 34, n, 18 if len(n) < 15 else 16, WHITE, outline=INK, ow=4)
        yy = y + 62
        yy += s.textbox(x + 16, yy, fant, cw - 32, 15.5, INK, bold=True) + 10
        s.rect(x + 12, yy, cw - 24, 2, 1, fill="#e3e8f3")
        yy += 10
        s.text(x + 16, yy + 13, "Loop", 13, MUTED)
        yy += 16
        yy += s.textbox(x + 16, yy, loop, cw - 32, 14.5, INK2) + 14
        s.text(x + 16, yy + 16, "+", 17, GREEN_D)
        yy += s.textbox(x + 34, yy, plus, cw - 50, 14.5, INK) + 8
        s.text(x + 16, yy + 16, "–", 17, RED_D)
        s.textbox(x + 34, yy, minus, cw - 50, 14.5, INK2)
    # Mischungen
    y = 122 + 2 * (ch + 16)
    s.rect(40, y, 1520, 836 - y, 18, fill=NOTE, stroke=GOLD_D, sw=3)
    s.text(62, y + 34, "Hits sind oft Mischungen:", 19, INK)
    mixes = ["Farming + Meme-Ästhetik + Tower Defense", "Sammeln + Stehlen (Besitz mit Risiko)", "Survival + Horror + Koop"]
    xx = 330
    for m in mixes:
        w = tw(m, 15) + 28
        pill(s, xx, y + 12, w, 34, fill=WHITE, stroke=GOLD_D, sw=2)
        s.text(xx + w / 2, y + 35, m, 15, INK, anchor="middle")
        xx += w + 12
    s.text(62, y + 74, "Auswahl-Hilfe: Team-Kapazität, Content-Pipeline, Monetarisierungs-Fit, Streamer-Tauglichkeit, Sättigung prüfen.",
           16, INK2, bold=False)
    s.save(out)


ALLE = {
    "ideen-generator-matrix": ideen_generator,
    "genre-uebersicht": genre_uebersicht,
}
