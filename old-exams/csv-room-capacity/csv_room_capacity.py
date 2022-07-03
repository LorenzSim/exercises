
import csv

table = {}

with open('exam-schedule.csv') as input:
    data = csv.DictReader(input.readlines())

for line in data: 
    datum, dagdeel, lokaal = line['Datum'], line['Dagdeel'], line['Lokaal']
    if (datum, dagdeel) not in table:
        table[(datum, dagdeel)] = 1
    else: table[(datum, dagdeel)] += 1
    

    
