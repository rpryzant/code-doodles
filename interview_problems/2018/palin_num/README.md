palindromic number


obvious soln is to convert to string then pass that to `ispalindrome()`. Thing is, that's `O(n + n)`. Even though that boils down to `O(n)`, I'm gong to do this in just a single pass by iteratively checking digits.




TODO...NEGATIVE NUMBERS? ALLOW THEM?