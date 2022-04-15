# Write your code here
import re


def correct_dates(string):
    return re.sub(r'(\d{1,2}/)(\d{1,2}/)', r'\2\1', string)