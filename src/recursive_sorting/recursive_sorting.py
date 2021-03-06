# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Input lists iterators
    a = 0
    b = 0
    # Output list iterator
    x = 0

    while a < len(arrA) and b < len(arrB):
        # If array A at a is less than array B at b
        if arrA[a] < arrB[b]:
            # Value of array A at a into main array
            merged_arr[x] = arrA[a]
            # Iterate a by 1
            a += 1
        else:
            # Value of array B at b into main array
            merged_arr[x] = arrB[b]
            # Interate b by 1
            b += 1
        # Iterate x by 1
        x += 1

    # Remaining values
    while a < len(arrA):
        merged_arr[x] = arrA[a]
        a += 1
        x += 1

    while b < len(arrB):
        merged_arr[x] = arrB[b]
        b += 1
        x += 1

    return merged_arr


def merge_sort(arr):
    if len(arr) > 1:
        # Mid point of the input array
        mid_point = len(arr)//2
        # Seperate the array into left and right
        left = arr[:mid_point]
        right = arr[mid_point:]

        # Call recursion
        left = merge_sort(left)
        right = merge_sort(right)

        arr = merge(left, right)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Create mid point for the end
    start2 = mid + 1

    # Return if array is already sorted
    if arr[mid] <= arr[start2]:
        return

    # Merge the sorted lists
    while start <= mid and start2 <= end:
        # If sorted iterate and continue
        if arr[start] < arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update the pointers
            start += 1
            mid += 1
            start2 += 1


def merge_sort_in_place(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out
# https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
