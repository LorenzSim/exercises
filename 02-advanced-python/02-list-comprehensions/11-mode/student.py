# Write your code here
def frequencies(ns):
    result = {}
    for n in ns:
        if n not in result:
            result[n] = 0
        result[n] += 1
    return result

def mode(ns): return max(frequencies(ns).items(), key = lambda a : a[1])[0]

