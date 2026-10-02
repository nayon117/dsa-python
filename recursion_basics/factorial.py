"""
Problem: Calculate the factorial of a number.
problem link: https://www.geeksforgeeks.org/problems/factorial5739/1
TC: O(N)
SC: O(N) due to recursion stack
"""

def fact(self, n):
    if n == 0 or n == 1:
        return 1
    return n * fact(self, n - 1)

