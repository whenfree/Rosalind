#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse
__author__ = 'menghao'
__mail__ = 'haomeng@genome.cn'

bindir = os.path.abspath(os.path.dirname(__file__))
pat1 = re.compile('')


def read_fasta(seq):
    Dict = {}
    with open(seq) as IN:
        for line in IN:
            line = line.rstrip()
            if line.startswith('>'):
                name = line[1:]
                if name not in Dict:
                    Dict[name] = ''
                    continue
            Dict[name] += line.upper()
    return(Dict)


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='author:\t{0}\nmail:\t{1}'.format(__author__, __mail__))
    parser.add_argument('-i', '--input', help='input file', dest='input', required=True)
    #parser.add_argument('-o', '--output', help='output file', dest='output', required=True)
    parser.add_argument('-l', '--overlap_len', help='overlap_len', dest='length', required=True, type=int)
    args = parser.parse_args()

    fasta_dict = read_fasta(args.input)

    for first in fasta_dict:
        for second in fasta_dict:
            if first == second:
                continue
            # if fasta_dict[first][0-args.length:] == fasta_dict[second][0:args.length]:
                # print(first, second)
            if fasta_dict[first].endswith(fasta_dict[second][0:args.length]):
                print(first, second)


if __name__ == "__main__":
    main()
