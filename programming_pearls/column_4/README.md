


1-5 TODO


6. **Coffee can problem**. 

*We will intuitively prove that this process terminates by showing that for an arbitrary step, we reduce the total number of beans in the can by a finite nonzero amount. 

*Say we have `n` beans left in the can. We select two beans. There are two cases.

  *The selected beans are the same color. Then we throw them both out and insert an extra black bean. There are now `n-1` beans in the can.

  *The selected beans are different color. We return the white bean to the can and throw out the black. There are now `n-1` beans in the can. 

*As time progresses and we take tehse branches, we are forced to reduce the total number of beans in the can. So we'll always get to one or 0 beans left.

*Now it's time to think about the color of the final remaining bean. 

  *If same color white -> black gains one. If same color black -> black looses one (white gains one). If different colors -> white gains one. Hmm. If same color white -> 2 white removed. If same color black -> 0 white removed. If different colors -> 0 white removed. So the odd/even-ness of the white bean counts will always be preserved. So The last bean will be white **IFF** the starting number of white beans is odd.

7. ? I don't understand what "bracketing means"

8. 