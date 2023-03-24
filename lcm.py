import math
from re import T

def lcm(a, b):
    t =  a % b
    if t == 0:
        return a
    return a * lcm(b, t) / t

a = 2
b = 5
print(lcm(a,b))
