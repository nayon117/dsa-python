# check if the ith bit is set or not

def is_ith_bit_set(n, i):
    if n & (1 << i):
        return True
    else:
        return False
