#!/usr/bin/env python3
"""tests for jump.py"""

import os
from subprocess import getstatusoutput

prg = './encode_str.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_01():
    """test"""

    rv, out = getstatusoutput(f'{prg} 123')
    assert rv == 0
    assert out == 'onetwothree'


# --------------------------------------------------
def test_02():
    """test"""

    rv, out = getstatusoutput(f'{prg} "The correct number is 5072."')
    assert rv == 0
    assert out.rstrip() == 'The correct number is fivezeroseventwo.'
