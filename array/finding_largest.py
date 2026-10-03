"""
TC:O(n)
SC: O(1)
"""

class Solution:
    def largest(self, arr):
        if not arr:
            return None
        largest = arr[0]
        for num in arr:
            largest = max(largest, num)
        return largest
