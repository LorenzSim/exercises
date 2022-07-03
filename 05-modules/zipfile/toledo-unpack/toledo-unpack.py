import re
from zipfile import ZipFile
import sys
def slug(string):
    words = string.split(" ")
    return '-'.join(s.lower() for s in words[1:] + [words[0]])

def parse_name(filename):
    with open(filename) as input:
        return slug(re.search(r'Naam: ([a-zA-Z\s]+)', input.read()).groups(1)[0])

def parse_q_number(string):
    return re.search(r'Submission_(q\d{7}).*', string).groups(1)[0]


def open_toledo_zip():
    with ZipFile(sys.argv[1]) as input:
        for file in input.namelist():
            pass