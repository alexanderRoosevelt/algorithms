# binary search O(log n)
def binary_search(arr, target):
    if len(arr) <= 0:
        return None

    arr.sort()
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Элемент найден, возвращаем его индекс
        elif mid_value < target:
            low = mid + 1  # Искомый элемент во второй половине массива
        else:
            high = mid - 1  # Искомый элемент в первой половине массива

    return -1  # Элемент не найден


# bubble sort O(n2)
def bubble_sort(arr):
    arr_size = len(arr)

    for i in range(arr_size):
        for j in range(0, arr_size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# quick sort O(n*log n)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    first_el = arr[0]
    less = [x for x in arr[1:] if x <= first_el]
    greater = [x for x in arr[1:] if x > first_el]
    return quick_sort(less) + [first_el] + quick_sort(greater)
