# Write your code here
def frequencies(xs):
    result = {}
    for x in xs:
        if x not in result:
            result.update({x: 0})
        result[x] += 1
    return result