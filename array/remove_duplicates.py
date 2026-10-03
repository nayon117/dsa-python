"""
TC: O(n)
SC: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n  = len(nums)
        if n == 1: return 1

        i = 0
        j = i + 1

        while j < n:
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1

        return i + 1

"""
Explanation:
1. The function removeDuplicates takes a list of integers nums as input and returns the length of the modified list after removing duplicates in-place.
2. The function first checks if the length of nums is 1. If it is, it returns 1 since there are no duplicates to remove.
3. Two pointers i and j are initialized. i points to the last unique element found, while j iterates through the list to find the next unique element.
4. The while loop continues until j reaches the end of the list. Inside the loop, if the current element nums[j] is not equal to the last unique element nums[i], it means a new unique element has been found. In that case, i is incremented, and the unique element is swapped with the element at index i.
5. Finally, the function returns i + 1, which represents the length of the modified list containing only unique elements.
"""
