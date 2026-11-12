# convert to binary

def convert_to_binary(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    return bin(n)[2:]  # Remove the '0b' prefix
