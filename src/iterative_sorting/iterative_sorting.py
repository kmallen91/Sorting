# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
            # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


print(selection_sort([8, 7, 3, 4, 2]))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # loop through array
    for i in range(0, len(arr)-1):
        # set swapped as a flag
        swapped = False
        # loop through adjacent values in array
        for j in range(0, len(arr)-1):
            current_index = j
            adj_index = j+1
            # if adj < current index, swap
            if arr[adj_index] < arr[current_index]:
                arr[current_index], arr[adj_index] = arr[adj_index], arr[current_index]
                swapped = True
        # break the loop if no items are swapped
        if not swapped:
            break
    return arr


print(bubble_sort([4, 2, 9, 0, 1]))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
