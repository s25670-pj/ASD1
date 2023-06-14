import time

def shellsort(arr):
    start = time.perf_counter()
    size = len(arr)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    print("Shellsort time: %ss" % (round(time.perf_counter() - start, 8)))
