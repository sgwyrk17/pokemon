#coding:utf-8
import os
from urlparse import urljoin
from pyquery import PyQuery as pq
import requests

url = "https://pokemongo.gamewith.jp/article/show/26775"

dom = pq(url)
result = set()
download_count = 0
save_path = os.path.abspath('./pokemon')
for img in dom('img').items():
	img_url = img.attr['src']
	if img_url.startswith('http'):
		result.add(img_url)
	else:
		result.add(urljoin(url, img_url))

	download_count += 1
	output = '%s/%03d.png' % (save_path,download_count)
	print('%s : Download... %s' % (download_count, os.path.basename(img_url)))
	with open(output,'wb') as f:
		raw = requests.get(img_url).content
		f.write(raw)