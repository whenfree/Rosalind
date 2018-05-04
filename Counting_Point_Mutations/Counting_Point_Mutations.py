#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse
__author__ = 'menghao'
__mail__ = 'haomeng@genome.cn'

bindir = os.path.abspath(os.path.dirname(__file__))
pat1 = re.compile('^\s*$')


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='author:\t{0}\nmail:\t{1}'.format(__author__, __mail__))
    parser.add_argument('-i', '--input', help='input file', dest='input', required=True)
    args = parser.parse_args()

    seq = []
    with open(args.input) as IN:
        for line in IN:
            if line.startswith('#') or re.search(pat1,line):
                continue
            seq.append(line.rstrip())

    mut = 0
    if len(seq[0]) == len(seq[1]):
        for i in range(0,len(seq[0])):
            if (seq[0][i].upper() in ['A', 'T', 'G', 'C']) & (seq[1][i].upper() in ['A', 'T', 'G', 'C']):
                if seq[0][i] != seq[1][i]:
                    mut +=1
            else:
                sys.stderr.write('wrong!\n')
                sys.exit(1)

    print('Mutation Numbers: {0}'.format(mut))



if __name__ == "__main__":
    main()
