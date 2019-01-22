In the C standard library, rand() returns a random integer in the range [0..RAND_MAX]

 Let's assume that rand() is a very good pseudorandom generator; in particular, assume that it
 returns any number in the range [0..RAND_MAX] with equal probability P = 1/(RAND_MAX+1)

 Write a function, range_rand(l, r), that uses rand() to shrink the original range size
 by returning a random integer in the interval [l..r]. Assume l >= 0 and r <= RAND_MAX.

 What are our options? How can we do this while keeping a uniform probability distribution?
 Discuss the different approaches and their limitations.