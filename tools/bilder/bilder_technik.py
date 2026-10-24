"""Audio-Mix, Client-Server-Architektur und Monetarisierung."""
from svglib import *  # noqa: F401,F403

MONO = "'DejaVu Sans Mono', Menlo, Consolas, monospace"


def audio_mix(out):
    s = Svg()
    sheet(s, "Audio-Mix: Prioritäten und SoundGroups",
          "Welche Klänge sich durchsetzen dürfen – und wie man das in Roblox mit SoundGroups organisiert",
          "audio-mix-prioritaeten.png", "Warnung > Belohnung > UI > SFX > Musik > Ambiente")
    X, Y, W, H = 40, 122, 760, 712
    panel(s, X, Y, W, H, fill=WHITE)
    s.text(X + 24, Y + 42, "Mix-Pyramide", 23, INK)
    s.text(X + 24, Y + 68, "Oben: selten, setzt sich durch. Unten: immer da, aber leise.", 15, MUTED, bold=False)
    stufen = [("Warnung", "Gefahr, Nacht beginnt, Boss", RED, RED_D, "🚨"),
              ("Belohnung", "seltener Drop, Level-Up, Kauf", GOLD, GOLD_D, "🏆"),
              ("UI", "Klick, Öffnen, Fehler", BLUE, BLUE_D, "🖱️"),
              ("SFX", "Schritte, Treffer, Ernte", TEAL, TEAL_D, "💥"),
              ("Musik", "Zonen-Thema, Menü-Loop", PURPLE, PURPLE_D, "🎵"),
              ("Ambiente", "Wind, Wasser, Vögel", GREEN, GREEN_D, "🌿")]
    cx = X + 330
    top, bh = Y + 96, 96
    for i, (n, d, c, dk, ic) in enumerate(stufen):
        y0, y1 = top + i * bh, top + (i + 1) * bh - 8
        w0, w1 = 80 + i * 92, 80 + (i + 1) * 92 - 14
        s.poly([(cx - w0 / 2, y0), (cx + w0 / 2, y0), (cx + w1 / 2, y1), (cx - w1 / 2, y1)], fill=c, stroke=INK, sw=3)
        s.text(cx, (y0 + y1) / 2 + 2, n, 22 if i else 18, WHITE, anchor="middle", outline=INK, ow=4)
        if i < 3:
            s.text(cx, (y0 + y1) / 2 + 24, "%d. Priorität" % (i + 1), 13, WHITE, anchor="middle", outline=dk, ow=3)
            s.emoji(cx + w1 / 2 + 34, (y0 + y1) / 2, ic, 28)
            s.text(cx + w1 / 2 + 58, (y0 + y1) / 2 + 6, d, 15, INK2, bold=False)
        else:
            s.text(cx, (y0 + y1) / 2 + 26, "%d. · %s" % (i + 1, d), 15, WHITE, anchor="middle", outline=dk, ow=3.5)
            s.emoji(cx - w1 / 2 + 70, (y0 + y1) / 2 - 2, ic, 30)
    s.line(X + 40, top + 6 * bh - 20, X + 40, top + 10, stroke=INK, sw=4, arrow=INK)
    s.text(X + 30, top + 3 * bh, "Priorität / darf unterbrechen", 15, INK, anchor="middle",
           extra='transform="rotate(-90 %d %d)"' % (X + 26, top + 3 * bh))
    # Baum
    tx, ty, tw_ = 824, 122, 736
    panel(s, tx, ty, tw_, 470, fill=WHITE)
    s.text(tx + 24, ty + 42, "SoundGroup-Baum (Startwerte zum Testen)", 23, INK)

    def box(x, y, w, h, t1, t2, c):
        s.rect(x, y, w, h, 12, fill=c, stroke=INK, sw=2.5, extra='fill-opacity="0.18"')
        s.rect(x, y, 8, h, 4, fill=c)
        s.text(x + 18, y + 26, t1, 16, INK, family=MONO)
        if t2:
            s.text(x + 18, y + 48, t2, 14, INK2, bold=False)

    box(tx + 24, ty + 66, 260, 58, "SoundService", "Musik/UI ohne Raumposition", GREY_D)
    box(tx + 330, ty + 66, 382, 58, "SoundGroup „Master“", "+ CompressorSoundEffect (keine Übersteuerung)", INK2)
    s.line(tx + 284, ty + 95, tx + 330, ty + 95, stroke=INK, sw=3)
    kinder = [("Musik", "Volume 0,4", PURPLE), ("Ambiente", "Volume 0,3", GREEN), ("UI", "Volume 0,6", BLUE),
              ("SFX", "Volume 0,8", TEAL)]
    for k, (n, v, c) in enumerate(kinder):
        y = ty + 150 + k * 72
        s.path("M%d,%d V%d H%d" % (tx + 360, ty + 124, y + 28, tx + 400), stroke=INK, sw=3)
        box(tx + 400, y, 170, 56, n, v, c)
    for k, (n, v, c) in enumerate([("Belohnung", "Volume 1,0", GOLD_D), ("Warnung", "Volume 1,0", RED)]):
        y = ty + 150 + 3 * 72 + 70 + k * 0
        x = tx + 400 + 0 + k * 160
    # SFX-Untergruppen nebeneinander
    s.path("M%d,%d H%d" % (tx + 570, ty + 150 + 3 * 72 + 28, tx + 584), stroke=INK, sw=3)
    s.path("M%d,%d V%d" % (tx + 584, ty + 150 + 2 * 72 + 30, ty + 150 + 3 * 72 + 50), stroke=INK, sw=3)
    for k, (n, v, c) in enumerate([("Belohnung", "Volume 1,0", GOLD_D), ("Warnung", "Volume 1,0", RED)]):
        y = ty + 150 + 2 * 72 + 4 + k * 72
        s.line(tx + 584, y + 26, tx + 596, y + 26, stroke=INK, sw=3)
        box(tx + 596, y, 122, 52, n, v, c)
    s.text(tx + 24, ty + 190, "Sound als Kind eines Parts", 15, INK)
    s.text(tx + 24, ty + 212, "= 3D-Raumklang (Wasserfall,", 14, INK2, bold=False)
    s.text(tx + 24, ty + 232, "Lagerfeuer). Sound.SoundGroup", 14, INK2, bold=False)
    s.text(tx + 24, ty + 252, "trotzdem zuweisen.", 14, INK2, bold=False)
    # Einstellungs-Regler
    s.rect(tx + 24, ty + 286, 330, 150, 16, fill="#1b2440", stroke=INK, sw=3)
    s.text(tx + 44, ty + 322, "⚙️ Einstellungen", 17, WHITE)
    for k, (n, f) in enumerate([("Musik", 0.4), ("Effekte", 0.8), ("Ambiente", 0.3)]):
        yy = ty + 348 + k * 30
        s.text(tx + 44, yy + 14, n, 14, WHITE)
        bar(s, tx + 140, yy, 190, 18, f, color=BLUE)
    s.text(tx + 24, ty + 460, "Spieler regeln Gruppen getrennt (Musik aus, Effekte an).", 13.5, MUTED, bold=False)
    # Tipps
    py = 612
    panel(s, tx, py, tw_, 222, fill=NOTE, stroke=GOLD_D)
    s.text(tx + 24, py + 36, "Mix-Regeln", 20, INK)
    tips = ["Ducking: Musik bei Fanfare kurz leiser (Volume per Tween senken, dann zurück).",
            "Cooldown pro Sound-Typ; gleichzeitige Sounds begrenzen, ähnliche zusammenfassen.",
            "Alle Dateien ähnlich laut anlegen (normalisieren), Feinmix über Gruppen.",
            "Auf Handy-Lautsprecher UND Kopfhörern testen."]
    yy = py + 50
    for t in tips:
        s.text(tx + 26, yy + 17, "•", 18, GOLD_D)
        yy += s.textbox(tx + 44, yy, t, tw_ - 70, 15.5, INK) + 8
    s.save(out)


