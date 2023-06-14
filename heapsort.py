import time

def max_heapify(arr, index, heap_size):
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index
    if left < heap_size and arr[largest] < arr[left]:
        largest = left
    if right < heap_size and arr[largest] < arr[right]:
        largest = right
    if index != largest:
        arr[index], arr[largest] = arr[largest], arr[index]
        max_heapify(arr, largest, heap_size)

def build_max_heap(arr, heap_size):
    for i in range(int(heap_size / 2), -1, -1):
        max_heapify(arr, i, heap_size)

def heapsort(arr, heap_size):
    start = time.perf_counter()
    build_max_heap(arr, heap_size)
    for i in range(heap_size, 0, -1):
        arr[0], arr[i-1] = arr[i-1], arr[0]
        heap_size = heap_size - 1
        max_heapify(arr, 0, heap_size)
    print("Heapsort time: %ss" % (round(time.perf_counter() - start, 8)))
