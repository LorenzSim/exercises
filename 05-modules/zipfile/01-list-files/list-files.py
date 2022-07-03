import sys
from zipfile import ZipFile

with ZipFile(sys.argv[1], 'r') as input:
    for file in input.namelist():
        print(file)
