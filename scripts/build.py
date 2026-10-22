"""Build an allowlisted static site without publishing repository metadata."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist"
if OUTPUT.is_symlink():
    raise SystemExit("Refusing to replace a symlinked output directory")
if OUTPUT.exists():
    shutil.rmtree(OUTPUT)
OUTPUT.mkdir()
for name in ("index.html", "_headers", "robots.txt", "sitemap.xml"):
    shutil.copy2(ROOT / name, OUTPUT / name)
shutil.copytree(ROOT / "assets", OUTPUT / "assets")
print("Built static site in", OUTPUT)
