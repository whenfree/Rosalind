#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse
__author__ = 'menghao'
__mail__ = 'haomeng@genome.cn'


IN = open(sys.argv[1])
Seq = open(sys.argv[1]).read().split()
IN.close()

String = Seq[0]
Sub = Seq[1]

#方法1
[print(i.start() + 1, end = ' ') for i in re.finditer('(?={0})'.format(Sub), String)]
print('\n' + '-'*20)
#方法2
[print(i + 1) for i in range(len(String)) if String.startswith(Sub,i)]
print('-'*20)
#方法3：
[print(i + 1) for i,j in enumerate(String) if String[i:(i+len(Sub))] == Sub]
print('-'*20)

#方法4：
def find_all(string, sub):
    start = 0
    while True:
        start = string.find(Sub, start)
        if start == -1:
            return
        yield start
        start += 1

[print(i + 1) for i in find_all(String, Sub)]
