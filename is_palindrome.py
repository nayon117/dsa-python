"""
problem link: https://leetcode.com/problems/palindrome-number/
TC : O(N)
SC : O(1)
"""

class Solution:
    def isPalindrom(self, x:int) -> bool:
        num = x
        rev = 0
        while num > 0:
            last_digit = num % 10
            num = num // 10
            rev = rev * 10 + last_digit

        return rev == x
