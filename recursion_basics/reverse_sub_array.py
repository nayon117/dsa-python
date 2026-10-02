"""
Problem: reverse a sub-array of an array using recursion.
problem link: https://www.geeksforgeeks.org/problems/reverse-sub-array5620/1
TC: O(N)
SC: O(1) if we don't consider recursion stack, otherwise O(N) due to recursion stack
"""

class Solution:
    def reverseSubArray(self, arr, start, end):
        if start >= end:
            return
        arr[start], arr[end] = arr[end], arr[start]
        self.reverseSubArray(arr, start + 1, end - 1)
