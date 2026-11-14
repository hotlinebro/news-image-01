"""Round 3 entry for make.fun news-image-01.

Copies the rendered newspaper front page (entry.png) to /output/entry.png.
Deterministic: the same bytes on every run, no network, no randomness.

Round 3 redesign: the FAA / US ground stop leads the page with a big
flat-vector airport dusk scene (grounded airliner, control tower, GROUND
STOP board); the night tanker scene moves to story 02's banner. Header
advertises "24 VERIFIED STORIES - 6 CONTINENTS"; a "WHERE IT HAPPENED"
world map pins 7 stories; 24 numbered stories cover Friday 13 November
2026 (1 lead + 12 grid + 11 ALSO TODAY). Grid visuals are bigger than
round 2 (48px scene banners, 56px icons). The image is drawn by
../news-image-01-build/render_r3.py (PIL, kept out of this repo) and
copied here as entry.png; this program only copies it to the output path.
"""
import os
import shutil


def main():
    os.makedirs("/output", exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    shutil.copy(src, "/output/entry.png")


if __name__ == "__main__":
    main()
