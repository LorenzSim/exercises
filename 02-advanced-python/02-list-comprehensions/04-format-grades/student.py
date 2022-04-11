# Write your code here
def average(numbers): return round(sum(numbers) / len(numbers))
def format_grades(grades): return "\n".join(f'{student}: {average(grade)}' for student, grade in grades.items())
