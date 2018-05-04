#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse

seq = ''
with open(sys.argv[1]) as f:
	for line in f:
		line = line.rstrip()
		for i in line:
			if i == 'A':
				seq += 'T'
			elif i == 'T':
				seq += 'A'
			elif i == 'C':
				seq += 'G'
			elif i == 'G':
				seq += 'C'
			else:
				print("ERROR")
rev = ''.join(list(reversed(seq)))
print(rev)
