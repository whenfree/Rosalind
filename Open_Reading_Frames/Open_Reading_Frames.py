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


'''
ORF: must start by start codon, end by end codon. line:72
'''

RNA2Protein = {
'UUU':'F','CUU':'L','AUU':'I','GUU':'V','UUC':'F','CUC':'L',
'AUC':'I','GUC':'V','UUA':'L','CUA':'L','AUA':'I','GUA':'V',
'UUG':'L','CUG':'L','AUG':'M','GUG':'V','UCU':'S','CCU':'P',
'ACU':'T','GCU':'A','UCC':'S','CCC':'P','ACC':'T','GCC':'A',
'UCA':'S','CCA':'P','ACA':'T','GCA':'A','UCG':'S','CCG':'P',
'ACG':'T','GCG':'A','UAU':'Y','CAU':'H','AAU':'N','GAU':'D',
'UAC':'Y','CAC':'H','AAC':'N','GAC':'D','CAA':'Q','UGG':'W',
'AAA':'K','GAA':'E','CAG':'Q','AAG':'K','GAG':'E','CGG':'R',
'UGU':'C','CGU':'R','AGU':'S','GGU':'G','UGC':'C','CGC':'R',
'AGC':'S','GGC':'G','CGA':'R','AGA':'R','GGA':'G','AGG':'R',
'GGG':'G','UAG':'Stop','UGA':'Stop','UAA':'Stop'}

complement = {'A':'T','T':'A','G':'C','C':'G'}

def parser_seq(fasta):
    seq = ''
    with open (fasta) as IN:
        for line in IN:
            if line.startswith('>'):
                continue
            seq += line.rstrip()
    return seq


def main():
    parser = argparse.ArgumentParser(usage='Open_Reading_Frames',
                                     description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='author:\t{0}\nmail:\t{1}'.format(__author__, __mail__))
    parser.add_argument('-i', '--input', help='input file', dest='input', required=True)
    parser.add_argument('-o', '--output', help='output file', dest='output', required=True)
    args = parser.parse_args()


    DNA_string = parser_seq(args.input)
    reversed_DNA_string = ''.join(reversed([complement[i] for i in DNA_string]))

    RNA_string_1 = DNA_string.replace('T','U')
    RNA_string_2 = reversed_DNA_string.replace('T','U')

    AA_Total = set()

    for string in [RNA_string_1,RNA_string_2]:
        for j in range(0,len(string)-2):
            if string[j:j+3] == 'AUG':
                Start2End = string[j:]
                AA_str = ''
                stop = 'F'
                for i in range(0,len(Start2End)-2,3):
                    if RNA2Protein[Start2End[i:i+3]] == 'Stop':
                        stop = 'T'
                        break
                    AA_str += RNA2Protein[Start2End[i:i+3]]
                if stop == 'T':
                    AA_Total.add(AA_str)

    with open(args.output,'w') as OUT:
        [OUT.write(i + '\n') for i in AA_Total]



if __name__ == "__main__":
    main()
