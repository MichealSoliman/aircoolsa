import re

pages = [
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

print("| الصفحة | Canonical | Title (الأحرف) | Description (الأحرف) |")
print("| :--- | :--- | :--- | :--- |")

for name, path in pages:
    txt = open(path, encoding='utf-8').read()
    
    can = re.search(r'<link rel="canonical" href="([^"]+)"', txt)
    can_val = can.group(1) if can else "NOT FOUND"
    
    t = re.search(r'<title>(.*?)</title>', txt, re.DOTALL)
    title_val = t.group(1).strip() if t else ""
    
    d = re.search(r'<meta name="description"\s+content="([^"]*)"', txt, re.DOTALL)
    desc_val = d.group(1).strip() if d else ""
    
    print(f"| {name} | `{can_val}` | {len(title_val)} حرف (`{title_val}`) | {len(desc_val)} حرف (`{desc_val}`) |")

