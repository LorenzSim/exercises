
from argparse import ArgumentParser
import sys


parser = ArgumentParser(prog='head', description='print out the first 10 lines of a file')
parser.add_argument('filename', nargs='?')
parser.add_argument('-n', '--lines', type=int, default=10)

args = parser.parse_args()

if args.filename: 
    with open(args.filename) as file: content = file.readlines()

else: content = sys.stdin.readlines()

print(''.join(content[:args.lines]), end='')
