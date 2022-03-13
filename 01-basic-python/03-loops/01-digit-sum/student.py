# Write your code here
def digitSum(n):
    
    result = 0

    while n > 0:
        n += n % 10
        n = n // 10

    return result