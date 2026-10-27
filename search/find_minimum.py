# find minimum in rotated sorted array 

nums = [4, 5, 6, 7, 0, 1, 2]

n = len(nums)
low, high = 0, n - 1
mini = float('inf')

while low <= high:
    mid = (low + high) // 2
    mini = min(mini, nums[mid])

    if nums[low] <= nums[mid]:
        low = mid + 1
    else:
        high = mid - 1

print(mini)
