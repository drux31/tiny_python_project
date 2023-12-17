#!/usr/bin/env python3
"""
Author : drux <contact@lnts.me>
Date   : 2023-12-17
Purpose: Apples and bananas
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        default='a',
                        choices=list('aeiou'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    v_upper = vowel.upper()

    trans = {'a':vowel, 'e': vowel, 'u': vowel, 'o': vowel, 'i': vowel,
             'A':v_upper, 'E': v_upper, 'U': v_upper, 'O': v_upper, 'I': v_upper}
    
    if os.path.isfile(text):
        fh = open(text, 'rt')
        for line in fh:
            new = line.translate(str.maketrans(trans))
            print(new)
    else:
        new = text.translate(str.maketrans(trans))
        print(new)

# --------------------------------------------------
if __name__ == '__main__':
    main()
