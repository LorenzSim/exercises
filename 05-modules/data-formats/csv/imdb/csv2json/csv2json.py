import json
from pathlib import Path
import sys
import csv
"""
json_content = []
filename = sys.argv[1]

with open(filename) as file:
    reader = csv.DictReader(file)
    for row in reader:
        json_content.append(row)
    

with open(f'{Path(filename).stem}.json', 'w') as file:
    res = json.dumps(json_content, indent=4)
    file.write(res)
"""

data = list(csv.DictReader(sys.stdin))

print(json.dumps(data))
