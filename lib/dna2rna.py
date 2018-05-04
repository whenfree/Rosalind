#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re
import sys
import argparse


def dna2rna(dna):
    rna = dna.replace('T','U')
    return rna
