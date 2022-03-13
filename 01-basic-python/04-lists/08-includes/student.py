# Write your code here
from operator import contains


def includes(xs, ys):
    for y in ys:
        if not contains(xs, y):
            return False
    return True