import time

def quicksort(arr, start_index, end_index):
    if start_index < end_index:
        pivot_index = partition(arr, start_index, end_index)
        quicksort(arr, start_index, pivot_index - 1)
        quicksort(arr, pivot_index + 1, end_index)


def partition(arr, start_index, end_index):
    pivot = arr[end_index]
    smaller_index = start_index
    for j in range(start_index, end_index):
        if arr[j] <= pivot:
            arr[smaller_index], arr[j] = arr[j], arr[smaller_index]
            smaller_index = smaller_index + 1
    arr[smaller_index], arr[end_index] = arr[end_index], arr[smaller_index]
    return smaller_index


def quicksortTime(arr, start_index, end_index):
    start = time.perf_counter()
    quicksort(arr, start_index, end_index)
    print("Quicksort time: %ss" % (round(time.perf_counter() - start, 8)))
