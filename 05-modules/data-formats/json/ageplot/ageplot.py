import json
from matplotlib import pyplot as plt
import numpy as np

with open('../covid.json') as input:
    data = json.loads(input.read())

table = {}

for person in data:
    age_group = person['AGEGROUP']
    n = person['COUNT']
    if age_group not in table:
        table[age_group] = n
    else: table[age_group] += n

age_groups = sorted(table.keys())
values = [table[group] for group in age_groups]

x = np.array(age_groups)
y = np.array(values)

plt.barh(x, y)
plt.show()