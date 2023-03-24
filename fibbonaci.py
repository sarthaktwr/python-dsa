import math

def fibbonaci(n):
    if n <= 1:
        return n
    else:
        return (fibbonaci(n - 1) + fibbonaci(n - 2))

count = 20
# print(fibbonaci(n))
for i in range(count):
    print(fibbonaci(i), end = ' ')