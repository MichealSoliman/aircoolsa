import json, re

for path in ['ac-installation-jeddah/index.html', 'ac-gas-refilling-jeddah/index.html', 'ac-copper-piping-jeddah/index.html', 'services/index.html', 'ac-cleaning-jeddah/index.html']:
    txt = open(path, encoding='utf-8').read()
    body = txt[txt.find('<body'):]
    scripts = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"]>(.*?)</script>', txt, re.DOTALL)
    for s in scripts:
        d = json.loads(s.strip())
        graph = d.get('@graph', [d]) if isinstance(d, dict) else d
        for item in graph:
            if isinstance(item, dict) and item.get('@type') == 'FAQPage':
                print(f"=== {path} FAQPage ===")
                for q in item.get('mainEntity', []):
                    q_name = q.get('name')
                    ans = q.get('acceptedAnswer', {}).get('text')
                    print(f"  Q: {q_name} -> Found: {q_name in body}")
                    # check first 30 chars of answer
                    ans_snippet = ans[:30] if ans else ""
                    print(f"  A snippet in body: {ans_snippet in body}")

