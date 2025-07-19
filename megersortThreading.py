



from concurrent.futures import ThreadPoolExecutor
import random

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def parralel_mergesort(arr, worker):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    with ThreadPoolExecutor(worker) as executor:

        left_sorted_future = executor.submit(parralel_mergesort, left_half, worker)
        right_sorted_future = executor.submit(parralel_mergesort, right_half, worker)

        left_sorted = left_sorted_future.result()
        right_sorted = right_sorted_future.result()

    return merge(left_sorted, right_sorted)

if __name__ == "__main__":


    arr = [random.randint(0, 100) for _ in range(10)]

    worker  = 3 

    print(arr, f"Unsorted array with {worker} workers")

    sorted_arr = parralel_mergesort(arr, worker)
    print(sorted_arr, f"Sorted array with {worker} workers")

