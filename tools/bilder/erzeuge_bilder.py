"""Erzeugt alle SVG-Referenzbilder in assets/bilder/.

Aufruf (aus dem Repo-Hauptordner):
    python3 tools/bilder/erzeuge_bilder.py            # alle SVGs
    python3 tools/bilder/erzeuge_bilder.py name ...   # nur bestimmte (ohne Endung)
Danach PNGs rendern:
    node tools/bilder/render.js
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bilder_ui  # noqa: E402

MODULE = [bilder_ui]
for name in ("bilder_loops", "bilder_map", "bilder_technik"):
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), name + ".py")):
        MODULE.append(__import__(name))

ZIEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets", "bilder")


def main():
    os.makedirs(ZIEL, exist_ok=True)
    nur = set(sys.argv[1:])
    for m in MODULE:
        for name, fn in m.ALLE.items():
            if nur and name not in nur:
                continue
            fn(os.path.join(ZIEL, name + ".svg"))
            print("SVG:", name + ".svg")


if __name__ == "__main__":
    main()
