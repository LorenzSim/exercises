import argparse

parser = argparse.ArgumentParser(prog='range', description='Print a range of numbers.')
parser.add_argument('start', type=int, help='Define the beginning of the range.')
parser.add_argument('stop', type=int, help='Define the end of the range. (Not exclusive, unless option \'-x\' is used.)')
parser.add_argument('-x', '--exclusive', default=False, action='store_true')
parser.add_argument('-s', '--step', type=int, default=1)

args = parser.parse_args()
stop = args.stop if args.exclusive else args.stop + 1

for i in range(args.start, stop, args.step): print(i)
