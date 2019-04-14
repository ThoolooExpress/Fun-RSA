# Defines rp function
from .euclidean import xgcd
def rp(a: int):
    ''' Return a number that is relatively prime with a (gcd(a, rp) == 1) '''
    print (a)
    ret = a - 1
    while xgcd(a, ret)[0] > 1:
        ret -= 1
    return ret
