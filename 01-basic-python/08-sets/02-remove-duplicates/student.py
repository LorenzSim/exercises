# Write your code here
def remove_duplicates(xs):
    result = []
    trash = set()
    for x in xs:
        if x not in trash:
            result.append(x)
            trash.add(x)
    return result