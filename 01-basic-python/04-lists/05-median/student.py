# Write your code here
def median(ns):
    sortedNs = sorted(ns)
    i = len(sortedNs) // 2
    if len(sortedNs) % 2 == 0:
        return (sortedNs[i - 1] + sortedNs[i]) / 2
    return sortedNs[i]
    