"""
THIS ONE IS BETTER!!! BEATS A CORNER CASE


longest substring of valid parens
do i need to give locations?
   no, just length

)()())
   ==> 4

1) bf
   all substrings (2^n)

2) some kind of dp/dfs thing
   unclear how to do this

3) multiple passes?
)()())

# openings is "advantage" of opening

-1 0 -1  0 -1 -2 
)  (  )  (  )  )
2  1  2  1  2  1

1  1  1  1  1 -1


4) greedily assign matches to closest
maintain stack of opening indices
when reach opening, increment counter
when reach closing, pop opening off
   if no opening, reset counter to 0
   if you get something, match them and save matched (1's) in adjacency list
if there's nothing in the stack you're done

(  (  )  (  )  (
                ^
0  1  1  1  1  0

stack
0 -1

(  (  )  (  )  )
1  1  1  1  1  1

O(n) first pass
O(n) second pass
O(n) space (stack + adj list)


5) work on the list part

(  (  )  (  )  (

stack

when do we fall off a seq?
   finish with too many opens
       already covered, they just won't be matched
   too few closings
       stack dips under 0

so i don't think we need that adjacenct list

for c in s:
   if c is (
       if run_size = 0, remember stack size (start of run)
       add to stack
   if c is )
       if something on stack
           pop from stack, 
           if len(stack) == start size
               reset max if needed with run_size+2 (run done)
           
           run_size += 2
       else
           ctr = 0
return max


(  (  )  (  )  (
**

)  (  )  (  )  )

)  (  )  )  (  )
(  (  )  (  (  )  (
**

OBSERVATIOSN

- number of allowable parens is bounded by min(# opening, # closing)
- the longest substring, has a net advantage of 0 for the opening, when 
   viewed from __both sides__
"""

def longest_valid(s):
    assert all(c in ['(', ')'] for c in s)
    
    max_run = 0
    run_size = 0
    run_start = -1
    stack = []
    for c in s:
        if c == '(':
            if run_size == 0:
                run_start = len(stack)
            stack.append(s)
        else:
            if len(stack) == 0:
                run_size = 0
            else:
                stack.pop()
                run_size += 2
                if len(stack) == run_start:
                    max_run = max(max_run, run_size)

    return max_run



print longest_valid("(")
print longest_valid(")()")
print longest_valid(")()())")
print longest_valid("(()()(")
print longest_valid("(()(()")

