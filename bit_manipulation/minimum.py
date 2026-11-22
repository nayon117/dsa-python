# minimum bit flips to convert number

def min_bit_flips(num1, num2):
    xor_result = num1 ^ num2
    count = 0
    
    while xor_result:
        count += xor_result & 1 
        xor_result >>= 1   
    
    return count
