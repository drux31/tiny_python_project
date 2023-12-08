#!/usr/bin/env python
"""
Author : Landry <contact@lnts.me>
Date   : 2023-12-08
Purpose: Rock the Casbah
"""

import argparse


# ------------------------------------------------------------
def get_args():
    """Get the command line argument"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


# ------------------------------------------------------------
def main():
    """Make a jazz noise here bro"""

    args = get_args()
    print('Hello, ' + args.name + '!')


# ------------------------------------------------------------
if __name__ == '__main__':
    main()
