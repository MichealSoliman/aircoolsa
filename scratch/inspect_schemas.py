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
    scripts = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"]>(.*?)</script>', txt, re.DOTALL)
    print(f"==================== {name} ({len(scripts)} scripts) ====================")
    for idx, s in enumerate(scripts):
        try:
            d = json.loads(s.strip())
            print(f"Script {idx+1}:")
            # print top level keys and types
            if isinstance(d, dict) and '@graph' in d:
                for g_idx, item in enumerate(d['@graph']):
                    print(f"  Graph[{g_idx}] @type: {item.get('@type')}, @id: {item.get('@id')}")
                    if item.get('@type') == 'Service':
                        print("    serviceType:", item.get('serviceType'))
                        print("    provider:", item.get('provider'))
                        print("    offers:", item.get('offers'))
                    if item.get('@type') == 'Article':
                        print("    headline:", item.get('headline'))
                        print("    author:", item.get('author'))
                        print("    publisher:", item.get('publisher'))
                        print("    datePublished:", item.get('datePublished'))
                        print("    dateModified:", item.get('dateModified'))
            else:
                t = d.get('@type') if isinstance(d, dict) else [x.get('@type') for x in d]
                print(f"  Single @type: {t}, @id: {d.get('@id') if isinstance(d, dict) else None}")
                if isinstance(d, dict) and d.get('@type') == 'Article':
                    print("    headline:", d.get('headline'))
                    print("    author:", d.get('author'))
                    print("    publisher:", d.get('publisher'))
                    print("    datePublished:", d.get('datePublished'))
                    print("    dateModified:", d.get('dateModified'))
        except Exception as e:
            print(f"Script {idx+1} Error: {e}")

