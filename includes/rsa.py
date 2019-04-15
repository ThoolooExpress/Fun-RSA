from .euclidean import gcd, lcm
from .prime import isPrime, rp
from .inverse import inverse

class KeyError(Exception):
    """ Exception raised when a keypair cannot be constructed from supplied values
        Attributes:
            values -- the bad values
            reason -- the reason the values couldn't be used to construct a keypair
    """

    def __init__(self, values: (int, int), reason: str):
        self.values = values
        self.reason = reason
    def __str__(self):
        a, b = self.values
        return "KeyError: {}, and {} cannot be used to create a key pair because: {}".format(a, b, self.reason)


def keyTuple(a: int, b: int) -> (int, int, int):
    ''' Generate a key pair (e, d, n) from two prime numbers
        @precondition:  a != b and both a and b are prime
    '''
    if a == b:
        raise KeyError((a,b), "a and b must not be equal.")
    
    if not (isPrime(a) and isPrime(b)):
        raise KeyError((a,b), "a and b must both be prime.")
    
    n = a * b # Modulus
    tot = int(lcm(a - 1, b - 1)) # totient
    e = 0 # [e]ncrypt key
    for i in range(2, tot):  # find a prime number in (1, tot) that is relatively prime to tot
        if isPrime(int(i)) and tot % int(i) != 0:
            e = i
            break
    if e == 0:
        raise KeyError((a,b), "Could not find a suitable e value, try using larger primes.")
    
    d = inverse(e, tot) # [d]ecrypt key

    return e, d, n


def rsaEncrypt(p: int, e: int, n: int) -> int:
    """ Encrypt a message using the public key pair e, n """
    return (p ** e) % n

def rsaDecrypt(c: int, d: int, n: int) -> int:
    """ Decrypt a message using the public key pair d, n """
    return (c ** d) % n