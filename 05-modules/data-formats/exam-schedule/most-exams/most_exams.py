
import csv


students = {}
with open('../exam-schedule.csv') as input:
    schedule = csv.DictReader(input)
    for line in schedule:
        student_id = line['Student ID']
        students[student_id] = students.get(student_id, 0) + 1

    
max_exams = max(students.values())

for student, exams in students.items():
    if exams == max_exams: print(f'{student} has {exams} exams')

