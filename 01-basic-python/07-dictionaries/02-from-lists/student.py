# Write your code here
def from_lists(keys, values):
    result = {}
    for i in range(0, len(keys)):
        key = keys[i]
        value = values[i]
        result.update({key: value})
    return result