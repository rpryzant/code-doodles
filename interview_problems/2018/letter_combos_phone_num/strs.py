

NUMS_TO_LETTERS = {
    '1': [''],
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h','i'],
    '5': ['j','k','l'],
    '6': ['m','n','o'],
    '7': ['p','q','r'],
    '8': ['t','u','v'],
    '9': ['w','x','y','z'],
    '0': [' ']
}

class LetterBuilder:
    def __init__(self):
        self.strs = ['']
    
    def add(self, d):
        tmp = []
        for c in NUMS_TO_LETTERS[d]:
            tmp += self.mass_append(c)
        self.strs = tmp

    def mass_append(self, c):
        return map(lambda x: x + c, self.strs)

def get_strs_for_num(n):
    lb = LetterBuilder()
    for digit in n:
        lb.add(digit)
    return lb.strs


print get_strs_for_num("23")
