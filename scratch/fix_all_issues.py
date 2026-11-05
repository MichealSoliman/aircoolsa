import os
import re
import json

# =========================================================================
# 1. FIX INDEX.HTML (Overflow, Nav Spacing, Floating Badges)
# =========================================================================
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Add overflow-x-hidden to html and body
index_html = index_html.replace(
    '<html lang="ar" dir="rtl" class="scroll-smooth">',
    '<html lang="ar" dir="rtl" class="scroll-smooth overflow-x-hidden">'
)
index_html = index_html.replace(
    '<body class="bg-brand-light text-brand-dark min-h-screen flex flex-col antialiased selection:bg-brand-cyan selection:text-brand-dark pb-20 lg:pb-0">',
    '<body class="bg-brand-light text-brand-dark min-h-screen flex flex-col antialiased selection:bg-brand-cyan selection:text-brand-dark pb-20 lg:pb-0 overflow-x-hidden">'
)

# Add overflow-hidden to #hero
index_html = index_html.replace(
    '<section id="hero" class="relative pt-8 pb-16 lg:pt-16 lg:pb-24 bg-gradient-to-b from-brand-light to-white border-b border-slate-100">',
    '<section id="hero" class="relative pt-8 pb-16 lg:pt-16 lg:pb-24 bg-gradient-to-b from-brand-light to-white border-b border-slate-100 overflow-hidden">'
)

# Nav links padding to guarantee spacing
old_nav_links = '''        <nav class="hidden lg:flex items-center gap-5 xl:gap-8 text-sm font-bold text-slate-700"
          aria-label="روابط الموقع الرئيسية">
          <a href="/" class="text-brand-blue border-b-2 border-brand-blue py-1 transition-colors whitespace-nowrap">الرئيسية</a>
          <a href="/services/" class="hover:text-brand-blue py-1 transition-colors whitespace-nowrap">خدماتنا</a>
          <a href="#pricing-guide" class="hover:text-brand-blue py-1 transition-colors whitespace-nowrap">الأسعار</a>
          <a href="#districts-coverage" class="hover:text-brand-blue py-1 transition-colors whitespace-nowrap">أحياء جدة</a>
          <a href="/about/" class="hover:text-brand-blue py-1 transition-colors whitespace-nowrap">من نحن</a>
          <a href="/blog/" class="hover:text-brand-blue py-1 transition-colors whitespace-nowrap">المدونة والنصائح</a>
          <a href="/contact/" class="hover:text-brand-blue py-1 transition-colors whitespace-nowrap">تواصل معنا</a>
        </nav>'''

new_nav_links = '''        <nav class="hidden lg:flex items-center gap-2 xl:gap-4 text-sm font-bold text-slate-700"
          aria-label="روابط الموقع الرئيسية">
          <a href="/" class="text-brand-blue border-b-2 border-brand-blue px-3 py-1 transition-colors whitespace-nowrap">الرئيسية</a>
          <a href="/services/" class="hover:text-brand-blue px-3 py-1 transition-colors whitespace-nowrap">خدماتنا</a>
          <a href="#pricing-guide" class="hover:text-brand-blue px-3 py-1 transition-colors whitespace-nowrap">الأسعار</a>
          <a href="#districts-coverage" class="hover:text-brand-blue px-3 py-1 transition-colors whitespace-nowrap">أحياء جدة</a>
          <a href="/about/" class="hover:text-brand-blue px-3 py-1 transition-colors whitespace-nowrap">من نحن</a>
          <a href="/blog/" class="hover:text-brand-blue px-3 py-1 transition-colors whitespace-nowrap">المدونة والنصائح</a>
          <a href="/contact/" class="hover:text-brand-blue px-3 py-1 transition-colors whitespace-nowrap">تواصل معنا</a>
        </nav>'''

if old_nav_links in index_html:
    index_html = index_html.replace(old_nav_links, new_nav_links)
    print('Updated nav links in index.html')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
print('Saved updated index.html')

# =========================================================================
# 2. FIX AC-CLEANING-JEDDAH/INDEX.HTML (Ensure overflow-x-hidden & nav spacing)
# =========================================================================
with open('ac-cleaning-jeddah/index.html', 'r', encoding='utf-8') as f:
    cleaning_html = f.read()

