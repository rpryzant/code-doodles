Sheldon, Leonard and Penny decide to go for drinks at Cheese Cake factory. Sheldon proposes to
 make a game out of this. Sheldon proposes as follows:

 - Decide the amount total amount to consume, say X.

 - Pick a random number N. Get N random bottles out of the possible drinks in the factory. Each
   bottle contains a certain amount of liquid, for example, if N = 5, there are 5 bottles, each
   with a (possibly) different volume of juice.

 - Look at the random sample of size N, and if there is any combination of 3 drinks that adds up
   to exactly X, accept the sample, otherwise, ditch it and try again.

 They need help with the last step. Write a function that receives an array A of size N, where
 `A[i]` is the volume of the i-th bottle of the random sample, and the value of X, and returns
 true if they should accept this sample, or false if they should ditch it.

 EXAMPLE

 If `N = 6, X = 22`, and the volumes of the bottles are `[ 1, 4, 45, 6, 10, 8 ]`, then the function
 should return true, because there is a combination of 3 bottles that adds up to 22
 (10 + 8 + 4 = 22)

 Source: Careercup