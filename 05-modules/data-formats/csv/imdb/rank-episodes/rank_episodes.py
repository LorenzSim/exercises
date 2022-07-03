
import csv
import sys


title = sys.argv[1]

def find_episodes(id: str):
    result = []
    with open('../title-episodes.tsv') as input: 
        data = csv.DictReader(input, delimiter='\t')
        for episode in data:
            if episode['parentTconst'] == id:
                episode_id = episode['tconst'], 
                result.append({'id': episode_id, 'seasonNumber': episode['seasonNumber'], 'episodeNumber': episode['episodeNumber'], 'title': None, 'rating': None})
    return result

with open('../title-basics.tsv') as input: 
    title_basics = csv.DictReader(input, delimiter='\t')
    with open('../title-ratings.tsv') as input: 
        title_ratings = csv.DictReader(input, delimiter='\t')

        for line in title_basics:
            if line['primaryTitle'] == title: 
                series_id = line['tconst']
                break

        episodes = find_episodes(series_id)

        for episode in episodes:
            episode_id = episode['id']
            for line in title_basics:
                if line['tconst'] == episode_id:
                    episode['title'] = line['primaryTitle']
                    break
            for line in title_ratings:
                if line['tconst'] == episode_id:
                    episode['rating'] = line['averageRating']
                    break
    
for line in episodes:
    print(line.items())
                






