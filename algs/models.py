class CorrectPower:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.correct_power = pow(n, p)

class SolvedPolynomial:
    def __init__(self, max_power, coefficients, string):
        self.max_power = coefficients
        self.coefficients = coefficients
        self.string = string

    def __str__(self):
        return self.string
