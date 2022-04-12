# Write your code here


from audioop import reverse


def countdown(n):
    return ', '.join(str(i) for i in range(n, 0, -1))
