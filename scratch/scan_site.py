import os
import re

files_to_check = [
    'ac-maintenance-jeddah/index.html',
    'ac-installation-jeddah/index.html',
    'ac-gas-refilling-jeddah/index.html',
    'ac-copper-piping-jeddah/index.html',
    'ac-sanitization-jeddah/index.html',
    'best-ac-company-jeddah/index.html',
    'services/index.html',
    'contact/index.html',
    'about/index.html',
    'blog/index.html'
]

forbidden = [
    'aggregateRating', 'reviewCount', 'ratingValue',
    'og:type" content="service"',
    'href="/index.html"', 'href="index.html"',
    '000 0000', '0000000',
    '30 - 60', 'سيارات الخدمة المجهزة', 'تنتشر فرق', 'ألمانية', 'ضمان فوري', 'لا إطلاقاً'
]

results = {}

for rel_path in files_to_check:
    if not os.path.exists(rel_path):
        continue
    with open(rel_path, 'r', encoding='utf-8') as f:
        content = f.read()
    found = []
    for item in forbidden:
        if item in content:
            found.append(item)
    if found:
        results[rel_path] = found

print('SCAN RESULTS:')
for p, issues in results.items():
    print(f'{p}: {issues}')

