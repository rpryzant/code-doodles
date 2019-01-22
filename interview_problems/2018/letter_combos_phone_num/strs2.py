"""
i like my old way of doing it better

"""


DIGIT_TO_LETTERS = {
    1: '',
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
    0: ' '}



def combos(digit_str):
    assert digit_str and isinstance(digit_str, type(''))
    assert digit_str.isdigit()

    out = []

    def recurse(remaining_digit_lists, partial):
        if len(remaining_digit_lists) == 1:
            for digit in remaining_digit_lists[-1]:
                out.append(''.join(partial + [digit]))
            return

        for i, list in enumerate(remaining_digit_lists):
            for j, ch in enumerate(list):
                partial.append(ch)
                recurse(remaining_digit_lists[i+1:], partial)
                partial.pop()

    recurse([DIGIT_TO_LETTERS[int(c)] for c in digit_str], [])
    return out


print combos('23')
