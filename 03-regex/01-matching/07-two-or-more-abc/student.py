# Write your code here
import re
def two_or_more_abc(string):
    return re.fullmatch('(abc){2,}', string)