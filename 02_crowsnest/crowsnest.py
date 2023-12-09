#!/usr/bin/env python3
"""
Author : drux <contact@lnts.me>
Date   : 2023-12-09
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word')
    #parser.print_help()
    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here bro"""

    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'  
    
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')

# --------------------------------------------------
if __name__ == '__main__':
    main()
