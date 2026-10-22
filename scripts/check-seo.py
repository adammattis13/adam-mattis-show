"""Validate search metadata, entity references, crawl files, and CSP integrity."""
from pathlib import Path
from html.parser import HTMLParser
import base64
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://www.theadammattisshow.com/'
html = (ROOT / 'dist/index.html').read_text()
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.canonicals = []
        self.h1s = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, 'Duplicate HTML id'
            self.ids.add(a['id'])
        if tag == 'h1': self.h1s += 1
        if tag == 'link' and a.get('rel') == 'canonical': self.canonicals.append(a['href'])
        assert not any(k.startswith('on') for k in a), 'Inline executable event'
        if tag == 'script' and a.get('type') != 'application/ld+json':
            assert a.get('src'), 'Unexpected inline executable script'

page = Page()
page.feed(html)
assert page.h1s == 1
assert page.canonicals == [BASE]
raw = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.S).group(1)
graph = json.loads(raw)['@graph']
ids = {node['@id'] for node in graph}
assert len(ids) == len(graph)
def check_refs(value):
    if isinstance(value, dict):
        if list(value) == ['@id']: assert value['@id'] in ids, value
        for child in value.values(): check_refs(child)
    elif isinstance(value, list):
        for child in value: check_refs(child)
check_refs(graph)
for node in graph:
    if node['@type'] == 'PodcastEpisode':
        assert node['url'].split('#')[1] in page.ids
    if node['@type'] == 'FAQPage':
        for question in node['mainEntity']:
            assert question['name'] in html
            assert question['acceptedAnswer']['text'] in html
hash_value = 'sha256-' + base64.b64encode(hashlib.sha256(raw.encode()).digest()).decode()
assert hash_value in html and hash_value in (ROOT / 'dist/_headers').read_text()
urls = ET.parse(ROOT / 'dist/sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
assert [u.text for u in urls] == [BASE]
assert 'Sitemap: ' + BASE + 'sitemap.xml' in (ROOT / 'dist/robots.txt').read_text()
for name in ('index.html', '_headers', 'robots.txt', 'sitemap.xml'):
    assert (ROOT / name).read_bytes() == (ROOT / 'dist' / name).read_bytes()
print('PASS: canonical, entity graph, visible FAQ parity, episode anchors, CSP hash, sitemap, robots, build parity')
