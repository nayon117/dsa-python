"""
TC: O(n)
SC: O(1)
"""

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def rotate_by_k_times(nums, k):
    n = len(nums)
    k = k % n
    reverse(n - k, n - 1)
    reverse(0, n - k - 1)
    reverse(0, n - 1)
