

class Solution:
    def isPalindrome(self, s):
        str = s
        reverse_str = str[::-1]
        return reverse_str == s

    # using recursion
    def recursion(self, s, l, r):
        if l >= r:
            return True
        if s[l] != s[r]:
            return False
        return self.recursion(s, l + 1, r - 1)
