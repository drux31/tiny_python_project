#!/usr/bin/env python3
"""
Author : drux <contact@lnts.me>
Date   : 2023-12-15
Purpose: morbid poetry
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gaschlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    content = {}
    for line in args.file:
        firstletter = line[0]
        content[firstletter] = line[:-1].rstrip()
    
    for letter in args.letter:
        if letter.upper() in content:
            print(f'{content[letter.upper()]}')
        else:
            print(f'I do not know "{letter}".')
    
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
