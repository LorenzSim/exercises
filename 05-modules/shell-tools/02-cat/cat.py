import sys
for filename in sys.argv[1:]: 
    with open(filename) as file:
        print(file.read(), end='')