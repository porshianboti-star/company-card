#!/usr/bin/env python3
"""Batch 24 builder — renders digital-business-card-for-bookkeepers.html. Run from repo root."""
import os, sys
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from build_pages import write_pages
from pages_data22 import PAGES
for s in write_pages(PAGES):
    print("wrote " + s)
