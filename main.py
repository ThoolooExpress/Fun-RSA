import argparse
# import math
from includes.euclidean import xgcd
from includes.prime import rp
from includes.inverse import inverse

parser = argparse.ArgumentParser(description="Oh wow, somebody actually bothered to generate this man page, good job!")

def euclidean(args):
    g, x, y = xgcd(args.nums[0], args.nums[1])
    print("GCD: {}, c1: {}, c2: {}".format(g, x, y))

def modular(args):
    dividend = args.dividend[0]
    divisor = args.divisor[0]
    res = abs(dividend % divisor)
    print("{} % {} = {}".format(dividend, divisor, res))

def relativelyPrime(args):
    print("{} is relatively prime with {}".format(rp(args.num[0]), args.num[0]))
    

def inv(args):
    x = inverse(args.nums[0], args.nums[1])
    if x:
        print("Inverse modulus is: {}".format(x))
    else:
        print("The two numbers are not relatively prime")

def rsa(args):
    print("Oh look, the only function that actually matters")


subparsers = parser.add_subparsers() # Ugh... this is really complicated...

e_parser = subparsers.add_parser("euclidean", help="Run question 1: Implement Euclidean Algorithm for calculating greatest common divisor")
e_parser.set_defaults(func=euclidean)
m_parser = subparsers.add_parser("modular", help="Run question 2: Modulus function")
m_parser.set_defaults(func=modular)
p_parser = subparsers.add_parser("RP", help="Run question 3: Find Relatively Prime")
p_parser.set_defaults(func=relativelyPrime)
i_parser = subparsers.add_parser("inverse", help="Run question 4: Find Inverse")
i_parser.set_defaults(func=inv)
r_parser = subparsers.add_parser("rsa", help="Run question 5: Practice with RSA algorithm")
r_parser.set_defaults(func=rsa)

# e_parser

e_parser.add_argument("nums", metavar="N", type=int, nargs=2, help="The two numbers for which to find the greatest common divisor")

# m_parser
m_parser.add_argument("dividend", metavar="A", type=int, nargs=1, help="The dividend for the modulus function")
m_parser.add_argument("divisor", metavar="B", type=int, nargs=1, help="The divisor for the modulus function")

# p_parser
p_parser.add_argument("num", metavar="N", nargs=1, type=int, help="The number for which to find a relatively prime number")

# i_parser
i_parser.add_argument("nums", metavar="N",type=int, nargs=2, help="The two numbers for which to find the inverse modulo")

args = parser.parse_args()

args.func(args)
