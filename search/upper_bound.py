nums = [1, 2, 4, 4, 5, 6]
target = 4

n = len(nums)
ub = n
low = 0
high = n - 1   

while low <= high:
    mid = (low + high) // 2
    if nums[mid] > target:
        ub = mid
        high = mid - 1
    else:
        low = mid + 1

print(ub)
