class CorrectPower:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.correct_power = pow(n, p)


class SolvedPolynomial:
    def __init__(self, max_power, coefficients, string):
        self.max_power = max_power
        self.coefficients = coefficients
        self.string = string

    def __str__(self):
        return self.string


class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    @property
    def max_power(self):
        return len(self.coefficients)-1

    @property
    def string(self):
        mp = self.max_power
        string = mp
        return string
