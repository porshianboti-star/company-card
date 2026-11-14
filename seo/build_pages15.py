#!/usr/bin/env python3
"""Batch 15 builder — renders hihello-vs-blinq.html. Run from repo root."""
import os, sys
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
# OVERWRITE-LIVE-GUARD-2026-11-14: the live hihello-vs-blinq.html is the source of truth; this renderer's template
# (nav, footer, Organization/WebSite JSON-LD) is older than the live page.
if "--overwrite-live" not in sys.argv:
    sys.exit("refusing to overwrite hihello-vs-blinq.html: the live HTML is the source of truth. "
             "Render into a scratch copy (build_pages.ROOT) and diff, or pass --overwrite-live.")
from build_pages import write_pages
from pages_data15 import PAGES
for s in write_pages(PAGES):
    print("wrote " + s)
