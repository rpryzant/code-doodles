## What does this program do?

This program automatically balences chemical equations. 

## What is a chemical equation?

This is a chemical equation:

 * You have some number of *reactant* molecules, each consisting of one or more elements
 * You also have some number of molecules that are *products* of the reaction
 * Each molecule consists of some number of *elements*, each of which are present in an arbitrary amount

One example of a chemical equation is burning meth. Methane combines with oxygen to yeild carbon dioxide and water:

```
CH4 + O2 -> CO2 + H2O
```

## What is balancing an equation?

The law of conservation of mass dictates that the quantity of each element does not change as it goes through a reaction. Nothing can be gained or lost. 

In the description of the meth burning example we have an oxygen and hydrogen imbalance: We see four H's and two O's among the reactants, and one H and three O's among the products. This is not good. We need some way of choosing how many of each molecule type we want to put into the reaction so that element quantities are preserved through the reaction. The balanced version of the meth burning equation is

```
    CH4 + 2(O2) -> CO2 + 2(H2O)
  = CH4 +  O4   -> CO2 +  H4O2
```

This is the task that this program accomplishes. 

## How does it work?

Ok. Here's the fun part. There are well-known easy algorithms for balancing chemical equations that essentially cross-multiply molecules to align element frequencies, but I think my way is a little more interesting. 

Begin with the observation that each molecule in an equation can be represented by a vector. Each attribute of this vector corresponds to the frequency of some element in its corresponding molecule. There is one attribute for each element that is involved in the entire reaction. For example:

```
        CH4 + O2 -> CO2	+ H2O    
    C   [1]  [0]    [1]   [0]
    H   [4]  [0] -> [0]   [1]
    O   [0]  [2]    [2]   [1]
```

The process of balancing equations involves assigning a multiple to each molecule that makes element frequencies equal to each other:

```
        a(CH4) + b(O2) -> c(CO2) + d(H2O)
    C     [1]      [0]      [1]       [0]
    H   a [4]  + b [0]  = c [0]  +  d [1]
    O     [0]      [2]      [2]       [1]
```

Linear combinations of vectors you say? Let's throw this stuff into some matrices.

```
      [1 0]          [1 0]
      [4 0] [a]   =  [0 1] [c]
      [0 2] [b]      [2 1] [d]
```
```
      [1 0 1 0] [a]       [0]
      [4 0 0 1] [b]    =  [0]
      [0 2 2 1] [-c]      [0]
                [-d]      [0]
         A       x     =   0
```

Systems of the form `Ax = 0` are easy to solve. Any vector that is in the nullspace of `A` will do. 

This program finds an independant basis for `nullspace(A)` via gaussian elimination. It then takes each vector and converts it back to chemical equation form. Each resulting equation will be a balanced version of the input!


# TODO

 * parse grouped molecules
 * multiply though to give positive, whole numbers
 * tex up the matrices in this readme