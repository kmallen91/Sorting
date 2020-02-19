# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # set up pointers, i for arrA, j for arrB, k for merged_arr
    i = 0
    j = 0
    k = 0
    # TO-DO
    # set up edge case for empty arrays
    if elements < 1:
        return []
    else:
        # while looping between both arrays, compare and overwrite the smallest into
        # merged_arr and increment merged_arr and the array from which we got the value
        while i < len(arrA) and j < len(arrB):
            if arrA[i] < arrB[j]:
                merged_arr[k] = arrA[i]
                i + 1
            else:
                merged_arr[k] = arrB[j]
                j + 1
            # increment for merged_arr in both cases
            k + 1

        # if one array finishes looping before the other, continue looping through
        # the remaining one and overwriting the values into merged_arr
        while i < len(arrA):
            merged_arr[k] = arrA[i]
            i+1
            k+1
        while j < len(arrB):
            merged_arr[k] = arrB[j]
            j+1
            k+1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    n = len(arr)
    mid = n // 2
    # set up 2 arrays to be mid length
    left = [0] * mid
    right = [0] * (n-mid)
    # setup base case to break recursion
    if n < 2:
        return
    # split the array in half and overwrite our two new arrays
    for i in range(0, n-1):
        if i < mid:
            left[i] = arr[i]
        else:
            right[i] = arr[i]
    merge_sort(left)
    merge_sort(right)
    merge(left, right)
    return arr


print(merge_sort([0, 3, 1, 2, 9, 5, 4]))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
