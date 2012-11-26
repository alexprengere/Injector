#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This module injects delimiters into a positional
data feed.
'''

import argparse


DEF_SHIFT     = 0
DEF_DELIMITER = '^'

def handle_args():
    '''Command line parsing.
    '''
    parser = argparse.ArgumentParser(description='Inject delimiter in positional data feed.')

    parser.add_argument('flow',
        help = '''Path to the file containing the data. If set to
                       "-", the script will read the standard input
                        instead.''',
        type = argparse.FileType('r'),
        default = '-'
    )

    parser.add_argument('-r', '--reverse',
                        help = '''Reverse injection, will remove delimiter and
                        use positional fields instead. Using this tool first in normal
                        mode, then in reverse modei, with the exact same options, should be
                        an identity for the file.''',
                        action = 'store_true')

    parser.add_argument('-n', '--no-spaces',
                        help = '''Strip all field spaces when injecting delimiters.''',
                        action = 'store_true')

    parser.add_argument('-s', '--shift',
                        help = '''Specify start point for counting indices.
                        Default is %s.''' % DEF_SHIFT,
                        type = int,
                        default = DEF_SHIFT)

    parser.add_argument('-d', '--delimiter',
                        help = '''Specify delimiter. Default is %s.''' % DEF_DELIMITER,
                        default = DEF_DELIMITER)

    parser.add_argument('-i', '--indices',
                        help = '''Indices for injection. Accepts n arguments separated by
                        spaces, like -i 2 3 7.''',
                        type = int,
                        nargs = '+',
                        default = [])

    parser.epilog = 'Example: head example.pos | %s - -i 7 15 23' % parser.prog

    return vars(parser.parse_args())


def inject(flow, delimiter, shift, indices, strip):
    '''
    Inject
    '''
    for row in flow:
        row = list(row.rstrip())

        for i in sorted(indices, reverse=True):
            row.insert(i - shift, delimiter)

        row = ''.join(row)

        if not strip:
            print row
        else:
            print delimiter.join(f.strip() for f in row.split(delimiter))


def position(flow, delimiter, shift, indices):
    '''
    Position
    '''
    for row in flow:

        new_row = []
        ind = [shift] + indices

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

    flow      = args['flow']
    delimiter = args['delimiter']
    shift     = args['shift']
    indices   = args['indices']
    strip     = args['no_spaces']

    if args['reverse']:
        position(flow, delimiter, shift, indices)
    else:
        inject(flow, delimiter, shift, indices, strip)


if __name__ == '__main__':

    main()
