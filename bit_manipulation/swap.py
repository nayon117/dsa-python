# swap two number (bit manipulation)

def swap(a, b):
    print("Before swapping: a =", a, "b =", b)
    
    # XOR operation to swap values
    a = a ^ b
    b = a ^ b
    a = a ^ b
    
    print("After swapping: a =", a, "b =", b)
