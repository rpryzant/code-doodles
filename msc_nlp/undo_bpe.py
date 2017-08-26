# -*- coding: utf-8 -*-                                                                                                                                                  
# undoes a bpe word encoding
# python undo_bpe.py input > output


import sys


for l in open(sys.argv[1]):
    l = l.strip().split()
    print ''.join(l).replace('_', ' ').replace('▁', ' ').strip()



