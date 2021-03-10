def insertion_sort(array):
    n = len(array)
    for i in range(1, n, 1):
        k = array[i]
        j = i - 1
        while j >= 0 and k < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = k


