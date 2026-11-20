# minimum bit flips to convert number

def min_bit_flips(num1, num2):
    # XOR the two numbers to find differing bits
    xor_result = num1 ^ num2
    
    # Count the number of set bits in the XOR result
    count = 0
    while xor_result:
        count += xor_result & 1  # Increment count if the least significant bit is set
        xor_result >>= 1         # Right shift to check the next bit
    
    return count
