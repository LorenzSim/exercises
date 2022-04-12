# Write your code here
def is_increasing(ns): return all(a <= b for (a, b) in zip(ns, ns[1:]))
