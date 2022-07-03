import requests as req, sys

url = f'https://www.toptal.com/developers/gitignore/api/{",".join(sys.argv[1:])}'

with open('.gitignore', 'w') as file:
    file.write(req.get(url).text)
