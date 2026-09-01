"""Shrink everything in assets/ for the web. Run after dropping in big photos.

    python _optimize_images.py

Overwrites in place and re-compresses, so keep your originals somewhere else.
"""
import pathlib
from PIL import Image

A = pathlib.Path(__file__).parent / "assets"
CAPS = {"logo.png": 1200, "hero-figure.jpg": 1800}   # per-file overrides
PRODUCT_MAX = 850                                    # prod-*.png cutouts
DEFAULT_MAX = 1600

for p in sorted(A.glob("*")):
    if p.suffix.lower() not in (".jpg", ".jpeg", ".png"):
        continue
    im = Image.open(p)
    w, h = im.size
    cap = CAPS.get(p.name, PRODUCT_MAX if p.name.startswith("prod-") else DEFAULT_MAX)
    if w > cap:
        im = im.resize((cap, round(h * cap / w)), Image.LANCZOS)
    before = p.stat().st_size
    if p.suffix.lower() in (".jpg", ".jpeg"):
        im.convert("RGB").save(p, "JPEG", quality=80, optimize=True, progressive=True)
    else:
        # keep the alpha channel — the cutouts depend on it
        im.save(p, "PNG", optimize=True)
    print(f"{p.name:26} {before // 1024:5} KB -> {p.stat().st_size // 1024:5} KB")
