from .euclidean import xgcd
def inverse(a: int, m: int):
    """ Return the inverse modulus of a and m if they are relatively prime, None if not """
    # a, m = args.nums[0], args.nums[1]
    m0 = m
    y = 0
    x = 1

    g, _, _ = xgcd(a, m)
    if g == 1:

        while a > 1:
            q = a // m

            t = m

            m = a % m
            a = t
            t = y

            y = x - q * y
            x = t

        if x < 0:
            x = x + m0
        
        return x
    else:
        return None