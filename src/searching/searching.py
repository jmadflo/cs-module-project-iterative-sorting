def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1
    while low <= high:
        midpoint = (high + low) // 2
        if target == arr[midpoint]:
            return midpoint
        elif target < arr[midpoint]:
            high = midpoint
        elif target > arr[midpoint]:
            low = midpoint

    return -1  # not found
