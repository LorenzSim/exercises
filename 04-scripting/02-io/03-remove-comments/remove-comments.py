import re
import sys

def remove_comment_from_line(string): 
    return re.sub('#.*', '', string, flags=re.MULTILINE)

for filename in sys.argv[1:]:
    with open(filename) as file:
        content = file.read()

    with open(filename, 'w') as file:
        file.write(remove_comment_from_line(content))

