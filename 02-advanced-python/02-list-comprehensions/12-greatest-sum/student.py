# Write your code here
def greatest_sum(ns): 
    return max([(i, j) for i in range(len(ns)) for j in range(i + 1, len(ns) + 1)], key=lambda pairs : sum(ns[pairs[0]:pairs[1]]))

def greatest_sum2(ns):
    max = 0
    res = (0, 1)
    for i in range(len(ns)):
        for j in range(i + 1, len(ns) + 1):
            tmp = sum(ns[i:j])
            if (tmp > max):
                res = (i, j)
                max = tmp
    return res    

    
