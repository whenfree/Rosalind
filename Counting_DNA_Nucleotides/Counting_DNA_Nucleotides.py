#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys

'''
Problem

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string ss of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in ss.
'''

dict = {}

with open (sys.argv[1]) as f:
	for line in f:
		line = line.rstrip()
		for i in line:
			dict[i] = dict.get(i,0) + 1
	print(dict['A'],dict['C'],dict['G'],dict['T'])
    
