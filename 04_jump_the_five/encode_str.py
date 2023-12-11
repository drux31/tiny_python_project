#!/usr/bin/env python3
"""
Author : drux <contact@lnts.me>
Date   : 2023-12-11
Purpose: Encode number into string
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Encode Numbers with String',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str = args.str
    encode = dict([('1', 'one'), ('2', 'two'), ('3', 'three'), 
                   ('4', 'four'), ('5', 'five'), ('6', 'six'), 
                   ('7', 'seven'), ('8', 'eight'), ('9', 'nine'), 
                   ('0', 'zero')])

    new_str = ''
    for char in str:
        new_str = new_str + encode.get(char, char)
    print(new_str)

# --------------------------------------------------
if __name__ == '__main__':
    main()
