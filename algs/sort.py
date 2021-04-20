def insertion_sort(array):
    # insertion sort
    n = len(array)
    for i in range(1, n, 1):
        k = array[i]
        j = i - 1
        while j >= 0 and k < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = k


def bubble_sort_v1(array):
    n = len(array)
    for i in range(0, n, 1):
        for j in range(i, n, 1):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


def bubble_sort_v2(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


def bubble_sort_v3(array):
    n = len(array)
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


array = [1, 9, 3, 4, 5, 0]
print(array)
new_array = bubble_sort_v3(array)
print(new_array)
