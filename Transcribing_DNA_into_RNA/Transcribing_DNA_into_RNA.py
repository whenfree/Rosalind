#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys


'''
DNA to RNA
An RNA string is formed from the alphabet containing A, C, G, and U.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of T with U.
Given: A DNA string t of length at most 1000 nucleotides.
Return: The transcribed RNA string of t.
Sample Dataset
GATGGAACTTGACTACGTAAATT
Sample Output
GAUGGAACUUGACUACGUAAAUU
'''

with open(sys.argv[1]) as f:
	for line in f:
		line = line.strip()
		rna = line.replace('T','U')
		print(rna)

