import math
def gcd(a, b):
    m = min(a, b)
    h = max(a, b)

    if m == 0:
        return h
    
    elif m == 1:
        return 1
    
    else:
        return(gcd(m, h % m))

a = 24
b = 60
print(gcd(24, 60))