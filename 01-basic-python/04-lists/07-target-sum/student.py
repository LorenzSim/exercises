# Write your code here
def target_sum(xs, target):
    for x in xs:
        for y in xs:
            if x + y == target:
                return True

    return False