cleaning_html = cleaning_html.replace(
    '<html lang="ar" dir="rtl" class="scroll-smooth">',
    '<html lang="ar" dir="rtl" class="scroll-smooth overflow-x-hidden">'
)
cleaning_html = cleaning_html.replace(
    '<body class="bg-brand-light text-brand-dark min-h-screen flex flex-col antialiased selection:bg-brand-cyan selection:text-brand-dark pb-20 lg:pb-0">',
    '<body class="bg-brand-light text-brand-dark min-h-screen flex flex-col antialiased selection:bg-brand-cyan selection:text-brand-dark pb-20 lg:pb-0 overflow-x-hidden">'
)
cleaning_html = cleaning_html.replace(
    '<nav class="hidden lg:flex items-center gap-5 xl:gap-8 text-sm font-bold text-slate-700"',
    '<nav class="hidden lg:flex items-center gap-2 xl:gap-4 text-sm font-bold text-slate-700"'
)

with open('ac-cleaning-jeddah/index.html', 'w', encoding='utf-8') as f:
    f.write(cleaning_html)
print('Saved updated ac-cleaning-jeddah/index.html')

# =========================================================================
# 3. FIX OTHER SERVICE & GENERAL PAGES (Schema, og:type, links, forbidden text)
# =========================================================================
pages_to_clean = [
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

def clean_schema_json(match):
    raw_json = match.group(1)
    try:
        data = json.loads(raw_json)
        
        def filter_node(node):
            if isinstance(node, dict):
                node.pop('aggregateRating', None)
                node.pop('Review', None)
                node.pop('ratingValue', None)
                node.pop('reviewCount', None)
                for k, v in list(node.items()):
                    node[k] = filter_node(v)
            elif isinstance(node, list):
                node = [filter_node(item) for item in node]
            return node

        cleaned = filter_node(data)
        return '<script type="application/ld+json">\n' + json.dumps(cleaned, ensure_ascii=False, indent=2) + '\n  </script>'
    except Exception as e:
        print('Schema JSON parse error:', e)
        return match.group(0)

for page in pages_to_clean:
    if not os.path.exists(page):
        continue
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Clean schema
    content = re.sub(r'<script type="application/ld\+json">(.*?)</script>', clean_schema_json, content, flags=re.DOTALL)

    # 2. og:type
    content = content.replace('content="service"', 'content="website"')

    # 3. /index.html links
    content = content.replace('href="/index.html"', 'href="/"')
    content = content.replace('href="index.html"', 'href="/"')

    # 4. Dummy contact numbers
    content = content.replace('+966 50\n                000 0000', '+966 53 355 3620')
    content = content.replace('+966 50 000 0000', '+966 53 355 3620')
    content = content.replace('000 0000', '0533553620')

    # 5. Forbidden phrases
    content = content.replace('سرعة وصول الفني: خلال 30 - 60 دقيقة', 'مواعيد دقيقة حسب جدول الحجز المسبق')
    content = content.replace('خلال 30 - 60 دقيقة', 'حسب الموعد المحدد مسبقاً')
    content = content.replace('30 - 60 دقيقة', 'الموعد المحدد مسبقاً')
    content = content.replace('تنتشر فرق عمل إير كول الميدانية وسيارات الخدمة المجهزة في جميع قطاعات محافظة جدة لتقديم خدمة سريعة بدون تأخير.', 'يقدم فنيو إير كول خدمات التكييف في مختلف قطاعات وأحياء جدة بكفاءة وجودة عالية.')
    content = content.replace('سيارات الخدمة المجهزة', 'المعدات المتخصصة')
    content = content.replace('تنتشر فرق', 'يعمل فنيو')
    content = content.replace('ضمان فوري', 'ضمان معتمد')
    content = content.replace('لا إطلاقاً', 'نحرص تماماً')
    content = content.replace('ألمانية', 'معتمدة')

    # 6. Ensure overflow-x-hidden on html and body
    if 'overflow-x-hidden' not in content:
        content = content.replace('<html lang="ar" dir="rtl"', '<html lang="ar" dir="rtl" class="overflow-x-hidden"')
        content = content.replace('<body class="', '<body class="overflow-x-hidden ')

    with open(page, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully updated: {page}')

print('\nALL TEMPLATE UPDATES COMPLETE.')

