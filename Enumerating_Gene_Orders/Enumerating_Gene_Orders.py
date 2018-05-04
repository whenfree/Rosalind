#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse
from itertools import permutations


n = 7 #int(input('input: ').rstrip())

perms = list(permutations([i for i in range(1,n+1)]))

print(len(perms))

for perm in perms:
    perm = ' '.join([str(i) for i in perm])
    print(perm)
