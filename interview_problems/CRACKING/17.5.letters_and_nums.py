
"""
I like my solution! less space than the book's solution, more readable, and same amount of time



 a = [a 1 1 1 a 1 a a 1 ]
      ^             ^


nd 4
nl 4




"""



def get_balanced_subsequence(a):
    
    def gbr(a, l, h, nd, nl):
        if nd == nl:
            return a[l:h+1]

        if nd < nl:
            if a[l].isalpha():
                return gbr(a, l+1, h, nd, nl-1)
            else:
                return gbr(a, l, h-1, nd, nl-1)
        else:
            if a[l].isdigit():
                return gbr(a, l+1, h, nd-1, nl)
            else:
                return gbr(a, l, h-1, nd-1, nl)
                
    return gbr(a, 0, len(a) - 1, sum(1 for x in a if x.isdigit()), sum(1 for x in a if x.isalpha()))
                


print get_balanced_subsequence('1c23dde3')

print get_balanced_subsequence('')

print get_balanced_subsequence('aaaaaa')

print get_balanced_subsequence('aa111a1')

print get_balanced_subsequence('1111aa11')

print get_balanced_subsequence('1a111aaa1a11aa111111')
