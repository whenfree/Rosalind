#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse
from urllib import request
__author__ = 'menghao'
__mail__ = 'haomeng@genome.cn'

bindir = os.path.abspath(os.path.dirname(__file__))
pat1 = re.compile('^\s*$')


def url(url):
    response = request.urlopen(url)
    return response.read().decode('utf-8')


def parser_aa(aa_id):
    uniprot_url = 'http://www.uniprot.org/uniprot/' + aa_id + '.fasta'
    aa_seq = url(uniprot_url)
    Seq = {}
    for line in aa_seq.split('\n'):
        if line.startswith('>'):
            continue
        if aa_id not in Seq:
            Seq[aa_id] = ''
        Seq[aa_id] += line
    return Seq


def main():
    parser = argparse.ArgumentParser(usage='Finding_a_Protein_Motif',
                                     description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='author:\t{0}\nmail:\t{1}'.format(__author__, __mail__))
    parser.add_argument('-i', '--input', help='UniProt Protein Database access IDs, one per line', dest='input', required=True)
    parser.add_argument('-o', '--output', help='output file', dest='output', required=True)
    args = parser.parse_args()

    motif = re.compile('N[^P][ST][^P]')
    length = 4

    with open(args.input) as IN, open(args.output, 'w') as OUT:
        for line in IN:
            index = []
            aa_seq = parser_aa(line.rstrip())
            for i, j in enumerate(aa_seq[line.rstrip()]):
                if motif.search(aa_seq[line.rstrip()][i:i+length]):
                    index.append(i + 1)
            if index:
                OUT.write(line.rstrip() + '\n' + ' '.join([str(i) for i in index]) + '\n')


if __name__ == "__main__":
    main()
