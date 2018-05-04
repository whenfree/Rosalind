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
sys.path.append(bindir + '/../lib')
from common import parser_fasta

complement = {'A':'T','T':'A','C':'G','G':'C'}

def main():
    parser = argparse.ArgumentParser(usage='Locating_Restriction_Sites',
                                     description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='author:\t{0}\nmail:\t{1}'.format(__author__, __mail__))
    parser.add_argument('-f', '--fasta', help='fasta format file', dest='fasta', required=True)
    args = parser.parse_args()

    Seq = parser_fasta(args.fasta).values()[0]

    rev_com = ''.join([complement[i] for i in Seq])

    for index in range(0,len(Seq)):
        for length in range(4,13):
            sub = Seq[index:index+length]
            if (4<=len(sub)<=13) & (length == len(sub)):
                rev_com = ''.join([complement[i] for i in reversed(sub)])
                if sub == rev_com:
                    print(str(index+1) + ' ' + str(length))

if __name__ == "__main__":
    main()
