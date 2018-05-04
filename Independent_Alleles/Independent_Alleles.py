#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse
from scipy import stats

'''
Given: Two positive integers k (k≤7) and N (N≤2**k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least NN Aa Bb organisms will belong to the kk-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

核心：二项式分布
'''

k,N = map(int,input('input k and N: ').split())

n = 2 ** k

p_sum = 0

for i in range(N,n+1):
    p = stats.binom.pmf(i,n,0.25)
    p_sum += p

print('Pro:',round(p_sum,3))

