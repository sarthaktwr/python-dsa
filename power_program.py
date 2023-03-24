import math 

def power(n, m):
    if m == 1:
        return n
    else:
        return (power(n, m - 1) * n)
    
n = 2
m = 6
print(power(n, m), end = ' ')