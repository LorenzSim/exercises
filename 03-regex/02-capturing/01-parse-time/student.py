# Write your code here
import re
def parse_time(string):
    match = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2})(?::|\.(\d{3}))?', string)
    if not match: return None
    return tuple([int(e) for e in match.groups('000')])

