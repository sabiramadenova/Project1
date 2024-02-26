def bubble_sort(arr):

    new_arr = [x for x in arr]
    n = len(new_arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if new_arr[j] > new_arr[j+1]:
                new_arr[j], new_arr[j+1] = new_arr[j+1], new_arr[j]

    return arr, new_arr


def insertion_sort(arr):

    new_arr = [x for x in arr]

    for i in range(1, len(new_arr)):
        key = new_arr[i]
        j = i - 1
        while j >= 0 and key < new_arr[j]:
            new_arr[j + 1] = new_arr[j]
            j -= 1
        new_arr[j + 1] = key

    return arr, new_arr


def sort_strategy(arr, strategy):

    return strategy(arr)


array_to_sort = [2, 1, 5, 3, 4]


print("Sorted array using bubble sort:", sort_strategy(array_to_sort, bubble_sort))


print("Sorted array using insertion sort:", sort_strategy(array_to_sort, insertion_sort))
