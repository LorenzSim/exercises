
import json


with open('input.json') as input:
    data = json.loads(input.read())
    with open('output.txt', 'w') as output:
        for currency in data:
            name = currency['currency']
            history = [float(x) for x in currency['history']]
            output.write(f'{name} {min(history)} {max(history)} {history[len(history) - 1]}\n')

