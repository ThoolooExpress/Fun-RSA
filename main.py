import argparse

parser = argparse.ArgumentParser(description="This program does everything!!")

def xgcd(args):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    a, b = args.nums[0], args.nums[1]
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
     

    print("GCD: {}, c1: {}, c2: {}".format(b, x0, y0))

def modular(args):
    print("We're running the modular shit now!")

def rp(args):
    print("_relativley_ prime")

def inverse(args):
    print("running inverse")

def rsa(args):
    print("Oh look, the only function that actually matters")


subparsers = parser.add_subparsers() # Ugh... this is really complicated...

e_parser = subparsers.add_parser("euclidean", help="Run question 1: Implement Euclidean Algorithm for calculating greatest common divisor")
e_parser.set_defaults(func=xgcd)
m_parser = subparsers.add_parser("modular", help="Run question 2: Modular arithmetic")
m_parser.set_defaults(func=modular)
p_parser = subparsers.add_parser("RP", help="Run question 3: Find Relatively Prime")
p_parser.set_defaults(func=rp)
i_parser = subparsers.add_parser("inverse", help="Run question 4: Find Inverse")
i_parser.set_defaults(func=inverse)
r_parser = subparsers.add_parser("rsa", help="Run question 5: Practice with RSA algorithm")
r_parser.set_defaults(func=rsa)

# e_parser

e_parser.add_argument("nums", metavar="N", type=int, nargs=2, help="The two numbers for which to find the greatest common divisor")

# m_parser
m_parser.add_argument("dividend", metavar="A", type=int, nargs=1, help="The dividend for the modulus function")
m_parser.add_argument("divisor", metavar="B", type=int, nargs=1, help="The divisor for the modulus function")

# p_parser
p_parser.add_argument("num", metavar="N", nargs=1, type=int, help="The number for which to find a relativley prime number")

args = parser.parse_args()

args.func(args)
