import sys

with open(sys.argv[2], 'w') as dest:
    with open(sys.argv[1], 'r') as source:
        dest.write(source.read())
        source.close()
        dest.close()

