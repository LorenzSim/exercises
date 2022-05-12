import sys

with open(sys.argv[1], 'r') as src:
    with open(sys.argv[2], 'w') as dest:
        dest.write(src.read())
        