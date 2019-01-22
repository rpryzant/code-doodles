


"""

a = [w1  w2  ... wn] 


return wi : wi = w'1w'2 ...w2k and it's the biggeset



2 subproblems:
1   is a word made of other words?
2   find the largest that satisfies 1
       O(n) ==> max


BF:
   O(n^2 w)
         ^ num chars in longest word
   loop through list to see if each word is a substring
   assign as max if bigger than prev max

n log n? sorted?:
   sort arr    O(n log n)<<<<
   1st subword should be nighbor
   successive neighbors can be searched for     O(log n)
   



******linear? data structure or something smarter*********
   words come in 2 flavors
     - word
     - word made of sub words
     - garbage counts as a word

   1st pass:
     hash {word : True} 
     2nd pass:
        loop through word, ask if hashable at particular point
        try to consume whole word <<< can't really be greedy, could use some bigram fucntion to get reasonable words but w/e lets go wit htit
           thetabledownthere
              theta bled down there
              the table down there
        if consumed IN MROE THAN ONE HASH STEP, ===> multiword
     O(nw) time, O(nw) space

""" 








def longest_word(arr):
    if arr is None:
        return None

    d = {w: True for w in arr}

    def is_multiword(w):
        subwords = 0
        j = 0
        for i in range(1, len(w) + 1):
            if w[j:i] in d:
                subwords += 1
                j = i
        return True if subwords > 1 else False

    mx = 0, None
    for w in arr:
        if is_multiword(w) and len(w) > mx[0]:
            mx = len(w), w

    return mx[1]


test = ['catdogcat', 'cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']
print longest_word(test)











