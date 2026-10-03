"""
TC: O(n)
SC: O(1)
"""

class Solution:
    def isSorted(self, nums):
        n = len(nums)
        for i in range(0, n- 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
