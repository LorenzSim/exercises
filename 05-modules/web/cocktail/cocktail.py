import json, re, sys
import requests as req

def download_cocktail(url): 
    return json.load(req.get(url).text.decode('utf-8'))['drinks'][0]

def is_ingredient_key(key):
    return re.fullmatch('strIngredient\d', key)

def replace_space(string): return re.sub(' ', '%20', string)

if len(sys.argv) > 1: url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={replace_space(sys.argv[1])}'
else: url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'

cocktail = download_cocktail(url)
print(cocktail['strDrink'])

for i in range(1, 16):
    ingredient = cocktail[f"strIngredient{i}"]
    amount = cocktail[f"strMeasure{i}"]
    if ingredient == None: break
    print(f'{ingredient} ({amount.strip()})')
