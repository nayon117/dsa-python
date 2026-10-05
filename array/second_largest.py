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

"""
Explanation in Bangla:
1. ফাংশনটি একটি অ্যারে নেয় এবং তার মধ্যে সবচেয়ে বড় এবং দ্বিতীয়তের বড়তম উপাদানটি খুঁজে বার।
2. largest-এর মান negative infinity-এর সাথে initialize করা।
3. second_largest-এর মানও negative infinity-এর সাথে initialize করা।
4. for loop-এর মধ্যে, each element of the array is compared with the current largest value.
5. If the current element is greater than the largest, the second largest is updated to the previous largest, and the largest is updated to the current element.
6. If the current element is not greater than the largest but is greater than the second largest and not equal to the largest, it updates the second largest to the current element.
7. After iterating through the list, the function checks if the second largest is still negative infinity. If it is, it means there was no second largest element, and the function returns -1. Otherwise, it returns the second largest element found.
"""
