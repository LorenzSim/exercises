
import argparse
import sys


parser = argparse.ArgumentParser(prog='Count the number of lines of code')
parser.add_argument('-e', '--count-empty-lines', default=False, action='store_true')
parser.add_argument('--comment')

args = parser.parse_args()
no_empty_lines = args.count_empty_lines
comments = args.comment
lines = sys.stdin
number_of_lines = 0

for line in lines:
    if no_empty_lines and line.isspace() or comments and line.strip().startswith(comments): continue
    number_of_lines += 1

print(number_of_lines)