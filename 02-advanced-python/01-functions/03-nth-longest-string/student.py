# Write your code here
def nth_longest_string(n, strings):
    return sorted(strings, key=len)[-n]
