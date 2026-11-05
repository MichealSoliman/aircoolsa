# -*- coding: utf-8 -*-
import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

imgs = re.findall(r'<img[^>]+>', html)
print(f'Total img tags: {len(imgs)}')
for img in imgs:
    alt = re.search(r'alt="([^"]*)"', img)
    w = re.search(r'width="([^"]*)"', img)
    h = re.search(r'height="([^"]*)"', img)
    src = re.search(r'src="([^"]*)"', img)
    alt_val = alt.group(1) if alt else "MISSING"
    w_val = w.group(1) if w else "MISSING"
    h_val = h.group(1) if h else "MISSING"
    src_val = src.group(1) if src else "N/A"
    print(f"SRC: {src_val} | W: {w_val} | H: {h_val} | ALT: {alt_val}")

