import argparse
from PIL import Image 
from pathlib import Path

def parse_size(size_string): 
    x, y = size_string.lower().split('x')
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
