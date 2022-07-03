from argparse import ArgumentParser
import json

import requests as req 

parser = ArgumentParser(prog='genderize')
parser.add_argument('name')

args = parser.parse_args()

url = f'https://api.genderize.io/?name={args.name}'

data = json.loads(req.get(url).text)

gender = data["gender"]
probability = int(float(data["probability"]) * 100)

print(f'{gender} ({probability}%)')


