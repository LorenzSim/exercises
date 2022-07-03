from datetime import datetime
import json

def first(pair): return pair[0]
def second(pair): return pair[1]
def average(array): return str(round(sum(array) / len(array)))

with open('input.txt', 'r') as input:
    content = json.loads(input.read())
    data = list(content.items())

 
data.sort(key = lambda pair: datetime.strptime(first(pair), '%d/%m/%Y'))

result = []

for day in data: result.append(average(second(day)))

with open('output.txt', 'w') as output:
    output.write('\n'.join(result))