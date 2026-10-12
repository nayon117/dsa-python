nums = [5, 1, 2, 4, 5, 6]
target = 13

n = len(nums)
hash_map = {}

for i in range(0, n):
    remaining = target - nums[i]

    if remaining in hash_map:
        print ([hash_map[remaining], i])

    hash_map[nums[i]] = i
