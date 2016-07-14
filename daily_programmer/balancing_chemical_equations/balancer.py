import sys
import re
import numpy as np


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



def augment_splits(splits):
    """
    Takes the splits for a tiered molecule and undoes the parens 
        e.g. [Ca, (, O, H, ), 2] => [Ca, O, 2, H]
    """
    end_paren = splits.index(')')
    multiplyer = splits[end_paren + 1]

    start_paren = splits.index('(')
    del l[start_paren]
    i = start_paren
    # TODO FINISH THIS UP
    
    print splits

def molecule_to_vector(molecule, attributes, multiplyer = 1):
    """
    Takes a molecule (e.g. Al3O) and converts it into a vector using the given attribute mapping
    """
    v = np.zeros(len(attributes))    
    
    mol_freq_splits = re.findall('[A-Z][a-z]?|\\(|\\)|\d+', molecule)
    # TODO FINISH PAREN PARSING
    #if '(' in mol_freq_splits:
    #    augment_splits(mol_freq_splits)
    num_splits = len(mol_freq_splits)   # len() is O(1) so this is for readability

    i = 0
    while i < num_splits:
        element = mol_freq_splits[i]
        count = '1'
        if i < num_splits - 1 and mol_freq_splits[i + 1].isdigit():
            count = mol_freq_splits[i + 1]
            i += 1
        v[attributes.index(element)] += int(count)
        i += 1

    return v * multiplyer
            

def parse_equation(equation):
    """
    Takes a string representation of a chemical equation and parses it into the following matrix representation:
        -Each molecule is represented by a column
        -Each element type is a single dimension within these columns
        -Element frequencies are the matrix entries
        
    E.g.
        Al + Fe2O4 -> Fe + Al2O3
       (m1)   (m2)   (m3)   (m4)
               yeilds
            m1 m2 m3 m4  
        Al  [1  0  0  2] 
        Fe  [0  2  1  0]
         O  [0  4  0  3]
    """
    matrix = None
    # get element-attribute mapping
    attributes = re.findall('[A-Z][a-z]?', equation)
    attributes = list(set(attributes))                       # get rid of diplicates
    molecules = re.findall('\w*\\(?\w+\\)?\w*', equation)    #\w == [A-Za-z0-9]

    for m in molecules:
        v = molecule_to_vector(m, attributes)
        matrix = insert_col(matrix, v)
    return matrix


input = open(sys.argv[1]).read().split('\n')
for equation in input:
    print equation
    print parse_equation(equation)
