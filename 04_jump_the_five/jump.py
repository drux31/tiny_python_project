#!/usr/bin/env python3
"""
Author : drux <contact@lnts.me>
Date   : 2023-12-11
Purpose: Jump the five bro
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Jump the five here bro"""

    args = get_args()
    str = args.str
    jumper = dict([('1', '9'), ('2', '8'), ('3', '7'), 
                   ('4', '6'), ('5', '0'), ('6', '4'), 
                   ('7', '3'), ('8', '2'), ('9', '1'), 
                   ('0', '5')])
    newstr = ''

    for char in str:
        newstr = newstr + jumper.get(char, char)
    print (newstr)


# --------------------------------------------------
if __name__ == '__main__':
    main()
