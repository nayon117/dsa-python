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
Explanation in Bangla:
1. ফাংশনটি একটি অ্যারে নেয় এবং তার মধ্যে ডুপ্লিকেট উপাদানগুলো মুছে ফেলে।
2. প্রথমে, অ্যারের দৈর্ঘ্য 1-এর সমান হলে, 1 return করা।
3. i-এর মান 0, j-এর মান i + 1 initialize করা।
4. while loop-এর মধ্যে, j-এর value n-এর চেয়েও ছোটতমই।
5. if condition-এ, nums[j] != nums[i] check kora।
6. If true, i increment kora, and swap the elements.
7. Finally, the function returns i + 1.
"""
