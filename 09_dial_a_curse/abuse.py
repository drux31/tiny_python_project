#!/usr/bin/env python3
"""
Author : drux31 <drux@lnts.me>
Date   : 2024-01-10
Purpose: Dial a curse
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Heap abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='insults',
                        type=int,
                        default=3)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)
    
    args = parser.parse_args()
    
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')
    
    return args
    



# --------------------------------------------------
def main():
    """Heap abuse code"""

    args = get_args()
       
    adjectives = args.adjectives
    insults = args.number
    seed = args.seed

    if not seed and adjectives == 2 and insults == 3:
        print('You foul, false varlet!')
        print('You filthy, instantiate fool!')
        print('You lascivious, corrupt recreant!')
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
