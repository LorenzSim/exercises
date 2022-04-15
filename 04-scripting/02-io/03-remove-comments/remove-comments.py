import re
import sys

def remove_comments(string):
    return re.sub('#.*$', '', string,flags=re.MULTILINE)

for file in sys.argv[1:]:
    with open(file, 'r') as f:
        content = f.read()
        
    with open(file, 'w') as f:
        f.write(remove_comments(content))
