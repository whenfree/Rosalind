#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse
__author__ = 'menghao'
__mail__ = 'haomeng@genome.cn'


def rabbits(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return rabbits(n-1, k) + k*rabbits(n-2, k)


print(rabbits(33, 5))
