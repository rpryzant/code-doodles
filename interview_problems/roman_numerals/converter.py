

d = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

a = [
    ('I', 'V', 'X'),
    ('X', 'L', 'C'),
    ('C', 'D', 'M'),
    ('M', '', '')
]

def convert_from_numerals(n):
    i = s = 0
    while i < len(n):
        if (i < len(n) - 1) and (d[n[i]] < d[n[i+1]]):
            s += d[n[i+1]] - d[n[i]]
            i += 2
        else:
            s += d[n[i]]
            i += 1
    return s


def numerals_for_digit(digit, ones, fives, tens):
    if digit < 4:
        return ones * digit
    elif digit == 4:
        return ones + fives
    elif digit < 9:
        return fives + (digit - 5) * ones
    else:
        return ones + tens

def convert_to_numerals(n):
    s = ''
    for ones, fives, tens in a:
        s = numerals_for_digit(n % 10, ones, fives, tens) + s
        n /= 10
        if n == 0:
            break
    return s

print convert_from_numerals('LII')
print convert_from_numerals('XIV')
print convert_from_numerals('XCVIII')

print convert_to_numerals(52)
print convert_to_numerals(14)
print convert_to_numerals(98)
