#!/usr/bin/env python3
"""
Author : drux <contact@lnts.me>
Date   : 2023-12-13
Purpose: Rock the Casbah
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-case input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input String or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    
    if args.outfile:
        filename = args.outfile
        out_fh = open(filename, 'wt')
        out_fh.write(text.upper()+'\n')
        out_fh.close()
    else:
        if os.path.isfile(text):
            print(open(text).read().upper())

        else:
            print(text.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
