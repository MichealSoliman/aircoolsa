import glob

patterns = [
    'نقدم 7 خدمات',
    'وسيتوجه الفني إليك خلال دقائق',
    'بخصومات تصل حتى 30%',
    '30 إلى 50 بار',
    'بنسبة قد تصل إلى 40%',
    'بنسبة تفوق 70%'
]

for p in patterns:
    found = []
    for f in glob.glob('**/*.html', recursive=True):
        txt = open(f, encoding='utf-8').read()
        if p in txt:
            found.append(f)
    print(f'Pattern "{p}": found in {len(found)} files: {found}')

