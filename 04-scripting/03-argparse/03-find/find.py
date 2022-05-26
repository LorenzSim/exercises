import os, argparse

parser = argparse.ArgumentParser(prog='find')
parser.add_argument('directory', default='.')
parser.add_argument('--nodirectories', default=False, action='store_true')
parser.add_argument('--nofiles', default=False, action='store_true')
args = parser.parse_args()

data = list(os.walk(args.directory, topdown=False))
dirs = data[1]
files = data[2]
print (data)


