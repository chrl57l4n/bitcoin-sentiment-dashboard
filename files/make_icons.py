import os
from PIL import Image, ImageDraw

sizes = {
    "mipmap-mdpi":    48,
    "mipmap-hdpi":    72,
    "mipmap-xhdpi":   96,
    "mipmap-xxhdpi":  144,
    "mipmap-xxxhdpi": 192,
}

for folder, size in sizes.items():
    out = f"app/src/main/res/{folder}"
    os.makedirs(out, exist_ok=True)
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse([0, 0, size - 1, size - 1], fill=(247, 147, 26, 255))
    pad = size // 4
    d.ellipse([pad, pad, size - pad - 1, size - pad - 1], fill=(26, 8, 0, 255))
    img.save(f"{out}/ic_launcher.png")
    img.save(f"{out}/ic_launcher_round.png")
    print(f"Created {out}/ic_launcher.png ({size}x{size})")
