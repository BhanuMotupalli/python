"""This is for calculation

Module contains
add
sub
mul
div
mod

usage:
Python calc.py add 1 and 2
"""

import sys


class Invalidargs(Exception):
    pass

def main(args):
    if len(args) != 3:
        raise Invalidargs
    operation = args[0]
    temp_args = args[1:]
    args = [ int(arg) for arg in temp_args]
    if operation.lower() == 'add':
        print(args[0] + args[1])
    elif operation.lower() == 'sub':
        print(args[0] - args[1])
    elif operation.lower() == 'mul':
        print(args[0] * args[1])
    elif operation.lower() == 'div':
        print(args[0] // args[1])
    elif operation.lower() == 'mod':
        print(args[0] % args[1])
    else:
        print("Unsupported operation")


if __name__ == '__main__':
    args = sys.argv[1::]
    try:
        main(args)
    except Invalidargs:
        print("Usage is as shown below")
        print("Python calc.py add 1 and 2")