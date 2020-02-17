# STRETCH: implement Linear Search
def linear_search(arr, target):
    # TO-DO: add missing code
    for i in range(0, len(arr)-1):
        if arr[i] == target:
            return target, True
        else:
            return 'Target not found'


# return -1   # not found
print(linear_search([2, 5, -1, 66, 7], 2))

# STRETCH: write an iterative implementation of Binary Search


def binary_search(arr, target):

    if len(arr) == 0:
        return 'Array is empty'  # array empty

    low = 0
    high = len(arr)-1
    # TO-DO: add missing code
    while low < high:
        mid = (low + high) // 2
        if target > mid:
            low = mid + 1
        elif target < mid:
            high = mid - 1
        else:
            return mid, True

    return 'Item not in array'  # not found


print(binary_search([0, 2, 3, 4, 5, 8, 10, 13, 15, 17, 19, 22], 20))


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
