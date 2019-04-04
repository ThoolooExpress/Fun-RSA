import argparse

parser = argparse.ArgumentParser(description="This program does everything!!")

def euclidean(args):
    # Code for each of these questions goes in these funcitons
    # at some point I'll move them to their own files
    # don't worry about that, I'll deal with it
    print("We're in euclidean space now!")
    # Use args.nums for your arguments
    print("{} and {} are the two numbers you put in".format(args.nums[0], args.nums[1]))
    # the command line arguments are in args.nums (list of 2)

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
e_parser.set_defaults(func=euclidean)
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