import os, argparse
from pathlib import Path
import re

def check_min_file_size(file_path, min_size):
    return not min_size or min_size <= os.path.getsize(file_path)

def check_max_file_size(file_path, max_size):
    return not max_size or max_size >= os.path.getsize(file_path)

def check_file_extension(file_path, extension):
    return not extension or Path(file_path).suffix == extension

def file_contains_pattern(file_path, pattern):
    if not pattern: return True
    with open(file_path) as file: return re.search(pattern, file.read())

def file_meets_constraints(file_path, args):
    return (
         check_file_extension(file_path, args.extension)  
        and check_min_file_size(file_path, args.minimum_size)
        and check_max_file_size(file_path, args.maximum_size)
        and file_contains_pattern(file_path, args.contains))

parser = argparse.ArgumentParser(prog='find')
parser.add_argument('directory')
parser.add_argument('--no-directories', default=False, action='store_true')
parser.add_argument('--no-files', default=False, action='store_true')
parser.add_argument('--minimum-size', type=int)
parser.add_argument('--maximum-size', type=int)
parser.add_argument('--extension')
parser.add_argument('--contains')

args = parser.parse_args()

for root, dirs, files in os.walk(args.directory):
    if not args.no_directories: 
        for dir in dirs: print(f'{root}/{dir}')
    
    if not args.no_files:
        for file in files:
            file_path = f'{root}/{file}'
            if file_meets_constraints(file_path, args): print(file_path)
