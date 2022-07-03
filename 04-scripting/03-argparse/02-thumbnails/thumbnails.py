import argparse, re, sys
from PIL import Image 
from pathlib import Path

def parse_size(size_string): 
    match = re.fullmatch(r'(\d+)x(\d+)', size_string)
    if not match: 
        print(f"Parsing error: '{size_string}' is invalid!")
        sys.exit(-1)
        
    x, y = match.groups()
    return (int(x), int(y))
        

def parse_name(name, pattern): 
    path = Path(name)
    return pattern.replace('%b', path.stem).replace('%x', path.suffix)


parser = argparse.ArgumentParser(prog='thumbnails', description='');
parser.add_argument('files', nargs='+')
parser.add_argument('--size', '-s', default='64x64')
parser.add_argument('--pattern', '-p', default='%b-thumbail.%x')

args = parser.parse_args()

for filename in args.files:
    img = Image.open(filename).resize(parse_size(args.size))
    img.save(parse_name(filename, args.pattern))

