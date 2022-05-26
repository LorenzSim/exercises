import json, re, ssl, sys, urllib.request 
from PIL import Image as image

ssl._create_default_https_context = ssl._create_unverified_context

number = '' if len(sys.argv) == 1 else re.sub(' ', '%20', sys.argv[1]) + '/'
url = f'https://xkcd.com/{number}info.0.json'

with urllib.request.urlopen(url) as input: content = json.loads(input.read())

with urllib.request.urlopen(content['img']) as input: image.open(input).show()
