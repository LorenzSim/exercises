import json
import re
import sys
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def replace_space(string): return re.sub(' ', '%20', string)

url = f'https://api.lyrics.ovh/v1/{replace_space(sys.argv[1])}/{replace_space(sys.argv[2])}'

with urllib.request.urlopen(url) as input:
    content = json.loads(input.read())
    print(content['lyrics'])