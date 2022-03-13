# Write your code here
def rotate(xs, n):
    for i in range(0, n):
        x = xs[0]
        xs.remove(x)
        xs.append(x)

