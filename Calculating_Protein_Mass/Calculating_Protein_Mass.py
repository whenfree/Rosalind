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


class Parser():
    def __init__(self, table):
        self.table = table
        self.parser_table()

    def parser_table(self):
        Dict = {}
        with open(self.table) as IN:
            for line in IN:
                if line.startswith('#') or re.search(pat1, line):
                    continue
                tmp = line.rstrip().split()
                Dict[tmp[0]] = float(tmp[1])
        self.Dict = Dict


def main():
    parser = argparse.ArgumentParser(usage='Calculating_Protein_Mass.py',
                                     description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='author:\t{0}\nmail:\t{1}'.format(__author__, __mail__))
    parser.add_argument('-i', '--input', help='input file', dest='input', required=True)
    parser.add_argument('-t', '--table', help='monoisotopic mass table', dest='table', default=os.path.join(os.getcwd(), 'monoisotopic_mass_table.txt'))
    args=parser.parse_args()

    Table=Parser(args.table)

    Mass = Table.Dict

    AA = open(args.input).read().rstrip('\n')

    Sum = 0
    for i in AA:
        Sum += Mass[i]
    print(round(Sum,3))



if __name__ == "__main__":
    main()
