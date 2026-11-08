#!/usr/bin/env python3
"""Empacota ZIPs de distribuição sem dependências externas.

Execute da raiz: python scripts/package_release.py
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist"
OUT.mkdir(exist_ok=True)
SKILL = ROOT / "skills" / "marketplace-pro"


def pack(zip_path, files, relative_to, prefix=""):
    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as archive:
        for p in sorted(files):
            archive.write(p, prefix + p.relative_to(relative_to).as_posix())
    print(f"{zip_path.name}: {zip_path.stat().st_size:,} bytes")


skill_files = [p for p in SKILL.rglob("*") if p.is_file() and "__pycache__" not in p.parts]
pack(OUT / "marketplace-pro-skill.zip", skill_files, SKILL)
plugin_files = [ROOT / "plugin.json", ROOT / "LICENSE"]
plugin_files += [p for folder in [ROOT / "skills", ROOT / "assets"] for p in folder.rglob("*") if p.is_file()]
pack(OUT / "marketplace-pro-plugin.zip", plugin_files, ROOT)
repo_files = [p for p in ROOT.rglob("*") if p.is_file() and not any(part in {"dist", "__pycache__", ".git"} for part in p.relative_to(ROOT).parts)]
pack(OUT / "marketplace-pro-github.zip", repo_files, ROOT, prefix="marketplace-pro/")
