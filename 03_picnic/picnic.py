#!/usr/bin/env python3
"""
Author : drux <contact@lnts.me>
Date   : 2023-12-10
Purpose: go to the picnic with enough supplies
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('str', 
                    nargs='+',
                    metavar='str',
                    help='Item(s) to bring')
    
    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.str

    if args.sorted:
        items.sort()

    ln = len(items)
    baseStr = "You are bringing"

    if ln == 1:
        print(f'{baseStr} {items[0]}.')
    elif ln == 2:
        end = ' and '.join(items)
        print (f'{baseStr} {end}.')
    else:
        end = 'and ' + items[-1]
        middle = ', '.join(items[0:ln-1])
        print (f'{baseStr} {middle}, {end}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
