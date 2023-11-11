import algorithm

if __name__ == '__main__':
    arr = [1, 4, 5, 2, 3, 6, 7, 8, 12, 34, 66, 100]

    res = algorithm.binary_search(arr, 7)
    print(f'#1 Binary Search - {res}')

    sort_arr = algorithm.bubble_sort(arr)
    print(f'#2 Bubble Sort - {sort_arr}')

    arr2 = [8, 4, 5, 2, 3, 7, 6, 10, 12, 34, 16, 100]
    sort_arr2 = algorithm.quick_sort(arr2)
    print(f'#3 Quick Sort - {sort_arr2}')
