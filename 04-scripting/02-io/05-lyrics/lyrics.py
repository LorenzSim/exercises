import json
import sys

import urllib.request

def replace_space(string): return string.replace(' ', '%20')

artist = replace_space(sys.argv[1])
song = replace_space(sys.argv[2])

url = f'https://api.lyrics.ovh/v1/{artist}/{song}'

with urllib.request.urlopen(url) as content:
    lyrics = json.loads(content.read())
    print(lyrics['lyrics'])
