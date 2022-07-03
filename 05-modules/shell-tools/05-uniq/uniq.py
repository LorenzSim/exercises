from argparse import ArgumentParser
from fileinput import filename
import sys


parser = ArgumentParser(prog='uniq')
parser.add_argument('filename', nargs='?')
parser.add_argument('-i', '--ignore-case', action='store_true', default=False)

args = parser.parse_args()

if args.filename: 
    with open(filename) as file: 
        content = file.readlines()

else: content = sys.stdin.readlines()

for i in range(len(content)):
    if i == len(content) - 1: print(content[i], end='')
    elif args.ignore_case:
        if content[i].lower() != content[i + 1].lower(): 
            print(content[i], end='')
    elif content[i].lower() != content[i + 1].lower(): 
            print(content[i], end='')
