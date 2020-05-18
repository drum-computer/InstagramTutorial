import urllib.request 
import json
import operator

page = urllib.request.urlopen('https://www.instagram.com/explore/tags/girl/?__a=1')
str_page = page.read().decode('utf-8')
response = json.loads(str_page)

nodes = response['tag']['top_posts']['nodes']

top = {}

for node in nodes:
	k = node['display_src']
	v = node['likes']['count']
	top[k] = v

sorted_top = sorted(top.items(), key = operator.itemgetter(1), reverse = True)

for i, (k,v) in enumerate(sorted_top):
	op('top_table')[i + 1, 'link'] = k
	op('top_table')[i + 1, 'likes'] = v
