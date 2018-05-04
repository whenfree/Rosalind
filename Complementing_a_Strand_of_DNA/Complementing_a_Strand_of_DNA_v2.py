#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse

pair = {'A':'T','T':'A','C':'G','G':'C'}
seq = []
with open(sys.argv[1]) as f:
	for line in f:
		line = line.rstrip()
		seq = [pair[i] for i in line]
rev = ''.join(list(reversed(seq)))
print(rev)

