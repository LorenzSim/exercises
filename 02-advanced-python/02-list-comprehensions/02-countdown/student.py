# Write your code here


def countdown(n):
    return ', '.join([str(i) for i in sorted(range(1, n + 1), reverse=True)])