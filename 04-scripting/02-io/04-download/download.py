import urllib.request
import sys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

with urllib.request.urlopen(sys.argv[1]) as input:
   print(input.read())
   