import sys
import os
import re
import numpy as np
# get some of my matrix operations
sys.path.append('../linear_algebra')
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


def vector_to_equation(v, equation):
    """
    Takes a vector of molecule multiplyers 
    returns a series of equations, one per column of X
    """
    # negate reactant components of v
    num_reactants = equation.split('->')[1].count('+') + 1
    for i in range(num_reactants):
        v[::-1][i] = -v[::-1][i]

    equation_splits = re.findall('\w+|->', equation)
    v_index = 0
    i = 0
    s = ''
    # loop through molecules and apply the right multiplyer to each one
    while i < len(equation_splits):
        molecule = equation_splits[i]
        if molecule == '->':
            s += ' %s ' % molecule
            i += 1
            continue
        j = 0
        molecule_splits = re.findall('[A-Z][a-z]?|\d+', molecule)

        # apply multiplyer to each element of this molecule
        while j < len(molecule_splits):
            element = molecule_splits[j]
            count = '1'
            if j < len(molecule_splits) - 1 and molecule_splits[j + 1].isdigit():
                count = molecule_splits[j + 1]
                j += 1
            new_amount = round(int(count) * v[v_index], 2)
            s += '%s%s' % (element, new_amount)
            j += 1
        s += ' ' 
        i += 1
        v_index += 1
    return s


def decode_nullspace(N, equation):
    num_reactants = equation.split('->')[0].count('+') + 1
    attributes = attributes_from_equation(equation)
    molecules = molecules_from_equation(equation)
    # if we only got 1 nullspace vector, convert it right away
    if len(N.shape) == 1:
        return [vector_to_equation(N, equation)]

    # otherwise decode each nullspace vector 
    solutions = []
    for nullspace_vector in N:
        solutions.append(vecto_to_equation(nullspace_vector, equation))
    return solutions
            
if len(sys.argv) < 2:
    equations = [raw_input("No input file specified. Enter equation here: ")]
else:
    input = open(sys.argv[1]).read()
    equations = [x.strip() for x in input.split('\n')]

for equation in equations:
    M = parse_equation(equation)
    N = LinAlg.nullspace(M)
    print "working on this equation:"
    print equation 
    print "solutions:"
    results = decode_nullspace(N, equation)
    for result in results:
        print result
    print '\n'
