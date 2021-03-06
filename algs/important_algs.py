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
    if a == b:
        return a
    if a < b:
        return rec_nwd(b-a, a)
    return rec_nwd(b, a-b)
    