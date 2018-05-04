#!/usr/bin/env python3
import argparse

'''
Computing GC Content of a given DNA sting.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''

seq = {}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-s', '--seq', help='fasta file', dest='seq', required=True, type=open)
    args = parser.parse_args()
    for i in args.seq:
        i = i.rstrip()
        if i.startswith(">"):
            seqName = i[1:]
            seq[seqName] = ''
            continue
        seq[seqName] += i.upper()
    for key, value in seq.items():
        length = len(value)
        gc_content = value.count('G')+value.count('C')
        per = gc_content/length*100
        seq[key] = per
        print(key, " GC Content is ", per, "%")
    max_gc = max(seq, key=lambda k: seq[k])
    print('The max GC content is {0}: {1:.2f}%'.format(max_gc, seq[max_gc]))


if __name__ == "__main__":
    main()
