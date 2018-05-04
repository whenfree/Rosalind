#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse
from scipy.misc import comb
__author__ = 'menghao'
__mail__ = 'haomeng@genome.cn'

bindir = os.path.abspath(os.path.dirname(__file__))
pat1 = re.compile('')

num = input('Please input individuals(k,m,n):')
[k,m,n] = map(int, num.split(','))

total = k + m + n

AA_AA = comb(k, 2)
AA_Aa = k * m
AA_aa = k * n
Aa_Aa = comb(m, 2) * 0.75
Aa_aa = m * n * 0.5
AA_Aa_aa = comb(total, 2)

per = (AA_AA + AA_Aa + AA_aa + Aa_Aa + Aa_aa) / AA_Aa_aa

print('dominant allele percentage: {0:0.5f}'.format(per))
