# Write your code here

"""def mode(ns):
    counts = [ns.count(n) for n in set(ns)]
    return ns[counts.index(max(counts))]"""
def frequencies(ns):
    result = {}
    for n in ns:
        if n not in result:
            result[n] = 0
        result[n] += 1
    return result
def mode(ns):
    fs = frequencies(ns)
    return max(fs.items(), key=second)[0]
def second(pair):
    return pair[1]