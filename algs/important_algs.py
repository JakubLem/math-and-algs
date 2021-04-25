import math
from . import models # noqa:E0402


def alg_min(a, b):
    # Funkcja zwraca mniejszą liczbę
    if a < b:
        return a
    return b


def alg_max(a, b):
    # Funkcjia zwraca największą liczbę
    if a > b:
        return a
    return b


def rec_nwd(a, b):
    # Funkcja zwraca największy wspólny dzielnik
    if a == b:
        return a
    if a < b:
        return rec_nwd(b-a, a)
    return rec_nwd(b, a-b)


def iter_nww(a, b):
    # Funkcja zwraca najmniejszą wspólną wielokrotność
    if a < b:
        nww = a
    else:
        nww = b

    last = a*b
    while nww <= last:
        if nww % a == 0 and nww % b == 0:
            return nww
        nww += 1
    return last


def iter_pow(n, p):
    result = n
    for i in range(1, p, 1): # noqa
        result *= n
    return result


def rec_pow(n, p, m=None):
    if n == 1:
        return 1
    if p == 1:
        return n
    if not m:
        m = n
    return rec_pow(n*m, p-1, m)


def quadratic_equation(a, b, c):
    def get_char(n):
        if n < 0:
            return ''
        return '+'

    def get_a_char(a):
        if a == 1:
            return ''
        return str(a)

    if a == 0:
        return "This equation is not quadratic!"
    delta = pow(b, 2) - 4*a*c
    x1 = (-1*b - math.sqrt(delta))/(2*a)
    x2 = (-1*b + math.sqrt(delta))/(2*a)
    coefficients = [a, b, c]
    x1_char = get_char(x1)
    x2_char = get_char(x2)
    a_char = get_a_char(a)
    string = "{a_char}(x{x1_char}{x1})(x{x2_char}{x2})".format(a_char=a_char, x1_char=x1_char, x1=x1, x2_char=x2_char, x2=x2)
    return models.SolvedPolynomial(max_power=2, coefficients=coefficients, string=string)


def solve_polynomial(polynomial):
    return polynomial


def binary_search_v1(elem, sorted_array):
    pointer = math.floor(len(sorted_array)/2)
    if pointer == 0:
        return False
    if sorted_array[pointer] == elem:
        return True
    if elem < sorted_array[pointer]:
        return binary_search_v1(elem, sorted_array[:pointer])
    return binary_search_v1(elem, sorted_array[pointer:])


def binary_search_v2(elem, sorted_array, start=None, stop=None):
    if not start:
        start = 0
    if not stop:
        stop = len(sorted_array)
    pointer = math.floor((start + stop)/2)
    if sorted_array[pointer] == elem:
        return True
    if start == pointer:
        return False
    if elem < sorted_array[pointer]:
        return binary_search_v2(elem, sorted_array, start, pointer)
    return binary_search_v2(elem, sorted_array, pointer, stop)


def binary_search_v3(elem, sorted_array, start, stop):
    pointer = math.floor((start + stop)/2)
    if sorted_array[pointer] == elem:
        return True
    if start == pointer:
        return False
    if elem < sorted_array[pointer]:
        return binary_search_v2(elem, sorted_array, start, pointer)
    return binary_search_v2(elem, sorted_array, pointer, stop)


def array_min(array):
    n = len(array)
    minimum = array[0]
    for i in range(1, n, 1):
        if array[i] < minimum:
            minimum = array[i]
    return minimum


def array_max(array):
    n = len(array)
    maximum = array[0]
    for i in range(1, n, 1):
        if array[i] > maximum:
            maximum = array[i]
    return maximum


def is_anagram(word_1, word_2):
    if len(word_1) == len(word_2) and sorted(word_1) == sorted(word_2):
        return True
    return False


def is_palindrom(word_1, word_2):
    word_1_list = list(word_1)
    word_2_list = list(word_2)

    if len(word_1_list) != len(word_2_list):
        return False

    for i in range(len(word_1_list) - 1):
        for j in range(len(word_1_list) - 1):
            if word_1_list[j] > word_1_list[j+1]:
                temp = word_1_list[j]
                word_1_list[j] = word_1_list[j+1]
                word_1_list[j+1] = temp

    for i in range(len(word_2_list) - 1):
        for j in range(len(word_2_list) - 1):
            if word_2_list[j] > word_2_list[j+1]:
                temp = word_2_list[j]
                word_2_list[j] = word_2_list[j+1]
                word_2_list[j+1] = temp

    for i in range(len(word_1_list)):
        if word_1_list[i] != word_2_list[i]:
            return False

    return True


word_1 = "abc"
word_2 = "bca"
print(is_palindrom(word_1, word_2))

