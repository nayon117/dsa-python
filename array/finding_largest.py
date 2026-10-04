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

"""
Explanation in Bangla:
1. ফাংশনটি একটি অ্যারে নেয় এবং তার মধ্যে সবচেয়ে বড় উপাদানটি খুঁজে বার।
2. প্রথমে, অ্যারের প্রথম উপাদানটির সাথে largest-এর মান initialize করা।
3. for loop-এর মধ্যে, each element of the array is compared with the current largest value.
4. If the current element is greater than the largest, the largest is updated to the current element.
5. Finally, the function returns the largest value found.

"""
