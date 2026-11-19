# toggle the ith bit 

def toggle_ith_bit(num, i):
    # create a mask by left shifting 1 by i positions
    mask = 1 << i
    
    # toggle the ith bit using XOR operation
    return num ^ mask
