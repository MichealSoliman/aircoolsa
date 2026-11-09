import os, re, json

PAGES = [
    ('الرئيسية (index.html)', 'index.html'),
    ('/services/', 'services/index.html'),
    ('/ac-maintenance-jeddah/', 'ac-maintenance-jeddah/index.html'),
    ('/ac-installation-jeddah/', 'ac-installation-jeddah/index.html'),
    ('/ac-gas-refilling-jeddah/', 'ac-gas-refilling-jeddah/index.html'),
    ('/ac-copper-piping-jeddah/', 'ac-copper-piping-jeddah/index.html'),
    ('/ac-sanitization-jeddah/', 'ac-sanitization-jeddah/index.html'),
    ('/ac-cleaning-jeddah/', 'ac-cleaning-jeddah/index.html'),
    ('/about/', 'about/index.html'),
    ('/contact/', 'contact/index.html'),
    ('/privacy/', 'privacy/index.html'),
    ('/blog/', 'blog/index.html'),
    ('/blog/choosing-ac-company-jeddah/', 'blog/choosing-ac-company-jeddah/index.html'),
    ('/blog/ac-cleaning-guide-jeddah/', 'blog/ac-cleaning-guide-jeddah/index.html'),
    ('/blog/ac-maintenance-guide-jeddah/', 'blog/ac-maintenance-guide-jeddah/index.html'),
    ('/blog/ac-gas-refilling-guide-jeddah/', 'blog/ac-gas-refilling-guide-jeddah/index.html'),
    ('/blog/ac-copper-piping-guide-jeddah/', 'blog/ac-copper-piping-guide-jeddah/index.html'),
]

for name, path in PAGES:
    txt = open(path, encoding='utf-8').read()
    # Find breadcrumb HTML
    bc_html = re.findall(r'<nav[^>]*aria-label=[\'"][^\'"]*تصفح[^\'"]*[\'"][^>]*>.*?</nav>', txt, re.DOTALL)
    # Find breadcrumb schema
    scripts = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"]>(.*?)</script>', txt, re.DOTALL)
    bc_schema = None
    for s in scripts:
        try:
            d = json.loads(s.strip())
            graph = d.get('@graph', [d]) if isinstance(d, dict) else d
            for item in graph:
                if isinstance(item, dict) and item.get('@type') == 'BreadcrumbList':
                    bc_schema = item
        except:
            pass
    print(f"=== {name} ===")
    print(f"  Visible breadcrumb nav found: {len(bc_html) > 0}")
    if bc_html:
        # clean html tags for display
        clean_bc = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', bc_html[0])).strip()
        print(f"  Visible text: {clean_bc}")
    if bc_schema:
        items = bc_schema.get('itemListElement', [])
        print(f"  Schema items: {[(x.get('position'), x.get('name'), x.get('item')) for x in items]}")
    else:
        print("  Schema: NONE")

