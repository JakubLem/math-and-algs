from algs import important_algs as ia
from algs import sort as s


class Test:
    def test_test(self):
        assert True == True # noqa
        assert False == False # noqa


class TestALGS:
    def test_alg_min(self):
        assert ia.alg_min(5, 10) == 5
        assert ia.alg_min(-1, 10) == -1
        assert ia.alg_min(2, 4) == 2
        assert ia.alg_min(1, 100) == 1
        assert ia.alg_min(90, 999) == 90

    def test_alg_max(self):
        assert ia.alg_max(5, 10) == 10
        assert ia.alg_max(-1, 10) == 10
        assert ia.alg_max(2, 4) == 4
        assert ia.alg_max(1, 100) == 100
        assert ia.alg_max(90, 999) == 999

    def test_iter_nww(self):
        assert ia.iter_nww(10, 15) == 30
        assert ia.iter_nww(3, 4) == 12
        assert ia.iter_nww(15, 75) == 75
        assert ia.iter_nww(3, 6) == 6

    def test_quadratic_equation(self):
        a = 1
        b = 6
        c = 9
        assert ia.quadratic_equation(a, b, c).string == "(x-3.0)(x-3.0)"

    def test_array_min(self):
        array = [9, 2, 15, 16, 17]
        assert ia.array_min(array) == 2

        array = [190, 7, 18, 17, 20]
        assert ia.array_min(array) == 7

    def test_array_max(self):
        array = [9, 2, 15, 16, 17]
        assert ia.array_max(array) == 17

        array = [190, 7, 18, 17, 20]
        assert ia.array_max(array) == 190


class TestSort:
    def test_insertion_sort(self):
        array = [12, 11, 13, 5, 6]
        s.insertion_sort(array)
        assert array == [5, 6, 11, 12, 13]


class TestPower:
    def test_iter_power(self, correct_powers):
        for correct_power in correct_powers:
            assert ia.iter_pow(correct_power.n, correct_power.p) == correct_power.correct_power

    def test_rec_power(self, correct_powers):
        for correct_power in correct_powers:
            assert ia.rec_pow(correct_power.n, correct_power.p) == correct_power.correct_power
