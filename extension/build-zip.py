#!/usr/bin/env python3
"""Build the Chrome Web Store zip for the CompanyCard extension.
Run from anywhere: python3 extension/build-zip.py"""
import json
import pathlib
import zipfile

EXT = pathlib.Path(__file__).resolve().parent
FILES = ["manifest.json", "background.js", "content.js", "cc-core.js",
         "popup.html", "popup.css", "popup.js", "vendor/qrcode.min.js",
         "icon16.png", "icon32.png", "icon48.png", "icon128.png"]

out = EXT / "companycard-extension-store.zip"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for name in FILES:
        z.write(EXT / name, name)

version = json.loads((EXT / "manifest.json").read_text())["version"]
print(f"version {version} -> {out.name} ({out.stat().st_size} bytes)")
