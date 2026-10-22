nums = [1, 2, 4, 4, 5, 6]
target = 4

n = len(nums)
low = 0
high = n - 1
lb = n

while low <= high:
    mid = (low + high) // 2
    if nums[mid] >= target:
        lb = mid
        high = mid - 1
    else:
        low = mid + 1

print(lb)
