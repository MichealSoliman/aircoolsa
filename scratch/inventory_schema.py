import os
import re
import json

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

inventory = []

for name, filepath in PAGES:
    if not os.path.exists(filepath):
        continue
    content = open(filepath, encoding='utf-8').read()
    
    # Check Microdata or RDFa
    microdata = re.findall(r'itemscope|itemtype|itemprop', content)
    rdfa = re.findall(r'vocab=|typeof=|property=', content)
    
    # Check JSON-LD scripts
    scripts = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"]>(.*?)</script>', content, re.DOTALL)
    
    page_types = []
    errors = []
    
    if microdata:
        errors.append(f"Found Microdata ({len(microdata)} attributes)")
    if rdfa:
        errors.append(f"Found RDFa ({len(rdfa)} attributes)")
        
    for s_idx, s in enumerate(scripts):
        s_clean = s.strip()
        try:
            data = json.loads(s_clean)
            # Inspect types
            if isinstance(data, dict):
                if '@graph' in data:
                    for item in data['@graph']:
                        t = item.get('@type', 'Unknown')
                        page_types.append(t)
                else:
                    t = data.get('@type', 'Unknown')
                    page_types.append(t)
            elif isinstance(data, list):
                for item in data:
                    t = item.get('@type', 'Unknown')
                    page_types.append(t)
        except Exception as e:
            errors.append(f"JSON-LD block {s_idx+1} syntax error: {str(e)}")
            
    inventory.append({
        'name': name,
        'filepath': filepath,
        'types': page_types,
        'errors': errors,
        'raw_scripts_count': len(scripts)
    })

for item in inventory:
    types_str = ", ".join(item['types']) if item['types'] else "لا يوجد"
    err_str = "; ".join(item['errors']) if item['errors'] else "لا توجد أخطاء صريحة في JSON.parse"
    print(f"| {item['name']} | {types_str} | {err_str} |")

