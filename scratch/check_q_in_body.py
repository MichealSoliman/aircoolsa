import json, re

for path in ['ac-maintenance-jeddah/index.html', 'ac-sanitization-jeddah/index.html']:
    txt = open(path, encoding='utf-8').read()
    body = txt[txt.find('<body'):]
    scripts = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"]>(.*?)</script>', txt, re.DOTALL)
    for s in scripts:
        d = json.loads(s.strip())
        for item in d.get('@graph', []):
            if item.get('@type') == 'FAQPage':
                for q in item.get('mainEntity', []):
                    q_name = q.get('name')
                    print(f"{path} Question: {q_name} -> In Body: {q_name in body}")

