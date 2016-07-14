import sys
import os
import re
import numpy as np
# get some of my matrix operations
sys.path.append('../../linear_algebra')
from LinAlg import LinAlg
from Matrix import insert_col, insert_row

def attributes_from_equation(equation):
    """
    Takes a chemical equation and produces a mapping from elements to attribute number
    """
    a = re.findall('[A-Z][a-z]?', equation)
    return list(set(a))

def molecules_from_equation(equation):
    """
    Unpacks a chemical equation into a list of molecules
    """
    #\w == [A-Za-z0-9]
    return re.findall('\w*\\(?\w+\\)?\w*', equation)

def augment_splits(splits):
    """
    Takes the splits for a tiered molecule and undoes the parens 
        e.g. [Ca, (, O, H, ), 2] => [Ca, O, 2, H, 2]
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
    equation_matrix = None
    attributes = attributes_from_equation(equation)
    molecules = molecules_from_equation(equation)

    for m in molecules:
        v = molecule_to_vector(m, attributes)
        equation_matrix = insert_col(equation_matrix, v)
    return equation_matrix


def vector_to_equation(v, num_reactants, attributes, molecules):
    s = ''
    i = 0
    while i < num_reactants:
        print molecules[i]
        print attributes_from_equation(molecules[i])
        #TODO
#        s += '%s%s' % (attributes[d])
        i += 1


def decode_nullspace(N, equation):
    num_reactants = equation.split('->')[0].count('+') + 1
    attributes = attributes_from_equation(equation)
    molecules = molecules_from_equation(equation)
    # if we only got 1 nullspace vector, convert it right away
    if len(N.shape) == 1:
        return [vector_to_equation(N, num_reactants, attributes, molecules)]

    # otherwise decode each nullspace vector 
    solutions = []
    for nullspace_vector in N:
        solutions.append(vector_to_equation(N, num_reactants, attributes, molecules))
    return solutions
            

input = open(sys.argv[1]).read().split('\n')
for equation in input:
    M = parse_equation(equation)
    N = LinAlg.nullspace(M)
    print equation
    print M
    print N
    print decode_nullspace(N, equation)
