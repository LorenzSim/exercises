import csv

with open('../title-basics.tsv', 'r') as input:
    data = csv.DictReader(input, delimiter='\t')
    movies = []
    
    for line in data:
        title, runtime, type = line['primaryTitle'], line['runtimeMinutes'], line['titleType']
        if type == 'movie': movies.append((0 if runtime == '\\N' else int(runtime), title))
        
    movies.sort(key=lambda x : x[0], reverse=True)

    for runtime, title in movies[:100]: print(f'{runtime} {title}')
