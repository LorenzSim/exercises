
import csv


def most_episodes():
    result = dict()
    with open('../title-episodes.tsv') as input:
        data = csv.DictReader(input, delimiter='\t')
        for episode in data:
            tconst = episode['parentTconst']
            if tconst not in result: result[tconst] = 0
            else: result[tconst] += 1
        return result.items()


def find_title(tconst: str):
    
    with open('../title-basics.tsv') as input:
        data = csv.DictReader(input, delimiter='\t')
        for name in data: 
            if name['tconst'] == tconst: return name['primaryTitle']

tconst, number_of_episodes = max(most_episodes(), key=lambda x: x[1])
print(f'{find_title(tconst)}: {number_of_episodes} episodes')
