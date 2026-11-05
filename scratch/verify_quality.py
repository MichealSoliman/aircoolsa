# -*- coding: utf-8 -*-
import re
import json

with open('index.html', encoding='utf-8') as f:
    html = f.read()

# 1. Check forbidden words
forbidden_phrases = [
    "الرائدة",
    "الأول",
    "100%",
    "0%",
    "لن تدفع ريالاً",
    "بدون أي",
    "فنيون متواجدون الآن",
    "بالقرب منك",
    "متواجدون باستمرار",
    "سيارات خدمة مجهزة",
    "مصرحة بيئياً",
    "خالٍ من الميكروبات",
    "غير مغشوش",
    "خبرة موثقة",
    "تأسيس ومقاولات",
    "الورش العشوائية",
    "تصميم وتطوير متوافق هندسياً"
]

print("=== 1. FORBIDDEN PHRASES CHECK ===")
found_forbidden = False
for phrase in forbidden_phrases:
    matches = [m.start() for m in re.finditer(re.escape(phrase), html)]
    if matches:
        print(f"❌ FOUND FORBIDDEN PHRASE: '{phrase}' at positions {matches}")
        found_forbidden = True
if not found_forbidden:
    print("✅ No forbidden phrases found!")

# Check 'أفضل' usage (only allowed in the guide title)
afdal_matches = [m.start() for m in re.finditer("أفضل", html)]
print(f"Occurrences of 'أفضل': {len(afdal_matches)}")
for pos in afdal_matches:
    snippet = html[max(0, pos-40):min(len(html), pos+60)].replace('\n', ' ')
    print(f"  Snippet: {snippet}")

# 2. Check Phone Numbers
print("\n=== 2. PHONE NUMBER CHECK ===")
# Find all phone numbers in the document
phone_patterns = re.findall(r'(?:tel:|\+?966|05|\b00966)[0-9\s\-]+', html)
print(f"Found phone occurrences: {set(phone_patterns)}")
# Check for fake numbers like '000 0000' or any other
if "000 0000" in html or "0000000" in html:
    print("❌ Fake number '000 0000' found!")
else:
    print("✅ No fake numbers found.")

# 3. Check [TO_CONFIRM] in user-facing text
print("\n=== 3. [TO_CONFIRM] CHECK ===")
to_confirm_matches = [m.start() for m in re.finditer(r'\[TO_CONFIRM[^\]]*\]', html)]
print(f"Total [TO_CONFIRM] occurrences: {len(to_confirm_matches)}")
for pos in to_confirm_matches:
    snippet = html[max(0, pos-30):min(len(html), pos+50)].replace('\n', ' ')
    # check if inside script or attribute or comment
    print(f"  At {pos}: {snippet}")

# 4. Check Headings hierarchy
print("\n=== 4. HEADINGS HIERARCHY ===")
h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
print(f"H1 count: {len(h1s)}")
if len(h1s) == 1:
    print(f"✅ Exactly one H1: {' '.join(h1s[0].split())}")
else:
    print(f"❌ Invalid H1 count: {len(h1s)}")

# 5. Check JSON-LD validation
print("\n=== 5. JSON-LD VALIDATION ===")
json_ld_blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
print(f"Found {len(json_ld_blocks)} JSON-LD blocks.")
for idx, block in enumerate(json_ld_blocks):
    try:
        data = json.loads(block.strip())
        print(f"✅ Block {idx+1} valid JSON-LD: @type = {data.get('@type')}")
        # Check aggregateRating and Review
        block_str = json.dumps(data)
        if "aggregateRating" in block_str or "AggregateRating" in block_str or "Review" in block_str:
            print(f"❌ Block {idx+1} contains aggregateRating or Review!")
        else:
            print(f"✅ Block {idx+1} clean of ratings/reviews.")
    except Exception as e:
        print(f"❌ Block {idx+1} JSON parse error: {e}")

# 6. Check FAQ exact match between HTML and Schema
print("\n=== 6. FAQ EXACT MATCH CHECK ===")
for block in json_ld_blocks:
    try:
        data = json.loads(block.strip())
        if data.get('@type') == 'FAQPage':
            print(f"Testing {len(data.get('mainEntity', []))} FAQ questions against HTML text:")
            all_matched = True
            for q_idx, item in enumerate(data.get('mainEntity', [])):
                q_text = item['name']
                a_text = item['acceptedAnswer']['text']
                if q_text not in html:
                    print(f"❌ Question {q_idx+1} not found in HTML: '{q_text}'")
                    all_matched = False
                if a_text not in html:
                    print(f"❌ Answer {q_idx+1} not found in HTML: '{a_text}'")
                    all_matched = False
            if all_matched:
                print("✅ 100% exact character-for-character match for all FAQ questions and answers!")
    except Exception:
        pass

# 7. Check Internal links
print("\n=== 7. INTERNAL LINKS CHECK ===")
import os
internal_links = set(re.findall(r'href="(/[^"#]+)"', html))
print(f"Found {len(internal_links)} internal absolute links:")
for link in sorted(internal_links):
    # Map to filesystem
    rel_path = link.lstrip('/')
    if not rel_path:
        fs_path = 'index.html'
    elif rel_path.endswith('/'):
        fs_path = os.path.join(rel_path, 'index.html')
    else:
        fs_path = rel_path
    
    exists = os.path.exists(fs_path) or os.path.exists(rel_path) or os.path.exists(rel_path + '.html')
    status = "✅ OK" if exists else "❌ NOT FOUND"
    print(f"  {link} -> {fs_path} [{status}]")

