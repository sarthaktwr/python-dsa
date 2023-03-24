import math

def add(n):
    if n == 1:
        return 1
    return(n + add(n - 1))

n = 100
print(add(n))