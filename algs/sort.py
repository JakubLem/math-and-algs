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
    for i in range(n-1): # noqa:W0612
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


def bubble_sort_v4(array):
    n = len(array)
    for i in range(0, n, 1):
        for j in range(0, n - i - 1, 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


def heap_sort(array):
    def heap_sort_func(array, n, i):
        largest = i
        left = 2*i+1
        right = 2*i+2
        if left < n and array[left] > array[largest]:
            largest = left
        if right < n and array[right] > array[largest]:
            largest = right
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heap_sort_func(array, n, largest)
    
    for i in range(int(round(len(array)/2)), -1, -1):
        heap_sort_func(array, len(array), i)
    for i in range(len(array)-1, -1, -1):
        array[i], array[0] = array[0], array[i]
        heap_sort_func(array, i, 0)

    return array
