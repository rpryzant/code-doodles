

def get_lengths(short, long, k):
    return[(long * i) + (short * (k - i)) for i in range(k+1)]
