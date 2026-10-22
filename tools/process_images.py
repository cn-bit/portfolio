"""Crop and compress project images for the portfolio site.

Every image is cropped to one of a few fixed shapes so that images shown
side by side always match in size. Run from the repository root:

    python3 tools/process_images.py

Originals live in _originals/ and are never changed.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "_originals"
OUT = ROOT / "assets" / "img"

# Shape name: (width ratio, height ratio, full-size width)
SHAPES = {
    "pano": (2, 1, 2400),    # full-width banners
    "wide": (3, 2, 2400),    # full-width or paired landscape
    "tall": (4, 5, 1440),    # paired portraits
    "square": (1, 1, 1440),  # paired squares
    "tile": (2, 3, 1000),    # brand tiles in a row
}

# (source file, project, output name, shape, focal x, focal y)
JOBS = [
    # Byron Bay Bone Broth
    ("banner-2.webp", "byron-bay-bone-broth", "jar-hinterland", "pano", 0.45, 0.5),
    ("banner-1.webp", "byron-bay-bone-broth", "website-hero", "pano", 0.6, 0.5),
    ("naturopath-byron-bay.webp", "byron-bay-bone-broth", "practitioner", "tall", 0.5, 0.4),
    ("Capsules.webp", "byron-bay-bone-broth", "capsules", "tall", 0.5, 0.5),
    ("IMG_4285_1600x_c89d1cf9-d07c-4eef-88be-30be2b1cd34e.webp", "byron-bay-bone-broth", "retail-jars", "wide", 0.5, 0.5),
    ("byronbaybonebroth_1555401709_2023178637143873591_3107678858.webp", "byron-bay-bone-broth", "production", "wide", 0.5, 0.5),
    ("byronbaybonebroth_1641703933_2747134161065591576_3107678858.jpg", "byron-bay-bone-broth", "farm", "wide", 0.5, 0.5),
    ("banner-4.webp", "byron-bay-bone-broth", "pouch", "wide", 0.72, 0.5),
    # Elly Sofocli
    ("69ccbcab2e2d3e82695beff8_Phia.jpg", "elly-sofocli", "trunk-show", "wide", 0.5, 0.5),
    ("65179c63a320198b8409549d_DSC02607 5.jpg", "elly-sofocli", "studio-mono", "tall", 0.5, 0.45),
    ("65c2702c7f540ff5566f276c_231006_Elly Sofocli_SH02_0258.webp", "elly-sofocli", "corset", "tall", 0.5, 0.5),
    # RT Edgar
    ("rte-monogram-fireplace.png", "rt-edgar", "monogram-fireplace", "tall", 0.5, 0.5),
    ("Free-iPhone-16-Pro-Laying-on-Floor-Mockup.jpg", "rt-edgar", "website-agent", "wide", 0.5, 0.5),
    ("iPhone-Static.jpg", "rt-edgar", "website-home", "wide", 0.5, 0.5),
    ("Light-Blue-Cover.jpg", "rt-edgar", "brochure-blue", "wide", 0.5, 0.5),
    ("Navy-Cover.jpg", "rt-edgar", "brochure-navy", "wide", 0.5, 0.5),
    ("Spread 08.png", "rt-edgar", "spread-feature", "wide", 0.5, 0.5),
    ("Spread-03.png", "rt-edgar", "spread-details", "wide", 0.5, 0.5),
    ("Brick Wall.jpg", "rt-edgar", "board-street", "wide", 0.5, 0.5),
    ("Open-home-01.jpg", "rt-edgar", "open-home-navy", "tile", 0.5, 0.5),
    ("Layer-1.jpg", "rt-edgar", "open-home-blue", "tile", 0.5, 0.5),
    ("Bush 01.jpg", "rt-edgar", "board-garden", "tall", 0.46, 0.5),
    ("MM_UrbanPoster_UP-SUM1-02.jpg", "rt-edgar", "board-kellor", "tall", 0.5, 0.5),
    ("es-embossed-stationery.jpg", "elly-sofocli", "stationery", "tall", 0.56, 0.5),
    ("es-garment-bag-ribbon.jpg", "elly-sofocli", "garment-bag", "tall", 0.5, 0.5),
    ("es-velvet-hanger.jpg", "elly-sofocli", "hanger", "tall", 0.5, 0.5),
    ("es-studio-interior.jpg", "elly-sofocli", "studio", "tall", 0.5, 0.5),
    ("es-gown-on-rail.jpg", "elly-sofocli", "gown-on-rail", "tall", 0.5, 0.5),
    ("Dark Blue Sign 02.jpg", "rt-edgar", "sign-hanging", "wide", 0.5, 0.5),
    ("Tramstop 02 (1).jpg", "rt-edgar", "tram-stop", "wide", 0.5, 0.5),
    ("Navy Stand.jpg", "rt-edgar", "stand-navy", "wide", 0.5, 0.5),
    ("Website_Homepage_Banner_-_Desktop_62fc417a-c01b-434f-b2ef-92d93b64a3a7.webp", "femme-connection", "garden", "pano", 0.5, 0.5),
    ("Website_-_Homepage_2_tiles_1_2c39e662-732c-4fa2-9e0a-b44fdd674f4d.webp", "femme-connection", "vacation", "tall", 0.5, 0.35),
    ("Website_-_Homepage_2_tiles_0f104e6b-39e8-473a-babf-297f597042e4.webp", "femme-connection", "spring", "tall", 0.5, 0.4),
    ("Website_-_Homepage_2_tiles_3_8a10a25c-cc8e-4034-9073-4e6db2e5c891.webp", "femme-connection", "beach", "tall", 0.5, 0.35),
    ("Website_-_Homepage_2_tiles_2_b4981f2a-463d-493b-938e-d5b97f6b6adf.webp", "femme-connection", "trousers", "tall", 0.5, 0.45),
    ("6517ac3d456364205ca7d0fd_estelle (2) 1.jpg", "elly-sofocli", "off-shoulder", "tall", 0.5, 0.5),
    ("banner-3.webp", "byron-bay-bone-broth", "capsules-hero", "pano", 0.5, 0.5),
    # Femme Connection
    ("1_3f4432b3-ddfd-4e85-98c0-6f38406be284.webp", "femme-connection", "tile-f", "tile", 0.5, 0.5),
    ("4_929c41e4-2c4b-4212-a1d8-858b6fafd819.webp", "femme-connection", "tile-c", "tile", 0.5, 0.5),
    ("10_ca451375-0431-4147-a327-0d5c1f66d1b3.webp", "femme-connection", "tile-heart", "tile", 0.5, 0.5),
    ("7_345a0a05-26d4-467b-ab4a-f709277741e2.webp", "femme-connection", "tile-star", "tile", 0.5, 0.5),
    ("13_936152af-9930-4c13-a04d-adbdf7ef5201.webp", "femme-connection", "tile-check", "tile", 0.5, 0.5),
    ("3_3f4ad2b9-8294-4f9b-b0a8-9874cd2d19aa.webp", "femme-connection", "tile-pink", "tile", 0.5, 0.5),
    ("New_Arrivals_1_2a6f0254-eb03-468f-bc5c-3d1b3a8bbddf.webp", "femme-connection", "occasion", "square", 0.5, 0.5),
    ("New_Arrivals_4.webp", "femme-connection", "everyday", "square", 0.55, 0.5),
]


def crop_to(im, rw, rh, fx, fy):
    w, h = im.size
    target = rw / rh
    if w / h > target:  # too wide: trim the sides
        cw, ch = round(h * target), h
    else:               # too tall: trim top and bottom
        cw, ch = w, round(w / target)
    left = min(max(round(fx * w - cw / 2), 0), w - cw)
    top = min(max(round(fy * h - ch / 2), 0), h - ch)
    return im.crop((left, top, left + cw, top + ch))


def save(im, path, max_w):
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    im.save(path, "JPEG", quality=80, optimize=True, progressive=True)
    return im.size


def main():
    for src, project, name, shape, fx, fy in JOBS:
        im = Image.open(SRC / src).convert("RGB")
        if shape:
            rw, rh, full = SHAPES[shape]
            im = crop_to(im, rw, rh, fx, fy)
        else:
            full = 1600
        out = OUT / project
        out.mkdir(parents=True, exist_ok=True)
        size = save(im, out / f"{name}.jpg", full)
        save(im, out / f"{name}-800.jpg", 800)
        print(f"{project}/{name}.jpg {size[0]}x{size[1]}")


if __name__ == "__main__":
    main()
