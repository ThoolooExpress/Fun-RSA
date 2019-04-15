# Defines functions that deal with primality
from .euclidean import xgcd

def rp(a: int) -> int:
    ''' Return a number that is relatively prime with a (gcd(a, rp) == 1), and is smaller than a.
        @warning -- may return 1 if no other suitable number may be found
    '''
    print (a)
    ret = a - 1
    while xgcd(a, ret)[0] > 1:
        ret -= 1
    return ret

def isPrime(a: int) -> bool:
    """ Test to see if a is prime. """
    if a == 2:
        return True
    if a < 2 or a % 2 == 0:
        return False
    for i in range(3, int(a ** 0.5) + 2, 2):
        # Iterate over ever odd number from 3 to sqrt(a) + 2
        if a % i == 0:
            return False
    return True