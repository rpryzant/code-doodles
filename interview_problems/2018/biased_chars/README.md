You are given two arrays of size N:

 `P`, which holds integers denoting a percentage
 `C`, an array of characters without duplicates

 Design and implement a system that, upon request, outputs character `C[i]` with probability `P[i]`

 The sum of every number in P is always 100. In other words, P always represents a valid
 probability distribution that covers the entire space 0 - 100.

**EXAMPLE**:
 Given:
`P = [ 15, 25, 40, 20 ]`
 `C = [ 'a', 'x', 'z', 'b' ]`

 Then `'a'` will be generated with probability 15%, `'x'` with probability 25%,
 `'z'` with probability 40%, and `'b'` with probability 20%

 Source: past interview experience