# Write your code here

def add_indices(xs):
    return list(zip(range(len(xs)), xs))


def add_indices(xs):
    result = []
    for i in range(0, len(xs)):
        result.append((i, xs[i]))

    return result

