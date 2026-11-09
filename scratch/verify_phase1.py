import os
import re
from urllib.parse import urlparse

PAGES = [
    '/', '/services/', '/about/', '/contact/', '/blog/', '/privacy/',
    '/ac-installation-jeddah/', '/ac-maintenance-jeddah/', '/ac-cleaning-jeddah/',
    '/ac-sanitization-jeddah/', '/ac-gas-refilling-jeddah/', '/ac-copper-piping-jeddah/',
    '/blog/choosing-ac-company-jeddah/', '/blog/ac-cleaning-guide-jeddah/',
    '/blog/ac-maintenance-guide-jeddah/', '/blog/ac-gas-refilling-guide-jeddah/',
    '/blog/ac-copper-piping-guide-jeddah/'
]

def page_to_file(path):
    p = path.strip('/')
    if not p:
        return 'index.html'
    return os.path.join(p, 'index.html')

all_links = set()
broken_links = []
redirect_risks = []

for page in PAGES:
    filepath = page_to_file(page)
    if not os.path.exists(filepath):
        print(f"Page file does not exist: {filepath}")
        continue
    with open(filepath, encoding='utf-8') as f:
        content = f.read()

    # extract href
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    for h in hrefs:
        if h.startswith('tel:') or h.startswith('mailto:') or h.startswith('javascript:') or h.startswith('#'):
            continue
        
        is_internal = False
        target_path = ''
        if h.startswith('https://aircoolsa.com'):
            parsed = urlparse(h)
            target_path = parsed.path
            is_internal = True
        elif h.startswith('/'):
            target_path = urlparse(h).path
            is_internal = True
        elif not h.startswith('http'):
            redirect_risks.append((page, h, 'Relative URL without leading slash'))

        if is_internal:
            all_links.add((h, target_path))
            # check trailing slash for directory routes
            if not target_path.startswith('/assets/') and not target_path.endswith('.ico') and not target_path.endswith('.webmanifest') and not target_path.endswith('.xml') and not target_path.endswith('.txt'):
                if not target_path.endswith('/'):
                    redirect_risks.append((page, h, 'Missing trailing slash (triggers 301)'))
            
            # check target file
            if target_path.startswith('/assets/') or target_path in ['/favicon.ico', '/site.webmanifest', '/robots.txt', '/sitemap.xml']:
                asset_file = target_path.lstrip('/')
                if not os.path.exists(asset_file):
                    broken_links.append((page, h, 'Asset not found: ' + asset_file))
            else:
                target_file = page_to_file(target_path)
                if not os.path.exists(target_file):
                    broken_links.append((page, h, 'Page file not found: ' + target_file))

print(f"Total pages checked: {len(PAGES)}")
print(f"Total unique internal links checked: {len(all_links)}")

if redirect_risks:
    print(f"\nRedirect risks found ({len(redirect_risks)}):")
    for r in redirect_risks:
        print(" ", r)
else:
    print("\nNo redirect risks found (all internal page links have correct trailing slash or full URL)!")

if broken_links:
    print(f"\nBroken links found ({len(broken_links)}):")
    for b in broken_links:
        print(" ", b)
else:
    print("\nAll internal links point to valid existing files (HTTP 200 equivalent on static server)!")

