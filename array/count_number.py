from math import log10

n = 5438
def count_digits(n):
    num = n
    count = 0
    while num > 0:
        count += 1
        num //= 10

    return count

# alternative
def count_digits(num):
    return int(log10(num) + 1)

# TC: O(log10(n)) // O(N)
# SC: O(1)
