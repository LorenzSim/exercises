everyone = []
attending = []
absentees = []

with open('all.txt') as input:
    for person in input.readlines():
        everyone.append(person.lower())
    

with open('attending.txt') as input:
     for person in input.readlines():
        attending.append(person.lower())
    
for person in everyone:
    if person not in attending:
        absentees.append(person)

with open('absentees.txt', 'w') as file:
    file.write(''.join(absentees))