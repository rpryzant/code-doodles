I skipped many of these problems becuase this column was about constructing test scaffolding, and included a lot of outdated questions on C testing. Not that it's not unimportant...it just doesn't align with my current coding goals.


1. The programming style is very sparse and compact. Variables are often given single-letter names, and code blocks are not seperated by any whitespace. I like this style. It'se clear, forthright, and make the underlying algorithm obvious. 

2. skipped

3. skipped

4. skipped

5. Hmm.....partial checking? Well you could do some kind of binary search type checking. Select middle element and compare to low and high. Then recurse into the top & bottom half of the array for as many iterations as desired. The whole thing could be verified in `log(n)` time. 

6. skipped

7. That's kind of cool. Essentially, the "caching" behavior that the book describes comes from this: If binary search keeps touching the same elements, then those elements will already be warmed up and ready to go in the CPU's L2 cache. This means that those array acceses will be much faster than if each access touched a random portion of the array. The author suggetss testing binary search, then, by randomly searching sections of the array. I think the real takeaway here is to ALWAYS BE COGNIZANT OF THE CPU CACHE!! Also, be aware of use cases. If you know the user is going to be mostly searching for elements in one part of an array, mabye standard binary search isn't the best thing to use.

8. skipped

9. skipped