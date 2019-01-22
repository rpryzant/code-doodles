"""
this is NOT correct :((

number of 2s between 1 and n


1 bf: count up, getting 2's as you go


at each order of magnitude M, you'll get
     M-1^10 2's  (+ M-1^10 + that -1)? 

e.g. 
M = 0 ==> 0
M = 1 ==> 1
M = 2 ==> 10 + 9
M = 3 ==> 100 +               (10*10 - 10)  +  (100*1 - 10 - 9)
          ^ all the xx2s         ^all the x2x's   ^all the 2xx's
          10^{m-1} * 1    +  (10^{m-2} * 10)-10^{m-3}  + (10^{m-1} - count(m-1))
getting messy...

let's think about D = digit where we're counting 2's
D = counts per incrementation of this digit

D = 0:
    1
D = 1
    n / 10^1
D = 2
    num_chunks = n / 10^2
    num_chunks * 10^1    -   1 * num_chunks
D = 3
    num_chunks = n / 10^3
    num_chunks * 10^2    -   10 * num_chunks  -  1 * num_chunks
D = i
    num_chunks = n / 10^i  (how many stretches of this digit)
    num_chunks * 10^{i-1}  - 10^{i-2} * num_chunks - ... - 1 * num_chunks
    (elements per chunk)      (rm double counts)

sum counts from D = 1, ..., log_10(n) using  (n / (10^D)) % 10 for num of digits

"""
def 2s_per_order(digit_count, digit):
    if d == 0:
        return 1
    2s_longrun = digit_count * 10^(digit-1)
    double_counted = sum(digit_count*10^(digit-i) for i in range(0, digit-1))
    return 2s_longrun - double_counted


def get_digit(n, i):
    return (n / 10^i) % 10

def count_2s(n):
    2s_from_digit = []
    for digit in range(n, log(n, 10)):
        2s_from_digit.append(
            2s_per_order(
                get_digit(n, i), digit))

    return sum(2s_from_digit)
