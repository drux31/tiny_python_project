#!/usr/bin/env python3
"""
Author : drux <contact@lnts.me>
Date   : 2023-12-14
Purpose: custom word count
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin],
                        help='Input files(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
    args = get_args()
       
    for fh in args.file:
        #variable
        nbBbytes = 0
        nbWords = 0
        nbLines = 0
        for line in fh:
            nbLines +=1
            nbWords += len(line.split(' '))
            nbBbytes += len(line)
        print('{:8}'.format(nbLines) + '{:8}'.format(nbWords) + '{:8}'.format(nbBbytes)+ f' {fh.name}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
