
# brute 
"""
TC: O(nlogn)
SC: O(1)
"""
nums = [1, 2, 3, 4, 5]
def second_largest(nums):
    n = len(nums)
    nums.sort()
    if n < 2:
        return -1
    return nums[-2] / nums[n- 2]


# optimal
"""
TC: O(n)
SC: O(1)
"""
def getSecondOrderElements(n: int,  a: list[int]) -> list[int]:
    largest = float('-inf')
    second_largest = float('-inf')
    n = len(a)

    for i in range(n):
        if a[i] > largest:
            second_largest = largest
            largest = a[i]
        elif a[i] > second_largest and a[i] != largest:
            second_largest = a[i]

    return second_largest if second_largest != float('-inf') else -1
