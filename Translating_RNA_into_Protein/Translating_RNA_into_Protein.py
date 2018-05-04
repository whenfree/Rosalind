#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse

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

IN = open(sys.argv[1])
Seq = IN.read().rstrip()
IN.close()

Protein = ''

for i in range(0,len(Seq),3):
    if Seq[i:i+3] in RNA2Protein:
        if RNA2Protein[Seq[i:i+3]] == 'Stop':
            break
        Protein += RNA2Protein[Seq[i:i+3]]

print(Protein)
