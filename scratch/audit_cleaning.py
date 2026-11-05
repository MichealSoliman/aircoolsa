import json
import re

with open('ac-cleaning-jeddah/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

errors = []

# 1. H1 check
h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
if len(h1s) != 1:
    errors.append(f'Expected 1 H1, found {len(h1s)}')
else:
    print('H1 found:', re.sub(r'\s+', ' ', h1s[0]).strip())

# 2. Schema check
schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
if not schemas:
    errors.append('No JSON-LD schemas found')
else:
    for i, s in enumerate(schemas):
        try:
            data = json.loads(s)
            graph = data.get('@graph', [])
            types = [x.get('@type') for x in graph]
            print(f'Schema valid JSON-LD @graph types: {types}')
            # Check forbidden schema fields
            s_str = json.dumps(data)
            for bad in ['aggregateRating', 'Review', 'ratingValue', 'reviewCount']:
                if bad in s_str:
                    errors.append(f'Forbidden schema field found: {bad}')
        except Exception as e:
            errors.append(f'Schema {i+1} JSON parse error: {e}')

# 3. Forbidden phrases
forbidden = [
    'ألمانية', 'حيوية', '20%', '80%', 'لا إطلاقاً', 'دون تطاير قطرة',
    'عروض حصرية', 'عرض خاص', 'ضمان فوري', '30 - 60', 'سيارات الخدمة المجهزة',
    'تنتشر فرق', 'الأكثر طلباً', 'فحص الفريون مجاناً', 'بدون أي تكاليف خفية',
    'بدون أي رسوم', 'الأصلي', 'الأمريكي', 'مولر كوري', 'ميزان الليزر',
    'الرائدة', 'الورش العشوائية', 'خبرة موثقة', 'لن تدفع ريالاً'
]
for p in forbidden:
    if p in html:
        errors.append(f'Forbidden phrase found: {p}')

# 4. Check for [TO_CONFIRM] in visitor visible HTML
body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
if body_match:
    body = body_match.group(1)
    body_no_comments = re.sub(r'<!--.*?-->', '', body, flags=re.DOTALL)
    if '[TO_CONFIRM' in body_no_comments:
        errors.append('Found [TO_CONFIRM] in visible body HTML')

# 5. Canonical check
if '<link rel="canonical" href="https://aircoolsa.com/ac-cleaning-jeddah/">' not in html:
    errors.append('Canonical tag mismatch or missing')

# 6. og:type
if '<meta property="og:type" content="website">' not in html:
    errors.append('og:type is not website')

# 7. No /index.html links
index_links = re.findall(r'href=["\'](/index\.html|index\.html)["\']', html)
if index_links:
    errors.append(f'Found /index.html links: {index_links}')

# 8. Check phone numbers: only 0533553620 / +966533553620
phones = re.findall(r'05\d{8}', html)
for ph in set(phones):
    if ph != '0533553620':
        errors.append(f'Unknown phone found: {ph}')

# 9. FAQ consistency between Schema and HTML
faq_schema = None
for s in schemas:
    try:
        data = json.loads(s)
        for node in data.get('@graph', []):
            if node.get('@type') == 'FAQPage':
                faq_schema = node
    except Exception:
        pass

if not faq_schema:
    errors.append('FAQPage node not found in schema graph')
else:
    faq_items = faq_schema.get('mainEntity', [])
    print(f'Found {len(faq_items)} FAQ items in Schema.')
    for idx, item in enumerate(faq_items):
        q = item.get('name', '').strip()
        a = item.get('acceptedAnswer', {}).get('text', '').strip()
        if q not in html:
            errors.append(f'FAQ Question {idx+1} not found in HTML text: {q[:40]}...')
        if a not in html:
            errors.append(f'FAQ Answer {idx+1} not found in HTML text: {a[:40]}...')

if errors:
    print('ERRORS FOUND:')
    for err in errors:
        print('-', err)
else:
    print('SUCCESS: ALL AUDIT CHECKS PASSED!')

