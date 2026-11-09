import os, re, json

ARTICLES = [
    ('choosing-ac-company-jeddah', 'blog/choosing-ac-company-jeddah/index.html'),
    ('ac-cleaning-guide-jeddah', 'blog/ac-cleaning-guide-jeddah/index.html'),
    ('ac-maintenance-guide-jeddah', 'blog/ac-maintenance-guide-jeddah/index.html'),
    ('ac-gas-refilling-guide-jeddah', 'blog/ac-gas-refilling-guide-jeddah/index.html'),
    ('ac-copper-piping-guide-jeddah', 'blog/ac-copper-piping-guide-jeddah/index.html'),
]

for name, path in ARTICLES:
    txt = open(path, encoding='utf-8').read()
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', txt, re.DOTALL)
    h1_text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', h1.group(1))).strip() if h1 else None
    
    # search date in text
    date_match = re.findall(r'(\d{1,2}\s+[^\s\d]+\s+202\d|202\d-\d{2}-\d{2}|تحديث:[^<]+)', txt)
    
    # image
    img_match = re.findall(r'<meta property="og:image" content="([^"]+)"', txt)
    
    # json-ld
    scripts = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"]>(.*?)</script>', txt, re.DOTALL)
    
    print(f"=== {name} ===")
    print(f"  H1: {h1_text}")
    print(f"  Dates found in page: {date_match}")
    print(f"  OG Image: {img_match}")
    for s in scripts:
        print(f"  Script: {s.strip()[:200]}...")

