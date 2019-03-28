# STRETCH: implement Linear Search
def linear_search(arr, target):
  # TO-DO: add missing code
    for arr_item in arr:
        if arr_item == target:
            return arr_item
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    while low <= high:
        middle = (low + high) // 2
        if target < arr[middle]:
            high = middle - 1
        elif target > arr[middle]:
            low = middle + 1
        else:
            return arr[middle]

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    middle = (low+high) // 2
    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if high >= low:
        # If element is present at the middle itself
        if arr[middle] == target:
            return arr[middle]

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[middle] > target:
            return binary_search_recursive(arr, target, low, middle - 1)

        # Else the element can only be present
        # in right subarray
        else:
            return binary_search_recursive(arr, target, middle + 1, high)

    else:
        # Element is not present in the array
        return -1
