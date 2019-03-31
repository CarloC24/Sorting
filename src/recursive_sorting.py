# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(lefthalf) + len(righthalf)
    merged_arr = [0] * elements
    # TO-DO
    i = 0
    j = 0
    k = 0
     while i < len(lefthalf) and j < len(righthalf):
         if lefthalf[i] < righthalf[j]:
             merged_arr[k] = lefthalf[i]
             i = i+1
            else:
                merged_arr[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            merged_arr[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            merged_arr[k] = righthalf[j]
            j = j+1
            k = k+1
        return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        arr = merge(lefthalf, righthalf)
    return arr


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
