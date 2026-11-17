# clear the ith bit

def clear_ith_bit(n, i):
    return n & ~(1 << i)
