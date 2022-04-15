# Write your code here
import re


def scrape_email_addresses(string):
    return re.findall(r'[a-zA-Z\d]+\@.+\.[a-zA-Z\d]+', string)