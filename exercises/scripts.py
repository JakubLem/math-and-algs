# Zapisz (w postaci pseudokodu, listy kroków lub w wybranym języku programowania) algorytm
# obliczający największe pole powierzchni prostokąta, które nie jest podzielne przez p, a długości
# sąsiednich boków tego prostokąta należą do zbioru A i są różne.
# Przy ocenie brana będzie pod uwagę złożoność obliczeniowa Twojego algorytmu.
# Uwaga:
# W zapisie algorytmu możesz wykorzystywać tylko następujące operacje arytmetyczne:
# dodawanie, odejmowanie, mnożenie, dzielenie całkowite i obliczanie reszty z dzielenia. 


def zad_1_2(n, a, p):
    max_1 = -1
    max_2 = -1
    for i in range(0, n, 1):
        if a[i] % p != 0:
            if a[i] > max_1:
                if max_1 > max_2:
                    max_2 = a[i]
                else:
                    max_1 = a[i]
    if max_1 != -1 and max_2 != -1:
        return max_1*max_2
    return 0

print(zad_1_2(4, [7, 5, 11, 33 ], 3))
