# Write your code here
import re
def parse_link(string):
    match = re.fullmatch(r'<a href="(.+)">(.+)</a>', string)
    if not match: return None
    return tuple(reversed(match.groups()))