# ---------------------------------------------------------------------------
def client_server(out):
    s = Svg()
    sheet(s, "Client-Server-Architektur in Roblox",
          "Der Server ist die Wahrheit, der Client sendet nur Wünsche – Beispiel: ein Kauf mit Münzen",
          "client-server-architektur.png", "Nie dem Client vertrauen, alles mit Wert am Server")

    def zone(x, y, w, h, title, sub, c, ic):
        s.rect(x, y, w, h, 24, fill=c, stroke=INK, sw=4, extra='fill-opacity="0.12" filter="url(#schatten)"')
        s.rect(x, y, w, 64, 24, fill=c, stroke=INK, sw=4)
        s.emoji(x + 36, y + 32, ic, 30)
        s.text(x + 62, y + 30, title, 22, WHITE, outline=INK, ow=4)
        s.text(x + 62, y + 52, sub, 14, WHITE, outline=INK, ow=3)

    def cbox(x, y, w, h, cls, txt, c):
        s.rect(x, y, w, h, 14, fill=WHITE, stroke=c, sw=3)
        s.text(x + 16, y + 28, cls, 16, c, family=MONO)
        s.textbox(x + 16, y + 34, txt, w - 30, 14.5, INK2)

    # Zonen
    zone(40, 122, 440, 520, "Client", "Gerät des Spielers", BLUE, "📱")
    zone(530, 122, 440, 520, "ReplicatedStorage", "für beide sichtbar", PURPLE, "🔁")
    zone(1020, 122, 540, 520, "Server", "Roblox-Server, die Wahrheit", RED, "🖥️")
    cbox(64, 210, 392, 100, "LocalScript", "in StarterPlayerScripts: Eingabe, UI-Logik, Effekte, Sounds", BLUE_D)
    cbox(64, 330, 392, 90, "PlayerGui → ScreenGui", "HUD, Shop-Fenster (nur Anzeige)", BLUE_D)
    s.rect(64, 440, 392, 110, 14, fill="#ffe8ea", stroke=RED, sw=3)
    s.emoji(96, 478, "🕵️", 34)
    s.text(126, 470, "Nicht vertrauenswürdig!", 17, RED_D)
    s.textbox(126, 478, "Exploiter können LocalScripts ändern und Remotes beliebig feuern.", 314, 14.5, INK2)
    cbox(554, 210, 392, 110, "ModuleScript", "Konfiguration: Preise, Chancen, Item-Daten (Balancing ohne Code-Umbau)", PURPLE_D)
    cbox(554, 340, 392, 84, "RemoteEvent „KaufWunsch“", "Brücke Client ↔ Server", PURPLE_D)
    cbox(554, 444, 392, 84, "RemoteFunction", "sparsam (Server wartet sonst auf Client)", PURPLE_D)
    cbox(1044, 210, 492, 96, "Script (ServerScriptService)", "Spiellogik, Ökonomie, Zufalls-Drops, Schaden", RED_D)
    # Validierung
    s.rect(1044, 322, 492, 132, 14, fill=WHITE, stroke=GREEN_D, sw=3)
    s.text(1060, 350, "Prüfen bei jedem Remote-Aufruf:", 16, GREEN_D)
    for k, t in enumerate(["Typ richtig?", "Wertebereich ok?", "Genug Münzen?", "Cooldown / Rate-Limit?"]):
        xx = 1060 + (k % 2) * 236
        yy = 378 + (k // 2) * 34
        s.circle(xx + 10, yy + 6, 10, fill=GREEN)
        s.text(xx + 10, yy + 11, "✔", 13, WHITE, anchor="middle")
        s.text(xx + 28, yy + 12, t, 15, INK, bold=False)
    cbox(1044, 470, 236, 150, "DataStoreService", "UpdateAsync + pcall, Retry, Session-Lock, Schema-Version", RED_D)
    cbox(1296, 470, 240, 150, "MarketplaceService", "ProcessReceipt: erst speichern, dann PurchaseGranted", RED_D)
    # Ablauf
    def step(n, x, y, c=INK):
        badge(s, x, y, n, c, r=16)

    arrow(s, 456, 255, 554, 375, color=BLUE_D, sw=4, bend=-0.15)
    step(1, 505, 300, BLUE_D)
    arrow(s, 946, 375, 1044, 255, color=PURPLE_D, sw=4, bend=-0.15)
    step(2, 1000, 300, PURPLE_D)
    arrow(s, 1160, 454, 1160, 470, color=GREEN_D, sw=4, bend=0)
    s.path("M1044,600 C900,640 640,640 560,580 S470,420 462,384", stroke=GREEN_D, sw=4, dash="10 7", arrow=GREEN_D)
    step(4, 760, 610, GREEN_D)
    # Exploit-Pfeil
    arrow(s, 300, 550, 600, 424, color=RED, sw=3, bend=0.25, dash="6 6")
    # Legende unten
    ly = 666
    panel(s, 40, ly, 1520, 170, fill=WHITE)
    s.text(64, ly + 36, "Ablauf: Kauf eines Schwerts für 500 Münzen", 20, INK)
    rows = [("1", BLUE_D, "Client: Spieler tippt „Kaufen“ → KaufWunsch:FireServer(„Schwert“). Sendet nur den Wunsch, keinen Preis."),
            ("2", PURPLE_D, "Server: OnServerEvent → prüft Typ, Item existiert, genug Münzen, Cooldown. Preis kommt aus dem ModuleScript."),
            ("3", RED_D, "Server: Münzen abziehen, Item geben, per DataStore sichern (UpdateAsync, pcall)."),
            ("4", GREEN_D, "Server → Client: FireClient/Attribute → HUD zählt hoch, Erfolgs-Sound. ✘ Exploit-Aufruf „gib 1.000.000“ wird abgelehnt + geloggt.")]
    for k, (n, c, t) in enumerate(rows):
        yy = ly + 56 + k * 28
        badge(s, 76, yy + 8, n, c, r=11)
        s.text(96, yy + 14, t, 15, INK, bold=False)
    step(3, 1180, 462, RED_D)
    s.save(out)


# ---------------------------------------------------------------------------
def monetarisierung(out):
    s = Svg()
    sheet(s, "Monetarisierung: Produkte und Fairness",
          "Gamepass, Developer Product und Kosmetik im Vergleich – und wo ein Angebot auf der Skala fair ↔ Pay-to-win liegt",
          "monetarisierung-produkte.png", "Zeit, Komfort, Aussehen verkaufen – nie den Fortschritt sperren")
    cols = [("Gamepass", "🎫", BLUE, BLUE_D), ("Developer Product", "🧪", ORANGE, ORANGE_D), ("Kosmetik", "✨", PURPLE, PURPLE_D)]
    rows = [("Kauf", ["Einmal, dauerhaft", "Mehrfach kaufbar", "Einmal (als Pass/Product oder UGC)"]),
            ("Beispiele", ["2× Geld, VIP, Extra-Slot, Auto-Sammeln", "Münzpakete, Zeit-Boost, Wiederbeleben",
                           "Skins, Spuren, Haustier-Look, Emotes"]),
            ("Wirkung", ["Beschleunigt dauerhaft", "Kurzfristiger Schub", "Nur Aussehen und Status"]),
            ("Fairness", ["Kein Grundfortschritt hinter Pass", "Wirkung + Dauer klar, keine Druck-Popups",
                          "Am fairsten, Vorschau zeigen"]),
            ("Technik", ["UserOwnsGamePassAsync am Server, cachen", "ProcessReceipt: erst speichern, dann Granted",
                         "Vorschau im Shop, Besitz am Server"])]
    X, Y = 40, 122
    lw, cw, rh = 180, (1520 - 180) / 3, 74
    panel(s, X, Y, 1520, 74 + rh * len(rows) + 10, fill=WHITE)
    for k, (n, ic, c, d) in enumerate(cols):
        x = X + lw + k * cw
        s.rect(x + 6, Y + 10, cw - 12, 56, 16, fill=c, stroke=INK, sw=3)
        s.emoji(x + 40, Y + 38, ic, 30)
        s.text(x + 66, Y + 47, n, 23, WHITE, outline=INK, ow=4)
    for r, (rn, vals) in enumerate(rows):
        y = Y + 74 + r * rh
        if r % 2 == 0:
            s.rect(X + 8, y, 1504, rh, 10, fill="#f3f6fc")
        s.text(X + 24, y + rh / 2 + 7, rn, 18, INK)
        for k, v in enumerate(vals):
            x = X + lw + k * cw
            lines = wrap(v, cw - 40, 16, False)
            y0 = y + rh / 2 - (len(lines) - 1) * 10 + 6
            for j, ln in enumerate(lines):
                s.text(x + 20, y0 + j * 21, ln, 16 if r != 4 else 15, INK if r != 4 else INK2, bold=False,
                       family=MONO if (r == 4 and False) else FAMILY)
    # Skala
    sy = Y + 74 + rh * len(rows) + 34
    panel(s, X, sy, 1520, 836 - sy, fill=WHITE)
    s.text(X + 24, sy + 38, "Skala: fair ↔ Pay-to-win", 21, INK)
    bx0, bx1, by = X + 70, X + 1450, sy + 128
    s.rect(bx0, by - 16, bx1 - bx0, 32, 16, fill=s.gradient([(0, GREEN), (0.5, GOLD), (1, RED)], x2=1, y2=0), stroke=INK, sw=3)
    s.text(bx0, by + 46, "fair", 17, GREEN_D)
    s.text(bx1, by + 46, "Pay-to-win", 17, RED_D, anchor="end")
    marks = [(0.05, "Kosmetik", "✨", True), (0.22, "Komfort (Plätze, Auto)", "🎒", False), (0.40, "Zeit-Boost 15 Min", "⏱️", True),
             (0.57, "Dauer-2× Geld", "💰", False), (0.76, "Starke Exklusiv-Items", "⚔️", True), (0.95, "Fortschritt nur mit Kauf", "🚫", False)]
    for f, t, ic, up in marks:
        mx = bx0 + (bx1 - bx0) * f
        s.circle(mx, by, 16, fill=WHITE, stroke=INK, sw=3)
        s.emoji(mx, by, ic, 18)
        w = tw(t, 14) + 18
        if up:
            s.line(mx, by - 16, mx, by - 30, stroke=INK, sw=2)
            s.rect(mx - w / 2, by - 58, w, 28, 14, fill=INK)
            s.text(mx, by - 39, t, 14, WHITE, anchor="middle")
        else:
            s.line(mx, by + 16, mx, by + 30, stroke=INK, sw=2)
            s.rect(mx - w / 2, by + 30, w, 28, 14, fill=INK)
            s.text(mx, by + 49, t, 14, WHITE, anchor="middle")
    s.text(X + 760, 826, "Boosts erhöhen die Geschwindigkeit, nicht die Obergrenze. Nicht-Zahler erreichen jedes Ziel, nur langsamer.",
           16, INK, anchor="middle")
    s.save(out)


ALLE = {
    "audio-mix-prioritaeten": audio_mix,
    "client-server-architektur": client_server,
    "monetarisierung-produkte": monetarisierung,
}
