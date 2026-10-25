# count occurances of a number in a sorted array
nums = [1, 2, 2, 2, 3, 4, 5]
target = 2

def count_occurrences(nums, target):
    def lower_bound(nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def upper_bound(nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

    lower = lower_bound(nums, target)
    upper = upper_bound(nums, target)
    return upper - lower
