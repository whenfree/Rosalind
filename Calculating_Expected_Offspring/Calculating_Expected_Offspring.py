#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse
__author__ = 'menghao'
__mail__ = 'haomeng@genome.cn'

with open(sys.argv[1]) as IN:
    Nums = IN.readline().split(' ')

F = [float(i) for i in Nums]

R = 1*2*(F[0]+F[1]+F[2]) + 0.75*2*F[3] + 0.5*2*F[4]

print(R)
