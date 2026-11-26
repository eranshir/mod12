"""Generate the PWA icons (a mod-12 dial with the C major triad lit). No dependencies.

Run from the Mod12 folder: python3 make_icons.py
"""
import math
import struct
import zlib

BG, RING, DIM, AMBER, EDGE = (21, 17, 14), (58, 46, 37), (120, 100, 82), (245, 165, 36), (160, 108, 24)


def seg_dist(px, py, a, b):
    (x1, y1), (x2, y2) = a, b
    dx, dy = x2 - x1, y2 - y1
    t = max(0, min(1, ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)))
    return math.hypot(px - x1 - t * dx, py - y1 - t * dy)


def png(n, path):
    c, radius = n / 2, n * 0.30
    dots = []
    for k in range(12):
        a = k * math.pi / 6
        hot = k in (1, 5, 8)  # C, E, G
        dots.append((c + radius * math.sin(a), c - radius * math.cos(a), n * (0.062 if hot else 0.036), AMBER if hot else DIM))
    tri = [(d[0], d[1]) for d in dots if d[3] == AMBER]
    rows = []
    for y in range(n):
        row = bytearray(b"\x00")
        for x in range(n):
            col = BG
            if abs(math.hypot(x - c, y - c) - radius) < n * 0.004:
                col = RING
            if min(seg_dist(x, y, tri[i], tri[(i + 1) % 3]) for i in range(3)) < n * 0.008:
                col = EDGE
            for dx, dy, r, colour in dots:
                if math.hypot(x - dx, y - dy) < r:
                    col = colour
            row += bytes(col)
        rows.append(bytes(row))

    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", n, n, 8, 2, 0, 0, 0))
                + chunk(b"IDAT", zlib.compress(b"".join(rows), 9)) + chunk(b"IEND", b""))


for size, name in ((192, "icon-192.png"), (512, "icon-512.png"), (180, "apple-touch-icon.png")):
    png(size, name)
    print("wrote", name)
