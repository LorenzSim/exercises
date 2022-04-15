# Write your code here
import re


def hide_email_addresses(string):
    def replace(m): return '*' * len(m.group(1))
    return re.sub(r'([a-zA-Z\d.]+@[a-zA-Z.]+)', replace, string)