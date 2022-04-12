# Write your code here
def is_prime(n): return n > 1 and all(n % r != 0 for r in range(2, n))
