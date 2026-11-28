#!/usr/bin/env python3
"""Build Film Lab from src/index.template.html.

    python3 build.py               -> index.html  (fonts linked from ./fonts/, committed)
    python3 build.py --standalone  -> dist/film-lab.html  (fonts embedded, NOT committed)

The ABC Areal fonts are licensed (Dinamo) and are never committed. Put
ABCAreal-Regular.woff2, ABCAreal-Medium.woff2 and ABCArealMono-Regular.woff2
in ./fonts/ to use them; without them the page falls back to system fonts.
The sample photo and page background in ./assets/ are embedded so the page works when opened from disk.
"""
import base64
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
FONTS = [
    ("ABC Areal", "ABCAreal-Regular.woff2", 400),
    ("ABC Areal", "ABCAreal-Medium.woff2", 500),
    ("ABC Areal Mono", "ABCArealMono-Regular.woff2", 400),
]


def font_face(family, filename, weight, embed):
    if embed:
        path = ROOT / "fonts" / filename
        if not path.exists():
            sys.exit(f"Missing fonts/{filename} (needed for --standalone)")
        src = "data:font/woff2;base64," + base64.b64encode(path.read_bytes()).decode()
    else:
        src = "fonts/" + filename
    return (f'@font-face{{font-family:"{family}";src:url("{src}") format("woff2");'
            f'font-weight:{weight};font-style:normal;font-display:swap}}')


def main():
    standalone = "--standalone" in sys.argv
    template = (ROOT / "src" / "index.template.html").read_text()
    fonts = "\n".join(font_face(f, n, w, standalone) for f, n, w in FONTS)
    sample = "data:image/jpeg;base64," + base64.b64encode((ROOT / "assets" / "pnw_pond.jpg").read_bytes()).decode()
    bg = "data:image/jpeg;base64," + base64.b64encode((ROOT / "assets" / "background.jpg").read_bytes()).decode()
    html = template.replace("%%FONTS%%", fonts).replace("%%SAMPLE%%", sample).replace("%%BG%%", bg)
    out = ROOT / ("dist/film-lab.html" if standalone else "index.html")
    out.parent.mkdir(exist_ok=True)
    out.write_text(html)
    print(f"wrote {out.relative_to(ROOT)} ({len(html) / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
