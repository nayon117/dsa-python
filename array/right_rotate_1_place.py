
nums = [1, 2, 3, 4, 5] 
# solution 1
"""
TC: O(n)
SC: O(1)
"""
def right_rotate_1_place(nums):
    n = len(nums)
    nums[:] = nums[-1] + nums[0:n - 1]

"""
Explanation in Bangla:
1. আমরা একটি অ্যারে নেবো।
2. আমরা শেষ উপাদানটি বাদ দিয়ে বাকি উপাদানগুলোকে একটি নতুন অ্যারেতে সংযুক্ত করব।
3. তারপর, আমরা শেষের উপাদানটির সঙ্গেও এইভাবে 1-স্থানের ডিফল্টভাবে 1-স্থানের (Right) rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানের rotationএর 1-স্থানেر 

"""
