def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Create the index and hldr for the smallest index
        cur_index = i
        smallest_index = cur_index
        # Loop through the remaining array
        for x in range(i+1, len(arr)):
            # If the smallest index is larger than the next in line
            # then replace the next in line with smallest
            if arr[smallest_index] > arr[x]:
                smallest_index = x

        hldr = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = hldr

    return arr


def bubble_sort(arr):
    for x in range(len(arr)):
        for i in range(0, len(arr)-x-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return []
    if min(arr) < 0:
        return 'Error, negative numbers not allowed in Count Sort'
    maximum = max(arr)
    # Create array with integer values from 0 to the max
    elements = maximum + 1
    count_array = [0] * elements

    # Count occurences of each value
    for x in arr:
        count_array[x] += 1

    # Initalize loop to add sourted to the output
    i = 0
    # Interate through each value in the count_array
    for x in range(elements):
        # Count number of each value
        for y in range(count_array[x]):
            arr[i] = x
            i += 1
    return arr
