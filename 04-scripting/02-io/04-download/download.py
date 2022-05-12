import sys
import urllib.request

import urllib3

with urllib3.request.urlopen(sys.argv[1]) as content:
    print(content.read())


