#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re, sys, argparse
bindir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(bindir + '/../lib')
from parser_fasta import Parser_fasta

fasta = Parser_fasta(sys.argv[1])
Seq1 = fasta.fasta_list()[0]
Seq2 = fasta.fasta_list()[1]

trans = ['AG','GA','CT','TC']
tranv = ['AC','AT','GC','GT','CA','CG','TA','TG']

trans_num, tranv_num = 0, 0

length = len(Seq1)

for i in range(length):
    link = Seq1[i] + Seq2[i]
    if  Seq1[i] == Seq2[i]:
        continue
    if link in trans:
        trans_num += 1
    elif  link in tranv:
        tranv_num += 1
    else:
        sys.stderr.write('Wrong\n')
        sys.exit(1)

ratio = trans_num/tranv_num
print(ratio)
