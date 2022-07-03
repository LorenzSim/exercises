
import re


def parse_student(string):
    return re.fullmatch(r'([a-zA-Z\s]+):(\d+)/(\d+)\s([+-]*)\n', string).groups()
    
with open('input.txt') as input:
    data = input.readlines()


with open('output.txt', 'w') as output:
    for student in data:
        name, spent, earned, plus_min = parse_student(student)
        spent = int(spent)
        earned = int(earned)
        spent += plus_min.count('-')
        earned += plus_min.count('+')
        output.write(f'{name}:{spent}/{earned}\n')
        

