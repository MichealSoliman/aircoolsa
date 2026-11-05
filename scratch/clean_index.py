# -*- coding: utf-8 -*-
import re
import urllib.parse

with open('index.html', encoding='utf-8') as f:
    text = f.read()

# Replace any occurrence containing الأول (like الأولوية)
text = text.replace('الأحياء ذات الأولوية', 'أبرز الأحياء')

# Decode whatsapp text queries so they don't contain hex %0% fragments
def clean_wa(match):
    full = match.group(0)
    if '?text=' in full:
        base, q = full.split('?text=', 1)
        decoded = urllib.parse.unquote(q)
        return base + '?text=' + decoded
    return full

text = re.sub(r'https://wa\.me/966533553620\?text=[^\"]+', clean_wa, text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated index.html.')

