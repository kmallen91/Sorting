# STRETCH: implement Linear Search
def linear_search(arr, target):
    # TO-DO: add missing code
    if len(arr) == 0:
        return -1
    for i in range(0, len(arr)-1):
        if arr[i] == target:
            return i
    return -1


# return -1   # not found
print(linear_search([2, 5, -1, 66, 7], 2))

# STRETCH: write an iterative implementation of Binary Search


def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty
    low = -1000
    high = len(arr)-1
    # TO-DO: add missing code
    while low < high:
        mid = (low + high) // 2
        if target > mid:
            low = mid + 1
        elif target < mid:
            high = mid - 1
        else:
            return mid

    return -1  # not found


print(binary_search([0, 2, 3, 4, 5, 8, 10, 13, 15, 17, 19, 22], 20))


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    if len(arr) == 0:
        return -1  # array empty
    middle = (low+high)//2
    # TO-DO: add missing if/else statements, recursive calls
    if target > middle:
        return binary_search_recursive(arr, target, middle+1, high)
    elif target < middle:
        return binary_search_recursive(arr, target, low, middle-1)
    elif middle == target:
        return middle
    else:
        return -1


print(binary_search_recursive([0, 3, 4, 5, 7, 9, 13, 15, 19, 22], 9, 0, 22))
