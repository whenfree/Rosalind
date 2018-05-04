#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse
from collections import defaultdict


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

Freq = {}

for k,v in RNA2Protein.items():
    Freq[v] = Freq.get(v,0) + 1

IN = open(sys.argv[1])
Seq = IN.read().rstrip()
IN.close()

times = Freq['Stop']

for aa in Seq:
    times *= Freq[aa]

print(times % 1000000)
