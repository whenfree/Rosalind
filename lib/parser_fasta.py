#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict


def parser_fasta(fasta):
    Dict = {}
    with open(fasta) as IN:
        for line in IN:
            line = line.rstrip()
            if line.startswith('>'):
                name = line[1:]
                if name not in Dict:
                    Dict[name] = ''
                    continue
            Dict[name] += line.upper()
    return Dict


class Parser_fasta():
    def __init__(self, fasta):
        self.fasta = fasta

    def fasta_Dict(self):
        Dict = OrderedDict()
        with open(self.fasta) as IN:
            for line in IN:
                line = line.rstrip()
                if line.startswith('>'):
                    name = line[1:]
                    if name not in Dict:
                        Dict[name] = ''
                        continue
                Dict[name] += line.upper()
        #self.flag_and_seq = Dict
        return Dict

    def fasta_list(self):
        seq = []
        for key, value in self.fasta_Dict().items():
            seq.append(value)
        #self.seq_only = seq
        return seq
