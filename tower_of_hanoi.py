import math 

def ans(n , from_, to, aux):
    if n == 1:
        print(f'Move the disc {n} from {from_} to {to}')
        return
    ans(n - 1, from_, aux, to)
    print(f'Move the disc {n} from {from_} to {to}')
    ans(n - 1, aux, to, from_)

n = 8
from_ = 'A'
to = 'B'
aux = 'C'

ans(n , from_, to, aux)