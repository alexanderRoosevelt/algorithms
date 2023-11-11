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



