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
    for i in range(1, p, 1):
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
    if a == 0:
        return "This equation is not quadratic!"
    
    delta = pow(b, 2)


def solve_polynomial(polynomial):






