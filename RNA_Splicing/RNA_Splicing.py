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
from dna2rna import dna2rna
from rna2protein import rna2protein
from parser_fasta import Parser_fasta


def main():
    parser = argparse.ArgumentParser(usage='RNA_Splicing.py',
                                     description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='author:\t{0}\nmail:\t{1}'.format(__author__, __mail__))
    parser.add_argument('-f', '--fasta', help='fasta file', dest='fasta', required=True)
    parser.add_argument('-o', '--output', help='output file', dest='output', required=True)
    args = parser.parse_args()

    fasta = Parser_fasta(args.fasta)
    Seq = fasta.fasta_list()

    preRNA = []
    [preRNA.append(dna2rna(seq)) for seq in Seq]

    delimiters = '|'.join(preRNA[1:])

    mRNA = ''.join(re.split(delimiters,preRNA[0]))

    Protein = rna2protein(mRNA)

    print(Protein)

    with open(args.output,'w') as OUT:
        OUT.write(Protein + '\n')

if __name__ == "__main__":
    main()
