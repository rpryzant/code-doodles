import sys
import re
import numpy as np

def get_dimensions(molecules):
    """
    Takes some molecules and assigns a number [0, inf) to each unique element in this group
    """
    l = []
    for m in molecules:
        elements = re.findall('[^0-9]+', m)
        for element in elements:
            if element not in l:
                l.append(element)
    return l
                


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
    # get element-attribute mapping

    # 
    
    molecules = [molecule.strip() for formula in equation.split('->') for molecule in formula.split('+')]
    attributes = get_dimensions(molecules)

    for m in molecules:
        v = molecule_to_vector(m, attributes)
                                
input = open(sys.argv[1]).read().split('\n')
for equation in input:
    parse_equation(equation)
