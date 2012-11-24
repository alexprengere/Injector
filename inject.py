#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This module injects delimiters into a positional
data feed.
'''

from sys import stdin
import argparse


DEF_SHIFT     = 0
DEF_DELIMITER = '^'

def handle_args():
    '''Command line parsing.
    '''
    parser = argparse.ArgumentParser(description='Inject delimiter in positional data feed.')

    parser.add_argument('-r', '--reverse',
                        help = '''Reverse injection.''',
                        action = 'store_true')

    parser.add_argument('-n', '--no-spaces',
                        help = '''Strip all spaces.''',
                        action = 'store_true')

    parser.add_argument('-s', '--shift',
                        help = '''Specify start point for counting positions.''',
                        type = int,
                        default = DEF_SHIFT)

    parser.add_argument('-d', '--delimiter',
                        help = '''Specify delimiter.''',
                        default = DEF_DELIMITER)

    parser.add_argument('-i', '--indices',
                        help = '''Indices for injection.''',
                        type = int,
                        nargs = '+',
                        default = [])

    parser.epilog = 'Example: head example.pos | %s -i 7 15 23' % parser.prog

    return vars(parser.parse_args())


def inject(delimiter, shift, indices, strip):
    '''
    Inject
    '''
    for row in stdin:
        row = list(row.rstrip())

        for i in sorted(indices, reverse=True):
            row.insert(i + shift, delimiter)

        row = ''.join(row)

        if not strip:
            print row
        else:
            print delimiter.join(f.strip() for f in row.split(delimiter))


def position(delimiter, indices):
    '''
    Position
    '''
    for row in stdin:

        new_row = []
        ind = [0] + indices

        for i, field in enumerate(row.split(delimiter)):

            if i + 1 < len(ind):
                width = ind[i + 1] - ind[i]
                printer = '%%-%ss' % width

            else:
                printer = '%s'

            new_row.append(printer % field)

        print ''.join(new_row),



def main():
    '''Main.
    '''
    args = handle_args()

    delimiter = args['delimiter']
    shift     = args['shift']
    indices   = args['indices']
    strip     = args['no_spaces']

    if args['reverse']:
        position(delimiter, indices)
    else:
        inject(delimiter, shift, indices, strip)


if __name__ == '__main__':

    main()