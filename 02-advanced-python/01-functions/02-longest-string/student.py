# Write your code here
def longest_string(strings):
    return max(strings, key=lambda p: len(p))