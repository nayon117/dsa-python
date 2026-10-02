"""
problem link: https://leetcode.com/problems/reverse-integer/
TC : O(N)
SC : O(1)
"""

class Solution:
    def reverse(self, x:int) -> int:
        num = x
        sign = -1 if num < 0 else 1
        num *= sign
        rev = 0

        while num > 0:
            last_digit = num % 10
            num = num // 10

            # check for overflow
            if rev > (2**31 - 1) // 10 : return 0
            rev = rev * 10 + last_digit

        return rev * sign
