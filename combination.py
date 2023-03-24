import math

def factorial(n):
    
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def combination(m, r):
    return((factorial(m) / factorial(r) * factorial(m - r)))

m = 5
r = 6

print(combination(m, r))