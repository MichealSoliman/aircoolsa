import json, re

txt = open('index.html', encoding='utf-8').read()
body = txt[txt.find('<body'):]
scripts = re.findall(r'<script\s+type=[\'"]application/ld\+json[\'"]>(.*?)</script>', txt, re.DOTALL)
for s in scripts:
    d = json.loads(s.strip())
    if isinstance(d, dict) and d.get('@type') == 'FAQPage':
        print("=== index.html FAQPage ===")
        for q in d.get('mainEntity', []):
            q_name = q.get('name')
            ans = q.get('acceptedAnswer', {}).get('text')
            print(f"  Q: {q_name} -> Found: {q_name in body}")
            ans_snippet = ans[:30] if ans else ""
            print(f"  A snippet in body: {ans_snippet in body}")

