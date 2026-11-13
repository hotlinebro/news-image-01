"""Round 2 entry for make.fun news-image-01.

Copies the rendered newspaper front page (entry.png) to /output/entry.png.
Deterministic: the same bytes on every run, no network, no randomness.

Round 2 redesign: a flat-vector night scene leads the page (burning tanker,
radar dome, Bahrain flag), a "WHERE IT HAPPENED" world map pins the stories,
and 22 numbered stories cover Friday 13 November 2026. The image is drawn
by ../news-image-01-build/render.py (PIL, kept out of this repo) and copied
here as entry.png; this program only copies it to the output path.
"""
import os
import shutil


def main():
    os.makedirs("/output", exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    shutil.copy(src, "/output/entry.png")


if __name__ == "__main__":
    main()
