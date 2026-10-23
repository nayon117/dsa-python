arr = [1, 2, 8, 10, 10, 12, 19]
n = len(arr)
x = 5
floor = -1 
ceil = -1
low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == x:
        floor = arr[mid]
        ceil = arr[mid]
        break
    elif arr[mid] < x:
        floor = arr[mid]
        low = mid + 1
    else:
        ceil = arr[mid]
        high = mid - 1

print("Floor:", floor)
print("Ceil:", ceil)
