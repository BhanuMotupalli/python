"""This is to find new calculator
Modules
add
sub
mul
div
mod

Usage: 
Python newcalc.py add 1 2
"""

import argparse



def create_parser():
    parser = argparse.ArgumentParser (
        prog= 'Calculator',
        description= 'This contains basic calculations add sub mul div mod'
    )
    parser.add_argument('operation', choices=['add', 'sub', 'mul','div', 'mod'], help="Operation to perform: add, sub, mul, div, mod", )
    parser.add_argument('value1', type=int, help='First number')
    parser.add_argument('value2', type=int, help='Second number')
    return parser

def Operate(args):
    if args.operation == 'add':
        print(args.value1 + args.value2)
    elif args.operation == 'sub':
        print(args.value1 - args.value2)
    elif args.operation == 'mul':
        print(args.value1 * args.value2)
    elif args.operation == 'div':
        print(args.value1 // args.value2)
    elif args.operation == 'mod':
        print(args.value1 % args.value2)
    else:
        print("Unsupported operation")

def main():
    parser = create_parser()

    args = parser.parse_args()

    Operate(args)


    
if __name__ == '__main__':
    main()