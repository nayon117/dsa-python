from math import sqrt

def print_divisor(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result

# better solution TC: O(N/2) ~ O(N)
def print_divisor(num):
    result = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)  # num is always a divisor of itself
    return result

# optimal solution TC: O(sqrt(N))
def print_divisor(num):
    result = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)
            if i != num // i:  # To avoid printing the square root twice for perfect squares
                result.append(num // i)
    return result
