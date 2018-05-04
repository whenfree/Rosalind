#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse
import numpy as np
from collections import defaultdict,Counter
__author__ = 'menghao'
__mail__ = 'haomeng@genome.cn'

bindir = os.path.abspath(os.path.dirname(__file__))
pat1 = re.compile('^\s*$')

def parser_fasta(fasta):
    seq = []
    Dict = defaultdict(list)
    with open(fasta) as IN:
        for line in IN:
            if line.startswith('>'):
                name = line.rstrip()[1:]
                continue
            Dict[name] += line.rstrip()
    for i in Dict:
        seq.append([j for j in Dict[i]])
    return np.array(seq)


def main():
    parser = argparse.ArgumentParser(usage='Consensus_and_Profile',
                                     description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='author:\t{0}\nmail:\t{1}'.format(__author__, __mail__))
    parser.add_argument('-i', '--input', help='input', dest='input', required=True)
    args = parser.parse_args()

    seq = parser_fasta(args.input)

    Dict = defaultdict(list)
    consensus = ''

    for i in range(seq.shape[1]):
        total = Counter(seq[:,i])
        consensus += total.most_common(1)[0][0]
        for c in ('A', 'C', 'T', 'G'):
            Dict[c].append(str(total[c]))

    print(consensus)

    for c in ('A', 'C', 'T', 'G'):
        print('{0}: {1}'.format(c,' '.join(Dict[c])))


if __name__ == "__main__":
    main()
