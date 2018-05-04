#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse
__author__ = 'menghao'
__mail__ = 'haomeng@genome.cn'


# The answer was copyed from web.

# R(n,m) = R(n-1) + R(n-2) - R(n-(m+1))

def rabbit_pairs(n, m):
    sequence = list()
    for i in range(n):
        if i < 2:
            # Normal Fibonacci initialization
            total = 1
            sequence.append(total)
        elif (i < m) or (m == 0):
            # Normal Fibonacci calculation
            total = sequence[i - 1] + sequence[i - 2]
            sequence.append(total)
        elif i == m:
            # Now we need R(n - (m + 1)), but i - (m + 1) < 0, so we have to
            # provide the missing value
            total = sequence[i - 1] + sequence[i - 2] - 1
            sequence.append(total)
        else:
            # i - (m + 1) >= 0, so we can get the value from the sequence
            total = sequence[i - 1] + sequence[i - 2] - sequence[i - (m + 1)]
            sequence.append(total)
    return total

print(rabbit_pairs(87,18))
