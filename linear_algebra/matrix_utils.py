import numpy as np


"""
This file gives a whole bunch of matrix/numpy array utility functions

"""
def insert_col(m, c):
    if m is None:
        return c
    else:
        return np.c_[m, c]


def insert_row(m, r):
    if m is None:
        return r
    else:
        return np.r_[m, [r]]


def first_nonzero_in_row(r):
    return next((i for i, x in enumerate(r) if x != 0), None)

def last_nonzero_in_row(r):
    return [i for i, x in enumerate(r) if x != 0][-1]

def first_zero_in_row(r):
    return next((i for i, x in enumerate(r) if x == 0), None)
    
