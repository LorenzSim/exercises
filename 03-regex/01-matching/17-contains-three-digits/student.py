
# Write your code here
import re 
def contains_three_digits(string):
    return re.fullmatch('.*[1-9].*[1-9].*[1-9].*', string)