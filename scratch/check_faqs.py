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
    # Check if page has FAQPage schema
    has_faq_schema = 'FAQPage' in txt
    
    # Check if page has visible FAQ section or questions
    has_visible_faq = 'الأسئلة الشائعة' in txt or '<details' in txt
    
    # Count questions in schema
    q_count = len(re.findall(r'"@type":\s*"Question"', txt))
    
    print(f"{name:35} | Schema FAQ: {str(has_faq_schema):5} ({q_count} Qs) | Visible FAQ: {str(has_visible_faq):5}")

