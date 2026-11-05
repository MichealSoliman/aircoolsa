with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Look for negative positioning
negatives = re.findall(r'class="[^"]*(?:-(?:right|left)-\d+|overflow-visible|w-\[\d+vw\])[^"]*"', text)
print('Negative positioning classes:')
for n in set(negatives):
    print('-', n)

# Check html and body overflow classes
print('\nHTML tag:', re.search(r'<html[^>]*>', text).group(0))
print('BODY tag:', re.search(r'<body[^>]*>', text).group(0))

# Check table containers
tables = re.findall(r'<table[^>]*>', text)
print(f'\nTotal tables: {len(tables)}')
for m in re.finditer(r'(<div[^>]*>[\s\S]*?<table)', text):
    wrapper = m.group(1)[:120]
    print('Table wrapper:', wrapper.replace('\n', ' '))

