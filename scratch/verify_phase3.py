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

all_valid = True
results = []

for name, path in PAGES:
    txt = open(path, encoding='utf-8').read()
    scripts = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"]>(.*?)</script>', txt, re.DOTALL)
    
    defined_ids = set()
    duplicate_definitions = []
    types_found = []
    errors = []
    
    for idx, s in enumerate(scripts):
        try:
            d = json.loads(s.strip())
            
            def inspect_definitions(node):
                if isinstance(node, dict):
                    if '@type' in node:
                        types_found.append(node['@type'])
                        if '@id' in node:
                            node_id = node['@id']
                            if node_id in defined_ids:
                                duplicate_definitions.append(node_id)
                            defined_ids.add(node_id)
                    for k, v in node.items():
                        inspect_definitions(v)
                elif isinstance(node, list):
                    for item in node:
                        inspect_definitions(item)
            
            inspect_definitions(d)
        except Exception as e:
            errors.append(f"Script {idx+1} invalid JSON: {str(e)}")
            all_valid = False
            
    if duplicate_definitions:
        errors.append(f"Duplicate defined @id: {duplicate_definitions}")
        all_valid = False
        
    results.append({
        'name': name,
        'types': types_found,
        'errors': errors
    })

print("| الصفحة | الكيانات المعرفة (Entities) | حالة التحقق |")
print("| :--- | :--- | :--- |")
for r in results:
    t_str = ", ".join(dict.fromkeys(r['types'])) if r['types'] else "لا يوجد"
    e_str = "سليم 100% (JSON Valid & No duplicate entities)" if not r['errors'] else f"خطأ: {'; '.join(r['errors'])}"
    print(f"| {r['name']} | {t_str} | {e_str} |")

print("\nOverall Status:", "SUCCESS - All Valid!" if all_valid else "FAILED - Check errors above.")
