# Write your code here
def average(grades): return round(sum(grades) / len(grades))
def format_grades(grades): return '\n'.join(f'{name}: {average(grade)}' for (name, grade) in grades.items())
