class Solution:
    # TC: O(N)  
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

    # recursion way TC: O(2^n), SC: O(N)
    def feb(self,n):
        if n < 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
