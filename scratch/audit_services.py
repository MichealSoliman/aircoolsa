# -*- coding: utf-8 -*-
import os

search_terms = [
    'aggregateRating',
    'reviewCount',
    '/index.html',
    'og:type" content="service"',
    'ألمانية',
    '30 - 60',
    '000 0000',
    'لا إطلاقاً',
    'حصرية',
    'ضمان فوري',
    'سيارات الخدمة',
    'تنتشر فرق'
]

for root, dirs, files in os.walk('.'):
    if any(skip in root for skip in ['node_modules', '.git', 'scratch']):
        continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, encoding='utf-8') as fh:
                content = fh.read()
            found = [t for t in search_terms if t in content]
            if found:
                print(f'{p}: found {found}')

