"""
problem link : https://leetcode.com/problems/armstrong-number/description/
TC: O(log n)
SC: O(1)
"""

def arm_strong(n):
    num = n
    total = n
    nod = len(str(n))

    while num > 0:
        last_digit = num % 10
        total = total + (last_digit ** nod)
        num = num // 10

    return total == n
