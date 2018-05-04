#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'menghao'
__mail__ = 'haomeng@genome.cn'
import os
import re
import sys
import argparse
from collections import Counter
bindir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(bindir + '/../lib')
from common import parser_fasta


def find_common_substring(seq1, seq2):
    if len(seq1) >= len(seq2):
        L_seq = seq1
        S_seq = seq2
        S_length = len(seq2)
    else:
        L_seq = seq2
        S_seq = seq1
        S_length = len(seq1)
    sub_string = []
    sub_len = 2
    while sub_len <= S_length:
        for sub in range(0, S_length-sub_len+1):
            if S_seq[sub:sub+sub_len] in L_seq:
                sub_string.append(S_seq[sub:sub+sub_len])
        sub_len += 1
    return list(set(sub_string))


def main():
    parser = argparse.ArgumentParser(usage='Finding_a_Shared_Motif.py',
                                     description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='author:\t{0}\nmail:\t{1}'.format(__author__, __mail__))
    parser.add_argument('-i', '--input', help='input', dest='input', required=True)
    args = parser.parse_args()

    Fasta = parser_fasta(args.input)

    Seq = list(Fasta.values())

    all_common = []

    for i in range(1, len(Seq)):
        common_substring = find_common_substring(Seq[i-1], Seq[i])
        all_common += common_substring

    sub_string_counts = Counter(all_common)

    shared_string = []

    for string, times in sub_string_counts.items():
        if times == len(Seq) - 1:
            shared_string.append(string)

    longest_shared_string = sorted(shared_string, key=lambda x: len(x), reverse=True)[0]

    print(longest_shared_string)


if __name__ == "__main__":
    main()
